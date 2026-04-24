#!/usr/bin/env python3
"""
Build docs/data/appendix.json from quotes.tex.

The input is the TeX narrative appendix at the repository root:

    quotes.tex

Its structure is:

    \\subsection[COUNTRY]{COUNTRY\\protect\\footnotemark}
    \\footnotetext{... country context ...}

    \\textbf{\\underline{Country YYYY}}
    \\textbf{... bold motivation paragraph ...}
    regular paragraph citing IMF staff reports ...
    regular paragraph ...
    \\textbf{Following these measures, we record ...}
    \\textbf{\\underline{Country YYYY}}
    ...

One JSON record is emitted per episode header. Fields mirror the existing
schema consumed by docs/quotes/app.js.

Inclusion flag
--------------
The authoritative inclusion rule is: `included = (tax + spend > 0)` in
`dataset.dta`. When `dataset.dta` at the repository root can be loaded with
`pandas.read_stata` (i.e. the real Stata file, not a Git LFS pointer), that
result is used. Otherwise the script falls back to TeX-based heuristics
driven by phrases the authors use systematically ("we record a narrative
fiscal action" → included; "do not classify", "do not constitute", "not
included in the narrative database", "offsetting measure" → excluded).
Ambiguous cases return None.

Re-run this script in an environment with Git LFS available (CI or a
developer workstation with `git lfs pull`) to refresh inclusion flags
against the authoritative dataset.

Usage:

    python scripts/quotes/parse_quotes_tex.py
"""
from __future__ import annotations

import json
import os
import re
import sys
from typing import Optional


COUNTRY_NAME_TO_ISO3 = {
    "ANGOLA": "AGO",
    "CÔTE D'IVOIRE": "CIV",
    "COTE D'IVOIRE": "CIV",
    "CAMEROON": "CMR",
    "CONGO, DEMOCRATIC REPUBLIC": "COD",
    "DEMOCRATIC REPUBLIC OF THE CONGO": "COD",
    "ETHIOPIA": "ETH",
    "GHANA": "GHA",
    "KENYA": "KEN",
    "MAURITIUS": "MUS",
    "MOZAMBIQUE": "MOZ",
    "NIGERIA": "NGA",
    "SENEGAL": "SEN",
    "SOUTH AFRICA": "ZAF",
    "TANZANIA": "TZA",
    "UGANDA": "UGA",
    "RWANDA": "RWA",
    "ZAMBIA": "ZMB",
}

COUNTRY_DISPLAY = {
    "AGO": "Angola",
    "CIV": "Côte d'Ivoire",
    "CMR": "Cameroon",
    "COD": "Democratic Republic of the Congo",
    "ETH": "Ethiopia",
    "GHA": "Ghana",
    "KEN": "Kenya",
    "MUS": "Mauritius",
    "MOZ": "Mozambique",
    "NGA": "Nigeria",
    "RWA": "Rwanda",
    "SEN": "Senegal",
    "TZA": "Tanzania",
    "UGA": "Uganda",
    "ZAF": "South Africa",
    "ZMB": "Zambia",
}

LFS_POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1"

SUBSECTION_RE = re.compile(
    r"^\\subsection\[[^\]]+\]\{(?P<name>[^\\}]+)\\protect\\footnotemark\}",
    re.MULTILINE,
)
FOOTNOTETEXT_RE = re.compile(r"^\\footnotetext\{", re.MULTILINE)
EPISODE_RE = re.compile(
    r"^\\textbf\{\\underline\{(?P<label>[^}]+)\}\}\s*$",
    re.MULTILINE,
)
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
IMF_REPORT_RE = re.compile(
    r"IMF (?:Staff )?Country Report (?:No\.|Report No\.)\s*(\d{2}/\d{1,4})"
    r"|IMF Country Report No\.\s*(\d{2}/\d{1,4})"
    r"|Staff Country Report No\.\s*(\d{2}/\d{1,4})"
)
SIZE_RE = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:percent|percentage\s*points?)\s*of\s*GDP",
    re.IGNORECASE,
)

INCLUDED_MARKERS = [
    "we record a narrative fiscal action",
    "record a narrative fiscal action",
    "we record a narrative",
    "record a fiscal action",
    "we thus record a narrative",
]
# Hard-exclude markers are explicit conclusions that trump any include phrase.
HARD_EXCLUDED_MARKERS = [
    "we do not classify",
    "do not classify",
    "not classified as a narrative",
    "not included in the narrative",
    "is not included in the narrative",
    "not included in the database",
    "not included as a narrative",
    "not a narrative fiscal action",
    "are not narrative fiscal actions",
    "is not a narrative",
    "no narrative fiscal action is recorded",
    "no narrative fiscal action",
    "does not reflect any discretionary",
    "does not reflect a genuine",
    "not a genuine policy",
    "should not be considered a discretionary",
    "not a discretionary fiscal",
    "do not meet the criteria",
    "do not constitute",
    "does not constitute",
    "do not make reference to any explicit fiscal consolidation",
    "fiscal measures aimed at restoring macroeconomic stability",
    "not linked to policy actions",
    "not driven by policy actions",
]
# Soft-exclude markers describe cyclical / offsetting context; they classify
# an episode as excluded only when there is no explicit include phrase.
SOFT_EXCLUDED_MARKERS = [
    "motivated by cyclical",
    "responded to cyclical",
    "responded to the cyclical",
    "responded to lower oil prices",
    "appears to have been motivated by cyclical",
    "cyclical conditions",
    "cyclical considerations",
    "was fully offset",
    "fully offset",
    "more than offset",
    "fiscal gains were offset",
    "gains were offset",
    "were offset by",
    "was offset by",
    "appears to have been offset",
    "accompanied by offsetting",
    "offsetting fiscal stimulus",
    "we consider it an offsetting",
    "we consider this an offsetting",
    "consider it an offsetting",
    "consider this an offsetting",
    "offsetting measure",
    "no net fiscal gain",
    "leaving no net",
    "fiscal slippage",
    "large fiscal slippage",
    "driven by the need to stabilize",
]
INCLUSION_CONTEXT_POSITIVE = [
    "amounting to",
    "motivated by the need to reduce",
    "motivated by the objective of reducing",
    "motivated by the desire to reduce",
    "motivated by long-term",
    "motivated by medium-term",
    "motivated by the need to ensure",
    "motivated by the objective of ensuring",
    "motivated by fiscal sustainability",
]


def strip_tex(text: str) -> str:
    t = text

    # Drop TeX comments.
    t = re.sub(r"(?m)^%.*$", "", t)

    # Remove footnotemark / protect / footnotetext contents (handled separately).
    t = re.sub(r"\\protect\\footnotemark", "", t)
    t = re.sub(r"\\footnotemark", "", t)

    # Drop \citep{...} / \citet{...} / \cite{...}.
    t = re.sub(r"\\cite[pt]?\{[^}]*\}", "", t)

    # Unwrap \textbf{X}, \underline{X}, \emph{X}, \textit{X}, \text{X}.
    macro_unwrap = re.compile(r"\\(?:textbf|underline|emph|textit|text)\{")
    while True:
        m = macro_unwrap.search(t)
        if not m:
            break
        start = m.start()
        i = m.end()
        depth = 1
        while i < len(t) and depth > 0:
            c = t[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        inner = t[m.end():i]
        t = t[:start] + inner + t[i + 1:]

    # Common escapes.
    t = t.replace("\\$", "$")
    t = t.replace("\\%", "%")
    t = t.replace("\\&", "&")
    t = t.replace("\\#", "#")
    t = t.replace("\\_", "_")
    t = t.replace("~", " ")

    # Drop TeX hard line breaks ("\\") -- the surrounding newline is kept.
    t = re.sub(r"\\\\", "", t)

    # TeX dashes: --- -> em dash, -- -> en dash (not inside hyphenated words).
    t = re.sub(r"(?<!-)---(?!-)", "—", t)
    t = re.sub(r"(?<![\w-])--(?![\w-])", "–", t)

    # TeX quote markers -> Unicode curly quotes (if any slipped through).
    t = t.replace("``", "“").replace("''", "”")

    # Strip any empty { } groups left over.
    t = re.sub(r"\{\s*\}", "", t)

    # Collapse whitespace inside paragraphs; preserve paragraph breaks.
    paragraphs = [re.sub(r"[ \t]+", " ", p).strip() for p in re.split(r"\n\s*\n", t)]
    paragraphs = [p for p in paragraphs if p]
    return "\n\n".join(paragraphs)


def parse_episode_label(label: str) -> tuple[Optional[str], Optional[int]]:
    label = label.strip()
    m = YEAR_RE.search(label)
    if not m:
        return (label, None)
    year = int(m.group(0))
    country_part = label[: m.start()].strip()
    return (country_part, year)


def detect_action_type(motivation: str) -> str:
    m = motivation.lower()
    tax = bool(re.search(r"\b(tax side|revenue side|tax-based|on the tax)\b", m))
    spend = bool(
        re.search(
            r"\b(spending side|expenditure side|spending-based|on the spending|"
            r"reduction in (?:primary )?expenditure|expenditure rationali[sz]ation)\b",
            m,
        )
    )
    if tax and spend:
        return "mixed"
    if tax:
        return "tax"
    if spend:
        return "spending"
    if re.search(r"\btax\b", m):
        return "tax"
    if re.search(r"\bspending\b|\bexpenditure\b", m):
        return "spending"
    return "unspecified"


def detect_size(motivation: str) -> Optional[float]:
    sizes = [float(x) for x in SIZE_RE.findall(motivation)]
    if not sizes:
        return None
    # Only consider the first two matches as tax+spend pieces when the
    # motivation explicitly splits; else the first value.
    if "tax" in motivation.lower() and "spending" in motivation.lower() and len(sizes) >= 2:
        return round(sizes[0] + sizes[1], 3)
    return sizes[0]


def detect_imf_reports(text: str) -> list[str]:
    found = []
    for m in IMF_REPORT_RE.finditer(text):
        for g in m.groups():
            if g:
                found.append(g)
                break
    # Preserve order, drop dups.
    seen = set()
    out = []
    for r in found:
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out


def heuristic_included(text: str, motivation: Optional[str]) -> Optional[bool]:
    lower = text.lower()
    for marker in HARD_EXCLUDED_MARKERS:
        if marker in lower:
            return False
    for marker in INCLUDED_MARKERS:
        if marker in lower:
            return True
    for marker in SOFT_EXCLUDED_MARKERS:
        if marker in lower:
            return False
    # Secondary: motivation opens with a concrete action framing and a number
    # (e.g. "A fiscal consolidation of 0.6 percent of GDP ... motivated by").
    if motivation:
        m = motivation.lower()
        starts_with_action = (
            m.startswith("a fiscal consolidation")
            or m.startswith("a revenue increase")
            or m.startswith("revenue measures with an estimated effect")
            or m.startswith("a fiscal consolidation measure")
        )
        if starts_with_action and re.search(r"\d", m):
            return True
        if any(k in m for k in INCLUSION_CONTEXT_POSITIVE):
            if re.search(r"\d", m):
                return True
    return None


def split_motivation(block_plain: str) -> tuple[Optional[str], str]:
    """First paragraph of the block, if short enough, is the motivation."""
    paras = block_plain.split("\n\n")
    if not paras:
        return None, block_plain
    first = paras[0].strip()
    rest = "\n\n".join(paras[1:]).strip()
    # Motivation paragraphs are short summaries, generally < 1200 chars.
    if first and len(first) < 1400:
        return first, rest
    return None, block_plain


def load_dataset_inclusion(path: str) -> Optional[dict[tuple[str, int], bool]]:
    """Return {(iso3, year): tax+spend>0} from dataset.dta, or None if unreachable.

    Returns None when the file is missing, is a Git LFS pointer, pandas is
    unavailable, or the Stata file cannot be parsed.
    """
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        head = f.read(len(LFS_POINTER_PREFIX))
    if head == LFS_POINTER_PREFIX:
        return None
    try:
        import pandas as pd
    except Exception:
        return None
    try:
        df = pd.read_stata(path)
    except Exception:
        return None
    cols = {c.lower(): c for c in df.columns}
    if "iso3" not in cols or "year" not in cols:
        return None
    tax_col = cols.get("tax")
    spend_col = cols.get("spend")
    total_col = cols.get("total")
    if tax_col is None or spend_col is None:
        if total_col is not None:
            tax_col = total_col
            spend_col = None
        else:
            return None
    out: dict[tuple[str, int], bool] = {}
    for _, row in df.iterrows():
        iso3 = str(row[cols["iso3"]]).strip().upper()
        try:
            year = int(row[cols["year"]])
        except Exception:
            continue
        tax = float(row[tax_col]) if row[tax_col] == row[tax_col] else 0.0
        spend = float(row[spend_col]) if spend_col and row[spend_col] == row[spend_col] else 0.0
        out[(iso3, year)] = (tax + spend) > 0
    return out


def parse_quotes(tex_path: str):
    with open(tex_path, encoding="utf-8") as f:
        tex = f.read()

    country_markers = list(SUBSECTION_RE.finditer(tex))
    if not country_markers:
        raise SystemExit("No country subsections found in quotes.tex")

    records = []
    for i, cm in enumerate(country_markers):
        country_name = cm.group("name").strip().rstrip("\\")
        iso3 = COUNTRY_NAME_TO_ISO3.get(country_name.upper())
        if iso3 is None:
            print(f"Warning: unknown country '{country_name}' - skipping", file=sys.stderr)
            continue
        display = COUNTRY_DISPLAY.get(iso3, country_name.title())

        country_start = cm.end()
        country_end = country_markers[i + 1].start() if i + 1 < len(country_markers) else len(tex)
        country_chunk = tex[country_start:country_end]

        episode_markers = list(EPISODE_RE.finditer(country_chunk))
        for j, em in enumerate(episode_markers):
            label = em.group("label")
            _, year = parse_episode_label(label)
            ep_start = em.end()
            ep_end = (
                episode_markers[j + 1].start()
                if j + 1 < len(episode_markers)
                else len(country_chunk)
            )
            block_raw = country_chunk[ep_start:ep_end]
            block_plain = strip_tex(block_raw)
            motivation, body = split_motivation(block_plain)
            if motivation is None:
                motivation_field = None
                quote_field = block_plain
            else:
                motivation_field = motivation
                quote_field = body if body else motivation

            action_type = (
                detect_action_type(motivation_field) if motivation_field else "unspecified"
            )
            size_pct = detect_size(motivation_field) if motivation_field else None
            full_text = (motivation_field or "") + "\n" + quote_field
            imf_reports = detect_imf_reports(full_text)
            imf_report_no = imf_reports[0] if imf_reports else None

            tags = []
            if action_type in {"tax", "spending", "mixed"}:
                tags.append(action_type)

            records.append({
                "episode_id": None,  # assigned below after dedup
                "country": display,
                "iso3": iso3,
                "year": year,
                "action_type": action_type,
                "size_pct_gdp": size_pct,
                "motivation": motivation_field,
                "quote": quote_field,
                "source_title": None,
                "imf_report_no": imf_report_no,
                "source_url": None,
                "page": None,
                "included": None,
                "tags": tags,
                "_full_text": full_text,
            })

    # Assign stable episode IDs: ISO3-YYYY-NAR, with -2, -3 suffixes on dups.
    seen_counts: dict[str, int] = {}
    for r in records:
        year = r.get("year")
        base = f"{r['iso3']}-{year}-NAR"
        n = seen_counts.get(base, 0) + 1
        seen_counts[base] = n
        r["episode_id"] = base if n == 1 else f"{base}-{n}"
    return records


def resolve_inclusion(records, inclusion_map):
    heuristic_count = 0
    dataset_count = 0
    unknown_count = 0
    for r in records:
        text = r.pop("_full_text")
        year = r.get("year")
        iso3 = r.get("iso3")
        decided = None
        if inclusion_map is not None and year is not None and iso3 is not None:
            if (iso3, year) in inclusion_map:
                decided = bool(inclusion_map[(iso3, year)])
                dataset_count += 1
        if decided is None:
            decided = heuristic_included(text, r.get("motivation"))
            if decided is not None:
                heuristic_count += 1
        if decided is None:
            unknown_count += 1
        r["included"] = decided
    return dataset_count, heuristic_count, unknown_count


def main() -> int:
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    tex_path = os.path.join(repo_root, "quotes.tex")
    out_path = os.path.join(repo_root, "docs", "data", "appendix.json")
    dataset_path = os.path.join(repo_root, "dataset.dta")

    records = parse_quotes(tex_path)
    inclusion_map = load_dataset_inclusion(dataset_path)
    used_dataset = inclusion_map is not None
    dataset_count, heuristic_count, unknown_count = resolve_inclusion(records, inclusion_map)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(records)} records to {out_path}")
    print(
        "Inclusion source:",
        "dataset.dta (authoritative)" if used_dataset else "TeX heuristic (dataset.dta not readable)",
    )
    print(f"  decided via dataset.dta: {dataset_count}")
    print(f"  decided via TeX heuristic: {heuristic_count}")
    print(f"  unknown (null): {unknown_count}")

    countries = sorted({r["iso3"] for r in records})
    print(f"  countries ({len(countries)}): {' '.join(countries)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

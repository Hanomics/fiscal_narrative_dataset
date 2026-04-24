# Quotes parser

`parse_quotes_tex.py` converts `quotes.tex` (the revised narrative appendix at
the repository root) into `docs/data/appendix.json`, which is the data source
for the Quotes Explorer at `docs/quotes/`.

## Usage

```sh
python scripts/quotes/parse_quotes_tex.py
```

The script only needs the standard library for parsing; `pandas` is only
required for the optional authoritative inclusion check against `dataset.dta`.

## What it does

- Parses country sections (`\subsection[...]{...\protect\footnotemark}`) and
  episode headers (`\textbf{\underline{Country YYYY}}`).
- Captures the first bold paragraph after each episode header as
  `motivation` and the rest of the block as `quote`.
- Cleans TeX markup (`\textbf`, `\underline`, `\emph`, `\citep`, common
  escapes) while preserving the author's wording.
- Extracts the first `IMF Country Report No. XX/YYY` reference as
  `imf_report_no`; leaves `source_title`, `source_url`, and `page` null to
  avoid fabricating report links or guessing a canonical page.
- Derives `action_type` (tax / spending / mixed / unspecified) and, when the
  motivation explicitly splits tax + spend sizes, `size_pct_gdp`.

## Inclusion flag

The authoritative rule is `included = (tax + spend > 0)` in `dataset.dta`.

1. **When `dataset.dta` can be loaded** (i.e. the real Stata file is present,
   not a Git LFS pointer, and `pandas` is available), the script uses it to
   decide inclusion for every `(iso3, year)` pair that matches a row in the
   dataset.
2. **When `dataset.dta` cannot be loaded** (e.g. the working copy is an LFS
   pointer because LFS was not pulled), the script falls back to text-based
   heuristics driven by phrases the authors use systematically:
   - Explicit "we record a narrative fiscal action" → included.
   - Explicit "we do not classify", "not included in the narrative",
     "no narrative fiscal action is recorded", "does not reflect a genuine",
     "do not meet the criteria", etc. → excluded.
   - "motivated by cyclical conditions", "responded to cyclical",
     "fully offset", "more than offset", "no net fiscal gain",
     "fiscal slippage" → excluded.
   - Motivation opens with "A fiscal consolidation of / amounting to ...
     motivated by ..." and a numeric size → included.
   - Otherwise `included` is left `null`.

The summary printed at the end of each run reports how many records were
decided via `dataset.dta` vs the heuristic vs left unknown. Re-run the
script any time `quotes.tex` or `dataset.dta` changes.

## Re-running against the authoritative dataset

In an environment with Git LFS available (CI or a local workstation):

```sh
git lfs pull --include="dataset.dta"
python scripts/quotes/parse_quotes_tex.py
```

This overwrites the heuristic-derived `included` values with the authoritative
ones from `dataset.dta` and reports the counts.

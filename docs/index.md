<nav style="margin-bottom:1rem;">
  <a href="./index.html">Home</a> ·
  <a href="./methods.html">Methods</a> ·
  <a href="./variables.html">Variables</a> ·
  <a href="./releases.html">Releases</a> ·
  <a href="./quotes/index.html">Quotes</a> ·
  <a href="./faq.html">FAQ</a>
</nav>

<section style="padding:1.5rem 0 0.5rem 0;">
  <h1 style="margin-bottom:0.25rem;">A Narrative Fiscal Consolidation Dataset for Sub‑Saharan Africa</h1>
  <p style="font-size:1.05rem; color:#444; max-width:46rem;">
    A transparent, narrative‑based record of discretionary fiscal consolidation
    episodes in Sub‑Saharan Africa, built from IMF staff reports and supporting
    documents. Designed for reproducible research on fiscal policy and its
    macroeconomic effects.
  </p>
  <p style="margin-top:1rem;">
    <a href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta"
       style="display:inline-block; padding:0.6rem 1.1rem; background:#1f6feb;
              color:#fff; border-radius:6px; text-decoration:none;
              font-weight:600;">
      ⬇ Download replication dataset (dataset.dta)
    </a>
    &nbsp;
    <a href="./quotes/index.html"
       style="display:inline-block; padding:0.6rem 1.1rem; background:#f3f4f6;
              color:#111; border-radius:6px; text-decoration:none;
              font-weight:600; border:1px solid #d1d5db;">
      Explore narrative quotes
    </a>
  </p>
</section>

> **Note — paper replication dataset.** This release is the paper replication
> dataset associated with the IMF working papers listed below. It is preserved
> as a fixed version so users can replicate the findings in the papers. Future
> annual updates of the narrative dataset will be released separately.

## Download the replication dataset

The authoritative replication file is `dataset.dta` at the root of the
repository. Download it directly:

- **[dataset.dta](https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta)**
  — Stata file. Load in Stata with `use dataset.dta`, in R with
  `haven::read_dta()`, or in Python with `pandas.read_stata()`.

This file is the authoritative replication dataset. Please cite this repository
(see [How to cite](#how-to-cite)) and the associated working papers when using
the data.

## Quick links

<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));
            gap:1rem; margin:1rem 0 1.5rem 0;">

  <div style="border:1px solid #e5e7eb; border-radius:8px; padding:1rem; background:#fafafa;">
    <h3 style="margin-top:0;">📦 Dataset</h3>
    <p style="margin:0 0 0.5rem 0;">Replication file <code>dataset.dta</code> used in the IMF working papers.</p>
    <a href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta">Download</a>
  </div>

  <div style="border:1px solid #e5e7eb; border-radius:8px; padding:1rem; background:#fafafa;">
    <h3 style="margin-top:0;">📄 Papers</h3>
    <p style="margin:0 0 0.5rem 0;">Construction of the dataset and an application to fiscal multipliers.</p>
    <a href="#associated-papers">See associated papers</a>
  </div>

  <div style="border:1px solid #e5e7eb; border-radius:8px; padding:1rem; background:#fafafa;">
    <h3 style="margin-top:0;">🔎 Quotes Explorer</h3>
    <p style="margin:0 0 0.5rem 0;">Browse narrative evidence by country, year, and inclusion status.</p>
    <a href="./quotes/index.html">Open explorer</a>
  </div>

  <div style="border:1px solid #e5e7eb; border-radius:8px; padding:1rem; background:#fafafa;">
    <h3 style="margin-top:0;">🛠 Methods</h3>
    <p style="margin:0 0 0.5rem 0;">Narrative identification, coding steps, and variable definitions.</p>
    <a href="./methods.html">Read methods</a>
  </div>

</div>

## Associated papers <a id="associated-papers"></a>

Two IMF working papers accompany this dataset. The first explains how the
dataset is constructed; the second is an application that uses the dataset to
estimate fiscal multipliers in Sub‑Saharan Africa. Future updates may
consolidate both into a single academic journal publication.

**A Narrative Fiscal Consolidation Dataset for Sub‑Saharan Africa**
*Construction of the dataset.*
DOI: <https://doi.org/10.5089/9798229034661.001>
PDF: [Narrative Dataset SSA.pdf](https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/Narrative%20Dataset%20SSA.pdf)

**The Fiscal Multipliers Narrative of Sub‑Saharan Africa**
*Application using the dataset.*
DOI: <https://doi.org/10.5089/9798229037792.001>
PDF: [Fiscal Multipliers Narrative of SSA.pdf](https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/Fiscal%20Multipliers%20Narrative%20of%20SSA.pdf)

## Country coverage

The replication dataset covers 16 Sub‑Saharan African countries from 1990
onwards. For each country the table lists the first and last years of coverage
and the number of consolidation episodes (years with non‑zero `tax` or `spend`).

| ISO3 | Country | First year | Last year | Episodes |
| --- | --- | --- | --- | --- |
| AGO | Angola | 1990 | 2024 | 0 |
| CIV | Côte d'Ivoire | 1990 | 2024 | 8 |
| CMR | Cameroon | 1990 | 2024 | 9 |
| COD | Democratic Republic of the Congo | 1990 | 2024 | 0 |
| ETH | Ethiopia | 1990 | 2024 | 5 |
| GHA | Ghana | 1990 | 2024 | 8 |
| KEN | Kenya | 1990 | 2024 | 6 |
| MOZ | Mozambique | 1990 | 2024 | 3 |
| MUS | Mauritius | 1990 | 2024 | 3 |
| NGA | Nigeria | 1990 | 2024 | 1 |
| RWA | Rwanda | 1990 | 2024 | 7 |
| SEN | Senegal | 1990 | 2024 | 6 |
| TZA | Tanzania | 1990 | 2024 | 9 |
| UGA | Uganda | 1990 | 2024 | 12 |
| ZAF | South Africa | 1990 | 2024 | 6 |
| ZMB | Zambia | 1990 | 2024 | 2 |

## Future annual updates

Future annual updates of the narrative dataset will be published as separate
releases. The replication file `dataset.dta` will remain unchanged so that the
findings in the two IMF working papers above can be reproduced exactly.
Release notes for updates will be posted on the [Releases](./releases.html)
page.

## How to cite

**APA**

Abdel‑Latif, H., Bechchani, K., David, A., & Lemaire, T. (2025). *A Narrative
Fiscal Consolidation Dataset for Sub‑Saharan Africa*. International Monetary
Fund Working Paper. <https://doi.org/10.5089/9798229034661.001>

**BibTeX**

```bibtex
@techreport{abdel_latif_2025_narrative_ssa,
  author      = {Abdel-Latif, Hany and Bechchani, Khalil and David, Antonio and Lemaire, Thibault},
  title       = {A Narrative Fiscal Consolidation Dataset for Sub-Saharan Africa},
  year        = {2025},
  institution = {International Monetary Fund},
  type        = {IMF Working Paper},
  doi         = {10.5089/9798229034661.001},
  url         = {https://github.com/Hanomics/fiscal_narrative_dataset}
}
```

## Further reading

- [Methods](./methods.html) — how consolidation episodes were identified.
- [Variables](./variables.html) — definitions of the dataset fields.
- [Releases](./releases.html) — release history and notes.
- [Quotes Explorer](./quotes/index.html) — browse narrative evidence.
- [FAQ](./faq.html) — frequently asked questions.

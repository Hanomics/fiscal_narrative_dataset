<nav style="margin-bottom:1rem;">
  <a href="./index.html">Home</a> ·
  <a href="./methods.html">Methods</a> ·
  <a href="./variables.html">Variables</a> ·
  <a href="./releases.html">Releases</a> ·
  <a href="./quotes/index.html">Quotes</a> ·
  <a href="./faq.html">FAQ</a>
</nav>

<style>
  .fig-grid { display:grid; gap:1rem; margin:1rem 0 1.5rem 0; }
  .fig-grid.cols-2 { grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); }
  .fig-grid.cols-4 { grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); }
  .fig-card { border:1px solid #e5e7eb; border-radius:8px; padding:1rem;
              background:#fafafa; margin:0; }
  .fig-card h4 { margin:0 0 0.35rem 0; font-size:1rem; }
  .fig-card .cap { margin:0 0 0.65rem 0; color:#444; font-size:0.95rem; }
  .fig-card .open {
    display:inline-block; padding:0.35rem 0.7rem; background:#1f6feb;
    color:#fff; border-radius:5px; text-decoration:none; font-size:0.9rem;
    font-weight:600;
  }
  .fig-card .open:hover { background:#1a5fd1; }
  .btn-primary {
    display:inline-block; padding:0.6rem 1.1rem; background:#1f6feb;
    color:#fff; border-radius:6px; text-decoration:none; font-weight:600;
  }
  .btn-secondary {
    display:inline-block; padding:0.6rem 1.1rem; background:#f3f4f6;
    color:#111; border-radius:6px; text-decoration:none; font-weight:600;
    border:1px solid #d1d5db;
  }
  .quick-grid {
    display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));
    gap:1rem; margin:1rem 0 1.5rem 0;
  }
  .quick-card {
    border:1px solid #e5e7eb; border-radius:8px; padding:1rem;
    background:#fafafa;
  }
  .quick-card h3 { margin-top:0; }
</style>

<section style="padding:1.5rem 0 0.5rem 0;">
  <h1 style="margin-bottom:0.25rem;">A Narrative Fiscal Consolidation Dataset for Sub‑Saharan Africa</h1>
  <p style="font-size:1.05rem; color:#444; max-width:46rem;">
    A transparent, narrative‑based record of discretionary fiscal consolidation
    episodes in Sub‑Saharan Africa, built from IMF staff reports and supporting
    documents. Designed for reproducible research on fiscal policy and its
    macroeconomic effects.
  </p>
  <p style="margin-top:1rem;">
    <a class="btn-primary"
       href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta">
      ⬇ Download replication dataset (dataset.dta)
    </a>
    &nbsp;
    <a class="btn-secondary" href="./quotes/index.html">
      Explore narrative quotes
    </a>
  </p>
</section>

> **Note — paper replication dataset.** This release is the paper replication
> dataset associated with the IMF working papers listed below. It is preserved
> as a fixed version so users can replicate the findings in the papers. Future
> annual updates of the narrative dataset will be released separately.

<figure class="fig-card" style="max-width:46rem;">
  <h4>Headline result — effect of a 1% of GDP fiscal consolidation on real GDP</h4>
  <p class="cap">Estimated effect of a 1 percent of GDP fiscal consolidation on real GDP.</p>
  <a class="open"
     href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_7_gdp_fc.pdf"
     target="_blank" rel="noopener">Open figure (PDF) →</a>
</figure>

## Quick links

<div class="quick-grid">

  <div class="quick-card">
    <h3>📦 Dataset</h3>
    <p style="margin:0 0 0.5rem 0;">Replication file <code>dataset.dta</code> used in the IMF working papers.</p>
    <a href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta">Download</a>
  </div>

  <div class="quick-card">
    <h3>📄 Papers</h3>
    <p style="margin:0 0 0.5rem 0;">Construction of the dataset and an application to fiscal multipliers.</p>
    <a href="#associated-papers">See associated papers</a>
  </div>

  <div class="quick-card">
    <h3>🔎 Quotes Explorer</h3>
    <p style="margin:0 0 0.5rem 0;">Browse narrative evidence by country, year, and inclusion status.</p>
    <a href="./quotes/index.html">Open explorer</a>
  </div>

  <div class="quick-card">
    <h3>🛠 Methods</h3>
    <p style="margin:0 0 0.5rem 0;">Narrative identification, coding steps, and variable definitions.</p>
    <a href="./methods.html">Read methods</a>
  </div>

</div>

## Why this dataset matters

Narrative identification isolates discretionary fiscal policy actions from
cyclically driven movements in deficits. Compared with identification based on
the cyclically adjusted primary balance (CAPB) or on forecast errors, narrative
shocks imply larger and more persistent output effects.

<figure class="fig-card" style="max-width:46rem;">
  <h4>Narrative vs. CAPB vs. forecast-error identification</h4>
  <p class="cap">Narrative shocks imply larger and more persistent output effects than CAPB or forecast-error approaches.</p>
  <a class="open"
     href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_8_narrshock_vs_CAPB_vs_consumptionFE.pdf"
     target="_blank" rel="noopener">Open figure (PDF) →</a>
</figure>

## Dataset coverage

The replication dataset covers 16 Sub‑Saharan African countries from 1990
onwards. The timeline below summarises the narrative fiscal consolidation
episodes identified for each country.

<figure class="fig-card" style="max-width:46rem;">
  <h4>Timeline of narrative fiscal consolidation episodes</h4>
  <p class="cap">Timeline of narrative fiscal consolidation episodes by country.</p>
  <a class="open"
     href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_4_timeline_episodes.pdf"
     target="_blank" rel="noopener">Open figure (PDF) →</a>
</figure>

<details>
  <summary>Country coverage table</summary>

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

</details>

## Key empirical findings

<div class="fig-grid cols-2">

  <figure class="fig-card">
    <h4>Composition matters</h4>
    <p class="cap">Spending-based consolidations are more contractionary than tax-based consolidations.</p>
    <a class="open"
       href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_10_tax_spend_fc.pdf"
       target="_blank" rel="noopener">Open figure (PDF) →</a>
  </figure>

  <figure class="fig-card">
    <h4>Timing matters</h4>
    <p class="cap">Output effects differ across booms and slumps.</p>
    <a class="open"
       href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_11_gdp_fc_nonlin_OG.pdf"
       target="_blank" rel="noopener">Open figure (PDF) →</a>
  </figure>

</div>

## External adjustment channels

Fiscal consolidation affects imports, exports, the current account balance,
and the real effective exchange rate.

<div class="fig-grid cols-4">

  <figure class="fig-card">
    <h4>Imports</h4>
    <p class="cap">Response of imports (BoP) to a fiscal consolidation.</p>
    <a class="open"
       href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_9_imports_BoP_fc.pdf"
       target="_blank" rel="noopener">Open figure (PDF) →</a>
  </figure>

  <figure class="fig-card">
    <h4>Exports</h4>
    <p class="cap">Response of exports (BoP) to a fiscal consolidation.</p>
    <a class="open"
       href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_9_exports_BoP_fc.pdf"
       target="_blank" rel="noopener">Open figure (PDF) →</a>
  </figure>

  <figure class="fig-card">
    <h4>Current account</h4>
    <p class="cap">Response of the current account balance (share of GDP).</p>
    <a class="open"
       href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_9_CABshare_BoP_fc.pdf"
       target="_blank" rel="noopener">Open figure (PDF) →</a>
  </figure>

  <figure class="fig-card">
    <h4>Real effective exchange rate</h4>
    <p class="cap">Response of the REER to a fiscal consolidation.</p>
    <a class="open"
       href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_9_REER_fc.pdf"
       target="_blank" rel="noopener">Open figure (PDF) →</a>
  </figure>

</div>

## External financing conditions matter

<figure class="fig-card" style="max-width:46rem;">
  <h4>Output effects under different ODA conditions</h4>
  <p class="cap">Output effects of fiscal consolidation differ with external financing conditions.</p>
  <a class="open"
     href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/figs/fig_12_gdp_fc_nonlin_ODA.pdf"
     target="_blank" rel="noopener">Open figure (PDF) →</a>
</figure>

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

## Download the replication dataset

The authoritative replication file is `dataset.dta` at the root of the
repository. Download it directly:

- **[dataset.dta](https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta)**
  — Stata file. Load in Stata with `use dataset.dta`, in R with
  `haven::read_dta()`, or in Python with `pandas.read_stata()`.

This file is the authoritative replication dataset. Please cite this repository
(see [How to cite](#how-to-cite)) and the associated working papers when using
the data.

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

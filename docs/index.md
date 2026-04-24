<nav style="margin-bottom:1rem;">
  <a href="./index.html">Home</a> ·
  <a href="./methods.html">Methods</a> ·
  <a href="./variables.html">Variables</a> ·
  <a href="./releases.html">Releases</a> ·
  <a href="./quotes/index.html">Quotes</a> ·
  <a href="./faq.html">FAQ</a>
</nav>

<style>
  .lede { font-size:1.05rem; color:#444; max-width:46rem; }
  .pill-grid {
    display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));
    gap:0.75rem; margin:1rem 0;
  }
  .pill {
    border:1px solid #e5e7eb; border-radius:8px; padding:0.85rem 1rem;
    background:#fafafa;
  }
  .pill h4 { margin:0 0 0.25rem 0; font-size:0.95rem; color:#111; }
  .pill p { margin:0; font-size:0.92rem; color:#444; }
  .btn-primary {
    display:inline-block; padding:0.6rem 1.1rem; background:#1f6feb;
    color:#fff; border-radius:6px; text-decoration:none; font-weight:600;
  }
  .btn-secondary {
    display:inline-block; padding:0.6rem 1.1rem; background:#f3f4f6;
    color:#111; border-radius:6px; text-decoration:none; font-weight:600;
    border:1px solid #d1d5db;
  }
  .callout {
    border-left:4px solid #1f6feb; background:#eef4ff; padding:0.85rem 1rem;
    border-radius:6px; margin:1.25rem 0;
  }
  .callout h3 { margin:0 0 0.4rem 0; font-size:1rem; color:#0b3a8c; }
  .callout ul { margin:0.4rem 0 0 1rem; padding:0; }
  .callout li { margin:0.15rem 0; color:#1f2937; }
  .quote-card {
    border:1px solid #e5e7eb; border-radius:8px; padding:0.95rem 1.1rem;
    background:#fff; margin:0.75rem 0;
  }
  .quote-card .qmeta { font-size:0.85rem; color:#555; margin:0 0 0.4rem 0; }
  .quote-card blockquote {
    margin:0; padding:0; color:#111; font-style:italic; border:0;
  }
  .fig-grid { display:grid; gap:1rem; margin:1rem 0 1.5rem 0; }
  .fig-grid.cols-2 { grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); }
  .fig-grid.cols-2x2 { grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); }
  .fig-card {
    border:1px solid #e5e7eb; border-radius:10px; padding:0.9rem;
    background:#fff; margin:0;
  }
  .fig-card img {
    display:block; width:100%; height:auto; border-radius:6px;
    border:1px solid #eef0f3;
  }
  .fig-card figcaption {
    margin:0.55rem 0.1rem 0 0.1rem; color:#444; font-size:0.95rem;
  }
</style>

<section style="padding:1.5rem 0 0.5rem 0;">
  <h1 style="margin-bottom:0.25rem;">A Narrative Fiscal Consolidation Dataset for Sub‑Saharan Africa</h1>
  <p class="lede">
    A transparent, narrative-based dataset of discretionary fiscal consolidation
    episodes in Sub-Saharan Africa, designed for policy analysis, empirical
    research, and replication.
  </p>

  <div class="pill-grid">
    <div class="pill">
      <h4>What it is</h4>
      <p>Country–year fiscal consolidation episodes identified from narrative evidence in IMF staff reports.</p>
    </div>
    <div class="pill">
      <h4>Why it matters</h4>
      <p>Isolates discretionary fiscal actions more cleanly than mechanical balance-based measures.</p>
    </div>
    <div class="pill">
      <h4>Who it is for</h4>
      <p>Researchers, policy economists, central banks, IFIs, and students of fiscal policy.</p>
    </div>
  </div>

  <p style="margin-top:1rem;">
    <a class="btn-primary"
       href="https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta">
      ⬇ Download replication dataset (.dta)
    </a>
    &nbsp;
    <a class="btn-secondary" href="./quotes/index.html">
      Open Quotes Explorer
    </a>
  </p>
</section>

<div class="callout">
  <h3>Reproducibility-first design</h3>
  <p style="margin:0;">
    This release is the fixed paper replication dataset associated with the
    IMF working papers. Future annual updates of the narrative dataset will be
    released separately and documented through versioned releases.
  </p>
  <ul>
    <li>Fixed replication dataset: <code>dataset.dta</code></li>
    <li>Transparent narrative evidence through the <a href="./quotes/index.html">Quotes Explorer</a></li>
    <li>Future annual updates kept separate from the paper replication release</li>
  </ul>
</div>

## Typical applications

- Estimate fiscal multipliers using narrative identification.
- Compare tax-based and spending-based consolidations.
- Study timing and state dependence of fiscal adjustment.
- Trace country–year episodes back to source text evidence.

## Narrative transparency

Every coded episode can be traced back to the underlying text evidence. Each
record links a country–year action to the IMF staff report that documents it,
together with the dataset’s narrative motivation summary.

<figure class="quote-card">
  <p class="qmeta"><b>Kenya · 2011</b> · Tax-side · Included · IMF Country Report No. 11/48</p>
  <blockquote>
    “A fiscal consolidation from the tax side amounting to 1.1 percent of GDP,
    driven by increases in income tax and VAT, and motivated by the objective
    of reducing the fiscal deficit and public debt and enhancing fiscal
    sustainability.”
  </blockquote>
</figure>

<p>
  <a class="btn-secondary" href="./quotes/index.html">Explore narrative evidence →</a>
</p>

## Headline result

<figure class="fig-card" style="max-width:850px;">
  <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_7_gdp_fc.png"
       alt="Estimated effect of a 1 percent of GDP fiscal consolidation on real GDP">
  <figcaption>Estimated effect of a 1 percent of GDP fiscal consolidation on real GDP.</figcaption>
</figure>

## Why narrative identification matters

Narrative identification isolates discretionary fiscal policy actions from
cyclically driven movements in deficits. Compared with identification based on
the cyclically adjusted primary balance (CAPB) or on forecast errors, narrative
shocks imply larger and more persistent output effects.

<figure class="fig-card" style="max-width:850px;">
  <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_8_narrshock_vs_CAPB_vs_consumptionFE.png"
       alt="Narrative shocks vs. CAPB vs. forecast-error identification">
  <figcaption>Narrative shocks imply larger and more persistent output effects than CAPB or forecast-error approaches.</figcaption>
</figure>

## Dataset coverage

The replication dataset covers 16 Sub-Saharan African countries from 1990
onwards. The timeline below summarises the narrative fiscal consolidation
episodes identified for each country.

<figure class="fig-card" style="max-width:850px;">
  <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_4_timeline_episodes.png"
       alt="Timeline of narrative fiscal consolidation episodes by country">
  <figcaption>Timeline of narrative fiscal consolidation episodes by country.</figcaption>
</figure>

## Key heterogeneity

<div class="fig-grid cols-2">
  <figure class="fig-card">
    <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_10_tax_spend_fc.png"
         alt="Tax-based vs. spending-based fiscal consolidation">
    <figcaption>Spending-based consolidations are more contractionary than tax-based consolidations.</figcaption>
  </figure>
  <figure class="fig-card">
    <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_11_gdp_fc_nonlin_OG.png"
         alt="Output effects across booms and slumps">
    <figcaption>Output effects differ across booms and slumps.</figcaption>
  </figure>
</div>

<details style="margin:1.25rem 0;">
  <summary><b>Additional results</b> — external adjustment channels and external financing conditions</summary>

  <p style="margin-top:0.75rem;">
    Fiscal consolidation also operates through trade and exchange-rate channels,
    and its effects depend on the availability of external financing.
  </p>

  <div class="fig-grid cols-2x2">
    <figure class="fig-card">
      <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_9_imports_BoP_fc.png"
           alt="Response of imports (BoP)">
      <figcaption>Imports (BoP).</figcaption>
    </figure>
    <figure class="fig-card">
      <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_9_exports_BoP_fc.png"
           alt="Response of exports (BoP)">
      <figcaption>Exports (BoP).</figcaption>
    </figure>
    <figure class="fig-card">
      <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_9_CABshare_BoP_fc.png"
           alt="Response of the current account balance">
      <figcaption>Current account balance (share of GDP).</figcaption>
    </figure>
    <figure class="fig-card">
      <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_9_REER_fc.png"
           alt="Response of the real effective exchange rate">
      <figcaption>Real effective exchange rate.</figcaption>
    </figure>
  </div>

  <figure class="fig-card" style="max-width:850px;">
    <img src="https://raw.githubusercontent.com/Hanomics/fiscal_narrative_dataset/main/figs/fig_12_gdp_fc_nonlin_ODA.png"
         alt="Output effects under different ODA conditions">
    <figcaption>Output effects of fiscal consolidation differ with external financing conditions.</figcaption>
  </figure>
</details>

## Associated papers

The first paper documents the construction of the dataset. The second paper
applies the dataset to estimate fiscal multipliers in Sub-Saharan Africa.

- **A Narrative Fiscal Consolidation Dataset for Sub-Saharan Africa**
  &nbsp;—&nbsp;
  <a href="https://doi.org/10.5089/9798229034661.001" target="_blank" rel="noopener">DOI: 10.5089/9798229034661.001</a>
- **The Fiscal Multipliers Narrative of Sub-Saharan Africa**
  &nbsp;—&nbsp;
  <a href="https://doi.org/10.5089/9798229037792.001" target="_blank" rel="noopener">DOI: 10.5089/9798229037792.001</a>

## Get started in 60 seconds

Direct download:
**[dataset.dta](https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta)**

```r
# R
library(haven)
df <- read_dta("https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta")
```

```python
# Python
import pandas as pd
df = pd.read_stata("https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta")
```

<details>
  <summary>View country coverage table</summary>

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

## How to cite

**APA**

Abdel-Latif, H., Bechchani, K., David, A., & Lemaire, T. (2025). *A Narrative
Fiscal Consolidation Dataset for Sub-Saharan Africa*. International Monetary
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

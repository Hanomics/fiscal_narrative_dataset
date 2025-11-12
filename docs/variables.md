<nav style="margin-bottom:1rem;">
  <a href="./index.html">Home</a> ·
  <a href="./methods.html">Methods</a> ·
  <a href="./variables.html">Variables</a> ·
  <a href="./releases.html">Releases</a> ·
  <a href="./faq.html">FAQ</a>
</nav>

# Variables

This page describes the variables included in the narrative fiscal consolidation dataset.  The table below corresponds to the machine‑readable schema in `data/schema/dataset_schema.json` and the variable dictionary in `data/metadata/variables.md`.

| Variable | Type | Description |
| --- | --- | --- |
| **country** | string | Country name in English. |
| **iso3** | string | ISO 3166‑1 alpha‑3 country code. |
| **year** | integer | Calendar year of the fiscal consolidation episode. |
| **tax** | number | Size of tax‑based consolidation in percent of GDP.  Positive values indicate fiscal tightening; zero indicates no action. |
| **spend** | number | Size of spending‑based consolidation in percent of GDP.  Positive values indicate fiscal tightening; zero indicates no action. |
| **total** | number | Sum of **tax** and **spend**, representing the overall size of the consolidation effort in percent of GDP. |

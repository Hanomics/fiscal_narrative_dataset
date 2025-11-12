# Data Release v2025.11

This folder contains the immutable data files for the `v2025.11` release of the narrative fiscal consolidation dataset.

## Files

* `narrative_shocks.csv` – the dataset in comma‑separated format.
* `narrative_shocks.dta` – the same dataset in Stata format.  Use `read.dta()` (R) or `pandas.read_stata()` (Python) to import.
* `narrative_shocks.xlsx` – the original Excel file used to construct this release.
* `README.md` – this file.

## Contents

The dataset contains annual series of narrative fiscal consolidations for 17 Sub‑Saharan African countries (1990–2024).  Each row corresponds to a country and year, with the size of tax‑based and spending‑based consolidation measured in percent of GDP.  A zero indicates no consolidation in that year.  See the main README and the documentation site for more details.

## Citation

Please cite the dataset as:

> Researcher, Sample (2025).  *Fiscal Consolidation Narrative Shocks for Sub‑Saharan Africa* (v2025.11).  DOI: 10.1234/ssa.fiscal.consolidation.2025.11

# Variable Dictionary

This document describes the variables included in the narrative fiscal consolidation dataset.

| Variable | Type | Description |
| --- | --- | --- |
| `country` | string | Country name in English. |
| `iso3` | string | ISO 3166‑1 alpha‑3 country code. |
| `year` | integer | Calendar year of the fiscal consolidation episode. |
| `tax` | number | Size of tax‑based consolidation in percent of GDP.  Positive values indicate fiscal tightening; zero indicates no action. |
| `spend` | number | Size of spending‑based consolidation in percent of GDP.  Positive values indicate fiscal tightening; zero indicates no action. |
| `total` | number | Sum of `tax` and `spend`, representing the total size of the consolidation episode in percent of GDP. |

If a country does not experience a narrative fiscal consolidation episode in a given year, the `tax`, `spend`, and `total` columns will be zero.

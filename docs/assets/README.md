# Site assets

This folder holds static images used by the documentation site (e.g. figures
from the IMF working papers). Figures are not yet uploaded — the list below is
a placeholder describing the visuals to add, with the filenames the landing
page and other doc pages will expect.

## Recommended visuals to upload

When ready, export these as PNG (ideally 1200–1600 px wide, < 400 KB each) and
place them in this folder using the filenames below. Source figures should be
drawn from the two IMF working papers at the repository root:

- `Narrative Dataset SSA.pdf`
- `Fiscal Multipliers Narrative of SSA.pdf`

| Filename | Content | Likely source |
| --- | --- | --- |
| `coverage_map.png` | Country coverage map or coverage table for the SSA sample. | Narrative Dataset SSA |
| `episodes_over_time.png` | Distribution of consolidation episodes over time. | Narrative Dataset SSA |
| `tax_vs_spending_composition.png` | Tax vs spending consolidation composition across the sample. | Narrative Dataset SSA |
| `avg_size_by_country.png` | Average size of consolidation by country (percent of GDP). | Narrative Dataset SSA |
| `multiplier_irf.png` | Fiscal multiplier impulse response figure. | Fiscal Multipliers Narrative of SSA |
| `multiplier_tax_vs_spend.png` | Tax vs spending multiplier comparison. | Fiscal Multipliers Narrative of SSA |

## Notes

- Do not commit low‑resolution screenshots or images with embedded
  copyrighted material that cannot be redistributed.
- Reference each image in the docs with a relative path, e.g.
  `![Coverage map](./assets/coverage_map.png)` from `docs/index.md`.
- When adding or replacing a figure, keep the filename stable so existing
  references in the docs continue to work.

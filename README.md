# A Narrative Fiscal Consolidation Dataset for Sub‑Saharan Africa

Welcome to the repository of the **Narrative Fiscal Consolidation Dataset** for
Sub‑Saharan Africa (SSA). It provides a longitudinal, narrative‑based record
of discretionary fiscal consolidation episodes for a group of SSA countries,
built from IMF staff reports and supporting documents, together with the two
IMF working papers that accompany the data.

Documentation site: <https://hanomics.github.io/fiscal_narrative_dataset/>

## Paper replication dataset

The authoritative file for replicating the findings in the two IMF working
papers below is `dataset.dta` at the root of this repository. It is preserved
as a fixed version. Future annual updates of the narrative dataset will be
released separately so that published results remain reproducible.

Direct download:
<https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta>

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

```stata
* Stata
use "https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/dataset.dta", clear
```

## Associated papers

The two IMF working papers that accompany the dataset are included at the root
of this repository.

- **A Narrative Fiscal Consolidation Dataset for Sub‑Saharan Africa** —
  construction of the dataset.
  DOI: <https://doi.org/10.5089/9798229034661.001>
  PDF: [Narrative Dataset SSA.pdf](https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/Narrative%20Dataset%20SSA.pdf)

- **The Fiscal Multipliers Narrative of Sub‑Saharan Africa** — an application
  using the dataset.
  DOI: <https://doi.org/10.5089/9798229037792.001>
  PDF: [Fiscal Multipliers Narrative of SSA.pdf](https://github.com/Hanomics/fiscal_narrative_dataset/raw/main/Fiscal%20Multipliers%20Narrative%20of%20SSA.pdf)

Future updates may consolidate both papers into a single academic journal
publication.

## Repository contents

- `dataset.dta` — authoritative paper replication dataset.
- `Narrative Dataset SSA.pdf`, `Fiscal Multipliers Narrative of SSA.pdf` —
  the two IMF working papers.
- `docs/` — documentation site (served at the link above) with methods,
  variables, releases, FAQ, and the Quotes Explorer.
- `paper/` — working‑paper materials, including the narrative appendix with
  the text excerpts used to identify episodes.
- `governance/` — governance documents, including a roadmap for future country
  expansions and guidelines for submitting new episodes.
- `scripts/` — small utilities to validate the dataset and build the site.

## Citation

If you use the dataset in your research, please cite this repository and the
associated working paper using the information in `CITATION.cff`.

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

## Contributing

We welcome feedback and contributions. Please open an issue or pull request to
report errors, suggest improvements, or propose new episodes. See
`CONTRIBUTING.md` for more details and `governance/submission_guide.md` for
guidance on proposing new episodes.

## License

The dataset and documentation are released under the Creative Commons
Attribution 4.0 International (CC BY 4.0) license. The code in this repository
is available under the MIT license. See `LICENSE` for details.

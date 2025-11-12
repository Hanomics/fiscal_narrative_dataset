# Fiscal Consolidation Narrative Shocks for Sub‑Saharan Africa

Welcome to the **Fiscal Consolidation Narrative Shocks** repository for Sub‑Saharan Africa (SSA).  This repository contains a longitudinal dataset of narrative fiscal consolidation episodes for a group of African countries, along with supporting documentation, a working paper appendix, and a simple documentation site.

The goal of this project is to provide a transparent and reproducible record of annual, narrative‑based fiscal consolidation actions for each country in the sample.  Researchers can explore the underlying text excerpts and download the structured data in multiple formats.

## What you will find here

* **Data files** under `data/` with annual series of tax and spending consolidation actions (`tax`, `spend`, `total`) for each country and year.  The `versions/` subdirectory contains immutable, versioned releases (e.g. `v2025.11`), while `current/` points to the most recent release for convenience.
* **Documentation** in `docs/` which powers a GitHub Pages site.  The site provides a coverage table, a variable dictionary, methodological notes, and release notes.
* **Working paper materials** in `paper/`.  The `appendix/` folder includes the narrative appendix with the text excerpts used to identify episodes.
* **Governance documents** in `governance/`, including a roadmap for future country expansions and guidelines for submitting new episodes.
* **Scripts** in `scripts/` to validate the dataset and build the documentation site.  These scripts are minimal at first but can be extended as the project grows.

## Quick start

1. Clone this repository:

   ```sh
   git clone https://github.com/yourusername/fiscal-consolidation-ssa.git
   cd fiscal-consolidation-ssa
   ```

2. Download the latest dataset in CSV format from `data/current/narrative_shocks.csv` or via the raw URL:

   ```r
   # R example
   shocks <- read.csv("https://raw.githubusercontent.com/yourusername/fiscal-consolidation-ssa/main/data/current/narrative_shocks.csv")
   ```

3. Visit the documentation site at <https://yourusername.github.io/fiscal-consolidation-ssa/> to browse the variable dictionary, country coverage table, and frequently asked questions.

## Citation

If you use this dataset or site in your research, please cite the accompanying working paper and the dataset release using the citation information in `CITATION.cff`.  You can also cite the data release DOI directly once it has been minted.

## Contributing

We welcome feedback and contributions.  Please open an issue or pull request to report errors, suggest improvements, or propose new episodes.  See `CONTRIBUTING.md` for more details on how to contribute and `governance/submission_guide.md` for guidance on proposing new episodes.

## License

The dataset and documentation are released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.  The code in this repository is available under the MIT license.  See `LICENSE` for details.

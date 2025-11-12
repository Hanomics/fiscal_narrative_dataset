# Submission Guide for New Episodes

We welcome contributions of new narrative fiscal consolidation episodes or additional countries.  To ensure consistency and transparency, please follow these steps when preparing your submission:

1. **Check the roadmap** – Make sure the country or episode you intend to submit is not already planned or under review.  See `roadmap.md` for current plans.
2. **Gather sources** – Collect primary documents such as budget speeches, policy statements, or IMF reports that clearly indicate a planned discretionary fiscal consolidation.  Record bibliographic details (title, date, URL if available).
3. **Code the episode** – Using the methodology described in the working paper, determine whether the consolidation is tax‑based, spending‑based, or mixed.  Estimate the size of the consolidation in percent of GDP using the available projections.
4. **Update data files** – Add your episode to a new row in the `data/` CSV following the schema.  If there are multiple measures in the same year, aggregate them.
5. **Provide narrative excerpts** – Extract the relevant text supporting the episode and include it in the appendix (e.g., in `paper/appendix/`).  Indicate the source and page number.
6. **Run validation** – Execute the validation script (`scripts/validate_data/validate_dataset.py`) to ensure your contribution complies with the schema and contains no duplicates.
7. **Document your changes** – Update `CHANGELOG.md` and add notes in `docs/releases.md` if applicable.
8. **Open a pull request** – Describe your contribution, include citations to sources, and tag relevant maintainers.  Pull requests without sufficient documentation may be delayed.

Thank you for helping to improve the coverage and quality of the Fiscal Consolidation SSA dataset!

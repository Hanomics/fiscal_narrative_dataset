# Contributing to the Fiscal Consolidation SSA Project

Thank you for your interest in contributing!  We welcome pull requests,
issues, and suggestions that improve the dataset, documentation, or site.  This
file describes how to get started and what to expect when contributing.

## Reporting issues

If you find an error in the dataset, documentation, or scripts, please open
an issue.  Clearly describe the problem and, if possible, include a minimal
example or a link to the relevant part of the data or docs.

## Proposing new episodes or countries

We encourage researchers to propose new narrative fiscal consolidation
episodes or to contribute data for additional countries.  Before submitting a
pull request, please read `governance/submission_guide.md` and follow the
outlined process.  In summary:

1. **Check the roadmap** in `governance/roadmap.md` to see whether your
   proposed country or episode is already planned or under review.
2. **Fork this repository** and create a new branch for your contribution.
3. **Add your data** following the schema in `data/schema/` and update any
   relevant metadata files.  Run the validation script in `scripts/validate_data/`
   to ensure your contribution is consistent with the existing data.
4. **Document your changes** in `CHANGELOG.md` and add release notes if
   necessary.
5. **Open a pull request** describing what you have done, citing sources,
   and referencing the issue (if applicable).  Use the pull request
   checklist in `.github/PULL_REQUEST_TEMPLATE.md` to ensure you have
   completed all steps.

## Coding standards

* Keep scripts simple and readable.  Use Python for data validation and
  documentation building scripts.  Place helper scripts in `scripts/`.
* Document any nontrivial code with comments and docstrings.
* Do not commit large binary files (other than data releases) to the
  repository.  Use git‑annex or provide links to external storage if
  necessary.

## Pull request review process

All pull requests are reviewed by maintainers and, where relevant, by
subject‑matter experts.  Reviews check for adherence to the schema,
accuracy of the data and documentation, and readability of code.  The
maintainers may request changes or additional information before merging.

Thank you for helping to build a reliable and useful resource!

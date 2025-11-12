# Review Process for New Contributions

To maintain the integrity and reliability of the Fiscal Consolidation SSA dataset, all proposed additions undergo a light peer‑review process.  The review has two objectives: (i) verify that the proposed episode follows the narrative identification methodology, and (ii) ensure the data are correctly formatted and documented.

## Stages of review

1. **Initial screening** – When a pull request is submitted, a maintainer performs a quick check for completeness (data, sources, documentation).  Incomplete submissions are returned to the contributor with a request for more information.
2. **Methodological review** – A subject‑matter expert reviews the narrative excerpts and the coding of the episode(s).  The reviewer may request clarification or additional sources.  If the episode does not meet the criteria for a discretionary consolidation, it is rejected.
3. **Data validation** – The maintainer runs the validation script and manually inspects the diff to ensure there are no unintended changes to other countries or years.
4. **Approval and merge** – Once the methodological review and validation are complete, the contribution is approved and merged into the main branch.  The contributor is credited in the release notes.

## Roles

* **Maintainer** – Coordinates the review process, checks technical and formatting issues, and merges approved contributions.
* **Reviewer** – A researcher with expertise in fiscal policy who evaluates the narrative evidence and coding decisions.
* **Contributor** – The individual proposing the new episode or country.

## Timeline

We aim to complete the review process within two weeks of submission.  Complex contributions may require additional time.

# Frequently Asked Questions

### What is a narrative fiscal consolidation?

A narrative fiscal consolidation is an instance of planned discretionary fiscal tightening identified through historical narratives such as budget speeches, policy statements, and IMF reports.  Unlike mechanical measures that rely purely on fiscal outturns, the narrative approach aims to isolate policy decisions that are not driven by contemporaneous economic conditions.

### Which countries are included?

The initial release includes 14 Sub‑Saharan African countries.  See the country coverage table on the [home page](index.md) for details.  We plan to expand to additional countries in future releases; see the roadmap in `governance/roadmap.md`.

### How are the sizes of consolidation episodes measured?

The `tax` and `spend` variables record the projected fiscal impact of the announced measures, expressed as a percentage of GDP.  These projections are taken from official documents (budget reports, medium‑term frameworks) or IMF staff reports.  The `total` variable is the sum of `tax` and `spend`.

### Can I download the data programmatically?

Yes.  You can use the raw file URL on GitHub to fetch the latest CSV.  For example, in Python:

```python
import pandas as pd
url = "https://raw.githubusercontent.com/yourusername/fiscal-consolidation-ssa/main/data/current/narrative_shocks.csv"
df = pd.read_csv(url)
```

You can also fetch specific releases by replacing `main` with the tag (e.g., `v2025.11`).

### How can I contribute a new country or episode?

Please read `CONTRIBUTING.md` and `governance/submission_guide.md` before submitting data.  In short, you should fork the repository, add your data following the schema, document your sources, and open a pull request.  We welcome contributions that adhere to the narrative identification methodology.

### Who maintains this project?

The project is maintained by a small team of researchers.  Contact information is available in `SECURITY.md` and the repository description.

<nav class="nav">
  <a href="../index.html">Home</a>
  <a href="../methods.html">Methods</a>
  <a href="../variables.html">Variables</a>
  <a href="../releases.html">Releases</a>
  <a href="../quotes/index.html">Quotes</a>
  <a href="../faq.html">FAQ</a>
</nav>

# Methods

## Narrative identification strategy

The narrative fiscal consolidation dataset follows the methodology pioneered by David and Leigh (2018) and extended to developing economies. The key idea is to identify episodes of discretionary fiscal tightening using narrative sources—such as budget speeches, parliamentary reports, and policy statements—rather than mechanical changes in deficit or debt ratios. This approach aims to isolate policy decisions that are exogenous to the contemporaneous economic cycle. In our dataset we rely mainly on IMF staff reports since 1990s. 

For each country and year we consult IMF staff reports to determine whether the government announced a multi‑year fiscal consolidation plan.  We classify the consolidation as **tax‑based** if it primarily relies on revenue increases (e.g. higher VAT, income taxes), **spending‑based** if it relies on expenditure cuts (e.g. wage bill reductions, subsidy reforms), or **mixed** when both channels are present.  The size of the consolidation is measured in percent of GDP, based on official projections at the time of announcement.

The narrative identification proceeds in three steps:

1. **Collection of sources** – IMF reports are gathered for each country since 1990s. 
2. **Coding of episodes** – manual extraction along with AI assisted approach to review IMF staff reports and extract instances of planned discretionary fiscal tightening, noting the announced measures, their motivations, and the projected fiscal impact.
3. **Cross‑checking** – extracted episodes are cross‑validated with secondary literature and, where available, macroeconomic data to ensure consistency and to avoid misclassifying cyclical adjustments as discretionary consolidations.

## Measurement of variables

* `tax` is the projected increase in revenue, expressed as a percentage of GDP, associated with the consolidation episode.  When multiple tax measures are announced in the same year, we aggregate them.
* `spend` is the projected reduction in expenditure, expressed as a percentage of GDP.  This includes cuts in current spending as well as reductions in investment or subsidies.
* `total` is simply the sum of `tax` and `spend` and represents the overall size of the fiscal consolidation effort.

If no narrative consolidation is identified in a given year, the `tax`, `spend`, and `total` values are recorded as zero.

## Limitations

While the narrative approach helps to isolate discretionary policy actions, users should be aware of several limitations:

* **Source availability** – for some countries and early years, IMF staff reports might not be available. 
* **Projection vs. realization** – the dataset records announced measures and their projected impact, while trying to trace ex‑post realization. However, actual fiscal outcomes may partially differ due to implementation delays or macroeconomic shocks.

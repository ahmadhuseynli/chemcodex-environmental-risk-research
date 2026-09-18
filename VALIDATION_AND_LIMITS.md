# Validation and limits

## Current status

This project contains a mature prototype history, but **not one validated production engine**.

The strongest architecture exists across several artifacts: workbooks, parser code, browser logic, an ERA workbook and later extraction experiments.

The public repository therefore separates:

- what was built;
- what was learned;
- what is currently defensible;
- what still requires validation.

## Historical rules that should not be treated as final

Several older implementations used shortcuts that are useful as development history but should not be carried into a production engine without revalidation.

Examples include:

- treating a regulatory-list match as automatic proof that no further assessment is needed;
- fixed PBT/bioaccumulation mixture triggers presented too broadly;
- converting BOD/COD relationships directly into persistence half-lives;
- generic species weighting in toxicity units;
- generic M-factor tables detached from substance-specific classifications;
- fixed PNEC assessment factors applied to every case;
- universal default PEC or dilution values;
- simplified sediment partition/deposition assumptions.

These are precisely the kinds of rules that a provenance-first system should expose rather than bury.

## Technical corrections from the recovered audit

Several quantitative details are important enough to state explicitly.

### Bioaccumulation

Some historical workbook/SOP versions used **BCF 1,000** as a bioaccumulation trigger and **BCF 5,000** as very bioaccumulative.

For REACH Annex XIII, the formal BCF thresholds are:

- **B: BCF > 2,000**
- **vB: BCF > 5,000**

Historical logKow thresholds around 4 and 5 are useful as screening/supporting information, but they should not be presented as final REACH B/vB criteria.

### M-factors

Historical workbooks contained generic M-factor logic.

Under CLP, M-factors are substance-specific multipliers for substances classified **Aquatic Acute 1 and/or Aquatic Chronic 1** and are used in mixture summation. They are not a universal generic multiplier table.

### Species weighting

The later JavaScript engine used experimental species multipliers, including algae weight 2 and daphnia weight 1.5.

No primary source was recovered that supports those factors as generic regulatory multipliers. They remain historical project heuristics.

### Historical PNEC / PEC defaults

The late risk workbook and 2026 deterministic experiment used fixed screening parameters in some branches.

Recovered examples include:

- screening dilution factors such as **100 / 500 / 1,000**;
- an additional regional-water step equivalent to a further **10-fold reduction**;
- fixed **AF = 1,000** for recognised acute endpoints in the 2026 experiment;
- fixed **AF = 100** for recognised chronic endpoints;
- universal experimental **default PEC = 0.05 mg/L**.

These values describe historical prototypes. They are not universal regulatory constants.

Assessment factors should depend on the available ecotoxicity dataset and the applicable method. PEC parameters should come from the release scenario, receiving environment and justified fate/mixing assumptions.

## Failed branches retained in the record

The project also has genuine failures:

- early logic sometimes mixed source concentration with environmental risk;
- some screening calculations risked double-counting dilution;
- the first ML branch had no useful label structure;
- some parser versions contained product-specific debugging fallbacks;
- pseudo-OCNS logic changed repeatedly;
- the recovered webtool is incomplete as a standalone deployment;
- a later deterministic risk function was only an experiment and was not integrated into the archived application.

## Sediment limitation

The project correctly identified sediment as a separate exposure pathway, but the recovered sediment calculations were exploratory.

A defensible future module should document:

- Kd/Koc or other partitioning basis;
- deposition/fate assumptions;
- sediment mixing depth;
- sediment density;
- bioavailability;
- water-sediment linkage.

A fixed geometry or partition shortcut should not be treated as a generic sediment-risk model.

## Validation needed before operational use

A credible next version needs:

- a curated benchmark set with manually reviewed SDS/component data;
- version-locked regulatory rules;
- unit tests for every deterministic calculation;
- independent ecotoxicology review;
- mixture and metals/inorganic edge cases;
- PLONOR/HOCNF and other regulatory routing cases;
- marine/freshwater endpoint tests;
- PNEC derivation validation;
- exposure-scenario validation;
- comparison with independently completed professional environmental risk assessments.

The extraction layer should be tested separately for:

- product/component identity recall;
- CAS accuracy;
- H-code recall;
- endpoint type/species/duration extraction;
- unit conversion;
- concentration-range parsing;
- component attribution;
- missing-data fidelity;
- hallucination rate.

The hazard/effect layer should be tested for:

- threshold and rule correctness;
- whole-mixture versus component evidence;
- metals/inorganics;
- regulatory routing;
- evidence reliability;
- data-gap handling;
- PNEC endpoint selection and assessment-factor justification.

The exposure layer should be tested for:

- mass balance;
- unit integrity;
- scenario parameters;
- dilution/fate assumptions;
- sediment pathways;
- sensitivity to uncertain inputs.

The risk engine should then be tested on benchmark cases with independently completed ERA outputs so parser error is not confused with calculation error.

## Regulatory position

The public code is for research and demonstration. It is not an official OSPAR, ECHA, GESAMP or competent-authority implementation.

For real regulatory work, the applicable current legislation, guidance, national requirements and specialist judgement govern.

For the detailed parameter-by-parameter audit, see TECHNICAL_AUDIT.md.

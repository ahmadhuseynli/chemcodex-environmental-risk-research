# Technical audit and scientific basis

This page records the most important scientific and technical conclusions from the recovered ChemCodex project history.

It separates **what historical prototypes actually implemented** from **what should be carried forward into a defensible engine**.

## 1. Toxicity and endpoint selection

The early workbook generations used internal acute and chronic concentration bands to turn raw aquatic endpoints into readable categories. Those bands were useful for consistency, but they are not a substitute for the full GESAMP Hazard Evaluation Procedure or for a PNEC derivation.

A later JavaScript engine improved this part of the design by ranking endpoint evidence according to reliability and by preserving species/category information instead of simply taking the numerically smallest value.

The recovered implementation also contained project-specific species multipliers - algae weight 2 and daphnia weight 1.5. No primary source was found that supports those multipliers as generic regulatory factors, so they should remain historical experimental logic rather than production rules.

## 2. Bioaccumulation, persistence and PBT/vPvB

Historical ChemCodex versions used BCF and logKow categories to flag increasing concern.

The current audit distinguishes that screening logic from formal REACH Annex XIII criteria:

- the historical workbook sometimes used BCF 1,000 as a "bioaccumulative" trigger;
- REACH Annex XIII uses **BCF >2,000 for B** and **BCF >5,000 for vB**;
- logKow can be useful screening/supporting evidence, but it should not be presented as the final regulatory B/vB determination.

Persistence requires the same discipline. Some workbook generations tried to infer persistence from biodegradation or BOD/COD relationships. Those are useful exploratory signals, but they are not replacements for compartment-specific degradation/half-life evidence under the applicable framework.

The future engine should preserve the source and status of each value: measured, guideline test, read-across, QSAR/modelled or missing.

## 3. Mixtures, metals and M-factors

The project tested several mixture ideas:

- whole-product evidence;
- component toxic-unit summation;
- concentration triggers;
- worst-component rules;
- persistence/bioaccumulation elevation.

No one formula is appropriate across every endpoint and regulatory framework.

A more defensible hierarchy is:

1. use valid whole-mixture evidence when it directly applies;
2. otherwise use transparent component-level rules for the stated framework;
3. do not count the same evidence twice.

Metals and inorganic substances should stay on a separate scientific path because speciation, solubility and bioavailability can make organic PBT/logKow logic inappropriate.

Under CLP, **M-factors are substance-specific multipliers for substances classified Aquatic Acute 1 and/or Aquatic Chronic 1** and are used in mixture summation. A generic table detached from the actual substance classification should not be treated as a universal multiplier.

## 4. Historical PEC/PNEC implementation

The late risk workbook was the point where ChemCodex moved from intrinsic hazard ranking into explicit environmental risk characterisation.

The recovered workbook implemented a source/exposure chain broadly equivalent to:

**chemical concentration x effluent volume -> released mass -> local water PEC -> regional PEC -> PNEC -> PEC/PNEC**

Important historical details were:

- mass release calculated from concentration and effluent volume;
- local water PEC estimated from released mass divided by a diluted receiving volume;
- local PEC capped by solubility in the prototype;
- an additional regional-water step used a further 10-fold reduction;
- historical screening dilution factors included values such as 100, 500 and 1,000 depending on application grouping;
- PNEC candidates were generated from effect endpoints using fixed assessment-factor logic;
- final screening logic compared one or more PEC/PNEC ratios.

Those values are preserved here because they explain the historical implementation. They are **not universal regulatory constants**.

## 5. 2026 deterministic RCR experiment

The later AI-assisted branch made an important architectural improvement: environmental arithmetic was moved outside the language model.

The experimental function:

- collected extracted ecotoxicity endpoints;
- converted numeric values deterministically;
- derived candidate PNECs;
- selected the lowest candidate PNEC;
- calculated an RCR against a PEC.

However, the experiment used fixed **AF = 1,000 for recognised acute endpoints**, **AF = 100 for recognised chronic endpoints**, and a universal **default PEC = 0.05 mg/L**.

Those parameters are useful evidence of the experiment, not recommended defaults. Assessment factors depend on the actual dataset and exposure values depend on the release scenario.

## 6. RQ/RCR interpretation

The clearest mature screening metric in the project is:

**RQ or RCR = PEC / PNEC**

Interpretation should stay deliberately narrow:

- **RQ > 1** means the selected exposure estimate exceeds the selected no-effect threshold under the stated assumptions and should trigger refinement, mitigation or further review;
- **RQ <= 1** means the selected exposure estimate does not exceed that threshold at that screening tier.

Neither result proves the absence or presence of all environmental effects.

## 7. Sediment and higher-tier exposure

The project correctly recognised that a water-only screen can miss benthic exposure.

The recovered sediment equations were exploratory and used simplified partition/deposition and geometry assumptions. A future sediment module should instead document defensible:

- Kd/Koc or other partitioning basis;
- deposition/fate behaviour;
- sediment mixing depth;
- density;
- bioavailability assumptions;
- water-sediment linkage.

Where hydrodynamics dominate the exposure estimate, ChemCodex should hand the case to a higher-tier model rather than force it through a static dilution formula.

## 8. Validation matrix

A production-quality version should validate each layer independently.

### SDS extraction

Measure:

- product/component identity recall;
- CAS accuracy;
- H-code recall;
- endpoint type/species/duration extraction;
- unit conversion;
- concentration-range parsing;
- component attribution;
- missing-data fidelity;
- hallucination rate.

### Hazard logic

Test:

- every threshold and rule;
- whole-mixture versus component handling;
- metals/inorganics;
- regulatory routing;
- evidence reliability;
- data gaps.

### PNEC

Validate:

- endpoint selection;
- marine/freshwater relevance;
- reliability;
- assessment-factor rule;
- documented derivation.

### PEC

Validate:

- mass balance;
- unit integrity;
- discharge/scenario parameters;
- dilution/fate assumptions;
- sediment pathway;
- sensitivity to uncertain inputs.

### Risk engine

Use benchmark cases with independently completed environmental risk assessments and confirm:

- correct RQ/RCR calculation;
- reproducibility;
- uncertainty handling;
- no hidden LLM arithmetic.

## 9. Consolidated target architecture

The strongest recovered architecture is now expressed as nine layers:

**Tier 0 - identity and context**  
Product, components, CAS/EC, concentration ranges, use/release, freshwater/marine context, jurisdiction and confidentiality.

**Tier 1 - evidence extraction**  
Structured evidence objects containing exact source section/page, endpoint type, species, duration, value, unit, comparator, reliability and measured/QSAR/read-across status.

**Tier 2 - regulatory routing**  
Versioned REACH/CLP/OSPAR/HOCNF/PLONOR flags route the workflow without silently declaring universal safety.

**Tier 3 - intrinsic hazard**  
Acute/chronic aquatic hazard, bioaccumulation, persistence, metals/inorganics and whole-mixture/component logic.

**Tier 4 - effect assessment**  
PNEC or other applicable threshold with an explicit derivation and assessment-factor rule.

**Tier 5 - exposure**  
Water/sediment PEC from mass release, flow/discharge, dilution/fate, degradation/partitioning and scenario geometry.

**Tier 6 - risk characterisation**  
PEC/PNEC or equivalent by compartment, with uncertainty, data-quality and validity flags.

**Tier 7 - escalation**  
Higher-tier hydrodynamic modelling, whole-effluent testing, specialist metal assessment, sediment modelling or monitoring.

**Tier 8 - report and audit**  
Machine-readable evidence package, human-readable report, rule/version hashes and reviewer decisions.

## 10. Architectural principle

The clearest design lesson is decoupling.

The AI extraction model should be replaceable without changing the deterministic environmental rules. Likewise, regulatory rules should be updatable without retraining the extraction model.

That separation is what makes the system testable, auditable and maintainable.

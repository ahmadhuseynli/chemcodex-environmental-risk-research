# Scientific architecture

The public architecture is deliberately modular. Each layer has a different scientific job and should be validated separately.

The strongest conclusion from the recovered project is that **intrinsic hazard, environmental exposure and environmental risk are related but not interchangeable**.

A useful ChemCodex engine therefore needs a traceable chain from source evidence to risk characterisation rather than one opaque composite score.

## Tier 0 - identity and context

Capture:

- product and component identity;
- CAS / EC identifiers where available;
- composition and concentration ranges;
- intended use and release scenario;
- freshwater or marine context;
- applicable jurisdiction;
- relevant confidentiality/data-gap status.

## Tier 1 - evidence extraction

Convert SDS and technical-source information into structured evidence objects.

Each object should preserve:

- exact source page/section where possible;
- endpoint type;
- value and unit;
- comparator / inequality;
- species or taxonomic group;
- test duration;
- whole-mixture versus component basis;
- reliability;
- measured / guideline / read-across / QSAR or estimated status.

The extraction layer should also preserve environmental H-codes, biodegradation and persistence evidence, BCF/logKow, PBT/vPvB statements, solubility, mobility and metals/inorganic flags.

Missing evidence should remain missing rather than being invented.

## Tier 2 - regulatory routing

Apply versioned regulatory/list context such as:

- REACH / CLP;
- OSPAR / HOCNF;
- PLONOR;
- other jurisdiction-specific routing rules.

A regulatory-list match can change the assessment path, but it should not automatically be interpreted as proof of zero scenario-specific environmental risk.

## Tier 3 - intrinsic hazard

Characterise the intrinsic environmental hazard using transparent evidence.

This may include:

- acute aquatic toxicity;
- chronic aquatic toxicity;
- bioaccumulation;
- persistence;
- PBT/vPvB evidence;
- metals/inorganics;
- whole-mixture and component-level evidence.

A mature engine should avoid unsupported hidden composite scores.

Where multiple endpoints are available, evidence quality matters. The later prototype direction correctly moved toward preferring experimental/GLP or recognised guideline evidence over weaker QSAR/read-across/estimated evidence, while still retaining the full evidence record.

## Tier 4 - effect assessment

Select the most defensible endpoint for the stated framework and derive the effect threshold required by the method.

For a PNEC workflow, retain:

- selected endpoint;
- species and duration;
- acute/chronic basis;
- marine/freshwater relevance;
- assessment factor or extrapolation rule;
- resulting PNEC;
- reason for the selection.

The assessment factor must depend on the available evidence and the applicable method. Fixed values can be screening assumptions only when they are explicitly justified.

## Tier 5 - exposure assessment

Exposure belongs to the release scenario, not to the SDS.

Potential inputs include:

- released mass or concentration;
- effluent/discharge volume;
- discharge rate and duration;
- receiving-water flow or mixing;
- dilution or hydrodynamic result;
- degradation/fate assumptions;
- partitioning;
- water and sediment compartments;
- local and regional scale;
- scenario geometry.

Defaults can be useful for screening, but they must remain visible assumptions rather than hidden constants.

## Tier 6 - risk characterisation

A simple screening calculation can use:

**RQ or RCR = PEC / PNEC**

Interpretation should remain narrow:

- **RQ > 1** means the selected exposure estimate exceeds the selected effect threshold under the stated assumptions and should trigger refinement, mitigation or further review;
- **RQ <= 1** means the selected exposure estimate does not exceed that threshold at that screening tier.

Neither result proves the presence or absence of every environmental effect.

Outputs should retain:

- input evidence;
- uncertainty;
- missing-data flags;
- compartment;
- scenario assumptions;
- calculation method;
- sensitivity/refinement needs.

## Tier 7 - escalation

A screening tool should know when to stop.

Escalation may be needed when:

- the release is large or prolonged;
- hydrodynamics dominate exposure;
- the mixture is complex;
- sediment pathways matter;
- metals/inorganics need specialist treatment;
- effect data are weak or contradictory;
- the result sits close to a decision threshold;
- sensitive receptors require site-specific treatment.

Higher-tier work can include hydrodynamic dispersion modelling, whole-effluent testing, specialist ecotoxicology, sediment modelling or environmental monitoring.

## Tier 8 - report and audit

A mature system should create both:

- a machine-readable evidence/calculation package; and
- a human-readable assessment report.

The audit record should preserve:

- rule/version identifiers;
- regulatory data version;
- calculation parameters;
- input evidence;
- model/extraction version;
- reviewer decisions and overrides;
- uncertainty and escalation status.

## Design principle

**AI may extract; deterministic rules decide.**

The AI extraction model should be replaceable without changing the environmental calculation rules.

Likewise, changing a regulatory rule should not require retraining the extraction model.

That decoupling is the clearest architectural lesson from the recovered project and is central to making ChemCodex testable, auditable and maintainable.

For the detailed historical-parameter audit, see TECHNICAL_AUDIT.md.

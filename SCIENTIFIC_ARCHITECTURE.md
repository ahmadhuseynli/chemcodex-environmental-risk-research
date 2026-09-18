# Scientific architecture

The public architecture is deliberately modular. Each stage has a different scientific job and should be validated separately.

## Tier 0 - identity and regulatory context

Capture:

- product and component identity;
- CAS / EC identifiers where available;
- composition and confidentiality ranges;
- relevant H-codes;
- OSPAR/HOCNF/PLONOR and REACH context where applicable;
- the intended use or discharge scenario;
- source and quality of each piece of information.

A regulatory list is a routing signal, not proof of zero environmental risk in every scenario.

## Tier 1 - evidence-controlled hazard extraction

Extract and normalise:

- acute aquatic endpoints such as LC50 / EC50 / LL50 / EL50;
- chronic endpoints such as NOEC / EC10 where available;
- species or taxonomic group;
- test duration;
- units and inequality signs;
- whole-mixture versus component evidence;
- biodegradation and persistence statements;
- BCF and logKow;
- PBT/vPvB statements;
- solubility and mobility information;
- metals/inorganic flags.

Each value should retain provenance and a reliability indicator.

## Tier 2 - effect assessment

Select the most relevant defensible endpoint and derive the effect threshold required by the applicable method.

For a PNEC workflow, the record should retain:

- selected endpoint;
- species and duration;
- acute/chronic basis;
- marine/freshwater relevance;
- assessment factor or extrapolation rule;
- the resulting PNEC;
- the reason that rule was selected.

Missing chronic evidence should remain missing. The tool should not quietly manufacture a chronic value.

## Tier 3 - exposure assessment

Exposure belongs to the scenario, not to the SDS.

Potential inputs include:

- released mass or concentration;
- discharge rate and duration;
- receiving-water flow or mixing;
- dilution or hydrodynamic result;
- degradation/fate assumptions;
- partitioning;
- water versus sediment compartment;
- local and regional scale.

Defaults can be used for screening, but they must be visible assumptions rather than hidden constants.

## Tier 4 - risk characterisation

A simple screening calculation can use:

**RQ = PEC / PNEC**

RQ above 1 is a screening concern under the assumptions used. RQ at or below 1 means the selected exposure estimate does not exceed the selected no-effect threshold at that tier. It does not prove zero environmental impact.

The result should travel with:

- input evidence;
- uncertainty;
- missing-data flags;
- compartment;
- scenario assumptions;
- the method used;
- any sensitivity or refinement required.

## Tier 5 - escalation

A screening tool should know when to stop.

Escalation may be needed when:

- the release is large or prolonged;
- hydrodynamics dominate exposure;
- the mixture is complex;
- sediment pathways matter;
- the substance is a metal/inorganic requiring specialist treatment;
- effect data are weak or contradictory;
- the result sits close to a decision threshold;
- sensitive receptors require site-specific treatment.

Higher-tier work can include hydrodynamic dispersion modelling, whole-effluent testing, specialist ecotoxicology or environmental monitoring.

## Design rule

**AI may extract; deterministic rules decide.**

That does not make the deterministic layer automatically correct. Every rule still needs a source, version, test case and review history.

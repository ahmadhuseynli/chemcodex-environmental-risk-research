# ChemCodex / Environmental Chemical Hazard & Risk Research

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22828340.svg)](https://doi.org/10.5281/zenodo.22828340)

This is an independent research project on a practical environmental problem: **how can raw chemical information be turned into a transparent assessment of environmental hazard and scenario-specific risk without hiding the assumptions in a single score?**

The work started from real marine-discharge assessment questions and gradually grew into spreadsheets, mixture logic, SDS parsers, a small web application, a JavaScript rules engine, explicit PEC/PNEC calculations and later AI-assisted extraction experiments.

The most important lesson was that three questions need to stay separate:

1. **What can the chemical intrinsically do?** - toxicity, persistence, bioaccumulation and relevant regulatory flags.
2. **What concentration is expected in the environment?** - the release scenario, dilution, fate and receiving compartment.
3. **Does that exposure exceed a defensible effect threshold?** - PEC/PNEC or another appropriate risk-characterisation method.

That separation is the centre of the current architecture.

**Project page:** https://ahmadhuseynli.github.io/chemcodex-environmental-risk-research/  
**Technical note:** https://ahmadhuseynli.github.io/chemcodex-environmental-risk-research/assets/CHEMCODEX_ENVIRONMENTAL_RISK_TECHNICAL_NOTE_v0.1.pdf  
**Zenodo project DOI:** https://doi.org/10.5281/zenodo.22828340  
**Historical prototype:** https://github.com/ahmadhuseynli/knowyourhazards

## What exists

The recovered project contains a substantial prototype lineage rather than one finished production engine:

- Excel/VBA hazard-screening workbooks;
- mixture toxicity, persistence and bioaccumulation logic;
- REACH / OSPAR / PLONOR / OCNS screening fields;
- a public Streamlit prototype called KnowYourHazards;
- rule-based SDS parsing for components, H-codes and aquatic endpoints;
- Flask/report-generation prototypes;
- a later JavaScript hazard engine with endpoint-reliability handling;
- an explicit PEC/PNEC/RQ environmental-risk workbook;
- sediment-risk concepts;
- AI-assisted SDS extraction experiments.

The public repository does **not** pretend that every historical formula was correct. Several early shortcuts were later found to be too simple or too confident. Those are part of the research record.

## What the deeper technical audit added

The final project-history audit made several parts of the scientific basis more precise.

It confirmed that:

- historical BCF/logKow screening logic must be kept separate from formal REACH Annex XIII criteria;
- generic M-factor tables and experimental species weights are not defensible as universal regulatory multipliers;
- historical dilution factors, assessment factors and default PEC values were prototype assumptions rather than fixed regulatory constants;
- sediment exposure needs a separate, defensible partitioning/fate treatment;
- the mature architecture is better represented as a nine-layer chain from identity/evidence through regulatory routing, hazard, PNEC, PEC, risk, escalation and audit;
- the AI extraction layer should be replaceable without changing the deterministic environmental rules.

The detailed parameter-by-parameter review is in [TECHNICAL_AUDIT.md](TECHNICAL_AUDIT.md).

## Current scientific direction

The strongest version of the idea is a provenance-first tiered engine:

**identity/context -> evidence extraction -> regulatory routing -> intrinsic hazard -> effect assessment -> exposure -> risk characterisation -> escalation -> report/audit**

AI can help extract and normalise evidence from SDS documents, but the scientific decision layer should remain deterministic, reviewable and tied to explicit sources and assumptions.

## Why this could be useful

Environmental teams often work across disconnected SDS files, spreadsheets, regulatory lists, discharge assumptions and specialist studies. A well-designed tool could bring those pieces into one traceable workflow.

If properly validated, this kind of system could help with:

- first-pass screening of chemical discharges;
- consistent review of large chemical inventories;
- locating missing or contradictory SDS evidence;
- documenting how PNECs and screening RQs were derived;
- deciding when a simple screen is enough and when hydrodynamic modelling, whole-effluent testing or specialist review is needed;
- creating auditable assessment records instead of opaque hazard scores.

## What this project does not claim

This is not a validated regulatory decision engine and it is not a substitute for competent-authority requirements, specialist ecotoxicology or site-specific modelling.

The recovered project includes historical heuristics that should not be reused as regulatory rules without revalidation. The current public code therefore focuses on **transparent evidence extraction and explicit screening calculations**, not on reproducing every older scoring shortcut.

See:

- [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
- [SCIENTIFIC_ARCHITECTURE.md](SCIENTIFIC_ARCHITECTURE.md)
- [TECHNICAL_AUDIT.md](TECHNICAL_AUDIT.md)
- [PROTOTYPE_LINEAGE.md](PROTOTYPE_LINEAGE.md)
- [VALIDATION_AND_LIMITS.md](VALIDATION_AND_LIMITS.md)
- [EVIDENCE_AND_PROVENANCE.md](EVIDENCE_AND_PROVENANCE.md)
- [REFERENCES.md](REFERENCES.md)
- [ROADMAP.md](ROADMAP.md)
- [prototype_code/](prototype_code/)

## Related independent research

- Atmospheric Dispersion Surrogate Research: https://ahmadhuseynli.github.io/aermod-surrogate-research/
- Methane Measurement & Quantification Conditions Research: https://ahmadhuseynli.github.io/methane-measurement-conditions-research/

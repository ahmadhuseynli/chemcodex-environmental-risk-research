# ChemCodex / Environmental Chemical Hazard & Risk Research

## Public technical note

This note describes the first consolidated public research architecture for ChemCodex, an independent project on environmental chemical hazard and risk assessment.

The project did not begin as a software-product exercise. It began with practical questions about chemical discharge to the marine environment: how much material is released, what concentration reaches the environment, what ecotoxicity evidence is available, and what a ratio such as PEC/PNEC actually means.

Over successive prototypes, the work moved from one-off calculations into reusable spreadsheets, mixture logic, SDS parsers, a small web application, browser-based rules, explicit PEC/PNEC calculations and later AI-assisted evidence extraction.

The main outcome is architectural rather than a claim that one formula is finished.

## 1. Hazard is not risk

A recurring problem in environmental chemical assessment is the temptation to treat a hazard number as if it were a scenario-specific risk result.

They are different.

Hazard asks what a chemical is intrinsically capable of doing. Relevant evidence may include acute and chronic aquatic toxicity, persistence, bioaccumulation, H-codes and classification or regulatory status.

Risk additionally asks what environmental exposure will occur under a defined release scenario.

A source concentration divided by an LC50 and a PEC divided by a PNEC may produce very different numbers because they are not the same calculation and do not answer the same question.

That distinction became the organising principle of the later project.

## 2. The first reusable hazard engine

The first substantial tool was an Excel workbook that combined information normally scattered across an SDS and regulatory references.

It captured product identity and components, aquatic H400-series statements, acute and chronic toxicity, REACH and offshore regulatory lookups, BCF/logKow, solubility, persistence and biodegradation.

Later workbook versions added separate sheets for toxicity, PBT, bioaccumulation and M-factor experiments, together with mixture logic and summary macros.

This stage was useful because it established a reusable information structure. It also created some shortcuts that later needed to be challenged.

For example, some versions converted simple biodegradation information into estimated persistence half-lives or used fixed mixture thresholds. Those may be useful development hypotheses, but they are not automatically equivalent to formal REACH or OSPAR rules.

## 3. From spreadsheet to application

The spreadsheet logic was converted into a small Streamlit application called KnowYourHazards.

That public prototype is still available at:

https://github.com/ahmadhuseynli/knowyourhazards

It shows the transition from an analyst workbook into an interactive assessment tool. It should be read as historical prototype code rather than the present scientific specification.

A separate machine-learning branch was also tried. Recovery of the underlying data later showed that the training corpus did not contain a meaningful label structure and the saved model effectively represented only an "Unknown" class.

No predictive claim is made from that branch. Its value is the lesson it created: machine learning should not be introduced merely because a folder contains data.

## 4. SDS extraction became the better automation problem

The next branch treated the SDS as an information-retrieval problem.

Rule-based parsers were developed to extract product identity, Section 3 components, CAS numbers, H400-H413 statements and environmental endpoints such as LC50, EC50, IC50, NOEC, LL50 and EL50.

The parser logic also tried to preserve species, test duration, comparators and units.

That direction is much easier to validate scientifically. An extraction layer can be scored for recall, unit accuracy, component linking and false extraction without mixing those errors with the environmental decision logic.

A later AI-assisted branch followed the same idea: let the model organise evidence from an SDS, but do not let it invent missing endpoints or silently decide which assessment factor should govern a risk result.

## 5. Explicit exposure and effect

The project became scientifically stronger when the workbook architecture separated exposure from effect.

The later environmental-risk workbook included discharge volume and duration, chemical concentration and mass release, dilution assumptions, local and regional water PEC, effect endpoints, acute/chronic PNEC fields, sediment considerations and a PEC/PNEC risk quotient.

The basic screening equation is simple:

RQ = PEC / PNEC

The interpretation needs more care.

RQ above 1 indicates a screening concern under the selected assumptions and normally calls for mitigation, refinement or escalation. RQ at or below 1 means the selected exposure estimate does not exceed the selected no-effect threshold at that tier. It does not prove that there is no environmental impact.

## 6. What the higher-tier evidence changed

A detailed marine-dispersion study recovered during the project review helped make one limitation clear: static dilution screening is not the right tool for every discharge.

Where currents, release duration, spatial footprint, time-integrated exposure or sediment processes matter, a hydrodynamic model can answer questions that a spreadsheet cannot.

That led to an important design requirement for ChemCodex: the tool should not only calculate. It should also know when to stop calculating and hand the case to a higher-tier method.

## 7. Current architecture

The consolidated architecture is best represented as a nine-layer chain.

Tier 0 - identity and context. Product/components, CAS/EC, concentration ranges, intended use/release, freshwater or marine context, applicable jurisdiction and data-quality/confidentiality status.

Tier 1 - evidence extraction. Structured evidence objects retain source section/page, endpoint type, species, duration, value, unit, comparator, reliability and measured/guideline/read-across/QSAR status.

Tier 2 - regulatory routing. Versioned REACH/CLP/OSPAR/HOCNF/PLONOR flags route the assessment workflow without silently declaring universal safety.

Tier 3 - intrinsic hazard. Characterise acute/chronic aquatic hazard, bioaccumulation, persistence, metals/inorganics and whole-mixture/component evidence without hiding unsupported composite scores.

Tier 4 - effect assessment. Derive PNEC or another applicable effect threshold from selected evidence with an explicit assessment-factor rule and justification.

Tier 5 - exposure. Calculate water/sediment PEC from mass release, discharge, dilution/fate, degradation/partitioning and scenario geometry with all defaults visible.

Tier 6 - risk characterisation. Calculate PEC/PNEC or another relevant metric by compartment with uncertainty, data-quality and validity flags.

Tier 7 - escalation. Route unsuitable screening cases to hydrodynamic modelling, whole-effluent toxicity, specialist metal assessment, sediment modelling or monitoring.

Tier 8 - report and audit. Preserve a machine-readable evidence package, human-readable report, rule/version identifiers and reviewer decisions.

The architectural principle is decoupling: the AI extraction model should be replaceable without changing the deterministic environmental rules, and regulatory-rule changes should not require retraining the extraction model.

## 8. Technical audit: parameters that should not become hidden defaults

The final project-history audit recovered several numerical parameters that are important to preserve because they explain what the historical prototypes actually did.

They are not recommended universal defaults.

Historical implementations included:

- BCF 1,000 as a bioaccumulation trigger in some workbook/SOP versions;
- experimental algae and daphnia species weights of 2 and 1.5 in the JavaScript engine;
- screening dilution factors including 100, 500 and 1,000 in the ERA workbook;
- an additional regional-water step using a further 10-fold reduction;
- fixed acute and chronic assessment factors of 1,000 and 100 in the 2026 deterministic experiment;
- an experimental default PEC of 0.05 mg/L.

The scientific audit makes the distinction explicit.

For REACH Annex XIII, BCF >2,000 is the B criterion and BCF >5,000 is the vB criterion. LogKow can support screening but is not itself the final Annex XIII B/vB decision.

M-factors under CLP are substance-specific multipliers tied to Aquatic Acute 1 and/or Aquatic Chronic 1 classification and mixture summation, rather than a universal generic table.

PNEC assessment factors must depend on the available ecotoxicity dataset and the applicable method. PEC values and dilution/fate assumptions must come from the actual release scenario.

Sediment exposure also remains a higher-tier module. A defensible future implementation should document partitioning basis, deposition/fate, sediment mixing depth, density, bioavailability and the link between water and sediment exposure.

## 9. What remains unresolved

The project is not yet a validated regulatory engine.

Several historical formulas were too broad or too confident. Examples include generic PBT mixture triggers, species weighting, generic M-factor handling, fixed assessment factors, universal PEC/dilution assumptions and simplified sediment partitioning.

The recovered web application is also a prototype rather than a clean production deployment.

The correct next step is not to hide those limitations. It is to rebuild the rule layer around locked sources, versioned formulas and benchmark cases.

## 10. Public prototype code

The public repository includes two small pieces of code.

The first extracts environmental H-codes and simple aquatic endpoint candidates from SDS text.

The second performs a transparent PEC/PNEC screening calculation in which the release mass, receiving volume, dilution factor, effect value and assessment factor are all explicit inputs.

These scripts are not intended to reproduce every older ChemCodex rule. They demonstrate the architecture that survived the research.

## 11. Validation needed

Before operational use, the system needs a curated benchmark set with manually reviewed SDS/component data and independently completed environmental risk assessments.

The extraction layer and the risk engine should be validated separately.

Extraction metrics should cover component and endpoint recall, unit accuracy, species/duration identification, component linking and hallucination rate.

The deterministic engine should then be tested with identical curated inputs so calculation error is not confused with extraction error.

## 12. Longer-term use

If validated, the same structure could support chemical inventory review, marine-discharge screening, environmental permitting, assessment QA and consistent handoff to higher-tier studies.

The main value would not be a colourful hazard ranking. It would be a traceable evidence chain showing where each conclusion came from and where the screening method stops being adequate.

## Public references

OSPAR Offshore Chemicals:
https://www.ospar.org/work-areas/oic/chemicals

ECHA Guidance on Information Requirements and Chemical Safety Assessment:
https://echa.europa.eu/guidance-documents/guidance-on-information-requirements-and-chemical-safety-assessment

OECD Guidelines for Testing of Chemicals, Section 2:
https://www.oecd.org/en/publications/oecd-guidelines-for-the-testing-of-chemicals-section-2_20745761.html

This is independent research and is not affiliated with or endorsed by OSPAR, ECHA, OECD, IMO/GESAMP or any competent authority.

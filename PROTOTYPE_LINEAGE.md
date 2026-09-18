# Prototype lineage

The project changed shape several times. The useful story is not a calendar of releases but how the problem definition improved.

## One-off discharge calculations

The earliest work dealt with real marine-discharge questions. Release mass, dilution, ecotoxicity and PEC/PNEC-style comparisons were used manually.

A key problem appeared early: a source concentration divided by an LC50 can give a completely different answer from a scenario-specific PEC/PNEC ratio. They are answering different questions.

That pushed the project toward separating exposure from effect.

## Excel hazard engine

The first reusable tool was an Excel workbook. It pulled together aquatic H-statements, acute and chronic toxicity, REACH and offshore regulatory lookups, BCF/logKow, persistence and biodegradation.

Later workbook versions added:

- mixture logic;
- dedicated PBT and bioaccumulation sheets;
- total-toxicity calculations;
- M-factor experiments;
- summary macros and reporting.

This stage created a useful data structure, but it also introduced some project-specific thresholds that were later found to be too confidently labelled as regulatory rules.

## KnowYourHazards

The spreadsheet logic was converted into a small Streamlit application. The original public repository is preserved here:

https://github.com/ahmadhuseynli/knowyourhazards

That application is a historical prototype. It is not the current scientific specification.

## Experimental ML branch

A random-forest experiment tried to learn hazard classes from extracted JSON/SDS features.

Recovery of the training assets showed that the corpus was effectively unlabeled and the saved model contained only the class "Unknown". No meaningful predictive validation can be claimed from it.

I keep this in the history because it changed the direction of the work: a model should not be trained simply because a folder of data exists.

## SDS parsing

The next branch treated the problem as information extraction rather than classification.

Parsers were developed to locate:

- product identity;
- Section 3 components;
- CAS numbers;
- H400-H413 statements;
- LC50 / EC50 / IC50 / NOEC / LL50 / EL50 values;
- species;
- duration;
- units and comparators.

This was a more useful technical direction because it could feed a transparent rule engine without pretending to learn unsupported labels.

## Web application and report generation

A Flask prototype added an assessment interface, an SDS parsing endpoint and PDF report generation. Later versions also experimented with AI-assisted extraction.

The recovered package is not a clean production deployment. It is best treated as a prototype codebase.

## JavaScript hazard engine

A later browser-oriented rules engine added endpoint reliability handling, component-level outputs, whole-mixture versus component logic and checks for discrepancies between hazard statements and numeric evidence.

Some of the scoring logic remains historical and needs regulatory revalidation, but the move toward evidence quality was an important improvement.

## Explicit environmental risk

The strongest scientific step was the move from hazard ranking into explicit exposure and effect.

The ERA workbook separated:

- discharge/source information;
- PEC;
- effect endpoints;
- PNEC;
- water and sediment considerations;
- risk quotient.

That is the basis of the current architecture.

## AI-assisted extraction

The final experimental branch used an LLM to structure SDS information while keeping the proposed calculation layer deterministic.

That remains the most credible use of AI in this project: help organise evidence, but do not let the model invent missing endpoints or silently make regulatory decisions.

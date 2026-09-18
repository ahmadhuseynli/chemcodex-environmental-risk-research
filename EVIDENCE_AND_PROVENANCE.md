# Evidence and provenance

## What the reconstruction found

The private project record contains:

- multiple generations of Excel/XLSM hazard workbooks;
- a large saved development transcript;
- VBA and formula histories;
- Streamlit and Flask application code;
- rule-based SDS parsers;
- report-generation code;
- a JavaScript hazard engine;
- an explicit PEC/PNEC/RQ environmental-risk workbook;
- presentation material describing the intended end-to-end workflow;
- later AI-assisted SDS extraction experiments;
- code/formula lineage and recovery audits.

The public repository is a cleaned research layer on top of that evidence. It is not a mirror of the private working folders.

## Scale of the recovered technical record

The controlled recovery found:

- a **401-file project-root manifest**;
- approximately **7.39 MiB** of standalone project material in that root, excluding the recovery workspace itself;
- a **484-record workbook formula register**;
- formula lineage across **eight recovered workbook versions**;
- a workbook-version difference audit;
- a source-code lineage audit;
- browser / GitHub / AI-tool provenance checks;
- a primary-reference audit.

One mature workbook generation contained **136 formulas** across user-guide, PBT, bioaccumulation, total-toxicity, M-factor and lookup/support sheets.

These numbers are useful as evidence of the depth of the prototype history. They are not performance metrics and do not establish scientific validation by themselves.

## Evidence hierarchy

The project recovery distinguishes between:

1. original workbook/code/report artifacts;
2. contemporaneous communications and saved development transcripts;
3. partial browser/chat traces;
4. retrospective reconstruction and scientific audit;
5. external authoritative scientific/regulatory sources used to audit the historical rules.

Where an original artifact conflicts with a later recollection, the original artifact is given more weight.

Historical implementation and current scientific validity are kept separate. A formula can be reported faithfully as evidence of what the prototype did while also being classified as a heuristic that should not be carried forward.

## Historical implementation versus current endorsement

A formula can be reproduced faithfully as evidence of what the prototype did without being endorsed as scientifically or regulatorily correct.

That distinction matters here because several old formulas were later challenged.

Examples include:

- BCF 1,000 being used as a historical bioaccumulation trigger even though current REACH Annex XIII uses BCF >2,000 for B and >5,000 for vB;
- generic logKow thresholds being treated too strongly;
- fixed PNEC assessment factors;
- fixed/default PEC values and dilution factors;
- experimental species weighting;
- generic M-factor treatment;
- simplified sediment assumptions.

The public code therefore avoids re-publishing questionable scoring shortcuts as if they were current rules.

## Historical public repository

The earlier public Streamlit prototype is retained as a real prototype artifact:

https://github.com/ahmadhuseynli/knowyourhazards

It shows an earlier stage of the project and should be read in that context.

## What remains private

The public repository does not publish:

- private email or chat content;
- browser-history databases;
- full recovery logs;
- local machine paths;
- API credentials;
- raw proprietary or third-party SDS data;
- external project reports that may carry redistribution restrictions;
- the full workbook library;
- confidential or employer-linked material.

## Security note

A credential was found in the recovered private webtool configuration during the publication review. That configuration is intentionally excluded from the public archive. No credential is required for the public prototype code in this repository.

## Why the provenance matters

ChemCodex did not evolve as one clean application with a single immutable algorithm. Different branches solved different parts of the problem.

The public record therefore avoids the misleading idea of one "final historical formula".

The stronger conclusion is that the final scientific architecture exists across complementary artifacts:

- structured evidence extraction;
- deterministic hazard logic;
- explicit PNEC/effect assessment;
- explicit PEC/exposure assessment;
- transparent PEC/PNEC risk characterisation;
- escalation and audit requirements.

That is the architecture carried forward in the current public project.

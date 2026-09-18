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
- an external higher-tier marine-dispersion example used as contextual evidence;
- later AI-assisted SDS extraction experiments;
- code/formula lineage and recovery audits.

The public repository is a cleaned research layer on top of that evidence. It is not a mirror of the private working folders.

## Evidence hierarchy

The project recovery distinguishes between:

1. original workbook/code/report artifacts;
2. contemporaneous communications and saved development transcripts;
3. partial browser/chat traces;
4. retrospective reconstruction and scientific audit.

Where an original artifact conflicts with a later recollection, the original artifact is given more weight.

## Historical implementation versus current endorsement

A formula can be reproduced faithfully as evidence of what the prototype did without being endorsed as scientifically or regulatorily correct.

That distinction matters here because several old formulas were later challenged.

The public code therefore avoids re-publishing questionable scoring shortcuts as if they were current rules.

## Historical public repository

The earlier public Streamlit repository is retained as a real prototype artifact:

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

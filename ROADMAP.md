# Roadmap

The next useful step is consolidation and validation, not another layer of scoring rules.

## 1. Freeze the evidence schema

Define one stable schema for:

- chemical identity and composition;
- endpoint type, value, unit, species and duration;
- reliability and source;
- biodegradation / persistence evidence;
- BCF / logKow;
- regulatory flags;
- release scenario;
- PEC, PNEC and risk output.

## 2. Build a reviewed benchmark set

Create a set of chemical cases where SDS fields and environmental endpoints have been manually checked.

Do not train or score against unreviewed parser output.

## 3. Validate extraction separately

Measure:

- component recall;
- endpoint recall;
- unit accuracy;
- species/duration identification;
- component-to-endpoint linking;
- false extraction and hallucination rate.

Compare rule-based and AI-assisted extraction on the same documents.

## 4. Rebuild the deterministic rule layer

Every rule should have:

- a named source;
- version/date;
- explicit applicability;
- unit test;
- edge-case tests;
- a human-readable explanation.

Unsupported historical heuristics should not quietly survive.

## 5. Validate exposure and risk

Test PEC/PNEC calculations against independently completed environmental risk assessments.

Include simple screening cases and cases that deliberately require escalation.

## 6. Add higher-tier handoff

A useful system should be able to say:

**this case is outside screening support - use hydrodynamic modelling, whole-effluent testing, specialist metal assessment or monitoring.**

That boundary is part of the product, not a failure of it.

## Longer-term direction

If the scientific engine is validated, the same evidence model could support chemical inventory review, environmental permitting, discharge screening and auditable compliance workflows.

The immediate priority remains scientific correctness and provenance.

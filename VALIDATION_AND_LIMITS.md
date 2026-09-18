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

## Failed branches retained in the record

The project also has genuine failures:

- early logic sometimes mixed source concentration with environmental risk;
- some cement-screening calculations risked double-counting dilution;
- the first ML branch had no useful label structure;
- some parser versions contained product-specific debugging fallbacks;
- pseudo-OCNS logic changed repeatedly;
- the recovered webtool is incomplete as a standalone deployment;
- a later deterministic risk function was only an experiment and was not integrated into the archived application.

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

The extraction layer should be tested separately for entity/endpoint recall, unit accuracy, component linking, species/duration extraction and hallucination rate.

The risk engine should then be tested with curated inputs so parser errors are not confused with scientific-rule errors.

## Regulatory position

The public code is for research and demonstration. It is not an official OSPAR, ECHA, GESAMP or competent-authority implementation.

For real regulatory work, the applicable current legislation, guidance, national requirements and specialist judgement govern.

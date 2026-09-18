# Project overview

## The problem

Chemical environmental review often begins with a Safety Data Sheet, but an SDS alone cannot answer whether a particular discharge will create unacceptable environmental risk.

An SDS may contain aquatic toxicity values, hazard statements, biodegradation information, BCF or logKow data and mixture composition. A discharge assessment still needs a source term, receiving-environment assumptions, an effect threshold and a clear way to compare exposure with effect.

This project grew from trying to connect those pieces in one repeatable workflow.

## The core distinction

The project eventually settled on a distinction that sounds simple but changes the whole architecture:

**hazard is not the same thing as risk.**

A substance can have serious intrinsic aquatic hazards and still produce a low scenario-specific exposure. A low-hazard material can still deserve modelling when the released mass is very large or the receiving environment is poorly mixed.

That means a useful tool should not compress everything into one unexplained number.

## The intended workflow

The current target architecture separates the work into stages:

1. establish chemical identity, composition and regulatory context;
2. extract environmental evidence from the SDS and other defensible sources;
3. assess toxicity, persistence and bioaccumulation with evidence quality attached;
4. derive an appropriate effect threshold such as a PNEC, with the assessment factor and justification preserved;
5. calculate a scenario-specific PEC or equivalent exposure estimate;
6. compare exposure with effect, normally through PEC/PNEC or another suitable metric;
7. carry uncertainty and missing-data flags forward;
8. escalate cases that cannot be represented safely by a screening calculation.

The last step matters. A spreadsheet dilution factor is not a substitute for hydrodynamic modelling when currents, release duration, spatial footprint or sediment exposure dominate the case.

## Where AI fits

The project included an experimental ML branch, but the recovered dataset was not fit for meaningful classification. That branch is retained as a failed experiment rather than presented as a result.

The more defensible role for AI emerged later: **extracting and normalising evidence**.

An AI-assisted parser can help locate Section 3 components, H-codes, aquatic endpoints, biodegradation statements, BCF/logKow data and PBT/vPvB information. The risk logic should then use explicit deterministic rules that can be inspected and reviewed.

This separation also makes validation easier: extraction accuracy can be tested independently from the scientific risk engine.

## What the project could become

A mature version could become a chemical environmental decision-support system rather than a simple hazard calculator.

The useful end state would be a traceable chain from:

**SDS + composition + regulatory context + release scenario -> structured evidence -> hazard/effect assessment -> environmental exposure -> risk characterisation -> escalation decision**

That could support inventory screening, offshore chemical review, environmental permit preparation, assessment QA and the handoff from simple screening to higher-tier modelling.

The project is not at that validated operational stage yet. The current public repository records the prototype work and the scientifically stronger architecture that emerged from it.

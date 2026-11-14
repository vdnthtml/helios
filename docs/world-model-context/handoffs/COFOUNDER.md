# Technical co-founder review handoff

## Objective and inputs

Give a rigorous independent review of world-modelx. Read current direction and decisions first, then `../reference/FOUNDER_HANDOFF.md` for the founder's reasoning and evolution, `../reference/TECHNICAL_REVIEW.md` for the detailed earlier engineering proposal, and `../reference/ARCHITECTURE_REQUIREMENTS.md` for the latest full scope. Specialist research findings, when available, should inform the critique rather than replace it.

## Questions to challenge

Is the ontology coherent or overly elaborate? Are assertions, events, hypotheses, qualifiers, multi-party interactions, identity reversal, evidence lineage, and time represented adequately? Is a relational canonical store with graph projections simpler than using an existing temporal graph system? Do segmentation or capsules add measurable value? How are current and historical indexes kept correct? Can retrieval scopes and derived outputs prevent private leakage? Which attribution claims are identifiable from the available evidence? What learning actually improves automatically, and what requires verified labels and evaluated updates? Can the prototype test a real advantage over strong baselines at affordable cost?

Challenge scope, acquisition feasibility, operational complexity, source reliability, benchmark leakage, model contamination, framework usefulness, customer utility, and research risk. Preserve the founder's cross-domain goal while recommending the smallest defensible test.

## Requested return

Architectural verdict; ranked critical flaws; concrete corrections; stack choices with alternatives/evidence; simplified but representative prototype; evaluation design; assumption-based engineering estimates; revised architecture; hardest unsolved problem; go/no-go or conditional-go assessment. Every proposed correction should cite the requirement, explain the failure, give the replacement and tradeoffs, and identify an experiment or test.

A trusted reviewer may recommend changing any technical proposal. Recommendations become explicit proposals rather than silent product decisions. Nothing in this packet claims the architecture has been implemented or validated. Record feedback and disagreements with provenance; do not overwrite the original rationale.

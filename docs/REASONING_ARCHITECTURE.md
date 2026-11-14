# Reasoning-first information world model

Founder direction: prioritize cross-domain inference, connecting evidence, historical understanding and learning. Signal briefs are one interface, not the architecture's purpose. This is a design, not a claim of implemented reasoning or predictive performance.

## Investigation contract

1. Define the question, entities, time horizon, access scope, evidence requirements and resource budget.
2. Retrieve cutoff-eligible observations using exact, lexical, semantic and typed relationship paths. Preserve source dependencies and conflicting evidence; follow cross-domain links when justified.
3. Generate competing hypotheses and explicit alternatives, including shared causes and independent emergence. Record each inference separately from observations and source assertions.
4. Seek disconfirming evidence and missing information; distinguish documented pathways from conjectured influence and causal attribution. Abstain when evidence cannot distinguish explanations.
5. Return evidence-linked findings, uncertainty, time boundaries, alternative explanations, missing evidence and investigation trace. Record model and tool versions, costs and stopping reason.
6. Revisit dependent conclusions on corrections, and measure errors against verified outcomes. Never treat model output or user feedback alone as ground truth.

## Historical reasoning

Maintain distinct event, publication, observation, ingestion, knowledge and revision times. Support both actual-system-knowledge and public-availability replay, with explicit unknown availability. Snapshot or reconstruct all derived indexes, identity mappings and summaries at the cutoff. Prevent future information leakage, including model contamination; label its residual uncertainty. Freeze forecasts and resolution criteria before revealing outcomes, compare with simple baselines and measure calibration and errors.

## Architecture and experiments

Use a canonical evidence and identity ledger, typed relationships, temporal queries, scope-enforced retrieval, versioned investigation plans, hypothesis records, evidence dependencies and feedback. Postgres, pgvector, language models and graph projections remain candidates. Compare lexical, hybrid and graph-assisted retrieval; test cross-domain recall, source fidelity, counterevidence recall, false connection rates, temporal leakage, latency and cost. Compare explicit hypothesis search to a direct-answer baseline. Capsules and model fine-tuning must earn their place against simpler baselines on frozen, source-separated evaluation sets.

Signal monitoring, open-ended research, personal and enterprise decision support, API and messaging experiences should all use the same core. No application-specific ranking may rewrite source evidence or dictate the ontology.

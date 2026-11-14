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
## Helios v3 final clarifications — 14 Nov 2026

Status: Planned. Helios v3 was approved as the architectural baseline on 14 Nov 2026 (conditional approval; see docs/STATUS_AND_DECISIONS.md). The clarifications below are part of that baseline. They are design decisions, not claims of implemented reasoning. No inference tests exist yet; the only implemented code on this branch is the SQLite evidence/identity ledger with 18 contract tests (see docs/BUILD_PLAN.md, section 9).

### Two-dimensional historical queries

Historical queries are two-dimensional: `as_of(valid_at, known_at)`.

- `valid_at` is real-world valid time: when something was true in the world.
- `known_at` is knowledge time: what Helios knew at that point, that is, which events had been ingested and not yet superseded.

Employment example. A person was hired on 1 Jan, Helios learned of the hiring on 1 Feb, the person left on 1 Mar, and Helios learned of the departure on 15 Mar:

- `valid_at=Mar 10, known_at=Mar 10` — the employment appeared ongoing: as of 10 Mar, Helios knew the hiring but not yet the departure.
- `valid_at=Mar 10, known_at=Mar 16` — the employment had ended on 1 Mar: by 16 Mar, Helios knew of the departure, so the 10 Mar state is revised.
- `valid_at=Feb 15, known_at=Mar 16` — the person was active on 15 Feb: the hiring was valid then, and the later departure does not change that.

Valid-time and knowledge-time are two independent projections from the immutable event log. Supersession closes knowledge validity (a superseding event ends what was previously known to be current); evidence determines real-world valid time. A correction therefore changes what is known, and what is known about the past, without rewriting the event log.

### Investigation taxonomy

There are 8 investigation types:

1. `claim_verification`
2. `trend_detection`
3. `origin_propagation`
4. `causal_influence`
5. `decision_adoption`
6. `event_explanation`
7. `comparative_diagnostic`
8. `forecast_scenario`

Classification and extraction belong in pipeline quality evaluation, not in investigation. Competing explanations are required for explanatory and causal investigations (for example `event_explanation` and `causal_influence`), not for every factual verification: a straightforward factual check does not need a rival explanation invented for it.

### Exclusivity and conflicting assertions

Exclusivity applies only to explicitly single-valued authoritative state properties, via a property-semantics registry that records, for each such property, its cardinality, temporal behaviour, authority, and permitted types. Multiple positions, suppliers, categories, and aliases are permitted, and conflicting source assertions coexist as separate source-anchored assertions; they are not collapsed into one value, and disagreement is preserved as evidence.

### Hindsight Gain

Hindsight Gain is not decomposed into exact leakage / legitimate / drift numbers without controlled experiments. Leakage is a factual audit finding first: establish what future information was available, and whether it could have influenced the result, before attributing any share of a gain to leakage.

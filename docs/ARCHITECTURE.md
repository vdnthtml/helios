# Helios v0 architecture

**Status:** architecture and research baseline, not an implementation specification with settled technology choices.

## Mission and boundary

Helios is intended to be a continuously evolving information world model that represents and investigates documented relationships across people, information, narratives, organizations, economics, technologies, decisions, events, and outcomes. It should help users inspect evidence, compare plausible explanations, reconstruct what was knowable at a point in time, and test forecasts against subsequent reality.

It must not imply omniscience, hidden access to private thoughts or conversations, causal certainty from chronology, or independent confirmation merely because several sources repeat the same upstream claim.

## Logical modules

These are responsibilities, not a microservice plan.

1. **Acquisition** — collect only authorized, licensed, or consented inputs; preserve source context and collection metadata.
2. **Extraction and normalization** — produce versioned candidates for entities, assertions, events, and relationships without replacing originals.
3. **Identity, temporal evidence, and governance** — maintain stable/provisional identity, provenance, bitemporal lineage, corrections, scopes, and auditability.
4. **Segmented world memory** — expose typed relational views, semantic indexes, domain projections, and summaries without losing cross-domain links.
5. **Investigation and inference** — plan bounded evidence gathering; form, compare, and qualify hypotheses.
6. **Expert framework reasoning** — apply explicitly represented, versioned professional methods rather than presenting prompt style as expertise.
7. **Attribution and prediction** — distinguish information pathways, explanatory mechanisms, and consequences; commit predictions before outcome evaluation.
8. **Learning and evaluation** — replay historical states, score outputs, capture corrections, and change models/policies only through evaluated controls.
9. **Monitoring and interfaces** — initially messaging-oriented; later API, CLI, MCP, and enterprise surfaces on shared contracts.

## Canonical objects and epistemic states

The exact schema is unresolved, but implementations must preserve these distinctions.

| Object | Meaning | Must not be confused with |
| --- | --- | --- |
| Source | Provider/origin, license, access, collection method | a truth rating |
| Observation | Source material recorded at a time, with content reference/hash | the claim it contains |
| Entity | Persistent, possibly provisional identity with aliases and evidence | a guaranteed real-world match |
| Assertion | A source-anchored statement: subject, predicate, object/value, qualifiers, modality, polarity | a verified event |
| Event | Something reported or determined to have occurred; can have many participants and roles | its announcement or intention |
| Relationship | Typed, qualified connection among entities/events/assertions | proof of mechanism or causality |
| Hypothesis | Explicit candidate explanation, inputs, assumptions, alternatives, status | a fact |
| Evidence link | Support, contradiction, context, or dependency relation with provenance | an independent source by default |
| Forecast/outcome | Time-bound prediction and later measured result | retrospective narrative |

Minimum metadata normally includes scope/access, source references, confidence or resolution state, creation/revision provenance, and temporal qualifiers. An assertion such as “plans to acquire,” “announced an acquisition,” and “completed an acquisition” must be represented as distinguishable states, not collapsed.

## Time and provenance

Useful replay requires more than one timestamp. Retain, where relevant:

- **valid/event time** — when something was true or occurred;
- **publication/observation time** — when a source made material available;
- **ingestion/knowledge time** — when Helios received it;
- **system/revision time** — when Helios created, superseded, or invalidated a record.

Never overwrite a correction as though the prior state never existed. Record the successor, reason, actor/process version, and affected derivatives. Preserve source independence: syndication and repeated articles may derive from one origin.

## Segmentation and memory

Helios should preserve a shared, evidence-native foundation while constructing query-relevant contexts. Segments can reflect domain, task, entity neighborhood, time window, evidence scope, access boundary, or investigation. They are retrieval and cost controls, not mutually exclusive labels for people or facts.

Proposed **evidence capsules** are compact, lineage-linked context packages that summarize a question-relevant subgraph and its disagreements. They are a hypothesis to test against direct retrieval and other baselines—not a canonical record or a claimed moat.

## Inference, attribution, and expert frameworks

An investigation should state its question, budget, permitted sources, activated scopes, evidence retrieved, alternatives considered, and stopping reason. It should report whether a conclusion is:

- a documented observation;
- an extracted assertion;
- an inference supported by stated evidence and assumptions;
- an unresolved competing explanation; or
- a forecast.

Attribution is not one score. Keep at least separate concepts for content similarity/lineage, pathway or exposure, potential mechanism, causal explanation, and observable outcome. Correlation, sequence, semantic resemblance, and repetition are evidence to assess—not proof of influence.

Expert frameworks should be versioned artifacts with applicability, inputs, procedure, output schema, known limits, and evaluation. They should be selectable and testable against suitable tasks; no framework is assumed universally correct.

## Learning and evaluation

Knowledge ingestion, retrieval policy updates, model retraining, and inference-policy changes are different operations. Each needs provenance, rollback, and evaluation. Historical testing must enforce an availability cutoff, avoid backfilled labels and future summaries, record the model/prompt/configuration, and compare against baselines. A forecast needs target, horizon, timestamp, confidence or distribution, evidence state, and scoring rule before its outcome is known.

## Privacy, access, and action boundaries

All records and derivatives must honor applicable license, source, retention, consent, and access restrictions. Permission must be explicit and inheritable; private workspaces cannot contribute to shared intelligence by accident. The system may reason about documented professional behavior and authorized material, but must not present speculative psychological profiling, private thoughts, or unauthorized acquisition as evidence.

## Proposed local-first implementation direction

The following is a starting hypothesis for a small prototype, not a selected stack:

| Layer | Candidate | Why it is plausible | What remains open |
| --- | --- | --- | --- |
| Service boundary | Python modular monolith, potentially FastAPI | Fast iteration and explicit contracts | language/runtime and API shape |
| Canonical ledger | PostgreSQL | transactional records, temporal/accountability modeling | bitemporal design and scale |
| Raw archive | local/object storage | source preservation and reproducibility | retention and encryption model |
| Semantic retrieval | pgvector or comparable index | simple local co-location | retrieval quality and operational limits |
| Relationship views | typed graph projections from canonical records | avoids premature graph-database lock-in | graph query needs and rebuild cost |
| Workers | explicit jobs/queue | incremental ingestion and evaluation | scheduler and orchestration choice |
| Models | provider-agnostic interfaces | supports controlled comparisons | chosen providers/models and data policy |

The prototype must validate its contracts before any large-scale distributed system, autonomous agent fleet, or model fine-tuning program.

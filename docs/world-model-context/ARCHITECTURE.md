# Architecture and implementation reasoning

Status: proposed mechanisms serving working requirements; no runtime exists yet. Full scope and original identifiers: `reference/ARCHITECTURE_REQUIREMENTS.md`.

## Ground-up structure

| Layer | Capability | Candidate approach and reason | Open question |
|---|---|---|---|
| Acquisition | Authorized heterogeneous sources, preserved originals and metadata | Small connector set, source registry, content hashes, incremental jobs | Sources, licenses, historical depth |
| Extraction | Schema-validated claims, events, entities, relations | Constrained model outputs plus deterministic validation; preserve source spans and parser versions | Models and extraction accuracy |
| Identity/evidence/time/access | Common foundations across every domain | Stable IDs, reversible match records, attributed assertions, temporal versions, access policies | Exact ontology and storage |
| Memory | Shared identity, domain projections, cross-domain links | Rebuildable text/vector/graph/time indexes over canonical evidence | Segmentation, capsules, graph engine |
| Investigation | Plan, retrieve, expand, compare explanations | Bounded durable jobs, hybrid retrieval, explicit support/conflict/missing evidence | Best planner, sufficiency and stopping policy |
| Expert frameworks | Represent and test professional analytical methods | Versioned methods with applicability, inputs, assumptions, failure conditions | Selection/composition advantage |
| Attribution/forecasting | Trace observed paths, investigate explanations, predict outcomes | Separate attribution tasks and explicit forecast contracts | Causal identification and calibration |
| Learning/evaluation | Measure errors and improvements | Historical replay, held-out cases, correction routing, evaluated changes | Learning policy and benchmark choice |
| Monitoring | New evidence triggers scoped research | Watch specifications, novelty/materiality checks, job budgets | Alert quality and operation cost |
| Interfaces | Messaging-first with portable state | Common investigation API and async result IDs; adapters for future channels | Initial channel and authentication |
| Security/operations | Isolation, lineage, reproducible runs, cost controls | Scope enforced before retrieval; inherited restrictions, audit events, model routing | Deployment requirements and isolation tests |

A modular application is the current candidate, not eleven independently deployed services. The point of boundaries is replaceability and testability while keeping early operation inexpensive.

## Candidate canonical contracts

Entity: stable ID, type, aliases, external mappings, resolution evidence and history. Source: origin, provider, license, collection method, access scope, historical availability. Observation: source ID, original reference, content hash, publication/observation/ingestion times, parsing run. Assertion: attributed subject/predicate/object, polarity, modality, qualifiers, validity, epistemic state, evidence and processing run. Event: typed identity, participant roles, status, time, evidence. Relationship: participants, mechanism, direction, context, validity, evidence, epistemic status, permissions. Hypothesis: target, support, conflict, alternatives, missing evidence, revisions, uncertainty, inference provenance.

Contexts, decisions, outcomes, frameworks, investigations, forecasts, jobs, and processing runs complete the contract family. An event reported by a source is not automatically established as having happened. Preserve its evidentiary state. Multi-party transactions need participant roles rather than forced binary links.

Do not equate announced capital commitments with completed cash movement, revenue with financing, possible suppliers with signed contracts, or semantic similarity with transmission or causation.

## Time and identity

Retain event time, validity, publication/availability time, observation time, ingestion/knowledge time, revision time, forecast creation, and resolution. Support both “publicly available by cutoff” and “actually ingested by cutoff” experiments; label which is being run. Later identity merges, summaries, or corrections must not silently rewrite historical snapshots.

Identity matches need candidate generation, evidence for and against, unresolved status, external IDs, and reversible merges. Domain membership is not a unique identity. Private mappings must not be exposed across customers.

## Candidate storage

The earlier technical draft proposes PostgreSQL for structured records, an original-source archive, pgvector for semantics, typed relationship projections, and lightweight workers. This reduces infrastructure count while testing contracts. A dedicated graph or temporal engine may be better; compare against measured historical, permission, multi-hop, correction, and recovery workloads before choosing.

Suggested record groups: sources/observations; entities/aliases/matches; assertions/events/participants/relationships/evidence; hypotheses/frameworks/decisions/outcomes; investigations/steps/forecasts/resolutions; tenants/access policies; jobs/processing runs; optional capsules and dependencies. These are candidate logical groups, not a finalized database schema.

## End-to-end flows

1. **Source → knowledge:** authorize acquisition → retain source and hash → parse/extract candidates → resolve identities → attach evidence/time/scope → update affected projections.
2. **Question → answer:** authenticate and scope → identify entities/time/objective → plan retrieval → assemble evidence across domains → generate alternatives → check contradictions and gaps → answer with sources/uncertainty → persist trace and costs.
3. **New evidence → revision:** identify affected assertions and hypotheses → preserve old states → invalidate dependent representations → reevaluate → notify authorized watchers if warranted.
4. **Historical evaluation:** choose cutoff semantics → reconstruct eligible evidence and derived views → commit forecast/configuration → reveal outcome → score and diagnose errors → test improvement separately.
5. **Expert learning:** acquire a documented method → encode inputs/assumptions/failures → test on historical cases → compare alternatives → retain results and versions.
6. **Private knowledge:** authorize connector and workspace → ingest privately → enforce scopes through retrieval and derivation → investigate → export/correct/delete according to rights and retention.

## Inference and learning discipline

Start shallow, deepen when significance or recurring evidence merits it, and stop on budget, evidence exhaustion, or low expected value. Keep content origin, observed pathway, causal explanation, and outcome contribution as separate tasks. Retrieval should support exact, text, semantic, typed graph, multi-hop, temporal, provenance, permission, analytical, and reranking operations.

Record frameworks and evidence used, material intermediate outputs, tool calls, model/prompt versions, costs, and final conclusions. An inspectable processing trace is required; this does not require exposing a model's private internal chain of thought.

Knowledge updates, corrected extraction, identity matching, retrieval tuning, attribution, framework selection, forecast calibration, and model training are different loops. Capture errors now; train specialized models only after reliable labels and a useful baseline exist. Generated hypotheses are not ground truth.

## Operations and costs

Idempotent content ingestion, durable jobs, partial-failure handling, retries, dead-letter review, schema and processing versioning, dependency invalidation, bounded tool/model calls, and observability are working requirements. Track cost per observation/assertion/relationship/investigation/forecast, storage growth, tokens, latency, and useful evidence coverage.

These details describe how the requirements could be implemented and why. They are reviewable proposals, not claims of novelty or working code.

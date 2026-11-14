# Helios Signal v0.1 — review proposal

> Founder correction: prioritize the general world model, inference, historical reasoning and cross-domain connections. The Monday Brief is an optional application, not the product boundary. See `../../REASONING_ARCHITECTURE.md`. This proposal remains historical where it conflicts with that direction.

**Date:** 2026-11-14 (IST)
**Status:** proposal for founder approval; no repository mutation, commit, push, PR, procurement, or source collection is authorized by this document.

## Purpose and boundaries

Helios Signal is the first commercial application of the Information World Model (IWM): a narrow, evidence-backed developer-community signal product. It must exercise, rather than replace, the shared IWM contracts for source, observation, assertion, entity, event, relationship, hypothesis, investigation, outcome, time, permissions, and cost.

The proposed v0.1 deliverable is a weekly/actionable “Monday Brief”: a short ranked set of customer problems, competitor moves, and unmet needs. Every item exposes its evidence, source/use restriction, reason for rank, alternatives/uncertainty, and a suggested human-reviewed next step. It is not a causal engine, a generic social listening dashboard, an alert feed, or a claim to train third-party models.

## Evidence position

The six attached specialist files are valuable dated research inputs, not acceptance of every vendor, pricing, licence, release, or security claim. Before any dependency/source is pinned, record its exact version/checkpoint, licence (code *and* weights), primary URL, date checked, security review, and the gate below. The public URL `https://github.com/vdnthtml/helios` returned an unauthenticated 404 during this review, so current remote state is **unverified**. Earlier local context reports a baseline commit and a separately preserved feature bundle; this proposal does not treat either as currently reachable from GitHub.

## Architecture proposal

One Python modular monolith plus worker. PostgreSQL is the canonical production ledger; SQLite remains a reference/test adapter; local filesystem then S3-compatible archive is the v0.1 raw-observation store. Postgres has full-text, pgvector and typed relational graph projections. No dedicated graph database, microservice fleet, vector database, causal engine, fine-tuned model, or multi-tenant production launch enters v0.1 without passing its trigger.

```text
permitted source -> replaceable adapter -> versioned observation/archive
  -> deterministic normalization/dedup -> grounded extraction/review
  -> evidence + bitemporal ledger -> lexical/vector/typed-edge projections
  -> candidate signals -> customer-specific transparent ranking
  -> bounded investigation -> action brief -> feedback/outcome/evaluation
```

Non-negotiable contract rules:

- Source material, source-attributed assertion, derived relationship, hypothesis, forecast and outcome are different records.
- Stable entity IDs are generated; names and aliases only produce match candidates. Merges require provenance and reversal.
- Important records are append-only corrections, with valid time and transaction/knowledge time. `as_of(valid_time, knowledge_time)` is a contract, not four decorative columns.
- All retrieval legs apply scope/permission and point-in-time filters before ranking. Derived artifacts retain dependency IDs and become stale when evidence changes.
- An LLM can propose an extraction or hypothesis; it cannot make source truth canonical. Significant output carries source spans and processing version.
- Customer relevance is a separate, recomputable interpretation of shared permitted evidence; it never rewrites the observation.

## Proposed decision set (draft ADRs)

| ADR | Proposal | Why / acceptance trigger |
|---|---|---|
| ADR-001 | Postgres + pgvector is canonical; SQLite is contract-test/reference only. | One transactional evidence store. Adopt exact supported versions only after primary-source and licence verification. |
| ADR-002 | Implement bitemporality in SQL/application contracts: range constraints, append-only corrections, as-of queries, and leakage tests. | Historical replay must be demonstrable. A database choice alone is insufficient. |
| ADR-003 | Typed Postgres edges and bounded recursive traversal; graph engine is a plugin only. | Promote only if a representative 2-hop query misses the agreed latency/operability budget. |
| ADR-004 | Local filesystem for initial archive, S3-compatible boundary thereafter. | Do not set MinIO, SeaweedFS, or any self-hosted object store as a v0.1 default until exact lifecycle/security claims are rechecked. |
| ADR-005 | LinkML-to-Pydantic/JSON Schema/SQL is the proposed contract source of truth. | Pilot a representative schema generation path before committing all models. |
| ADR-006 | Hybrid retrieval: Postgres lexical + embeddings + RRF + reranking, all time/scope constrained. | Must beat lexical-only on a frozen, point-in-time gold set at a stated budget. |
| ADR-007 | Start with a versioned transparent ranking formula, intent taxonomy, and human review. | Learning-to-rank needs sufficient independently labeled pairs and an untouched evaluation set. |
| ADR-008 | PydanticAI/DBOS are replaceable candidates behind `jobs.py`; FastAPI/typed API boundary is proposed. | Durable restart and idempotency tests pass; no framework adoption by reputation. |
| ADR-009 | Authorize official/permitted sources only for product data. | Experimental adapters may be isolated for evaluation with authorized data; never make bypassed access, session cookies, fake accounts, or retention beyond terms a product dependency. |
| ADR-010 | Fine-tune only after a measured task gap and reviewed labels. | Base/prompt/retrieval baselines first; promote only on frozen data with source-fidelity and temporal checks. |

## Ownership and dependency inventory

| Classification | Proposed components | Helios ownership / rule |
|---|---|---|
| Paid when justified | Hosted model calls; official X access; compute/hosting/storage; email; later payments. | Use explicit budgets and provider adapters; prices and terms must be rechecked on purchase day. |
| Official/permitted source interfaces | GitHub API/webhooks, Hacker News API, Bluesky public APIs/Jetstream, RSS/Atom, selected publisher feeds, later GDELT/OpenAlex/EDGAR/GLEIF where terms allow. | Build adapters and a source-rights registry; retain/process/redistribute/train permissions are distinct fields. |
| Direct open-source candidates | PostgreSQL, pgvector, FastAPI, Pydantic, SQLAlchemy/Alembic, spaCy, Splink, DuckDB, PydanticAI, DBOS, FastMCP, DeepEval, PEFT/TRL, llama.cpp/vLLM. | Pin only after primary licence/security verification; keep provider/storage/job interfaces replaceable. |
| Benchmark-only candidates | GLiNER2.5, Qwen3 extraction/embedding/reranking, LangExtract, bge-m3/reranker, LightGBM, NetworkX/rustworkx, Graphiti, XTDB. | No endorsement or inclusion until local benchmark, exact checkpoint licence and hardware fit are recorded. |
| Patterns/code to study, not copy wholesale | Harken normalization, OpenMagpie connector/relevance shape, Lead Signal Listener explainable scoring, Octolens context relevance, SnitchFeed intent taxonomy, Brandwatch/Meltwater explained change. | Reimplement clean-room behavior/contracts; do not copy proprietary code, branding, data, undocumented internal stacks, or claimed results. |
| Build from scratch | Evidence/bitemporal ledger; source-rights registry; identity review/reversal workflow; typed relation semantics; signal/relevance logic; investigation trace; action brief; feedback/outcome/evaluation; access policy and audit trail. | This is the differentiated application layer. It must preserve IWM evidence/time/permission constraints. |
| Fine-tune later | Extraction adapter first; then reranker; planner only after baselines. | Reviewable labels, time/source-family splits, manifest, rollback, and predefined promotion thresholds required. No foundation-model training. |
| Explicitly defer/reject | Dedicated graph DB, GraphRAG dependency, causal claims/engine, automatic private-data linking, OpenFGA/Keycloak, Kafka/Airflow/Temporal, autonomous outreach, production multi-tenancy. | Add only after the measured trigger and a new ADR. |

## Proposed repository documentation tree

```text
helios/
  README.md                         # product boundary, runnable status, quick start
  docs/
    PRODUCT_SCOPE.md                # IWM ↔ Signal boundary, user outcomes, non-goals
    ARCHITECTURE.md                  # modules, contracts, trust boundaries
    DATA_CONTRACTS.md                # observation/assertion/etc.; LinkML generation plan
    TEMPORAL_AND_PROVENANCE.md       # as-of semantics, corrections, leakage controls
    SOURCE_POLICY.md                 # source register, allowed uses, retention, adapter status
    TOOLING_AND_OWNERSHIP.md         # this inventory; licences checked at adoption
    MODEL_AND_TRAINING.md            # routing, benchmark plan, fine-tuning gate
    EVALUATION.md                    # gold set, PIT replay, metrics, promotion gates
    SECURITY.md                      # scopes, tenancy roadmap, threat model, data handling
    PRODUCT_INSIGHTS.md              # competitor-derived patterns and anti-patterns
    ROADMAP_V0_1.md                  # milestones, owners, gates, risks
    RESEARCH_INPUTS.md               # six uploads, provenance and verification limits
    adr/
      0001-canonical-store.md ... 0010-fine-tuning-gate.md
  schemas/
    helios.yaml                      # proposed LinkML source
  apps/api/                          # FastAPI boundary (after M1 approval)
  packages/core/                     # canonical contracts and domain rules
  packages/adapters/                 # source, archive, db, model, jobs adapters
  migrations/                        # Postgres migrations (after M2 approval)
  tests/contract/ tests/integration/ tests/evaluation/
  evals/gold/                        # restricted manifests/labels, never raw restricted content
  infra/                             # local compose/deploy templates only after M2
  .github/workflows/ci.yml           # lint, contract, migration, leakage, eval gates
```

The first documentation-only PR should add `docs/`, ADRs and a dependency/source register, not claim code exists. Move pre-existing documents into this shape only after a file-by-file collision review; preserve history rather than overwrite work.

## Milestone plan and engineering gates

| Milestone | Scope and owner | Exit gate |
|---|---|---|
| M0 — approval and corpus | Founder selects one buyer problem, customer context and permitted seed corpus; engineering records policies. | Written source/retention decision; success metric and budget; no ambiguous data route. |
| M1 — contract foundation | Engineering: LinkML spike; SQLite contract suite; source/observation/assertion/entity/event/relation/hypothesis/forecast records. | Same-name collision, content revision, idempotency, evidence-span, correction, scope and cutoff tests pass. |
| M2 — production-shaped ledger | Engineering: Postgres migration and equivalent adapter; archive boundary; typed edges and as-of queries. | SQL constraints + append-only correction + valid/knowledge-time replay + leakage negative tests pass. |
| M3 — permitted ingestion and review | Engineering/research: one official/permitted source importer, archive, deterministic normalization, review queue. | Reingestion no-op; changed item versions cleanly; deletion/restriction handling documented; sampled extraction has span fidelity. |
| M4 — retrieval and signals | Engineering: lexical/vector hybrid, RRF, reranking experiment, cluster/relevance baseline. | Frozen gold set exists before tuning; retrieval recall, rank quality, cost, latency, source-independence and ANN-vs-exact recall reported. |
| M5 — brief and investigation | Product/engineering: bounded plan, alternatives, evidence trace, human reviewed Monday Brief. | Each brief item links evidence, rank explanation, uncertainty, action; no unsupported-claim test failures. |
| M6 — replay/learning decision | Engineering/research: point-in-time historical replay and forecast/outcome record; feedback capture. | Forecast committed before outcome; Brier/calibration vs baseline; error analysis; no future-evidence leak. |
| M7 — pilot decision | Founder: invited user validation and operating cost review. | Repeated usefulness evidence, source/right fit, support burden and unit economics justify next investment. |

## Acceptance gates and metrics to pre-register

Before benchmark work, freeze a corpus universe, observation cutoff, source-family/time split, label instructions, metric definitions and promotion threshold. Minimum gates:

- Contract: migrations apply; canonical invariants and adapter suite pass.
- Time: every historical query excludes `knowledge_time > cutoff`; deliberately injected future evidence must fail the test.
- Evidence: sampled outputs keep exact evidence references/spans; unsupported material claims are rejected or labeled hypothesis.
- Identity: no automatic name-only merge; candidate/merge/reversal tests pass.
- Retrieval: compare lexical, vector, hybrid and reranked variants on pre-registered recall/nDCG/latency/cost; use time-aware relevance labels.
- Ranking: transparent baseline is versioned; customer feedback never changes shared evidence; LTR cannot promote without enough held-out labeled pairs.
- Safety/governance: source policy and scope filter apply in every retrieval leg; deletion/restriction propagation is tested.
- Operations: idempotent imports, bounded retries, recorded model/checkpoint/prompt/cost; durable recovery before automation.
- Product: a reviewer can explain why a delivered item ranked, what would change it, and what it does not establish.

## Open verification questions and risks

1. **Remote state/access:** authenticate read-only and inspect branch history/files before applying any plan; reconcile the reported baseline/feature bundle with remote state.
2. **Licensing:** audit exact versions, code, checkpoint weights, training data and commercial terms; research uploads flag several non-commercial/source-available/GPL/AGPL/SSPL risks.
3. **Source rights:** official API access does not automatically permit retention, redistribution or training. LinkedIn and non-official X routes are especially unsuitable as a foundation.
4. **Audit freshness:** release dates, vulnerabilities, pricing and competitor claims in the uploads require primary-source recheck at adoption/purchase.
5. **Historical truth:** transaction time is not public availability. Decide and encode both before promising replay fidelity.
6. **Evaluation validity:** gold labels, time splits, source-family deduplication and outcome definition are higher-risk than model selection.
7. **Commercial hypothesis:** the Monday Brief and $57–170 range are hypotheses; buyer willingness and usefulness remain unvalidated.
8. **Operational complexity:** Postgres/RLS/object archive/model runners impose backup, security and compute responsibilities; defer production multi-tenancy until proven necessary.

## Approval requested

Approve, amend, or reject: (a) Helios Signal as the developer-community action-brief wedge, (b) the contract-first/postgres candidate architecture, (c) official/permitted-source-only production policy, (d) the M0 corpus/buyer selection, and (e) the documentation tree/ADRs. Only after approval: inspect authenticated remote state, stage a non-destructive documentation branch, show its diff, then seek separate authorization to commit/push/open a PR.

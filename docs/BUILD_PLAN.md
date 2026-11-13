# Helios: fast architecture and model build plan

Date: 2026-11-14. Status: engineering proposal plus a tested first evidence-contract feature. This advances the founder's current request to start creating the project; the former research-only sequencing is no longer a reason to defer reversible implementation.

## 1. The first useful product loop

Select a bounded public AI-infrastructure ecosystem as a proposed test, initially around 10–20 organizations plus relevant people, publications, transactions, and suppliers. Start with permitted official documents and user-supplied authorized text. The exact seed list remains adjustable to buyer relevance and data availability.

The first end-to-end workflow must do this: ingest a document; extract attributed claims and typed relationships; attach source evidence; connect known entities across contexts; answer a cross-domain question; separate documented paths from hypotheses; reconstruct a historical state; record a forecast; score the outcome; expose mistakes and cost. Build this progressively while retaining the general architecture.

A practical example: a company announces a compute expansion; trace documented financing, suppliers, research, and professional relationships; distinguish confirmed contracts from candidate consequences; state what further evidence would change the explanation. Announcements are not completed transactions and paths are not causal proof.

## 2. Starting architecture

| Responsibility | Proposed starting choice | Reason / adoption condition |
|---|---|---|
| API and contracts | Python + FastAPI + Pydantic | Typed extraction and investigation contracts; quick integration |
| Canonical production ledger | PostgreSQL + SQLAlchemy/Alembic | Evidence, identity, time, source and access records in one transactional foundation |
| Similarity search | pgvector | Keep semantic retrieval alongside evidence; start exact on small data, measure ANN recall when scaling |
| Keyword search | PostgreSQL full-text initially | Cheap baseline; label it correctly as Postgres lexical ranking, not BM25 |
| Relationship graph | Typed relational projections + bounded traversal | Evidence and qualifying states remain inspectable; dedicated graph store only after measured need |
| Source archive | Content-addressed local files, then compatible object storage | Rebuild extraction and indexes from permitted originals |
| Investigations | PydanticAI + DBOS | Typed steps and persisted workflow recovery; model calls/tools must be wrapped correctly |
| Model routing | Provider interface first; LiteLLM where it reduces integration work | Select per task, record model/version/tokens/cost; avoid an extra proxy until needed |
| User interface | Owned web chat, then MCP, then Slack | Common API and evidence-inspection experience; WhatsApp is deferred per Muse's recommendation, without relying on unverified policy claims here |
| Security | Explicit trusted scope initially; authenticated identity + Postgres RLS before multi-user use | Do not confuse a supplied tenant string or successful scope-filter test with production authorization |
| Evaluation | Versioned JSONL cases + tests and scored runs | Start with a small adjudicated gold set; add tracking services after the loop exists |

Only Python's standard library is required by the current feature. Package installation failed due to DNS/network restrictions, so API, Postgres, PydanticAI, DBOS, LiteLLM, and model runners are proposed integrations rather than installed components.

Avoid day-one accumulation of Keycloak, OpenFGA, Kafka, Airflow, Temporal, multiple graph stores, causal engines, and incremental-compute servers. These may become useful, but their adoption must solve a measured requirement. Before private multi-user launch implement real authorization, provider boundaries, restriction inheritance, and isolation tests; complex relationship authorization can then justify OpenFGA.

## 3. What to take from Muse, and what to correct

Muse source: `Pasted text(2).txt`, Library ID `libfile_47bdd5351aa48191b72333cf426e3c60`, 15,796 lines, dated research/scaffold 2026-11-11/12. Reviewed synthesis C1–C12, relevant model/storage/inference sections, and actual scaffold contracts/extraction/resolution. This is not a claim to have audited every repository or every line of that 1.5 MB package.

Adopt the useful direction: evidence ledger, Postgres candidate, strong retrieval baseline, graph traversal only where useful, bounded durable investigation, separate models, and measured fine-tuning. Capsules remain an experiment. Version and licensing claims need primary-source verification at adoption; an evidence tag written by another AI is not independent verification by us.

Concrete issues found by reading the supplied scaffold:

- `Person.id` hashes a normalized name when a strong ID is absent: two different same-name people receive one ID. Use generated stable entity IDs and source-qualified external identifiers instead.
- Resolver `_aliases` records canonical names and `_resolve` returns the alias hit without review: its code contradicts the nearby “name-only matches are never auto-merged” comment. Names/aliases should generate candidates, not authorize a merge.
- `RawItem.payload_sha256` can fall back to URL/title without body: content changes can be missed. Hash complete normalized source content and preserve revisions.
- Claim IDs include observation timestamps: a retry can produce new claims. Design extraction idempotency around observation revision, extractor version, and normalized claim content; this first feature implements observation idempotency, not assertion idempotency.
- Heuristic extraction assigns the author/first resolved entity as a sentence subject: this can confuse reporter, speaker, and real-world subject. Extract attribution roles and evidence spans explicitly.
- The heuristic treats `predicts` as belief and hardcodes confidence 0.4: predictions need their own semantics and probabilities require calibration. These values are not measured accuracy.
- A literal public URL requirement excludes legitimate private document references. Require a resolvable permitted source URI/reference instead.

Graphiti remains a useful comparison candidate. Deprecation of one optional storage backend would not alone prove the whole project unsuitable. Likewise, a narrow forecasting benchmark win cannot establish causation. Do not repeat these research-report shortcuts as settled architecture conclusions.

## 4. Different models for different jobs

| Job | First candidate | What it outputs | Evaluation |
|---|---|---|---|
| Entity mentions | GLiNER, checkpoint/license pinned separately | Mention spans and types | Span precision/recall, ambiguity failures |
| Structured extraction | Qwen3-8B; compare Qwen3-14B as a stronger tier | Schema-valid assertions, speakers/subjects, events, roles, modality/status, evidence spans | Gold extraction F1, evidence fidelity, identity/number/status errors |
| Embeddings | Qwen3-Embedding-0.6B | Versioned document/assertion vectors | Evidence recall at fixed retrieval budget |
| Reranking | Qwen3-Reranker-0.6B | Relevance scores for retrieved candidates | Recall/ranking versus latency and token cost |
| Investigation and hypothesis generation | Qwen3-14B or an approved stronger hosted model through the same interface | Structured plan, alternatives, missing evidence, source-grounded answer | Unsupported claims, cross-domain evidence recall, cost |
| Verification | Schema/identity/time/numeric checks plus a separately evaluated entailment scorer | Support/contradiction/unknown with source links | False support, entity swaps, amount errors, disagreement |
| Forecasting | Base-rate baseline; simple statistical models where suitable; reasoning-assisted probability as a challenger | Frozen target/horizon/probability/resolution contract | Brier/calibration and usefulness against baseline |

These are real verified candidate checkpoints, not claims that they are the newest, best, locally fast enough, or benchmarked on our data. Their cited model cards list Apache-2.0. GLiNER code licensing does not settle each weight checkpoint's license. Hosted API prices, GPU rental, machine RAM, and data budget have not been verified or purchased.

On supported local hardware, test quantized small models via llama.cpp. For a later GPU server, evaluate vLLM. Do not require every developer to host all models simultaneously. Record model revision, quantization, prompts, schema version, and generation settings; compare inference quality under quantization.

A model proposes a relationship; source evidence and checks determine how it may be represented. Neither deterministic validation nor a second LLM can generally prove a source claim true. Disagreement should be visible and unresolved cases should abstain or enter review.

## 5. Building relationships and memory

Canonical IDs are independent of names. Maintain observations, assertions, event participants, relationship types/qualifiers, evidence links, source dependencies, hypotheses, decisions, outcomes, forecasts, processing runs, and access scopes separately. Sources may assert incompatible facts.

Relationship families include employment, authorship, citation, ownership, financing, acquisition, supply, participation, technical dependency, and proposed explanatory links. Financial records retain amount/currency/status/roles; semantic similarity only creates a candidate. Source-dependency links distinguish many repeated reports from independent confirmation.

A relationship projection can group evidence-backed assertions, but must retain the evidence IDs and epistemic state. Shared identities connect logical finance/research/narrative/people contexts; retrieval applies tenant/time/licensing restrictions and then assembles a small query-specific context. No need to permanently assign a person to only one community.

A normal investigation uses a deterministic bounded plan: resolve objective/entities/time; hybrid retrieval; selectively follow typed edges; rerank; generate alternatives; seek contradictions; compose an answer; record missing evidence, stopping reason, tokens/cost, and the evidence trace. Store procedural traces and material outputs, not private internal model chain-of-thought.

New observations invalidate dependent summaries/hypotheses and enqueue only affected work. Start with explicit dependency IDs and stale flags. Advanced ATMS, provenance semirings, learned traversal, and stream-compute engines are possible later experiments, not prerequisites for the first useful answer.

## 6. Fine-tuning plan

Keep changing facts in the ledger. Train task behavior and decision boundaries rather than trying to store the live world in model weights.

1. Use the base models with constrained extraction. Capture predictions, source spans, corrected labels, abstentions, false merges, number/status errors, and failed evidence searches from day one.
2. Build an initial gold set: first 20 carefully reviewed questions/documents, expanding to around 50–100 diverse evaluation cases. These are proposed starting sizes, not sufficient evidence for every accuracy claim.
3. First fine-tuning target: a narrow extraction adapter for actor/subject roles, typed relations, modality, status, source span selection, and abstention. A provisional 500–2,000 adjudicated examples is a learning-curve starting range; do not train solely because a count is reached.
4. Use Hugging Face Transformers + PEFT LoRA/QLoRA and a compatible pinned TRL SFT release. Pilot LoRA first; use QLoRA only on supported training hardware and verify the quantization/training path. Do not assume NVIDIA tooling works on the user's Mac.
5. Deduplicate documents and their syndications; split by time, document/source family, and where appropriate entity/event. Freeze the test set before training; never mix future labels or adjacent versions of a held-out source into training.
6. Compare base model, improved prompt, retrieval-only change, and adapter on the same untouched cases. Promote an adapter only if it yields useful quality/cost gains without regressions in source fidelity, identity, temporal behavior, and unsupported-claim rate. Set thresholds before running.
7. Second target: tune a reranker using adjudicated relevant/irrelevant evidence pairs, especially hard negatives. Later: learn a bounded planning/escalation policy from traces if it outperforms the deterministic policy.
8. Retain base model + adapter + training data manifest + evaluation report and rollback reference. Capture corrections continuously; training/deployment is an evaluated batch process.

Teacher-generated examples may help propose labels, but require permitted use and review. Model agreement, hypotheses, and user corrections do not automatically become truth labels. Do not train a foundation model or GNN before a baseline shows a specific task it improves.

## 7. First ten working days

These are targeted slices, not a guaranteed schedule. End each day with a runnable increment, tests, and one branch/PR where access permits.

| Day | Deliverable | Observable completion |
|---|---|---|
| 1 | Evidence and identity contracts | Same-name, content-change, source quote, correction, cutoff and scope tests pass (first reference feature completed) |
| 2 | Postgres repository adapter + schema migration; Pydantic request models | Reference contract suite passes on both adapters; relational constraints and restricted queries checked |
| 3 | One permitted real source importer + original archive | Reingestion is a no-op; changed source creates a new observation; real source trace inspectable |
| 4 | Structured extraction + review queue | Pinned model tested on first reviewed examples; actor/status/amount/span errors recorded |
| 5 | Keyword/vector retrieval + reranking | Same evidence queries scored with retrieval and cost instrumentation |
| 6 | Typed cross-domain paths + evidence dependencies | Paths expose supporting sources, independent origins, and uncertainty |
| 7 | Bounded investigation + web chat | A user gets an async answer with citations, alternatives and missing information |
| 8 | Durable restart + corrections + time/scope tests | Interrupted job resumes safely; retraction invalidates dependent artifacts; future evidence excluded |
| 9 | Forecast/outcome contracts + first replay/prospective records | Predictions committed before reveal; scores and misses retained |
| 10 | Baseline comparison and usable demo | Full question-set report, actual cost/latency, failure examples, next buyer-relevant feature |

The working loop can be demonstrated early; model learning claims require more evidence than a ten-day sprint. Fine-tuning follows the measured gap and dataset, not a calendar deadline.

## 8. Daily collaboration and shipping

Muse: bounded fresh-source/repository verification, corpus/source rights research, seed discovery, benchmark candidates, and reproducible task packets with exact URLs and dates. Its output must include evidence and proposed code changes, not just conclusions. A specialist does not need to redesign the entire stack every day.

Implementation agent: inspect latest repo, choose the next small dependency-ready slice, implement, test, update decisions, commit on a feature branch, and push/open a reviewable PR when authentication is available. The user requested daily features/changes; do not create empty commits merely to keep a streak. Failed tests or authentication errors are reported explicitly. Never force-push or overwrite another agent's in-progress branch.

Founder: select/adjust the first paid workflow, provide permitted introductions/data where needed, review behavior on real questions, and adjudicate domain-sensitive examples. Technical work should continue while nonblocking business questions are answered.

Daily acceptance: working behavior; meaningful checks; measured model/retrieval impact where relevant; reproducible run instructions; source/license/version evidence; clear next task. Main remains the known-good line; changes go through feature branches and CI.

## 9. First feature: exact scope and limitations

Implemented `helios/evidence.py` with a SQLite reference adapter and immutable record objects: stable entity IDs, scoped external IDs, content hashes including body, idempotent observations, evidence-quoted assertions, source-asserted states, modality and transaction status, valid-time filters, actual-ingestion cutoff queries, and append-only correction operations. Assertions preserve full correction history and source references. Eighteen synthetic-fixture tests passed locally on the available Python interpreter. GitHub Actions is configured for Python 3.11/3.12/3.13 but has not run remotely.

The contract API uses append-only operations, but direct database tampering is not prevented. It is a development library, not an authenticated service. No claim of Postgres equivalence, database RLS, public-availability replay, semantic entailment validation, complete bitemporality, license enforcement, extraction idempotency, reversible identity merge workflow, concurrent-worker safety, or model integration is made. Literal source quotation is traceability only: it does not validate an asserted status or prove truth.

## 10. Primary-source checks used in this proposal

Checked by retrieval on 2026-11-14; docs/model cards, not local performance benchmarks. Pin exact adopted release/checkpoint revisions during integration.

- PostgreSQL vector retrieval and filtered ANN behavior: https://github.com/pgvector/pgvector
- Durable agent integration and I/O wrapping: https://pydantic.dev/docs/ai/capabilities/durable_execution/dbos/
- Provider routing: https://github.com/BerriAI/litellm
- Entity extraction library: https://github.com/urchade/GLiNER
- Qwen extraction/reasoning candidates: https://huggingface.co/Qwen/Qwen3-8B and https://huggingface.co/Qwen/Qwen3-14B
- Embedding and reranking candidates: https://huggingface.co/Qwen/Qwen3-Embedding-0.6B and https://huggingface.co/Qwen/Qwen3-Reranker-0.6B
- Local inference candidate: https://github.com/ggml-org/llama.cpp
- Fine-tuning: https://github.com/huggingface/peft and https://huggingface.co/docs/trl/main/en/sft_trainer
- Graph comparison candidate: https://github.com/getzep/graphiti

These checks do not adopt all maintenance claims, security advisories, API quotas, pricing, legal interpretations, or novelty assertions in Muse's package. Those remain independently verifiable claims.

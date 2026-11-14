# Decision register

Version 0.1.0 · baseline recorded 2026-11-14. Source line numbers refer to the supplied transcript. Status `direction` preserves the founder's intent; `working requirement` reflects the latest assistant-produced reference scope; neither implies implemented behavior.

| ID | Status | Decision or position | Why / evidence |
|---|---|---|---|
| D-001 | direction | Build a general relational information world model | Latest scope 7603–7640; founder correction 3994–4025 |
| D-002 | direction | No universal priority among people, narratives, economics, organizations, and technology | Explicit correction described at 3994–4025 |
| D-003 | direction | Segmented but connected memory; context selected per question | 4157–4208; direct initial answers 1–36 |
| D-004 | direction | Demonstrate historical prediction, evaluation, and learning from mistakes | Direct initial answers 1–36; 4461–4517; 9693–9776 |
| D-005 | direction | Start with a small useful, commercially relevant ecosystem | Direct initial answers 1–36; 4834–4920; ecosystem not selected |
| D-006 | direction | Preserve uncertain observations without upgrading them to facts | Direct initial answers 1–36; 4598–4622 |
| D-007 | direction | Begin shallow investigation; deepen when recurring or relevant | Direct initial answers 1–36; 4343–4371 |
| D-008 | direction | Study published methods, interviews, and expert cases | Direct initial answers 1–36; 4372–4460 |
| D-009 | direction | Portable project state outside any one AI provider | 5059–5103; current user instruction |
| D-010 | direction | Messaging first; broader channels on a shared service | 4687–4833; latest 9225–9392 |
| D-011 | direction | Private information stays within authorized scopes; contributions explicit | Direct initial answers 1–36; 4623–4655; latest 9083–9147 |
| D-012 | direction | Keep behavioral and professional decision research in scope | 3834–3893; avoid replacing it with fixed personality labels |
| D-013 | direction | Private technical core, selective collaborators, credible public research | 4921–5010 |
| D-014 | working requirement | Preserve separate observations, assertions, events, relationships, hypotheses, and evidence | 7696–8050; exact ontology is open |
| D-015 | working requirement | Time, permissions, source independence, corrections, and cost tracking are foundational | 8226–8400; 9083–9147; 9455–9506 |
| D-016 | direction | Research and independent technical criticism precede a finalized implementation packet | 10156–10167; current task organizes context rather than authorizing a whole product build |
| D-017 | documentation decision | Latest explicit founder direction wins; keep raw and historical records | Current user instruction |
| D-018 | direction | Use the Helios GitHub repository as the canonical v0 architecture repository for implementation-facing documentation and technical decisions; retain the broader portable bundle as research context | Founder request, 2026-11-14; repository inspection found an empty default branch, so this session establishes its initial documented baseline |
| P-001 | proposed | Python/FastAPI/PostgreSQL/pgvector/object archive/typed graph projections/modular monolith | 9507–9573 and earlier technical drafts; alternatives may replace these |
| P-002 | proposed | Evidence capsules as compressed, evidence-linked context | 8401–8465; research hypothesis, not invention or dependency |
| P-003 | proposed | AI infrastructure ecosystem as initial test | 1095–1131; 2972–3049; not selected |
| P-004 | proposed | Specific framework, confidence, routing, and model algorithms | Must be compared experimentally, not inherited as facts |
| L-001 | future option | Enterprise meeting capture and selective wearables | 9393–9454; consent, retention, ownership unresolved |
| H-001 | historical / not adopted | Publicly obtained personal information is categorically never removable | Early founder answer 1–36; latest reference 9083–9147 requires applicable rights and retention handling |

## Unresolved decisions

Exact ontology; canonical and graph storage; temporal implementation; identity algorithms; evidence scoring; partitioning; capsule utility; retrieval and hypothesis evaluation; causal methods; framework selection; forecasting; fine-tuning; model providers; orchestration; monitoring; production infrastructure; source licenses; initial customer; pricing. See source 10017–10065 and `OPEN_QUESTIONS.md`.

## Add or supersede a decision

Record ID, date, status, decision, alternatives, rationale, source/evidence, owner or authority, affected requirements/files, superseded IDs, and verification required. Append history; do not silently rewrite accepted intent. Agent recommendations become proposals until the appropriate founder or delegated decision authority accepts them.

## 2026-11-14 — Build authorization and candidate stack

- D-019 — Current founder direction: propose a concrete architecture/model/fine-tuning plan and start creating useful features quickly, targeting daily Git changes. Supersedes D-016's research-before-implementation sequence as a reason to defer reversible coding; source: current user instruction.
- P-005 — Engineering proposal: Python/FastAPI/Pydantic, canonical Postgres with pgvector, typed relational graph projections, PydanticAI/DBOS, task-specific models and adapter fine-tuning after a measured gap. Candidate checkpoints and primary URLs are recorded in BUILD_PLAN.md; no local inference benchmark has run.
- P-006 — Founder-review proposal: Helios Signal v0.1 is a narrow evidence-backed developer-community action-brief application built on, not instead of, IWM contracts. It proposes Postgres/pgvector, bitemporal enforcement, typed relational projections, a replaceable source/model/job boundary and official/permitted sources only for product use. All six specialist audits remain dated inputs pending primary verification. Source: `context/proposals/HELIOS_SIGNAL_V0_1_PROPOSAL.md`; no approval or implementation implied.
- I-001 — Implemented: dependency-free SQLite reference evidence/identity ledger with 18 passing contract tests, branch feat/evidence-foundation, commit 3b2c776. Production DB/API/security/model integration remains future work.
- O-016 — Shipping blocker: GitHub/PyPI DNS failures and absent GitHub CLI authentication. No scheduled push configured. Portable Git bundle is the current verified code checkpoint.
## 14 Nov 2026 — Helios v3 approved baseline

- Helios v3 is APPROVED as the architectural baseline (conditional approval; see docs/STATUS_AND_DECISIONS.md). Broad redesign is stopped. The 18 ledger tests (I-001, SQLite ledger) and all source history above are preserved unchanged; no duplicate registry is created.
- Proposed technologies are CANDIDATES until verified: do not mark GLiNER2.5, Qwen3-8B, bge-m3, pgvector, or any other proposed technology as implemented or pinned until verified. Only the SQLite evidence/identity ledger is Implemented (18 contract tests, 0 inference tests, no gold set, no Postgres).

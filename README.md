# Helios

> **Version 0 — Architecture Foundation. No product implementation exists in this repository yet.**

Helios is an evidence-backed, temporal Information World Model: a proposed foundation for connecting documented information about people, ideas, narratives, organizations, economic activity, technologies, decisions, events, and outcomes.

It is not a generic chatbot, a claim that Helios already has world-scale knowledge, or proof of predictive superiority. Version 0 records the product direction, engineering constraints, open research questions, and the contracts a future implementation must respect.

## Why this exists

The hypothesis behind Helios is that an intelligence system can be more useful when it preserves source evidence, identity uncertainty, time, access boundaries, and competing explanations—rather than flattening documents into an answer or treating a graph edge as fact. The system should support investigation and forecasting that can be replayed, inspected, and evaluated against later outcomes.

The ambition is cross-domain. No domain is structurally privileged: a question may connect a publication, a person, an organization, a decision, an economic event, and a later outcome. A first product must be much narrower and measurable.

## Read this first

| If you are… | Start with |
| --- | --- |
| A founder or collaborator | [Architecture](docs/ARCHITECTURE.md) then [Roadmap](docs/ROADMAP.md) |
| An engineer | [Architecture](docs/ARCHITECTURE.md), [Status & decisions](docs/STATUS_AND_DECISIONS.md), then [Contributing](docs/CONTRIBUTING.md) |
| A research or coding agent | [Handoff](docs/HANDOFF.md) |
| Reviewing what is actually decided | [Status & decisions](docs/STATUS_AND_DECISIONS.md) |

## Version-0 status

| Category | Status |
| --- | --- |
| Product runtime, database, schemas, APIs, ingestion, evaluation | **Not implemented** |
| Architecture, requirements, and operating constraints | **Documented for review** |
| Python / FastAPI / PostgreSQL / pgvector / object storage / graph projections | **Proposed local-first stack; not selected** |
| Evidence capsules, inference algorithms, model providers, first market | **Research questions; not validated** |

## Architecture at a glance

```text
Authorized sources
  -> immutable source observations
  -> extracted candidate entities / assertions / events / relationships
  -> identity + temporal evidence ledger + permissions
  -> segmented memory and retrievable graph/index projections
  -> bounded investigation + expert frameworks + competing hypotheses
  -> attributable findings / forecasts / interfaces
  -> outcomes, corrections, replay, evaluation, controlled improvement
```

The canonical records are the source-preserving observation and evidence ledger. Indexes, graph projections, summaries, and capsules are derived artifacts: they must retain lineage and be rebuildable.

## Non-negotiable design principles

- **Observation is not assertion; assertion is not inference; inference is not causation.**
- **Time is first-class.** Preserve event/valid time, publication time, ingestion time, and knowledge/revision time where relevant.
- **Evidence stays inspectable.** Derived output must carry source links, versions, and uncertainty.
- **Memory is segmented yet connected.** Retrieval should activate relevant contexts, not blindly load everything.
- **Identity resolution is reversible.** Similar names or embeddings do not prove the same entity.
- **Privacy, licensing, and permissions propagate.** Private or restricted inputs never become shared by implication.
- **Learning is measured, not assumed.** Historical replay and prospective forecasts must avoid future-data leakage.
- **Investigation is cost-bounded.** The system starts shallow and deepens only with justified relevance or evidence.

## What comes next

The immediate goal is not to build every component. It is to choose one authorized, dense historical corpus; define minimal contracts; and demonstrate end-to-end extraction, evidence tracing, point-in-time replay, a committed forecast, outcome scoring, and visible error analysis.

See the [phased roadmap](docs/ROADMAP.md) and the [agent/engineer handoff](docs/HANDOFF.md).

## Repository conventions

- Keep durable architecture decisions in `docs/STATUS_AND_DECISIONS.md`.
- Record an implementation-affecting decision before treating it as settled.
- Keep raw source observations separate from extracted claims and generated conclusions.
- Do not commit credentials, private corpus content, or licensed material without explicit authorization.
- Update the relevant docs and decision log with meaningful architectural changes.

## License

No license has been selected. Do not assume reuse or redistribution rights until one is added by the project owner.

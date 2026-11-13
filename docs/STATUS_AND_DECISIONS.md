# Status and decision log

## Status vocabulary

- **Direction** — explicit founder intent; it guides work but does not prove implementation.
- **Working requirement** — capability the architecture should accommodate; exact design may remain open.
- **Proposal** — an option to test, not a chosen solution.
- **Research question** — an unresolved claim needing evidence or experiment.
- **Implemented** — only use after code, verification, and location are recorded.

## Current status

Helios v0 is documentation only. There is no runtime, database, ingestion connector, schema, model integration, evaluation run, pilot, or validated commercial claim in this repository.

## Direction and working requirements

| ID | Status | Position |
| --- | --- | --- |
| D-001 | Direction | Build a general, relational information world model; do not reduce it to one pilot domain. |
| D-002 | Direction | Treat people, narratives, economics, organizations, and technology as connected dimensions without a universal hierarchy. |
| D-003 | Direction | Use segmented but connected memory selected by question and permissions. |
| D-004 | Direction | Demonstrate historical replay, forecast scoring, and visible learning from error. |
| D-005 | Direction | Start with a small, useful, commercially relevant ecosystem; the ecosystem and buyer remain unselected. |
| D-006 | Direction | Preserve uncertainty; do not promote an observation or repeated wording into fact. |
| D-007 | Direction | Begin investigations shallowly and deepen only when evidence/relevance justifies cost. |
| D-008 | Direction | Study and test expert frameworks and cases rather than hard-code unexamined expertise. |
| D-009 | Direction | Use a messaging-first interaction initially; expose broader interfaces through common contracts later. |
| D-010 | Direction | Keep private data in explicit authorized scopes; contribution to shared intelligence is opt-in. |
| R-001 | Working requirement | Preserve observations, assertions, events, relationships, hypotheses, forecasts, outcomes, and evidence as distinct objects. |
| R-002 | Working requirement | Make time, provenance, source independence, corrections, permissions, and investigation cost foundational. |

## Proposals, not commitments

| ID | Proposal | Decision needed |
| --- | --- | --- |
| P-001 | Python/FastAPI modular monolith with PostgreSQL, vector search, object archive, and graph projections | Compare with viable alternatives against the MVP contract. |
| P-002 | Evidence capsules for compressed, evidence-linked context | Measure quality/cost against direct and graph-assisted retrieval. |
| P-003 | AI infrastructure as first ecosystem | Validate buyer, source rights, density, and measurable outcomes. |
| P-004 | Particular confidence, routing, attribution, and model algorithms | Define baselines and experiments before adoption. |

## Open decisions

Canonical ontology and schema; storage and graph strategy; bitemporal semantics; identity resolution and reversal; source licensing; access/retention policies; segmentation/capsule utility; retrieval and hypothesis evaluation; attribution/causal methods; expert-framework selection; forecasting protocol; model providers; deployment/monitoring; initial customer and pricing.

## How to add a decision

Append rather than silently rewrite. Include date, status, decision, alternatives, rationale/evidence, authority, affected files/contracts, superseded records, and required verification. A proposal becomes selected only through an explicit decision with evidence appropriate to its risk.

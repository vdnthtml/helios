# Technical co-founder architecture review

Source: `context/sources/conversation-2026-11-14.txt`, lines 1491–3632.
Status: preserved conversation extract; assistant-authored proposals are not independently verified findings or automatically accepted decisions. Original dates and claims are preserved as history.

---


INFORMATION WORLD MODEL
Technical Architecture, Research Proposal & Engineering Review
Version: 0.1 — Technical Review Draft
Date: November 11, 2026
Status: Pre-implementation; architecture and research hypotheses, not a validated system
Intended reader: Technical co-founder / systems architect

1. Executive Technical Summary
We propose building a continuously evolving Information World Model (IWM): a system that represents observable relationships among people, information, organizations, economic activity, decisions, and events, and uses those relationships to reconstruct developments, investigate possible causes, and forecast outcomes.

The fundamental research hypothesis is:

A temporally structured, evidence-grounded, cross-domain information model can produce more useful inferences than conventional retrieval, isolated knowledge graphs, or unstructured LLM reasoning, while controlling retrieval and inference costs.

The project is not primarily a chatbot, financial terminal, social listening tool, or generic GraphRAG implementation.

It is an attempt to develop a reusable information representation, memory, and inference architecture from which multiple intelligence applications can be built.

The system should:

Ingest structured and unstructured information from multiple authorized sources.

Extract entities, claims, events, interactions, decisions, and relationships.

Resolve identities and preserve source-level provenance.

Organize information into interconnected, context-specific memory structures.

Discover and investigate relationships across different domains.

Distinguish directly observed connections from inferred or causal hypotheses.

Apply documented expert analytical frameworks where appropriate.

Reconstruct historical information states without future-data leakage.

Generate measurable predictions and compare them against outcomes.

Update its knowledge and inference processes as new information arrives.

Operate through a common API, initially exposed through a messaging-style interface.

Support private enterprise knowledge without mixing confidential customer information into shared intelligence.

The first implementation must prove the architecture on a small, dense, cross-domain historical dataset, not attempt internet-scale knowledge acquisition.

2. Why This Architecture Is Different
Most existing systems specialize in particular information tasks.

System category	Primary capability	Limitation relevant to our research
Conventional RAG	Retrieve documents to answer questions	Weak explicit temporal and relational modeling
Knowledge graphs	Represent entities and relationships	Often need additional machinery for provenance, uncertainty, and changing evidence
GraphRAG	Use graph structure to improve retrieval	Does not inherently solve causal attribution or outcome-based learning
Temporal context graphs	Preserve changing relationships and history	Do not automatically supply our intended cross-domain economic and human decision inference
Market intelligence	Analyze companies, transactions, and markets	Coverage and reasoning vary by provider
Narrative intelligence	Analyze information diffusion, actors, and communities	Not necessarily integrated with financial events, professional decisions, and private business context
General-purpose LLMs	Flexible language reasoning	Knowledge may be stale, incomplete, or difficult to verify independently
Several existing systems already implement substantial parts of our proposed architecture.

This is not an assertion that none of these capabilities exist.

Our proposed technical differentiation is the integration of source-level evidence, temporal relationships, adaptive context construction, explicit hypothesis tracking, expert reasoning methods, and empirical outcome evaluation.

The key question is whether that integration creates a measurable improvement.

That must be demonstrated experimentally.

3. Foundational Architectural Principles
3.1 Relationship-native rather than domain-native
The system should not privilege financial, social, organizational, or informational data as its fundamental unit.

Instead, it must support distinct types of relationships among heterogeneous objects.

A company investing in a supplier, an executive citing a publication, a researcher introducing an idea, and a product gaining adoption are different events.

Their relationships may become meaningful when investigated together.

We therefore need a shared information representation capable of expressing different relationship mechanisms without flattening them into generic, ambiguous edges.

3.2 Observation is not explanation
The system needs three independent epistemic categories.

Observation: What was recorded by a source.

Assertion: What that source claims or what an extraction system interprets it as saying.

Inference: What the system hypothesizes based on the available evidence.

An observation can be authentic while the underlying claim is false.

An inference can be plausible without being causally established.

These distinctions must be enforced in storage, retrieval, and response generation.

3.3 Time is foundational
Every significant observation, event, assertion, and relationship should support temporal reasoning.

At minimum, distinguish:

Event or valid time.

Publication time.

Ingestion time.

System knowledge time.

Revision or invalidation time.

The system must support point-in-time queries.

For example:

"What would the system have concluded on January 1, 2024, using only information available then?"

This is necessary for meaningful historical evaluation.

3.4 Evidence must remain reconstructable
No derived relationship, summary, hypothesis, or answer should become an independent source of truth without a traceable evidence chain.

Derived information should retain source identifiers, processing versions, and dependency information.

Graph projections and compressed summaries should be rebuildable.

3.5 Information access must be context-dependent
The system will eventually possess multiple information environments.

They may have different data models, index structures, permissions, update frequencies, and retention requirements.

A query should activate the relevant environments rather than process the entire network.

3.6 Learning and knowledge updating are different
The system can continuously incorporate new evidence without continuously retraining a foundation model.

Knowledge updates, inference-policy changes, statistical model updates, and neural fine-tuning should be separately controlled and evaluated.

4. Proposed High-Level Architecture
We propose a modular architecture divided into five functional systems.

A. Observation System
Responsible for information ingestion, source management, extraction, and normalization.

B. World Memory System
Responsible for identity, evidence, events, relationships, time, segmentation, and retrieval.

C. Inference System
Responsible for investigation planning, relationship discovery, hypothesis evaluation, and attribution.

D. Learning and Evaluation System
Responsible for historical replay, feedback, model evaluation, forecasting, and improving system behavior.

E. Product and Integration System
Responsible for user interaction, agent execution, messaging, APIs, private workspaces, and monitoring.

End-to-end pipeline
Information sources

↓ Source connectors and authorization

Raw evidence store

↓ Parsing and extraction

Entity resolution + event normalization

↓ Evidence registration

Temporal assertion and relationship ledger

↓ Domain projections and memory segmentation

Context retrieval and query planning

↓ Expert-framework selection and investigation

Hypothesis generation + evidence evaluation

↓ Historical comparison and forecasting

Response / monitoring / decision support

↓ Outcomes and corrections

Learning and evaluation feedback

The process is not strictly linear.

New evidence should update affected portions of memory and trigger relevant investigations.

An answer may also cause the system to discover missing information and initiate additional retrieval.

5. Core Ontology and Data Contracts
I recommend separating the canonical evidence schema from domain-specific extensions.

This avoids prematurely hardcoding assumptions about every industry.

5.1 Entity
Represents a persistent identifiable object.

Possible types:

Person.

Organization.

Product.

Technology.

Publication.

Concept.

Community.

Asset.

Location.

Institution.

Suggested fields:

Field	Purpose
entity_id	Internal stable identifier
entity_type	Entity classification
canonical_name	Preferred display name
aliases	Alternative names
external_identifiers	Registry IDs or source-specific references
identity_status	Resolved, provisional, disputed
created_at	First internal creation
updated_at	Latest metadata update
scope_id	Applicable data boundary
Important: an entity ID is an identity key, not proof that two records refer to the same real-world entity.

5.2 Observation
Represents information obtained from a particular source.

Suggested fields:

observation_id

source_id

source_record_id

content_hash

source_uri

content_reference

published_at

observed_at

ingested_at

content_type

language

license_policy

access_scope

extraction_status

Original source material should be stored separately from extracted assertions.

Identical-content detection should use content hashes where appropriate, but duplicate content from separate sources may still be relevant to propagation analysis.

5.3 Assertion
Represents a claim made by a source.

Example:

"Company A announced a $500 million investment in Company B."

Suggested fields:

assertion_id

subject_entity_id

predicate

object_entity_id or structured value

qualifiers

claiming_source_id

modality

polarity

valid_time

recorded_at

epistemic_status

extractor_version

Modality distinguishes statements such as:

Will invest.

Intends to invest.

Announced an investment.

Has invested.

Completed an investment.

These must not be treated as equivalent.

5.4 Event
Events should be first-class objects rather than only graph edges.

Examples include:

Acquisition.

Investment.

Conversation.

Publication.

Hiring.

Partnership.

Product release.

Contract award.

Regulatory decision.

An event may have multiple participants with different roles.

Example:

Event: Investment announcement
Participant A: Announcing investor
Participant B: Intended recipient
Amount: $500 million
Status: Announced commitment
Date: Publication date
Evidence: Original announcement

Later evidence of actual payment should produce a separate event or state transition.

This is important for money-trail analysis.

5.5 Relationship
A typed connection between two or more entities, assertions, events, or concepts.

Proposed relationship families:

Family	Examples
Organizational	employed_by, founded, owns, advises
Financial	invested_in, acquired, supplied, contracted_with
Informational	cited, referenced, responded_to, contradicted
Participatory	attended, collaborated, contributed_to
Semantic	supports, contradicts, resembles
Temporal	preceded, overlapped, superseded
Hypothetical	may_have_influenced, possible_dependency
Every relationship should specify:

Relationship type.

Participating object IDs.

Evidence IDs.

Temporal validity.

Epistemic status.

Provenance.

Processing version.

Applicable permissions.

The first implementation should favor typed relationship tables and event-participant records over a completely unrestricted property graph.

5.6 Hypothesis
Represents a proposed explanation.

Example:

"Public discussion of Technology X contributed to Company A's decision to acquire Company B."

Suggested fields:

hypothesis_id

statement

target_event_ids

supporting_evidence_ids

contradicting_evidence_ids

alternative_hypothesis_ids

missing_evidence_requirements

evaluation_method

uncertainty_estimate

status

created_at

last_evaluated_at

model_version

Hypotheses should be independently addressable, revisable, and comparable.

5.7 Decision, Framework, and Outcome
These should also be first-class concepts.

Decision: Documented choice by an actor or organization.

Framework: Analytical method used to investigate a problem.

Outcome: Observable result that follows a decision or predicted event.

The system should be capable of linking decisions to reported considerations and later outcomes without assuming a complete causal explanation.

6. Entity Resolution
This is a major technical risk.

A large information network becomes unreliable if the system merges distinct people or organizations.

I propose a staged entity-resolution pipeline.

Stage 1 — Exact identification
Match authoritative identifiers when available.

Examples include legal entity identifiers, company registration numbers, stable public account identifiers, and known document IDs.

Stage 2 — Candidate generation
For unidentified entities, retrieve possible matches using:

Names and aliases.

Organizations.

Document context.

Geographic context where relevant.

Professional roles.

Stable source identifiers.

Semantic representations.

Stage 3 — Candidate scoring
Evaluate evidence for and against each match.

Contextual similarity should not override contradictory identity evidence.

Stage 4 — Resolution
Possible outcomes:

Match existing entity.

Create new entity.

Retain unresolved candidate identities.

Refer ambiguous cases for review.

Stage 5 — Reversibility
Identity merges must preserve the original source identities and merge history.

A mistaken merge should be reversible.

This is especially important because false identity connections can create many downstream relationships.

Technical recommendation: Store source-specific identity mappings separately from canonical entity records. Treat identity reconciliation as a versioned process rather than permanently rewriting all historical references.

7. Evidence and Provenance Architecture
I recommend a provenance system based on explicit dependency records.

Every derived object should answer:

Which original observations support it?

Which transformation created it?

Which model and prompt version were used?

Which other derived objects did it depend on?

What evidence contradicts it?

Can it be reconstructed?

The result is a provenance dependency graph separate from the semantic world graph.

That distinction matters.

A semantic connection such as "Company A supplies Company B" is different from the computational connection "Assertion 103 was generated from Source 55 by Extractor v2."

Both graphs are necessary.

Proposed evidence states
Observed.

Extracted.

Proposed.

Supported.

Disputed.

Superseded.

Retracted.

Not every status transition should be automatic.

Evidence can strengthen an assertion without establishing causality.

Source independence
The system must distinguish:

Independent corroboration: Separate sources with independently obtained evidence.

Dependent repetition: Multiple sources repeating one original source.

A claim repeated 500 times may be highly prominent without being independently corroborated.

For narrative intelligence, all 500 repetitions may be relevant.

For factual verification, they may contribute little independent evidence.

Prominence, reliability, and corroboration must therefore be stored separately.

Provenance standards
We should investigate W3C PROV-O as a conceptual foundation for provenance relationships and OpenLineage for tracking data-processing jobs.

Neither should replace our domain-specific evidence semantics.

8. Temporal Memory and Historical Reconstruction
We need a bitemporal or stronger event-time/knowledge-time model.

For each important fact or relationship, distinguish:

Valid time: When the fact applied in the world.

Knowledge time: When the system had access to that information.

For example:

An investment occurred in January.

A public filing disclosed it in March.

Our system ingested the filing in April.

A historical query simulating February must not use that April-ingested record as knowledge available in February.

This remains true even if the event itself occurred in January.

Implementation implications
Preserve source publication timestamps.

Preserve ingestion timestamps.

Store revisions rather than overwriting history.

Support as_of queries.

Maintain provenance for historical states.

Prevent future information from leaking through summaries and embeddings.

Version inference outputs and predictions.

This becomes the foundation for historical backtesting.

Incremental updates
When new evidence arrives:

Identify affected entities, claims, and events.

Update canonical records.

Re-evaluate dependent relationships.

Invalidate affected derived summaries.

Refresh affected indexes and graph projections.

Reassess impacted hypotheses.

Trigger relevant monitoring or evaluation jobs.

We should avoid rebuilding the entire information model after every new observation.

9. Memory Segmentation
This is one of the primary proprietary research areas.

The central problem is:

How can we preserve broad interconnected information while retrieving only the relevant portion needed for a specific investigation?

We need to distinguish logical segmentation from physical database sharding.

Initially, I propose logical partitions based on:

Domain.

Entity.

Event.

Time window.

Information source.

Customer or permission scope.

Contextual relevance.

These dimensions can overlap.

An observation about an executive discussing an investment should be accessible through relevant financial, organizational, and information-network contexts.

It should not be duplicated as three independent facts.

Shared identity spine
Maintain one canonical identity system with source-specific mappings.

Domain projections can reference the same canonical entity without duplicating its identity.

Evidence capsules
I propose experimenting with a derived structure called an evidence capsule.

A capsule contains:

Relevant entity references.

Related observations.

Assertions and events.

Typed relationships.

Temporal range.

Summary representation.

Source dependencies.

Permission labels.

Cross-links to related capsules.

Model and construction version.

Capsules are materialized views, not the authoritative source of truth.

We should compare several capsule-construction strategies:

Entity-centered: Information associated with a particular entity.

Event-centered: Information surrounding a particular event.

Domain-centered: Information associated with a topic or industry.

Community-centered: Related information discovered through graph structure.

Dynamic: Context assembled for a specific query.

It is not yet established which is superior.

Research problem
The segmentation system should optimize:

Retrieval relevance.

Evidence coverage.

Cross-domain recall.

Latency.

Token usage.

Index-maintenance cost.

Historical correctness.

The risk is that aggressive segmentation will suppress weak but important cross-domain connections.

We need to benchmark that explicitly.

10. Query Planning and Context Routing
The inference engine should not immediately send the user's question to an LLM with a large collection of retrieved documents.

Instead, it should construct an investigation plan.

Example query
"Investigate how a major AI infrastructure development connects relevant executives, suppliers, capital commitments, and public technical discussions."

The query planner should:

Classify the question.

Resolve named entities.

Determine the relevant time window.

Identify required evidence types.

Select applicable domain indexes.

Retrieve initial evidence.

Identify unresolved connections.

Decide whether further investigation is justified.

Apply suitable analytical frameworks.

Produce a source-grounded conclusion.

Retrieval methods
The system should support a combination of:

Exact identifier retrieval.

Full-text search.

Vector similarity.

Typed graph traversal.

Temporal filtering.

Structured analytical queries.

Evidence-strength filtering.

Cross-domain expansion.

Adaptive investigation depth
We should not use a fixed traversal depth for all questions.

A simple factual query might need one or two retrieval operations.

A cross-domain attribution investigation may require several rounds.

I propose a bounded expansion policy using:

Expected information value, unresolved uncertainty, relevance, significance, and computational cost.

The system should stop expanding when additional retrieval is unlikely to materially change the answer or when the authorized investigation budget is exhausted.

This is a research hypothesis, not an established optimal algorithm.

11. Inference Engine Design
I recommend separating inference into specialized operations rather than building a single unrestricted autonomous agent.

11.1 Extraction
Identify entities, claims, events, references, and relationships from source material.

Use constrained structured outputs and schema validation.

11.2 Relationship discovery
Detect possible connections from:

Explicit references.

Shared entities.

Chronological sequences.

Common events.

Repeated information patterns.

Documented organizational or financial links.

Semantic similarity.

Semantic similarity alone must never establish a causal relationship.

11.3 Hypothesis generation
Construct alternative explanations for relevant observations.

11.4 Hypothesis evaluation
Retrieve supporting and contradicting evidence.

Evaluate assumptions and known confounding factors.

11.5 Attribution analysis
Separate:

Source attribution.

Information-pathway attribution.

Causal attribution.

Outcome attribution.

11.6 Consequence analysis
Investigate plausible second-order effects and dependencies.

For example:

A company announces a major infrastructure investment.

The system can inspect documented supplier relationships, technical capacity requirements, financing arrangements, and related industry developments.

It can identify possible downstream effects.

It must distinguish confirmed contracts from inferred opportunities.

11.7 Response generation
Generate a conclusion containing:

Answer.

Supporting evidence.

Relevant relationships.

Alternative explanations.

Uncertainty.

Missing information.

Possible next developments.

The final response should be independently traceable to the underlying investigation record.

12. Human Decision-Making and Expert Frameworks
The original motivation for the system involves understanding how people encounter information, form interpretations, make decisions, and influence others.

We need to preserve that research direction.

However, the technically defensible approach is to model observable professional behavior and explicitly shared decision criteria, rather than asserting hidden psychological states.

Individual decision records
Each decision can contain:

Actor or organization.

Decision context.

Available documented information.

Explicitly stated criteria.

Relevant external conditions.

Decision outcome.

Historical follow-up.

Evolving decision-pattern representations
The system can investigate recurring professional patterns across documented decisions.

These representations should be contextual and tentative.

They should not become permanent personality labels.

Expert Framework Registry
We should study:

Venture investors.

Corporate strategy professionals.

Management consultants.

Economists.

Quantitative researchers.

Security analysts.

Narrative researchers.

Experienced operators.

A framework record should include:

Framework identifier.

Professional domain.

Applicable problem types.

Required evidence.

Analytical steps.

Assumptions.

Failure conditions.

Expected outputs.

Sources.

Evaluation history.

Framework-selection engine
Given a question, the system selects one or more frameworks.

Example:

An acquisition investigation might use:

Corporate strategy: Strategic rationale and organizational incentives.

Financial analysis: Transaction structure and capital consequences.

Information diffusion: Relevant observable information pathways.

Historical analysis: Similar documented cases and outcomes.

The system should not assume that combining more frameworks always improves the answer.

Framework selection must be experimentally evaluated.

13. Forecasting and Learning
This is a major requirement of the initial prototype.

The system must be able to make predictions using historical information and subsequently evaluate them.

Prediction record
A forecast should include:

Forecast ID.

Question.

Target event.

Prediction timestamp.

Evidence cutoff.

Prediction horizon.

Predicted outcome or distribution.

Confidence or probability.

Supporting information.

Inference method.

Model version.

Resolution criteria.

Final observed result.

A prediction should be committed before its outcome becomes known.

Historical replay
For a selected historical case:

Establish a cutoff date.

Exclude later information from retrieval and derived context.

Run the investigation.

Store the prediction.

Reveal subsequent outcomes.

Score the prediction.

Record failures and missing evidence.

Compare against baseline methods.

Metrics
For categorical predictions:

Accuracy.

Precision and recall where appropriate.

Calibration.

Brier score for probability forecasts.

For quantitative predictions:

MAE or RMSE.

Error distribution.

Calibration intervals.

Relative improvement over simple baselines.

For historical relationship prediction:

Link-prediction metrics where appropriate.

Relationship precision.

False-positive rate.

Evidence support.

For the full intelligence system:

Answer correctness.

Evidence recall.

Attribution quality.

Cost per investigation.

Latency.

User utility.

The objective is measurable improvement, not a promise that every prediction becomes more accurate than the previous one.

Learning loops
I recommend separating:

Knowledge updating.

Entity-resolution improvement.

Retrieval optimization.

Extraction-model improvement.

Attribution-model improvement.

Forecast calibration.

Framework-selection improvement.

Fine-tuning should only begin when there is a validated dataset, an appropriate baseline, and evidence that training would improve performance.

14. Training Strategy
We do not need a new foundation model at the start.

Initially, use existing models as interchangeable components.

Proposed model responsibilities
Model/component	Responsibility
Structured extractor	Entities, events, assertions
Embedding model	Semantic indexing
Entity matcher	Candidate identity resolution
Reranker	Evidence relevance
Hypothesis generator	Possible explanatory relationships
Evidence evaluator	Supporting and contradicting information
Forecasting component	Time-dependent predictions
Response model	Grounded natural-language answers
Some responsibilities may initially share one LLM.

Others should be deterministic or statistical.

Proposed progression
Stage 1: Existing LLMs with schema-constrained outputs.

Stage 2: Benchmark extraction and retrieval quality.

Stage 3: Collect corrected examples.

Stage 4: Fine-tune specialized models where justified.

Stage 5: Experiment with temporal graph learning or other specialized inference architectures.

Stage 6: Compare improvements against cost, latency, and maintainability.

The proprietary asset may ultimately be the complete inference procedure and validated information representations rather than one large model checkpoint.

15. Initial Storage Architecture
I recommend beginning with a modular monolith.

PostgreSQL
Canonical structured records:

Entities.

Identity mappings.

Observations.

Assertions.

Events.

Event participants.

Relationships.

Evidence links.

Hypotheses.

Forecasts.

Permissions.

Investigation history.

Object storage
Original permitted source documents and attachments.

pgvector
Semantic embeddings for source passages, assertions, and selected memory representations.

Typed graph projections
Graph traversal implemented initially through relational tables and graph-analysis libraries.

Background workers
Incremental ingestion, extraction, reindexing, monitoring, and evaluation.

Cache
Reusable retrieval results and derived context, invalidated when underlying evidence changes.

Important design decision
PostgreSQL should initially be the canonical structured store. The graph should be a derived representation.

This is not necessarily the optimal final implementation.

It is a practical starting hypothesis that reduces infrastructure complexity and preserves control over the underlying evidence contracts.

A dedicated graph database should be introduced when measured query workloads justify it.

16. Proposed Database Tables
The first schema could include:

Table	Purpose
sources	Source metadata and permissions
observations	Raw evidence references
entities	Canonical entity registry
entity_aliases	Source-specific names and identifiers
entity_matches	Candidate resolutions and merge history
assertions	Source-attributed claims
events	Historical events
event_participants	Participants and event roles
relationships	Typed connections
relationship_evidence	Supporting and conflicting evidence
hypotheses	Proposed explanations
hypothesis_evidence	Evidence attached to hypotheses
frameworks	Expert analytical methods
decisions	Documented decisions
outcomes	Observed results
capsules	Derived memory partitions
capsule_members	References from capsules to evidence
investigations	Research sessions
investigation_steps	Query plans and executed steps
forecasts	Predictions
forecast_resolutions	Actual outcomes and scoring
processing_runs	Model and pipeline lineage
tenants	Customer boundaries
access_policies	Authorization rules
jobs	Background processing state
Exact normalization and indexing decisions remain open.

A serious schema review should test constraints, key design, temporal queries, referential integrity, and scalability before implementation.

17. Incremental Processing Architecture
The system must not process every document through every model each time information changes.

Proposed pipeline:

Source discovered

→ Create ingestion job.

Content fetched

→ Compute content hash and check for existing records.

New or changed content

→ Register observation and provenance.

Extraction

→ Generate structured candidate entities, events, and assertions.

Resolution

→ Match identities and connect evidence.

Memory update

→ Update affected graph projections and capsule dependencies.

Hypothesis impact analysis

→ Identify existing hypotheses affected by new evidence.

Selective reevaluation

→ Recompute only affected inference outputs.

Notification

→ Trigger alerts when a monitored condition is satisfied.

Engineering requirements
Idempotent ingestion.

Durable job state.

Retry policies.

Dead-letter handling.

Versioned processing.

Duplicate detection.

Dependency tracking.

Reprocessing support.

Audit logs.

Explicit processing budgets.

A workflow engine such as Temporal or an agent runtime such as LangGraph may be useful later.

The initial system should avoid adopting a complex orchestration framework without a concrete need.

18. Source Acquisition Strategy
The architecture should support different information categories, but actual ingestion must remain permission-aware.

Initial candidate sources
Economic and organizational

SEC EDGAR, GLEIF, government spending records, company announcements, public filings.

Research and technical

OpenAlex, research publications, official technology documentation, patents where accessible.

Public information propagation

Permitted social-platform data, public citations, interviews, authorized transcripts, publications.

Private customer context

Explicitly connected documents, company records, meetings, and research.

Expert research

Authorized interviews, case studies, published methodologies.

Acquisition strategy
We should not indiscriminately collect everything.

Instead:

Select a historical test ecosystem.

Identify required evidence classes.

Acquire a small, sufficiently interconnected corpus.

Evaluate whether missing evidence prevents useful conclusions.

Add sources only where they materially improve evaluation.

Information priority
Use different scores for:

Relevance.

Novelty.

Source independence.

Verification value.

Historical significance.

Economic or organizational significance.

Retrieval and processing cost.

Rumors and unverified claims may be retained as observations.

Their existence and spread may be analytically useful.

They should not automatically become verified factual premises.

19. Security and Data Isolation
The eventual enterprise product will contain highly sensitive information.

Security cannot be added only after we sign customers.

Required principles
Tenant isolation

Private customer records must remain isolated.

Authorization-first retrieval

Permission constraints must apply before evidence is passed to retrieval or generation components.

Derived-data restrictions

A generated conclusion must not reveal protected information indirectly.

Encryption

Encryption in transit and at rest as a baseline.

Auditability

Record meaningful data access, changes, exports, and external actions.

Scoped connectors

External integrations should receive only the permissions necessary for their tasks.

Deletion and correction

Support authorized removal and correction through dependent indexes and derived artifacts.

Model-provider boundaries

Customer information must not be sent to third-party inference services without appropriate authorization and contractual protection.

Prompt-injection resistance

Retrieved documents and tool outputs are untrusted data, not instructions.

Customer-private versus shared intelligence
The architecture should support:

Shared public or licensed intelligence.

Private customer intelligence.

Explicitly approved shared contributions.

These environments may use common schemas and algorithms without sharing underlying confidential records.

For highly sensitive customers, private deployment or stronger customer-controlled key-management models can be considered.

20. Product Interface and Agent Capabilities
The initial user experience should be messaging-first.

The core system must remain independent of the interface.

Common intelligence API
Proposed operations:

investigate(question, scope, as_of)

resolve_entity(query, scope)

trace_relationship(start, target, constraints)

get_evidence(assertion_id)

compare_history(subject, period_a, period_b)

get_hypotheses(subject)

create_monitor(subject, conditions)

list_forecasts(scope)

submit_research(record)

get_investigation_status(job_id)

These are proposed application contracts, not final REST signatures.

Initial product flow
User submits a question.

Backend creates an investigation.

The investigation planner identifies required contexts.

Relevant information is retrieved.

The inference pipeline evaluates relationships and explanations.

The final answer is stored with an investigation ID.

The user receives a response with evidence and optional follow-up investigation.

Long-running work should be represented by durable jobs rather than holding an HTTP request indefinitely.

Future integrations
WhatsApp Business messaging.

Slack.

MCP.

CLI.

Enterprise APIs.

Authorized Gmail and calendar integrations.

Private company document systems.

Optional meeting-recording interfaces.

External actions such as sending messages or modifying company systems require explicit authorization and appropriate approval controls.

21. Monitoring and Autonomous Investigation
Monitoring should not consist of repeatedly asking a large LLM to summarize all newly published information.

Proposed design:

Watch specifications
Each monitored subject defines:

Entities or concepts.

Relevant sources.

Time window.

Event or relationship types.

Notification conditions.

Processing budget.

Access scope.

Monitoring pipeline
New data arrives.

The system identifies relevant watch specifications.

It evaluates novelty and material changes.

If a threshold is met, it performs a bounded investigation.

The investigation may update existing hypotheses.

An alert is produced only if the result satisfies configured significance and evidentiary rules.

Investigation escalation
A weak new signal receives limited processing.

A recurring signal can receive additional investigation.

A consequential unresolved claim can be flagged for researcher review.

We should avoid requiring researchers to manually approve ordinary data updates.

22. First Prototype: Required Demonstration
The prototype must test the architecture, not simply produce an impressive interface.

Proposed test environment
A selected historical technology ecosystem containing:

Publicly documented people and organizations.

Technical publications.

Important events.

Organizational decisions.

Investment and supplier relationships.

Historical changes.

Observable subsequent outcomes.

AI infrastructure is one candidate, but the final selection should consider data accessibility and buyer demand.

Minimum prototype capabilities
Capability A — Information extraction

Ingest a small heterogeneous corpus and extract useful structured information.

Capability B — Segmentation

Organize it into multiple connected contexts.

Capability C — Cross-domain investigation

Answer questions that require connecting information across several contexts.

Capability D — Evidence-backed attribution

Distinguish documented connections from hypotheses.

Capability E — Historical replay

Reconstruct what could have been known at a chosen date.

Capability F — Forecasting

Make a measurable prediction using only prior information.

Capability G — Feedback

Record actual outcomes and show what the system got wrong.

Capability H — Messaging interface

Allow a user to perform the investigation through a simple conversational client.

Non-negotiable demonstration
We should be able to show:

What information entered the system.

How it was structured.

Which contexts were selected.

What relationships were discovered.

Which hypotheses were proposed.

Why those hypotheses were supported or rejected.

What prediction was generated.

What happened afterward.

How the system measured and recorded its error.

Without this, we have an AI research assistant, not evidence of a learning information world model.

23. Evaluation Framework
The proposed architecture must be compared with simpler alternatives.

Baseline 1 — Hybrid RAG
Keyword and semantic search plus an LLM.

Baseline 2 — Standard GraphRAG
Graph-based retrieval using existing implementations.

Candidate 3 — Proposed IWM
Temporal evidence ledger, segmented memory, adaptive retrieval, hypothesis evaluation, and feedback.

Evaluation dimensions
Dimension	Metric
Extraction	Precision, recall, structured-output validity
Entity resolution	False merges, missed merges
Retrieval	Recall@k, ranking quality, evidence coverage
Attribution	Supported-path accuracy, false causal claims
Temporal reasoning	Historical correctness, future-data leakage
Forecasting	Calibration and predictive error
Efficiency	Cost, latency, memory usage
Learning	Improvement over fixed baselines
End-to-end utility	Human evaluation on realistic investigations
Experimental controls
All candidates should receive the same permitted corpus.

Use the same historical cutoff.

Record model versions and prompts.

Evaluate using held-out cases.

Include negative examples where apparent relationships are coincidental.

Avoid judging the system solely through LLM-based scoring.

Use expert-reviewed reference cases where necessary.

24. Resource and Cost Architecture
The current project is unfunded.

The first system should run on a local development machine with minimal external spending.

Initial cost categories
Data acquisition.

Document parsing.

Embeddings.

LLM inference.

Database and storage.

Background processing.

Evaluation.

Human review.

Messaging/API delivery.

Cost controls
Incremental ingestion: Process new material rather than repeatedly processing the same documents.

Model routing: Use simpler models for straightforward tasks.

Caching: Cache stable derived results with dependency-based invalidation.

Scoped retrieval: Limit expensive searches to relevant contexts.

Investigation budgets: Bound autonomous expansions.

Deferred processing: Run costly enrichment only when needed.

Selective source expansion: Acquire additional data where it is expected to improve an investigation.

Metrics to record from the beginning
Cost per ingested source.

Cost per extracted assertion.

Cost per accepted relationship.

Cost per investigation.

Tokens per investigation.

Retrieval latency.

Evidence coverage.

Cost per correctly resolved historical question.

Cost per useful prediction or insight.

Do not optimize only for lower token usage.

The relevant objective is useful, verifiable intelligence per unit of cost.

25. Suggested Initial Stack
Layer	Proposed technology	Reason
Language	Python	NLP, data processing, ML, backend ecosystem
API	FastAPI	Lightweight typed Python service
Database	PostgreSQL	Strong structured consistency and flexible querying
Vector search	pgvector	Avoid separate vector infrastructure initially
Source storage	Local filesystem or S3-compatible storage	Preserve permitted original evidence
Graph	Typed relational graph representation	Maintain explicit control over semantics
Graph experimentation	NetworkX	Research and analysis
Data validation	Pydantic / JSON Schema	Strict model outputs
Inference	Replaceable LLM adapters	Vendor independence
Workers	Simple persistent queue	Asynchronous processing
Frontend	Minimal messaging client	Test experience without building a large dashboard
Testing	pytest + custom evaluations	Reproducibility
Deployment	Local Docker Compose	Simple initial environment
Important alternatives to evaluate
Graphiti: Existing temporal context graph construction, provenance, and hybrid retrieval.

Microsoft GraphRAG: Existing graph-based indexing and local/global retrieval.

Neo4j / FalkorDB / other graph engines: Dedicated graph traversal and graph-management capabilities.

LangGraph: Agent state and controlled reasoning workflows.

Temporal: Durable long-running workflows and retries.

Dedicated search engines: Potentially necessary if full-text and vector retrieval requirements exceed PostgreSQL's practical limits.

Build-versus-buy principle
Use existing open-source infrastructure unless replacing it creates a measurable technical advantage.

Avoid spending engineering effort recreating solved infrastructure.

Reserve original research for context construction, inference, attribution, learning, and cross-domain reasoning.

26. Recommended Code Architecture
The repository should initially use a modular monolith.

Proposed logical structure:

core/identity — Canonical identities and resolution.

core/ontology — Shared schemas and domain extensions.

core/temporal — Time semantics and historical querying.

core/evidence — Assertions, provenance, support, contradiction.

core/permissions — Tenant and access policies.

ingestion/connectors — Source adapters.

ingestion/extraction — Structured information processing.

memory/graph — Relationships and traversal.

memory/indexes — Semantic and keyword retrieval.

memory/capsules — Derived contextual memory.

inference/planner — Investigation planning.

inference/hypotheses — Explanation generation and testing.

inference/frameworks — Expert analytical methods.

inference/attribution — Source, pathway, and causal analysis.

learning/forecasts — Predictions and resolutions.

learning/evaluation — Benchmarks and regression tests.

agents/monitoring — Watchlists and change detection.

interfaces/api — Core service API.

interfaces/messaging — Initial conversational interface.

interfaces/mcp — Future agent interoperability.

workspace/research — Founder and expert research records.

Module boundaries should be enforced through stable interfaces.

Storage implementations should be replaceable without redefining the ontology.

27. Development Sequence
I recommend engineering in dependency order.

Phase 0 — Architecture verification
Formalize the data contracts and identify any fundamental contradictions.

Outputs:

Ontology specification.

Temporal semantics.

Evidence-state definitions.

Permission model.

Evaluation design.

Sample source records.

Representative queries.

Phase 1 — Minimal information pipeline
Implement:

Source ingestion.

Raw evidence registration.

Structured extraction.

Basic entity resolution.

Assertions and events.

Source-backed retrieval.

Exit criterion: reconstruct structured information accurately from a small real dataset.

Phase 2 — Relationship and memory system
Implement:

Typed relationships.

Temporal records.

Domain projections.

Cross-domain retrieval.

Rebuildable derived context.

Exit criterion: answer multi-source, cross-domain questions with inspectable evidence.

Phase 3 — Inference
Implement:

Investigation planning.

Hypothesis generation.

Alternative explanations.

Evidence evaluation.

Bounded investigation expansion.

Exit criterion: produce useful explanations without treating weak connections as established causes.

Phase 4 — Historical learning
Implement:

Point-in-time replay.

Prediction records.

Outcome resolution.

Evaluation metrics.

Error inspection.

Exit criterion: demonstrate reproducible historical tests and compare performance with baselines.

Phase 5 — Product demonstration
Implement:

Messaging interface.

Investigation history.

Evidence inspection.

Bounded monitoring.

User feedback.

Exit criterion: an external evaluator can investigate a real question without accessing internal engineering tools.

Phase 6 — Commercial validation
Demonstrate the system to selected researchers and prospective paying customers.

Identify the first use case with credible willingness to pay.

Only then decide which specialized product should be productionized.

28. Critical Technical Risks
These are the areas where we specifically want an experienced engineer to challenge our assumptions.

Risk 1 — Inference may not improve with graph complexity
Adding graph structure does not guarantee better reasoning.

A simpler retrieval pipeline may outperform the proposed architecture on many questions.

Required test: Controlled comparison against hybrid RAG and GraphRAG.

Risk 2 — Ground truth for attribution is scarce
Historical observation does not reveal every information exposure or private decision process.

Required mitigation: Separate factual and causal claims. Use direct evidence, explicit alternative hypotheses, and calibrated uncertainty.

Risk 3 — Entity-resolution mistakes compound
One incorrect merge may generate hundreds of false connections.

Required mitigation: Conservative resolution, reversible merges, identity confidence, and downstream dependency tracking.

Risk 4 — Context segmentation may lose important information
Selective retrieval could miss weak but valuable cross-domain links.

Required test: Compare adaptive partitions against unsegmented retrieval and broader graph search.

Risk 5 — Source quality may dominate model quality
A sophisticated inference engine cannot reliably reconstruct unavailable events.

Required mitigation: Track evidence coverage and acknowledge unresolved gaps.

Risk 6 — Model-generated relationships can become self-reinforcing
If generated hypotheses are treated as source evidence, the model may amplify its own errors.

Required mitigation: Strict separation between original observations, derived assertions, and hypotheses.

Risk 7 — Historical evaluations can leak future information
Later publications, current summaries, or revised indexes may contain knowledge unavailable at the target date.

Required mitigation: Knowledge-time filtering throughout retrieval, summarization, and forecast generation.

Risk 8 — Continuous enrichment may become expensive
Unbounded extraction, relationship discovery, and autonomous investigations could produce high recurring compute costs.

Required mitigation: Incremental processing, relevance gating, caching, bounded exploration, and cost observability.

Risk 9 — Private information can leak through derived outputs
A cross-domain model could accidentally reveal confidential customer information through summaries or relationships.

Required mitigation: Authorization-aware derivation, access-scope propagation, and tenant-isolation testing.

Risk 10 — The proprietary architecture may not be novel
Many proposed components already exist individually.

Required mitigation: Define specific technical claims and compare their measured performance against established systems.

Risk 11 — The first prototype may overreach
Attempting to implement the complete long-term vision could prevent us from validating any core hypothesis.

Required mitigation: A small but structurally representative test environment.

Risk 12 — A useful system may still lack a customer
Technical performance does not establish willingness to pay.

Required mitigation: Customer discovery and paid pilot discussions in parallel with engineering.

29. What We Want the Technical Reviewer to Challenge
We do not want agreement for the sake of agreement.

We want an independent assessment of whether this architecture is technically coherent and where it should change.

A. Data and ontology
Are the proposed foundational objects sufficient?

Which distinctions are redundant or poorly defined?

Should events, assertions, and relationships be modeled differently?

What is the best approach for multi-party relationships?

How should uncertainty and temporal validity be represented without excessive complexity?

B. Graph and storage
Is PostgreSQL an appropriate canonical store?

Should a graph database be introduced immediately?

Does separating canonical evidence from graph projections create unnecessary duplication?

How should identity resolution and reversible merges work?

How should evidence dependencies and incremental invalidation be implemented?

C. Memory architecture
Are evidence capsules technically useful or just another form of materialized summaries?

Is our segmentation strategy likely to improve retrieval?

How should relevant cross-domain information be discovered without exhaustive traversal?

What indexing and caching approach is most appropriate?

Which existing systems already solve these problems adequately?

D. Inference and learning
Which inference steps should be deterministic, statistical, or LLM-based?

What practical approaches exist for hypothesis evaluation?

How should causal uncertainty be represented?

Can expert frameworks be selected and tested automatically?

Is there a realistic path from historical evidence to predictive improvement?

What is the smallest meaningful experiment that could prove or disprove the core research thesis?

E. Engineering and scale
Which components should be built versus reused?

Is a modular monolith the correct starting architecture?

What are the likely performance bottlenecks?

How should background processing, indexing, and monitoring scale?

What would be the estimated infrastructure and inference costs at prototype and early production scale?

F. Security and commercial feasibility
Does the architecture sufficiently isolate enterprise information?

What security controls must exist before handling real customer data?

Which initial customer use case is technically and commercially most plausible?

What should be removed, redesigned, or deferred before implementation?

30. The Review Output We Want
Please return the assessment in the following format.

1. Architectural verdict
Is the overall system technically coherent?

Where does the design make unjustified assumptions?

2. Critical flaws
Rank the most consequential problems by severity.

3. Proposed corrections
Provide specific architectural fixes, not only general suggestions.

4. Technology recommendations
Identify existing open-source frameworks, databases, and research implementations worth evaluating.

5. Simplified MVP design
Propose the smallest system that can demonstrate the core information, inference, and historical-learning hypothesis.

6. Evaluation design
Specify experiments capable of falsifying the central assumptions.

7. Engineering estimates
Provide realistic effort, complexity, infrastructure cost, and staffing requirements.

8. Revised architecture
Suggest the architecture you would personally build, including why it is preferable.

9. Hardest unsolved problem
Identify the part of the system that requires genuine research rather than ordinary software engineering.

10. Go / no-go assessment
What evidence should we require before committing additional time or capital?

31. Final Technical Thesis
We are proposing an evidence-native, temporal, relationship-oriented intelligence architecture capable of representing and investigating developments across heterogeneous information environments.

The system combines:

Structured source observations.

Canonical entity resolution.

Temporal events and typed relationships.

Provenance and epistemic state.

Segmented, cross-domain memory.

Adaptive retrieval and investigation.

Explicit hypothesis and attribution tracking.

Expert analytical frameworks.

Historical reconstruction.

Forecasting and outcome-based evaluation.

Continuous, bounded learning.

Secure and portable interfaces.

The objective is not simply to generate better prose from retrieved documents.

It is to create a system that can reconstruct how information and real-world events relate, explain what the evidence supports, identify what remains uncertain, and improve its analytical usefulness through measured feedback.

The central technical question:

Can this architecture produce measurably better cross-domain explanations, historical reconstructions, and forecasts than simpler systems at an economically acceptable cost?

That is the question we need the first prototype—and this technical review—to answer.

Appendix A — Reference Technologies
These are research references, not mandatory dependencies.

Graphiti — Temporal context graphs
https://github.com/getzep/graphiti

Microsoft GraphRAG — Graph indexing and retrieval
https://github.com/microsoft/graphrag

pgvector — PostgreSQL vector indexing
https://github.com/pgvector/pgvector

NetworkX — Graph algorithms
https://networkx.org/

LangGraph — Agent workflow orchestration
https://github.com/langchain-ai/langgraph

Temporal — Durable execution
https://docs.temporal.io/

W3C PROV-O — Provenance modeling
https://www.w3.org/TR/prov-o/

OpenLineage — Processing lineage
https://openlineage.io/

Temporal Graph Benchmark — Temporal graph evaluation
https://tgb.complexdatalab.com/

Microsoft GraphRAG research and documentation
https://microsoft.github.io/graphrag/

Model Context Protocol
https://modelcontextprotocol.io/

Appendix B — Example Data Sources
SEC EDGAR
https://www.sec.gov/search-filings/edgar-application-programming-interfaces

GLEIF Legal Entity Data
https://www.gleif.org/en/lei-data/gleif-api

USAspending
https://api.usaspending.gov/

OpenAlex
https://openalex.org/

Bluesky AT Protocol
https://docs.bsky.app/

These sources vary in coverage, access conditions, licensing, and permitted commercial use.

End of technical review draft v0.1.

What I specifically want him to examine first
There are four decisions in this memo that I would not want Codex—or any other implementation agent—to make independently.

1. Canonical storage: Is PostgreSQL with graph projections the correct starting point, or would a temporal graph engine reduce enough engineering complexity to justify using it immediately? Graphiti already supports temporal relationships, provenance, and incremental graph construction, but requires surrounding application services for tenancy and authorization. 

GitHub

2. Segmented memory: Does the proposed evidence-capsule mechanism actually offer an advantage over existing hybrid retrieval? Microsoft GraphRAG already supports local, global, basic, and DRIFT retrieval, so we need a measurable distinction. 

GraphRAG
+1

3. Inference quality: How do we establish that the system is finding meaningful relationships rather than plausible connections? Existing temporal-retrieval benchmarks expose how challenging historically complete evidence retrieval remains. 

ACL Anthology

4. The learning loop: What can improve automatically through new evidence, what requires evaluated model updates, and what can be measured with reliable historical outcomes? The Temporal Graph Benchmark is a useful reference for part of this problem, though it does not evaluate the entire proposed system. 

Temporal Graph Benchmark

One additional issue deserves a direct challenge: our proposed architecture may be too broad for the first implementation even if each component is individually reasonable. I want him to tell us which three components create the essential technical experiment, which existing implementations to reuse, and which components to eliminate until the experiment succeeds.

The most useful response from him would be a revised design with explicit reasons, a realistic build estimate, and a list of assumptions that can be disproved. That will give us something substantially stronger to hand to Codex than an ambitious architecture alone.

for now i need somehting off you now, we are on the right direction

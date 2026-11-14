# Complete architecture requirements register

Source: `context/sources/conversation-2026-11-14.txt`, lines 7590–10169.
Status: preserved conversation extract; assistant-authored proposals are not independently verified findings or automatically accepted decisions. Original dates and claims are preserved as history.

---

Document 2 — Complete Architecture Requirements Register
This is the companion specification. It defines the complete set of capabilities the architecture needs to accommodate, including those we will not implement immediately.

The research AI should use it to identify technical approaches and evaluate whether existing systems satisfy our requirements.

INFORMATION WORLD MODEL
Complete Architecture Requirements & Capability Register
Version: 1.0 — Research Reference Architecture
Date: November 11, 2026
Purpose: Define the complete technical scope, required capabilities, system interactions, data contracts, research problems, evaluation criteria, and future expansion needs for the Information World Model.

Status: Requirements established; implementation choices and proprietary research claims remain subject to evaluation.

1. SYSTEM MISSION
Build an evolving information infrastructure capable of representing and investigating complex relationships across:

People.

Information.

Narratives.

Conversations.

Organizations.

Money and economic activity.

Technologies.

Industries.

Communities.

Decisions.

Historical events.

Outcomes.

Other relevant real-world contexts.

The system must preserve differences between relationship types while allowing them to interact.

It should use evidence and historical information to generate explanations, identify emerging developments, and evaluate predictions.

It should learn from new information and previous mistakes.

The goal is a generalizable information architecture with specialized, measurable intelligence capabilities.

Not a universal model that claims perfect knowledge.

2. REQUIREMENT PRIORITIES
Every major requirement should have one of four states.

State	Meaning
M0 — Core prototype	Must be exercised in the first functional demonstration
F — Foundational	Must be accommodated in the architecture, even if initially simplified
L — Long-term	Important for later commercial or technical expansion
R — Research	Requires comparative experimentation before final selection
An M0 requirement can be implemented minimally.

An F requirement does not necessarily require a complete implementation immediately.

R requirements must not be presented as solved.

3. SYSTEM-LEVEL ARCHITECTURE
The proposed system is organized into the following functional components.

Component 1 — Source and Information Acquisition
Collects authorized information and preserves source context.

Component 2 — Extraction and Normalization
Converts source information into structured candidate entities, events, claims, and relationships.

Component 3 — Identity, Evidence, and Temporal Foundation
Maintains canonical identities, provenance, assertions, temporal history, and permissions.

Component 4 — Segmented World Memory
Maintains graph structures, domain projections, semantic indexes, contextual summaries, and cross-domain connections.

Component 5 — Investigation and Inference Engine
Plans investigations, retrieves evidence, constructs hypotheses, and evaluates relationships.

Component 6 — Expert Framework Engine
Represents and applies professional analytical methodologies.

Component 7 — Attribution and Prediction Engine
Investigates information pathways, explanatory mechanisms, potential consequences, and forecasts.

Component 8 — Learning and Evaluation Engine
Compares predictions against outcomes and improves evaluated system components.

Component 9 — Autonomous Monitoring
Watches relevant developments and triggers bounded investigations.

Component 10 — Interfaces and Applications
Exposes intelligence through messaging, APIs, CLI, MCP, and enterprise integrations.

Component 11 — Security and Governance
Controls access, licensing, private information boundaries, auditability, and permitted actions.

These components are logical modules.

They do not require separate physical services.

4. CANONICAL INFORMATION OBJECTS
The architecture needs a common representation that different information domains can extend.

4.1 Entity
Represents a persistent identifiable object.

Required capabilities:

Stable identity.

Entity type.

Canonical name.

Aliases.

Source-specific identifiers.

Identity confidence or resolution status.

Historical metadata.

Relationship references.

Domain memberships.

Access boundaries.

Candidate types include:

Person, Organization, Institution, Product, Technology, Concept, Publication, Community, Asset, Location, Project, and Research Subject.

Priority: M0

4.2 Source
Represents an information provider or origin.

Required fields:

Source ID.

Source type.

Publisher or provider.

Original location.

License and usage permissions.

Reliability-related metadata.

Access restrictions.

Update frequency.

Collection method.

Historical availability.

Priority: M0

4.3 Observation
Represents source material collected at a specific point.

Examples:

Filing.

Public statement.

Article.

Video metadata.

Transcript.

Meeting note.

Structured dataset record.

Required fields:

Observation ID.

Source ID.

Original content reference.

Content hash.

Publication timestamp.

Observation timestamp.

Ingestion timestamp.

Content type.

Access scope.

Parsing version.

Extraction status.

Priority: M0

4.4 Assertion
Represents a statement about the world.

Required capabilities:

Subject.

Predicate.

Object or structured value.

Source attribution.

Qualifiers.

Polarity.

Modality.

Temporal validity.

Evidence links.

Epistemic state.

Model version.

Example distinctions:

"Company A intends to acquire Company B."

"Company A announced an acquisition."

"Company A completed the acquisition."

These are separate assertions.

Priority: M0

4.5 Event
Represents something that occurred or was reported to have occurred.

Required capabilities:

Event identity.

Event type.

Multiple participants.

Participant roles.

Event time.

Source evidence.

Event properties.

Event status.

Temporal revisions.

Related events.

Priority: M0

4.6 Relationship
Represents a typed connection.

Required capabilities:

Relationship identity.

Endpoint or participant identifiers.

Relationship type.

Directed or undirected semantics.

Temporal validity.

Evidence references.

Context.

Qualifiers.

Certainty or epistemic classification.

Versioning.

Permissions.

Priority: M0

4.7 Hypothesis
Represents a possible explanation.

Required capabilities:

Statement.

Target observations or events.

Supporting evidence.

Contradictory evidence.

Alternative hypotheses.

Missing evidence.

Uncertainty.

Evaluation status.

Historical revisions.

Inference provenance.

Priority: M0

4.8 Context
Represents the conditions under which information should be interpreted and retrieved.

Examples:

Industry.

Research problem.

Organization.

Community.

Historical period.

Customer workspace.

Professional domain.

Priority: F

4.9 Decision
Represents a documented choice by an identifiable actor.

Required fields may include:

Decision-maker.

Decision context.

Alternatives considered, when known.

Documented information available.

Explicitly stated criteria.

Date.

Decision.

Related evidence.

Subsequent outcomes.

Priority: F

4.10 Outcome
Represents an observable result.

Should link to:

Relevant events.

Decisions.

Forecasts.

Evidence.

Resolution criteria.

Historical context.

Priority: M0 for forecast evaluation; broader representation F

4.11 Analytical Framework
Represents a reusable reasoning procedure.

Required fields:

Framework identity.

Domain.

Applicable problem classes.

Input requirements.

Analytical steps.

Assumptions.

Failure criteria.

Evidence requirements.

Source or expert.

Version.

Evaluation history.

Priority: F

4.12 Investigation
Represents a reproducible research process.

Required fields:

Investigation ID.

Question.

User or system initiator.

Time restrictions.

Access scope.

Query plan.

Sources used.

Context retrieved.

Models and tools used.

Hypotheses generated.

Conclusions.

Cost and latency.

Evaluation history.

Priority: M0

5. RELATIONSHIP MECHANISM REGISTRY
We need a typed registry of how real-world relationships function.

Initial families:

Family	Example mechanisms
Professional	Employment, advisory role, collaboration, appointment
Organizational	Ownership, control, partnership, subsidiary relationship
Informational	Citation, reference, response, publication, reinterpretation
Economic	Investment, acquisition, purchase, supply, financing, contract
Social/participatory	Public collaboration, documented interaction, event participation
Technical	Dependency, implementation, integration, adoption
Research	Authorship, citation, hypothesis support, independent replication
Temporal	Precedence, overlap, succession, revision
Explanatory	Possible influence, potential dependency, shared cause
Decision-related	Considered, selected, rejected, implemented, revised
Requirements:

New relation types can be introduced.

Every type has clear semantics.

Financial transactions retain amount, currency, status, and roles where applicable.

Information interactions retain source and reference context.

Explanatory relationships are distinguished from direct observations.

Complex events support multiple participants.

Domain-specific constraints can validate relationships.

Priority: M0 for the initial registry; extensibility F

6. ENTITY RESOLUTION
Requirements
ID-01 — Canonical identifiers

Generate stable internal entity identifiers independent of names.

ID-02 — Source mappings

Preserve original source IDs and handles.

ID-03 — Candidate matching

Generate candidate identity matches from names, identifiers, context, and other legitimate evidence.

ID-04 — Uncertain matches

Allow unresolved identities without forcing a merge.

ID-05 — Confidence and contradiction

Record evidence for and against candidate identity matches.

ID-06 — Reversible merges

Preserve original identities and merge history.

ID-07 — Cross-domain resolution

Link verified entities across financial, informational, organizational, and technical environments.

ID-08 — Private identity separation

Avoid linking private customer identities to public or cross-customer profiles without an authorized reason.

ID-09 — Automated regression tests

Test same-name collisions, changing names, organizational aliases, and mistaken merges.

Priority: M0 for basic identity resolution; F for advanced resolution

7. INFORMATION INGESTION
7.1 Connector contract
Every source connector should expose:

Source identity.

Supported content types.

Authentication requirements.

Collection method.

Pagination or streaming support.

Update tracking.

Rate-limit handling.

Usage restrictions.

Failure behavior.

Data transformation rules.

7.2 Supported information types
The architecture should accommodate:

Structured JSON and API data.

HTML and public web content used with permission.

CSV and tabular data.

Documents.

PDFs.

Research papers.

Publications.

Transcripts.

Audio, where properly authorized.

Relevant video metadata.

Corporate records.

Financial disclosures.

Meeting notes.

Research observations.

7.3 Processing requirements
Detect duplicates.

Track source lineage.

Preserve original references.

Support incremental updates.

Validate schemas.

Handle partial failures.

Preserve uncertainty from parsing.

Distinguish source text from model-generated interpretations.

Support reprocessing with newer extractors.

7.4 Data acquisition priorities
The system should prioritize new information according to expected usefulness.

Potential factors:

Relevance to an investigation.

Novelty.

Source independence.

Historical significance.

Information prominence.

Evidence value.

Investigation uncertainty.

Cost of acquisition and processing.

A repeated, already verified fact may have low extraction priority.

Its repetition may still be important as a narrative-propagation signal.

Priority: M0 for a small source collection; F for connector framework

8. PROVENANCE AND EVIDENCE
Core requirements
EV-01 — Source traceability

Every material assertion must link to its source.

EV-02 — Extraction traceability

Record which processing run produced an assertion.

EV-03 — Model and prompt versioning

Preserve enough information to reproduce extraction and inference.

EV-04 — Independent-source distinction

Distinguish multiple independent sources from repetition of one source.

EV-05 — Contradictory evidence

Support conflicting claims without deleting earlier records.

EV-06 — Retractions

Support source correction, withdrawal, and invalidation.

EV-07 — Distinct epistemic states

Represent observed, proposed, supported, disputed, superseded, or retracted information.

EV-08 — Prominence separation

A widely discussed claim must not automatically become more credible.

EV-09 — Derived dependency tracking

Know which conclusions and summaries depend on an observation.

EV-10 — Reproducibility

Reconstruct important analytical results from their evidence and processing versions.

Priority: M0 for traceability and epistemic separation; F for complete lineage

9. TEMPORAL ARCHITECTURE
Required time concepts
Event time.

Validity period.

Publication time.

Observation time.

Ingestion time.

Knowledge time.

Revision time.

Forecast creation time.

Forecast resolution time.

Requirements
TM-01 — Historical queries

Reconstruct the state of relevant information at a chosen date.

TM-02 — Knowledge-time filtering

Do not include information learned after the selected historical cutoff.

TM-03 — Public-availability distinction

Support separate evaluation of what was publicly available versus what the system had actually ingested.

TM-04 — Append-only historical records

Important updates must not silently erase prior states.

TM-05 — Temporal graph traversal

Find relationships valid during particular periods.

TM-06 — Source publication delays

Represent events discovered after their actual occurrence.

TM-07 — Historical corrections

Allow later evidence to change the current interpretation without rewriting what was known historically.

TM-08 — Historical index isolation

Prevent current summaries or embeddings from leaking future information into historical replay.

Priority: M0

10. SEGMENTED WORLD MEMORY
Purpose
Store a broad body of information while retrieving only the context necessary for a particular investigation.

Required structural components
A. Shared identity spine

Stable canonical entities and source mappings.

B. Canonical evidence store

Observations, assertions, events, provenance, and permissions.

C. Domain projections

Specialized views for finance, organizations, information, research, people, decisions, and other domains.

D. Semantic indexes

Efficient retrieval of conceptually related information.

E. Graph indexes

Efficient retrieval of typed relationships and paths.

F. Temporal indexes

Efficient point-in-time information retrieval.

G. Contextual memory

Compressed, derived views of selected information.

Requirements
MM-01 — Logical segmentation

Information can belong to multiple contexts without duplicating canonical facts.

MM-02 — Cross-domain connectivity

Relevant relationships remain discoverable across domain boundaries.

MM-03 — Dynamic context construction

Queries can assemble temporary information contexts.

MM-04 — Context compression

Summaries reduce retrieval cost while retaining references to original evidence.

MM-05 — Rebuildability

Derived memory can be regenerated from canonical records.

MM-06 — Incremental invalidation

Updates refresh affected representations without rebuilding everything.

MM-07 — Domain-specific retention

Different information types can have different freshness, retention, and archival policies.

MM-08 — Budget-aware retrieval

Retrieval can stop or expand according to relevance and resource budgets.

MM-09 — Cross-domain recall evaluation

Measure whether segmentation causes important evidence to be missed.

MM-10 — Storage independence

Logical information contracts should not depend on one database engine.

Priority: M0 for basic segmentation and cross-domain retrieval; R for optimized methods

11. EVIDENCE CAPSULE RESEARCH
Evidence capsules are a proposed optimization, not a confirmed invention.

A capsule should potentially contain:

Capsule ID.

Construction method.

Domain labels.

Relevant entity references.

Event references.

Assertion references.

Evidence references.

Temporal boundaries.

Context summary.

Cross-links.

Permissions.

Generation version.

Dependency list.

Invalidation status.

Candidate construction methods
Entity-centered.

Event-centered.

Domain-centered.

Community-centered.

Investigation-centered.

Dynamically assembled.

Required research
Determine:

Whether capsules improve retrieval.

Whether they reduce token usage.

Whether they introduce information loss.

Whether they become stale too frequently.

Whether standard materialized views are sufficient.

Whether graph-community summaries already solve this.

Whether dynamic context construction is preferable.

Priority: R

12. INFORMATION RETRIEVAL
Required retrieval capabilities:

Retrieval type	Purpose
Exact lookup	Known entities, documents, contracts, IDs
Full-text	Specific phrases and terminology
Vector search	Semantic similarity
Typed graph search	Explicit relationships
Multi-hop search	Indirect relationships
Temporal retrieval	Historical validity
Context filtering	Relevant industries and information environments
Provenance filtering	Evidence and source requirements
Permission filtering	Authorized information access
Analytical queries	Aggregation, financial and temporal calculations
Hybrid reranking	Prioritize relevant evidence
Requirements
RT-01 — Query classification

Identify required information types.

RT-02 — Multi-index planning

Select appropriate search mechanisms.

RT-03 — Cross-domain expansion

Follow relevant connections between contexts.

RT-04 — Evidence sufficiency

Identify when retrieved evidence is insufficient.

RT-05 — Retrieval budgets

Bound search cost and traversal depth.

RT-06 — Explicit query trace

Record why specific retrieval operations occurred.

RT-07 — Reproducibility

Store retrieved evidence IDs and search parameters.

RT-08 — Evaluation

Measure relevance, recall, latency, and cost.

Priority: M0

13. INFERENCE ENGINE
Primary objective
Generate meaningful, evidence-grounded explanations and predictions from interconnected information.

Required operations
IN-01 — Query understanding
Identify:

Investigation objective.

Requested outcome.

Relevant entities.

Time window.

Context.

Evidence requirements.

Authorization boundary.

IN-02 — Investigation planning
Produce a structured plan of information requirements and retrieval steps.

IN-03 — Relationship discovery
Generate candidate connections using documented references, relevant events, temporal alignment, semantic information, and graph structure.

IN-04 — Hypothesis generation
Construct competing explanations.

IN-05 — Hypothesis evaluation
Search for evidence supporting and contradicting each explanation.

IN-06 — Alternative explanations
Identify possible confounders, shared causes, and independent developments.

IN-07 — Missing-information detection
Specify what information would materially improve the investigation.

IN-08 — Investigation expansion
Perform additional research when justified.

IN-09 — Uncertainty representation
Distinguish documented facts from candidate explanations and unresolved questions.

IN-10 — Evidence-grounded response
Every significant factual conclusion must be traceable.

IN-11 — Explanation revision
Update affected hypotheses when new evidence arrives.

IN-12 — Computational efficiency
Use bounded context, model routing, caching, and stopping conditions.

Priority: M0 for the complete basic inference loop; R for optimal algorithms

14. ATTRIBUTION ARCHITECTURE
We need to support four distinct problems.

Content attribution
Where was something first observed?

Information-pathway attribution
Which documented references or interactions connect sources?

Causal attribution
What evidence suggests a particular development contributed to another?

Outcome attribution
How can a result be related to earlier documented causes, conditions, and decisions?

Requirements
AT-01 — Multiple explanations

Do not force a single explanation when evidence is ambiguous.

AT-02 — Explicit source pathways

Reconstruct known citations and references.

AT-03 — Temporal consistency

Prevent inferred influence from violating known chronology.

AT-04 — Common-source consideration

Account for the possibility that multiple actors relied on the same source.

AT-05 — Independent emergence

Recognize that similar ideas may arise independently.

AT-06 — Missing-observation awareness

Represent uncertainty caused by inaccessible or unrecorded information.

AT-07 — Direct verification

Support authorized interviews and additional research as evidence sources.

AT-08 — Accuracy evaluation

Measure supported and unsupported inferred relationships separately.

AT-09 — Calibrated confidence

Avoid unwarranted certainty.

AT-10 — Explicit limits

Never claim complete causal attribution where evidence does not support it.

Priority: M0 for basic attribution distinctions; R for improved methods

15. HUMAN AND PROFESSIONAL INFORMATION MODEL
Purpose
Understand observable professional relationships, information pathways, decisions, and context.

Supported information
Professional affiliations.

Public roles.

Documented expertise.

Publicly expressed positions.

Published research.

Professional projects.

Explicitly disclosed motivations.

Verified professional relationships.

Documented collaborations.

Public information references.

Historical decisions.

Observed outcomes.

Self-reported personal context in authorized private workspaces.

Requirements
HU-01 — Context-specific representation

Do not assume a person behaves identically across all situations.

HU-02 — Decision history

Preserve independent decision records.

HU-03 — Evolving patterns

Support tentative, evidence-backed summaries of documented professional decision-making.

HU-04 — Historical changes

Represent changing professional interests, affiliations, and expressed positions.

HU-05 — Cross-domain participation

Connect relevant activities across multiple fields.

HU-06 — Provenance

Link information to actual disclosures or observations.

HU-07 — Identity uncertainty

Prevent unsupported personal attribution.

HU-08 — Private context separation

Keep private user information within its authorized scope.

HU-09 — Sensitive inference boundary

Do not infer hidden sensitive identities or psychological vulnerabilities from private conversation histories or content consumption.

Priority: F; M0 for public entity and decision relationships

16. EXPERT FRAMEWORK ENGINE
Purpose
Represent analytical practices used by experienced professionals.

Initial domains
Venture investing.

Corporate strategy.

Quantitative research.

Economics.

Market research.

Narrative analysis.

Security research.

Organizational decision-making.

Requirements
EF-01 — Framework storage

Store analytical methods as versioned structured records.

EF-02 — Applicability

Represent which questions a framework is appropriate for.

EF-03 — Required inputs

Specify evidence needed.

EF-04 — Assumptions

Represent underlying assumptions.

EF-05 — Analytical procedures

Define steps or computations.

EF-06 — Limitations

Record when the method may fail.

EF-07 — Framework selection

Choose methods based on investigation needs.

EF-08 — Framework composition

Combine complementary methods.

EF-09 — Evaluation

Measure usefulness against independent outcomes.

EF-10 — Expert provenance

Preserve original sources, interviews, or publications.

Priority: F; framework selection R

17. ECONOMIC AND MONEY-FLOW INTELLIGENCE
Purpose
Investigate documented relationships between people, decisions, organizations, capital, and market developments.

Required information types
Investments.

Financing.

Ownership.

Acquisitions.

Partnerships.

Contracts.

Purchases.

Capital commitments.

Supply relationships.

Procurement.

Corporate spending.

Industry dependencies.

Capacity constraints.

Organizational decisions.

Market developments.

Critical semantic distinctions
The system must distinguish:

Proposed investment.

Announced investment.

Contractually committed investment.

Completed investment.

Equity versus debt.

Revenue versus financing.

Purchase orders versus delivered purchases.

Financial relationships versus technological dependencies.

Verified supply contracts versus potential supplier relationships.

Requirements
EC-01 — Financial event representation

Amounts, currencies, parties, roles, status, and dates.

EC-02 — Relationship paths

Investigate direct and indirect organizational relationships.

EC-03 — Historical financial context

Compare developments across time.

EC-04 — Economic dependency analysis

Identify documented dependencies and potential downstream consequences.

EC-05 — Cross-domain linkage

Connect economic evidence with people, information, technology, and events.

EC-06 — Source-backed conclusions

Never invent transactions from semantic proximity or inferred relationships.

EC-07 — Real-world outcome evaluation

Compare forecasts with documented subsequent developments.

Priority: F; representative economic events M0

18. NARRATIVE AND INFORMATION-FLOW INTELLIGENCE
Purpose
Understand observable information development across sources and communities.

Required capabilities
NV-01 — Claim identification

Extract identifiable claims and ideas.

NV-02 — Semantic grouping

Identify related claims expressed differently.

NV-03 — Source tracing

Identify documented references.

NV-04 — Temporal propagation

Track when information appears across sources.

NV-05 — Community and domain movement

Investigate transitions between contexts.

NV-06 — Novelty detection

Distinguish emerging developments from repeated information.

NV-07 — Prominence measurement

Measure attention without treating prominence as truth.

NV-08 — Contradiction and reinterpretation

Track changes in meaning.

NV-09 — Historical narrative reconstruction

Reconstruct information development through time.

NV-10 — Cross-domain consequences

Investigate possible connections to organizations, decisions, and economic changes.

Priority: M0 for a limited example; F for broader coverage

19. FORECASTING AND HISTORICAL LEARNING
Required forecast structure
Every evaluated forecast needs:

Forecast identifier.

Question.

Target event or outcome.

Prediction timestamp.

Evidence cutoff.

Historical knowledge boundary.

Forecast horizon.

Prediction.

Uncertainty or probability.

Supporting evidence.

Model and method version.

Resolution criteria.

Actual result.

Evaluation score.

Requirements
FC-01 — Historical replay

Reconstruct information available at a chosen cutoff.

FC-02 — Prediction commitment

Record predictions before revealing later results.

FC-03 — Outcome resolution

Determine how the forecast should be scored.

FC-04 — Proper evaluation

Use suitable scoring rules.

FC-05 — Baseline comparison

Compare against simpler forecasting methods.

FC-06 — Calibration

Measure whether predicted probabilities correspond to observed frequencies.

FC-07 — Error inspection

Identify failed assumptions and missing evidence.

FC-08 — Learning feedback

Route errors to the relevant component.

FC-09 — No future leakage

Prevent later records, current embeddings, or summaries from entering historical runs.

FC-10 — Reproducibility

Preserve the complete evaluation configuration.

Priority: M0

20. AUTOMATIC LEARNING AND MODEL IMPROVEMENT
Different forms of learning must be separated.

Knowledge updates
New evidence changes stored information.

Extraction improvement
Corrected extractions improve extraction quality.

Entity-resolution improvement
Verified identity decisions inform matching.

Retrieval improvement
Missing or irrelevant evidence informs query planning and ranking.

Attribution improvement
Verified and disproven explanations inform hypothesis evaluation.

Forecasting improvement
Resolved predictions inform calibrated forecasting.

Framework improvement
Measured performance informs framework selection.

Requirements
Keep correction records.

Avoid treating generated hypotheses as verified training labels.

Version models.

Preserve evaluation sets.

Separate production updates from training experiments.

Evaluate changes before deployment.

Support rollback.

Monitor regressions.

Avoid automatic acceptance of user corrections without verification where external factual claims are concerned.

Priority: M0 for feedback capture and replay; F for advanced continual learning

21. AUTONOMOUS MONITORING AND INVESTIGATION
Purpose
Identify relevant developments and investigate them without requiring a user to ask every time.

Required components
Watchlist registry.

Monitored entity and concept definitions.

Source subscriptions.

Scheduled or streaming ingestion.

Change detection.

Relevance evaluation.

Novelty detection.

Investigation priority.

Resource budget.

Investigation execution.

Alert generation.

Feedback tracking.

Requirements
AM-01 — Question answering

Respond to explicit investigations.

AM-02 — Scheduled research

Produce periodic updates.

AM-03 — Continuous monitoring

Track selected sources according to authorized policies.

AM-04 — Autonomous investigation

Launch bounded research when relevant signals appear.

AM-05 — Repetition-based escalation

Increase investigation priority when a developing signal becomes relevant again.

AM-06 — Investigation stopping conditions

Control time, retrieval volume, model calls, and cost.

AM-07 — Researcher escalation

Refer high-impact unresolved cases for review.

AM-08 — Alert traceability

Every notification should link to the underlying evidence and investigation.

Priority: F; basic monitoring later in MVP

22. PRIVATE INFORMATION AND ENTERPRISE SECURITY
Information environments
Shared public intelligence
Permitted public and licensed information.

Private user intelligence
Authorized personal workspace information.

Private enterprise intelligence
Customer-controlled organizational information.

Explicit contribution intelligence
Records whose authorized owners deliberately approve broader use.

Requirements
SEC-01 — Tenant isolation

Customers must not be able to access each other's private data.

SEC-02 — Authorization before retrieval

Permissions apply before content reaches LLMs or other inference services.

SEC-03 — Derived-information restrictions

Derived relationships and summaries inherit applicable source restrictions.

SEC-04 — Encryption

Secure transport and protected storage.

SEC-05 — Scoped connectors

Use only required third-party permissions.

SEC-06 — Audit logging

Record meaningful access and modifications.

SEC-07 — Data correction and deletion

Support applicable rights and retention policies.

SEC-08 — Source license tracking

Preserve usage restrictions for ingested data.

SEC-09 — Model-provider boundaries

Prevent unauthorized transmission of private information to external inference services.

SEC-10 — Prompt-injection resistance

External source content cannot become authoritative instructions.

SEC-11 — Enterprise deployment options

Accommodate more restrictive hosting and key-management requirements later.

SEC-12 — Information contribution controls

Private data enters shared intelligence only through explicit, authorized contribution.

Priority: M0 for isolation and authorization; L for advanced enterprise deployment

23. FOUNDER AND RESEARCH KNOWLEDGE WORKSPACE
Purpose
Maintain the project's own developing information.

Information types
Founder hypotheses.

Architecture decisions.

Technical objections.

Research findings.

Customer interviews.

Expert meetings.

Product feedback.

Outreach drafts.

Sent outreach.

Meeting notes.

Experiment results.

Competitive observations.

Decisions and outcomes.

Required distinctions
A draft is not a sent message.

A hypothesis is not a verified fact.

An interviewee's statement is evidence of what they said, not necessarily evidence that the statement is true.

A proposed architecture is not an implemented architecture.

An experimental result is not a general proof without supporting evaluation.

Requirements
FW-01 — Structured research entries

Every important research entry has context and provenance.

FW-02 — Decision history

Record what changed and why.

FW-03 — Meeting ingestion

Support authorized meeting summaries and notes.

FW-04 — Objection tracking

Link objections to corresponding hypotheses and follow-up experiments.

FW-05 — Research retrieval

Find previous discussions and decisions.

FW-06 — Agent portability

Export relevant context for another AI agent.

FW-07 — Version control

Maintain canonical project specifications.

FW-08 — Confidentiality

Keep founder and company research within its intended scope.

Priority: F; basic project documentation M0

24. PRODUCT EXPERIENCE
Primary experience
Messaging-first intelligence.

The user should be able to submit a complex question conversationally.

The system should return a useful answer, supporting evidence, uncertainty, and relevant follow-up possibilities.

Required response structure
Answer

What the available evidence supports.

Relationships

The relevant people, organizations, events, information, or economic connections.

Explanation

Why those connections matter.

Uncertainty

Which conclusions are inferred or unresolved.

Potential developments

What could happen next and why.

Sources

Where the supporting evidence comes from.

Missing information

What would improve the investigation.

Requirements
UX-01 — Messaging-first

An initial conversational interface.

UX-02 — Investigation history

Users can revisit previous investigations.

UX-03 — Source inspection

Users can examine supporting evidence they are authorized to view.

UX-04 — Follow-up research

Continue an investigation without starting over.

UX-05 — Monitoring

Support optional ongoing intelligence updates.

UX-06 — Asynchronous jobs

Long-running research must not depend on one synchronous request.

UX-07 — Cross-channel interfaces

Support APIs, MCP, CLI, and enterprise interfaces through a common backend.

UX-08 — Feedback capture

Users can identify missing evidence, incorrect information, or useful findings.

UX-09 — Appropriate approval

External actions must respect authorization and approval boundaries.

Priority: M0 for minimal conversational interface; F for broader delivery

25. API AND INTEROPERABILITY CONTRACTS
Candidate interface operations:

Operation	Purpose
investigate	Create an evidence-backed research investigation
get_investigation	Retrieve investigation state and results
resolve_entity	Retrieve candidate or confirmed identities
trace_relationship	Find documented and inferred connection paths
get_evidence	Retrieve supporting permitted source records
get_hypotheses	Retrieve competing explanatory hypotheses
compare_history	Compare historical states
create_forecast	Record a testable prediction
resolve_forecast	Score a prediction against an outcome
create_monitor	Register authorized ongoing monitoring
submit_research	Add a structured research observation
export_context	Export a permitted information package
These are conceptual operations, not final API signatures.

Shared API requirements
Authentication.

Authorization.

Stable identifiers.

Versioned schemas.

Structured errors.

Idempotent writes where appropriate.

Job IDs for long-running tasks.

Result pagination.

Source citations.

Request tracing.

Budget controls.

Export support.

Priority: F; minimal investigation API M0

26. MESSAGING AND CONNECTOR ARCHITECTURE
The messaging channel must not own the underlying intelligence state.

The same investigation should be accessible through multiple interfaces.

Candidate channels
Simple local web chat.

WhatsApp Business.

Slack.

MCP.

CLI.

Enterprise API.

Other supported messaging platforms.

Integration requirements
User authentication.

Session and workspace identification.

Query submission.

Investigation status.

Asynchronous response delivery.

Evidence links.

Optional monitoring alerts.

Permission-aware context.

Feedback.

External action authorization.

The first prototype may use a simple local messaging-style client rather than immediately integrating a commercial messaging provider.

The requirement is a messaging experience, not dependence on any specific platform.

Priority: M0 for one interface; L for additional channels

27. SPECIALIZED ENTERPRISE CAPABILITIES
Future enterprise features may include:

Private research workspaces.

Company knowledge integrations.

Team-level access policies.

Customer-managed encryption keys.

Private deployment.

Enterprise audit logs.

Research collaboration.

CRM integration.

Email and calendar integration.

Decision-history intelligence.

Strategic monitoring.

Contract and supplier analysis.

Industry intelligence.

Approved meeting transcription.

Executive wearable concept
A selective enterprise recording device could serve as an optional source of authorized meeting context.

This is not a mass consumer distribution requirement.

Required future considerations:

Participant authorization.

Recording transparency.

Storage and retention.

Transcript accuracy.

Private context extraction.

Confidentiality.

Processing costs.

Device provisioning.

Data ownership.

Enterprise security.

Explicit contribution permissions.

Priority: L

28. PERFORMANCE AND COST REQUIREMENTS
Primary objective
Maximize useful, source-grounded intelligence per unit of computation and storage.

Metrics
Cost per ingested observation.

Cost per extracted assertion.

Cost per supported relationship.

Cost per investigation.

Cost per forecast.

Cost per successful historical reconstruction.

Retrieval latency.

Inference latency.

Storage growth.

Indexing time.

Cache effectiveness.

Model-token usage.

Evidence coverage.

Error rate.

Required system behavior
Do not reprocess unchanged information unnecessarily.

Support incremental updates.

Reuse stable derived representations.

Limit investigation breadth when additional work provides little value.

Select model capability according to task complexity.

Track processing costs per job.

Support explicit cost and resource budgets.

Preserve the ability to use smaller or local models.

Priority: M0 for instrumentation; R for optimization

29. REFERENCE DEPLOYMENT ARCHITECTURE
Initial target
Local development with limited external cost.

Suggested logical components:

Application server.

Canonical structured database.

Source archive.

Vector index.

Graph representation.

Ingestion workers.

Inference workers.

Evaluation runner.

Minimal messaging interface.

Requirements
DEP-01 — Local-first

The first system can run on a developer machine or small server.

DEP-02 — Modular boundaries

Components communicate through defined interfaces.

DEP-03 — Reproducible setup

Dependencies and configuration can be recreated.

DEP-04 — Environment separation

Development, testing, and later production remain distinct.

DEP-05 — Replaceable model providers

Model choice is not hardcoded into foundational records.

DEP-06 — Rebuildable indexes

Derived indexes can be regenerated.

DEP-07 — Durable jobs

Background investigations survive process interruptions.

DEP-08 — Observability

Measure system errors, costs, and processing performance.

DEP-09 — Security

Private data boundaries remain enforceable.

DEP-10 — Migration path

Infrastructure can evolve without replacing canonical information contracts.

Priority: M0

30. REQUIRED END-TO-END SYSTEM FLOWS
The research team must map and test these flows.

Flow A — Source to knowledge
Source record discovered.

Access and licensing checked.

Original content registered.

Parsing completed.

Entities, claims, and events extracted.

Entity identities resolved.

Evidence links created.

Temporal state recorded.

Relevant graph projections updated.

Affected memory indexes refreshed.

Flow B — Question to inference
User submits a question.

User identity and scope resolved.

Relevant entities identified.

Investigation plan constructed.

Appropriate contexts and frameworks selected.

Evidence retrieved.

Relationships reconstructed.

Hypotheses generated.

Contradictions and alternatives checked.

Answer produced with evidence and uncertainty.

Investigation stored for reuse and review.

Flow C — New evidence to revised understanding
New observation arrives.

Existing entities and assertions identified.

Changes compared with historical state.

Relevant relationships updated.

Affected hypotheses identified.

Hypotheses re-evaluated.

Derived memory invalidated or refreshed.

Monitoring rules checked.

Any significant changes surfaced to authorized users.

Flow D — Historical prediction and evaluation
Historical cutoff selected.

Allowed evidence reconstructed.

Query executed under point-in-time restrictions.

Forecast generated and stored.

Actual later outcome revealed.

Forecast scored.

Error categories identified.

Evaluation results stored.

Candidate improvements tested separately.

Improved components deployed only after appropriate validation.

Flow E — Expert learning
Professional method obtained from a valid source or authorized interview.

Framework documented.

Assumptions and applicability recorded.

Historical cases selected.

Framework applied.

Results compared against alternatives.

Performance recorded.

Framework registry updated.

Flow F — Private enterprise information
Customer authorizes integration.

Source scope and permissions established.

Information enters a private workspace.

Evidence and derived indexes inherit access restrictions.

Customer performs authorized investigations.

Results remain private unless explicitly approved for sharing.

Correction, deletion, and retention policies are enforced.

31. FIRST DEMONSTRATION — REQUIRED CAPABILITY SET
The first demonstration must be structurally representative.

It should not be limited to one isolated information type.

Choose a historical domain containing:

Relevant people.

Public information.

Organizations.

Technological or industrial events.

Economic activity.

Documented decisions.

Subsequent outcomes.

Demonstration requirements
D-01

Ingest real historical information.

D-02

Extract entities and events.

D-03

Resolve overlapping identities.

D-04

Build typed relationships.

D-05

Segment information into different contexts.

D-06

Retrieve and connect information across those contexts.

D-07

Generate alternative hypotheses.

D-08

Explain which relationships are documented and which are inferred.

D-09

Reconstruct a past information state.

D-10

Generate a testable historical prediction.

D-11

Reveal and score the subsequent outcome.

D-12

Display the resulting errors and learning feedback.

D-13

Record compute and retrieval costs.

D-14

Make the investigation accessible through a messaging interface.

D-15

Provide an inspectable evidence and processing trace.

This is the first meaningful proof of the architecture.

32. ACCEPTANCE TESTS
The initial system must correctly handle representative cases such as:

Scenario	Required behavior
Two different people share a name	Avoid automatic identity merge
One claim appears in 100 dependent sources	Preserve prominence without treating repetition as independent verification
A company announces an investment	Do not report a completed transaction without corresponding evidence
Two similar claims arise independently	Avoid automatically inferring direct transmission
A source is corrected	Re-evaluate dependent assertions
A hypothesis loses supporting evidence	Revise its status
A question crosses multiple domains	Retrieve relevant information across contexts
A historical query is executed	Exclude future information
An entity appears in several domains	Preserve one appropriately resolved identity
A customer requests private information	Enforce authorization
A private source influences an answer	Prevent unauthorized disclosure
A forecast fails	Record the error and evaluation
A source is repeatedly ingested	Avoid unnecessary duplicate processing
An investigation becomes too expensive	Enforce the configured budget
A graph edge is speculative	Do not present it as verified fact
An expert method fails on a case	Preserve the failed evaluation
A model is upgraded	Preserve enough version history to compare outcomes
33. BASELINE COMPARISONS
We need empirical comparisons.

Baseline A — Conventional RAG
Structured retrieval where useful, keyword/vector search, and an LLM.

Baseline B — Existing GraphRAG
An established graph-based retrieval implementation.

Baseline C — Proposed IWM
Temporal evidence model, segmented memory, adaptive retrieval, explicit hypotheses, and outcome-based evaluation.

Comparison dimensions
Source correctness.

Relationship accuracy.

Cross-domain completeness.

Retrieval recall.

Historical fidelity.

Attribution error.

Prediction quality.

Compute cost.

Latency.

Practical research usefulness.

A candidate architecture should not be declared superior without measured evidence.

34. TECHNICAL RESEARCH QUESTIONS
The specialist research agent should investigate each question and return evidence.

Ontology
What structure best represents heterogeneous, time-dependent, multi-party relationships?

Identity
How can entities be resolved conservatively and corrected later?

Provenance
How can every derived conclusion be traced to the underlying observations?

Temporal memory
How can we efficiently reconstruct past states without future-data leakage?

Segmentation
How can information remain broadly connected while only relevant contexts are activated?

Retrieval
What techniques produce the best evidence recall under limited compute budgets?

Inference
How should the model produce, compare, and revise explanations?

Attribution
What forms of information and causal attribution are measurable with available data?

Human decision modeling
How should documented professional decision-making patterns be represented and evaluated?

Expert frameworks
How can analytical methods be selected, combined, and tested automatically?

Forecasting
Can historical relationships improve future outcome prediction over simpler baselines?

Autonomous learning
Which components should update continuously, and which require evaluated training?

Security
How can private and shared information coexist without cross-tenant leakage?

Economics
What information and inference operations dominate costs?

Product delivery
What is the simplest way to expose the intelligence through messaging while preserving portability?

35. DOCUMENTATION AND AI-AGENT COORDINATION
The project should maintain version-controlled records for:

Vision.

Confirmed product decisions.

Architecture.

Ontology.

Data sources.

Evidence semantics.

Temporal semantics.

Memory.

Inference.

Expert frameworks.

Learning.

Evaluation.

Security.

Product interfaces.

Economics.

Experiments.

Change history.

Every AI-agent handoff should include:

Objective.

Relevant requirements.

Existing information.

Approved sources.

Constraints.

Expected output.

Acceptance tests.

Assumptions.

Unresolved issues.

Changes proposed.

Research agents must not silently convert hypotheses into architecture decisions.

Coding agents must not change foundational contracts without recording the change.

All major findings should retain source links and dates.

36. PROPRIETARY RESEARCH TARGETS
The following are potential research directions, not established innovations.

P1 — Adaptive evidence composition
Can the system dynamically select and assemble relevant evidence across domains more effectively than fixed retrieval?

P2 — Context-aware memory partitioning
Can the system compress and segment information without materially losing important cross-domain relationships?

P3 — Explicit uncertainty and hypothesis revision
Can competing explanations and source-independent evidence improve attribution quality?

P4 — Expert-guided inference
Can reusable analytical frameworks improve reasoning and decision support?

P5 — Historical outcome-driven learning
Can historical evaluation improve the choice of retrieval, reasoning, and prediction methods?

P6 — Cost-aware intelligence planning
Can the system choose how much investigation to perform based on expected information value?

P7 — Incremental relational understanding
Can new evidence update affected portions of the model without expensive global recomputation?

These directions should be tested individually and in combination.

37. COMMERCIAL AND PRODUCT REQUIREMENTS
The architecture should potentially support:

Personal intelligence
Portable research memory, authorized context, relevant monitoring, affordable integrations.

Market intelligence
Companies, investments, relationships, market changes, economic dependencies.

Information security
Narratives, attribution, information-integrity investigations, documented propagation networks.

Enterprise decision intelligence
Private organizational knowledge, strategic research, approved integrations, executive briefings.

Intelligence infrastructure
Developer APIs, agent tools, evidence retrieval, historical claims, relationship intelligence.

These products may share the same foundational technology.

They do not necessarily share the same data permissions or pricing.

The first paying customer and pricing are not yet validated.

The initial commercial strategy must be informed by customer discovery and evidence of existing spending.

38. BUILD-VERSUS-RESEARCH DECISION REGISTER
For every major subsystem, return one of the following recommendations:

Reuse: An existing implementation is sufficiently capable.

Integrate: Several existing components should be combined.

Extend: An existing implementation provides a foundation but requires modifications.

Build: A relatively straightforward component should be implemented internally.

Research: The problem requires experimentation or original methods.

Defer: Not necessary to validate the current hypothesis.

Reject: Technically inappropriate, unnecessarily expensive, or unsupported by evidence.

Every recommendation must include a reason.

39. EXPLICITLY OPEN DECISIONS
The following must remain open until the appropriate technical research is completed:

Exact ontology implementation.

Graph database engine.

Canonical storage architecture.

Temporal implementation.

Entity-resolution algorithms.

Evidence scoring methods.

Memory partitioning strategy.

Evidence-capsule usefulness.

Adaptive retrieval algorithms.

Hypothesis evaluation methods.

Causal attribution methods.

Expert-framework selection.

Forecasting architecture.

Specialized fine-tuning approach.

Model choices.

Workflow orchestration.

Monitoring system.

Production infrastructure.

Data-licensing strategy.

Initial commercial vertical.

Pricing and packaging.

These are not invitations to invent arbitrary answers.

Each requires explicit comparison, experimentation, or business evidence.

40. FINAL SYSTEM REQUIREMENTS
The Information World Model must ultimately be:

Relationship-native

It represents heterogeneous interactions and their changing mechanisms.

Evidence-native

Every material conclusion has a traceable evidence basis or explicit uncertainty.

Temporal

It preserves historical states, revisions, and event sequences.

Cross-domain

It connects relevant information without privileging one category.

Context-sensitive

It retrieves and reasons over the information necessary for a particular question.

Autonomously updating

It incorporates new evidence and revises affected interpretations.

Evaluable

Its extraction, retrieval, attribution, and predictions can be measured.

Cost-aware

Research and inference operate under practical resource budgets.

Permission-aware

Private data and derived outputs retain access boundaries.

Model-independent

It can replace underlying models without losing its information.

Portable

Its canonical records, research, and specifications survive changes in tools.

Expandable

New information domains and capabilities can be added without rebuilding the foundation.

FINAL INSTRUCTION TO THE RESEARCH AGENT
Use this architecture requirements register as the complete reference scope for your investigation.

For every subsystem:

Identify the underlying technical problem.

Find existing approaches.

Find credible implementations.

Compare their strengths and weaknesses.

Identify missing capabilities.

Determine whether the requirement should be retained or amended.

Recommend a justified technical direction.

Provide a benchmark or acceptance test.

Explain the cost and complexity implications.

Document all significant assumptions.

Do not assume every proposed component is necessary.

Do not assume the system is novel.

Do not assume the most complex solution is the best.

Do not collapse the project into a single intelligence vertical.

Our task is to discover the smallest technically coherent architecture capable of demonstrating the larger relational information-world hypothesis, while preserving a clear path toward the complete system.

The research output should enable a technical co-founder or coding agent to move from architectural requirements to a defensible implementation plan without inventing missing decisions.

End of Architecture Requirements Register v1.0.

How to use the two handoffs
Give both documents to the specialist research AI.

Document 1 is the mission. Document 2 is the technical reference. Ask it to return verified findings, comparisons, missing architectural requirements, and recommended experiments—not code yet.

Get independent technical criticism.

Have your former technical co-founder assess the proposed architecture against the specialist's findings. Conflicting recommendations should remain explicit until resolved.

Only then create the Codex implementation handoff.

That handoff should contain selected components, versioned schemas, repository structure, exact interfaces, tests, build order, and confirmed decisions. Codex should not be expected to make foundational research decisions on its own.

The most important distinction between these documents is that Document 2 defines the capability we need, while Document 1 searches for the best way to achieve it.

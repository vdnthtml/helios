# Original master definition

Source: `context/sources/conversation-2026-11-14.txt`, lines 37–1490.
Status: preserved conversation extract; assistant-authored proposals are not independently verified findings or automatically accepted decisions. Original dates and claims are preserved as history.

---

So, again for the thirteenth, how do you want to measure the accuracy whether the source and events are authentic, whether the pathway is documented? Now, again everything should be measured, bro. It's like just depends on whatever. What should people, what should the model learn about people? Again, I've explained this a lot of times to you, and. Like it's up there. Professional interests, explicit positions, relationship decisions, process, historical choices, observations, private, self-reported context, everything should be there. And also, who do they follow, who do they talk to, who are their friends, and stuff like that. What are they connected to? What do they work in? Why do they work in that? What is their motivation to work in a specific field? And things like that. That is all given on their, like profiles, like on their LinkedIn, on their X, and then. That's just monitoring and finding the right people. Now, again, we won't go around finding all that information for every single person because that is very, very expensive. We will only go for the people that we actually care about and are the key characters for our learning and the model testing. How should expert reasoning framework into the system? It's the fifteenth question. Would you prefer to begin studying published professional methods? Direct interview specialist asking them to analyze legal cases combining all three. I think expert reasoning I'll need to ask people and also like you know learning whatever way is possible. It's like again we need to do what we gotta do. We can't just keep working like monkeys all the time right? So we'll do whatever is efficient. So all three combined yes. So should the model eventually select and combine reasoning frameworks? Yes it should. Yeah it should. Yes. So the systems like these based on questions. I mean yeah whatever it works. I think you can make sense of that. Seventeenth, what should the system learn from its mistake? Um, whatever you prefer, bro. Because again, when we think about the learning loops, it's mostly, I can think of attribution. I think you can think more deeply around this. So I'll leave that to you.
…
We have enough information to stop questioning the vision and start defining the actual system.

I've consolidated your answers and our discussions into one master draft. This separates what you've decided, how I recommend implementing it, and what we still need to prove. I haven't reduced the project to financial intelligence, narrative analysis, or personal AI memory. They're all applications of the same underlying architecture.

INFORMATION WORLD MODEL
Master Product & Architecture Definition — v1.0
Status: Foundational product decisions established. Technical implementation proposed, pending experiments.

Objective: Build a proprietary intelligence system that represents, connects, interprets, and learns from information about the world, allowing it to reconstruct historical developments, understand relationships, identify emerging changes, and generate increasingly useful predictions.

PART I — WHAT WE ARE BUILDING
1. The core vision
The world generates information continuously.

People exchange ideas, develop beliefs, establish relationships, make decisions, invest money, create companies, publish research, and influence one another.

These activities are connected.

An executive's decision may depend on a conversation, market conditions, financial incentives, previous experiences, or information encountered in an entirely different industry.

The resulting decision can influence companies, capital allocation, technologies, communities, and public narratives.

Today, these connections are fragmented across different sources and information systems.

We want to build an evolving model of these relationships and the mechanisms through which they produce changes in the world.

Our system must be capable of answering five fundamental questions:

What happened?

What is connected to what?

Why might these relationships and events have occurred?

What can historical evidence teach us?

What might happen next, and how can we test that prediction?

The objective isn't to know everything.

It is to extract the greatest possible reliable understanding from the information available.

2. What the system is NOT
It is not simply:

A social listening platform.

A financial database.

A personal memory chatbot.

A competitor monitoring dashboard.

A graph database connected to an LLM.

A collection of autonomous agents.

A tool that claims to know what everyone privately thinks.

These can be features, reference systems, or specialized applications.

Our actual product is the underlying information and inference architecture that allows these capabilities to work together.

3. Fundamental principles
Principle 1 — Relationships are foundational.

People, information, transactions, organizations, conversations, technology, and economic outcomes should not exist in isolated systems.

Principle 2 — No information domain has universal priority.

Money trails aren't more important than people. People aren't more important than economic outcomes. Their relative significance depends on the investigation.

Principle 3 — The model must understand nuances.

A company discussing an acquisition, considering an acquisition, announcing an acquisition, and completing an acquisition are different things.

Principle 4 — Evidence and inference are different.

The system can investigate uncertain relationships without declaring them factual.

Principle 5 — Historical learning is essential.

Every prediction should be testable against subsequent outcomes, and every failed explanation should help improve the system.

Principle 6 — Intelligence must be economical.

The model should retrieve and process the information needed for an investigation, not its entire database.

Principle 7 — Architecture should be expandable.

New information types, sources, domains, models, analytical methods, and user interfaces must fit without rebuilding the foundation.

Principle 8 — Human expertise matters.

We need to study how experienced researchers, investors, economists, consultants, executives, and other specialists evaluate information and make decisions.

PART II — THE INFORMATION MODEL
4. What exists in the world model?
Our initial analytical dimensions are:

Dimension	Examples
People	Professional roles, public activity, relationships, decisions
Information	Ideas, claims, publications, narratives, evidence
Economics	Capital, transactions, financial incentives, demand
Organizations	Companies, institutions, teams, ownership structures
Environments	Industries, technologies, communities, markets
Time	Historical events, sequences, changes, outcomes
These are not permanent categories.

They describe dimensions of information, not isolated databases.

We should be able to add geography, regulation, infrastructure, products, scientific research, and other domains.

5. The foundational ontology
I propose twelve foundational object types.

Object	What it represents
Entity	Something identifiable: person, company, product, technology, community
Observation	Information captured from a specific source
Assertion	A statement about the world made by a source or extractor
Event	Something that occurred, was announced, or was reported
Relationship	A typed, contextual connection between objects
Context	Conditions that affect interpretation: domain, time, situation, access
Hypothesis	A proposed explanation of evidence
Framework	A reusable analytical or decision-making methodology
Decision	A documented choice made by a person or organization
Outcome	A subsequent observable result
Evidence record	Source provenance and support for an assertion or hypothesis
Analysis record	How the system investigated a question and reached its result
These objects work together.

For example:

A person participates in a conversation. The conversation contains claims. The claims relate to a technology. An organization announces an investment. A hypothesis connects the earlier conversation with the investment.

The system preserves each element independently.

It does not assume the conversation caused the investment.

6. How relationships work
There will be different relationship families.

Structural relationships

Employment, ownership, membership, partnership, organizational roles.

Information relationships

Published, cited, referenced, repeated, challenged, interpreted, responded to.

Economic relationships

Invested, acquired, supplied, contracted, financed, purchased, committed capital.

Social and professional relationships

Collaborated, attended the same event, participated in a public discussion, formally advised.

Temporal relationships

Preceded, followed, overlapped, changed, replaced, became inactive.

Explanatory relationships

Potentially influenced, possibly contributed to, likely depended on, may share a common cause.

The final category is different.

An explanatory relationship is a hypothesis until its evidence supports a stronger conclusion.

Complex interactions should allow multiple participants and roles, rather than forcing everything into two-node connections.

7. Identity resolution
Names are not identities.

Every entity gets a stable internal identifier.

For example:

person_000104
organization_000078
event_000912

A person can have multiple public handles, aliases, or historical professional affiliations.

Those identifiers are mapped to the same entity only when the evidence is sufficient.

Uncertain matches must remain separate until resolved.

An incorrect merge must be reversible without destroying the original evidence.

PART III — THE MEMORY SYSTEM
8. Memory architecture
We will not build one enormous database that every model query must traverse.

Instead, we will maintain a shared evidence and identity foundation with specialized, connected information partitions.

The structure:

SHARED FOUNDATION
    |
    |-- Entity Registry
    |-- Source / Evidence Ledger
    |-- Temporal Event Ledger
    |-- Assertion Registry
    |-- Permission Registry
    |
    +-- INFORMATION PARTITIONS
            |
            |-- People & Professional Networks
            |-- Narratives & Publications
            |-- Financial & Economic Networks
            |-- Organizations & Markets
            |-- Technology & Research
            |-- Decisions & Outcomes
            |-- Private Customer Context
            |-- Additional Future Domains
The partitions aren't necessarily separate physical databases.

They're logical information environments with specific schemas, indexes, processing rules, and permissions.

The shared foundation allows information to be connected across partitions.

9. Contextual memory segmentation
Consider a person who is involved in technology, fashion, venture capital, and gaming.

The system should not retrieve their entire information history when answering a question about their documented venture investments.

It should retrieve the appropriate financial, professional, historical, and organizational context.

If evidence indicates that an idea originated in fashion and subsequently influenced a business decision, the system should expand into that domain.

This produces a dynamic context, constructed according to the question.

We need multiple retrieval mechanisms:

Exact entity and identifier matching.

Keyword and full-text search.

Semantic similarity.

Graph relationship traversal.

Temporal filtering.

Domain-specific retrieval.

Source reliability and evidence filtering.

No single retrieval method should control the whole architecture.

10. Evidence capsules
I propose testing a memory abstraction called an evidence capsule.

A capsule is a compact representation of an information context.

Example:

CAPSULE: AI_INFRASTRUCTURE_042

Relevant entities:
- Organization A
- Organization B
- Technology X

Domains:
- Technology
- Finance
- Infrastructure

Relevant events:
- Investment announcement
- Supplier expansion
- Product release

Assertions:
- Linked to original evidence

Hypotheses:
- Possible increase in downstream demand

Temporal range:
- Defined start and end dates

Access:
- Authorized scope

Cross-links:
- Other relevant capsules
Capsules are not permanent containers of truth.

They are rebuildable representations derived from original evidence.

When their evidence changes, affected capsules are updated.

This is important for keeping information compact while retaining historical accuracy.

11. Different kinds of memory need different retention policies
There should be no universal historical cutoff.

A technological investigation may benefit most from recent events.

A financial investigation may require decades of historical comparison.

A professional relationship may need a long history to understand how a collaboration developed.

We therefore need domain-specific policies for:

Retention periods.

Compression.

Historical summarization.

Source freshness.

Retrieval depth.

Relevance decay.

Legal deletion and correction.

Older information may be less important for one question but essential for another.

The system should preserve useful historical evidence where permitted, while allowing lower-priority derived representations to be compressed or regenerated.

PART IV — THE INFERENCE ENGINE
12. The core proprietary research
This is our highest technical priority.

The proposed research direction is:

Adaptive, evidence-grounded, cross-domain inference guided by documented reasoning frameworks.

The system should understand which information matters, retrieve it efficiently, connect it meaningfully, evaluate possible explanations, and learn from outcomes.

The methodology must be tested against existing approaches.

13. How one investigation works
USER QUESTION / NEW SIGNAL
           |
           v
1. Understand the objective
           |
           v
2. Identify relevant entities and contexts
           |
           v
3. Select appropriate analytical frameworks
           |
           v
4. Construct an investigation plan
           |
           v
5. Retrieve relevant evidence and relationships
           |
           v
6. Identify changes, patterns and anomalies
           |
           v
7. Generate possible explanatory hypotheses
           |
           v
8. Search for supporting and conflicting evidence
           |
           v
9. Determine what remains unknown
           |
           v
10. Expand investigation if justified
           |
           v
11. Produce an evidence-backed conclusion
           |
           v
12. Record predictions and evaluation criteria
           |
           v
13. Learn from future evidence and outcomes
This process must be modular.

Simple questions shouldn't require thirteen expensive stages.

A factual lookup might only need retrieval and verification.

A complex attribution investigation may require the entire pipeline.

14. Investigation depth
The system should not investigate every possible connection indefinitely.

When it discovers a new relationship, it initially performs a limited investigation.

It gathers enough information to understand:

What was observed.

Which entities are involved.

Whether the relationship may be relevant.

What evidence exists.

What remains uncertain.

The relationship is then stored at an appropriate evidentiary status.

If it becomes relevant again, gains new evidence, or affects an important investigation, the system can investigate more deeply.

We should evaluate investigation priority using:

Expected information value, relevance, novelty, uncertainty, potential significance, and computational cost.

This is initially a heuristic, not a proven universal formula.

The objective is to maximize useful intelligence while controlling compute.

15. How hypotheses are handled
Suppose Executive A discusses Technology X.

Six months later, their company acquires a business working on Technology X.

Possible explanations include:

The conversation contributed to the acquisition.

The acquisition was already under consideration.

Both events were caused by wider industry developments.

Several independent factors contributed.

The model should maintain these explanations separately.

Each hypothesis needs:

Supporting evidence.

Contradictory evidence.

Relevant historical comparisons.

Missing information.

An uncertainty estimate.

A revision history.

Conditions that would strengthen or weaken it.

The system should not force one explanation simply because it sounds convincing.

16. Attribution
We will distinguish four attribution problems.

Type	Question
Content attribution	Where was information first observed?
Pathway attribution	Through which observable sources did it travel?
Causal attribution	What evidence suggests one event influenced another?
Outcome attribution	How did particular factors contribute to measurable results?
We will measure them independently.

Complete attribution is often impossible because relevant information may be private, unavailable, or never recorded.

The goal is to improve the quality and calibration of partial attribution.

The system must never mistake a plausible historical explanation for a proven cause.

17. The verification system
We need separate measurements of:

Source authenticity.

Evidence reliability.

Source independence.

Assertion support.

Relationship support.

Information prominence.

Information novelty.

Temporal relevance.

Predictive performance.

A rumor spreading widely is evidence of attention.

It is not necessarily evidence that the rumor is true.

Rumors may be retained as clearly labeled observations because their propagation can itself be informative.

Unverified assertions must not silently become established facts or contaminate downstream conclusions.

18. Autonomous learning
The system updates itself as new evidence arrives.

However, updating its knowledge and training its model weights are different processes.

Knowledge updates can occur continuously.

Model training and major inference-policy updates should be evaluated before deployment.

I recommend seven learning loops:

Learning loop	What improves
Extraction	Identifying claims, events, and relationships
Identity resolution	Matching entities accurately
Retrieval	Finding relevant information efficiently
Attribution	Distinguishing supported relationships from speculation
Framework selection	Choosing useful analytical methods
Forecasting	Improving probability calibration and predictions
Investigation planning	Allocating research effort efficiently
The system must record errors, corrections, and outcomes.

Improvement is an objective to measure, not a guarantee that every new prediction becomes more accurate.

PART V — HUMAN INTELLIGENCE AND EXPERT FRAMEWORKS
19. Understanding human decision-making
We will maintain two complementary representations:

Individual decision records

What was decided, what evidence was publicly or voluntarily disclosed, what alternatives were considered, and what happened afterward.

Evolving decision-pattern models

Tentative summaries of documented professional decision-making patterns across multiple cases.

The second never replaces the first.

A person can act differently in different circumstances.

The system should not assume a fixed personality explains all decisions.

20. What information about people matters?
Relevant information may include:

Professional roles and experience.

Public work and projects.

Explicitly expressed positions.

Published interests and expertise.

Verified professional affiliations.

Public collaborations and interactions.

Documented decisions.

Relevant organizational relationships.

Self-reported decision criteria.

Historical outcomes.

Public information sources they explicitly reference.

Private information can enrich an individual's own workspace when authorized.

We should distinguish verified relationships from speculative social associations.

We should also distinguish professional behavior from private psychological or political profiling. The system can study publicly documented information pathways and decisions without assigning sensitive hidden beliefs to individuals.

21. Expert framework registry
We need a formal registry of analytical methods.

Initial categories:

Venture capital analysis.

Corporate strategy.

Economics.

Quantitative research.

Organizational decision-making.

Market intelligence.

Narrative and information diffusion.

Security and attribution research.

Every framework should contain:

Framework ID
Name
Domain
Source / Expert
Applicable questions
Required inputs
Decision criteria
Assumptions
Analytical method
Alternative explanations
Failure conditions
Expected outputs
Evaluation history
Version
Frameworks can be learned from published literature, authorized interviews, case studies, and expert-led evaluations.

They must be tested rather than automatically treated as correct because an expert recommended them.

The inference engine should eventually select and combine frameworks according to the problem.

22. The founder's research is part of the system
Our own meetings, objections, outreach, experiments, and architectural decisions generate valuable information.

We need a private Founder Intelligence Workspace.

Inputs include:

Expert meetings.

Customer interviews.

Research notes.

Objections and counterarguments.

Founder hypotheses.

Product feedback.

Competitive analysis.

Outreach drafts and responses.

Architecture revisions.

Experiment results.

Each entry records its original context, source, classification, assumptions, and follow-up actions.

A draft is not a sent message.

An interviewee's opinion is not a verified market fact.

A founder hypothesis is not an observed outcome.

These distinctions must remain intact.

PART VI — INFORMATION ACQUISITION
23. The complete information-source universe
We should design the architecture to support many source types, even though the prototype will only implement a few.

Public and institutional information

Company filings, public contracts, government expenditure, legal-entity registries, published research, patents, publications, official announcements, public interviews, and historical archives.

Media and narrative information

Licensed news, public commentary, articles, videos, transcripts, podcasts, and permitted social-platform data.

Economic information

Investments, acquisitions, ownership, corporate relationships, financial disclosures, contracts, supply chains, procurement, and market indicators.

Professional information

Public professional profiles, organizational roles, research contributions, published collaborations, and documented business activity.

Authorized private information

Company documents, CRM data, meeting records, internal research, approved communications, and selected personal AI context.

Original research

Expert interviews, surveys, user research, direct verification, and independent investigations.

Specialized commercial datasets

Private-market intelligence, financial feeds, business-relationship datasets, and other licensed sources.

This is the potential information scope, not permission to collect everything.

Actual ingestion must respect access rights, contractual restrictions, confidentiality, and applicable law.

24. Three information environments
Public and licensed intelligence
Information used under its permitted terms.

Private intelligence
Individual or enterprise data maintained within its authorized environment.

Shared contribution intelligence
Specific information deliberately approved for contribution.

Private customer data does not automatically enter the shared model.

Derived outputs must preserve the restrictions of their underlying evidence.

Users should be able to correct, export, and request deletion of their contributed private information. Treatment of independently obtained public personal data must follow applicable rights and legal obligations rather than an unconditional rule that public data is never removable.

25. Research-driven acquisition
We won't collect everything simply because it exists.

Our investigation engine should also guide what information to acquire next.

For example:

A question requires understanding an organizational investment relationship.

The system identifies missing information concerning the transaction.

It checks permitted public records and relevant licensed sources.

If still unresolved, it records the evidence gap.

Where worthwhile, a researcher can conduct an authorized interview or request additional documentation.

The acquired information is then incorporated into the evidence system.

Information acquisition becomes problem-directed rather than indiscriminate.

PART VII — PRODUCTS AND EXPERIENCE
26. The first product interface
The preferred experience is messaging.

A customer should be able to ask an intelligence question in a familiar conversation.

Example:

Investigate the relationship between two AI infrastructure companies. Find the important people, financial connections, relevant public discussions, and possible implications.

The system should return:

What we found

A short explanation of the most relevant documented connections.

Why it matters

The practical or economic significance.

What might be happening

Clearly identified explanatory hypotheses.

What could happen next

Potential developments and their uncertainty.

Evidence

Relevant citations and source records.

What's missing

Information that would materially improve the conclusion.

No graph visualization should be required for ordinary use.

27. Product channels
Initial preference: Messaging-first.

Candidate implementations include official WhatsApp business messaging and a simple internal chat interface for development.

iMessage compatibility can be evaluated later.

Subsequent interfaces:

MCP for supported AI assistants.

CLI for advanced researchers.

APIs for AI companies.

Slack and enterprise integrations.

Dedicated research workspace when useful.

Every interface should call the same underlying intelligence service.

28. Proactive agent capabilities
The system should eventually:

Answer questions.

Monitor selected subjects.

Detect unusual changes.

Initiate bounded investigations.

Produce scheduled briefings.

Maintain a research watchlist.

Draft outreach and research reports.

Update authorized customer workflows.

Suggest follow-up investigations.

External actions such as sending messages, changing records, or making commitments should follow explicit authorization and approval rules.

Untrusted source content must not be allowed to issue instructions to the agent.

29. Executive intelligence and wearables
The wearable concept is intended for a limited number of high-value enterprise customers.

It is not a mass hardware giveaway.

A recording device could be bundled with a substantial enterprise contract to make authorized meetings easier to document and search.

Possible future capabilities:

Meeting recording with appropriate authorization.

Transcription.

Summaries.

Decision extraction.

Follow-up tracking.

Private contextual memory.

Secure enterprise retrieval.

Retention, consent, participant rights, and whether raw audio is necessary remain to be determined.

This is not required for the initial prototype.

PART VIII — BUSINESS MODEL
30. Potential customers
We currently have several plausible markets.

Customer	Existing problem	Potential product
Founders	Fragmented research and missed developments	Personal intelligence
VCs and investment teams	Discovering companies and evaluating opportunities	Market and relationship intelligence
Corporate strategy teams	Understanding competitors, partnerships, and market changes	Strategic intelligence
Executives	Too much disconnected information	Private decision-support agent
Security and media teams	Difficult information attribution and emerging risks	Narrative and integrity intelligence
AI companies	Need for external, continuously updated evidence	Intelligence infrastructure API
No initial paying customer has been selected or validated yet.

We should use a scoring process based on urgency, budget, data availability, ability to demonstrate value, sales complexity, and accessibility through our network.

The first commercial product can be narrower than the underlying architecture without making any information domain secondary.

31. How we compete
We must compare against products customers already pay for.

Relevant references include:

Graphika.

CB Insights.

Palantir.

Recorded Future.

AlphaSense.

Existing GraphRAG and AI-memory platforms.

Our potential advantage is the combination of:

Cross-domain information relationships + historical evidence + source-aware inference + expert reasoning frameworks + real-world outcome evaluation + accessible product interfaces.

That combination is a research thesis, not yet a proven competitive moat.

We must compare equivalent tasks, not marketing statements.

32. Monetization
Possible models:

Personal intelligence: Affordable subscriptions or usage-based plans.

Team intelligence: Workspace subscriptions and collaborative research capabilities.

Enterprise intelligence: Annual contracts, private deployments, data integrations, advanced controls, and specialist support.

Infrastructure: API access, metered inference, monitoring, and licensed intelligence services.

Research services: Paid investigations or pilot projects using the underlying system.

The first revenue goal is to obtain a genuine financial commitment that validates an important customer problem.

We should not invent pricing before learning what customers would actually pay.

33. Distribution and reputation
The company can maintain a private technical core while being publicly known for its research.

Public activities may include:

Explaining information systems and attribution.

Publishing selected benchmarks.

Demonstrating evidence-backed investigations.

Discussing technological limitations.

Publishing original research where rights permit.

Inviting qualified collaborators.

Private assets include proprietary implementations, confidential customer data, commercial agreements, and unpublished research.

The audience should grow because the work is useful and credible.

The core development group should remain selective rather than becoming an unrestricted public contribution network.

PART IX — ENGINEERING
34. Initial technical architecture
The first prototype should be a modular application, not a complicated microservice platform.

Component	Proposed starting technology
Primary language	Python
Backend	FastAPI
Structured storage	PostgreSQL
Semantic retrieval	pgvector
Source archive	Local or S3-compatible object storage
Graph representation	Typed relationships in PostgreSQL
Graph analysis	NetworkX where needed
Model inference	Replaceable open-source or hosted models
Background jobs	Simple durable job queue
Initial interface	Messaging-style client
Agent interfaces	MCP and API later
Evaluation	Automated tests and historical replay
These are engineering defaults, not final selections.

We may adopt a specialized graph engine when real query requirements justify it.

35. Model architecture
Separate the following responsibilities:

Extraction models.

Entity-resolution models.

Semantic representations.

Relationship classification.

Framework selection.

Hypothesis generation.

Evidence checking.

Forecasting.

Response generation.

Some functions may initially share the same language model.

Others may be better implemented using deterministic rules or conventional statistical methods.

Fine-tuning comes after building validated training and evaluation data.

Training a large foundation model is not a prerequisite.

36. Internal system boundaries
The initial code should maintain distinct modules for:

core/
    identity/
    ontology/
    evidence/
    temporal/
    permissions/

ingestion/
    adapters/
    extraction/
    normalization/

memory/
    partitions/
    graph/
    retrieval/
    capsules/

inference/
    planner/
    frameworks/
    hypotheses/
    attribution/
    verification/

learning/
    feedback/
    historical_replay/
    evaluation/

agents/
    monitoring/
    investigations/
    notifications/

interfaces/
    api/
    messaging/
    mcp/
    cli/

workspace/
    research/
    meetings/
    decisions/
This is a proposed logical organization, not yet an exact repository structure.

It keeps responsibilities separate while permitting shared deployment.

37. Portability
The system of record must not live inside ChatGPT, Claude, or any single AI vendor.

We need:

Versioned schemas.

Stable entity IDs.

Source-preserving exports.

Portable structured data.

Rebuildable search indexes.

Model-provider abstraction.

Reproducible inference records.

Versioned research decisions.

Documented APIs.

Secure migration procedures.

Research and founder knowledge should be exportable as structured records with readable Markdown summaries and original permitted references.

Other AI agents should consume explicit specifications rather than infer the company's architecture from incomplete chat messages.

PART X — TESTING AND EVALUATION
38. The first prototype's actual objective
The first prototype must demonstrate that the architecture can:

Acquire information → structure it → segment it → connect it → infer relationships → test historical hypotheses → generate predictions → evaluate its mistakes.

The objective is not complete accuracy.

It is evidence that the system can learn useful relationships and produce measurable intelligence within a constrained information environment.

39. First historical experiment
Choose an ecosystem with:

Dense historical information.

Multiple interacting domains.

Documented people and organizations.

Observable economic or organizational outcomes.

Accessible potential buyers.

A candidate is the AI infrastructure ecosystem because it connects technical research, public narratives, executives, companies, financing, and supply chains.

But selection should ultimately follow commercial validation and source feasibility.

For a historical test:

Choose a past cutoff date.

Provide only information known to the system by that date.

Ask it to identify possible subsequent developments.

Record predictions before revealing future evidence.

Reveal what happened afterward.

Evaluate accuracy, uncertainty, and missed signals.

Compare with simpler retrieval and forecasting baselines.

Save the complete experiment for future model improvements.

The system must not accidentally use future information during historical reconstruction.

40. Evaluation metrics
Metric	What it measures
Entity-resolution accuracy	Correct identities and avoided false merges
Assertion accuracy	Fidelity to underlying source evidence
Relationship precision	Proportion of proposed connections supported by evaluation evidence
Evidence recall	Relevant information retrieved versus missed
Attribution quality	Ability to distinguish documented pathways from unsupported causal claims
Forecast calibration	Whether predicted probabilities align with actual frequencies
Historical correctness	Absence of future-information leakage
Context efficiency	Quality relative to retrieval and inference cost
Learning improvement	Measured change across repeated evaluation rounds
User utility	Whether investigations improve real research decisions
The system must also be able to abstain when available evidence is insufficient.

41. Mandatory failure tests
Before calling the prototype reliable, it must handle:

Two different people with the same name.

One claim repeated by many dependent sources.

Conflicting company announcements.

An investment announced but never completed.

Two similar ideas arising independently.

A source correction or withdrawal.

An important missing link.

A historical query restricted to past evidence.

Private information from an unauthorized organization.

A previously supported hypothesis weakened by new evidence.

A prediction that fails.

An incorrect expert framework selected for an investigation.

The architecture must make these failures observable and correctable.

PART XI — BUILDING WITH LIMITED RESOURCES
42. Current resources
The project currently has:

A founding team.

Some software-development experience.

Access to modern AI coding and research tools.

Potential technical and professional connections.

No committed development budget.

An interest in grants, research support, and early customer funding.

Development should therefore begin locally and avoid expensive infrastructure commitments.

The architecture should support later cloud migration without requiring a rewrite.

43. Implementation milestones
Milestone A — Foundational contracts

Define the ontology, source records, evidence states, timestamps, relationship types, permissions, and evaluation criteria.

Milestone B — Information memory

Build source ingestion, entity resolution, structured events, basic graph relationships, and queryable history.

Milestone C — Segmented retrieval

Implement domain projections, semantic indexing, relationship traversal, and context selection.

Milestone D — Inference

Implement hypothesis creation, evidence comparison, alternative explanations, and reproducible investigation records.

Milestone E — Learning

Implement historical replay, scoring, correction handling, and feedback loops.

Milestone F — Product

Create a messaging-style research interface, ongoing monitoring, and approved notifications.

Milestone G — Validation

Demonstrate with real historical cases and prospective customers.

The milestones are dependency-based. A compressed prototype can combine them, but implementation speed must not replace testing.

44. Cost discipline
Track:

Cost per observation.

Cost per extracted assertion.

Cost per supported relationship.

Cost per investigation.

Cost per historical evaluation.

Cost per useful intelligence signal.

Average latency.

Storage and retrieval costs.

Use incremental processing, caching, staged inference, and computation budgets.

Do not repeatedly process unchanged evidence.

Use expensive models only when simpler methods prove inadequate.

PART XII — RESEARCH, PEOPLE, AND COMPANY DEVELOPMENT
45. Researchers and specialists
A small invited group should help us evaluate the system.

Relevant expertise includes:

Knowledge graphs and information retrieval.

Temporal data modeling.

Causal inference and statistics.

Economics and financial networks.

Professional decision-making research.

Narrative and information diffusion.

Security and privacy engineering.

Enterprise workflow design.

Initially, specialists may be advisors, research collaborators, or scoped paid contributors rather than full-time employees.

Each person should have a clearly defined problem to investigate.

46. Customer discovery
We must understand:

What information customers already purchase.

What investigations they perform repeatedly.

What tools they currently use.

What conclusions are difficult to reach.

What missing information causes costly decisions.

What existing products get right.

What those products fail to provide.

What improvements customers would actually pay for.

Each interview should become a structured, permission-controlled research record.

47. Funding
We should explore early customer-paid pilots, incubators, research grants, startup grants, and eventually investors.

Funding applications should emphasize measurable research objectives rather than claims that we've already created a universal world model.

The initial evidence should demonstrate that the architecture works and that somebody values its output.

48. Public presence and private development
The company's technical core can remain private.

Research, demonstrations, technical explanations, and selected progress can be public.

We want people to understand the importance of information provenance, relationships, and independent intelligence.

The public identity should attract researchers, potential customers, and collaborators without disclosing confidential implementation or customer data.

PART XIII — DOCUMENTATION AND HANDOFFS
49. Foundational documentation
Before substantial autonomous implementation, produce the following controlled specifications:

Document	Purpose
VISION.md	Purpose, principles, full scope, boundaries
DECISIONS.md	Confirmed decisions, assumptions, unresolved experiments
ONTOLOGY.md	Objects, schemas, identity, relationships
EVIDENCE.md	Provenance, verification, source independence
TEMPORAL.md	Historical events, valid time, knowledge time
MEMORY.md	Segmentation, indexes, capsules, retrieval
INFERENCE.md	Query planning, attribution, hypotheses
FRAMEWORKS.md	Expert reasoning methods and selection
LEARNING.md	Updating, feedback, training, evaluation
SECURITY.md	Permissions, isolation, encryption, deletion
PRODUCT.md	User experience, agents, interfaces
DATA_SOURCES.md	Source registry, permissions, acquisition
EVALUATION.md	Benchmarks and acceptance tests
ECONOMICS.md	Operating costs, customers, pricing experiments
ROADMAP.md	Milestones and dependencies
AGENTS.md	Instructions and constraints for coding agents
The documents must be version-controlled.

An architectural change should update the relevant specification and record why it changed.

50. AI-agent handoff contract
Every handoff should contain:

Objective: What the agent must accomplish.

Relevant architecture: Which existing components it may use or modify.

Confirmed requirements: Decisions that must be preserved.

Inputs: Approved data and accessible resources.

Constraints: Permissions, technical boundaries, cost limits, prohibited assumptions.

Outputs: Required files, schemas, code, tests, or findings.

Acceptance criteria: How we determine whether the task is complete.

Open questions: What the agent must flag instead of inventing.

Change log: What was modified and why.

This prevents a research agent from silently making foundational product decisions and prevents a coding agent from implementing a different architecture.

PART XIV — WHAT IS DECIDED AND WHAT MUST STILL BE PROVEN
51. Confirmed product decisions
We are building an information world model.

Relationships are foundational.

People, economics, narratives, and organizations are interconnected, not hierarchical priorities.

The ontology must support nuanced relationships, events, and decisions.

Memory must be segmented but cross-domain.

Historical reasoning and attribution matter.

Expert analytical frameworks belong in the inference system.

The model should learn from new evidence and measurable mistakes.

Autonomous investigation is required.

Compute efficiency matters.

Messaging is the preferred first experience.

MCP, CLI, and APIs are later access channels.

Private enterprise intelligence is strategically important.

Wearables are a selective future enterprise channel.

The founding research group should remain small and deliberate.

Commercial value must be demonstrated early.

Everything must be portable, documented, and expandable.

52. Proposed engineering defaults
These are recommendations, not established facts:

Evidence-native temporal records as the system of record.

Shared identity spine with domain-specific projections.

Rebuildable evidence capsules.

Adaptive retrieval and investigation depth.

Explicit hypothesis tracking.

Separate learning loops for extraction, retrieval, attribution, and forecasting.

PostgreSQL and Python for the initial implementation.

Existing models before custom training.

Local-first development.

Historical replay before claims of predictive superiority.

53. Research questions requiring experiments
Which memory partitioning method performs best?

Do evidence capsules actually improve retrieval efficiency?

Can our inference methodology outperform ordinary RAG and GraphRAG?

Which expert frameworks improve different types of analysis?

Can relationship-based reasoning improve historical forecasting?

Can attribution accuracy improve with additional evidence without creating excessive false positives?

Which customer use case produces the earliest willingness to pay?

What information sources are worth licensing?

Which parts of the inference system are genuinely differentiating?

When does specialized model training become economically justified?

We should not present these as solved.

FINAL DEFINITION
We are building a continuously evolving information world model that connects people, ideas, organizations, economic activity, decisions, and historical events through an evidence-backed relational architecture.

The system maintains segmented, interconnected memory; investigates relationships using documented analytical frameworks; distinguishes observed facts from inferred explanations; learns through new evidence and historical outcomes; and delivers useful intelligence through familiar interfaces.

The long-term goal is to create a proprietary inference infrastructure capable of making fragmented information understandable, historically traceable, economically useful, and increasingly predictive.

The first technical milestone is proving that segmented information, cross-domain relationships, and evidence-grounded inference produce measurable advantages over simpler approaches.

The first commercial milestone is finding a customer who values that improvement enough to pay for it.

The architecture is intended to accommodate the wider ambition from the beginning, even while the initial prototype operates on a limited, deliberately selected information environment.

End of Master Definition v1.0.

Important external checks
I verified several practical details that affect how this draft should eventually be implemented.

Existing technology: Graphiti already supports incremental temporal context graphs. Microsoft GraphRAG already offers local, global, and DRIFT retrieval approaches. Our inference and segmentation ideas therefore need direct benchmarks against these systems before we call them proprietary improvements. 

Zep Documentation
+2

Competition: Graphika explicitly describes an AI World Model connecting narratives, actors, and communities. We need to compete on verified capability, not claim that the category doesn't exist. 

Graphika

Messaging: WhatsApp's official business platform supports messaging through its API and uses templates for certain outbound messages. ChatGPT's custom MCP support also has plan and permission differences. These should be considered when selecting our eventual integration strategy. 

Postman API Network
+1

Available data: The SEC provides public filing APIs, while GLEIF offers legal-entity and corporate-relationship information. These could support early financial and organizational investigations without purchasing an entire commercial dataset. 

data.sec.gov
+1

Funding: India's Startup India Seed Fund Scheme describes potential support of up to ₹20 lakh for proof-of-concept and prototype work and up to ₹50 lakh through specified debt-linked instruments for commercialization, subject to eligibility and incubator selection. This is one avenue worth evaluating—not funding we can assume we'll receive. 

seedfund.startupindia.gov.in

This draft now gives us a common reference for what the company is trying to build. The next stage should turn its proposed objects, inference rules, memory operations, and learning loops into formal technical contracts, then test them against the real use cases you've described.

specifically - i need you to write tehincal information and capabilities and how do we achieve that and whqat does stuff look like from the ground up and why and all the relevant information around that- sneding it to my ex technical cofounder - he will go through it and let me know all the problems and fixes and how i shold make the ammends and fix it - i trust this guy so dont hold back
This is the version I'd send to your former technical co-founder. It is deliberately more rigorous than the previous architecture: I've included data structures, processing pipelines, inference mechanisms, storage choices, model training, evaluation methods, system boundaries, technical risks, and implementation priorities.

I've also included specific decisions for him to challenge, because we need his criticism of the engineering, not just his opinion of the idea.

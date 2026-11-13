# Roadmap: from architecture to evidence

This is an intent and sequencing guide, not a delivery promise. Exit criteria matter more than dates.

## v0 — Architecture foundation (current)

**Goal:** give humans and coding agents a durable, falsifiable blueprint.

**Artifacts:** architecture, decision/status log, contributor rules, handoff, and phased roadmap.

**Exit:** a technical reviewer can identify assumptions, missing contracts, and bounded experiments without mistaking documentation for a product.

## v0.1 — Research and contract selection

**Goal:** choose a narrow, authorized historical corpus and evaluate competing foundations.

**Work:** source/license review; M0 object contracts; a point-in-time availability policy; prototype data fixtures; comparison of storage/retrieval choices; explicit evaluation plan and cost budget.

**Exit:** the team can explain what enters the system, what each record means, how permissions propagate, and how success will be scored.

## v0.2 — Evidence-native vertical slice

**Goal:** prove the canonical path on a small corpus.

**Work:** capture observations; extract versioned candidate entities/assertions/events; identity review; evidence links; temporal query; restricted-scope retrieval; inspectable source trace.

**Exit:** a user can trace a finding back to permitted raw evidence and distinguish source content, extraction, and inference.

## v0.3 — Investigation and replay

**Goal:** make reasoning inspectable and historically fair.

**Work:** bounded query planner; alternatives/hypothesis records; framework versioning; time-cutoff replay; leakage tests; baseline comparison.

**Exit:** a prior-time question can be rerun using only then-available information, with a logged evidence trail and costs.

## v0.4 — Forecast and feedback loop

**Goal:** demonstrate learning claims with measurement.

**Work:** prediction contract; timestamped forecast commitment; outcome capture; scoring; error taxonomy; controlled policy/model changes and rollback.

**Exit:** at least one predeclared task has a reproducible forecast/outcome evaluation and a documented response to error.

## v1 — Narrow product pilot

**Goal:** turn the demonstrated loop into a useful, secure workflow for one validated ecosystem.

**Work:** buyer discovery, authorized data operations, messaging interface, workspace isolation, monitoring, reliability/cost controls, and user feedback.

**Exit:** usefulness, economics, permissions, and operational quality are demonstrated for a scoped user group—not assumed from technical novelty.

## Later versions

Additional domains, integrations, enterprise workflows, monitoring, expanded automation, and scale work follow only when the evidence foundation and pilot justify them. No roadmap phase authorizes collecting private data, bypassing licenses, or declaring causal/predictive performance without measurement.

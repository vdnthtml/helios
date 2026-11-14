# Evaluation and acceptance

## First meaningful demonstration

Choose a bounded real historical ecosystem with people, information, organizations, technology or industry, economic activity, documented decisions, and observable later outcomes. AI infrastructure is a candidate. Source availability and potential buyer usefulness should drive selection.

Exercise all original D-01 through D-15 requirements: real ingestion; extraction; identity; typed relations; segmentation; cross-domain retrieval; alternatives; fact/inference separation; past-state replay; committed prediction; outcome scoring; error feedback; compute accounting; messaging delivery; inspectable evidence/processing trace.

## Comparative experiment

Compare conventional RAG, a verified existing GraphRAG implementation, and the proposed IWM on the same corpus, questions, cutoff conditions, model/budget assumptions, and outcome rules. Include simple forecasting baselines. Ablate capsules, segmentation, adaptive expansion, expert frameworks, and explicit hypothesis evaluation separately before attributing gains to the combined system.

Measure extraction fidelity, identity false merges, relationship precision, evidence recall, cross-domain completeness, citation correctness, independent-source handling, temporal fidelity, attribution false positives, cost, latency, and researcher usefulness. Use appropriate probability scoring and calibration for forecasts, and suitable quantitative errors for numeric targets. Define thresholds and adjudication before evaluating; no numeric success threshold was agreed in the source.

## Historical leakage controls

Specify whether evidence must have been publicly available or actually ingested at cutoff. Freeze eligible records, identity mappings, summaries, graph projections, caches, and other derived representations. Commit the forecast with target, horizon, probability, resolution rule, evidence IDs, versions, and configuration before revealing the outcome.

Additional review risk recorded in this baseline: modern pretrained models may already know historical outcomes even if retrieval is cutoff-safe. Disclose this limitation; use blinded/controlled cases where practical and prospective forecasts to strengthen validation. Do not label a retrospective run equivalent to an actual contemporaneous prediction.

## Mandatory failure scenarios

| Scenario | Expected behavior |
|---|---|
| Same-name people; name changes; mistaken merges | Preserve separate candidates; reverse errors without losing provenance |
| One claim repeated by 100 dependent sources | Count attention separately from independent corroboration |
| Announced, delayed, canceled, or completed transactions | Preserve distinct statuses and dates |
| Similar ideas without documented transmission | Maintain independent/common-source alternatives |
| Correction, withdrawal, or lost support | Revise dependencies and current conclusions; retain appropriate history |
| Multiple domains and one entity | Retrieve across projections with consistent identity |
| Historical query and later-derived summary | Exclude future evidence and future-contaminated context |
| Cross-tenant/private-source answer | Deny unauthorized retrieval and derived disclosure |
| Failed forecast or expert framework | Retain result, score, error, and relevant version |
| Repeated ingestion | Avoid duplicate processing while retaining meaningful propagation events |
| Exhausted research budget | Stop predictably and explain evidence limitations |
| Model upgrade | Preserve reproducible comparison and rollback information |

Status: evaluation specification only; no product tests or experiments have run. The next research phase must propose datasets, sample sizes, adjudication, baselines, metrics, thresholds, and expected costs.

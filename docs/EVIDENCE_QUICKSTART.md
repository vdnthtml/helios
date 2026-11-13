# First evidence feature

Run from the repository root with Python 3.11+:

```sh
python -m unittest discover -s tests -v
```

No network, model API key, GPU, or external dependency is needed for these contract tests. All fixture names/content are explicitly synthetic; they are not real-world research findings.

```python
from datetime import datetime, timezone
from helios.evidence import Ledger

ledger = Ledger("local.db")
company = ledger.create_entity("workspace-1", "organization", "Example fixture")
observation = ledger.observe(
    "workspace-1", "fixture", "record-1", "fixture://record-1",
    "Example fixture announced a proposed expansion.",
)
ledger.assert_relation(
    "workspace-1", observation.id, company.id, "expands",
    "announced a proposed expansion", object_value="capacity",
    modality="intended", event_status="announced",
)
print(ledger.assertions("workspace-1", as_of=datetime.now(timezone.utc)))
ledger.close()
```

This is a SQLite reference ledger, not the production database or an authenticated API. Only trusted in-process callers can use it safely. Scope strings are not proof of authorization. Publication dates do not backdate system ingestion. Source quotes establish traceability, not truth/entailment. See BUILD_PLAN for exact limitations, model strategy and next adapters.

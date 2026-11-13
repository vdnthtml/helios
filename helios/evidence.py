"""Immutable evidence records. No model may promote an assertion to truth here."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
import sqlite3
from typing import Callable, Literal
from uuid import uuid4


def timestamp(value: datetime) -> str:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("timezone-aware timestamp required")
    return value.astimezone(timezone.utc).isoformat(timespec="microseconds")


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def required(*values: str) -> None:
    if any(not isinstance(v, str) or not v.strip() for v in values):
        raise ValueError("non-empty text required")


def canonical(value: dict) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


@dataclass(frozen=True)
class Observation:
    id: str
    tenant_id: str
    source_id: str
    source_item_id: str
    source_uri: str
    content: str
    content_hash: str
    published_at: str | None
    recorded_at: str


@dataclass(frozen=True)
class Entity:
    id: str
    tenant_id: str
    kind: str
    name: str
    recorded_at: str


@dataclass(frozen=True)
class Assertion:
    id: str
    tenant_id: str
    observation_id: str
    subject_id: str
    predicate: str
    object_id: str | None
    object_value: str | None
    evidence_quote: str
    modality: str
    event_status: str
    valid_from: str | None
    valid_to: str | None
    recorded_at: str
    supersedes_id: str | None
    extractor_version: str
    epistemic_state: str = "source_asserted"


SCHEMA = """
CREATE TABLE IF NOT EXISTS records (
 id TEXT PRIMARY KEY,
 kind TEXT NOT NULL CHECK(kind IN ('entity','observation','assertion')),
 tenant_id TEXT NOT NULL,
 recorded_at TEXT NOT NULL,
 payload TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS record_scope_time ON records(tenant_id, kind, recorded_at);
CREATE TABLE IF NOT EXISTS identifiers (
 tenant_id TEXT NOT NULL,
 namespace TEXT NOT NULL,
 external_id TEXT NOT NULL,
 entity_id TEXT NOT NULL REFERENCES records(id),
 PRIMARY KEY(tenant_id, namespace, external_id)
);
"""


class Ledger:
    """SQLite reference adapter, not the selected production store.

    Trusted callers supply scope. This is not authentication or tenant RLS.
    Public-availability replay, identity merges, search and model calls are later.
    """
    def __init__(self, path: str = ":memory:", *, clock: Callable[[], datetime] = utcnow):
        self.db = sqlite3.connect(path)
        self.db.execute("PRAGMA foreign_keys = ON")
        self.db.executescript(SCHEMA)
        self.clock = clock

    def close(self) -> None:
        self.db.close()

    def _put(self, kind: str, record: Observation | Entity | Assertion) -> None:
        self.db.execute("INSERT INTO records VALUES (?, ?, ?, ?, ?)",
                        (record.id, kind, record.tenant_id, record.recorded_at,
                         canonical(asdict(record))))

    def _get(self, record_id: str, tenant: str, kind: str) -> dict:
        row = self.db.execute(
            "SELECT payload FROM records WHERE id=? AND tenant_id=? AND kind=?",
            (record_id, tenant, kind)).fetchone()
        if row is None:
            raise ValueError("record unavailable in requested scope")
        return json.loads(row[0])

    def create_entity(self, tenant: str, kind: str, name: str, *,
                      namespace: str | None = None, external_id: str | None = None) -> Entity:
        required(tenant, kind, name)
        if (namespace is None) != (external_id is None):
            raise ValueError("identifier requires both namespace and value")
        if namespace is not None:
            required(namespace, external_id)
        # The caller must use an authoritative, source-qualified namespace.
        # Names and aliases are never identity keys.
        with self.db:
            if namespace is not None:
                hit = self.db.execute(
                    "SELECT entity_id FROM identifiers WHERE tenant_id=? AND namespace=? AND external_id=?",
                    (tenant, namespace, external_id)).fetchone()
                if hit:
                    found = Entity(**self._get(hit[0], tenant, "entity"))
                    if found.kind != kind:
                        raise ValueError("identifier already belongs to another entity type")
                    return found
            entity = Entity(str(uuid4()), tenant, kind, name, timestamp(self.clock()))
            self._put("entity", entity)
            if namespace is not None:
                self.db.execute("INSERT INTO identifiers VALUES (?, ?, ?, ?)",
                                (tenant, namespace, external_id, entity.id))
            return entity

    def observe(self, tenant: str, source: str, item: str, uri: str, content: str, *,
                published_at: datetime | None = None) -> Observation:
        required(tenant, source, item, uri, content)
        # URI may be a permitted internal document reference, not only a public URL.
        digest = hashlib.sha256(content.encode()).hexdigest()
        published = timestamp(published_at) if published_at else None
        identity = dict(tenant=tenant, source=source, item=item, uri=uri,
                        content_hash=digest, published_at=published)
        record_id = hashlib.sha256(canonical(identity).encode()).hexdigest()
        with self.db:
            existing = self.db.execute(
                "SELECT payload FROM records WHERE id=? AND kind='observation' AND tenant_id=?",
                (record_id, tenant)).fetchone()
            if existing:
                return Observation(**json.loads(existing[0]))
            observation = Observation(record_id, tenant, source, item, uri, content,
                                      digest, published, timestamp(self.clock()))
            self._put("observation", observation)
            return observation

    def assert_relation(self, tenant: str, observation_id: str, subject_id: str,
                        predicate: str, evidence_quote: str, *,
                        object_id: str | None = None, object_value: str | None = None,
                        modality: Literal["reported", "intended", "possible", "denied"] = "reported",
                        event_status: Literal["unspecified", "proposed", "announced", "committed", "completed", "cancelled"] = "unspecified",
                        valid_from: datetime | None = None, valid_to: datetime | None = None,
                        supersedes_id: str | None = None,
                        extractor_version: str = "manual-v1") -> Assertion:
        required(tenant, observation_id, subject_id, predicate, evidence_quote, extractor_version)
        if (object_id is None) == (object_value is None):
            raise ValueError("provide exactly one object entity or value")
        if object_value is not None:
            required(object_value)
        if object_id is not None:
            required(object_id)
        if modality not in {"reported", "intended", "possible", "denied"}:
            raise ValueError("invalid assertion modality")
        if event_status not in {"unspecified", "proposed", "announced", "committed", "completed", "cancelled"}:
            raise ValueError("invalid event status")
        start = timestamp(valid_from) if valid_from else None
        end = timestamp(valid_to) if valid_to else None
        if end and not start:
            raise ValueError("valid_to requires valid_from")
        if start and end and end <= start:
            raise ValueError("valid_to must follow valid_from")
        with self.db:
            obs = self._get(observation_id, tenant, "observation")
            subject = self._get(subject_id, tenant, "entity")
            refs = [obs, subject]
            if object_id:
                refs.append(self._get(object_id, tenant, "entity"))
            if evidence_quote not in obs["content"]:
                raise ValueError("evidence quote not found in observation")
            # A source span establishes traceability, not semantic entailment/truth.
            now = timestamp(self.clock())
            if supersedes_id:
                previous = self._get(supersedes_id, tenant, "assertion")
                if previous["subject_id"] != subject_id or previous["predicate"] != predicate:
                    raise ValueError("a correction must target the same subject and predicate")
                refs.append(previous)
            if any(ref["recorded_at"] > now for ref in refs):
                raise ValueError("dependency is newer than processing time")
            assertion = Assertion(str(uuid4()), tenant, observation_id, subject_id,
                                  predicate, object_id, object_value, evidence_quote,
                                  modality, event_status, start, end, now,
                                  supersedes_id, extractor_version)
            self._put("assertion", assertion)
            return assertion

    def assertions(self, tenant: str, *, as_of: datetime,
                   valid_at: datetime | None = None, include_history: bool = False) -> list[Assertion]:
        """What this ledger actually recorded by as_of (not public-availability replay).

        Correction records are append-only; later corrections never hide a row in
        an earlier snapshot. Concurrent conflicting corrections remain visible.
        """
        required(tenant)
        cutoff = timestamp(as_of)
        rows = self.db.execute(
            "SELECT payload FROM records WHERE tenant_id=? AND kind='assertion' "
            "AND recorded_at<=? ORDER BY recorded_at,id", (tenant, cutoff)).fetchall()
        candidates = [Assertion(**json.loads(r[0])) for r in rows]
        superseded = {a.supersedes_id for a in candidates if a.supersedes_id}
        result = []
        for a in candidates:
            deps = [self._get(a.observation_id, tenant, "observation"),
                    self._get(a.subject_id, tenant, "entity")]
            if a.object_id:
                deps.append(self._get(a.object_id, tenant, "entity"))
            if any(d["recorded_at"] > cutoff for d in deps):
                continue
            if not include_history and a.id in superseded:
                continue
            if valid_at:
                point = timestamp(valid_at)
                if a.valid_from and a.valid_from > point:
                    continue
                if a.valid_to and a.valid_to <= point:
                    continue
            result.append(a)
        return result

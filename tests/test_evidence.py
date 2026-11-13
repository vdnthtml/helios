"""Synthetic fixtures: these organizations and people are not real-world findings."""
from datetime import datetime, timedelta, timezone
import tempfile
import unittest
from pathlib import Path
from helios.evidence import Ledger

T0 = datetime(2026, 1, 1, tzinfo=timezone.utc)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.now = T0
        self.ledger = Ledger(clock=lambda: self.now)
        self.a = self.ledger.create_entity("a", "organization", "Fixture Alpha")
        self.b = self.ledger.create_entity("a", "organization", "Fixture Beta")
        self.obs = self.ledger.observe("a", "fixture", "item-1", "fixture://item-1",
                                      "Alpha announced a proposed acquisition of Beta.",
                                      published_at=T0 - timedelta(days=1))

    def tearDown(self):
        self.ledger.close()

    def assertion(self, **kw):
        return self.ledger.assert_relation("a", self.obs.id, self.a.id, "acquires",
                                          self.obs.content, object_id=self.b.id, **kw)

    def test_same_name_people_are_distinct(self):
        x = self.ledger.create_entity("a", "person", "Fixture Same Name")
        y = self.ledger.create_entity("a", "person", "Fixture Same Name")
        self.assertNotEqual(x.id, y.id)

    def test_source_qualified_identity_is_reused(self):
        x = self.ledger.create_entity("a", "person", "Name A", namespace="fixture:author", external_id="1")
        y = self.ledger.create_entity("a", "person", "Alias A", namespace="fixture:author", external_id="1")
        self.assertEqual(x.id, y.id)
        z = self.ledger.create_entity("a", "person", "Name A", namespace="different:author", external_id="1")
        self.assertNotEqual(x.id, z.id)

    def test_external_id_does_not_cross_scope_or_type(self):
        x = self.ledger.create_entity("a", "person", "Fixture", namespace="fixture:author", external_id="1")
        y = self.ledger.create_entity("b", "person", "Fixture", namespace="fixture:author", external_id="1")
        self.assertNotEqual(x.id, y.id)
        with self.assertRaises(ValueError):
            self.ledger.create_entity("a", "organization", "Wrong", namespace="fixture:author", external_id="1")

    def test_observation_idempotency_retains_first_ingestion(self):
        self.now += timedelta(days=1)
        again = self.ledger.observe("a", "fixture", "item-1", "fixture://item-1", self.obs.content,
                                    published_at=T0 - timedelta(days=1))
        self.assertEqual(self.obs, again)

    def test_changed_body_produces_new_revision(self):
        revised = self.ledger.observe("a", "fixture", "item-1", "fixture://item-1", "Changed body")
        self.assertNotEqual(self.obs.id, revised.id)
        self.assertNotEqual(self.obs.content_hash, revised.content_hash)

    def test_quoted_source_required(self):
        with self.assertRaises(ValueError):
            self.ledger.assert_relation("a", self.obs.id, self.a.id, "acquires",
                                        "This sentence is absent", object_id=self.b.id)

    def test_cross_tenant_observation_and_entity_rejected(self):
        outsider = self.ledger.create_entity("b", "organization", "Fixture Elsewhere")
        with self.assertRaises(ValueError):
            self.ledger.assert_relation("b", self.obs.id, outsider.id, "acquires", self.obs.content,
                                        object_value="value")
        with self.assertRaises(ValueError):
            self.ledger.assert_relation("a", self.obs.id, self.a.id, "acquires", self.obs.content,
                                        object_id=outsider.id)

    def test_historical_cutoff_is_ingestion_not_publication(self):
        self.now += timedelta(days=10)
        a = self.assertion(event_status="announced")
        self.assertEqual([], self.ledger.assertions("a", as_of=T0))
        self.assertEqual([a], self.ledger.assertions("a", as_of=self.now))

    def test_correction_does_not_rewrite_history(self):
        old = self.assertion(event_status="announced")
        self.now += timedelta(days=1)
        correction = self.ledger.observe("a", "fixture", "item-2", "fixture://item-2", "Alpha cancelled acquisition of Beta.")
        new = self.ledger.assert_relation("a", correction.id, self.a.id, "acquires", correction.content,
                                          object_id=self.b.id, event_status="cancelled", supersedes_id=old.id)
        self.assertEqual([old], self.ledger.assertions("a", as_of=T0))
        self.assertEqual([new], self.ledger.assertions("a", as_of=self.now))
        self.assertEqual(2, len(self.ledger.assertions("a", as_of=self.now, include_history=True)))

    def test_assertion_is_not_automatically_verified(self):
        a = self.assertion(event_status="announced", modality="intended")
        self.assertEqual("announced", a.event_status)
        self.assertEqual("intended", a.modality)
        self.assertEqual("source_asserted", a.epistemic_state)

    def test_validity_uses_half_open_interval(self):
        self.assertion(valid_from=T0, valid_to=T0 + timedelta(days=1))
        self.assertEqual(1, len(self.ledger.assertions("a", as_of=T0, valid_at=T0)))
        self.assertEqual([], self.ledger.assertions("a", as_of=T0, valid_at=T0 + timedelta(days=1)))
        with self.assertRaises(ValueError):
            self.assertion(valid_from=T0, valid_to=T0)

    def test_unknown_modality_and_status_rejected(self):
        with self.assertRaises(ValueError):
            self.assertion(modality="verified")
        with self.assertRaises(ValueError):
            self.assertion(event_status="probably_completed")

    def test_naive_datetime_rejected(self):
        with self.assertRaises(ValueError):
            self.ledger.assertions("a", as_of=datetime(2026, 1, 1))

    def test_missing_or_two_objects_rejected(self):
        with self.assertRaises(ValueError):
            self.ledger.assert_relation("a", self.obs.id, self.a.id, "acquires", self.obs.content)
        with self.assertRaises(ValueError):
            self.assertion(object_value="duplicate")

    def test_empty_object_id_rejected(self):
        with self.assertRaises(ValueError):
            self.ledger.assert_relation("a", self.obs.id, self.a.id, "acquires", self.obs.content,
                                        object_id="")

    def test_correction_cannot_silently_change_subject(self):
        old = self.assertion()
        with self.assertRaises(ValueError):
            self.ledger.assert_relation("a", self.obs.id, self.b.id, "acquires", self.obs.content,
                                        object_id=self.a.id, supersedes_id=old.id)

    def test_scope_filter_returns_no_other_tenant_records(self):
        self.assertion()
        self.assertEqual([], self.ledger.assertions("b", as_of=T0))

    def test_persistence_survives_reopening(self):
        with tempfile.TemporaryDirectory() as folder:
            path = str(Path(folder) / "fixture.db")
            one = Ledger(path, clock=lambda: T0)
            ent = one.create_entity("a", "organization", "Fixture", namespace="fixture", external_id="id")
            one.close()
            two = Ledger(path, clock=lambda: T0)
            again = two.create_entity("a", "organization", "Fixture", namespace="fixture", external_id="id")
            two.close()
            self.assertEqual(ent, again)


if __name__ == "__main__":
    unittest.main()

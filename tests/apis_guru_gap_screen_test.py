#!/usr/bin/env python3
"""End-to-end boundary tests for the APIs.guru gap screening command."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts/apis-guru-gap-screen.py"
REPORT = REPO / "docs/openapi-surface/apis-guru-gap-witnesses.tsv"
STAMP = "2026-09-08T12:00:00Z"


class GapScreenTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def spec(self, name: str, contents: str) -> str:
        path = self.root / name
        path.write_text(contents, encoding="utf-8")
        return path.as_uri()

    def index(self, versions: list[tuple[str, str, str]]) -> str:
        catalogue: dict[str, dict] = {}
        for api_id, version, url in versions:
            catalogue.setdefault(api_id, {"versions": {}})["versions"][version] = {
                "swaggerUrl": url
            }
        path = self.root / "list.json"
        path.write_text(json.dumps(catalogue, sort_keys=True), encoding="utf-8")
        return path.as_uri()

    def invoke(
        self,
        index: str,
        output: Path | None = None,
        provenance: Path | None = None,
        *extra_args: str,
    ):
        output = output or self.root / "report.tsv"
        provenance = provenance or REPO / "docs/openapi-surface/apis-guru-publisher-provenance.tsv"
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--index-url", index, "--output", str(output),
             "--provenance-map", str(provenance), "--snapshot-utc", STAMP,
             "--workers", "2", "--attempts", "2", *extra_args],
            cwd=REPO, capture_output=True, text=True, timeout=30,
        )
        return completed, output

    def test_real_command_writes_complete_deterministic_snapshot(self) -> None:
        # One real JSON document hits two owned selectors; two versions of the
        # same API prove versions are independent catalogue declarations.
        publisher_source = (
            "https://github.com/example/publisher/blob/"
            "0123456789abcdef0123456789abcdef01234567/openapi.json"
        )
        admitted = self.spec("admitted.json", json.dumps({
            "openapi": "3.0.0", "info": {
                "title": "A", "version": "1", "license": {"name": "MIT"},
                "x-origin": [{"url": publisher_source}],
            },
            "paths": {}, "components": {"schemas": {"Hit": {"anyOf": [{
                "type": "array", "items": {"type": "object", "properties": {"x": {"type": "string"}}}
            }]}}},
        }))
        untrusted = self.spec("untrusted.json", json.dumps({
            "openapi": "3.0.0", "info": {
                "title": "U", "version": "1", "license": {"name": "MIT"},
                "x-origin": [{"url": publisher_source}],
            },
            "paths": {}, "components": {"schemas": {"Hit": {"anyOf": [{
                "type": "array", "items": {"type": "object", "properties": {"x": {"type": "string"}}}
            }]}}},
        }))
        unknown = self.spec("unknown.yaml", """openapi: 3.0.0
info:
  title: B
  version: '1'
  license:
    name: Custom Public Terms
paths: {}
components:
  schemas:
    Hit:
      anyOf:
        - type: object
          properties:
            x:
              type: string
""")
        refused = self.spec("refused.json", json.dumps({
            "openapi": "3.0.0", "info": {"title": "C", "version": "1"}, "paths": {},
            "components": {"schemas": {"Hit": {"anyOf": [{"type": "string"}]}}},
        }))
        index = self.index([
            ("z.example", "2", admitted), ("z.example", "1", admitted),
            ("asana.com", "1.0", admitted), ("untrusted.example", "1", untrusted),
            ("a.example", "1", unknown), ("m.example", "1", refused),
        ])
        provenance = self.root / "provenance.tsv"
        provenance.write_text(
            "api_id\tversion\tsource_url\timmutable_ref\n"
            f"asana.com\t1.0\t{publisher_source}\t0123456789abcdef0123456789abcdef01234567\n",
            encoding="utf-8",
        )
        first, output = self.invoke(index, provenance=provenance)
        self.assertEqual(first.returncode, 0, first.stderr)
        original = output.read_bytes()
        second, _ = self.invoke(index, output, provenance)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(output.read_bytes(), original)
        with output.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, dialect="excel-tab"))
        self.assertEqual(len({row["gap_key"] for row in rows}), 30)
        self.assertTrue(all(row["snapshot_utc"] == STAMP for row in rows))
        ordering = [(r["gap_key"], r["api_id"], r["version"], r["spec_url"]) for r in rows]
        self.assertEqual(ordering, sorted(ordering))
        hits = [r for r in rows if r["outcome"] == "candidate"]
        self.assertIn("admitted", {r["license_screen"] for r in hits})
        self.assertIn("unknown", {r["license_screen"] for r in hits})
        self.assertIn("refused", {r["license_screen"] for r in hits})
        self.assertEqual({r["version"] for r in hits if r["api_id"] == "z.example"}, {"1", "2"})
        self.assertTrue(all(int(r["declaration_count"]) > 0 for r in hits))
        traced = [r for r in hits if r["api_id"] == "asana.com"]
        self.assertTrue(traced)
        self.assertTrue(all(r["source_url"] == publisher_source for r in traced))
        self.assertTrue(all(
            r["immutable_ref"] == "0123456789abcdef0123456789abcdef01234567"
            for r in traced
        ))
        self.assertTrue(all("ownership evidenced by provenance mapping" in r["notes"] for r in traced))
        self.assertTrue(all("repeats the rejected-spec table" in r["notes"] for r in traced))
        untrusted_rows = [r for r in hits if r["api_id"] == "untrusted.example"]
        self.assertTrue(untrusted_rows)
        self.assertTrue(all(not r["source_url"] and not r["immutable_ref"] for r in untrusted_rows))
        self.assertTrue(all("not evidenced" in r["notes"] for r in untrusted_rows))
        none = [r for r in rows if r["outcome"] == "none-found"]
        self.assertTrue(none)
        self.assertTrue(all(not r["api_id"] and not r["declaration_count"] for r in none))

    def test_tracked_snapshot_obeys_the_consumer_contract(self) -> None:
        with REPORT.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, dialect="excel-tab")
            self.assertEqual(tuple(reader.fieldnames or ()), (
                "snapshot_utc", "catalogue_digest", "gap_key", "selector", "outcome",
                "api_id", "version", "spec_url", "source_url", "immutable_ref", "license",
                "license_screen", "declaration_count", "notes",
            ))
            rows = list(reader)
        keys = {row["gap_key"] for row in rows}
        self.assertEqual(len(keys), 30)
        self.assertIn("oneof-bare-object-example-variant", keys)
        self.assertFalse(any(word in REPORT.read_text(encoding="utf-8") for word in ("TODO", "placeholder")))
        for key in keys:
            owned = [row for row in rows if row["gap_key"] == key]
            outcomes = {row["outcome"] for row in owned}
            self.assertIn(outcomes, ({"candidate"}, {"none-found"}))
            if outcomes == {"none-found"}:
                self.assertEqual(len(owned), 1)
                self.assertTrue(all(not owned[0][field] for field in (
                    "api_id", "version", "spec_url", "source_url", "immutable_ref",
                    "license", "license_screen", "declaration_count",
                )))
            else:
                for row in owned:
                    self.assertTrue(row["api_id"] and row["version"] and row["spec_url"])
                    self.assertGreater(int(row["declaration_count"]), 0)
                    self.assertIn(row["license_screen"], {"admitted", "refused", "unknown"})
                    self.assertEqual(bool(row["source_url"]), bool(row["immutable_ref"]))

    def test_malformed_document_refuses_to_publish(self) -> None:
        malformed = self.spec("bad.json", "{not json")
        output = self.root / "must-not-exist.tsv"
        completed, _ = self.invoke(self.index([("bad.example", "1", malformed)]), output)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("malformed JSON", completed.stderr)
        self.assertFalse(output.exists())

    def test_fetch_failure_refuses_to_publish_after_bounded_retries(self) -> None:
        missing = (self.root / "missing.yaml").as_uri()
        output = self.root / "must-not-exist.tsv"
        completed, _ = self.invoke(self.index([("missing.example", "1", missing)]), output)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("unanswered after 2 bounded attempts", completed.stderr)
        self.assertFalse(output.exists())

    def test_nonpositive_numeric_arguments_are_rejected(self) -> None:
        index = self.index([])
        expected = "apis-guru-gap-screen: attempts, workers, and timeout must be positive\n"
        for option, value in (
            ("--attempts", "0"),
            ("--workers", "0"),
            ("--timeout", "0"),
        ):
            with self.subTest(option=option):
                completed, output = self.invoke(index, None, None, option, value)
                self.assertEqual(completed.returncode, 2)
                self.assertEqual(completed.stderr, expected)
                self.assertEqual(completed.stdout, "")
                self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()

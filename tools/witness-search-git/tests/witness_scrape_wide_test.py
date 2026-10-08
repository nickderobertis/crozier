#!/usr/bin/env python3
"""witness-scrape-wide's journeys. Its `derive` records the checkout's commit
through the real `git rev-parse HEAD`, and every case here derives a report, so
they run in this git-backed project. The fixtures they share with
witness-search's offline suites stay in `tools/witness-search/tests/`.
Run: `just nx run witness-search-git:test`.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "witness-search" / "tests"))

import witness_search_redo_test as redo  # noqa: E402 - the shared fixtures' directory must be on sys.path first
from witness_search_redo_test import (  # noqa: E402 - the shared fixtures' directory must be on sys.path first
    CONTRACT,
    REPO,
    ROOT,
    SCRIPT,
    SHARDS,
    WideWitnessFixture,
)


class WideWitnessTests(WideWitnessFixture, unittest.TestCase):
    """Acquire pinned bytes and validate reports through the actual CLI boundary."""

    def test_diagnostics_survive_legacy_child_encoding(self) -> None:
        inventory = self.work / "inventaire-é.json"
        inventory.write_text("{}", encoding="utf-8")
        args = [
            "acquire",
            "--inventory",
            str(inventory),
            "--cache",
            str(self.work / "cache"),
            "--contract",
            str(self.report / "keys.md"),
            "--output",
            str(self.work / "result.json"),
        ]
        env = dict(os.environ, PYTHONIOENCODING="cp1252")
        refused = subprocess.run([sys.executable, str(self.wide), *args], cwd=REPO, capture_output=True, env=env)
        self.assertEqual(1, refused.returncode)
        self.assertIn("inventaire-é.json", refused.stderr.decode("utf-8"))
        # Inject a raw diagnostic at Python startup, while running the actual
        # acquisition and census unchanged. Native children need not emit UTF-8.
        startup = self.work / "startup"
        startup.mkdir()
        (startup / "sitecustomize.py").write_text(
            "import os\nos.write(2, b'publisher diagnostic: \\xe9\\n')\n", encoding="utf-8"
        )
        env["PYTHONPATH"] = str(startup)
        inventory.write_text(json.dumps({"schema_version": 1, "sources": []}), encoding="utf-8")
        recovered = subprocess.run([sys.executable, str(self.wide), *args], cwd=REPO, capture_output=True, env=env)
        self.assertEqual(0, recovered.returncode, recovered.stderr)
        result = json.loads((self.work / "result.json").read_text(encoding="utf-8"))
        self.assertEqual(0, result["census_exit"])
        self.assertIn(r"publisher diagnostic: \xe9", (self.work / "result.census.log").read_text(encoding="utf-8"))

    def test_derive_preserves_key_specific_screening_metadata(self) -> None:
        root = self.work / "history"
        root.mkdir()
        shutil.copyfile(CONTRACT, root / "contract.md")
        # A `handwritten` row's baseline membership is read off the shards
        # beside the contract, so the history carries them.
        for shard in SHARDS:
            shutil.copyfile(shard, root / shard.name)
        # A `handwritten` key's membership follows this very candidates table,
        # so a witness recorded for one would drop it; screen `gap` keys only.
        # The tree no longer holds a frozen search-incomplete `gap` row, so three
        # are restored in a copy of the region files the derivations read.
        sys.path.insert(0, str(REPO / "tools" / "surface-census" / "tests"))
        from region_flip import restore_gap_row

        regions = self.work / "regions"
        regions.mkdir()
        for region in (REPO / "docs/openapi-surface").glob("*.md"):
            shutil.copyfile(region, regions / region.name)
        shutil.copyfile(REPO / "docs/openapi-surface/witness-search-keys.tsv", regions / "witness-search-keys.tsv")
        for key in (
            "array-item-inheritance-union",
            "property-sole-anyof-composed-member",
            "property-sole-oneof-empty-object-member",
        ):
            restore_gap_row(regions / "schemas.md", key)
        handwritten = {
            line.split("|")[1].strip()
            for line in (regions / "schemas.md").read_text(encoding="utf-8").splitlines()
            if line.startswith("| ") and "| handwritten |" in line
        }
        keys = [
            key
            for key in json.loads((self.report / "baseline.json").read_text(encoding="utf-8"))["keys"]
            if key not in handwritten
        ]
        retained, discarded, absent = keys[:3]
        screens = [
            "passed: publisher grant",
            "passed: pinned publisher",
            "passed: generated SDK",
            f"passed: retained first model; discarded keys: `{discarded}`",
        ]
        blocked = ["blocked: no publisher grant", "not reached", "not reached", "not reached"]
        table = "\n".join(self.candidate.splitlines()[:2]) + "\n"
        table += (
            f"| `publisher/retained-é.json` | `{retained}`, `{discarded}` | "
            + " | ".join(screens)
            + " | `witness-found` | evidence.txt |\n"
        )
        table += (
            f"| `publisher/blocked.json` | `{discarded}` | "
            + " | ".join(blocked)
            + " | `witness-blocked` | evidence.txt |\n"
        )
        (root / "candidates.md").write_text(table, encoding="utf-8")
        output = self.work / "derived"
        result = self.cli("derive", "--report", output, "--contract", root / "contract.md", "--regions", regions)
        self.assertEqual(0, result.returncode, result.stderr)
        baseline = json.loads((output / "baseline.json").read_text(encoding="utf-8"))
        pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, encoding="utf-8").strip()
        self.assertEqual(pin, baseline["source_commit"])
        items = baseline["keys"]
        self.assertTrue(items[retained]["usable_witness"])
        self.assertFalse(items[discarded]["usable_witness"])
        self.assertFalse(items[absent]["usable_witness"])
        self.assertEqual([], items[absent]["candidates"])
        self.assertEqual(
            [
                {
                    "artifact": "publisher/retained-é.json",
                    "screens": screens,
                    "disposition": "witness-found",
                    "discarded": False,
                }
            ],
            items[retained]["candidates"],
        )
        self.assertEqual(
            [
                {
                    "artifact": "publisher/retained-é.json",
                    "screens": screens,
                    "disposition": "witness-found",
                    "discarded": True,
                },
                {
                    "artifact": "publisher/blocked.json",
                    "screens": blocked,
                    "disposition": "witness-blocked",
                    "discarded": False,
                },
            ],
            items[discarded]["candidates"],
        )
        # Changing a derived key's frozen selector must refuse derivation before
        # writing a report. The key has to be one derivation still reads: a row
        # a registration has since made `golden` is no longer derived at all.
        contract = root / "contract.md"
        row = f"| `{retained}` | `schema."
        text = contract.read_text(encoding="utf-8")
        self.assertIn(row, text)
        contract.write_text(text.replace(row, f"| `{retained}` | `unknown.", 1), encoding="utf-8")
        refused = self.cli("derive", "--report", self.work / "refused", "--contract", contract, "--regions", regions)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("selector", refused.stderr)
        self.assertFalse((self.work / "refused").exists())

    def test_inventory_boundary_refusals_precede_acquisition_and_recover(self) -> None:
        inventory = self.work / "inventaire-é.json"
        cache = self.work / "cache"
        output = self.work / "acquisition.json"
        source = {"artifact": (self.work / "absent.json").as_uri()}
        cases = [
            ([], "expected inventory"),
            ({}, "expected inventory"),
            ({"schema_version": 2, "sources": []}, "expected inventory"),
            ({"schema_version": 1, "sources": {}}, "expected inventory"),
        ]
        for row in (None, {}, {"artifact": ""}, {"artifact": 7}):
            cases.append(({"schema_version": 1, "sources": [row]}, "missing artifact identity"))
        cases.append(({"schema_version": 1, "sources": [source, source]}, "duplicate artifact"))
        for field in ("sha256", "prior_sha256"):
            for value in ("A" * 64, "a" * 63, 42):
                cases.append(({"schema_version": 1, "sources": [dict(source, **{field: value})]}, f"malformed {field}"))
        local = {"path": "APIs/x/openapi.yaml", "sha256": "a" * 64}
        for row in (
            dict(source, local_path="/etc/passwd", **local),
            dict(source, local_path="/tree/APIs/x/openapi.yaml", path="APIs/x/openapi.yaml"),
            dict(source, local_path="tree/APIs/x/openapi.yaml", **local),
            dict(source, local_path="/tree/../etc/APIs/x/openapi.yaml", **local),
            dict(source, local_path=7, **local),
            # A tree `path` that is itself absolute would let any file pass as its own tree's.
            dict(source, local_path="/etc/passwd", path="/etc/passwd", sha256="a" * 64),
        ):
            cases.append(({"schema_version": 1, "sources": [row]}, "malformed local_path"))
        args = (
            "acquire",
            "--inventory",
            inventory,
            "--cache",
            cache,
            "--contract",
            self.report / "keys.md",
            "--output",
            output,
        )
        for invalid, message in cases:
            with self.subTest(invalid=invalid):
                inventory.write_text(json.dumps(invalid), encoding="utf-8")
                refused = self.cli(*args)
                self.assertNotEqual(0, refused.returncode)
                self.assertIn(message, refused.stderr)
                self.assertIn("inventaire-é.json", refused.stderr)
                self.assertFalse(cache.exists())
                self.assertFalse(output.exists())
        inventory.write_text(json.dumps({"schema_version": 1, "sources": [source]}), encoding="utf-8")
        recovered = self.cli(*args)
        self.assertEqual(0, recovered.returncode, recovered.stderr)
        self.assertEqual("inaccessible", json.loads(output.read_text(encoding="utf-8"))["sources"][0]["status"])

    def test_real_report_validator_rejects_contract_drift_and_recovers(self) -> None:
        good = self.validate()
        self.assertEqual(0, good.returncode, good.stderr)
        changes = [
            ("candidates.md", self.candidate.replace("witness-found", "invented"), "unknown candidate disposition"),
            ("ranking.tsv", self.rank_header + self.rank_row * 2, "duplicate rank"),
            ("ranking.tsv", self.rank_header + self.rank_row.replace("1\t", "0\t", 1), "malformed"),
            ("ranking.tsv", self.rank_header + self.rank_row.replace(self.key, "unknown-key"), "unknown keys"),
            ("ranking.tsv", self.rank_header + self.rank_row.replace("fern.txt", "absent-é.txt"), "absent-é.txt"),
            (
                "keys.md",
                (self.report / "keys.md").read_text(encoding="utf-8").replace("schema.", "invented.", 1),
                "selector",
            ),
            (
                "candidates.md",
                self.candidate.replace("passed: retained model", f"passed: other model; discarded keys: `{self.key}`"),
                "retained candidate screens",
            ),
        ]
        for filename, text, message in changes:
            with self.subTest(message=message):
                path = self.report / filename
                old = path.read_text(encoding="utf-8")
                path.write_text(text, encoding="utf-8")
                failed = self.validate()
                self.assertNotEqual(0, failed.returncode)
                self.assertIn(message, failed.stderr)
                path.write_text(old, encoding="utf-8")
        recovered = self.validate()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_report_table_failures_identify_the_broken_contract_and_recover(self) -> None:
        candidate_row = self.candidate.splitlines()[-1] + "\n"
        exhausted = "| slot-1 | — | [] | exhausted | comparison.txt |\n"
        baseline = json.loads((self.report / "baseline.json").read_text(encoding="utf-8"))
        baseline["schema_version"] = 2
        changes = [
            ("baseline.json", json.dumps(baseline), "baseline schema_version must be 1"),
            ("candidates.md", self.candidate.replace("redistribution", "grant"), "candidate header"),
            ("candidates.md", self.candidate.replace(" | fern.txt |", " |"), "eight columns"),
            ("candidates.md", self.candidate.replace("passed: grant", ""), "missing a screen state"),
            ("candidates.md", self.candidate + candidate_row, "duplicate candidate artifact"),
            ("candidates.md", self.candidate.replace(self.key, "unknown-key"), "candidate has unknown keys"),
            ("ranking.tsv", (self.rank_header + self.rank_row).replace("rank\t", "position\t", 1), "ranking header"),
            ("slots.md", self.slots_header.replace("disposition", "result"), "slot header"),
            ("slots.md", self.slots_header + exhausted.replace(" | comparison.txt |", " |"), "five columns"),
            ("slots.md", self.slots_header + exhausted * 2, "duplicate or empty slot"),
            ("slots.md", self.slots_header + exhausted.replace("slot-1", ""), "duplicate or empty slot"),
            ("slots.md", self.slots_header + exhausted.replace("exhausted", "invented"), "unknown slot disposition"),
            ("slots.md", self.slots_header + exhausted.replace("—", self.sha), "absent artifact and keys"),
            (
                "slots.md",
                self.slots_header + exhausted.replace("[]", json.dumps([self.key])),
                "absent artifact and keys",
            ),
        ]
        for filename, broken, diagnostic in changes:
            with self.subTest(diagnostic=diagnostic, broken=broken):
                path = self.report / filename
                original = path.read_text(encoding="utf-8")
                path.write_text(broken, encoding="utf-8")
                refused = self.validate()
                self.assertNotEqual(0, refused.returncode)
                self.assertIn(diagnostic, refused.stderr)
                path.write_text(original, encoding="utf-8")
        recovered = self.validate()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_slots_reject_conflicting_claims_and_accept_exhaustion(self) -> None:
        path = self.report / "slots.md"
        row = f"| slot-1 | {self.sha} | {json.dumps([self.key])} | registered | comparison.txt |\n"
        path.write_text(self.slots_header + row, encoding="utf-8")
        self.assertEqual(0, self.validate().returncode)
        path.write_text(self.slots_header + row + row.replace("slot-1", "slot-2"), encoding="utf-8")
        failed = self.validate()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn("conflicting slot claim", failed.stderr)
        path.write_text(self.slots_header + "| slot-1 | — | [] | exhausted | comparison.txt |\n", encoding="utf-8")
        self.assertEqual(0, self.validate().returncode)

    def multiple_ranked_candidates(self) -> tuple[list[tuple[str, str, list[str]]], list[str]]:
        keys = list(json.loads((self.report / "baseline.json").read_text(encoding="utf-8"))["keys"])[:2]
        # Expected order is explicit: coverage beats firmness, then firmness beats
        # the digest, and the equal-firmness pair is ordered by ascending digest.
        definitions = [("d", keys, 0), ("b", keys[:1], 2), ("a", keys[:1], 1), ("c", keys[:1], 1)]
        header = self.candidate.splitlines()[:2]
        candidates = []
        sources = []
        for label, owned, firmness in definitions:
            sha = label * 64
            artifact = f"https://publisher.example/{'1' * 40}/{label}/openapi.json"
            candidates.append((sha, artifact, owned))
            header.append(
                f"| `{artifact}` | "
                + ", ".join(f"`{key}`" for key in owned)
                + " | passed: grant | passed: publisher pin | passed: generation | passed: retained model | `witness-found` | fern.txt |"
            )
            row = {
                "artifact": artifact,
                "sha256": sha,
                "ref": "1" * 40,
                "repository": "APIs-guru/openapi-directory" if firmness == 0 else "publisher/api",
                "status": "readable",
                "document": sha + ".json",
            }
            row["repository_licences"] = [{"evidence": "fern.txt"}]
            if firmness in {0, 2}:
                row["document_license"] = {"name": "Document grant"}
            sources.append(row)
        # A retained provenance alias uses the existing byte rank, never a fifth rank.
        alias = "https://publisher.example/" + "1" * 40 + "/mirror-b/openapi.json"
        header.append(
            f"| `{alias}` | `{keys[0]}` | passed: grant | passed: publisher pin | passed: generation | passed: retained model | `witness-found` | fern.txt |"
        )
        sources.append(dict(sources[1], artifact=alias))
        (self.report / "candidates.md").write_text("\n".join(header) + "\n", encoding="utf-8")
        (self.report / "acquisition.json").write_text(
            json.dumps({"schema_version": 1, "sources": sources}), encoding="utf-8"
        )
        self.write_ranks(candidates)
        return candidates, keys

    def write_ranks(self, candidates: list[tuple[str, str, list[str]]], ranks: list[int] | None = None) -> None:
        numbers = ranks if ranks is not None else list(range(1, len(candidates) + 1))
        rows = [
            f"{rank}\t{sha}\t{artifact}\t{json.dumps(keys)}\tfern.txt\tcomparison.txt\n"
            for rank, (sha, artifact, keys) in zip(numbers, candidates)
        ]
        (self.report / "ranking.tsv").write_text(self.rank_header + "".join(rows), encoding="utf-8")

    def test_ranked_bytes_must_match_acquisition_and_allow_provenance_aliases(self) -> None:
        import hashlib

        spec = self.work / "publisher.json"
        alias = self.work / "miroir-é.json"
        spec.write_text('{"openapi":"3.0.3","info":{"title":"Publisher","version":"1"},"paths":{}}', encoding="utf-8")
        alias.write_bytes(spec.read_bytes())
        sha = hashlib.sha256(spec.read_bytes()).hexdigest()
        inventory = self.work / "inventory.json"
        inventory.write_text(
            json.dumps(
                {"schema_version": 1, "sources": [{"artifact": path.as_uri(), "sha256": sha} for path in (spec, alias)]}
            ),
            encoding="utf-8",
        )
        acquisition = self.report / "acquisition.json"
        acquired = self.cli(
            "acquire",
            "--inventory",
            inventory,
            "--cache",
            self.work / "cache",
            "--contract",
            self.report / "keys.md",
            "--output",
            acquisition,
        )
        self.assertEqual(0, acquired.returncode, acquired.stderr)
        original = acquisition.read_text(encoding="utf-8")
        candidates = self.candidate.replace(self.artifact, spec.as_uri())
        candidates += self.candidate.splitlines()[-1].replace(self.artifact, alias.as_uri()) + "\n"
        (self.report / "candidates.md").write_text(candidates, encoding="utf-8")
        slots = self.report / "slots.md"
        for identity in (spec.as_uri(), alias.as_uri()):
            with self.subTest(identity=identity):
                acquisition.write_text(original, encoding="utf-8")
                (self.report / "candidates.md").write_text(candidates, encoding="utf-8")
                self.write_ranks([(sha, identity, [self.key])])
                slots.write_text(
                    self.slots_header
                    + f"| slot-1 | {sha} | {json.dumps([self.key])} | registered | comparison.txt |\n",
                    encoding="utf-8",
                )
                valid = self.validate()
                self.assertEqual(0, valid.returncode, valid.stderr)
                substituted = "f" * 64
                self.assertNotEqual(sha, substituted)
                self.write_ranks([(substituted, identity, [self.key])])
                slots.write_text(slots.read_text(encoding="utf-8").replace(sha, substituted), encoding="utf-8")
                # Keep only the ranked candidate so alias-completeness checks
                # cannot accidentally catch the unrelated digest substitution.
                (self.report / "candidates.md").write_text(
                    self.candidate.replace(self.artifact, identity), encoding="utf-8"
                )
                refused = self.validate()
                self.assertNotEqual(0, refused.returncode)
                self.assertIn("ranked digest differs from acquisition", refused.stderr)
                self.assertIn(identity, refused.stderr)
                self.write_ranks([(sha, identity, [self.key])])
                slots.write_text(self.slots_header, encoding="utf-8")
                for missing_digest in (False, True):
                    data = json.loads(original)
                    if missing_digest:
                        next(row for row in data["sources"] if row["artifact"] == identity).pop("sha256")
                    else:
                        data["sources"] = [row for row in data["sources"] if row["artifact"] != identity]
                    acquisition.write_text(json.dumps(data), encoding="utf-8")
                    refused = self.validate()
                    self.assertNotEqual(0, refused.returncode)
                    self.assertIn("ranked artifact lacks acquisition digest", refused.stderr)
                acquisition.unlink()
                refused = self.validate()
                self.assertNotEqual(0, refused.returncode)
                self.assertIn("ranked artifact lacks acquisition digest", refused.stderr)
                acquisition.write_text(original, encoding="utf-8")
                (self.report / "candidates.md").write_text(candidates, encoding="utf-8")
                recovered = self.validate()
                self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_multiple_ranks_freeze_coverage_firmness_and_digest_order(self) -> None:
        candidates, _keys = self.multiple_ranked_candidates()
        valid = self.validate()
        self.assertEqual(0, valid.returncode, valid.stderr)
        for first, second, reason in [(0, 1, "coverage"), (1, 2, "firmness"), (2, 3, "digest")]:
            with self.subTest(reason=reason):
                wrong = list(candidates)
                wrong[first], wrong[second] = wrong[second], wrong[first]
                self.write_ranks(wrong)
                refused = self.validate()
                self.assertNotEqual(0, refused.returncode)
                self.assertIn("ranking violates", refused.stderr)
        self.write_ranks(candidates, [1, 2, 3, 5])
        refused = self.validate()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("ranks must be contiguous", refused.stderr)
        self.write_ranks(candidates[:-1])
        refused = self.validate()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("retained candidate missing rank", refused.stderr)
        alias = "https://publisher.example/" + "1" * 40 + "/mirror-b/openapi.json"
        self.write_ranks(candidates + [(candidates[1][0], alias, candidates[1][2])])
        refused = self.validate()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("duplicate ranked digest", refused.stderr)
        self.write_ranks(candidates)
        recovered = self.validate()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_blocked_slots_do_not_claim_keys_but_registered_slots_cannot_conflict(self) -> None:
        candidates, keys = self.multiple_ranked_candidates()
        path = self.report / "slots.md"
        blocked = f"| slot-1 | {candidates[0][0]} | {json.dumps(keys[:1])} | blocked | comparison.txt |\n"
        registered = f"| slot-2 | {candidates[1][0]} | {json.dumps(keys[:1])} | registered | comparison.txt |\n"
        path.write_text(self.slots_header + blocked + registered, encoding="utf-8")
        valid = self.validate()
        self.assertEqual(0, valid.returncode, valid.stderr)
        path.write_text(
            self.slots_header + blocked.replace("| blocked |", "| registered |") + registered, encoding="utf-8"
        )
        refused = self.validate()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("conflicting registered key claims", refused.stderr)
        path.write_text(self.slots_header + blocked + registered, encoding="utf-8")
        recovered = self.validate()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_supplements_are_optional_additive_and_discarded_keys_do_not_pass(self) -> None:
        shards, schemas = self.completed_documents()
        key = self.contract_keys()[0][0]
        supplemental = self.work / "supplement.md"
        supplemental.write_text(self.candidate.replace(self.key, key), encoding="utf-8")
        command = [
            sys.executable,
            str(SCRIPT),
            str(CONTRACT),
            *(str(p) for p in shards),
            "--reconcile",
            "--schemas",
            str(schemas),
            "--candidates",
            str(schemas.parent / "candidates.md"),
        ]
        run = lambda extra: subprocess.run(
            command + extra, cwd=REPO, capture_output=True, errors="backslashreplace", encoding="utf-8"
        )
        self.assertEqual(0, run([]).returncode)
        supplement = ["--supplement-candidates", str(supplemental)]
        self.assertIn("expected 'witness-found'", run(supplement).stderr)
        schemas.write_text(
            schemas.read_text(encoding="utf-8").replace(
                "search outcome `search-incomplete`", "search outcome `witness-found`", 1
            ),
            encoding="utf-8",
        )
        self.assertEqual(0, run(supplement * 2).returncode)
        self.assertNotEqual(0, run([]).returncode)
        supplemental.write_text(
            supplemental.read_text(encoding="utf-8").replace(
                "passed: retained model", f"passed: other model; discarded keys: `{key}`"
            ),
            encoding="utf-8",
        )
        self.assertIn("expected 'search-incomplete'", run(supplement).stderr)
        missing = self.work / "absent-supplément.md"
        missing_args = ["--supplement-candidates", str(missing)]
        refused = run(missing_args)
        self.assertEqual(2, refused.returncode)
        self.assertIn("requires a candidate file", refused.stderr)
        missing.write_text(self.candidate.replace(self.key, key), encoding="utf-8")
        self.assertEqual(0, run(missing_args).returncode)
        malformed = self.work / "malformed.md"
        malformed.write_text(f"| `artifact` | `{key}` | witness-found |\n", encoding="utf-8")
        torn = run(["--supplement-candidates", str(malformed)])
        self.assertEqual(1, torn.returncode, torn.stderr)
        self.assertIn("malformed.md:1: a candidate row has 3 cells, not the 8", torn.stderr)

    def test_http_acquisition_records_success_refusal_and_interrupted_transfer(self) -> None:
        import hashlib
        import http.server
        import threading

        document = json.dumps({"openapi": "3.0.3", "info": {"title": "Réseau", "version": "1"}, "paths": {}}).encode()
        served: list[str] = []

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                served.append(self.path)
                if self.path == "/refused.json":
                    self.send_response(403)
                    self.send_header("Content-Length", "9")
                    self.end_headers()
                    self.wfile.write(b"Forbidden")
                    return
                self.send_response(200)
                if self.path == "/interrupted.json":
                    # The headers promise the whole document; the connection
                    # drops after its first ten bytes.
                    self.send_header("Content-Length", str(len(document)))
                    self.end_headers()
                    self.wfile.write(document[:10])
                    self.wfile.flush()
                    self.close_connection = True
                    return
                self.send_header("Content-Length", str(len(document)))
                self.end_headers()
                self.wfile.write(document)

            def log_message(self, *_args) -> None:
                pass

        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        inventory = self.work / "inventory.json"
        inventory.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "sources": [
                        {"artifact": f"{url}/ok.json"},
                        {"artifact": f"{url}/refused.json"},
                        {"artifact": f"{url}/interrupted.json"},
                    ],
                }
            ),
            encoding="utf-8",
        )
        cache = self.work / "cache"
        output = self.work / "acquisition.json"
        args = (
            "acquire",
            "--inventory",
            inventory,
            "--cache",
            cache,
            "--contract",
            self.report / "keys.md",
            "--output",
            output,
        )
        run = self.cli(*args)
        self.assertEqual(0, run.returncode, run.stderr)
        self.assertEqual(sorted(served), ["/interrupted.json", "/ok.json", "/refused.json"])
        ok, refused, interrupted = json.loads(output.read_text(encoding="utf-8"))["sources"]
        sha = hashlib.sha256(document).hexdigest()
        self.assertEqual(("readable", "newly-fetched", sha), (ok["status"], ok["acquisition"], ok["sha256"]))
        self.assertEqual(document, (cache / "documents" / ok["document"]).read_bytes())
        self.assertEqual(("inaccessible", "HTTP Error 403: Forbidden"), (refused["status"], refused["diagnostic"]))
        self.assertEqual("inaccessible", interrupted["status"])
        self.assertIn("IncompleteRead", interrupted["diagnostic"])
        # Neither failure left bytes in the cache: only the complete document's.
        self.assertEqual([sha], sorted(path.name for path in cache.iterdir() if path.is_file()))
        self.assertEqual([ok["document"]], [path.name for path in (cache / "documents").iterdir()])
        self.assertEqual(0, json.loads(output.read_text(encoding="utf-8"))["census_exit"])
        # The cached digest authorizes reuse; nothing is fetched again.
        served.clear()
        inventory.write_text(
            json.dumps({"schema_version": 1, "sources": [{"artifact": f"{url}/ok.json", "sha256": sha}]}),
            encoding="utf-8",
        )
        reused = self.cli(*args)
        self.assertEqual(0, reused.returncode, reused.stderr)
        self.assertEqual("verified-reuse", json.loads(output.read_text(encoding="utf-8"))["sources"][0]["acquisition"])
        self.assertEqual([], served)

    def test_wide_acquisition_reads_openapi_3_as_github_search_does_and_the_local_census_takes_all_of_it(self) -> None:
        # The wide tier screens by the GitHub search's version expression, so the
        # two agree on every version; and it hands every document it reads as
        # OpenAPI 3 to the local census, which must census each one. The census
        # may read more (`3.0`), which only the wide tier's own reading gates.
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "wide_version_github", REPO / "tools/witness-search/witness-search-github.py"
        )
        github = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = github
        spec.loader.exec_module(github)
        versions = (
            "3.0.0",
            "3.0.3",
            "3.1.0",
            "3.1.1",
            "3.2.0",
            "3.0.0-rc1",
            "3.1.0+build",
            "3.0",
            "3",
            "2.0",
            "4.0.0",
            "30.0.0",
            " 3.0.3",
            "",
        )
        documents = self.work / "versions"
        documents.mkdir()
        rows = []
        for index, version in enumerate(versions):
            path = documents / f"v{index}.json"
            path.write_text(
                json.dumps({"openapi": version, "info": {"title": "V", "version": "1"}, "paths": {}}), encoding="utf-8"
            )
            rows.append({"artifact": path.as_uri()})
        inventory = self.work / "inventory.json"
        inventory.write_text(json.dumps({"schema_version": 1, "sources": rows}), encoding="utf-8")
        output = self.work / "acquisition.json"
        run = self.cli(
            "acquire",
            "--inventory",
            inventory,
            "--cache",
            self.work / "cache",
            "--contract",
            self.report / "keys.md",
            "--output",
            output,
        )
        self.assertEqual(0, run.returncode, run.stderr)
        wide = {
            version: row["status"] == "readable"
            for version, row in zip(versions, json.loads(output.read_text(encoding="utf-8"))["sources"], strict=True)
        }
        census = subprocess.run(
            [
                sys.executable,
                str(REPO / "tools/witness-search/witness-search-local-census.py"),
                "--contract",
                str(self.report / "keys.md"),
                "--documents",
                f"local={documents}",
                "--all-documents-jsonl",
            ],
            cwd=REPO,
            capture_output=True,
            encoding="utf-8",
        )
        local = {
            Path(row["document"]).name: row["classification"] == "openapi-3"
            for row in map(json.loads, census.stdout.splitlines())
        }
        for index, version in enumerate(versions):
            with self.subTest(version=version):
                self.assertEqual(bool(github.OPENAPI_VERSION.fullmatch(version)), wide[version])
                if wide[version]:
                    self.assertTrue(local[f"v{index}.json"], "the local census would not census it")
        self.assertTrue(wide["3.2.0"])
        self.assertFalse(wide["2.0"])

    def test_acquisition_uses_real_files_cache_and_census_with_failure_recovery(self) -> None:
        (self.report / "ranking.tsv").write_text(self.rank_header, encoding="utf-8")
        (self.report / "candidates.md").write_text("\n".join(self.candidate.splitlines()[:2]) + "\n", encoding="utf-8")
        import hashlib

        spec = self.work / "publisher.yaml"  # publisher suffix may disagree with unchanged JSON bytes
        spec.write_text(
            json.dumps(
                {
                    "openapi": "3.0.3",
                    "info": {"title": "Réel", "version": "1"},
                    "paths": {},
                    "components": {
                        "schemas": {"Sample": {"properties": {"x": {"anyOf": [{"type": "object", "properties": {}}]}}}}
                    },
                }
            ),
            encoding="utf-8",
        )
        sha = hashlib.sha256(spec.read_bytes()).hexdigest()
        malformed = self.work / "malformé.json"
        malformed.write_text("{é", encoding="utf-8")
        legacy = self.work / "legacy.json"
        legacy.write_text(
            json.dumps({"swagger": "2.0", "info": {"title": "Legacy", "version": "1"}, "paths": {}}), encoding="utf-8"
        )
        metadata = self.work / "versions.json"
        metadata.write_text('{"versions": ["1", "2"]}', encoding="utf-8")
        inventory = self.work / "inventory.json"
        rows = [
            {"artifact": spec.as_uri(), "sha256": sha, "prior_sha256": sha},
            {"artifact": malformed.as_uri()},
            {"artifact": (self.work / "absent.json").as_uri()},
            {"artifact": legacy.as_uri()},
            {"artifact": metadata.as_uri()},
        ]
        inventory.write_text(json.dumps({"schema_version": 1, "sources": rows}), encoding="utf-8")
        import gzip

        compressed = inventory.with_suffix(".json.gz")
        compressed.write_bytes(gzip.compress(inventory.read_bytes(), mtime=0))
        inventory = compressed
        cache = self.work / "cache"
        output = self.report / "acquisition.json"
        args = (
            "acquire",
            "--inventory",
            inventory,
            "--cache",
            cache,
            "--contract",
            self.report / "keys.md",
            "--output",
            output,
        )
        for workers in ("0", "-1"):
            refused = self.cli(*args, "--workers", workers)
            self.assertNotEqual(0, refused.returncode)
            self.assertIn("workers must be positive", refused.stderr)
            self.assertFalse(cache.exists(), "invalid worker counts must not start acquisition")
        args += ("--workers", "2")
        first = self.cli(*args)
        self.assertEqual(0, first.returncode, first.stderr)
        outcomes = json.loads(output.read_text(encoding="utf-8"))["sources"]
        self.assertEqual(
            ["readable", "unreadable", "inaccessible", "excluded", "excluded"], [r["status"] for r in outcomes]
        )
        for excluded in outcomes[3:]:
            self.assertIn("no conversion performed", excluded["diagnostic"])
            self.assertNotIn("document", excluded)
        self.assertEqual("newly-fetched", outcomes[0]["acquisition"])
        self.assertEqual(sha + ".json", outcomes[0]["document"])
        self.assertNotIn("document_license", outcomes[0])
        self.assertIn(
            "property-sole-anyof-empty-object-member", output.with_suffix(".census.tsv").read_text(encoding="utf-8")
        )
        self.assertEqual(0, self.validate("--inventory", inventory).returncode)
        spec.unlink()  # exact cached bytes still support a real census offline
        second = self.cli(*args)
        self.assertEqual(0, second.returncode, second.stderr)
        self.assertEqual("verified-reuse", json.loads(output.read_text(encoding="utf-8"))["sources"][0]["acquisition"])
        (cache / sha).write_bytes(b"changed cached bytes")
        third = self.cli(*args)
        self.assertEqual(0, third.returncode, third.stderr)
        self.assertEqual("inaccessible", json.loads(output.read_text(encoding="utf-8"))["sources"][0]["status"])
        spec.write_text('{"openapi":"3.1.0"}', encoding="utf-8")
        self.assertEqual(0, self.cli(*args).returncode)
        measured = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual("digest-changed", measured["sources"][0]["status"])
        measured["sources"].pop()
        output.write_text(json.dumps(measured), encoding="utf-8")
        partial = self.validate("--inventory", inventory)
        self.assertNotEqual(0, partial.returncode)
        self.assertIn("partial inventory", partial.stderr)

    def test_changed_publisher_bytes_record_the_document_licence(self) -> None:
        import hashlib

        spec = self.work / "publisher.json"
        document = {
            "openapi": "3.0.3",
            "info": {
                "title": "Éditeur",
                "version": "2",
                "license": {"name": "Publisher grant", "url": "https://publisher.example/grant"},
            },
            "paths": {},
        }
        spec.write_text(json.dumps(document), encoding="utf-8")
        sha = hashlib.sha256(spec.read_bytes()).hexdigest()
        inventory = self.work / "inventory.json"
        inventory.write_text(
            json.dumps(
                {"schema_version": 1, "sources": [{"artifact": spec.as_uri(), "sha256": sha, "prior_sha256": "0" * 64}]}
            ),
            encoding="utf-8",
        )
        output = self.work / "acquisition.json"
        run = self.cli(
            "acquire",
            "--inventory",
            inventory,
            "--cache",
            self.work / "cache",
            "--contract",
            self.report / "keys.md",
            "--output",
            output,
        )
        self.assertEqual(0, run.returncode, run.stderr)
        row = json.loads(output.read_text(encoding="utf-8"))["sources"][0]
        self.assertEqual("readable", row["status"])
        self.assertEqual("changed-bytes", row["prior_relation"])
        self.assertEqual(sha, row["sha256"])
        self.assertEqual(document["info"]["license"], row.get("document_license"))

    def test_acquisition_preserves_failed_real_census_logs_and_recovers(self) -> None:
        # JSON decoding succeeds, but a deeply nested schema exceeds the real
        # census walk's recursion depth. No substitute census process is used.
        spec = self.work / "profond.json"
        schema = {"type": "string"}
        for _ in range(700):
            schema = {"items": schema}
        document = {
            "openapi": "3.0.3",
            "info": {"title": "Profond", "version": "1"},
            "paths": {},
            "components": {"schemas": {"Deep": schema}},
        }
        spec.write_text(json.dumps(document), encoding="utf-8")
        inventory = self.work / "inventory.json"
        inventory.write_text(
            json.dumps({"schema_version": 1, "sources": [{"artifact": spec.as_uri()}]}), encoding="utf-8"
        )
        output = self.work / "acquisition.json"
        args = (
            "acquire",
            "--inventory",
            inventory,
            "--cache",
            self.work / "cache",
            "--contract",
            self.report / "keys.md",
            "--output",
            output,
        )
        refused = self.cli(*args)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("census failed; see", refused.stderr)
        self.assertIn(str(output.with_suffix(".census.log")), refused.stderr)
        recorded = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual("readable", recorded["sources"][0]["status"])
        self.assertNotEqual(0, recorded["census_exit"])
        self.assertIn("RecursionError", output.with_suffix(".census.log").read_text(encoding="utf-8"))
        document["components"]["schemas"]["Deep"] = {"type": "string"}
        spec.write_text(json.dumps(document), encoding="utf-8")
        recovered = self.cli(*args)
        self.assertEqual(0, recovered.returncode, recovered.stderr)
        self.assertEqual(0, json.loads(output.read_text(encoding="utf-8"))["census_exit"])

    def test_committed_wide_report(self) -> None:
        root = REPO / "docs/openapi-surface/witness-scrape-wide"
        result = self.cli("validate", "--report", root, "--inventory", root / "inventory.json.gz")
        self.assertEqual(0, result.returncode, result.stderr)

    def test_consolidated_report_rejects_lost_screens_and_census_evidence(self) -> None:
        import gzip
        import hashlib

        root = self.work / "consolidated"
        shutil.copytree(REPO / "docs/openapi-surface/witness-scrape-wide", root)
        run = lambda: self.cli("validate", "--report", root, "--inventory", root / "inventory.json.gz")
        good = run()
        self.assertEqual(0, good.returncode, good.stderr)
        candidates = root / "candidates.md"
        original = candidates.read_text(encoding="utf-8")
        row = next(line for line in original.splitlines(keepends=True) if line.startswith("| `"))
        candidates.write_text(original.replace(row, "", 1), encoding="utf-8")
        failed = run()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn("missing completed or blocked screens", failed.stderr)
        candidates.write_text(original, encoding="utf-8")
        owned = re.findall(r"`([^`]+)`", row.split("|")[2])
        known = json.loads((root / "baseline.json").read_text(encoding="utf-8"))["keys"]
        other = next(key for key in known if key not in owned)
        candidates.write_text(original.replace(row, row.replace(f"`{owned[0]}`", f"`{other}`", 1), 1), encoding="utf-8")
        failed = run()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn("candidate keys disagree with measured declarations", failed.stderr)
        candidates.write_text(original, encoding="utf-8")
        evidence = root / "publisher-census.tsv"
        content = evidence.read_bytes()
        evidence.unlink()
        failed = run()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn("missing or outside-report evidence", failed.stderr)
        evidence.write_bytes(content)
        acquisition = root / "acquisition.json.gz"
        original_acquisition = acquisition.read_bytes()
        outcome = json.loads(gzip.decompress(original_acquisition))
        catalogue = root / "catalogue-census.tsv"
        # Restore the exact hashed evidence, without platform newline rewriting.
        catalogue_bytes = catalogue.read_bytes()
        catalogue.write_bytes(catalogue_bytes.replace(b"schema.", b"unknown.", 1))
        for record in outcome["census_runs"]:
            if record["stdout"] == catalogue.name:
                record["stdout_sha256"] = hashlib.sha256(catalogue.read_bytes()).hexdigest()
        acquisition.write_bytes(gzip.compress(json.dumps(outcome).encode("utf-8"), mtime=0))
        failed = run()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn("unknown document, selector or key", failed.stderr)
        catalogue.write_bytes(catalogue_bytes)
        acquisition.write_bytes(original_acquisition)
        recovered = run()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_consolidated_report_rejects_corrupt_accounting_and_recovers(self) -> None:
        import gzip
        import hashlib

        root = self.work / "consolidated"
        shutil.copytree(REPO / "docs/openapi-surface/witness-scrape-wide", root)
        run = lambda: self.cli("validate", "--report", root, "--inventory", root / "inventory.json.gz")
        fingerprints = root / "historical-sha256.tsv"
        original_fingerprints = fingerprints.read_text(encoding="utf-8")
        lines = original_fingerprints.splitlines()
        cells = lines[1].split("\t")
        header = lines[0].split("\t")
        cells[header.index("sha256")] = "0" * 64
        lines[1] = "\t".join(cells)
        fingerprints.write_text("\n".join(lines) + "\n", encoding="utf-8")
        refused = run()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("historical report bytes changed", refused.stderr)
        fingerprints.write_text(original_fingerprints, encoding="utf-8")
        acquisition = root / "acquisition.json.gz"
        original = acquisition.read_bytes()
        for mode, message in [
            ("outcome", "missing acquisition outcome"),
            ("diagnostic", "failed acquisition missing diagnostic"),
            ("runs", "missing census runs"),
            ("exit", "unfinished or failed census"),
            ("digest", "census evidence digest changed"),
            ("header", "census evidence header changed"),
            ("count", "invalid declaration count"),
        ]:
            with self.subTest(mode=mode):
                data = json.loads(gzip.decompress(original))
                catalogue = root / "catalogue-census.tsv"
                census_bytes = catalogue.read_bytes()
                if mode == "outcome":
                    data["sources"][0].pop("status")
                elif mode == "diagnostic":
                    failed = next(row for row in data["sources"] if row["status"] != "readable")
                    failed.pop("diagnostic")
                elif mode == "runs":
                    data["census_runs"] = []
                elif mode == "exit":
                    data["census_runs"][0]["exit_code"] = 1
                elif mode == "digest":
                    data["census_runs"][0]["stdout_sha256"] = "0" * 64
                else:
                    rows = census_bytes.decode("utf-8").splitlines()
                    if mode == "header":
                        rows[0] = rows[0].replace("count", "total")
                    else:
                        cells = rows[1].split("\t")
                        cells[-1] = "0"
                        rows[1] = "\t".join(cells)
                    catalogue.write_text("\n".join(rows) + "\n", encoding="utf-8")
                    record = next(row for row in data["census_runs"] if row["stdout"] == catalogue.name)
                    record["stdout_sha256"] = hashlib.sha256(catalogue.read_bytes()).hexdigest()
                acquisition.write_bytes(gzip.compress(json.dumps(data).encode("utf-8"), mtime=0))
                refused = run()
                self.assertNotEqual(0, refused.returncode)
                self.assertIn(message, refused.stderr)
                catalogue.write_bytes(census_bytes)
                acquisition.write_bytes(original)
        recovered = run()
        self.assertEqual(0, recovered.returncode, recovered.stderr)


class PostFreezeGapRowTests(unittest.TestCase):
    """The frozen contract binds its own keys; a gap row admitted later is not its to refuse."""

    REGION_NAMES = redo.WIDE_REGION_NAMES

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.work = Path(self.directory.name)
        self.regions = self.work / "regions"
        self.regions.mkdir()
        for name in self.REGION_NAMES:
            shutil.copyfile(REPO / "docs/openapi-surface" / f"{name}.md", self.regions / f"{name}.md")
        # A `handwritten` row keeps the selector its search ran on only here.
        shutil.copyfile(REPO / "docs/openapi-surface/witness-search-keys.tsv", self.regions / "witness-search-keys.tsv")
        self.schemas = self.regions / "schemas.md"
        self.frozen = dict(redo.WitnessSearchRedoTests.contract_keys(self))

    def cli(self, *args) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(REPO / "tools/witness-search/witness-scrape-wide.py"), *(str(a) for a in args)],
            cwd=REPO,
            capture_output=True,
            encoding="utf-8",
        )

    def derive(self) -> subprocess.CompletedProcess[str]:
        return self.cli("derive", "--report", self.work / "report", "--regions", self.regions)

    def frozen_row(self) -> tuple[str, str]:
        """A search-incomplete gap row the contract owns, and its key.

        Every such row the tree held has since been moved to `handwritten`, so
        one is restored in the copy: the derivation of a frozen gap row is still
        what these tests are about.
        """
        for line in self.schemas.read_text(encoding="utf-8").splitlines():
            key = line.split("|")[1].strip().strip("`") if line.startswith("| ") else ""
            if key in self.frozen and "search outcome `search-incomplete`" in line and " gap " in line:
                return key, line
        sys.path.insert(0, str(REPO / "tools" / "surface-census" / "tests"))
        from region_flip import restore_gap_row

        key = "property-sole-oneof-composed-member"
        self.assertIn(key, self.frozen)
        return key, restore_gap_row(self.schemas, key)

    def test_a_search_incomplete_gap_row_admitted_after_the_freeze_is_skipped(self) -> None:
        key, line = self.frozen_row()
        admitted = line.replace(f"| {key} |", "| admitted-after-freeze |", 1).replace(
            f"| `{key}` |", "| `admitted-after-freeze` |", 1
        )
        self.assertNotEqual(line, admitted)
        text = self.schemas.read_text(encoding="utf-8")
        self.schemas.write_text(text.replace(line, f"{line}\n{admitted}", 1), encoding="utf-8")
        derived = self.derive()
        self.assertEqual(0, derived.returncode, derived.stderr)
        keys = json.loads((self.work / "report" / "baseline.json").read_text(encoding="utf-8"))["keys"]
        self.assertIn(key, keys)
        self.assertNotIn("admitted-after-freeze", keys)

    def test_a_flip_to_handwritten_keeps_the_baseline_the_shards_decide(self) -> None:
        """A frozen key whose row a hand-written fixture moved stays reconciled.

        Its row carries no inline outcome any more, so the shards decide its
        membership: a `search-incomplete` key stays in the baseline with its
        tracked selector, a `witness-found` one stays out, and the committed
        wide report still validates over the flipped regions, which it can only
        do by reading the flipped row's selector from the tracked file.
        """
        sys.path.insert(0, str(REPO / "tools" / "surface-census" / "tests"))
        from region_flip import flipped_regions

        before = self.derive()
        self.assertEqual(0, before.returncode, before.stderr)
        baseline = (self.work / "report" / "baseline.json").read_bytes()
        kept, excluded = "annotated-ref-target-string-const", "oneof-bare-object-example-variant"
        self.assertIn(kept, json.loads(baseline)["keys"])
        self.assertNotIn(excluded, json.loads(baseline)["keys"])
        for key in (kept, excluded):
            with self.subTest(key=key):
                regions = flipped_regions(self.work / f"flipped-{key}", key)
                derived = self.cli("derive", "--report", self.work / f"report-{key}", "--regions", regions)
                self.assertEqual(0, derived.returncode, derived.stderr)
                self.assertEqual(baseline, (self.work / f"report-{key}" / "baseline.json").read_bytes())
                committed = REPO / "docs/openapi-surface/witness-scrape-wide"
                validated = self.cli(
                    "validate",
                    "--report",
                    committed,
                    "--inventory",
                    committed / "inventory.json.gz",
                    "--regions",
                    regions,
                )
                self.assertEqual(0, validated.returncode, validated.stderr)
        regions = self.work / f"flipped-{kept}"
        tracked = (regions / "witness-search-keys.tsv").read_text(encoding="utf-8")
        (regions / "witness-search-keys.tsv").write_text(
            tracked.replace(f"{kept}\t{self.frozen[kept]}", f"{kept}\tschema.oneOf", 1), encoding="utf-8"
        )
        refused = self.cli("derive", "--report", self.work / "refused", "--regions", regions)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn(f"schemas/{kept}: selector disagrees with frozen authority", refused.stderr)
        (regions / "witness-search-keys.tsv").write_text(
            "".join(line for line in tracked.splitlines(keepends=True) if not line.startswith(f"{kept}\t")),
            encoding="utf-8",
        )
        missing = self.cli("derive", "--report", self.work / "missing", "--regions", regions)
        self.assertNotEqual(0, missing.returncode)
        self.assertIn(f"schemas/{kept}: handwritten, and no selector in witness-search-keys.tsv", missing.stderr)

    def test_a_frozen_key_whose_row_leaves_its_census_selector_still_fails(self) -> None:
        key, line = self.frozen_row()
        moved = line.replace(f"census `{self.frozen[key]}`", "census `schema.oneOf`", 1)
        self.assertNotEqual(line, moved)
        text = self.schemas.read_text(encoding="utf-8")
        self.schemas.write_text(text.replace(line, moved, 1), encoding="utf-8")
        refused = self.derive()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn(f"schemas/{key}: selector disagrees with frozen authority", refused.stderr)

    def test_a_frozen_shard_whose_bytes_change_still_fails(self) -> None:
        report = self.work / "wide"
        shutil.copytree(REPO / "docs/openapi-surface/witness-scrape-wide", report)
        (REPO / ".local").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=REPO / ".local") as local:
            shard = Path(local) / "catalogue-portals.md"
            original = ROOT / "catalogue-portals.md"
            shard.write_bytes(original.read_bytes() + b"| `admitted-after-freeze` |\n")
            fingerprints = report / "historical-sha256.tsv"
            text = fingerprints.read_text(encoding="utf-8")
            relative = original.relative_to(REPO).as_posix()
            self.assertIn(relative, text)
            fingerprints.write_text(text.replace(relative, shard.relative_to(REPO).as_posix(), 1), encoding="utf-8")
            refused = self.cli("validate", "--report", report, "--inventory", report / "inventory.json.gz")
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("historical report bytes changed", refused.stderr)


if __name__ == "__main__":
    unittest.main()

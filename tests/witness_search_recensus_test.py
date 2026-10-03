#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier has no Nx workspace; this test sits in tests/ beside the other witness-search suites and runs under `just test-census-fallback`, which CI's live-e2e leg runs.
"""`scripts/witness-search-recensus.py`, driven through its real CLI.

`full-yaml` over a temporary ledger whose parse failures name real documents in
a temporary cache: one only the full YAML parser reads, one only its lenient
reading reads, one no reading reads, one that is YAML but no OpenAPI
description, and one that names Swagger 2.0. Each ledger row it appends, and the `records.tsv` row
`witness-search-github-index.py` derives from it, says what was read and how.
A parse failure no cache holds is read again at its recorded commit from a
loopback Sourcegraph, and refused where what it serves is not the pinned digest.

`reacquire-head` against a loopback server standing in for api.github.com,
raw.githubusercontent.com and Sourcegraph: a file the head still holds, a
deleted repository whose blob Sourcegraph's mirror still serves, and one
nothing serves. `reacquire-namesake` against the same server: a refused fork
whose parent's history still holds its blob, and ones no namesake holds. Every
REST call is logged by the rate-limit guard.

It needs the search's pinned ruamel.yaml: run it as `just test-census-fallback`.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "witness-search-recensus.py"
KEY = "property-sole-anyof-composed-member"
SELECTOR = "schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf"

# The census's stdlib loader refuses the explicit `? ` key; YAML 1.2 reads it.
DECLARER = b"""openapi: 3.0.3
info: {title: Pets, version: '1'}
paths:
  ? /pets
  : get:
      responses:
        '200': {description: ok}
components:
  schemas:
    Base:
      type: object
      properties:
        id: {type: string}
    Pet:
      type: object
      properties:
        owner:
          anyOf:
            - allOf:
                - $ref: '#/components/schemas/Base'
"""
# A duplicate key the strict construction refuses and the lenient reading keeps last.
DUPLICATE = b"""openapi: 3.0.3
info: {title: First, version: '1'}
info: {title: Second, version: '1'}
paths: {}
"""
TEMPLATE = b"{{- if .Values.enabled }}\nopenapi: 3.0.0\n{{- end }}\n"
NOT_OPENAPI = b"name: chart\nversion: 1.0.0\n"
# Names a version, but Swagger 2.0's, which the census does not read.
SWAGGER = b"swagger: '2.0'\ninfo: {title: Legacy, version: '1'}\npaths: {}\n"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


INDEX = _load("witness_search_github_index", REPO / "scripts" / "witness-search-github-index.py")


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


OTHER = "oneof-anyof-variant"


def keys_file(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "keys.json").write_text(json.dumps({"keys": {
        KEY: {"region": "schemas", "selector": SELECTOR, "selector_status": "available"},
        OTHER: {"region": "schemas", "selector": "schema.oneOf>schema.anyOf", "selector_status": "available"},
    }}), encoding="utf-8")


def run(*args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True,
                          env={**os.environ, **(env or {})}, timeout=300)


class FullYamlTest(unittest.TestCase):
    def test_each_parse_failure_is_read_again_and_recorded_with_its_reading(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            rows = []
            for name, data in (("declarer", DECLARER), ("duplicate", DUPLICATE), ("template", TEMPLATE),
                               ("chart", NOT_OPENAPI), ("legacy", SWAGGER)):
                digest = hashlib.sha256(data).hexdigest()
                (cache / "documents" / f"{digest}.yaml").write_bytes(data)
                rows.append({"source": "sourcegraph", "key": KEY, "selector": SELECTOR,
                             "repository": f"github.com/example/{name}", "path": "openapi.yaml",
                             "commit": "c" * 40, "sha256": digest, "document": f"{digest}.yaml",
                             "disposition": "parse-failure", "diagnostic": "the stdlib loader refused it"})
            other = {**rows[0], "key": OTHER, "selector": "schema.oneOf>schema.anyOf"}
            (evidence / "candidates.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in [*rows, other]), encoding="utf-8")

            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                            "--cache", str(cache), "--jobs", "2", "--key", KEY)
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("5 parse-failure row(s) over 5 document(s) read again", completed.stdout)

            appended = {row["repository"].rsplit("/", 1)[1]: row
                        for _, row in INDEX.jsonl(evidence / "candidates.jsonl") if row.get("loader")}
            self.assertEqual("declares", appended["declarer"]["disposition"])
            self.assertEqual(1, appended["declarer"]["selector_count"])
            self.assertEqual("ruamel.yaml 0.19.1 (YAML 1.2)", appended["declarer"]["loader"])
            self.assertEqual("does-not-declare", appended["duplicate"]["disposition"])
            self.assertIn("duplicate keys last-wins", appended["duplicate"]["loader"])
            self.assertEqual("census-refused", appended["template"]["disposition"])
            self.assertIn("ruamel.yaml 0.19.1", appended["template"]["diagnostic"])
            self.assertIn(f"sha256 {rows[2]['sha256']}", appended["template"]["diagnostic"])
            self.assertEqual("excluded-non-openapi-3", appended["chart"]["disposition"])
            self.assertIn("0 naming an `openapi` or `swagger` version", appended["chart"]["diagnostic"])
            self.assertEqual("excluded-non-openapi-3", appended["legacy"]["disposition"])
            self.assertEqual("names `openapi` None / `swagger` '2.0'", appended["legacy"]["diagnostic"])
            self.assertEqual(0, appended["legacy"]["selector_count"])

            records = {row["candidate"].split("/", 1)[1].split(":")[0]: row
                       for row in INDEX.source_rows(root, "sourcegraph")}
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["declarer"]["census"])
            self.assertEqual("outstanding", records["declarer"]["disposition"])  # its screens are owed
            self.assertTrue(records["duplicate"]["census"].startswith("census 0; read by ruamel.yaml"))
            self.assertEqual("rejected", records["duplicate"]["disposition"])
            self.assertTrue(records["template"]["census"].startswith("census-refused: ruamel.yaml 0.19.1"))
            self.assertEqual("rejected", records["template"]["disposition"])
            self.assertEqual("rejected", records["chart"]["disposition"])
            self.assertEqual("rejected", records["legacy"]["disposition"])

            # The key filter left the other key's row to a later run, which reads it and no more.
            self.assertEqual("outstanding", next(r for r in INDEX.source_rows(root, "sourcegraph")
                                                 if r["key"] == OTHER)["disposition"])
            again = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache))
            self.assertEqual(0, again.returncode, again.stderr)
            self.assertIn("1 parse-failure row(s) over 1 document(s) read again: 1 does-not-declare", again.stdout)

    def test_a_publisher_tree_document_is_censused_for_every_key(self) -> None:
        # A publisher tree's ledger is `documents.jsonl`, keyed by document rather than by key:
        # each reading records every key's count under `status`, whatever `--key` names.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-publisher-trees"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            rows = []
            for name, data in (("declarer", DECLARER), ("template", TEMPLATE), ("chart", NOT_OPENAPI)):
                digest = hashlib.sha256(data).hexdigest()
                (cache / "documents" / f"{digest}.yaml").write_bytes(data)
                rows.append({"source": "github-publisher-trees", "repository": "example/publisher",
                             "path": f"{name}.yaml", "commit": "c" * 40, "blob": git_blob(data),
                             "sha256": digest, "status": "parse-failure",
                             "diagnostic": "the stdlib loader refused it"})
            (evidence / "documents.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")

            completed = run("--evidence-root", str(root), "full-yaml", "--source", "github-publisher-trees",
                            "--cache", str(cache), "--key", OTHER)
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("github-publisher-trees: 3 parse-failure row(s) over 3 document(s) read again: "
                          "1 census-refused, 1 excluded-non-openapi-3, 1 readable", completed.stdout)

            appended = {row["path"].split(".")[0]: row
                        for _, row in INDEX.jsonl(evidence / "documents.jsonl") if row.get("loader")}
            self.assertEqual({"declarer", "template", "chart"}, set(appended))
            self.assertTrue(all("disposition" not in row for row in appended.values()))
            self.assertEqual("readable", appended["declarer"]["status"])
            self.assertEqual({KEY: 1, OTHER: 0}, appended["declarer"]["selector_counts"])
            self.assertEqual("census-refused", appended["template"]["status"])
            self.assertIn(f"sha256 {rows[1]['sha256']}", appended["template"]["diagnostic"])
            self.assertEqual("excluded-non-openapi-3", appended["chart"]["status"])
            self.assertNotIn("selector_count", appended["chart"])

            records = {(row["key"], row["candidate"].split(":")[1].split(".")[0]): row
                       for row in INDEX.source_rows(root, "github-publisher-trees")}
            self.assertEqual(6, len(records), records)  # the re-reading supersedes each parse failure
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records[(KEY, "declarer")]["census"])
            self.assertEqual("census 0; read by ruamel.yaml 0.19.1 (YAML 1.2)", records[(OTHER, "declarer")]["census"])
            self.assertTrue(records[(KEY, "template")]["census"].startswith("census-refused: ruamel.yaml 0.19.1"))
            self.assertEqual("rejected", records[(OTHER, "chart")]["disposition"])

            again = run("--evidence-root", str(root), "full-yaml", "--source", "github-publisher-trees",
                        "--cache", str(cache))
            self.assertIn("0 parse-failure row(s) over 0 document(s) read again", again.stdout)

    def test_a_key_added_after_a_publisher_tree_rereading_is_counted_from_the_same_copy(self) -> None:
        # The full parser read the document while `keys.json` named only KEY; OTHER joined
        # later, so its record would stay owed until the same copy is read again for it.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-publisher-trees"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            digest = hashlib.sha256(DECLARER).hexdigest()
            (cache / "documents" / f"{digest}.yaml").write_bytes(DECLARER)
            first = {"source": "github-publisher-trees", "repository": "example/publisher",
                     "path": "declarer.yaml", "commit": "c" * 40, "blob": git_blob(DECLARER),
                     "sha256": digest, "status": "parse-failure", "diagnostic": "the stdlib loader refused it"}
            read = {**{k: v for k, v in first.items() if k != "diagnostic"}, "status": "readable",
                    "loader": "ruamel.yaml 0.19.1 (YAML 1.2)", "recensus_of": "parse-failure",
                    "selector_counts": {KEY: 1}}
            (evidence / "documents.jsonl").write_text(json.dumps(first) + "\n" + json.dumps(read) + "\n",
                                                      encoding="utf-8")
            owed = {row["key"]: row for row in INDEX.source_rows(root, "github-publisher-trees")}
            self.assertEqual("outstanding", owed[OTHER]["disposition"])
            self.assertIn("never counted this key", owed[OTHER]["census"])

            completed = run("--evidence-root", str(root), "full-yaml", "--source", "github-publisher-trees",
                            "--cache", str(cache), "--key", OTHER)
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("github-publisher-trees: 0 parse-failure row(s) and 1 full-parser reading(s) "
                          "missing a key's count over 1 document(s) read again: 1 readable", completed.stdout)
            appended = [row for _, row in INDEX.jsonl(evidence / "documents.jsonl")][-1]
            self.assertEqual({KEY: 1, OTHER: 0}, appended["selector_counts"])
            self.assertEqual("parse-failure", appended["recensus_of"])

            records = {row["key"]: row for row in INDEX.source_rows(root, "github-publisher-trees")}
            self.assertEqual("census 0; read by ruamel.yaml 0.19.1 (YAML 1.2)", records[OTHER]["census"])
            self.assertEqual("rejected", records[OTHER]["disposition"])
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records[KEY]["census"])

            again = run("--evidence-root", str(root), "full-yaml", "--source", "github-publisher-trees",
                        "--cache", str(cache))
            self.assertIn("0 parse-failure row(s) over 0 document(s) read again", again.stdout)

    def test_a_document_past_the_time_bound_is_refused_with_the_bound(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            # Large enough that the pure-Python parser cannot finish it inside one second.
            data = b"openapi: 3.0.3\nx:\n" + b"".join(b"  k%d: [a, {b: c}]\n" % n for n in range(400_000))
            digest = hashlib.sha256(data).hexdigest()
            (cache / "documents" / f"{digest}.yaml").write_bytes(data)
            row = {"source": "sourcegraph", "key": KEY, "repository": "github.com/example/huge", "path": "a.yaml",
                   "commit": "c" * 40, "sha256": digest, "disposition": "parse-failure"}
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                            "--cache", str(cache), "--timeout", "1")
            self.assertEqual(0, completed.returncode, completed.stderr)
            refused = [r for _, r in INDEX.jsonl(evidence / "candidates.jsonl") if r.get("loader")]
            self.assertEqual("census-refused", refused[0]["disposition"])
            self.assertIn("parse exceeded 1 s", refused[0]["diagnostic"])
            self.assertIn(f"sha256 {digest}", refused[0]["diagnostic"])

    def test_a_census_walk_past_its_bound_or_its_depth_is_refused(self) -> None:
        # Aliases cost the parser nothing and the walk everything: eleven levels of eight
        # shared `allOf` members is 8^11 schemas to walk, and a 1,500-link chain kept under an
        # `x-` extension is one schema 1,500 levels deep.
        bomb = ["openapi: 3.0.3", "info: {title: t, version: '1'}", "paths: {}", "components:", "  schemas:",
                "    L0: &l0 {type: object, properties: {a: {type: string}}}"]
        bomb += [f"    L{n}: &l{n} {{allOf: [{', '.join([f'*l{n - 1}'] * 8)}]}}" for n in range(1, 12)]
        chain = ["openapi: 3.0.3", "info: {title: t, version: '1'}", "paths: {}", "x-chain:", "  - &l0 {type: string}"]
        chain += [f"  - &l{n} {{type: array, items: *l{n - 1}}}" for n in range(1, 1500)]
        chain += ["components:", "  schemas:", "    Deep: *l1499"]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            rows = []
            for name, text in (("bomb", bomb), ("chain", chain)):
                data = ("\n".join(text) + "\n").encode()
                digest = hashlib.sha256(data).hexdigest()
                (cache / "documents" / f"{digest}.yaml").write_bytes(data)
                rows.append({"source": "sourcegraph", "key": KEY, "repository": f"github.com/example/{name}",
                             "path": "a.yaml", "commit": "c" * 40, "sha256": digest, "disposition": "parse-failure"})
            (evidence / "candidates.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                            "--cache", str(cache), "--timeout", "2")
            self.assertEqual(0, completed.returncode, completed.stderr)
            refused = {r["repository"].rsplit("/", 1)[1]: r
                       for _, r in INDEX.jsonl(evidence / "candidates.jsonl") if r.get("loader")}
            self.assertEqual({"census-refused"}, {r["disposition"] for r in refused.values()})
            self.assertTrue(refused["bomb"]["diagnostic"].startswith(
                "census walk over the ruamel.yaml 0.19.1 (YAML 1.2) reading exceeded 2 s; sha256 "))
            self.assertTrue(refused["chain"]["diagnostic"].startswith(
                "census walk over the ruamel.yaml 0.19.1 (YAML 1.2) reading: RecursionError: "))
            self.assertIn(f"sha256 {rows[1]['sha256']}", refused["chain"]["diagnostic"])

    def test_an_absent_copy_and_a_bad_bound_name_their_repair(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            row = {"source": "sourcegraph", "key": KEY, "repository": "github.com/example/api", "path": "a.yaml",
                   "commit": "c" * 40, "sha256": "a" * 64, "disposition": "parse-failure"}
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
            missing = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                          "--cache", str(Path(tmp) / "empty"))
            self.assertEqual(1, missing.returncode)
            self.assertIn(f"no cached copy of sha256 {'a' * 64}", missing.stderr)
            self.assertIn(f"and it cannot be reacquired: the ledger row for github.com/example/api/a.yaml@{'c' * 40} "
                          "records no acquisition route to reacquire its document by", missing.stderr)
            self.assertIn("pass the cache it was acquired into with --cache", missing.stderr)
            bound = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                        "--cache", str(Path(tmp) / "empty"), "--jobs", "0")
            self.assertEqual(2, bound.returncode)
            self.assertIn("--jobs and --timeout must be positive", bound.stderr)

    def test_a_copy_no_cache_holds_is_reacquired_at_its_commit_and_refused_if_it_differs(self) -> None:
        """A parse failure whose bytes no cache holds is read from its recorded source, verified first."""
        server = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        env = {"CROZIER_SOURCEGRAPH_URL": f"http://127.0.0.1:{server.server_port}"}
        digest = hashlib.sha256(DECLARER).hexdigest()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            row = {"source": "sourcegraph", "key": KEY, "selector": SELECTOR,
                   "repository": "github.com/example/mirrored", "path": "openapi.yaml", "commit": PINNED,
                   "acquisition_route": "sourcegraph-paced", "sha256": digest, "document": f"{digest}.yaml",
                   "disposition": "parse-failure", "diagnostic": "the stdlib loader refused it"}
            ledger = evidence / "candidates.jsonl"
            ledger.write_text(json.dumps({**row, "repository": "github.com/example/tampered"}) + "\n",
                              encoding="utf-8")
            refused = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                          "--cache", str(cache), env=env)
            self.assertEqual(1, refused.returncode)
            self.assertIn(f"refused: github.com/example/tampered/openapi.yaml@{PINNED} served sha256 "
                          f"{hashlib.sha256(DUPLICATE).hexdigest()}, not the {digest} the ledger pins",
                          refused.stderr)
            self.assertEqual(1, len(ledger.read_text(encoding="utf-8").splitlines()))
            self.assertEqual([], list((cache / "documents").glob("*")) if (cache / "documents").is_dir() else [])

            ledger.write_text(json.dumps(row) + "\n", encoding="utf-8")
            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                            "--cache", str(cache), env=env)
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("1 parse-failure row(s) over 1 document(s) read again: 1 declares", completed.stdout)
            self.assertEqual([f"/github.com/example/tampered/-/raw/openapi.yaml?rev={PINNED}",
                              f"/github.com/example/mirrored/-/raw/openapi.yaml?rev={PINNED}"], server.paths)
            self.assertEqual(DECLARER, (cache / "documents" / f"{digest}.yaml").read_bytes())

            # A source that no longer serves the document leaves it unread, naming the repair.
            gone = {**row, "repository": "github.com/example/gone", "sha256": "b" * 64, "document": f"{'b' * 64}.yaml"}
            ledger.write_text(json.dumps(gone) + "\n", encoding="utf-8")
            unserved = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                           "--cache", str(cache), env=env)
            self.assertEqual(1, unserved.returncode)
            self.assertIn(f"no cached copy of sha256 {'b' * 64}", unserved.stderr)
            self.assertIn("its recorded source no longer serves it; pass the cache it was acquired into with --cache",
                          unserved.stderr)

            # With no --cache the reacquired copy lands in the gitignored default cache.
            default = REPO / ".local" / "witness-search-cache" / "documents" / f"{digest}.yaml"
            if not default.exists():
                self.addCleanup(default.unlink, missing_ok=True)
            ledger.write_text(json.dumps(row) + "\n", encoding="utf-8")
            defaulted = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", env=env)
            self.assertEqual(0, defaulted.returncode, defaulted.stderr)
            self.assertEqual(DECLARER, default.read_bytes())
            self.assertEqual(0, subprocess.run(["git", "check-ignore", "--quiet", str(default)], cwd=REPO).returncode)

    def test_a_copy_read_from_the_mirror_is_reacquired_from_the_mirror(self) -> None:
        """A GitHub row the mirror served is read from the mirror again, under its host, verified first."""
        server = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        env = {"CROZIER_GITHUB_API_URL": url, "CROZIER_RAW_GITHUB_URL": url,
               "CROZIER_SOURCEGRAPH_URL": url, "GITHUB_TOKEN": "offline-test-token"}
        digest = hashlib.sha256(DECLARER).hexdigest()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-code-search"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            row = {"source": "github-code-search", "key": KEY, "selector": SELECTOR,
                   "repository": "example/mirrored", "path": "openapi.yaml", "commit": PINNED,
                   "blob": git_blob(DECLARER), "acquisition_route": "sourcegraph-mirror", "sha256": digest,
                   "document": f"{digest}.yaml", "disposition": "parse-failure",
                   "diagnostic": "the stdlib loader refused it"}
            ledger = evidence / "candidates.jsonl"
            ledger.write_text(json.dumps({**row, "repository": "example/tampered"}) + "\n", encoding="utf-8")
            refused = run("--evidence-root", str(root), "full-yaml", "--source", "github-code-search",
                          "--cache", str(cache), env=env)
            self.assertEqual(1, refused.returncode)
            self.assertIn(f"refused: example/tampered/openapi.yaml@{PINNED} served sha256 "
                          f"{hashlib.sha256(DUPLICATE).hexdigest()}, not the {digest} the ledger pins",
                          refused.stderr)
            self.assertFalse((cache / "documents").is_dir() and any((cache / "documents").iterdir()))

            ledger.write_text(json.dumps(row) + "\n", encoding="utf-8")
            completed = run("--evidence-root", str(root), "full-yaml", "--source", "github-code-search",
                            "--cache", str(cache), env=env)
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("1 parse-failure row(s) over 1 document(s) read again: 1 declares", completed.stdout)
            self.assertEqual([f"/github.com/example/tampered/-/raw/openapi.yaml?rev={PINNED}",
                              f"/github.com/example/mirrored/-/raw/openapi.yaml?rev={PINNED}"], server.paths)
            self.assertEqual(DECLARER, (cache / "documents" / f"{digest}.yaml").read_bytes())

    def test_a_copy_that_does_not_hash_to_its_pin_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            digest = hashlib.sha256(DECLARER).hexdigest()
            (cache / "documents" / f"{digest}.yaml").write_bytes(DUPLICATE)
            row = {"source": "sourcegraph", "key": KEY, "repository": "github.com/example/api", "path": "a.yaml",
                   "commit": "c" * 40, "sha256": digest, "disposition": "parse-failure"}
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache))
            self.assertEqual(1, completed.returncode)
            self.assertIn("does not hash to the pinned sha256", completed.stderr)
            self.assertIn("re-acquire it at its commit", completed.stderr)


HEAD = "d" * 40
PINNED = "e" * 40
OLDER = "f" * 40


class Upstream(BaseHTTPRequestHandler):
    def log_message(self, *args: object) -> None:
        pass

    def reply(self, status: int, body: bytes | dict) -> None:
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        self.server.paths.append(self.path)
        reset = int(time.time()) + 60
        if self.path == "/rate_limit":
            self.reply(200, {"resources": {"core": {"limit": 5000, "used": 0, "remaining": 5000, "reset": reset},
                                           "search": {"limit": 30, "used": 0, "remaining": 30, "reset": reset}}})
        elif self.path == "/search/repositories?q=forked%20in%3Aname&per_page=100":
            # The candidate itself, a parent and an unrelated partial match: only the parent is a namesake.
            self.reply(200, {"items": [{"full_name": "example/forked"}, {"full_name": "upstream/Forked"},
                                       {"full_name": "other/forked-too"}]})
        elif self.path == "/search/repositories?q=stale%20in%3Aname&per_page=100":
            self.reply(200, {"items": [{"full_name": "upstream/stale"}]})
        elif self.path == "/repos/upstream/stale/commits?path=openapi.yaml&per_page=100":
            self.reply(500, {"message": "Server Error"})
        elif self.path == "/search/repositories?q=orphan%20in%3Aname&per_page=100":
            self.reply(200, {"items": []})
        elif self.path == "/search/repositories?q=unsearched%20in%3Aname&per_page=100":
            self.reply(422, {"message": "Validation Failed"})
        elif self.path == "/repos/upstream/Forked/commits?path=openapi.yaml&per_page=100":
            self.reply(200, [{"sha": HEAD}, {"sha": OLDER}])  # changed since the fork, held before it
        elif self.path == f"/upstream/Forked/{HEAD}/openapi.yaml":
            self.reply(200, DUPLICATE)
        elif self.path == f"/upstream/Forked/{OLDER}/openapi.yaml":
            self.reply(200, DECLARER)
        elif self.path == "/repos/example/kept":
            self.reply(200, {"default_branch": "main"})
        elif self.path == "/repos/example/kept/commits/main":
            self.reply(200, {"sha": HEAD})
        elif self.path == f"/example/kept/{HEAD}/openapi.yaml":
            self.reply(200, DECLARER)
        elif self.path in ("/repos/example/moved", "/repos/example/dropped", "/repos/example/headless",
                           "/repos/example/unlisted"):
            self.reply(200, {"default_branch": "main"})
        elif self.path == "/repos/example/unlisted/commits/main":
            self.reply(200, {"sha": HEAD})
        elif self.path.startswith("/repos/example/unlisted/commits?path="):
            self.reply(500, {"message": "Server Error"})
        elif self.path in ("/repos/example/moved/commits/main", "/repos/example/dropped/commits/main"):
            self.reply(200, {"sha": HEAD})
        elif self.path == f"/repos/example/moved/commits?path=openapi.yaml&sha={HEAD}&per_page=100":
            self.reply(200, [{"sha": HEAD}, {"sha": OLDER}])  # removed at head, present before it
        elif self.path == f"/repos/example/dropped/commits?path=openapi.yaml&sha={HEAD}&per_page=100":
            self.reply(200, [])
        elif self.path == f"/example/moved/{OLDER}/openapi.yaml":
            self.reply(200, DECLARER)
        elif self.path.startswith("/repos/"):
            self.reply(404, {"message": "Not Found"})
        elif self.path == f"/github.com/example/mirrored/-/raw/openapi.yaml?rev={PINNED}":
            self.reply(200, DECLARER)
        elif self.path == f"/github.com/example/tampered/-/raw/openapi.yaml?rev={PINNED}":
            self.reply(200, DUPLICATE)
        else:
            self.reply(404, b"Not Found")


class ReacquireHeadTest(unittest.TestCase):
    def test_each_404_is_requested_at_head_then_at_the_mirror(self) -> None:
        server = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-code-search"
            keys_file(evidence)
            rows = [{"source": "github-code-search", "key": KEY, "selector": SELECTOR,
                     "repository": f"example/{name}", "path": "openapi.yaml", "commit": PINNED,
                     "blob": git_blob(DECLARER), "disposition": "acquisition-failure", "status": 404,
                     "diagnostic": "404: Not Found"}
                    for name in ("kept", "mirrored", "gone", "moved", "dropped", "headless", "unlisted")]
            (evidence / "candidates.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")

            completed = run("--evidence-root", str(root), "reacquire-head", "--cache-dir", str(Path(tmp) / "cache"),
                            env={"CROZIER_GITHUB_API_URL": url, "CROZIER_RAW_GITHUB_URL": url,
                                 "CROZIER_SOURCEGRAPH_URL": url, "GITHUB_TOKEN": "offline-test-token"})
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("7 404 candidate(s) requested at head: 4 acquisition-failure, 3 declares", completed.stdout)

            records = {row["candidate"].split(":")[0].split("/")[1]: row
                       for row in INDEX.source_rows(root, "github-code-search")}
            self.assertEqual(7, len(records), records)  # a read at another commit supersedes its pinned 404
            self.assertEqual(HEAD, records["kept"]["revision"])
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["kept"]["census"])
            self.assertEqual(PINNED, records["mirrored"]["revision"])
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["mirrored"]["census"])
            self.assertEqual("outstanding", records["gone"]["disposition"])
            self.assertIn("GET /repos/example/gone answered HTTP 404 at", records["gone"]["census"])
            self.assertIn(f"Sourcegraph's mirror at {PINNED} served HTTP 404 at", records["gone"]["census"])

            # Head served, file gone from it: the path's history reaches the pinned blob.
            self.assertEqual(OLDER, records["moved"]["revision"])
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["moved"]["census"])
            # Head served, and neither its history nor the mirror holds the blob: refused, at its pin.
            self.assertEqual(PINNED, records["dropped"]["revision"])
            self.assertEqual("outstanding", records["dropped"]["disposition"])
            self.assertIn(f"openapi.yaml at {HEAD} (head of main) answered HTTP 404 at", records["dropped"]["census"])
            self.assertIn(f"the path's history at {HEAD} lists 0 commit(s), none serving blob", records["dropped"]["census"])
            self.assertIn(f"Sourcegraph's mirror at {PINNED} served HTTP 404 at", records["dropped"]["census"])
            # A head commit GitHub will not name, and a history GitHub will not list.
            self.assertIn("GET /repos/example/headless/commits/main answered HTTP 404 at", records["headless"]["census"])
            self.assertIn(f"the path's history at {HEAD} answered HTTP 500 at", records["unlisted"]["census"])
            self.assertEqual({"outstanding"}, {records[name]["disposition"] for name in ("headless", "unlisted")})

            ledger = {row["repository"].split("/")[1]: row for _, row in INDEX.jsonl(evidence / "candidates.jsonl")}
            self.assertEqual("sourcegraph-mirror", ledger["mirrored"]["acquisition_route"])
            guarded = [row for _, row in INDEX.jsonl(evidence / "rate-limit-calls.jsonl") if row.get("bucket") == "core"]
            rest = [path for path in server.paths if path.startswith("/repos/")]
            self.assertEqual(len(rest), len(guarded))
            # seven repositories, five head commits asked for, and three histories of the path
            self.assertEqual(15, len(rest))
            sourcegraph = [row for _, row in INDEX.jsonl(evidence / "rate-limit-calls.jsonl")
                           if row.get("host") == "sourcegraph"]
            self.assertEqual(5, len(sourcegraph))

            # A second run leaves what the first decided; `--again` requests only what is still refused.
            env = {"CROZIER_GITHUB_API_URL": url, "CROZIER_RAW_GITHUB_URL": url,
                   "CROZIER_SOURCEGRAPH_URL": url, "GITHUB_TOKEN": "offline-test-token"}
            second = run("--evidence-root", str(root), "reacquire-head", "--cache-dir", str(Path(tmp) / "cache"), env=env)
            self.assertIn("0 404 candidate(s) requested at head", second.stdout)
            again = run("--evidence-root", str(root), "reacquire-head", "--again",
                        "--cache-dir", str(Path(tmp) / "cache"), env=env)
            self.assertEqual(0, again.returncode, again.stderr)
            self.assertIn("4 404 candidate(s) requested at head: 4 acquisition-failure", again.stdout)
            self.assertEqual(7, len(INDEX.source_rows(root, "github-code-search")))

            misspelt = run("--evidence-root", str(root), "reacquire-head", "--key", "no-such-key",
                           "--cache-dir", str(Path(tmp) / "cache"))
            self.assertEqual(2, misspelt.returncode)
            self.assertIn("--key ['no-such-key'] names no key of witness-search-github-code-search/keys.json",
                          misspelt.stderr)

            invalid = run("--evidence-root", str(root), "reacquire-head", "--again",
                          "--cache-dir", str(Path(tmp) / "cache"),
                          env={"CROZIER_GITHUB_API_URL": url, "CROZIER_SOURCEGRAPH_URL": "file:///etc/passwd"})
            self.assertEqual(1, invalid.returncode)
            self.assertIn("CROZIER_SOURCEGRAPH_URL must use https://sourcegraph.com", invalid.stderr)


class MirrorHashTest(unittest.TestCase):
    def test_a_mirror_blob_of_another_hash_is_not_the_candidate(self) -> None:
        server = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-code-search"
            keys_file(evidence)
            row = {"source": "github-code-search", "key": KEY, "selector": SELECTOR, "repository": "example/tampered",
                   "path": "openapi.yaml", "commit": PINNED, "blob": git_blob(DECLARER),
                   "disposition": "acquisition-failure", "status": 404, "diagnostic": "404: Not Found"}
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
            completed = run("--evidence-root", str(root), "reacquire-head", "--cache-dir", str(Path(tmp) / "cache"),
                            env={"CROZIER_GITHUB_API_URL": url, "CROZIER_RAW_GITHUB_URL": url,
                                 "CROZIER_SOURCEGRAPH_URL": url, "GITHUB_TOKEN": "offline-test-token"})
            self.assertEqual(0, completed.returncode, completed.stderr)
            (record,) = INDEX.source_rows(root, "github-code-search")
            self.assertEqual((PINNED, "outstanding"), (record["revision"], record["disposition"]))
            self.assertIn(f"Sourcegraph's mirror at {PINNED} served a blob hashing to {git_blob(DUPLICATE)}, "
                          f"not {git_blob(DECLARER)} at", record["census"])


class ReacquireNamesakeTest(unittest.TestCase):
    def test_each_refused_candidate_is_sought_in_its_namesakes(self) -> None:
        server = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        env = {"CROZIER_GITHUB_API_URL": url, "CROZIER_RAW_GITHUB_URL": url, "GITHUB_TOKEN": "offline-test-token"}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-code-search"
            keys_file(evidence)
            refusal = "GET /repos/example/{} answered HTTP 404 at 2026-09-29T06:00:00+00:00"
            rows = [{"source": "github-code-search", "key": KEY, "selector": SELECTOR,
                     "repository": f"example/{name}", "path": "openapi.yaml", "commit": PINNED,
                     "blob": git_blob(DECLARER), "disposition": "acquisition-failure", "status": 404,
                     "reacquired_at_head": True, "diagnostic": refusal.format(name)}
                    for name in ("forked", "orphan", "unsearched", "stale")]
            # A 404 `reacquire-head` has not requested yet is not this stage's to seek.
            rows.append({**rows[1], "repository": "example/unrequested", "reacquired_at_head": False})
            (evidence / "candidates.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")

            completed = run("--evidence-root", str(root), "reacquire-namesake",
                            "--cache-dir", str(Path(tmp) / "cache"), env=env)
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertEqual("witness-search-recensus: 4 refused candidate(s) sought in namesake repositories: "
                             "3 acquisition-failure, 1 declares\n", completed.stdout)

            records = {row["candidate"].split(":")[0].split("/")[1]: row
                       for row in INDEX.source_rows(root, "github-code-search")}
            self.assertEqual(5, len(records), records)  # the namesake's read supersedes the pinned refusal
            self.assertEqual(OLDER, records["forked"]["revision"])
            # The stdlib loader refuses its `? ` key, so the full parser reads it as `full-yaml` would.
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2); served by upstream/Forked",
                             records["forked"]["census"])
            self.assertEqual("outstanding", records["forked"]["disposition"])  # its screens are still owed
            self.assertEqual(PINNED, records["orphan"]["revision"])
            self.assertIn(refusal.format("orphan"), records["orphan"]["census"])
            self.assertIn("the repository search for `orphan` names 0 namesake(s) (none) at",
                          records["orphan"]["census"])
            self.assertIn("the repository search for `unsearched` answered HTTP 422 at",
                          records["unsearched"]["census"])
            self.assertIn("upstream/stale's history of the path answered HTTP 500 at", records["stale"]["census"])
            self.assertEqual({"outstanding"}, {records[name]["disposition"]
                                               for name in ("orphan", "unsearched", "stale", "unrequested")})

            ledger = [row for _, row in INDEX.jsonl(evidence / "candidates.jsonl")]
            served = next(row for row in ledger if row.get("served_by"))
            self.assertEqual(f"{url}/upstream/Forked/{OLDER}/openapi.yaml", served["raw_url"])
            self.assertEqual(PINNED, served["supersedes"])
            self.assertEqual(refusal.format("forked"), served["github_refusal"])
            calls = [row for _, row in INDEX.jsonl(evidence / "rate-limit-calls.jsonl") if row.get("host") == "github"]
            rest = [path for path in server.paths if path.startswith(("/repos/", "/search/"))]
            self.assertEqual(len(rest), len(calls))  # every REST call went through the guard
            # four repository searches and the two namesakes' histories of the path
            self.assertEqual((4, 2), (sum(p.startswith("/search/") for p in rest),
                                      sum(p.startswith("/repos/") for p in rest)))

            # A second run leaves what the first sought; `--again` seeks only what is still refused.
            second = run("--evidence-root", str(root), "reacquire-namesake",
                         "--cache-dir", str(Path(tmp) / "cache"), env=env)
            self.assertIn("0 refused candidate(s) sought", second.stdout)
            again = run("--evidence-root", str(root), "reacquire-namesake", "--again",
                        "--cache-dir", str(Path(tmp) / "cache"), env=env)
            self.assertIn("3 refused candidate(s) sought in namesake repositories: 3 acquisition-failure",
                          again.stdout)


if __name__ == "__main__":
    unittest.main()

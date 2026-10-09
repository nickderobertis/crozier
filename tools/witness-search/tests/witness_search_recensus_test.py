#!/usr/bin/env python3
"""`tools/witness-search/witness-search-recensus.py`, driven through its real CLI.

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

Without SIGALRM (as on Windows), each stage reads through spawned readers, one
killed mid-reading failing the stage.

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
from typing import Any

# Every child these tests start has its output decoded as UTF-8, so a Python
# child writes UTF-8 too, whatever the platform locale (cp1252 on Windows).
os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "witness-search" / "witness-search-recensus.py"
KEY = "property-sole-anyof-composed-member"
SELECTOR = "schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf"

# The census's stdlib loader refuses the YAML tag; YAML 1.2 reads it.
DECLARER = b"""openapi: 3.0.3
info:
  title: !!str Pets
  version: '1'
paths:
  /pets:
    get:
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


INDEX = _load("witness_search_github_index", REPO / "tools" / "witness-search" / "witness-search-github-index.py")


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


OTHER = "oneof-anyof-variant"


def keys_file(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "keys.json").write_text(
        json.dumps(
            {
                "keys": {
                    KEY: {"region": "schemas", "selector": SELECTOR, "selector_status": "available"},
                    OTHER: {
                        "region": "schemas",
                        "selector": "schema.oneOf>schema.anyOf",
                        "selector_status": "available",
                    },
                }
            }
        ),
        encoding="utf-8",
        newline="\n",
    )


def run(*args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        env={**os.environ, **(env or {})},
        timeout=300,
        encoding="utf-8",
    )


# A startup hook for one run: once a reader enters the census walk, the alarm
# `read_document` armed is raised early, after RECENSUS_TEST_WALK_LINES lines of the
# census's code have run, so its bound is reached by a known amount of walk work,
# however slow the runner is. Lines, not calls: much of the walk is loops.
WALK_ALARM = """\
import os, signal, sys
_after = int(os.environ["RECENSUS_TEST_WALK_LINES"])
_lines = None
def _line(frame, event, arg):
    global _lines
    if event == "line" and _lines is not None and _lines < _after:
        _lines += 1
        if _lines == _after:
            # The bound must be armed: the alarm is raised early, never set here.
            if signal.alarm(0) == 0:
                os.write(2, b"WALK_ALARM: the reader armed no census bound\\n")
                os._exit(5)
            signal.raise_signal(signal.SIGALRM)
    return _line
def _call(frame, event, arg):
    global _lines
    if not frame.f_code.co_filename.endswith("openapi-surface-census.py"):
        return None
    if _lines is None and frame.f_code.co_name == "census_document":
        _lines = 0
    return _line if _lines is not None and _lines < _after else None
sys.settrace(_call)
"""


def walk_alarm(tmp: str, lines: int) -> dict[str, str]:
    """The environment that runs the script with `WALK_ALARM` raising its alarm at `lines` lines."""
    startup = Path(tmp) / "walk-alarm"
    startup.mkdir(exist_ok=True)
    (startup / "sitecustomize.py").write_text(WALK_ALARM, encoding="utf-8")
    return {
        "RECENSUS_TEST_WALK_LINES": str(lines),
        "PYTHONPATH": os.pathsep.join(filter(None, (str(startup), os.environ.get("PYTHONPATH")))),
    }


class OpaqueContinuationTest(unittest.TestCase):
    def test_each_continuation_skips_opaque_history_and_refuses_unknown_versions(self) -> None:
        server = UpstreamServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        env = {
            "CROZIER_GITHUB_API_URL": url,
            "CROZIER_SOURCEGRAPH_URL": url,
            "CROZIER_RAW_GITHUB_URL": url,
            "GITHUB_TOKEN": "offline-test-token",
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            token = "screened-nonpublic-input:v2:" + "a" * 32 + ":731"
            for stage, source, status in (
                ("full-yaml", "sourcegraph", "parse-failure"),
                ("reacquire-head", "github-code-search", "acquisition-failure"),
                ("reacquire-namesake", "github-code-search", "acquisition-failure"),
            ):
                with self.subTest(stage=stage):
                    evidence = root / f"witness-search-{source}"
                    keys_file(evidence)
                    ledger = evidence / "candidates.jsonl"
                    historical = {
                        "source": source,
                        "key": KEY,
                        "selector": SELECTOR,
                        "repository": "fern-api/fern",
                        "path": token,
                        "sha256": token,
                        "blob": token,
                        "commit": token,
                        "disposition": status,
                        "status": 404,
                        "reacquired_at_head": stage == "reacquire-namesake",
                        "diagnostic": "HTTP 404",
                    }
                    prior = token.rsplit(":", 1)[0] + ":730"
                    earlier = {**historical, "path": token, "sha256": prior, "blob": prior, "commit": prior}
                    historical["supersedes"] = prior
                    repeated = {k: v for k, v in historical.items() if k != "supersedes"}
                    original = "".join(json.dumps(row) + "\n" for row in (earlier, historical, repeated))
                    ledger.write_text(original, encoding="utf-8", newline="\n")
                    cache = Path(tmp) / stage
                    options = (
                        ("--source", source, "--cache", str(cache))
                        if stage == "full-yaml"
                        else ("--cache-dir", str(cache), "--again")
                    )
                    completed = run("--evidence-root", str(root), stage, *options, env=env)
                    self.assertEqual(0, completed.returncode, completed.stderr)
                    self.assertIn("1 opaque v2 record(s) screened by repository rule", completed.stdout)
                    self.assertEqual(1, len(completed.stdout.splitlines()))
                    self.assertEqual(original, ledger.read_text(encoding="utf-8"))
                    self.assertFalse((cache / "documents").exists())
                    self.assertFalse((evidence / "raw-github-calls.jsonl").exists())
                    self.assertEqual([], server.paths)
                    ledger.write_text(original.replace(":v2:", ":v3:"), encoding="utf-8", newline="\n")
                    rejected = run("--evidence-root", str(root), stage, *options, env=env)
                    self.assertEqual(1, rejected.returncode)
                    self.assertIn("unsupported opaque identity version v3", rejected.stderr)
                    ledger.write_text(original, encoding="utf-8", newline="\n")
                    recovered = run("--evidence-root", str(root), stage, *options, env=env)
                    self.assertEqual(0, recovered.returncode, recovered.stderr)
                    self.assertEqual(original, ledger.read_text(encoding="utf-8"))


class FullYamlTest(unittest.TestCase):
    def test_each_parse_failure_is_read_again_and_recorded_with_its_reading(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            rows = []
            for name, data in (
                ("declarer", DECLARER),
                ("duplicate", DUPLICATE),
                ("template", TEMPLATE),
                ("chart", NOT_OPENAPI),
                ("legacy", SWAGGER),
            ):
                digest = hashlib.sha256(data).hexdigest()
                (cache / "documents" / f"{digest}.yaml").write_bytes(data)
                rows.append(
                    {
                        "source": "sourcegraph",
                        "key": KEY,
                        "selector": SELECTOR,
                        "repository": f"github.com/example/{name}",
                        "path": "openapi.yaml",
                        "commit": "c" * 40,
                        "sha256": digest,
                        "document": f"{digest}.yaml",
                        "disposition": "parse-failure",
                        "diagnostic": "the stdlib loader refused it",
                    }
                )
            other = {**rows[0], "key": OTHER, "selector": "schema.oneOf>schema.anyOf"}
            (evidence / "candidates.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in [*rows, other]), encoding="utf-8", newline="\n"
            )

            completed = run(
                "--evidence-root",
                str(root),
                "full-yaml",
                "--source",
                "sourcegraph",
                "--cache",
                str(cache),
                "--jobs",
                "2",
                "--key",
                KEY,
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("5 parse-failure row(s) over 5 document(s) read again", completed.stdout)

            appended = {
                row["repository"].rsplit("/", 1)[1]: row
                for _, row in INDEX.jsonl(evidence / "candidates.jsonl")
                if row.get("loader")
            }
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

            records = {
                row["candidate"].split("/", 1)[1].split(":")[0]: row for row in INDEX.source_rows(root, "sourcegraph")
            }
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["declarer"]["census"])
            self.assertEqual("outstanding", records["declarer"]["disposition"])  # its screens are owed
            self.assertTrue(records["duplicate"]["census"].startswith("census 0; read by ruamel.yaml"))
            self.assertEqual("rejected", records["duplicate"]["disposition"])
            self.assertTrue(records["template"]["census"].startswith("census-refused: ruamel.yaml 0.19.1"))
            self.assertEqual("rejected", records["template"]["disposition"])
            self.assertEqual("rejected", records["chart"]["disposition"])
            self.assertEqual("rejected", records["legacy"]["disposition"])

            # The key filter left the other key's row to a later run, which reads it and no more.
            self.assertEqual(
                "outstanding",
                next(r for r in INDEX.source_rows(root, "sourcegraph") if r["key"] == OTHER)["disposition"],
            )
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
                rows.append(
                    {
                        "source": "github-publisher-trees",
                        "repository": "example/publisher",
                        "path": f"{name}.yaml",
                        "commit": "c" * 40,
                        "blob": git_blob(data),
                        "sha256": digest,
                        "status": "parse-failure",
                        "diagnostic": "the stdlib loader refused it",
                    }
                )
            (evidence / "documents.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8", newline="\n"
            )

            completed = run(
                "--evidence-root",
                str(root),
                "full-yaml",
                "--source",
                "github-publisher-trees",
                "--cache",
                str(cache),
                "--key",
                OTHER,
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn(
                "github-publisher-trees: 3 parse-failure row(s) over 3 document(s) read again: "
                "1 census-refused, 1 excluded-non-openapi-3, 1 readable",
                completed.stdout,
            )

            appended = {
                row["path"].split(".")[0]: row
                for _, row in INDEX.jsonl(evidence / "documents.jsonl")
                if row.get("loader")
            }
            self.assertEqual({"declarer", "template", "chart"}, set(appended))
            self.assertTrue(all("disposition" not in row for row in appended.values()))
            self.assertEqual("readable", appended["declarer"]["status"])
            self.assertEqual({KEY: 1, OTHER: 0}, appended["declarer"]["selector_counts"])
            self.assertEqual("census-refused", appended["template"]["status"])
            self.assertIn(f"sha256 {rows[1]['sha256']}", appended["template"]["diagnostic"])
            self.assertEqual("excluded-non-openapi-3", appended["chart"]["status"])
            self.assertNotIn("selector_count", appended["chart"])

            records = {
                (row["key"], row["candidate"].split(":")[1].split(".")[0]): row
                for row in INDEX.source_rows(root, "github-publisher-trees")
            }
            self.assertEqual(6, len(records), records)  # the re-reading supersedes each parse failure
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records[(KEY, "declarer")]["census"])
            self.assertEqual("census 0; read by ruamel.yaml 0.19.1 (YAML 1.2)", records[(OTHER, "declarer")]["census"])
            self.assertTrue(records[(KEY, "template")]["census"].startswith("census-refused: ruamel.yaml 0.19.1"))
            self.assertEqual("rejected", records[(OTHER, "chart")]["disposition"])

            again = run(
                "--evidence-root", str(root), "full-yaml", "--source", "github-publisher-trees", "--cache", str(cache)
            )
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
            first = {
                "source": "github-publisher-trees",
                "repository": "example/publisher",
                "path": "declarer.yaml",
                "commit": "c" * 40,
                "blob": git_blob(DECLARER),
                "sha256": digest,
                "status": "parse-failure",
                "diagnostic": "the stdlib loader refused it",
            }
            read = {
                **{k: v for k, v in first.items() if k != "diagnostic"},
                "status": "readable",
                "loader": "ruamel.yaml 0.19.1 (YAML 1.2)",
                "recensus_of": "parse-failure",
                "selector_counts": {KEY: 1},
            }
            (evidence / "documents.jsonl").write_text(
                json.dumps(first) + "\n" + json.dumps(read) + "\n", encoding="utf-8", newline="\n"
            )
            owed = {row["key"]: row for row in INDEX.source_rows(root, "github-publisher-trees")}
            self.assertEqual("outstanding", owed[OTHER]["disposition"])
            self.assertIn("never counted this key", owed[OTHER]["census"])

            completed = run(
                "--evidence-root",
                str(root),
                "full-yaml",
                "--source",
                "github-publisher-trees",
                "--cache",
                str(cache),
                "--key",
                OTHER,
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn(
                "github-publisher-trees: 0 parse-failure row(s) and 1 full-parser reading(s) "
                "missing a key's count over 1 document(s) read again: 1 readable",
                completed.stdout,
            )
            appended = [row for _, row in INDEX.jsonl(evidence / "documents.jsonl")][-1]
            self.assertEqual({KEY: 1, OTHER: 0}, appended["selector_counts"])
            self.assertEqual("parse-failure", appended["recensus_of"])

            records = {row["key"]: row for row in INDEX.source_rows(root, "github-publisher-trees")}
            self.assertEqual("census 0; read by ruamel.yaml 0.19.1 (YAML 1.2)", records[OTHER]["census"])
            self.assertEqual("rejected", records[OTHER]["disposition"])
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records[KEY]["census"])

            again = run(
                "--evidence-root", str(root), "full-yaml", "--source", "github-publisher-trees", "--cache", str(cache)
            )
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
            row = {
                "source": "sourcegraph",
                "key": KEY,
                "repository": "github.com/example/huge",
                "path": "a.yaml",
                "commit": "c" * 40,
                "sha256": digest,
                "disposition": "parse-failure",
            }
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
            completed = run(
                "--evidence-root",
                str(root),
                "full-yaml",
                "--source",
                "sourcegraph",
                "--cache",
                str(cache),
                "--timeout",
                "1",
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            refused = [r for _, r in INDEX.jsonl(evidence / "candidates.jsonl") if r.get("loader")]
            self.assertEqual("census-refused", refused[0]["disposition"])
            self.assertIn("parse exceeded 1 s", refused[0]["diagnostic"])
            self.assertIn(f"sha256 {digest}", refused[0]["diagnostic"])

    def test_a_census_walk_past_its_bound_or_its_depth_is_refused(self) -> None:
        # Aliases cost the parser nothing and the walk everything: eleven levels of eight
        # shared `allOf` members is 8^11 schemas to walk, and a 1,500-link chain kept under an
        # `x-` extension is one schema 1,500 levels deep. Both are read at a bound no runner
        # reaches. The bomb's bound is reached by work instead: `WALK_ALARM` raises the alarm
        # the stage set after a fixed number of the walk's lines, so it lands inside the walk
        # however slow the runner is; the chain's depth alone refuses it.
        bomb = [
            "openapi: 3.0.3",
            "info: {title: t, version: '1'}",
            "paths: {}",
            "components:",
            "  schemas:",
            "    L0: &l0 {type: object, properties: {a: {type: string}}}",
        ]
        bomb += [f"    L{n}: &l{n} {{allOf: [{', '.join([f'*l{n - 1}'] * 8)}]}}" for n in range(1, 12)]
        chain = ["openapi: 3.0.3", "info: {title: t, version: '1'}", "paths: {}", "x-chain:", "  - &l0 {type: string}"]
        chain += [f"  - &l{n} {{type: array, items: *l{n - 1}}}" for n in range(1, 1500)]
        chain += ["components:", "  schemas:", "    Deep: *l1499"]
        with tempfile.TemporaryDirectory() as tmp:
            refused = {}
            for name, text, env in (("bomb", bomb, walk_alarm(tmp, 100_000)), ("chain", chain, None)):
                root = Path(tmp) / name / "evidence"
                evidence = root / "witness-search-sourcegraph"
                keys_file(evidence)
                cache = Path(tmp) / name / "cache"
                (cache / "documents").mkdir(parents=True)
                data = ("\n".join(text) + "\n").encode("utf-8")
                digest = hashlib.sha256(data).hexdigest()
                (cache / "documents" / f"{digest}.yaml").write_bytes(data)
                row = {
                    "source": "sourcegraph",
                    "key": KEY,
                    "repository": f"github.com/example/{name}",
                    "path": "a.yaml",
                    "commit": "c" * 40,
                    "sha256": digest,
                    "disposition": "parse-failure",
                }
                (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
                try:
                    completed = run(
                        "--evidence-root",
                        str(root),
                        "full-yaml",
                        "--source",
                        "sourcegraph",
                        "--cache",
                        str(cache),
                        "--timeout",
                        "600",
                        env=env,
                    )
                except subprocess.TimeoutExpired:
                    self.fail(f"the census walk over the {name} was not ended by its bound or its depth")
                self.assertEqual(0, completed.returncode, completed.stderr)
                [refused[name]] = [r for _, r in INDEX.jsonl(evidence / "candidates.jsonl") if r.get("loader")]
                self.assertEqual("census-refused", refused[name]["disposition"], refused[name])
                self.assertIn(f"sha256 {digest}", refused[name]["diagnostic"])
            self.assertTrue(
                refused["bomb"]["diagnostic"].startswith(
                    "census walk over the ruamel.yaml 0.19.1 (YAML 1.2) reading exceeded 600 s; sha256 "
                ),
                refused["bomb"]["diagnostic"],
            )
            self.assertTrue(
                refused["chain"]["diagnostic"].startswith(
                    "census walk over the ruamel.yaml 0.19.1 (YAML 1.2) reading: RecursionError: "
                ),
                refused["chain"]["diagnostic"],
            )

    def test_an_absent_copy_and_a_bad_bound_name_their_repair(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            row = {
                "source": "sourcegraph",
                "key": KEY,
                "repository": "github.com/example/api",
                "path": "a.yaml",
                "commit": "c" * 40,
                "sha256": "a" * 64,
                "disposition": "parse-failure",
            }
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
            missing = run(
                "--evidence-root",
                str(root),
                "full-yaml",
                "--source",
                "sourcegraph",
                "--cache",
                str(Path(tmp) / "empty"),
            )
            self.assertEqual(1, missing.returncode)
            self.assertIn(f"no cached copy of sha256 {'a' * 64}", missing.stderr)
            self.assertIn(
                f"and it cannot be reacquired: the ledger row for github.com/example/api/a.yaml@{'c' * 40} "
                "records no acquisition route to reacquire its document by",
                missing.stderr,
            )
            self.assertIn("pass the cache it was acquired into with --cache", missing.stderr)
            bound = run(
                "--evidence-root",
                str(root),
                "full-yaml",
                "--source",
                "sourcegraph",
                "--cache",
                str(Path(tmp) / "empty"),
                "--jobs",
                "0",
            )
            self.assertEqual(2, bound.returncode)
            self.assertIn("--jobs and --timeout must be positive", bound.stderr)

    def test_a_copy_no_cache_holds_is_reacquired_at_its_commit_and_refused_if_it_differs(self) -> None:
        """A parse failure whose bytes no cache holds is read from its recorded source, verified first."""
        server = UpstreamServer(("127.0.0.1", 0), Upstream)
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
            row = {
                "source": "sourcegraph",
                "key": KEY,
                "selector": SELECTOR,
                "repository": "github.com/example/mirrored",
                "path": "openapi.yaml",
                "commit": PINNED,
                "acquisition_route": "sourcegraph-paced",
                "sha256": digest,
                "document": f"{digest}.yaml",
                "disposition": "parse-failure",
                "diagnostic": "the stdlib loader refused it",
            }
            ledger = evidence / "candidates.jsonl"
            ledger.write_text(
                json.dumps({**row, "repository": "github.com/example/tampered"}) + "\n", encoding="utf-8", newline="\n"
            )
            refused = run(
                "--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache), env=env
            )
            self.assertEqual(1, refused.returncode)
            self.assertIn(
                f"refused: github.com/example/tampered/openapi.yaml@{PINNED} served sha256 "
                f"{hashlib.sha256(DUPLICATE).hexdigest()}, not the {digest} the ledger pins",
                refused.stderr,
            )
            self.assertEqual(1, len(ledger.read_text(encoding="utf-8").splitlines()))
            self.assertEqual([], list((cache / "documents").glob("*")) if (cache / "documents").is_dir() else [])

            ledger.write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
            completed = run(
                "--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache), env=env
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("1 parse-failure row(s) over 1 document(s) read again: 1 declares", completed.stdout)
            self.assertEqual(
                [
                    f"/github.com/example/tampered/-/raw/openapi.yaml?rev={PINNED}",
                    f"/github.com/example/mirrored/-/raw/openapi.yaml?rev={PINNED}",
                ],
                server.paths,
            )
            self.assertEqual(DECLARER, (cache / "documents" / f"{digest}.yaml").read_bytes())

            # A source that no longer serves the document leaves it unread, naming the repair.
            gone = {**row, "repository": "github.com/example/gone", "sha256": "b" * 64, "document": f"{'b' * 64}.yaml"}
            ledger.write_text(json.dumps(gone) + "\n", encoding="utf-8", newline="\n")
            unserved = run(
                "--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache), env=env
            )
            self.assertEqual(1, unserved.returncode)
            self.assertIn(f"no cached copy of sha256 {'b' * 64}", unserved.stderr)
            self.assertIn(
                "its recorded source no longer serves it; pass the cache it was acquired into with --cache",
                unserved.stderr,
            )

            # With no --cache the reacquired copy lands in the gitignored default cache.
            default = REPO / ".local" / "witness-search-cache" / "documents" / f"{digest}.yaml"
            if not default.exists():
                self.addCleanup(default.unlink, missing_ok=True)
            ledger.write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
            defaulted = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", env=env)
            self.assertEqual(0, defaulted.returncode, defaulted.stderr)
            self.assertEqual(DECLARER, default.read_bytes())
            self.assertEqual(0, subprocess.run(["git", "check-ignore", "--quiet", str(default)], cwd=REPO).returncode)

    def test_a_copy_read_from_the_mirror_is_reacquired_from_the_mirror(self) -> None:
        """A GitHub row the mirror served is read from the mirror again, under its host, verified first."""
        server = UpstreamServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        env = {
            "CROZIER_GITHUB_API_URL": url,
            "CROZIER_RAW_GITHUB_URL": url,
            "CROZIER_SOURCEGRAPH_URL": url,
            "GITHUB_TOKEN": "offline-test-token",
        }
        digest = hashlib.sha256(DECLARER).hexdigest()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-code-search"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            row = {
                "source": "github-code-search",
                "key": KEY,
                "selector": SELECTOR,
                "repository": "example/mirrored",
                "path": "openapi.yaml",
                "commit": PINNED,
                "blob": git_blob(DECLARER),
                "acquisition_route": "sourcegraph-mirror",
                "sha256": digest,
                "document": f"{digest}.yaml",
                "disposition": "parse-failure",
                "diagnostic": "the stdlib loader refused it",
            }
            ledger = evidence / "candidates.jsonl"
            ledger.write_text(
                json.dumps({**row, "repository": "example/tampered"}) + "\n", encoding="utf-8", newline="\n"
            )
            refused = run(
                "--evidence-root",
                str(root),
                "full-yaml",
                "--source",
                "github-code-search",
                "--cache",
                str(cache),
                env=env,
            )
            self.assertEqual(1, refused.returncode)
            self.assertIn(
                f"refused: example/tampered/openapi.yaml@{PINNED} served sha256 "
                f"{hashlib.sha256(DUPLICATE).hexdigest()}, not the {digest} the ledger pins",
                refused.stderr,
            )
            self.assertFalse((cache / "documents").is_dir() and any((cache / "documents").iterdir()))

            ledger.write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
            completed = run(
                "--evidence-root",
                str(root),
                "full-yaml",
                "--source",
                "github-code-search",
                "--cache",
                str(cache),
                env=env,
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("1 parse-failure row(s) over 1 document(s) read again: 1 declares", completed.stdout)
            self.assertEqual(
                [
                    f"/github.com/example/tampered/-/raw/openapi.yaml?rev={PINNED}",
                    f"/github.com/example/mirrored/-/raw/openapi.yaml?rev={PINNED}",
                ],
                server.paths,
            )
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
            row = {
                "source": "sourcegraph",
                "key": KEY,
                "repository": "github.com/example/api",
                "path": "a.yaml",
                "commit": "c" * 40,
                "sha256": digest,
                "disposition": "parse-failure",
            }
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache))
            self.assertEqual(1, completed.returncode)
            self.assertIn("does not hash to the pinned sha256", completed.stderr)
            self.assertIn("re-acquire it at its commit", completed.stderr)


HEAD = "d" * 40
PINNED = "e" * 40
OLDER = "f" * 40


class UpstreamServer(ThreadingHTTPServer):
    paths: list[str]


class Upstream(BaseHTTPRequestHandler):
    server: UpstreamServer

    def log_message(self, format: str, *args: Any) -> None:
        pass

    def reply(self, status: int, body: bytes | dict | list) -> None:
        data = body if isinstance(body, bytes) else json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        self.server.paths.append(self.path)
        reset = int(time.time()) + 60
        if self.path == "/rate_limit":
            self.reply(
                200,
                {
                    "resources": {
                        "core": {"limit": 5000, "used": 0, "remaining": 5000, "reset": reset},
                        "search": {"limit": 30, "used": 0, "remaining": 30, "reset": reset},
                    }
                },
            )
        # Answers whose fields are not what they must be before joining a URL.
        elif self.path == "/repos/example/branchless":
            self.reply(200, {"default_branch": 7})
        elif self.path in ("/repos/example/shorthead", "/repos/example/tainted", "/repos/example/untold"):
            self.reply(200, {"default_branch": "main"})
        elif self.path == "/repos/example/shorthead/commits/main":
            self.reply(200, {"sha": "abc123"})
        elif self.path in ("/repos/example/tainted/commits/main", "/repos/example/untold/commits/main"):
            self.reply(200, {"sha": HEAD})
        elif self.path == f"/repos/example/tainted/commits?path=openapi.yaml&sha={HEAD}&per_page=100":
            self.reply(
                200, [{"sha": "../../../evil"}, {"sha": OLDER.upper()}, {"sha": OLDER[:12]}, {"sha": 7}, {"sha": OLDER}]
            )
        elif self.path == f"/repos/example/untold/commits?path=openapi.yaml&sha={HEAD}&per_page=100":
            self.reply(200, [{"sha": "../../../evil"}, {"sha": OLDER[:12]}])
        elif self.path == f"/example/tainted/{OLDER}/openapi.yaml":
            self.reply(200, DECLARER)
        elif self.path == "/search/repositories?q=malformed%20in%3Aname&per_page=100":
            self.reply(
                200,
                {
                    "items": [
                        {"full_name": "malformed"},
                        {"full_name": "up stream/malformed"},
                        {"full_name": "upstream/malformed/extra"},
                        {"full_name": "upstream/malformed"},
                    ]
                },
            )
        elif self.path == "/repos/upstream/malformed/commits?path=openapi.yaml&per_page=100":
            self.reply(200, [{"sha": "../../../evil"}, {"sha": OLDER[:12]}, {"sha": OLDER}])
        elif self.path == f"/upstream/malformed/{OLDER}/openapi.yaml":
            self.reply(200, DECLARER)
        elif self.path == "/search/repositories?q=forked%20in%3Aname&per_page=100":
            # The candidate itself, a parent and an unrelated partial match: only the parent is a namesake.
            self.reply(
                200,
                {
                    "items": [
                        {"full_name": "example/forked"},
                        {"full_name": "upstream/Forked"},
                        {"full_name": "other/forked-too"},
                    ]
                },
            )
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
        elif self.path in (
            "/repos/example/moved",
            "/repos/example/dropped",
            "/repos/example/headless",
            "/repos/example/unlisted",
        ):
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
        server = UpstreamServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-code-search"
            keys_file(evidence)
            rows = [
                {
                    "source": "github-code-search",
                    "key": KEY,
                    "selector": SELECTOR,
                    "repository": f"example/{name}",
                    "path": "openapi.yaml",
                    "commit": PINNED,
                    "blob": git_blob(DECLARER),
                    "disposition": "acquisition-failure",
                    "status": 404,
                    "diagnostic": "404: Not Found",
                }
                for name in ("kept", "mirrored", "gone", "moved", "dropped", "headless", "unlisted")
            ]
            (evidence / "candidates.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8", newline="\n"
            )

            completed = run(
                "--evidence-root",
                str(root),
                "reacquire-head",
                "--cache-dir",
                str(Path(tmp) / "cache"),
                env={
                    "CROZIER_GITHUB_API_URL": url,
                    "CROZIER_RAW_GITHUB_URL": url,
                    "CROZIER_SOURCEGRAPH_URL": url,
                    "GITHUB_TOKEN": "offline-test-token",
                },
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("7 404 candidate(s) requested at head: 4 acquisition-failure, 3 declares", completed.stdout)

            records = {
                row["candidate"].split(":")[0].split("/")[1]: row
                for row in INDEX.source_rows(root, "github-code-search")
            }
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
            self.assertIn(
                f"the path's history at {HEAD} lists 0 commit(s), none serving blob", records["dropped"]["census"]
            )
            self.assertIn(f"Sourcegraph's mirror at {PINNED} served HTTP 404 at", records["dropped"]["census"])
            # A head commit GitHub will not name, and a history GitHub will not list.
            self.assertIn(
                "GET /repos/example/headless/commits/main answered HTTP 404 at", records["headless"]["census"]
            )
            self.assertIn(f"the path's history at {HEAD} answered HTTP 500 at", records["unlisted"]["census"])
            self.assertEqual({"outstanding"}, {records[name]["disposition"] for name in ("headless", "unlisted")})

            ledger = {row["repository"].split("/")[1]: row for _, row in INDEX.jsonl(evidence / "candidates.jsonl")}
            self.assertEqual("sourcegraph-mirror", ledger["mirrored"]["acquisition_route"])
            guarded = [
                row for _, row in INDEX.jsonl(evidence / "rate-limit-calls.jsonl") if row.get("bucket") == "core"
            ]
            rest = [path for path in server.paths if path.startswith("/repos/")]
            self.assertEqual(len(rest), len(guarded))
            # seven repositories, five head commits asked for, and three histories of the path
            self.assertEqual(15, len(rest))
            sourcegraph = [
                row for _, row in INDEX.jsonl(evidence / "rate-limit-calls.jsonl") if row.get("host") == "sourcegraph"
            ]
            self.assertEqual(5, len(sourcegraph))

            # A second run leaves what the first decided; `--again` requests only what is still refused.
            env = {
                "CROZIER_GITHUB_API_URL": url,
                "CROZIER_RAW_GITHUB_URL": url,
                "CROZIER_SOURCEGRAPH_URL": url,
                "GITHUB_TOKEN": "offline-test-token",
            }
            second = run(
                "--evidence-root", str(root), "reacquire-head", "--cache-dir", str(Path(tmp) / "cache"), env=env
            )
            self.assertIn("0 404 candidate(s) requested at head", second.stdout)
            again = run(
                "--evidence-root",
                str(root),
                "reacquire-head",
                "--again",
                "--cache-dir",
                str(Path(tmp) / "cache"),
                env=env,
            )
            self.assertEqual(0, again.returncode, again.stderr)
            self.assertIn("4 404 candidate(s) requested at head: 4 acquisition-failure", again.stdout)
            self.assertEqual(7, len(INDEX.source_rows(root, "github-code-search")))

            misspelt = run(
                "--evidence-root",
                str(root),
                "reacquire-head",
                "--key",
                "no-such-key",
                "--cache-dir",
                str(Path(tmp) / "cache"),
            )
            self.assertEqual(2, misspelt.returncode)
            self.assertIn(
                "--key ['no-such-key'] names no key of witness-search-github-code-search/keys.json", misspelt.stderr
            )

            invalid = run(
                "--evidence-root",
                str(root),
                "reacquire-head",
                "--again",
                "--cache-dir",
                str(Path(tmp) / "cache"),
                env={"CROZIER_GITHUB_API_URL": url, "CROZIER_SOURCEGRAPH_URL": "file:///etc/passwd"},
            )
            self.assertEqual(1, invalid.returncode)
            self.assertIn("CROZIER_SOURCEGRAPH_URL must use https://sourcegraph.com", invalid.stderr)


class MirrorHashTest(unittest.TestCase):
    def test_a_mirror_blob_of_another_hash_is_not_the_candidate(self) -> None:
        server = UpstreamServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-code-search"
            keys_file(evidence)
            row = {
                "source": "github-code-search",
                "key": KEY,
                "selector": SELECTOR,
                "repository": "example/tampered",
                "path": "openapi.yaml",
                "commit": PINNED,
                "blob": git_blob(DECLARER),
                "disposition": "acquisition-failure",
                "status": 404,
                "diagnostic": "404: Not Found",
            }
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
            completed = run(
                "--evidence-root",
                str(root),
                "reacquire-head",
                "--cache-dir",
                str(Path(tmp) / "cache"),
                env={
                    "CROZIER_GITHUB_API_URL": url,
                    "CROZIER_RAW_GITHUB_URL": url,
                    "CROZIER_SOURCEGRAPH_URL": url,
                    "GITHUB_TOKEN": "offline-test-token",
                },
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            (record,) = INDEX.source_rows(root, "github-code-search")
            self.assertEqual((PINNED, "outstanding"), (record["revision"], record["disposition"]))
            self.assertIn(
                f"Sourcegraph's mirror at {PINNED} served a blob hashing to {git_blob(DUPLICATE)}, "
                f"not {git_blob(DECLARER)} at",
                record["census"],
            )


class ReacquireNamesakeTest(unittest.TestCase):
    def test_each_refused_candidate_is_sought_in_its_namesakes(self) -> None:
        server = UpstreamServer(("127.0.0.1", 0), Upstream)
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
            rows = [
                {
                    "source": "github-code-search",
                    "key": KEY,
                    "selector": SELECTOR,
                    "repository": f"example/{name}",
                    "path": "openapi.yaml",
                    "commit": PINNED,
                    "blob": git_blob(DECLARER),
                    "disposition": "acquisition-failure",
                    "status": 404,
                    "reacquired_at_head": True,
                    "diagnostic": refusal.format(name),
                }
                for name in ("forked", "orphan", "unsearched", "stale")
            ]
            # A 404 `reacquire-head` has not requested yet is not this stage's to seek.
            rows.append({**rows[1], "repository": "example/unrequested", "reacquired_at_head": False})
            (evidence / "candidates.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8", newline="\n"
            )

            completed = run(
                "--evidence-root", str(root), "reacquire-namesake", "--cache-dir", str(Path(tmp) / "cache"), env=env
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertEqual(
                "witness-search-recensus: 4 refused candidate(s) sought in namesake repositories: "
                "3 acquisition-failure, 1 declares\n",
                completed.stdout,
            )

            records = {
                row["candidate"].split(":")[0].split("/")[1]: row
                for row in INDEX.source_rows(root, "github-code-search")
            }
            self.assertEqual(5, len(records), records)  # the namesake's read supersedes the pinned refusal
            self.assertEqual(OLDER, records["forked"]["revision"])
            # The stdlib loader refuses its YAML tag, so the full parser reads it as `full-yaml` would.
            self.assertEqual(
                "census 1; read by ruamel.yaml 0.19.1 (YAML 1.2); served by upstream/Forked",
                records["forked"]["census"],
            )
            self.assertEqual("outstanding", records["forked"]["disposition"])  # its screens are still owed
            self.assertEqual(PINNED, records["orphan"]["revision"])
            self.assertIn(refusal.format("orphan"), records["orphan"]["census"])
            self.assertIn(
                "the repository search for `orphan` names 0 namesake(s) (none) at", records["orphan"]["census"]
            )
            self.assertIn(
                "the repository search for `unsearched` answered HTTP 422 at", records["unsearched"]["census"]
            )
            self.assertIn("upstream/stale's history of the path answered HTTP 500 at", records["stale"]["census"])
            self.assertEqual(
                {"outstanding"},
                {records[name]["disposition"] for name in ("orphan", "unsearched", "stale", "unrequested")},
            )

            ledger = [row for _, row in INDEX.jsonl(evidence / "candidates.jsonl")]
            served = next(row for row in ledger if row.get("served_by"))
            self.assertEqual(f"{url}/upstream/Forked/{OLDER}/openapi.yaml", served["raw_url"])
            self.assertEqual(PINNED, served["supersedes"])
            self.assertEqual(refusal.format("forked"), served["github_refusal"])
            calls = [row for _, row in INDEX.jsonl(evidence / "rate-limit-calls.jsonl") if row.get("host") == "github"]
            rest = [path for path in server.paths if path.startswith(("/repos/", "/search/"))]
            self.assertEqual(len(rest), len(calls))  # every REST call went through the guard
            # four repository searches and the two namesakes' histories of the path
            self.assertEqual(
                (4, 2), (sum(p.startswith("/search/") for p in rest), sum(p.startswith("/repos/") for p in rest))
            )

            # A second run leaves what the first sought; `--again` seeks only what is still refused.
            second = run(
                "--evidence-root", str(root), "reacquire-namesake", "--cache-dir", str(Path(tmp) / "cache"), env=env
            )
            self.assertIn("0 refused candidate(s) sought", second.stdout)
            again = run(
                "--evidence-root",
                str(root),
                "reacquire-namesake",
                "--again",
                "--cache-dir",
                str(Path(tmp) / "cache"),
                env=env,
            )
            self.assertIn("3 refused candidate(s) sought in namesake repositories: 3 acquisition-failure", again.stdout)


def serve_upstream(test: unittest.TestCase) -> tuple[UpstreamServer, str]:
    server = UpstreamServer(("127.0.0.1", 0), Upstream)
    server.paths = []
    threading.Thread(target=server.serve_forever, daemon=True).start()
    test.addCleanup(server.server_close)
    test.addCleanup(server.shutdown)
    return server, f"http://127.0.0.1:{server.server_port}"


def refused_rows(evidence: Path, names: tuple[str, ...], **extra: object) -> None:
    keys_file(evidence)
    rows = [
        {
            "source": "github-code-search",
            "key": KEY,
            "selector": SELECTOR,
            "repository": f"example/{name}",
            "path": "openapi.yaml",
            "commit": PINNED,
            "blob": git_blob(DECLARER),
            "disposition": "acquisition-failure",
            "status": 404,
            "diagnostic": "404: Not Found",
            **extra,
        }
        for name in names
    ]
    (evidence / "candidates.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")


class MalformedGitHubAnswerTest(unittest.TestCase):
    """A field GitHub answers that is not the type and identity it must be never joins a URL."""

    def test_a_head_or_history_naming_no_full_commit_is_refused_not_requested(self) -> None:
        server, url = serve_upstream(self)
        env = {
            "CROZIER_GITHUB_API_URL": url,
            "CROZIER_RAW_GITHUB_URL": url,
            "CROZIER_SOURCEGRAPH_URL": url,
            "GITHUB_TOKEN": "offline-test-token",
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            refused_rows(root / "witness-search-github-code-search", ("branchless", "shorthead", "tainted", "untold"))
            completed = run(
                "--evidence-root", str(root), "reacquire-head", "--cache-dir", str(Path(tmp) / "cache"), env=env
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("4 404 candidate(s) requested at head: 3 acquisition-failure, 1 declares", completed.stdout)
            records = {
                row["candidate"].split(":")[0].split("/")[1]: row
                for row in INDEX.source_rows(root, "github-code-search")
            }
            self.assertIn(
                "GET /repos/example/branchless answered HTTP 200 without a default branch name at",
                records["branchless"]["census"],
            )
            self.assertIn(
                "GET /repos/example/shorthead/commits/main answered HTTP 200 without a full commit SHA at",
                records["shorthead"]["census"],
            )
            # The history's one full commit is read; the four entries naming none are not.
            self.assertEqual(OLDER, records["tainted"]["revision"])
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["tainted"]["census"])
            self.assertIn(
                f"the path's history at {HEAD} lists 2 commit(s), none serving blob {git_blob(DECLARER)} "
                "(2 naming no full commit SHA, not read), at",
                records["untold"]["census"],
            )
            self.assertEqual(
                {"outstanding"}, {records[name]["disposition"] for name in ("branchless", "shorthead", "untold")}
            )
        requested = [path for path in server.paths if not path.startswith(("/repos/", "/rate_limit", "/github.com/"))]
        self.assertEqual(
            [
                f"/example/tainted/{HEAD}/openapi.yaml",
                f"/example/tainted/{OLDER}/openapi.yaml",
                f"/example/untold/{HEAD}/openapi.yaml",
            ],
            sorted(requested),
        )
        self.assertFalse(
            [
                path
                for path in server.paths
                if "evil" in path or "abc123" in path or OLDER.upper() in path or "/branchless/commits" in path
            ]
        )

    def test_a_namesake_or_its_history_that_is_malformed_is_skipped_not_requested(self) -> None:
        server, url = serve_upstream(self)
        env = {"CROZIER_GITHUB_API_URL": url, "CROZIER_RAW_GITHUB_URL": url, "GITHUB_TOKEN": "offline-test-token"}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            refused_rows(root / "witness-search-github-code-search", ("malformed",), reacquired_at_head=True)
            completed = run(
                "--evidence-root", str(root), "reacquire-namesake", "--cache-dir", str(Path(tmp) / "cache"), env=env
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertEqual(
                "witness-search-recensus: 1 refused candidate(s) sought in namesake repositories: 1 declares\n",
                completed.stdout,
            )
            (record,) = INDEX.source_rows(root, "github-code-search")
            self.assertEqual(OLDER, record["revision"])
            self.assertEqual(
                "census 1; read by ruamel.yaml 0.19.1 (YAML 1.2); served by upstream/malformed", record["census"]
            )
        # Only the one owner/name full_name was asked for its history, and only
        # its full commit was read.
        self.assertEqual(
            ["/repos/upstream/malformed/commits?path=openapi.yaml&per_page=100"],
            [path for path in server.paths if path.startswith("/repos/")],
        )
        self.assertEqual(
            [f"/upstream/malformed/{OLDER}/openapi.yaml"],
            [path for path in server.paths if not path.startswith(("/repos/", "/search/", "/rate_limit"))],
        )


# Each duplicate `Pet` keeps one of two readings; only the anyOf-of-allOf one
# declares KEY, so the count says which survived.
PET_PLAIN = "    Pet: {type: object, properties: {owner: {type: string}}}\n"
PET_DECLARING = (
    "    Pet: {type: object, properties: {owner: {anyOf: [{allOf: [{$ref: '#/components/schemas/Base'}]}]}}}\n"
)
DUPLICATE_HEAD = (
    "openapi: 3.0.3\ninfo: {title: t, version: '1'}\npaths: {}\ncomponents:\n  schemas:\n"
    "    Base: {type: object, properties: {id: {type: string}}}\n"
)
# Every construct KEY needs sits under a tag no constructor knows, on a
# mapping, a sequence and a scalar: only the untagged reading of all three counts it.
TAGGED = b"""openapi: 3.0.3
info: {title: !vendor/title Pets, version: '1'}
paths: {}
components:
  schemas:
    Base: {type: object, properties: {id: {type: string}}}
    Pet: !merge-objects
      type: object
      properties:
        owner:
          anyOf: !!python/tuple
            - allOf:
                - $ref: !vendor/ref '#/components/schemas/Base'
"""


class LenientReadingTest(unittest.TestCase):
    """What the relaxed reading keeps where the strict construction refuses."""

    def full_yaml(self, documents: dict[str, bytes]) -> dict[str, dict]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            rows = []
            for name, data in documents.items():
                digest = hashlib.sha256(data).hexdigest()
                (cache / "documents" / f"{digest}.yaml").write_bytes(data)
                rows.append(
                    {
                        "source": "sourcegraph",
                        "key": KEY,
                        "selector": SELECTOR,
                        "repository": f"github.com/example/{name}",
                        "path": "openapi.yaml",
                        "commit": "c" * 40,
                        "sha256": digest,
                        "disposition": "parse-failure",
                    }
                )
            (evidence / "candidates.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8", newline="\n"
            )
            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache))
            self.assertEqual(0, completed.returncode, completed.stderr)
            return {
                row["repository"].rsplit("/", 1)[1]: row
                for _, row in INDEX.jsonl(evidence / "candidates.jsonl")
                if row.get("loader")
            }

    def test_a_duplicate_key_keeps_its_last_value(self) -> None:
        read = self.full_yaml(
            {
                "last-declares": (DUPLICATE_HEAD + PET_PLAIN + PET_DECLARING).encode(),
                "first-declares": (DUPLICATE_HEAD + PET_DECLARING + PET_PLAIN).encode(),
            }
        )
        self.assertEqual(
            ("declares", 1), (read["last-declares"]["disposition"], read["last-declares"]["selector_count"])
        )
        self.assertEqual(
            ("does-not-declare", 0), (read["first-declares"]["disposition"], read["first-declares"]["selector_count"])
        )
        for row in read.values():
            self.assertEqual(
                "ruamel.yaml 0.19.1 (YAML 1.2), duplicate keys last-wins, unrecognised tags read untagged",
                row["loader"],
            )

    def test_an_unknown_tag_reads_the_untagged_mapping_sequence_or_scalar(self) -> None:
        read = self.full_yaml({"tagged": TAGGED})["tagged"]
        self.assertEqual(("declares", 1), (read["disposition"], read["selector_count"]))
        self.assertIn("unrecognised tags read untagged", read["loader"])


# A startup hook for this run and every child it spawns: it removes
# `signal.SIGALRM`, so a stage takes the branch it takes on Windows, and with
# RECENSUS_TEST_DIE_ON set, a spawned reader opening that document dies there
# without a verdict, as one the host kills would. It closes its pipe a second
# before it exits, so the stage always sees the pipe end before the process can
# be reaped, the order a loaded host only sometimes gives.
WITHOUT_SIGALRM = """\
import multiprocessing, os, signal, sys, time
del signal.SIGALRM
_doomed = os.environ.get("RECENSUS_TEST_DIE_ON")
if _doomed:
    def _die(event, args):
        if event == "open" and _doomed in str(args[0]) and multiprocessing.parent_process() is not None:
            os.closerange(3, os.sysconf("SC_OPEN_MAX") if hasattr(os, "sysconf") else 4096)
            time.sleep(1)
            os._exit(3)
    sys.addaudithook(_die)
"""


def without_sigalrm(tmp: str, **extra: str) -> dict[str, str]:
    """The environment that runs the script with `WITHOUT_SIGALRM` installed."""
    startup = Path(tmp) / "startup"
    startup.mkdir(exist_ok=True)
    (startup / "sitecustomize.py").write_text(WITHOUT_SIGALRM, encoding="utf-8")
    return {
        **os.environ,
        **extra,
        "PYTHONPATH": os.pathsep.join(filter(None, (str(startup), os.environ.get("PYTHONPATH")))),
    }


class SpawnBoundTest(unittest.TestCase):
    """The bound where SIGALRM does not exist, as on Windows: spawned readers ended at it.

    `WITHOUT_SIGALRM` removes `signal.SIGALRM` from this run and from every
    child it spawns, so each stage takes the branch it takes on Windows."""

    def test_parse_and_census_end_at_the_requested_bound_without_sigalrm(self) -> None:
        huge = b"openapi: 3.0.3\nx:\n" + b"".join(b"  k%d: [a, {b: c}]\n" % n for n in range(400_000))
        bomb = [
            "openapi: 3.0.3",
            "info: {title: t, version: '1'}",
            "paths: {}",
            "components:",
            "  schemas:",
            "    L0: &l0 {type: object, properties: {a: {type: string}}}",
        ]
        bomb += [f"    L{n}: &l{n} {{allOf: [{', '.join([f'*l{n - 1}'] * 8)}]}}" for n in range(1, 12)]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            rows = []
            for name, data in (("huge", huge), ("bomb", ("\n".join(bomb) + "\n").encode()), ("declarer", DECLARER)):
                digest = hashlib.sha256(data).hexdigest()
                (cache / "documents" / f"{digest}.yaml").write_bytes(data)
                rows.append(
                    {
                        "source": "sourcegraph",
                        "key": KEY,
                        "repository": f"github.com/example/{name}",
                        "path": "a.yaml",
                        "commit": "c" * 40,
                        "sha256": digest,
                        "disposition": "parse-failure",
                    }
                )
            (evidence / "candidates.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8", newline="\n"
            )
            env = without_sigalrm(tmp)
            probe = subprocess.run(
                [sys.executable, "-c", "import signal; print(hasattr(signal, 'SIGALRM'))"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                env=env,
                timeout=60,
            )
            self.assertEqual("False", probe.stdout.strip(), probe.stderr)
            started = time.monotonic()
            try:
                completed = subprocess.run(
                    [
                        sys.executable,
                        str(SCRIPT),
                        "--evidence-root",
                        str(root),
                        "full-yaml",
                        "--source",
                        "sourcegraph",
                        "--cache",
                        str(cache),
                        "--timeout",
                        "1",
                        "--jobs",
                        "2",
                    ],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    env=env,
                    timeout=120,
                )
            except subprocess.TimeoutExpired:
                self.fail("without SIGALRM the stage did not end its readers at the 1 s bound")
            elapsed = time.monotonic() - started
            self.assertEqual(0, completed.returncode, completed.stderr)
            read = {
                r["repository"].rsplit("/", 1)[1]: r
                for _, r in INDEX.jsonl(evidence / "candidates.jsonl")
                if r.get("loader")
            }
            self.assertEqual("census-refused", read["huge"]["disposition"])
            self.assertTrue(
                read["huge"]["diagnostic"].startswith("ruamel.yaml 0.19.1 (YAML 1.2): parse exceeded 1 s; sha256 "),
                read["huge"]["diagnostic"],
            )
            self.assertEqual("census-refused", read["bomb"]["disposition"])
            self.assertTrue(
                read["bomb"]["diagnostic"].startswith(
                    "census walk over the ruamel.yaml 0.19.1 (YAML 1.2) reading exceeded 1 s; sha256 "
                ),
                read["bomb"]["diagnostic"],
            )
            # A document inside the bound is read and counted on the same branch.
            self.assertEqual(("declares", 1), (read["declarer"]["disposition"], read["declarer"]["selector_count"]))
            self.assertLess(elapsed, 90)

    def test_a_reader_that_dies_without_a_verdict_fails_the_stage_and_records_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            digest = hashlib.sha256(DECLARER).hexdigest()
            (cache / "documents" / f"{digest}.yaml").write_bytes(DECLARER)
            row = {
                "source": "sourcegraph",
                "key": KEY,
                "repository": "github.com/example/doomed",
                "path": "a.yaml",
                "commit": "c" * 40,
                "sha256": digest,
                "disposition": "parse-failure",
            }
            ledger = evidence / "candidates.jsonl"
            ledger.write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
            args = ("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache))
            died = subprocess.run(
                [sys.executable, str(SCRIPT), *args],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=120,
                env=without_sigalrm(tmp, RECENSUS_TEST_DIE_ON=digest),
            )
            self.assertEqual(1, died.returncode, died.stderr)
            self.assertNotIn("Traceback", died.stderr)
            self.assertIn(
                f"witness-search-recensus: the reader of sha256 {digest} exited 3 without a verdict; "
                "inspect the ledger and cache named and rerun",
                died.stderr,
            )
            self.assertEqual(json.dumps(row) + "\n", ledger.read_text(encoding="utf-8"))
            # The rerun the message names reads it.
            rerun = subprocess.run(
                [sys.executable, str(SCRIPT), *args],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=120,
                env=without_sigalrm(tmp),
            )
            self.assertEqual(0, rerun.returncode, rerun.stderr)
            self.assertIn("1 parse-failure row(s) over 1 document(s) read again: 1 declares", rerun.stdout)

    def test_a_document_reacquired_at_head_or_from_a_namesake_is_read_by_a_spawned_reader(self) -> None:
        _server, url = serve_upstream(self)
        with tempfile.TemporaryDirectory() as tmp:
            # The doomed document is the one each stage reacquires, so only a
            # spawned reader of it — never this process — can have read it.
            env = without_sigalrm(
                tmp,
                CROZIER_GITHUB_API_URL=url,
                CROZIER_RAW_GITHUB_URL=url,
                CROZIER_SOURCEGRAPH_URL=url,
                GITHUB_TOKEN="offline-test-token",
            )
            for stage, name, extra, served in (
                ("reacquire-head", "kept", {}, "census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)"),
                (
                    "reacquire-namesake",
                    "forked",
                    {"reacquired_at_head": True},
                    "census 1; read by ruamel.yaml 0.19.1 (YAML 1.2); served by upstream/Forked",
                ),
            ):
                with self.subTest(stage=stage):
                    root = Path(tmp) / stage
                    refused_rows(root / "witness-search-github-code-search", (name,), **extra)
                    completed = subprocess.run(
                        [
                            sys.executable,
                            str(SCRIPT),
                            "--evidence-root",
                            str(root),
                            stage,
                            "--cache-dir",
                            str(Path(tmp) / f"{stage}-cache"),
                        ],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        timeout=120,
                        env=env,
                    )
                    self.assertEqual(0, completed.returncode, completed.stderr)
                    (record,) = INDEX.source_rows(root, "github-code-search")
                    self.assertEqual(served, record["census"])
                    # The same reading, its reader killed, fails the stage rather than record it.
                    refused_rows(root / "witness-search-github-code-search", (name,), **extra)
                    digest = hashlib.sha256(DECLARER).hexdigest()
                    died = subprocess.run(
                        [
                            sys.executable,
                            str(SCRIPT),
                            "--evidence-root",
                            str(root),
                            stage,
                            "--cache-dir",
                            str(Path(tmp) / f"{stage}-cache-again"),
                        ],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        timeout=120,
                        env={**env, "RECENSUS_TEST_DIE_ON": digest},
                    )
                    self.assertEqual(1, died.returncode, died.stderr)
                    self.assertIn("without a verdict; inspect the ledger and cache named and rerun", died.stderr)

    def test_a_lenient_reading_past_the_bound_records_the_strict_refusal_and_the_lenient_timeout(self) -> None:
        # The strict reading refuses the first document's tag at once; only the
        # lenient one reads on, into a second document too large for the bound.
        data = b"--- !unknown {a: 1}\n---\n" + b"".join(b"k%d: [a, {b: c}]\n" % n for n in range(400_000))
        digest = hashlib.sha256(data).hexdigest()
        with tempfile.TemporaryDirectory() as tmp:
            for branch, env in (("alarm", dict(os.environ)), ("spawned reader", without_sigalrm(tmp))):
                with self.subTest(branch):
                    root = Path(tmp) / branch / "evidence"
                    evidence = root / "witness-search-sourcegraph"
                    keys_file(evidence)
                    cache = Path(tmp) / branch / "cache"
                    (cache / "documents").mkdir(parents=True)
                    (cache / "documents" / f"{digest}.yaml").write_bytes(data)
                    (evidence / "candidates.jsonl").write_text(
                        json.dumps(
                            {
                                "source": "sourcegraph",
                                "key": KEY,
                                "repository": "github.com/example/tagged",
                                "path": "a.yaml",
                                "commit": "c" * 40,
                                "sha256": digest,
                                "disposition": "parse-failure",
                            }
                        )
                        + "\n",
                        encoding="utf-8",
                    )
                    completed = subprocess.run(
                        [
                            sys.executable,
                            str(SCRIPT),
                            "--evidence-root",
                            str(root),
                            "full-yaml",
                            "--source",
                            "sourcegraph",
                            "--cache",
                            str(cache),
                            "--timeout",
                            "1",
                        ],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        env=env,
                        timeout=120,
                    )
                    self.assertEqual(0, completed.returncode, completed.stderr)
                    [read] = [r for _, r in INDEX.jsonl(evidence / "candidates.jsonl") if r.get("loader")]
                    self.assertEqual("census-refused", read["disposition"])
                    strict, lenient = read["diagnostic"].split("; ruamel.yaml 0.19.1 (YAML 1.2), duplicate keys", 1)
                    self.assertTrue(strict.startswith("ruamel.yaml 0.19.1 (YAML 1.2): ConstructorError: "), strict)
                    self.assertIn("!unknown", strict)
                    self.assertTrue(
                        lenient.startswith(
                            f" last-wins, unrecognised tags read untagged: parse exceeded 1 s; sha256 {digest}"
                        ),
                        lenient,
                    )


if __name__ == "__main__":
    unittest.main()

"""Boundary coverage for the judged tier's plugin resolution.

The `llmlint` PR check used to resolve its rule plugins over the network at job
time, so a refused fetch failed a required check for reasons that had nothing to
do with the branch. The repair vendors the resolved plugin documents into
`llmlint-plugins/` and records them in `llmlint-plugins/lock.json`
(docs/llmlint-plugins.md says why that mechanism and not another).

These tests hold the repair in place by driving the REAL `llmlint` binary over
this repository's REAL `llmlint.yml` with the plugin origin made unreachable
from the process — a proxy pointed at a closed local port, a cold plugin cache,
and `LLMLINT_PLUGIN_TTL=0` so no cached copy can answer. The repaired config
resolves; the pre-repair spelling (the same config with each plugin restored to
the URL the lock records) does not, which is what keeps these assertions from
being ones that could never fail.

Run: `just test-llmlint-plugins` (part of `just check`). The llmlint-driving
tests skip where the binary is absent, so the offline `check` matrix stays
toolchain-light; CI's `llmlint` job sets `CROZIER_REQUIRE_LLMLINT=1`, which
turns that skip into a failure so the required check can never no-op.
"""

from __future__ import annotations

import fnmatch
import hashlib
import http.server
import json
import sys
import os
import shutil
import socket
import subprocess
import tempfile
import threading
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
LOCK = REPO / "llmlint-plugins" / "lock.json"
CONFIG = REPO / "llmlint.yml"
RECORD = json.loads(LOCK.read_text(encoding="utf-8"))
PLUGINS = RECORD["plugins"]
VENDORED = [plugin for plugin in PLUGINS if not plugin.get("bundled")]


def configured_excludes() -> list[str]:
    """Read the quoted exclude entries from the repository's llmlint config."""
    lines = CONFIG.read_text(encoding="utf-8").splitlines()
    start = lines.index("  exclude:") + 1
    end = next(
        index
        for index in range(start, len(lines))
        if lines[index] and not lines[index].startswith(" ")
    )
    return [
        line.strip().removeprefix("- ").strip('"')
        for line in lines[start:end]
        if line.strip().startswith('- "')
    ]


class GeneratedProbeExpectationsStayNarrowlyExcluded(unittest.TestCase):
    """Keep generated probe output out without hiding its authored machinery."""

    def test_exclusion_covers_expectations_but_not_authored_paths(self) -> None:
        excludes = configured_excludes()
        expectation = (
            "docs/openapi-surface/probe-expected/"
            "annotated-ref-target-closed-object/src/fern/types/target.py"
        )
        authored = (
            "docs/openapi-surface/probes/annotated-ref-target-closed-object.yml",
            "tools/surface-census/openapi-surface-census.py",
            "tools/surface-census/tests/surface_census_test.py",
            "crates/crozier-e2e/tests/e2e.rs",
        )

        self.assertTrue(
            any(fnmatch.fnmatchcase(expectation, pattern) for pattern in excludes),
            "llmlint.yml no longer excludes the generated Fern probe expectations",
        )
        for path in authored:
            with self.subTest(path=path):
                self.assertTrue((REPO / path).is_file(), f"authored path is missing: {path}")
                self.assertFalse(
                    any(fnmatch.fnmatchcase(path, pattern) for pattern in excludes),
                    f"llmlint.yml excludes authored probe machinery: {path}",
                )


def llmlint_binary() -> str | None:
    """The llmlint binary, including the `uv tool` bin dir setup-llmlint.sh uses."""
    local_bin = str(Path.home() / ".local" / "bin")
    path = os.pathsep.join([os.environ.get("PATH", ""), local_bin])
    return shutil.which("llmlint", path=path)


def require_llmlint() -> bool:
    return os.environ.get("CROZIER_REQUIRE_LLMLINT") == "1"


def config_with_urls() -> str:
    """The pre-repair configuration: every vendored path back to its recorded URL.

    Built from the repository's own `llmlint.yml` so the control differs from the
    repaired config in exactly one respect — where the plugins resolve from.
    """
    text = CONFIG.read_text(encoding="utf-8")
    for plugin in VENDORED:
        spelling = f'"./{plugin["file"]}"'
        if spelling not in text:
            raise AssertionError(
                f"llmlint.yml does not name {spelling}; the lock and the config have drifted"
            )
        text = text.replace(spelling, f'"{plugin["url"]}@{plugin["pin"]}"')
    return text


class LockRecordsTheVendoredRuleSet(unittest.TestCase):
    """The record is what identifies the rule set, so it must match the tree."""

    def test_every_vendored_plugin_matches_its_recorded_hash_and_version(self) -> None:
        for plugin in VENDORED:
            with self.subTest(plugin=plugin["name"]):
                document = (REPO / plugin["file"]).read_text(encoding="utf-8")
                self.assertEqual(
                    hashlib.sha256(document.encode("utf-8")).hexdigest(),
                    plugin["sha256"],
                    f"{plugin['file']} is not the document the lock records — a rule"
                    " may have been substituted under an unchanged name; re-run"
                    " `just llmlint-plugins-refresh` and review the diff",
                )
                self.assertIn(
                    f"\nversion: {plugin['version']}\n",
                    f"\n{document}",
                    f"{plugin['file']} does not declare version {plugin['version']}",
                )
                self.assertEqual(
                    plugin["version"].split(".")[: len(plugin["pin"].split("."))],
                    plugin["pin"].split("."),
                    f"{plugin['name']} version {plugin['version']} escapes its pin"
                    f" @{plugin['pin']}",
                )

    def test_config_resolves_plugins_only_from_the_recorded_set(self) -> None:
        text = CONFIG.read_text(encoding="utf-8")
        for plugin in VENDORED:
            with self.subTest(plugin=plugin["name"]):
                self.assertIn(f'"./{plugin["file"]}"', text)
        bundled = [plugin for plugin in PLUGINS if plugin.get("bundled")]
        for plugin in bundled:
            with self.subTest(plugin=plugin["name"]):
                # The bundled plugin ships inside the llmlint binary and resolves
                # offline, so it stays a URL: it is not a job-time fetch.
                self.assertIn(f'"{plugin["url"]}@{plugin["pin"]}"', text)
        recorded = {f'{plugin["url"]}@{plugin["pin"]}' for plugin in bundled}
        quoted = [line.strip().strip("- ").strip('"') for line in text.splitlines()]
        fetched = [
            entry
            for entry in quoted
            if entry.startswith(("http://", "https://")) and entry not in recorded
        ]
        self.assertEqual(
            fetched,
            [],
            "llmlint.yml resolves a plugin over the network at judge time; vendor it"
            " with `just llmlint-plugins-refresh` instead (docs/llmlint-plugins.md)",
        )


class AMalformedLockIsRefusedBeforeAnyFetch(unittest.TestCase):
    """`refresh` reads the lock's hand-edited fields first; a lock of the wrong
    shape fails there with the fix, before any network or llmlint call."""

    def refresh_over(self, lock: object) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script = root / "tools" / "llmlint" / "llmlint-plugins.py"
            script.parent.mkdir(parents=True)
            shutil.copy2(REPO / "tools" / "llmlint" / "llmlint-plugins.py", script)
            (root / "llmlint-plugins").mkdir()
            (root / "llmlint-plugins" / "lock.json").write_text(json.dumps(lock), encoding="utf-8")
            return subprocess.run([sys.executable, str(script), "refresh"], capture_output=True, text=True,
                                  env={**os.environ, "PATH": ""}, timeout=60)

    def test_a_lock_that_is_not_an_object_is_refused(self) -> None:
        run = self.refresh_over([{"name": "base"}])
        self.assertEqual(1, run.returncode, run.stdout + run.stderr)
        self.assertIn("declares no plugins", run.stderr)
        self.assertNotIn("Traceback", run.stderr)

    def test_an_entry_missing_its_hand_edited_fields_is_refused(self) -> None:
        run = self.refresh_over({"schema": 1, "plugins": [{"name": "base", "url": "", "pin": 1}]})
        self.assertEqual(1, run.returncode, run.stdout + run.stderr)
        self.assertIn("plugin #1 lacks url, pin, file", run.stderr)
        self.assertIn("non-empty name, url, pin and file", run.stderr)
        self.assertNotIn("Traceback", run.stderr)

    def test_a_file_outside_the_vendor_directory_is_refused(self) -> None:
        # A loopback http URL: were the path accepted, the fetch would refuse it
        # without touching the network, with a different message.
        for file in (
            "/tmp/base.llmlint.yml",
            "../base.llmlint.yml",
            "llmlint-plugins/../../base.llmlint.yml",
            "docs/base.llmlint.yml",
            "llmlint-plugins",
            "llmlint-plugins\\..\\..\\base.llmlint.yml",
        ):
            with self.subTest(file=file):
                run = self.refresh_over({"schema": 1, "plugins": [
                    {"name": "base", "url": "http://127.0.0.1:9/base.yml", "pin": "1", "file": file}]})
                self.assertEqual(1, run.returncode, run.stdout + run.stderr)
                self.assertIn(f"plugin #1 file {file!r} is not under llmlint-plugins/", run.stderr)
                self.assertIn("record a relative path inside llmlint-plugins/ with no '..'", run.stderr)
                self.assertNotIn("Traceback", run.stderr)


class AMalformedLlmlintAnswerIsRefused(unittest.TestCase):
    """`refresh` names each plugin's rules from `llmlint config --sources`; a
    stub `llmlint` on PATH answering in the wrong shape must fail with the fix.
    A bundled-only lock reaches that call without fetching anything."""

    def refresh_with_answer(self, answer: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script = root / "tools" / "llmlint" / "llmlint-plugins.py"
            script.parent.mkdir(parents=True)
            shutil.copy2(REPO / "tools" / "llmlint" / "llmlint-plugins.py", script)
            (root / "llmlint-plugins").mkdir()
            lock = {"schema": 1, "plugins": [{
                "name": "config-lint", "url": "https://example.test/config_lint.yml", "pin": "1",
                "file": "llmlint-plugins/config-lint.yml", "bundled": True}]}
            (root / "llmlint-plugins" / "lock.json").write_text(json.dumps(lock), encoding="utf-8")
            stubs = root / "bin"
            stubs.mkdir()
            (stubs / "llmlint").write_text(
                f"#!/bin/sh\ncat <<'ANSWER'\n{answer}\nANSWER\n", encoding="utf-8"
            )
            (stubs / "llmlint").chmod(0o755)
            run = subprocess.run([sys.executable, str(script), "refresh"], capture_output=True, text=True,
                                 env={**os.environ, "PATH": f"{stubs}{os.pathsep}{os.environ['PATH']}"}, timeout=60)
            self.assertEqual(json.loads((root / "llmlint-plugins" / "lock.json").read_text()), lock,
                             "a refused answer must leave the lock untouched")
            return run

    @unittest.skipIf(os.name == "nt", "the stub llmlint is a POSIX shell script")
    def test_each_malformed_answer_names_the_fix(self) -> None:
        for answer, message in (
            ("not json", "printed no JSON document"),
            ("[]", "no `sources.rules` object"),
            ('{"sources": {}}', "no `sources.rules` object"),
            ('{"sources": {"rules": ["base"]}}', "no `sources.rules` object"),
            ('{"sources": {"rules": {"base": "here"}}}', "rule 'base' without a source string"),
            ('{"sources": {"rules": {"base": {"source": 7}}}}', "rule 'base' without a source string"),
        ):
            with self.subTest(answer=answer):
                run = self.refresh_with_answer(answer)
                self.assertEqual(1, run.returncode, run.stdout + run.stderr)
                self.assertIn(message, run.stderr)
                self.assertIn("reinstall it with that recipe), then re-run", run.stderr)
                self.assertNotIn("Traceback", run.stderr)


class _Plugins(http.server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - the stdlib's handler name
        body = self.server.documents.get(self.path)
        self.server.requests.append(self.path)
        self.send_response(200 if body is not None else 404)
        self.end_headers()
        if body is not None:
            self.wfile.write(body)

    def log_message(self, *_args: object) -> None:
        pass


@unittest.skipIf(os.name == "nt", "the stub llmlint is a POSIX shell script")
class ARefreshFetchesScreensAndRecords(unittest.TestCase):
    """A whole `refresh` over a synthetic root: the vendored plugin fetched from
    a loopback server (`CROZIER_LLMLINT_PLUGINS_ORIGIN`), its version screened
    against its pin, the copy and the lock rewritten, and the rules named by a
    stub `llmlint` that answers as the real one does."""

    URL = "https://plugins.example.test/rules/base.llmlint.yml"
    BUNDLED = "https://plugins.example.test/rules/config_lint.yml"
    DOCUMENT = b"version: 1.4.2\nrules:\n  - name: alpha\n"

    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.script = self.root / "tools" / "llmlint" / "llmlint-plugins.py"
        self.script.parent.mkdir(parents=True)
        shutil.copy2(REPO / "tools" / "llmlint" / "llmlint-plugins.py", self.script)
        (self.root / "llmlint-plugins").mkdir()
        self.lock_path = self.root / "llmlint-plugins" / "lock.json"
        self.vendored = self.root / "llmlint-plugins" / "base.llmlint.yml"
        self.write_lock({"schema": 1, "plugins": [
            {"name": "base", "url": self.URL, "pin": "1", "file": "llmlint-plugins/base.llmlint.yml"},
            {"name": "config-lint", "url": self.BUNDLED, "pin": "1",
             "file": "llmlint-plugins/config-lint.yml", "bundled": True},
        ]})
        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Plugins)
        self.server.documents = {"/rules/base.llmlint.yml": self.DOCUMENT}
        self.server.requests = []
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(thread.join)
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.origin = "http://127.0.0.1:{}".format(self.server.server_address[1])
        stubs = self.root / "bin"
        stubs.mkdir()
        (stubs / "llmlint").write_text(
            '#!/bin/sh\n'
            'if [ "$1" = --version ]; then printf "%s\\n" "$STUB_VERSION"; exit 0; fi\n'
            'cat "$STUB_SOURCES"\n',
            encoding="utf-8",
        )
        (stubs / "llmlint").chmod(0o755)
        self.sources = self.root / "sources.json"
        self.answer({"alpha": str(self.vendored), "beta": str(self.vendored),
                     "gamma": f"{self.BUNDLED}@1"})
        self.env = {**os.environ, "PATH": f"{stubs}{os.pathsep}{os.environ['PATH']}",
                    "STUB_SOURCES": str(self.sources), "STUB_VERSION": "llmlint 0.9.1",
                    "CROZIER_LLMLINT_PLUGINS_ORIGIN": self.origin}

    def write_lock(self, lock: dict) -> None:
        self.lock_path.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")

    def lock(self) -> dict:
        return json.loads(self.lock_path.read_text(encoding="utf-8"))

    def answer(self, rules: dict[str, str]) -> None:
        self.sources.write_text(json.dumps(
            {"sources": {"rules": {rule: {"source": source} for rule, source in rules.items()}}}),
            encoding="utf-8")

    def refresh(self, **env: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(self.script), "refresh"], capture_output=True,
                              text=True, env={**self.env, **env}, timeout=60)

    def test_a_refresh_vendors_the_document_and_records_what_llmlint_resolved(self) -> None:
        run = self.refresh()
        self.assertEqual(0, run.returncode, run.stderr)
        self.assertEqual(["/rules/base.llmlint.yml"], self.server.requests, "a bundled plugin is never fetched")
        self.assertEqual(self.DOCUMENT, self.vendored.read_bytes())
        base, bundled = self.lock()["plugins"]
        self.assertEqual(self.URL, base["url"], "the lock keeps the recorded URL, not the test origin")
        self.assertEqual("1.4.2", base["version"])
        self.assertEqual(hashlib.sha256(self.DOCUMENT).hexdigest(), base["sha256"])
        self.assertEqual(["alpha", "beta"], base["rules"])
        self.assertEqual(["gamma"], bundled["rules"])
        self.assertEqual("0.9.1", bundled["captured_with_llmlint"])
        self.assertIn("llmlint-plugins: base 1.4.2 (2 rules)\n  + alpha\n  + beta\n", run.stdout)
        self.assertIn("review the diff and commit llmlint-plugins/ together", run.stdout)
        again = self.refresh()
        self.assertEqual(0, again.returncode, again.stderr)
        self.assertEqual("llmlint-plugins: unchanged (2 plugins)\n", again.stdout)

    def test_a_moved_rule_set_is_listed_rule_by_rule(self) -> None:
        self.assertEqual(0, self.refresh().returncode)
        self.answer({"alpha": str(self.vendored), "delta": str(self.vendored), "gamma": f"{self.BUNDLED}@1"})
        run = self.refresh()
        self.assertEqual(0, run.returncode, run.stderr)
        self.assertIn("  + delta\n  - beta\n", run.stdout)
        self.assertEqual(["alpha", "delta"], self.lock()["plugins"][0]["rules"])

    def test_each_refusal_names_its_fix_and_leaves_the_lock_as_it_was(self) -> None:
        before = self.lock_path.read_bytes()
        cases = [
            ("a version the pin rejects", {"/rules/base.llmlint.yml": b"version: 2.0.0\n"}, {},
             "declares version 2.0.0, which its pin @1 rejects", "widen or bump `pin` for base"),
            ("no version line", {"/rules/base.llmlint.yml": b"rules: []\n"}, {},
             "declares no top-level `version:`", "report it upstream"),
            ("a fetch the origin refuses", {}, {},
             f"could not fetch {self.URL}: HTTP Error 404", "check the network and the recorded URL"),
            ("an origin that is not loopback", {"/rules/base.llmlint.yml": self.DOCUMENT},
             {"CROZIER_LLMLINT_PLUGINS_ORIGIN": "http://example.test:80"},
             "CROZIER_LLMLINT_PLUGINS_ORIGIN='http://example.test:80' is not a loopback origin",
             "unset CROZIER_LLMLINT_PLUGINS_ORIGIN"),
            ("an llmlint with no version", {"/rules/base.llmlint.yml": self.DOCUMENT}, {"STUB_VERSION": ""},
             "`llmlint --version` exited 0 and printed '', no version", "reinstall llmlint"),
        ]
        for name, documents, env, message, remedy in cases:
            with self.subTest(name):
                self.server.documents = documents
                run = self.refresh(**env)
                self.assertEqual(1, run.returncode, run.stdout + run.stderr)
                self.assertIn(message, run.stderr)
                self.assertIn(remedy, run.stderr)
                self.assertNotIn("Traceback", run.stderr)
                self.assertEqual(before, self.lock_path.read_bytes())

    def test_a_plugin_llmlint_resolves_no_rules_for_is_refused(self) -> None:
        self.answer({"gamma": f"{self.BUNDLED}@1"})
        run = self.refresh()
        self.assertEqual(1, run.returncode, run.stdout + run.stderr)
        self.assertIn("base contributed no rules to the resolved config", run.stderr)
        self.assertIn("check the plugin document, then re-run", run.stderr)

    def test_a_bundled_flag_that_is_not_a_boolean_is_refused_before_any_fetch(self) -> None:
        lock = self.lock()
        lock["plugins"][1]["bundled"] = "false"
        self.write_lock(lock)
        run = self.refresh()
        self.assertEqual(1, run.returncode, run.stdout + run.stderr)
        self.assertIn("plugin #2 has `bundled` 'false', not a boolean", run.stderr)
        self.assertEqual([], self.server.requests)


class TheGateAndTheRequiredCheckRunThisSuite(unittest.TestCase):
    """Where this suite runs is what keeps it from passing vacuously.

    The llmlint-driving tests below skip where the binary is absent — which is
    every `check` runner. The one job that HAS the binary is the required
    `llmlint` check, so it must run this suite with the skip turned into a
    failure, and must do so before it spends a judge call.
    """

    def test_check_runs_this_file(self) -> None:
        # `just check` runs every affected project's `test`; this project's
        # aggregate names the target that runs this file, outside the promoted
        # tiers, and the recipe CI's llmlint job calls is that target.
        project = json.loads((REPO / "tools" / "llmlint" / "project.json").read_text(encoding="utf-8"))
        self.assertNotIn("tier:promoted", project["tags"])
        self.assertIn("test-plugins", project["targets"]["test"]["dependsOn"])
        self.assertEqual(f"python3 {Path(__file__).resolve().relative_to(REPO).as_posix()}",
                         project["targets"]["test-plugins"]["options"]["command"])
        self.assertIn({"env": "CROZIER_REQUIRE_LLMLINT"}, project["targets"]["test-plugins"]["inputs"])
        justfile = (REPO / "justfile").read_text(encoding="utf-8").splitlines()
        recipe = justfile[justfile.index("test-llmlint-plugins:") + 1].strip()
        self.assertEqual("@just nx run llmlint-tooling:test-plugins", recipe)

    def test_the_required_llmlint_check_runs_it_without_the_skip(self) -> None:
        workflow = (REPO / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        boundary = workflow.find("run: just test-llmlint-plugins")
        self.assertNotEqual(boundary, -1, "the llmlint job no longer runs this suite")
        self.assertIn(
            'CROZIER_REQUIRE_LLMLINT: "1"',
            workflow[:boundary],
            "the llmlint job runs this suite with the missing-binary skip still live",
        )
        for judged in ("just lint-llm-validate", "just lint-llm-diff"):
            with self.subTest(step=judged):
                self.assertLess(
                    boundary,
                    workflow.index(judged),
                    f"{judged} runs before the plugin set is proven resolvable",
                )


@unittest.skipIf(
    llmlint_binary() is None and not require_llmlint(),
    "llmlint is not installed (`just setup-llmlint`)",
)
class ResolvesWithTheOriginUnreachable(unittest.TestCase):
    """Drive the real binary with the plugin origin refused from this process."""

    def setUp(self) -> None:
        self.llmlint = llmlint_binary()
        if self.llmlint is None:
            self.fail(
                "CROZIER_REQUIRE_LLMLINT=1 but llmlint is not installed —"
                " run `just setup-llmlint`"
            )
        self.temporary = tempfile.TemporaryDirectory()
        self.scratch = Path(self.temporary.name)
        self.addCleanup(self.temporary.cleanup)

    def offline_env(self) -> dict[str, str]:
        """Point every proxy variable at a closed local port: connection refused.

        A cold cache directory and `LLMLINT_PLUGIN_TTL=0` remove the other way a
        run could survive — no cached copy is present, and none would be trusted
        without revalidating — so anything that resolves came out of the tree.
        """
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            refused = f"http://127.0.0.1:{probe.getsockname()[1]}"
        env = dict(os.environ)
        for name in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"):
            env[name] = refused
            env[name.lower()] = refused
        env.pop("NO_PROXY", None)
        env.pop("no_proxy", None)
        cache = self.scratch / f"cache-{len(list(self.scratch.iterdir()))}"
        cache.mkdir()
        env["LLMLINT_CACHE_DIR"] = str(cache)
        env["LLMLINT_PLUGIN_TTL"] = "0"
        return env

    def resolve(self, config: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [self.llmlint, *args, "-c", str(config), "--cwd", str(REPO)],
            capture_output=True,
            text=True,
            check=False,
            env=self.offline_env(),
        )

    def test_repaired_config_reaches_a_verdict_with_the_origin_refused(self) -> None:
        validated = self.resolve(CONFIG, "validate", "--diff-base", "HEAD")
        self.assertEqual(
            validated.returncode,
            0,
            f"the judged tier's first llmlint step failed offline:\n{validated.stderr}",
        )

    def test_the_judged_run_plans_every_recorded_rule_with_the_origin_refused(self) -> None:
        """`--plan-only` is the judged command's own path, minus the model call.

        `just lint-llm-diff` resolves the plugins, selects the files, and batches
        the rules before it spends a judge call; planning it offline shows that
        whole path reaching the point of judging without the origin.
        """
        planned = self.resolve(CONFIG, "--plan-only")
        self.assertEqual(planned.returncode, 0, planned.stderr)
        for plugin in PLUGINS:
            for rule in plugin["rules"]:
                with self.subTest(rule=rule):
                    self.assertIn(rule, planned.stdout)

    def test_resolved_rules_are_exactly_the_ones_the_lock_records(self) -> None:
        resolved = self.resolve(CONFIG, "config", "--sources")
        self.assertEqual(resolved.returncode, 0, resolved.stderr)
        by_source: dict[str, set[str]] = {}
        for rule, origin in json.loads(resolved.stdout)["sources"]["rules"].items():
            by_source.setdefault(origin["source"], set()).add(rule)
        for plugin in PLUGINS:
            with self.subTest(plugin=plugin["name"]):
                source = (
                    f'{plugin["url"]}@{plugin["pin"]}'
                    if plugin.get("bundled")
                    else str(REPO / plugin["file"])
                )
                self.assertEqual(
                    sorted(by_source.pop(source, set())),
                    plugin["rules"],
                    f"{plugin['name']} did not contribute the rules the lock records",
                )
        self.assertEqual(
            {source: sorted(rules) for source, rules in by_source.items()},
            {},
            "a rule resolved from a source the lock does not record",
        )

    def test_the_url_spelling_still_fails_with_the_origin_refused(self) -> None:
        control = self.scratch / "pre-repair.llmlint.yml"
        control.write_text(config_with_urls(), encoding="utf-8")
        resolved = self.resolve(control, "config", "--sources")
        self.assertNotEqual(
            resolved.returncode,
            0,
            "the pre-repair configuration resolved with the origin refused, so this"
            " suite is not actually inducing the failure it claims to induce",
        )
        self.assertIn(VENDORED[0]["url"], resolved.stderr)


if __name__ == "__main__":
    unittest.main()

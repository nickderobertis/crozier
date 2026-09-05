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

import hashlib
import json
import os
import shutil
import socket
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOCK = REPO / "llmlint-plugins" / "lock.json"
CONFIG = REPO / "llmlint.yml"
RECORD = json.loads(LOCK.read_text(encoding="utf-8"))
PLUGINS = RECORD["plugins"]
VENDORED = [plugin for plugin in PLUGINS if not plugin.get("bundled")]


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


class TheGateAndTheRequiredCheckRunThisSuite(unittest.TestCase):
    """Where this suite runs is what keeps it from passing vacuously.

    The llmlint-driving tests below skip where the binary is absent — which is
    every `check` runner. The one job that HAS the binary is the required
    `llmlint` check, so it must run this suite with the skip turned into a
    failure, and must do so before it spends a judge call.
    """

    def test_check_runs_this_file(self) -> None:
        justfile = (REPO / "justfile").read_text(encoding="utf-8").splitlines()
        gate = next(line for line in justfile if line.startswith("check:"))
        self.assertIn("test-llmlint-plugins", gate.split())
        recipe = justfile[justfile.index("test-llmlint-plugins:") + 1].strip()
        self.assertEqual(f"python3 tests/{Path(__file__).name}", recipe)

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

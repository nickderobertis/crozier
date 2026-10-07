"""The Fern goldens tooling's offline suites: the committed golden state against
the tool's own computation, and `fern-overlay-goldens.sh` with a stand-in
generator. The suites that drive the real `git` or `just` are
`tools/fern-goldens-git/tests/fern_goldens_git_test.py`'s, which imports the
helpers defined here.
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
import unittest.mock
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
TOOL = REPO / "tools" / "fern-goldens" / "fern-goldens"


def mirror(root: Path, *paths: str) -> None:
    """Copy each repository-relative path to the same place under `root`, so the
    copied scripts find their neighbours where the real tree keeps them."""
    for path in paths:
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / path, root / path)
STATE = ".crozier-fern-golden.json"
ALIASES = REPO / "tests" / "fixtures" / "corpus-aliases.tsv"
PIN_MANIFEST = REPO / "tests" / "fixtures" / "corpus-remote-ref-pins.tsv"
KNOWN_FAILURE = (
    REPO
    / "tests"
    / "fixtures"
    / "calorieninjas.com"
    / "known-fern-failure.json"
)


def load_goldens_tool():
    """`tools/fern-goldens/fern-goldens` as a module. It has no `.py` suffix, so the loader
    is named explicitly rather than inferred from the path."""
    loader = importlib.machinery.SourceFileLoader("fern_goldens", str(TOOL))
    spec = importlib.util.spec_from_loader("fern_goldens", loader)
    module = importlib.util.module_from_spec(spec)
    sys.modules["fern_goldens"] = module
    loader.exec_module(module)
    return module


class CommittedGoldenStateTests(unittest.TestCase):
    """`expected_state` over the REAL tree, against the REAL committed state files.

    `is_current()` byte-compares a golden's state file against `expected_state`,
    so these are the tests that say whether the corpus is current — a branch
    cannot answer that for the goldens `main` carries.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.tool = load_goldens_tool()
        cls.rows = cls.tool.load_manifest(REPO)

    def committed(self, row) -> Path:
        return REPO / "tests" / "fixtures" / row.fixture / "expected" / STATE

    def test_the_pinned_row_state_is_what_the_tool_computes_for_it(self) -> None:
        row = next(r for r in self.rows if r.name == "helios-verifiable-api")
        committed = self.committed(row)
        payload = json.loads(committed.read_text(encoding="utf-8"))
        self.assertEqual(
            committed.read_bytes(),
            self.tool.expected_state(REPO, row, payload["fern_python_sdk_version"]),
        )
        self.assertEqual(len(payload["corpus_remote_ref_pins"]), 7)
        for pin in payload["corpus_remote_ref_pins"]:
            self.assertEqual(sorted(pin), ["pinned_url", "sha256", "url"])

    def test_multi_file_golden_state_names_every_pinned_member(self) -> None:
        for name in ("folio-mod-authtoken", "raybot"):
            row = next(r for r in self.rows if r.name == name)
            payload = json.loads(self.committed(row).read_text(encoding="utf-8"))
            pins = payload["corpus_tree_pins"]
            self.assertGreater(len(pins), 1)
            self.assertEqual(
                {pin["path"] for pin in pins},
                {record.path for record in self.tool.load_pins_module(REPO).tree_records_for(name, REPO)},
            )
            self.assertEqual(
                self.committed(row).read_bytes(),
                self.tool.expected_state(REPO, row, payload["fern_python_sdk_version"]),
            )

    def test_every_row_without_pin_records_keeps_the_state_it_already_had(self) -> None:
        """The conditional-emission guarantee, stated over the committed corpus."""
        checked = 0
        for row in self.rows:
            committed = self.committed(row)
            if not committed.is_file():
                continue
            if self.tool.corpus_remote_ref_pins(REPO, row):
                continue
            payload = json.loads(committed.read_text(encoding="utf-8"))
            with self.subTest(row.fixture):
                self.assertNotIn("corpus_remote_ref_pins", payload)
                self.assertEqual(
                    committed.read_bytes(),
                    self.tool.expected_state(
                        REPO, row, payload["fern_python_sdk_version"]
                    ),
                )
            checked += 1
        self.assertGreater(checked, 100, "the committed corpus should be most of the rows")


@unittest.skipIf(os.name == "nt", "Fern golden workflow scripts run on Linux")
class FixtureNewTests(unittest.TestCase):
    """`fixture-new.sh` over a synthetic root: the placeholder and the wiring steps it
    prints, and a fixture directory it cannot complete left absent, not half-made."""

    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        mirror(self.root, "tools/fern-goldens/fixture-new.sh", "scripts/lib.sh")
        self.fixtures = self.root / "tests" / "fixtures"
        self.fixtures.mkdir(parents=True)

    def scaffold(self, name: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([str(self.root / "tools" / "fern-goldens" / "fixture-new.sh"), name],
                              capture_output=True, text=True, check=False)

    def test_a_fixture_is_scaffolded_with_its_wiring_steps(self) -> None:
        done = self.scaffold("shapes")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn("openapi: 3.0.0", (self.fixtures / "shapes" / "openapi.yml").read_text(encoding="utf-8"))
        self.assertIn("copy an existing FEATURE_TARGETS entry", done.stderr)
        self.assertIn("tools/fern-goldens/generate-fern-fixture.sh shapes", done.stderr)

    def test_a_fixture_it_cannot_write_is_left_absent_with_the_fix(self) -> None:
        if os.geteuid() == 0:
            self.skipTest("root writes through a read-only directory")
        self.fixtures.chmod(0o555)
        self.addCleanup(self.fixtures.chmod, 0o755)
        refused = self.scaffold("shapes")
        self.assertEqual(1, refused.returncode, refused.stderr)
        self.assertIn("could not create", refused.stderr)
        self.assertIn("check that tests/fixtures/ is writable and the disk has free space", refused.stderr)
        self.assertFalse((self.fixtures / "shapes").exists())

    def test_a_placeholder_it_cannot_write_removes_the_directory_it_made(self) -> None:
        if os.geteuid() == 0:
            self.skipTest("root writes through a read-only directory")
        # Under this umask the new fixture directory is made unwritable, so
        # creating it succeeds and writing its openapi.yml fails.
        refused = subprocess.run(["sh", "-c", 'umask 0277 && exec "$0" shapes',
                                  str(self.root / "tools" / "fern-goldens" / "fixture-new.sh")],
                                 capture_output=True, text=True, check=False)
        self.assertEqual(1, refused.returncode, refused.stderr)
        self.assertIn("could not create", refused.stderr)
        self.assertNotIn("could not remove", refused.stderr)
        self.assertFalse((self.fixtures / "shapes").exists())


class GoldenOverlayReductionTests(unittest.TestCase):
    """`golden_overlay.py reduce` over real directories: what it keeps of an
    overlay tree, and each argument it refuses before touching the tree."""

    SCRIPT = REPO / "tools" / "fern-goldens" / "golden_overlay.py"

    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.base = Path(scratch.name) / "expected"
        self.tree = Path(scratch.name) / "expected-literals"
        for root, enum in ((self.base, "python_enums"), (self.tree, "literals")):
            (root / "src" / "types").mkdir(parents=True)
            (root / "src" / "client.py").write_text("class Client: ...\n", encoding="utf-8")
            (root / "src" / "types" / "color.py").write_text(f"# {enum}\n", encoding="utf-8")
        (self.base / "src" / "types" / "gone.py").write_text("x = 1\n", encoding="utf-8")

    def reduce(self, tree: Path, provenance: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(self.SCRIPT), "reduce", str(self.base), str(tree), provenance],
                              capture_output=True, text=True, check=False)

    def test_the_overlay_keeps_only_what_differs_and_names_what_it_lacks(self) -> None:
        done = self.reduce(self.tree, '{"enum_type": "literals", "base": "expected"}')
        self.assertEqual(done.returncode, 0, done.stderr)
        kept = sorted(p.relative_to(self.tree).as_posix() for p in self.tree.rglob("*") if p.is_file())
        self.assertEqual(kept, [".crozier-overlay.json", "src/types/color.py"])
        manifest = json.loads((self.tree / ".crozier-overlay.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest, {"enum_type": "literals", "base": "expected", "removed": ["src/types/gone.py"]})

    def test_each_refused_argument_names_its_fix_and_leaves_the_tree(self) -> None:
        for label, tree, provenance, message in (
            ("no tree", self.tree.parent / "absent", "{}", "no generated tree at"),
            ("not JSON", self.tree, "{enum_type: literals}", "PROVENANCE_JSON is not JSON"),
            ("not an object", self.tree, '["literals"]', "must be a JSON object"),
            ("a removed key", self.tree, '{"removed": []}', "without a `removed` key"),
        ):
            with self.subTest(label):
                refused = self.reduce(tree, provenance)
                self.assertEqual(refused.returncode, 1, refused.stderr)
                self.assertIn(message, refused.stderr)
                self.assertNotIn("Traceback", refused.stderr)
                self.assertTrue((self.tree / "src" / "client.py").is_file(), "a refused run reduced the tree")


@unittest.skipIf(os.name == "nt", "Fern golden workflow scripts run on Linux")
class FernOverlayGoldensTests(unittest.TestCase):
    """`tools/fern-goldens/fern-overlay-goldens.sh` over a synthetic repository root: the
    real script and `lib.sh`, a stand-in `generate-fern-fixture.sh` that writes
    the setting it was given as the overlay, where the script asks."""

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "repo"
        scripts = self.root / "scripts"
        scripts.mkdir(parents=True)
        mirror(self.root, "tools/fern-goldens/fern-overlay-goldens.sh", "scripts/lib.sh")
        pin = {"fern_python_sdk_version": "4.3.17"}
        for fixture in ("eos.local", "alpha", "beta"):
            expected = self.root / "tests" / "fixtures" / fixture / "expected"
            expected.mkdir(parents=True)
            (expected / STATE).write_text(json.dumps(pin), encoding="utf-8")
            (expected.parent / "openapi.yml").write_text("openapi: 3.0.3\n", encoding="utf-8")
        generator = self.root / "tools/fern-goldens/generate-fern-fixture.sh"
        generator.write_text(
            textwrap.dedent(
                r"""
                #!/usr/bin/env bash
                set -euo pipefail
                setting="$1 $2"
                shift 2
                fixture="$1" destination="$4"
                [ "$fixture" != "${FAIL_GENERATE:-}" ] || { echo "simulated Fern failure" >&2; exit 3; }
                mkdir -p "$destination"
                echo "$setting" >"$destination/version.py"
                # A stage the worker cannot move the overlay out of.
                [ "$fixture" != "${FAIL_INSTALL:-}" ] || chmod a-w "$(dirname "$destination")"
                """
            ).lstrip(),
            encoding="utf-8",
        )
        generator.chmod(0o755)

    def run_overlay(
        self, *fixtures: str, fail_install: str = "", fail_generate: str = ""
    ) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [
                str(self.root / "tools" / "fern-goldens" / "fern-overlay-goldens.sh"),
                "--jobs",
                "2",
                "--enum-type",
                "literals",
                *fixtures,
            ],
            env={**os.environ, "FAIL_INSTALL": fail_install, "FAIL_GENERATE": fail_generate},
            capture_output=True,
            text=True,
            check=False,
        )
        for stage in (self.root / "tests" / "fixtures").glob("*/.fern-overlay-stage.*"):
            stage.chmod(0o755)
        return result

    def test_each_fixture_gets_its_overlay_golden_under_one_summary_line(self) -> None:
        result = self.run_overlay("alpha", "beta")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout,
            "generated alpha/expected-literals, beta/expected-literals"
            " at fernapi/fern-python-sdk:4.3.17\n",
        )
        for fixture in ("alpha", "beta"):
            golden = self.root / "tests" / "fixtures" / fixture / "expected-literals"
            self.assertEqual((golden / "version.py").read_text(encoding="utf-8"), "--enum-type literals\n")

    def test_a_failed_golden_install_fails_the_run_and_is_not_reported(self) -> None:
        if os.geteuid() == 0:
            self.skipTest("root moves out of a read-only directory")
        result = self.run_overlay("alpha", "beta", fail_install="alpha")
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertNotIn("generated alpha/", result.stdout)
        self.assertIn("alpha: could not install expected-literals", result.stderr)
        self.assertIn("make tests/fixtures/alpha writable, then move it into place", result.stderr)
        stage = next((self.root / "tests" / "fixtures" / "alpha").glob(".fern-overlay-stage.*"))
        self.assertIn(f"(mv {stage}/expected-literals ", result.stderr)
        self.assertIn(f"discard it (rm -rf {stage})", result.stderr)
        self.assertFalse((self.root / "tests" / "fixtures" / "alpha" / "expected-literals").exists())
        self.assertEqual(
            result.stdout, "generated beta/expected-literals at fernapi/fern-python-sdk:4.3.17\n"
        )

    def test_a_failed_generation_names_its_log_and_the_command_that_retries_it(self) -> None:
        result = self.run_overlay("alpha", "beta", fail_generate="alpha")
        self.assertNotEqual(result.returncode, 0, result.stdout)
        log = self.root / ".local" / "fern-overlay" / "alpha.log"
        # The cause, from the log's last line, then where the whole run is.
        self.assertIn("alpha: Fern generation failed: simulated Fern failure\n", result.stderr)
        self.assertIn(f"alpha: the whole run is in {log}", result.stderr)
        self.assertIn("simulated Fern failure", log.read_text(encoding="utf-8"))
        self.assertIn(
            "then re-run tools/fern-goldens/fern-overlay-goldens.sh --enum-type literals alpha",
            result.stderr,
        )
        self.assertFalse(list((self.root / "tests" / "fixtures" / "alpha").glob(".fern-overlay-stage.*")))
        self.assertEqual(
            result.stdout, "generated beta/expected-literals at fernapi/fern-python-sdk:4.3.17\n"
        )

    def test_a_stage_that_cannot_be_made_names_the_step_and_the_fix(self) -> None:
        if os.geteuid() == 0:
            self.skipTest("root writes through a read-only directory")
        alpha = self.root / "tests" / "fixtures" / "alpha"
        alpha.chmod(0o555)
        try:
            result = self.run_overlay("alpha", "beta")
        finally:
            alpha.chmod(0o755)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertRegex(result.stderr, r"fern-overlay-goldens: line \d+: 'mktemp -d [^']*' failed \(exit 1\)")
        self.assertIn("then re-run this script for the fixtures that failed", result.stderr)
        self.assertEqual(
            result.stdout, "generated beta/expected-literals at fernapi/fern-python-sdk:4.3.17\n"
        )

    def test_a_pinned_rows_fetch_that_fails_reports_its_cause_and_the_retry(self) -> None:
        fixtures = self.root / "tests" / "fixtures"
        pinned = fixtures / "pinned" / "expected"
        pinned.mkdir(parents=True)
        (pinned / STATE).write_text(json.dumps({"fern_python_sdk_version": "4.3.17"}), encoding="utf-8")
        (fixtures / "corpus-remote-ref-pins.tsv").write_text("pinned\tpinned\n", encoding="utf-8")
        stubs = self.root / "stub-bin"
        stubs.mkdir()
        (stubs / "just").write_text("#!/bin/sh\necho 'fetch-corpus: the pinned commit is gone' >&2\nexit 1\n",
                                    encoding="utf-8")
        (stubs / "just").chmod(0o755)
        result = subprocess.run(
            [str(self.root / "tools" / "fern-goldens" / "fern-overlay-goldens.sh"), "--enum-type", "literals", "pinned"],
            env={**os.environ, "PATH": f"{stubs}{os.pathsep}{os.environ['PATH']}"},
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("pinned: just fetch-corpus failed: fetch-corpus: the pinned commit is gone", result.stderr)
        self.assertIn("then re-run tools/fern-goldens/fern-overlay-goldens.sh --enum-type literals pinned",
                      result.stderr)

    def test_fixtures_at_different_fern_pins_name_each_pin_in_the_summary(self) -> None:
        (self.root / "tests" / "fixtures" / "beta" / "expected" / STATE).write_text(
            json.dumps({"fern_python_sdk_version": "4.4.0"}), encoding="utf-8"
        )
        result = self.run_overlay("alpha", "beta")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout,
            "generated alpha/expected-literals at fernapi/fern-python-sdk:4.3.17,"
            " beta/expected-literals at fernapi/fern-python-sdk:4.4.0\n",
        )

    def test_each_refused_fixture_names_its_fix_and_the_rest_still_generate(self) -> None:
        fixtures = self.root / "tests" / "fixtures"
        (fixtures / "bare").mkdir()
        (fixtures / "bare" / "openapi.yml").write_text("openapi: 3.0.3\n", encoding="utf-8")
        (fixtures / "beta" / "expected" / STATE).write_text("{not json", encoding="utf-8")
        result = self.run_overlay("..", "bare", "beta", "alpha")
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(
            "..: invalid fixture name — pass the name of one directory under tests/fixtures/",
            result.stderr,
        )
        self.assertIn("[A-Za-z0-9][A-Za-z0-9._-]*", result.stderr)
        self.assertIn("bare: no expected/ golden to overlay — restore it", result.stderr)
        self.assertIn("tools/fern-goldens/generate-fern-fixture.sh bare", result.stderr)
        self.assertIn("beta: unreadable expected/.crozier-fern-golden.json — restore it", result.stderr)
        self.assertIn(
            "git checkout -- tests/fixtures/beta/expected/.crozier-fern-golden.json", result.stderr
        )
        self.assertEqual(
            result.stdout, "generated alpha/expected-literals at fernapi/fern-python-sdk:4.3.17\n"
        )


if __name__ == "__main__":
    unittest.main()

"""`tools/fern-goldens/certified_pair.py check`: the real tree states only the
pair `assets/scaffolding/metadata.json` declares, and a copy of a small tree
that states another pair, in each form the repository spells one, fails.

The versions written here are composed from the certified pair at run time, so
this file states no pair of its own.
"""

from __future__ import annotations

import fnmatch
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "fern-goldens" / "certified_pair.py"
METADATA = REPO / "assets" / "scaffolding" / "metadata.json"
PROJECT = Path(__file__).resolve().parents[1]


def load():
    spec = importlib.util.spec_from_file_location("certified_pair", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


certified_pair = load()


def bumped(version: str) -> str:
    """A version the pair is not: `version` with its patch incremented."""
    major, minor, patch = version.split(".")
    return f"{major}.{minor}.{int(patch) + 1}"


RECORD = json.loads(METADATA.read_text(encoding="utf-8"))
CLI, SDK = RECORD["cliVersion"], RECORD["generatorVersion"]
OTHER_CLI, OTHER_SDK = bumped(CLI), bumped(SDK)

# Every form a pair statement takes in this repository, with the members it
# states. `{cli}`/`{sdk}` are filled with the version under test.
FORMS = (
    ('"cliVersion": "{cli}",', ("cli",)),
    ('"generatorVersion": "{sdk}",', ("sdk",)),
    ('"\\"generatorVersion\\": \\"{sdk}\\",\\n"', ("sdk",)),
    ('fern_cli_version = "{cli}"', ("cli",)),
    ("fern_python_sdk_version: {sdk}", ("sdk",)),
    ('("fern_python_sdk_version", "{sdk}"),', ("sdk",)),
    ("npm install -g fern-api@{cli}", ("cli",)),
    ("docker pull fernapi/fern-python-sdk:{sdk}", ("sdk",)),
    ("fern generate (python-sdk@{sdk}, packaged)", ("sdk",)),
    ("Fern CLI {cli}, python-sdk {sdk}", ("cli", "sdk")),
    ("Fern CLI {cli} / python-sdk {sdk}", ("cli", "sdk")),
    ('{{ "organization": "fern", "version": "{cli}" }}', ("cli",)),
    ("      - name: fernapi/fern-python-sdk\n        version: {sdk}\n", ("sdk",)),
    ('"  - name: fernapi/fern-python-sdk\\n"\n    "    version: {sdk}\\n"', ("sdk",)),
    ('FERN_CLI = "{cli}"', ("cli",)),
    ('FERN_PYTHON_SDK: str = "{sdk}"', ("sdk",)),
    ('const FERN_CLI_VERSION: &str = "{cli}";', ("cli",)),
    ('FERN_CLI_VERSION="${{FERN_CLI_VERSION:-{cli}}}"', ("cli",)),
    ('PIN = FernPair(cli="{cli}", generator="{sdk}")', ("cli", "sdk")),
)


def wired(within: str) -> str:
    """A delegated root's project definition, running the check over itself from its lint."""
    command = f"python3 tools/fern-goldens/certified_pair.py check --within {within.rstrip('/')}"
    return json.dumps(
        {
            "targets": {
                "lint-certified-pair": {"options": {"command": command}},
                "lint": {"dependsOn": ["lint-certified-pair"]},
            }
        }
    )


WIRED = {f"{delegated}project.json": wired(delegated) for delegated in certified_pair.DELEGATED}


def run_check(root: Path, *options: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "check", str(root), *options],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


class FormTests(unittest.TestCase):
    pair = certified_pair.Pair(cli=CLI, sdk=SDK)

    def test_each_form_naming_the_certified_pair_passes(self) -> None:
        for form, _members in FORMS:
            with self.subTest(form=form):
                text = form.format(cli=CLI, sdk=SDK)
                self.assertEqual([], list(certified_pair.drifts("tool.py", text, self.pair)))

    def test_each_form_naming_another_pair_is_a_drift(self) -> None:
        for form, members in FORMS:
            with self.subTest(form=form):
                text = form.format(cli=OTHER_CLI, sdk=OTHER_SDK)
                found = list(certified_pair.drifts("tool.py", text, self.pair))
                self.assertEqual(sorted(members), sorted(drift.member for drift in found), text)
                self.assertTrue(all(drift.line == 1 for drift in found), found)

    def test_a_comment_or_a_marked_stand_in_is_not_a_statement(self) -> None:
        statement = f'FERN_CLI = "{OTHER_CLI}"'
        for text in (
            f"# {statement}",
            f"// Measured at fernapi/fern-python-sdk:{OTHER_SDK} on",
            f"/// Fern CLI {OTHER_CLI}, python-sdk {OTHER_SDK}",
            f"{statement}  # certified-pair: stand-in",
        ):
            with self.subTest(text=text):
                self.assertEqual([], list(certified_pair.drifts("tool.py", text, self.pair)))

    def test_a_version_sharing_the_pair_s_numbers_with_a_suffix_is_a_drift(self) -> None:
        for suffix in ("-rc.1", "+build.7"):
            for template, members in FORMS:
                with self.subTest(form=template, suffix=suffix):
                    text = template.format(cli=CLI + suffix, sdk=SDK + suffix)
                    found = list(certified_pair.drifts("probe.py", text, certified_pair.Pair(cli=CLI, sdk=SDK)))
                    self.assertEqual(sorted(members), sorted(drift.member for drift in found), text)
                    stated = {CLI + suffix, SDK + suffix}
                    self.assertTrue(all(drift.stated in stated for drift in found), found)

    def test_only_a_member_that_differs_is_reported(self) -> None:
        found = list(certified_pair.drifts("x.rs", f"Fern CLI {CLI}, python-sdk {OTHER_SDK}", self.pair))
        self.assertEqual([("sdk", OTHER_SDK)], [(drift.member, drift.stated) for drift in found])


class CheckTests(unittest.TestCase):
    def test_the_real_tree_states_only_the_certified_pair(self) -> None:
        result = run_check(REPO)
        self.assertEqual((0, "", ""), (result.returncode, result.stdout, result.stderr), result.stderr)

    def test_the_target_inputs_name_every_file_the_check_reads(self) -> None:
        """The target's inputs are its cache key and affected trigger: a scanned
        file outside them would never rerun the check."""
        project = json.loads((PROJECT / "project.json").read_text(encoding="utf-8"))
        patterns = [
            pattern.removeprefix("{workspaceRoot}/")
            for pattern in project["targets"]["test-certified-pair"]["inputs"]
            if pattern.startswith("{workspaceRoot}/")
        ]
        own = PROJECT.relative_to(REPO).as_posix() + "/"

        def covered(path: str) -> bool:
            for pattern in patterns:
                if pattern.endswith("/**/*") and path.startswith(pattern.removesuffix("**/*")):
                    return True
                if pattern.count("/") == path.count("/") and fnmatch.fnmatchcase(path, pattern):
                    return True
            return path.startswith(own)  # `default`

        scanned = certified_pair.scanned(REPO)
        self.assertIn(certified_pair.METADATA.as_posix(), patterns)
        self.assertTrue(scanned)
        missing = sorted({path for path in scanned if not covered(path)})
        self.assertEqual([], missing, "add each one's directory to test-certified-pair's inputs")

    def tree(self, files: dict[str, str]) -> Path:
        """A git work tree holding `files` and a copy of the real metadata.json."""
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        files = {"assets/scaffolding/metadata.json": METADATA.read_text(encoding="utf-8"), **files}
        for path, text in files.items():
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            (root / path).write_text(text, encoding="utf-8")
        for command in (["init", "-q"], ["add", "-A"]):
            subprocess.run(["git", "-C", str(root), *command], check=True, capture_output=True)
        return root

    def test_a_tree_stating_another_pair_fails_naming_each_statement(self) -> None:
        root = self.tree(
            {
                "tools/probe/probe.py": f'FERN_CLI = "{CLI}"\nFERN_PYTHON_SDK = "{OTHER_SDK}"\n',
                "justfile": f"pull:\n    docker pull fernapi/fern-python-sdk:{OTHER_SDK}\n",
                "tests/recipe.rs": f'assert!(log.starts_with("Fern CLI {OTHER_CLI}, python-sdk {SDK}\\n"));\n',
                # History and committed Fern output are never statements of the pair.
                "docs/history.md": f"Measured with Fern CLI {OTHER_CLI}, python-sdk {OTHER_SDK}.\n",
                "tests/fixtures/x/expected/.fern/metadata.json": f'{{"cliVersion": "{OTHER_CLI}"}}\n',
                "CHANGELOG.md": f"- pin fern-api@{OTHER_CLI}\n",
                # A root file is no history.
                "README.md": f"npm install -g fern-api@{OTHER_CLI}\n",
            }
        )
        result = run_check(root)
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertEqual("", result.stdout)
        lines = result.stderr.splitlines()
        self.assertEqual(
            [
                f"README.md:1: states Fern CLI {OTHER_CLI}: npm install -g fern-api@{OTHER_CLI}",
                f"justfile:2: states fern-python-sdk {OTHER_SDK}: docker pull fernapi/fern-python-sdk:{OTHER_SDK}",
                f'tests/recipe.rs:1: states Fern CLI {OTHER_CLI}: assert!(log.starts_with("Fern CLI {OTHER_CLI},'
                f' python-sdk {SDK}\\n"));',
                f'tools/probe/probe.py:2: states fern-python-sdk {OTHER_SDK}: FERN_PYTHON_SDK = "{OTHER_SDK}"',
            ],
            lines[:-1],
        )
        self.assertIn("4 statement(s) disagree with assets/scaffolding/metadata.json", lines[-1])
        self.assertIn(f"Fern CLI {CLI}, fern-python-sdk {SDK}", lines[-1])
        self.assertIn("derive the version from that file", lines[-1])

    def test_a_statement_in_any_tooling_or_test_path_fails_the_check_that_owns_it(self) -> None:
        """No tracked tooling or test file escapes: one outside the delegated
        roots fails the whole-tree check, and one inside a delegated root fails
        the `--within` check that root's own project runs."""
        statement = f'FERN_PYTHON_SDK = "{OTHER_SDK}"\n'
        planted = {
            "screenshots/capture.py": statement,
            "pool-maintenance/measure.sh": f"FERN_CLI_VERSION=${{FERN_CLI_VERSION:-{OTHER_CLI}}}\n",
            "templates/pin.j2": f"fern-api@{OTHER_CLI}\n",
            **{f"{delegated}probe.py": statement for delegated in certified_pair.DELEGATED},
            **WIRED,
        }
        root = self.tree(planted)
        result = run_check(root)
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertEqual(
            ["pool-maintenance/measure.sh", "screenshots/capture.py", "templates/pin.j2"],
            [line.split(":", 1)[0] for line in result.stderr.splitlines()[:-1]],
        )
        for delegated in certified_pair.DELEGATED:
            with self.subTest(within=delegated):
                result = run_check(root, "--within", delegated.rstrip("/"))
                self.assertEqual(1, result.returncode, result.stderr)
                self.assertEqual(
                    [f'{delegated}probe.py:1: states fern-python-sdk {OTHER_SDK}: FERN_PYTHON_SDK = "{OTHER_SDK}"'],
                    result.stderr.splitlines()[:-1],
                )
        clean = self.tree(
            {
                **{f"{delegated}probe.py": f'FERN_PYTHON_SDK = "{SDK}"\n' for delegated in certified_pair.DELEGATED},
                **WIRED,
            }
        )
        for delegated in certified_pair.DELEGATED:
            with self.subTest(clean=delegated):
                self.assertEqual(0, run_check(clean, "--within", delegated).returncode)
                self.assertEqual(0, run_check(clean, "--within", f"./{delegated}").returncode)

    def test_a_within_root_that_is_not_delegated_or_not_wired_is_refused(self) -> None:
        delegated = certified_pair.DELEGATED[0].rstrip("/")
        probe = {f"{delegated}/probe.py": f'FERN_PYTHON_SDK = "{SDK}"\n'}
        cases: tuple[tuple[str, dict[str, str], str, str], ...] = (
            ("a typo", {**probe, **WIRED}, "tests/runtme", "is no delegated root"),
            ("not delegated", {**probe, **WIRED, "tools/probe/x.py": ""}, "tools/probe", "is no delegated root"),
            (
                "the target dropped",
                {**probe, f"{delegated}/project.json": json.dumps({"targets": {"lint": {"dependsOn": []}}})},
                delegated,
                "lint-certified-pair target must run",
            ),
            (
                "another root checked",
                {**probe, f"{delegated}/project.json": wired("tests/elsewhere")},
                delegated,
                "lint-certified-pair target must run",
            ),
            ("no definition", probe, delegated, "is no readable project definition"),
            (
                "options no object",
                {
                    **probe,
                    f"{delegated}/project.json": json.dumps({"targets": {"lint-certified-pair": {"options": []}}}),
                },
                delegated,
                "lint-certified-pair target must run",
            ),
            (
                "dependsOn a string",
                {
                    **probe,
                    f"{delegated}/project.json": json.dumps(
                        {
                            "targets": {
                                **json.loads(wired(delegated))["targets"],
                                "lint": {"dependsOn": "lint-certified-pair"},
                            }
                        }
                    ),
                },
                delegated,
                "lint target must depend on lint-certified-pair",
            ),
        )
        for label, files, within, message in cases:
            with self.subTest(label):
                root = self.tree(files)
                result = run_check(root, "--within", within)
                self.assertEqual(1, result.returncode, result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertIn(message, result.stderr)

    def test_the_whole_tree_and_the_delegated_roots_cover_every_tracked_file_but_history(self) -> None:
        listed = subprocess.run(
            ["git", "-C", str(REPO), "ls-files", "-z"], capture_output=True, check=True, text=True, encoding="utf-8"
        )
        history = certified_pair.HISTORY_DIRS
        tracked = {
            path
            for path in listed.stdout.split("\0")
            if path and not path.startswith(history) and path not in certified_pair.HISTORY_FILES
        }
        covered = set(certified_pair.scanned(REPO))
        for delegated in certified_pair.DELEGATED:
            within = certified_pair.scanned(REPO, delegated)
            self.assertTrue(within, f"{delegated} lists no tracked file; drop it from DELEGATED")
            self.assertFalse(covered & set(within), delegated)
            covered |= set(within)
        self.assertEqual(sorted(tracked), sorted(covered))

    def test_a_tracked_path_it_cannot_read_as_text_is_skipped_and_the_rest_still_checked(self) -> None:
        root = self.tree(
            {
                "tools/probe/drift.py": f'FERN_CLI = "{OTHER_CLI}"\n',
                "tools/probe/deleted.py": f'FERN_CLI = "{OTHER_CLI}"\n',
                "tools/probe/now-a-directory.py": f'FERN_CLI = "{OTHER_CLI}"\n',
            }
        )
        # A binary file, a tracked file deleted in the worktree, and one replaced by a directory.
        (root / "tools/probe/image.bin").write_bytes(b"\xff\xfe fern-api@" + OTHER_CLI.encode() + b"\x00")
        subprocess.run(["git", "-C", str(root), "add", "tools/probe/image.bin"], check=True, capture_output=True)
        (root / "tools/probe/deleted.py").unlink()
        (root / "tools/probe/now-a-directory.py").unlink()
        (root / "tools/probe/now-a-directory.py").mkdir()
        result = run_check(root)
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(
            [f'tools/probe/drift.py:1: states Fern CLI {OTHER_CLI}: FERN_CLI = "{OTHER_CLI}"'],
            result.stderr.splitlines()[:-1],
        )

    @unittest.skipIf(os.name == "nt" or os.geteuid() == 0, "needs a POSIX mode a non-root reader is refused by")
    def test_a_tracked_file_it_is_refused_permission_to_read_is_skipped_and_the_rest_still_checked(self) -> None:
        # The PermissionError Windows raises for a path replaced by a directory, reached on POSIX.
        root = self.tree(
            {
                "tools/probe/drift.py": f'FERN_CLI = "{OTHER_CLI}"\n',
                "tools/probe/unreadable.py": f'FERN_CLI = "{OTHER_CLI}"\n',
            }
        )
        unreadable = root / "tools/probe/unreadable.py"
        unreadable.chmod(0)
        self.addCleanup(unreadable.chmod, 0o644)
        result = run_check(root)
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(
            [f'tools/probe/drift.py:1: states Fern CLI {OTHER_CLI}: FERN_CLI = "{OTHER_CLI}"'],
            result.stderr.splitlines()[:-1],
        )

    def test_moving_the_declaration_moves_what_passes(self) -> None:
        statement = {"tools/probe/probe.py": f'FERN_CLI = "{OTHER_CLI}"\n'}
        root = self.tree(statement)
        self.assertEqual(1, run_check(root).returncode)
        metadata = root / "assets/scaffolding/metadata.json"
        metadata.write_text(json.dumps({**RECORD, "cliVersion": OTHER_CLI}), encoding="utf-8")
        result = run_check(root)
        self.assertEqual((0, ""), (result.returncode, result.stderr))

    def test_an_unreadable_declaration_names_the_file_and_the_fix(self) -> None:
        root = self.tree({})
        (root / "assets/scaffolding/metadata.json").write_text("{", encoding="utf-8")
        result = run_check(root)
        self.assertNotEqual(0, result.returncode)
        self.assertIn(
            "cannot read cliVersion and generatorVersion from assets/scaffolding/metadata.json", result.stderr
        )
        self.assertIn("git checkout -- assets/scaffolding/metadata.json", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_a_malformed_declaration_names_the_file_and_the_fix(self) -> None:
        root = self.tree({})
        for record in (
            '["5.163.1"]',
            '{"cliVersion": null, "generatorVersion": "5.41.3"}',
            '{"cliVersion": 5}',
            '{"cliVersion": "5.163.1-rc.1", "generatorVersion": "5.41.3"}',  # certified-pair: stand-in
        ):
            with self.subTest(record=record):
                (root / "assets/scaffolding/metadata.json").write_text(record, encoding="utf-8")
                result = run_check(root)
                self.assertEqual(1, result.returncode, result.stderr)
                self.assertIn(
                    "must be an object whose cliVersion and generatorVersion are exact versions", result.stderr
                )
                self.assertIn("git checkout -- assets/scaffolding/metadata.json", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_a_root_outside_git_names_the_fix(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "assets/scaffolding").mkdir(parents=True)
            (root / "assets/scaffolding/metadata.json").write_text(METADATA.read_text(encoding="utf-8"))
            result = run_check(root)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("git ls-files failed", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_usage(self) -> None:
        self.assertEqual(2, certified_pair.main([]))
        self.assertEqual(2, certified_pair.main(["lint"]))
        self.assertEqual(2, certified_pair.main(["check", "--within", "/"]))
        self.assertEqual(2, certified_pair.main(["check", "a", "b", "--within", "tests"]))


if __name__ == "__main__":
    unittest.main()

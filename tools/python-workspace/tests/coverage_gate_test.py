#!/usr/bin/env python3
"""`coverage_gate.py`, run for real over scratch workspaces measured by real pytest.

Each case builds a small workspace laid out like this repository's (a coverage
`source` project whose suite drives its script only as a subprocess, an
extensionless Python script, test files under `tests/`), measures it with the
same pytest + pytest-cov + `patch = ["subprocess"]` configuration the tooling
projects' `test` targets use, and then runs the real gate over the data.
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

GATE = Path(__file__).resolve().parents[1] / "coverage_gate.py"

CONFIG = """\
[tool.coverage.run]
parallel = true
relative_files = true
patch = ["subprocess"]
include = ["*/proj/*"]
omit = ["*/tests/*"]

[tool.coverage.paths]
proj = ["proj/", "*/proj/"]
"""

TOOL = """\
import sys


def main(argv):
    if argv:
        print("tool", *argv)
        return 0
    print("tool: no arguments", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
"""

SCRIPT = """\
#!/usr/bin/env python3
import sys

print("script", len(sys.argv))
"""

# The suite reaches `tool.py` and `script` only through subprocesses, as most of
# this repository's suites reach their scripts, and `script` only as a copy run
# from a scratch root, as many of them do.
SUITE = """\
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]


class ToolTests(unittest.TestCase):
    def test_the_tool_echoes(self):
        run = subprocess.run([sys.executable, str(PROJECT / "tool.py"), "a"], capture_output=True, text=True)
        self.assertEqual("tool a\\n", run.stdout)

    def test_the_tool_refuses_no_arguments(self):
        run = subprocess.run([sys.executable, str(PROJECT / "tool.py")], capture_output=True, text=True)
        self.assertEqual(2, run.returncode)

    def test_a_copy_of_the_script_runs(self):
        with tempfile.TemporaryDirectory() as scratch:
            copy = Path(scratch) / "proj" / "script"
            copy.parent.mkdir()
            shutil.copy2(PROJECT / "script", copy)
            run = subprocess.run([sys.executable, str(copy)], capture_output=True, text=True)
        self.assertEqual("script 1\\n", run.stdout)
"""


def measuring_environment() -> dict[str, str]:
    """This process's environment without the outer run's coverage hooks.

    The nested pytest measures the scratch workspace with its own configuration;
    inheriting the outer `COVERAGE_*` variables would point its subprocesses at
    this repository's data instead.
    """
    return {name: value for name, value in os.environ.items() if not name.startswith("COVERAGE_")}


class ScratchWorkspace(unittest.TestCase):
    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        (self.root / "pyproject.toml").write_text(CONFIG, encoding="utf-8")
        project = self.root / "proj"
        (project / "tests").mkdir(parents=True)
        (project / "tool.py").write_text(TOOL, encoding="utf-8")
        script = project / "script"
        script.write_text(SCRIPT, encoding="utf-8")
        script.chmod(0o755)
        (project / "tests" / "tool_test.py").write_text(SUITE, encoding="utf-8")

    def measure(self, target: str = "test") -> None:
        """Run the scratch suite the way a tooling project's `test` target does."""
        run = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--cov", "--cov-report=", "proj/tests"],
            cwd=self.root,
            env={**measuring_environment(), "COVERAGE_FILE": f".coverage-data/proj/{target}/.coverage"},
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertEqual(0, run.returncode, run.stdout + run.stderr)

    def gate(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(GATE), *args],
            cwd=self.root,
            capture_output=True,
            text=True,
            timeout=300,
        )


class TheFloorHolds(ScratchWorkspace):
    def test_a_script_driven_only_as_a_subprocess_counts_as_covered(self) -> None:
        self.measure()
        passed = self.gate("--fail-under", "95", "--by-project")
        self.assertEqual(0, passed.returncode, passed.stdout + passed.stderr)
        # tool.py (8 statements) and the extensionless script (3) were run only
        # in subprocesses, the script only as a copy elsewhere, and every line of
        # both counts against the project's own files.
        self.assertEqual(
            "python-coverage: 100.00% of 11 lines across 2 files (floor 95%, 0 never run)\n"
            "  proj                                     11/11     100.00%\n",
            passed.stdout,
        )
        self.assertEqual("", passed.stderr)

    def test_every_targets_data_is_combined(self) -> None:
        self.measure("test-a")
        (self.root / "proj" / "tests" / "tool_test.py").write_text(
            SUITE.replace("def test_the_tool_refuses_no_arguments", "def skip_refusal"), encoding="utf-8"
        )
        self.measure("test-b")
        passed = self.gate("--fail-under", "100")
        self.assertEqual(0, passed.returncode, passed.stdout + passed.stderr)
        self.assertTrue((self.root / ".coverage-data" / ".coverage").is_file())


class TheFloorFails(ScratchWorkspace):
    def test_a_file_no_test_touches_counts_as_wholly_uncovered(self) -> None:
        (self.root / "proj" / "orphan.py").write_text("ONE = 1\nTWO = 2\nTHREE = 3\n", encoding="utf-8")
        self.measure()
        refused = self.gate("--fail-under", "95")
        self.assertEqual(1, refused.returncode, refused.stdout + refused.stderr)
        self.assertEqual("", refused.stdout)
        self.assertIn("proj/orphan.py", refused.stderr.replace(os.sep, "/"))
        self.assertIn(
            "combined line coverage 78.57% of 14 lines across 3 files (floor 95%, 1 never run)", refused.stderr
        )
        self.assertIn("lower the floor only with the measurement and the reason recorded in AGENTS.md", refused.stderr)

    def test_an_extensionless_script_no_run_records_is_still_counted(self) -> None:
        # `coverage` discovers only `*.py`; the gate finds the shebang script.
        unrun = self.root / "proj" / "unrun"
        unrun.write_text("#!/usr/bin/env python3\nprint('a')\nprint('b')\nprint('c')\n", encoding="utf-8")
        self.measure()
        refused = self.gate("--fail-under", "95")
        self.assertEqual(1, refused.returncode, refused.stdout + refused.stderr)
        self.assertIn("78.57% of 14 lines across 3 files (floor 95%, 1 never run)", refused.stderr)
        self.assertIn("proj/unrun", refused.stderr.replace(os.sep, "/"))

    def test_a_failing_branch_left_unrun_is_below_a_full_floor(self) -> None:
        (self.root / "proj" / "tests" / "tool_test.py").write_text(
            SUITE.replace("def test_the_tool_refuses_no_arguments", "def skip_refusal"), encoding="utf-8"
        )
        self.measure()
        refused = self.gate("--fail-under", "100")
        self.assertEqual(1, refused.returncode, refused.stdout + refused.stderr)
        self.assertIn("is below the floor", refused.stderr)
        self.assertIn("  proj ", refused.stderr)


class TheGateRefusesWhatItCannotMeasure(ScratchWorkspace):
    def test_no_data_is_a_named_failure(self) -> None:
        refused = self.gate("--fail-under", "95")
        self.assertEqual(1, refused.returncode, refused.stdout + refused.stderr)
        self.assertIn("no coverage data under .coverage-data/<project>/<target>/.coverage", refused.stderr)
        self.assertIn("run the tooling projects' tests first", refused.stderr)

    def test_a_project_path_that_is_not_a_directory_is_named(self) -> None:
        self.measure()
        (self.root / "pyproject.toml").write_text(CONFIG + 'gone = ["gone/", "*/gone/"]\n', encoding="utf-8")
        refused = self.gate("--fail-under", "95")
        self.assertEqual(1, refused.returncode, refused.stdout + refused.stderr)
        self.assertIn("coverage path 'gone' is not a directory", refused.stderr)

    def test_a_config_naming_no_project_is_named(self) -> None:
        self.measure()
        (self.root / "pyproject.toml").write_text(CONFIG.split("[tool.coverage.paths]")[0], encoding="utf-8")
        refused = self.gate("--fail-under", "95")
        self.assertEqual(1, refused.returncode, refused.stdout + refused.stderr)
        self.assertIn("names no project directories", refused.stderr)

    def test_a_floor_that_is_not_a_percentage_is_refused(self) -> None:
        for floor in ("0", "101", "ninety"):
            with self.subTest(floor=floor):
                refused = self.gate("--fail-under", floor)
                self.assertEqual(2, refused.returncode, refused.stdout + refused.stderr)
                self.assertIn("--fail-under", refused.stderr)

    def test_the_floor_is_required(self) -> None:
        refused = self.gate()
        self.assertEqual(2, refused.returncode, refused.stdout + refused.stderr)
        self.assertIn("--fail-under", refused.stderr)


class ScriptRecognition(unittest.TestCase):
    def test_only_python_shebangs_and_py_files_are_sources(self) -> None:
        sys.path.insert(0, str(GATE.parent))
        self.addCleanup(sys.path.remove, str(GATE.parent))
        import coverage_gate

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases = {
                "a.py": ("", True),
                "b": ("#!/usr/bin/env python3\n", True),
                "c": ("#!/usr/bin/env bash\n", False),
                "d.sh": ("#!/usr/bin/env python3\n", False),
                "e": ("print('no shebang')\n", False),
            }
            for name, (body, expected) in cases.items():
                with self.subTest(name=name):
                    (root / name).write_text(body, encoding="utf-8")
                    self.assertEqual(expected, coverage_gate.is_python_source(root / name))
            self.assertEqual("(outside every source)", coverage_gate.project_of(Path("elsewhere/x.py"), ["proj"]))


if __name__ == "__main__":
    unittest.main()

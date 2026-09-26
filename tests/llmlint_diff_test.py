#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier has no Nx workspace; this boundary test sits in tests/ beside llmlint_plugins_test.py and runs under `just test-llmlint-diff`.
"""Offline tests for `scripts/llmlint-diff.py`, the `lint-llm-diff` recipe's body.

Each case builds a real git repository with a base branch and a feature branch,
and runs the script as a subprocess inside it. The only stand-in is `llmlint`
itself, the paid judge: a stub on PATH answers `llmlint config` with an exclude
list and records every other invocation's arguments, exiting with the status the
case asks of it.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "llmlint-diff.py"

STUB = textwrap.dedent(
    """\
    #!/usr/bin/env python3
    import json, os, sys
    if sys.argv[1:] == ["config"]:
        print(json.dumps({"config": {"files": {"exclude": ["**/.git/**", "data/**/*.tsv"]}}}))
        sys.exit(0)
    with open(os.environ["STUB_LOG"], "a", encoding="utf-8") as log:
        log.write(json.dumps(sys.argv[1:]) + "\\n")
    files = [a for a in sys.argv[1:] if not a.startswith("-") and a not in ("git", "base")]
    code = int(os.environ.get("STUB_EXIT_" + (files[0].replace("/", "_").replace(".", "_") if files else "ALL"), "0"))
    if code < 0:
        os.kill(os.getpid(), -code)
    sys.exit(code)
    """
)


class LlmlintDiffTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory(prefix="llmlint-diff-test-")
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        bin_dir = self.root / "bin"
        bin_dir.mkdir()
        if os.name == "nt":
            # Windows runs no shebang; a `.cmd` shim is how an installed CLI is reached there.
            stub = self.root / "llmlint-stub.py"
            stub.write_text(STUB, encoding="utf-8")
            (bin_dir / "llmlint.cmd").write_text(
                f'@"{sys.executable}" "{stub}" %*\n@exit /b %ERRORLEVEL%\n', encoding="utf-8"
            )
        else:
            stub = bin_dir / "llmlint"
            stub.write_text(STUB, encoding="utf-8")
            stub.chmod(0o755)
        self.log = self.root / "calls.jsonl"
        self.env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}", "STUB_LOG": str(self.log)}
        self.git("init", "-q", "-b", "base")
        self.write("README.md", "base\n")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")
        self.git("checkout", "-q", "-b", "feature")

    def git(self, *args: str) -> None:
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
                       cwd=self.repo, check=True, capture_output=True)

    def write(self, path: str, text: str) -> None:
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def commit(self, files: dict[str, str]) -> None:
        for path, text in files.items():
            self.write(path, text)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "change")

    def run_script(self, *args: str, **exits: str) -> subprocess.CompletedProcess[str]:
        env = {**self.env, **{f"STUB_EXIT_{k}": v for k, v in exits.items()}}
        return subprocess.run([sys.executable, str(SCRIPT), "base", *args], cwd=self.repo, env=env,
                              capture_output=True, text=True)

    def calls(self) -> list[list[str]]:
        if not self.log.is_file():
            return []
        return [json.loads(line) for line in self.log.read_text(encoding="utf-8").splitlines()]

    def test_a_diff_that_fits_runs_the_one_plain_invocation(self) -> None:
        self.commit({"a.py": "x = 1\n", "b.md": "doc\n"})
        run = self.run_script("--rationales")
        self.assertEqual(0, run.returncode, run.stderr)
        self.assertEqual([["--diff", "git", "--diff-base", "base", "--rationales"]], self.calls())
        self.assertEqual("", run.stdout)

    def test_a_diff_over_budget_is_judged_in_path_ordered_batches_under_it(self) -> None:
        self.commit({"src/a.rs": "a" * 400, "src/b.rs": "b" * 400, "docs/c.md": "c" * 400,
                     "data/big/rows.tsv": "t" * 5000, "gone.md": "x\n"})
        self.git("rm", "-q", "gone.md")
        self.git("commit", "-q", "-m", "drop")
        run = self.run_script("--budget", "1500")
        self.assertEqual(0, run.returncode, run.stderr)
        base = ["--diff", "git", "--diff-base", "base"]
        # Each file weighs its 400 bytes plus a ~470-byte diff, so two do not fit
        # under 1,500; the excluded TSV and the deleted file are never named.
        self.assertEqual([[*base, "docs/c.md"], [*base, "src/a.rs"], [*base, "src/b.rs"]], self.calls())
        self.assertIn("llmlint-diff: batch 1/3: 1 file(s)", run.stdout)
        self.assertIn("llmlint-diff: batch 3/3: 1 file(s)", run.stdout)

    def test_files_that_fit_together_share_a_batch_and_an_oversized_one_stands_alone(self) -> None:
        self.commit({"a.md": "a", "b.md": "b", "c.md": "c" * 3000})
        run = self.run_script("--budget", "1200")
        self.assertEqual(0, run.returncode, run.stderr)
        named = [call[4:] for call in self.calls()]
        self.assertEqual([["a.md", "b.md"], ["c.md"]], named)

    def test_the_worst_batch_status_is_the_exit_status(self) -> None:
        self.commit({"a.md": "a" * 900, "b.md": "b" * 900, "c.md": "c" * 900})
        run = self.run_script("--budget", "1000", a_md="1", b_md="2")
        self.assertEqual(2, run.returncode)
        self.assertEqual(3, len(self.calls()), "a failing batch does not stop the batches after it")

    def test_a_batch_killed_before_its_verdict_fails_the_run(self) -> None:
        self.commit({"a.md": "a" * 900, "b.md": "b" * 900})
        run = self.run_script("--budget", "1000", b_md="-9")
        self.assertEqual(2, run.returncode, "a batch with no verdict is an error, never a pass")
        run = self.run_script(ALL="-9")
        self.assertEqual(2, run.returncode, "so is the single plain invocation")

    def test_every_changed_file_is_judged_in_exactly_one_batch(self) -> None:
        files = {f"d{n}/f{n}.md": "x" * (200 * n) for n in range(1, 9)}
        self.commit(files)
        self.assertEqual(0, self.run_script("--budget", "2500").returncode)
        named = [path for call in self.calls() for path in call[4:]]
        self.assertEqual(sorted(files), sorted(named))
        self.assertEqual(len(named), len(set(named)))

    def test_a_non_positive_budget_and_an_unknown_base_are_refused_with_the_fix(self) -> None:
        self.commit({"a.md": "a"})
        run = self.run_script("--budget", "0")
        self.assertNotEqual(0, run.returncode)
        self.assertIn("--budget must be a positive byte count", run.stderr)
        run = subprocess.run([sys.executable, str(SCRIPT), "no-such-base"], cwd=self.repo, env=self.env,
                             capture_output=True, text=True)
        self.assertNotEqual(0, run.returncode)
        self.assertIn("git fetch origin main", run.stderr)
        self.assertEqual([], self.calls())

    def test_the_recipe_runs_this_script(self) -> None:
        justfile = (REPO / "justfile").read_text(encoding="utf-8")
        self.assertIn('lint-llm-diff base="origin/main" *args:\n    python3 scripts/llmlint-diff.py {{base}} {{args}}',
                      justfile)


if __name__ == "__main__":
    unittest.main()

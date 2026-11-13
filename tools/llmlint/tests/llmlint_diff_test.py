#!/usr/bin/env python3
"""Offline tests for `tools/llmlint/llmlint-diff.py`, the `lint-llm-diff` recipe's body.

Each case builds a real git repository with a base branch and a feature branch,
and runs the script as a subprocess inside it. The only stand-in is `llmlint`
itself, the paid judge: a stub on PATH answers `llmlint config` with an exclude
list and records every other invocation's arguments, exiting with the status the
case asks of it.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "llmlint" / "llmlint-diff.py"

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
    key = files[0].replace("/", "_").replace(".", "_") if files else "ALL"
    # A comma list scripts successive calls for the same batch: "2,0" errors once, then passes.
    script = os.environ.get("STUB_EXIT_" + key, "0").split(",")
    counter = os.environ["STUB_LOG"] + "." + key
    seen = int(open(counter).read()) if os.path.exists(counter) else 0
    with open(counter, "w") as count:
        count.write(str(seen + 1))
    code = int(script[min(seen, len(script) - 1)])
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
        self.env = {
            **os.environ,
            "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
            "STUB_LOG": str(self.log),
            "LLMLINT_DIFF_RETRY_DELAY": "0",
        }
        self.git("init", "-q", "-b", "base")
        self.write("README.md", "base\n")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")
        self.git("checkout", "-q", "-b", "feature")

    def git(self, *args: str) -> None:
        subprocess.run(
            ["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], cwd=self.repo, check=True, capture_output=True
        )

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
        return subprocess.run(
            [sys.executable, str(SCRIPT), "base", *args], cwd=self.repo, env=env, capture_output=True, text=True
        )

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
        self.commit(
            {
                "src/a.rs": "a" * 400,
                "src/b.rs": "b" * 400,
                "docs/c.md": "c" * 400,
                "data/big/rows.tsv": "t" * 5000,
                "gone.md": "x\n",
            }
        )
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

    def test_a_name_git_would_quote_still_reaches_the_judge(self) -> None:
        # git quotes "a b.md" and "café.md" in its line-per-path output. The
        # `.cmd` shim that reaches the stub on Windows does not carry a non-ASCII
        # argument through intact (CI saw "caf\ufffd.md"), so the accented name
        # is asserted where the stub is the executable itself.
        names = ["a b.md"] if os.name == "nt" else ["a b.md", "café.md"]
        self.commit(dict.fromkeys(names, "a" * 400))
        run = self.run_script("--budget", "500")
        self.assertEqual(0, run.returncode, run.stderr)
        base = ["--diff", "git", "--diff-base", "base"]
        self.assertEqual([[*base, name] for name in names], self.calls())

    def test_files_that_fit_together_share_a_batch_and_an_oversized_one_stands_alone(self) -> None:
        self.commit({"a.md": "a", "b.md": "b", "c.md": "c" * 3000})
        run = self.run_script("--budget", "1200")
        self.assertEqual(0, run.returncode, run.stderr)
        named = [call[4:] for call in self.calls()]
        self.assertEqual([["a.md", "b.md"], ["c.md"]], named)

    def test_a_failed_rule_is_the_exit_status_even_beside_an_unanswered_batch(self) -> None:
        self.commit({"a.md": "a" * 900, "b.md": "b" * 900, "c.md": "c" * 900})
        run = self.run_script("--budget", "1000", a_md="1", b_md="2")
        self.assertEqual(1, run.returncode, "a rejection is a verdict, whatever else went unanswered")
        named = [call[4:] for call in self.calls()]
        # The rejected batch is never re-sent; the unanswered one is, twice.
        self.assertEqual([["a.md"], ["b.md"], ["b.md"], ["b.md"], ["c.md"]], named)
        self.assertIn("verification unavailable: 1 of 3 batch(es)", run.stderr)

    def test_a_batch_killed_before_its_verdict_fails_the_run(self) -> None:
        self.commit({"a.md": "a" * 900, "b.md": "b" * 900})
        run = self.run_script("--budget", "1000", b_md="-9")
        self.assertEqual(2, run.returncode, "a batch with no verdict is an error, never a pass")
        run = self.run_script(ALL="-9")
        self.assertEqual(2, run.returncode, "so is the single plain invocation")

    def test_an_unanswered_batch_is_retried_alone_until_the_judge_answers(self) -> None:
        self.commit({"a.md": "a" * 900, "b.md": "b" * 900, "c.md": "c" * 900})
        run = self.run_script("--budget", "1000", b_md="2,2,0")
        self.assertEqual(0, run.returncode, run.stdout + run.stderr)
        named = [call[4:] for call in self.calls()]
        self.assertEqual([["a.md"], ["b.md"], ["b.md"], ["b.md"], ["c.md"]], named, "answered batches are not replayed")
        self.assertIn("llmlint-diff: batch 2/3: no verdict from the judge; retry 1/2 on the same tree", run.stdout)
        self.assertIn("retry 2/2", run.stdout)
        self.assertNotIn("verification unavailable", run.stderr)

    def test_a_judge_still_unanswered_after_its_retries_is_unavailable_not_rejected(self) -> None:
        self.commit({"a.md": "a"})
        run = self.run_script(ALL="2")
        self.assertEqual(2, run.returncode)
        self.assertEqual(3, len(self.calls()), "the plain invocation is retried twice")
        self.assertIn("verification unavailable: 1 of 1 batch(es) got no verdict after 2 retries", run.stderr)

    def test_each_retry_waits_longer_than_the_last(self) -> None:
        self.commit({"a.md": "a"})
        env = {**self.env, "LLMLINT_DIFF_RETRY_DELAY": "0.3", "STUB_EXIT_ALL": "2,2,0"}
        started = time.monotonic()
        run = subprocess.run(
            [sys.executable, str(SCRIPT), "base"], cwd=self.repo, env=env, capture_output=True, text=True
        )
        self.assertEqual(0, run.returncode, run.stdout + run.stderr)
        self.assertIn("retry 1/2 on the same tree in 0.3s", run.stdout)
        self.assertIn("retry 2/2 on the same tree in 0.6s", run.stdout)
        self.assertGreaterEqual(time.monotonic() - started, 0.9, "the waits were 0.3 s and then 0.6 s")

    def test_a_rule_failure_is_never_retried(self) -> None:
        self.commit({"a.md": "a"})
        run = self.run_script(ALL="1")
        self.assertEqual(1, run.returncode)
        self.assertEqual(1, len(self.calls()))
        self.assertNotIn("retry", run.stdout)

    def test_a_retry_delay_that_is_not_seconds_is_refused_before_any_batch(self) -> None:
        self.commit({"a.md": "a"})
        env = {**self.env, "LLMLINT_DIFF_RETRY_DELAY": "soon"}
        run = subprocess.run(
            [sys.executable, str(SCRIPT), "base"], cwd=self.repo, env=env, capture_output=True, text=True
        )
        self.assertEqual(2, run.returncode)
        self.assertIn("LLMLINT_DIFF_RETRY_DELAY must be a number of seconds", run.stderr)
        self.assertEqual([], self.calls())

    def test_every_changed_file_is_judged_in_exactly_one_batch(self) -> None:
        files: dict[str, str] = {f"d{n}/f{n}.md": "x" * (200 * n) for n in range(1, 9)}
        self.commit(files)
        self.assertEqual(0, self.run_script("--budget", "2500").returncode)
        named = [path for call in self.calls() for path in call[4:]]
        self.assertEqual(sorted(files), sorted(named))
        self.assertEqual(len(named), len(set(named)))

    def test_a_non_positive_budget_and_an_unknown_base_are_refused_with_the_fix(self) -> None:
        self.commit({"a.md": "a"})
        run = self.run_script("--budget", "0")
        self.assertEqual(2, run.returncode)
        self.assertIn("--budget must be a positive byte count", run.stderr)
        run = subprocess.run(
            [sys.executable, str(SCRIPT), "no-such-base"], cwd=self.repo, env=self.env, capture_output=True, text=True
        )
        self.assertEqual(2, run.returncode, "a run that cannot be made is no rule failure")
        self.assertIn("git fetch origin main", run.stderr)
        self.assertEqual([], self.calls())

    @unittest.skipIf(os.name == "nt", "the failing git wrapper is a POSIX shell script")
    def test_a_per_file_diff_git_refuses_fails_the_run_before_any_batch(self) -> None:
        self.commit({"a.md": "a"})
        real_git = shutil.which("git")
        assert real_git
        wrapper = self.root / "failing-git"
        wrapper.mkdir()
        (wrapper / "git").write_text(
            "#!/bin/sh\n"
            'if [ "$1" = diff ] && [ "$3" = -- ]; then echo "fatal: simulated" >&2; exit 128; fi\n'
            f'exec "{real_git}" "$@"\n',
            encoding="utf-8",
        )
        (wrapper / "git").chmod(0o755)
        env = {**self.env, "PATH": f"{wrapper}{os.pathsep}{self.env['PATH']}"}
        run = subprocess.run(
            [sys.executable, str(SCRIPT), "base"], cwd=self.repo, env=env, capture_output=True, text=True
        )
        self.assertEqual(2, run.returncode)
        self.assertIn("-- a.md` exited 128: fatal: simulated", run.stderr)
        self.assertIn("run from inside the checkout, then retry", run.stderr)
        self.assertEqual([], self.calls(), "a size it could not measure must not reach the judge")

    def test_the_recipe_runs_this_script(self) -> None:
        justfile = (REPO / "justfile").read_text(encoding="utf-8")
        self.assertIn(
            'lint-llm-diff base="origin/main" *args:\n    python3 tools/llmlint/llmlint-diff.py {{base}} {{args}}',
            justfile,
        )


if __name__ == "__main__":
    unittest.main()

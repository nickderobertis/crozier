"""The required `lint` job's judged-lint steps, run as `.github/workflows/ci.yml` defines them.

Each case reads the job's steps from the workflow: the `judge` step and every
step whose condition reads its outputs. It runs their commands with bash, as
the runner does, honouring each step's `if:`, its environment, `$GITHUB_OUTPUT`
and GitHub's job-conclusion rules: a failed step fails the job and skips the
steps after it, and a cancelled run concludes the job `cancelled`, which is
neither the `success` that passes the merge gate nor the `failure` that reads
as rejected code.

The checkout is a scratch repository holding this repository's real `justfile`,
`llmlint.yml`, vendored rule plugins and `tools/llmlint/llmlint-diff.py`, with a
change on top of `origin/main`. The real `just` and the real `llmlint` run. Two
processes are doubled, both third-party boundaries: the judge harness
`oneharness`, which llmlint spawns through `LLMLINT_ONEHARNESS_BIN` and which
answers with its own JSON report, and the `gh` CLI, whose `run cancel` call is
recorded instead of reaching GitHub's API and ends the job the way the runner
does when the run is cancelled.

It needs llmlint, so it skips where the binary is absent unless
`CROZIER_REQUIRE_LLMLINT=1`, which the required `lint` job sets.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from llmlint_resolution_test import llmlint_binary, require_llmlint

REPO = Path(__file__).resolve().parents[3]
WORKFLOW = REPO / ".github" / "workflows" / "ci.yml"

# The judge harness: unavailable for the first FAKE_UNAVAILABLE runs, then an
# answer for every rule llmlint's schema asks about. Under FAKE_REJECT the
# first rule that can fail does, on the changed file, and its name is recorded.
ONEHARNESS = textwrap.dedent(
    """\
    import json, os, sys
    args = sys.argv[1:]
    if args == ["--version"]:
        print("oneharness 0.28.5")
        sys.exit(0)
    count_file = os.environ["FAKE_STATE"] + "/runs"
    runs = int(open(count_file).read()) if os.path.exists(count_file) else 0
    with open(count_file, "w") as handle:
        handle.write(str(runs + 1))
    if runs < int(os.environ.get("FAKE_UNAVAILABLE", "0")):
        reason = "`claude` could not reach its provider; nothing executed"
        print(json.dumps({
            "schema_version": "0.13",
            "fallback": {"ran": None, "fell_through": [{"harness": "claude-code", "reason": "unavailable", "detail": reason}],
                         "stopped_without_work": True},
            "results": [{"harness": "claude-code", "harness_id": "claude-code", "available": False, "status": "skipped",
                         "exit_code": None, "structured": None, "schema_valid": None, "stdout": "", "stderr": "",
                         "error": reason}],
        }))
        print("oneharness: no selected harness could be run", file=sys.stderr)
        sys.exit(1)
    schema = json.load(open(args[args.index("--schema") + 1], encoding="utf-8"))
    verdict = {}
    for name, rule in schema["properties"].items():
        answer = {"name": name, "rationale": "doubled judge"}
        rejected_file = os.environ["FAKE_STATE"] + "/rejected"
        reject = os.environ.get("FAKE_REJECT") == "1" and not os.path.exists(rejected_file)
        if "relevant" in rule["required"]:
            # A relevance-gated rule: judged only when the judge calls it relevant.
            answer["relevant"] = reject
        if "holds" in rule["required"] or reject:
            answer["holds"] = not reject
        if reject:
            with open(rejected_file, "w") as handle:
                handle.write(name)
            answer["violations"] = [{"file": os.environ["FAKE_CHANGED"], "line": 1, "message": "doubled rejection"}]
        verdict[name] = answer
    print(json.dumps({
        "schema_version": "0.13",
        "fallback": {"ran": "claude-code", "fell_through": [], "stopped_without_work": False},
        "results": [{"harness": "claude-code", "harness_id": "claude-code", "available": True, "status": "ok",
                     "exit_code": 0, "structured": verdict, "schema_valid": True, "schema_attempts": 1,
                     "schema_error": None, "stdout": "", "stderr": "", "error": None, "text": json.dumps(verdict)}],
    }))
    """
)

# GitHub's CLI: records each call, and a `run cancel` as the cancellation the runner acts on.
GH = textwrap.dedent(
    """\
    import json, os, sys
    with open(os.environ["FAKE_STATE"] + "/gh", "a", encoding="utf-8") as handle:
        handle.write(json.dumps(sys.argv[1:]) + "\\n")
    if sys.argv[1:3] == ["run", "cancel"]:
        open(os.environ["FAKE_STATE"] + "/cancelled", "w").close()
    """
)

CONDITION = re.compile(r"^\s*(github\.event_name|steps\.([\w-]+)\.outputs\.([\w-]+))\s*==\s*'([^']*)'\s*$")
EXPRESSION = re.compile(r"\$\{\{\s*([^}]+?)\s*\}\}")


class Conclusion(Enum):
    """A GitHub Actions job's conclusion, as the required check reports it."""

    SUCCESS = "success"
    FAILURE = "failure"
    CANCELLED = "cancelled"


@dataclass(frozen=True)
class Step:
    """The parts of a workflow step this runner reads."""

    name: str
    run: str = ""
    uses: str = ""
    id: str = ""
    condition: str | None = None
    env: dict[str, str] = field(default_factory=dict)
    continue_on_error: bool = False

    @classmethod
    def parse(cls, raw: dict[str, Any]) -> Step:
        return cls(
            name=str(raw.get("name", raw.get("uses", ""))),
            run=str(raw.get("run", "")),
            uses=str(raw.get("uses", "")),
            id=str(raw.get("id", "")),
            condition=None if "if" not in raw else str(raw["if"]),
            env={str(key): str(value) for key, value in (raw.get("env") or {}).items()},
            continue_on_error=bool(raw.get("continue-on-error", False)),
        )


def lint_steps() -> list[Step]:
    workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    return [Step.parse(raw) for raw in workflow["jobs"]["lint"]["steps"]]


def judged_steps() -> list[Step]:
    """The `judge` step and every later step whose condition reads its outputs."""
    steps = lint_steps()
    start = next(index for index, step in enumerate(steps) if step.id == "judge")
    return [steps[start], *(step for step in steps[start + 1 :] if "steps.judge." in (step.condition or ""))]


class Job:
    """One run of the judged-lint steps, concluded as GitHub concludes a job."""

    def __init__(self, checkout: Path, env: dict[str, str], state: Path) -> None:
        self.checkout = checkout
        self.env = env
        self.state = state
        self.outputs: dict[str, dict[str, str]] = {}
        self.log = ""
        self.conclusion = Conclusion.SUCCESS

    def condition(self, expression: str) -> bool:
        """A step's `if:`: the conjunction of equalities the judged steps use, after the implicit success()."""
        if self.conclusion is not Conclusion.SUCCESS:
            return False
        for term in expression.split("&&"):
            match = CONDITION.match(term)
            if match is None:
                raise AssertionError(f"this runner does not evaluate the condition {term.strip()!r}; extend it")
            if match.group(1) == "github.event_name":
                actual = "pull_request"
            else:
                actual = self.outputs.get(match.group(2), {}).get(match.group(3), "")
            if actual != match.group(4):
                return False
        return True

    def expand(self, value: str) -> str:
        known = {
            "secrets.CLAUDE_CODE_OAUTH_TOKEN": "doubled-credential",
            "github.token": "doubled-token",
        }

        def substitute(match: re.Match[str]) -> str:
            if match.group(1) not in known:
                raise AssertionError(f"this runner has no value for ${{{{ {match.group(1)} }}}}; extend it")
            return known[match.group(1)]

        return EXPRESSION.sub(substitute, value)

    def run(self, steps: list[Step]) -> None:
        for number, step in enumerate(steps):
            if step.condition is not None and not self.condition(step.condition):
                continue
            if step.condition is None and self.conclusion is not Conclusion.SUCCESS:
                continue
            output = self.state / f"output-{number}"
            output.touch()
            script = self.state / f"step-{number}.sh"
            script.write_text(self.expand(step.run), encoding="utf-8")
            env = {
                **self.env,
                **{key: self.expand(value) for key, value in step.env.items()},
                "GITHUB_OUTPUT": str(output),
            }
            log = self.state / f"log-{number}"
            with log.open("w", encoding="utf-8") as handle:
                process = subprocess.Popen(
                    ["bash", "--noprofile", "--norc", "-eo", "pipefail", str(script)],
                    cwd=self.checkout,
                    env=env,
                    stdout=handle,
                    stderr=subprocess.STDOUT,
                    start_new_session=True,
                )
                status = self.wait(process)
            self.log += log.read_text(encoding="utf-8")
            if step.id:
                lines = output.read_text(encoding="utf-8").splitlines()
                self.outputs[step.id] = dict(line.split("=", 1) for line in lines if "=" in line)
            if status is None:
                self.conclusion = Conclusion.CANCELLED
                return
            if status != 0 and not step.continue_on_error:
                self.conclusion = Conclusion.FAILURE

    def wait(self, process: subprocess.Popen[bytes]) -> int | None:
        """The step's exit status, or None once the run is cancelled, which stops the step as the runner does."""
        deadline = time.monotonic() + 600
        while time.monotonic() < deadline:
            if (self.state / "cancelled").exists():
                os.killpg(process.pid, signal.SIGTERM)
                process.wait()
                return None
            status = process.poll()
            if status is not None:
                return status
            time.sleep(0.2)
        os.killpg(process.pid, signal.SIGKILL)
        raise AssertionError("a judged-lint step outlived 600 s")


class TheJudgedStepsAreTheWorkflowsOwn(unittest.TestCase):
    def test_the_judge_step_and_the_step_that_withholds_its_verdict_are_read_from_ci_yml(self) -> None:
        steps = judged_steps()
        self.assertEqual("Judge the changed files", steps[0].name)
        self.assertIn("just lint-llm-diff origin/main", steps[0].run)
        self.assertTrue(
            any("gh run cancel" in step.run for step in steps[1:]),
            "no step after the judge withholds the lane's verdict",
        )
        self.assertEqual(steps[-1], lint_steps()[-1], "the verdict is withheld only after every other step ran")
        permissions = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))["jobs"]["lint"]["permissions"]
        self.assertEqual("write", permissions.get("actions"), "cancelling the run needs actions: write")


@unittest.skipIf(os.name == "nt", "the job runs on ubuntu-latest; its steps are bash")
@unittest.skipIf(
    llmlint_binary() is None and not require_llmlint(),
    "llmlint is not installed (`just setup-llmlint`)",
)
class TheRequiredLintJobsConclusion(unittest.TestCase):
    """Drive the judged-lint steps over a changed checkout with the judge doubled."""

    CHANGED = "tools/example/report.py"

    def setUp(self) -> None:
        llmlint = llmlint_binary()
        if llmlint is None:
            self.fail("CROZIER_REQUIRE_LLMLINT=1 but llmlint is not installed — run `just setup-llmlint`")
        if shutil.which("just") is None:
            self.fail("just is not on PATH — run `just bootstrap`")
        temporary = tempfile.TemporaryDirectory(prefix="judged-lint-job-")
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        self.checkout = root / "checkout"
        self.state = root / "state"
        doubles = root / "bin"
        for directory in (self.checkout, self.state, doubles):
            directory.mkdir()
        for path in ("justfile", "llmlint.yml", "oneharness.toml", "tools/llmlint/llmlint-diff.py"):
            target = self.checkout / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / path, target)
        shutil.copytree(REPO / "llmlint-plugins", self.checkout / "llmlint-plugins")
        self.git("init", "-q", "-b", "main")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")
        self.git("update-ref", "refs/remotes/origin/main", "HEAD")
        changed = self.checkout / self.CHANGED
        changed.parent.mkdir(parents=True)
        changed.write_text('"""Report a total."""\n\n\ndef total(values: list[int]) -> int:\n    return sum(values)\n')
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "change")
        for name, body in (("oneharness", ONEHARNESS), ("gh", GH)):
            double = doubles / name
            double.write_text(f"#!{sys.executable}\n{body}", encoding="utf-8")
            double.chmod(0o755)
        self.env = {
            **os.environ,
            "PATH": os.pathsep.join([str(doubles), str(Path(llmlint).parent), os.environ.get("PATH", "")]),
            "LLMLINT_ONEHARNESS_BIN": str(doubles / "oneharness"),
            "LLMLINT_DIFF_RETRY_DELAY": "0",
            "XDG_STATE_HOME": str(root / "xdg-state"),
            "XDG_CACHE_HOME": str(root / "xdg-cache"),
            "GITHUB_RUN_ID": "4242",
            "GITHUB_REPOSITORY": "example/crozier",
            "FAKE_STATE": str(self.state),
            "FAKE_CHANGED": self.CHANGED,
        }

    def git(self, *args: str) -> None:
        subprocess.run(
            ["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
            cwd=self.checkout,
            check=True,
            capture_output=True,
        )

    def job(self, **fake: str) -> Job:
        job = Job(self.checkout, {**self.env, **fake}, self.state)
        job.run(judged_steps())
        return job

    def gh_calls(self) -> list[list[str]]:
        calls = self.state / "gh"
        if not calls.exists():
            return []
        return [json.loads(line) for line in calls.read_text(encoding="utf-8").splitlines()]

    def test_batches_unavailable_and_then_answered_conclude_success(self) -> None:
        job = self.job(FAKE_UNAVAILABLE="2")
        self.assertIs(Conclusion.SUCCESS, job.conclusion, job.log)
        self.assertIn("no verdict from the judge; retry 1/2 on the same tree", job.log)
        self.assertNotIn("verification unavailable", job.log)
        self.assertEqual([], self.gh_calls(), "an answered judge withholds nothing")

    def test_batches_unanswered_after_the_retries_conclude_neither_success_nor_failure(self) -> None:
        job = self.job(FAKE_UNAVAILABLE="1000")
        self.assertIs(Conclusion.CANCELLED, job.conclusion, job.log)
        self.assertIn("retry 2/2", job.log)
        self.assertIn("verification unavailable", job.log)
        self.assertIn("Verification unavailable: the judged lint got no verdict", job.log)
        self.assertNotRegex(job.log, r"(?m)^FAIL ", "an unanswered judge names no rejected rule")
        self.assertEqual([["run", "cancel", "4242", "--repo", "example/crozier"]], self.gh_calls())

    def test_a_rule_violation_concludes_failure_and_names_the_rule(self) -> None:
        job = self.job(FAKE_REJECT="1")
        self.assertIs(Conclusion.FAILURE, job.conclusion, job.log)
        rejected = (self.state / "rejected").read_text(encoding="utf-8")
        self.assertRegex(job.log, rf"(?m)^FAIL {re.escape(rejected)}$")
        self.assertIn(f"{self.CHANGED}:1: doubled rejection", job.log)
        self.assertNotIn("verification unavailable", job.log)
        self.assertEqual([], self.gh_calls(), "a rejection is a verdict, never withheld")


if __name__ == "__main__":
    unittest.main()

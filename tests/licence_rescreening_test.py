"""Boundary coverage for the screening-record gate.

`docs/licence-rescreening.md` is the only record of which licence-blocked
candidates the widened corpus rule admits, and the node that registers
witnesses works from it. A line that omits its verdict, its reason, its pinned
reference, either half of the Fern screen, or that names a coverage row the
region files do not carry reads exactly like a screening that happened, so
`scripts/licence-rescreening-check.py` refuses it.

These tests drive the REAL script over the REAL repository — the invocation
`just lint-licence-rescreening` runs — and then, for each demand the gate
makes, plant a record breaking exactly that demand and require the failure to
name it. Without the planted half, "the gate passes" would be
indistinguishable from "the gate matches nothing at all".

Run: `just test-licence-rescreening` (part of `just check`).
"""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "licence-rescreening-check.py"
RECORD = "docs/licence-rescreening.md"

# One line that satisfies every demand, for the planted cases to break one at a
# time. `format-ipv6` is a real `schemas` region key.
GOOD = (
    "| `example/repo` `openapi.yaml` | commit `"
    + "0" * 40
    + "` | MIT | admitted | the widened rule reaches every grant of"
    " redistribution, and this is one | `format-ipv6` = **1** |"
    " `fern check` at CLI 5.114.1 → **exit 0**, `Found 0 errors` |"
    " `fern generate --group python-sdk --preview` at 5.20.0 → **exit 0**,"
    " 12 `.py` files |"
)
HEADER = (
    "| candidate | pinned ref | licence | admission |"
    " why the rule reaches it or does not | rows it declares |"
    " document check | generate |\n"
    "|---|---|---|---|---|---|---|---|"
)


def load_gate():
    spec = importlib.util.spec_from_file_location("licence_rescreening_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_gate(root: Path = REPO) -> subprocess.CompletedProcess[str]:
    """The gate exactly as `just lint-licence-rescreening` runs it."""
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=root,
        capture_output=True,
        text=True,
    )


class TheGateHoldsTheFinishedRecord(unittest.TestCase):
    def test_the_committed_record_passes(self) -> None:
        result = run_gate()
        self.assertEqual(
            result.returncode, 0, f"{RECORD} does not hold:\n{result.stderr}"
        )

    def test_it_is_quiet_on_success(self) -> None:
        result = run_gate()
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")

    def test_the_record_screens_the_certain_candidate(self) -> None:
        """LORIS is the one candidate the task named as already settled."""
        text = (REPO / RECORD).read_text(encoding="utf-8")
        self.assertIn("aces/Loris", text)
        self.assertIn("3305a00312178ea75f135be1564beaf222b25822", text)


class TheGateStillDiscriminates(unittest.TestCase):
    """Plant a record breaking one demand; require a failure naming it."""

    def plant(self, rows: str) -> Path:
        """A tree whose record is `rows`, sharing the real region files."""
        root = Path(tempfile.mkdtemp(prefix="licence-rescreening-probe-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        (root / "docs" / "openapi-surface").mkdir(parents=True)
        for region in load_gate().REGIONS:
            source = REPO / "docs" / "openapi-surface" / f"{region}.md"
            (root / "docs" / "openapi-surface" / f"{region}.md").write_text(
                source.read_text(encoding="utf-8"), encoding="utf-8"
            )
        (root / RECORD).write_text(
            f"# probe\n\n## The record\n\n{HEADER}\n{rows}\n", encoding="utf-8"
        )
        (root / "scripts").mkdir()
        (root / "scripts" / SCRIPT.name).write_text(
            SCRIPT.read_text(encoding="utf-8"), encoding="utf-8"
        )
        return root

    def gate_over(self, rows: str) -> subprocess.CompletedProcess[str]:
        root = self.plant(rows)
        return subprocess.run(
            [sys.executable, str(root / "scripts" / SCRIPT.name)],
            cwd=root,
            capture_output=True,
            text=True,
        )

    def test_the_reference_line_passes_so_each_planted_break_is_the_break(self) -> None:
        result = self.gate_over(GOOD)
        self.assertEqual(
            result.returncode,
            0,
            f"the reference line does not pass, so the cases below prove"
            f" nothing:\n{result.stderr}",
        )

    def test_a_missing_verdict_fails(self) -> None:
        result = self.gate_over(GOOD.replace("| admitted |", "|  |"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("admission is", result.stderr)

    def test_a_verdict_outside_the_two_words_fails(self) -> None:
        result = self.gate_over(GOOD.replace("| admitted |", "| maybe |"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("'maybe'", result.stderr)

    def test_a_verdict_with_no_reason_fails(self) -> None:
        result = self.gate_over(
            GOOD.replace(
                "the widened rule reaches every grant of redistribution,"
                " and this is one",
                "yes",
            )
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("carries no reason", result.stderr)

    def test_an_unpinned_candidate_fails(self) -> None:
        result = self.gate_over(GOOD.replace("commit `" + "0" * 40 + "`", "HEAD"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("pinned ref", result.stderr)

    def test_no_immutable_ref_passes_when_it_says_why(self) -> None:
        result = self.gate_over(
            GOOD.replace(
                "commit `" + "0" * 40 + "`",
                "none — SwaggerHub exposes only a mutable version reference",
            )
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_a_missing_document_check_fails(self) -> None:
        result = self.gate_over(
            GOOD.replace("`fern check` at CLI 5.114.1 → **exit 0**, `Found 0 errors`", "")
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("`fern check`", result.stderr)

    def test_a_document_check_with_no_outcome_fails(self) -> None:
        result = self.gate_over(GOOD.replace("→ **exit 0**, `Found 0 errors`", "run"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("carries no `fern check` result", result.stderr)

    def test_a_missing_generate_fails(self) -> None:
        result = self.gate_over(
            GOOD.replace(
                "`fern generate --group python-sdk --preview` at 5.20.0 →"
                " **exit 0**, 12 `.py` files",
                "",
            )
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("`fern generate`", result.stderr)

    def not_run(self, check_reason: str, generate_reason: str) -> str:
        """The reference line with both Fern halves recorded as `not run`."""
        return GOOD.replace(
            "`fern check` at CLI 5.114.1 → **exit 0**, `Found 0 errors`",
            f"`fern check` not run — {check_reason}",
        ).replace(
            "`fern generate --group python-sdk --preview` at 5.20.0 →"
            " **exit 0**, 12 `.py` files",
            f"`fern generate` not run — {generate_reason}",
        )

    def test_not_run_with_a_reason_is_an_acceptable_result(self) -> None:
        """A blocked candidate is screened by the licence, not by Fern."""
        result = self.gate_over(
            self.not_run(
                "nothing grants redistribution, so Fern's verdict could not matter",
                "the same licence bar, and a generate buys nothing here",
            )
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_not_run_with_no_reason_fails(self) -> None:
        result = self.gate_over(
            self.not_run(
                "nothing grants redistribution, so Fern's verdict could not matter",
                "the same",
            )
        )
        self.assertEqual(result.returncode, 1, "`not run — the same` is not a reason")
        self.assertIn("carries no `fern generate` result", result.stderr)

    def test_an_unknown_coverage_row_fails(self) -> None:
        result = self.gate_over(GOOD.replace("`format-ipv6`", "`format-ipv7`"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("format-ipv7", result.stderr)
        self.assertIn("no region file carries", result.stderr)

    def test_declaring_nothing_must_say_so(self) -> None:
        result = self.gate_over(GOOD.replace("`format-ipv6` = **1**", "—"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("does not say `none`", result.stderr)

    def test_a_short_row_fails(self) -> None:
        result = self.gate_over(GOOD.replace(" | MIT |", " |"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("cells, not 8", result.stderr)


class TheRecordIsWhereTheGateSaysItIs(unittest.TestCase):
    def test_a_record_with_no_table_fails(self) -> None:
        root = Path(tempfile.mkdtemp(prefix="licence-rescreening-probe-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        (root / "docs").mkdir(parents=True)
        (root / RECORD).write_text("# probe\n\nno table here\n", encoding="utf-8")
        (root / "scripts").mkdir()
        (root / "scripts" / SCRIPT.name).write_text(
            SCRIPT.read_text(encoding="utf-8"), encoding="utf-8"
        )
        result = subprocess.run(
            [sys.executable, str(root / "scripts" / SCRIPT.name)],
            cwd=root,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("records nothing", result.stderr)

    def test_the_region_keys_it_validates_against_are_the_real_ones(self) -> None:
        keys = load_gate().region_keys(REPO)
        self.assertGreater(len(keys), 300, "the region walk found almost no keys")
        self.assertEqual(keys["parameter-style-spacedelimited-query-scalar"], "parameters")
        self.assertEqual(keys["media-type-range"], "bodies-media")
        self.assertEqual(keys["duplicate-normalized-paths"], "document-paths")
        self.assertEqual(keys["http-hoba"], "security")
        self.assertEqual(keys["reference-summary"], "oas31-extensions")


class TheGateAndItsTestsAreBothInTheDeterministicTier(unittest.TestCase):
    def test_check_runs_both(self) -> None:
        justfile = (REPO / "justfile").read_text(encoding="utf-8").splitlines()
        gate = next(line for line in justfile if line.startswith("check:")).split()
        self.assertIn("lint-licence-rescreening", gate)
        self.assertIn("test-licence-rescreening", gate)
        self.assertEqual(
            justfile[justfile.index("lint-licence-rescreening:") + 1].strip(),
            f"python3 {SCRIPT.relative_to(REPO).as_posix()}",
        )
        self.assertEqual(
            justfile[justfile.index("test-licence-rescreening:") + 1].strip(),
            f"python3 tests/{Path(__file__).name}",
        )


if __name__ == "__main__":
    unittest.main()

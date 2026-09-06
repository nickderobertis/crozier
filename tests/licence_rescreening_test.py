"""Boundary coverage for the screening-record gate.

`docs/licence-rescreening.md` is the only record of which licence-blocked
candidates the widened corpus rule admits, and the node that registers
witnesses works from it. Two ways it can lie: a line can omit half its
screening, and a line can cover several documents at once so that the ones
nobody screened are hidden inside a plural. `scripts/licence-rescreening-check.py`
refuses both, and derives the candidate set from the six region ledgers rather
than from the record's own account of its scope.

These tests drive the REAL script. `TheGateHoldsTheFinishedRecord` runs it over
the REAL repository — the invocation `just lint-licence-rescreening` runs. The
mutation cases plant a small but REAL tree (six region files with the sections
the gate reads, and a record answering them) and break one demand at a time,
requiring the failure to name it: without that half, "the gate passes" would be
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
SHA = "0" * 40
OTHER_SHA = "1" * 40

RECORD_HEADER = (
    "| candidate | source | pinned ref | licence | admission |"
    " why the rule reaches it or does not | rows it declares |"
    " document check | generate |\n"
    "|---|---|---|---|---|---|---|---|---|"
)
ENTRIES = (
    "## Entries\n\n"
    "| key | oas | spec location | category | evidence | crozier sites |"
    " why bytes could move | settlement |\n"
    "|---|---|---|---|---|---|---|---|\n"
    "| `format-ipv6` | 3.1 | Schema Object.format | gap | none | none |"
    " none | FIXTURE |\n"
)
LEDGER_HEADER = (
    "| candidate | ref | license | counted in the fetched bytes |"
    " what became of it |\n|---|---|---|---|---|"
)


def ledger_row(candidate: str) -> str:
    return (
        f"| {candidate} | commit `{SHA}` | none declared | `format: ipv6`=1 |"
        " not a witness — nothing grants redistribution |"
    )


def record_line(
    candidate: str = "`example/one` `openapi.yaml`",
    source: str = "`schemas.md:{row}`",
    ref: str = (
        "commit `" + SHA + "`, at"
        " `https://raw.githubusercontent.com/example/one/" + SHA + "/openapi.yaml`"
        " (1,024 bytes, MD5 `" + "a" * 32 + "`)"
    ),
    licence: str = "none declared",
    verdict: str = "still-blocked",
    why: str = "nothing grants redistribution, so the widening reaches nothing",
    declares: str = "`format-ipv6` = **1**",
    checked: str = "`fern check` at CLI 5.114.1 → **exit 0**, `All checks passed`",
    generated: str = (
        "`fern generate --group python-sdk --preview` at 5.20.0 → **exit 0**,"
        " 12 `.py` files"
    ),
) -> str:
    cells = [
        candidate,
        source,
        ref,
        licence,
        verdict,
        why,
        declares,
        checked,
        generated,
    ]
    return "| " + " | ".join(cells) + " |"


def load_gate():
    spec = importlib.util.spec_from_file_location("licence_rescreening_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_gate(root: Path = REPO, script: Path = SCRIPT):
    """The gate exactly as `just lint-licence-rescreening` runs it."""
    return subprocess.run(
        [sys.executable, str(script)], cwd=root, capture_output=True, text=True
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

    def test_no_line_records_a_fern_run_as_not_run(self) -> None:
        gate = load_gate()
        _, rows = gate.record_rows((REPO / RECORD).read_text(encoding="utf-8"))
        self.assertGreater(len(rows), 60, "the record lost most of its lines")
        for line, cells in rows:
            self.assertNotIn(
                "not run", " ".join(cells[-2:]), f"{RECORD}:{line} skips a Fern run"
            )


class TheAuthoritativeSetComesFromTheRegionLedgers(unittest.TestCase):
    """The gate derives its scope; these hold that derivation to the real files."""

    def test_the_real_region_files_yield_the_real_candidate_set(self) -> None:
        gate = load_gate()
        documents, rows = gate.authoritative(REPO)
        self.assertGreater(len(documents), 60)
        self.assertGreater(len(rows), 40)
        for expected in (
            "aces/Loris:modules/dataquery/static/schema.yml",
            "drakkan/sftpgo:openapi/openapi.yaml",
            "https://api.short.io/openapi.json",
            "fulfillment.com/2.0",
            "DANIELCHURCHLEY/vehicle-api/1.0.0",
            "curedao/curedao-monorepo",
        ):
            self.assertIn(expected, documents, f"{expected} fell out of the set")
        for expected in ("security.md:502", "parameters.md:404", "schemas.md:932"):
            self.assertIn(expected, rows, f"{expected} fell out of the in-scope rows")

    def test_a_pooled_region_row_splits_into_its_members(self) -> None:
        """The ten SwaggerHub documents of one `schemas.md` row are ten."""
        gate = load_gate()
        row = (REPO / "docs/openapi-surface/schemas.md").read_text(
            encoding="utf-8"
        ).split("\n")[931]
        candidate = row.strip().strip("|").split(" | ")[0]
        self.assertEqual(len(gate.documents_in(candidate)), 10)

    def test_a_settled_witness_row_is_not_in_scope(self) -> None:
        """`witness-found` rows are answers, not blocked candidates."""
        gate = load_gate()
        _, rows = gate.authoritative(REPO)
        self.assertNotIn("bodies-media.md:268", rows)


class TheGateStillDiscriminates(unittest.TestCase):
    """Plant a real tree, break one demand, require a failure naming it."""

    def plant(self, ledger: list[str], lines, extra_region: str = "") -> Path:
        root = Path(tempfile.mkdtemp(prefix="licence-rescreening-probe-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        surface = root / "docs" / "openapi-surface"
        surface.mkdir(parents=True)
        gate = load_gate()
        body = (
            "# probe\n\n"
            + ENTRIES
            + "\n### Witness search (issue #188)\n\n"
            + LEDGER_HEADER
            + "\n"
            + "\n".join(ledger)
            + "\n"
            + extra_region
        )
        for region in gate.REGIONS:
            text = body if region == "schemas" else "# probe\n\n" + ENTRIES
            (surface / f"{region}.md").write_text(text, encoding="utf-8")
        rows = {}
        schemas = (surface / "schemas.md").read_text(encoding="utf-8").split("\n")
        for index, line in enumerate(schemas, start=1):
            if line in ledger:
                rows[ledger.index(line)] = index
        rendered = [
            line.format(**{f"row{n}": rows[n] for n in rows}, row=rows.get(0, 0))
            for line in lines
        ]
        (root / RECORD).write_text(
            "# probe\n\n## The record\n\n"
            + RECORD_HEADER
            + "\n"
            + "\n".join(rendered)
            + "\n",
            encoding="utf-8",
        )
        (root / "scripts").mkdir()
        script = root / "scripts" / SCRIPT.name
        script.write_text(SCRIPT.read_text(encoding="utf-8"), encoding="utf-8")
        return root

    def gate_over(self, ledger, lines, extra_region: str = ""):
        root = self.plant(ledger, lines, extra_region)
        return run_gate(root, root / "scripts" / SCRIPT.name)

    def one(self, **overrides):
        return [ledger_row("`example/one` `openapi.yaml`")], [record_line(**overrides)]

    def test_the_reference_tree_passes_so_each_planted_break_is_the_break(self) -> None:
        result = self.gate_over(*self.one())
        self.assertEqual(
            result.returncode,
            0,
            f"the reference tree does not pass, so the cases below prove"
            f" nothing:\n{result.stderr}",
        )

    def test_a_grouped_line_fails(self) -> None:
        """Two documents on one line is the failure this record exists to avoid."""
        ledger = [ledger_row("`example/one` `openapi.yaml`; `example/two` `api.json`")]
        lines = [
            record_line(candidate="`example/one` `openapi.yaml`; `example/two` `api.json`")
        ]
        result = self.gate_over(ledger, lines)
        self.assertEqual(result.returncode, 1)
        self.assertIn("names 2 documents, not 1", result.stderr)

    def test_an_omitted_member_of_a_pool_fails(self) -> None:
        ledger = [ledger_row("`example/one` `openapi.yaml`; `example/two` `api.json`")]
        result = self.gate_over(ledger, [record_line()])
        self.assertEqual(result.returncode, 1)
        self.assertIn("example/two:api.json", result.stderr)
        self.assertIn("no line of the record screens", result.stderr)

    def test_splitting_the_pool_passes(self) -> None:
        ledger = [ledger_row("`example/one` `openapi.yaml`; `example/two` `api.json`")]
        lines = [
            record_line(),
            record_line(candidate="`example/two` `api.json`"),
        ]
        result = self.gate_over(ledger, lines)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_a_duplicated_document_fails(self) -> None:
        result = self.gate_over(
            [ledger_row("`example/one` `openapi.yaml`")],
            [record_line(), record_line()],
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("is already recorded at line", result.stderr)

    def test_an_uncited_in_scope_row_fails(self) -> None:
        ledger = [
            ledger_row("`example/one` `openapi.yaml`"),
            ledger_row("`example/two` `api.json`"),
        ]
        lines = [record_line(), record_line(candidate="`example/two` `api.json`")]
        # Both documents are screened, but the second line cites the first row.
        result = self.gate_over(ledger, [line.replace("{row1}", "{row}") for line in lines])
        self.assertEqual(result.returncode, 1)
        self.assertIn("no line of the record cites it", result.stderr)

    def test_a_citation_that_does_not_name_the_document_fails(self) -> None:
        ledger = [
            ledger_row("`example/one` `openapi.yaml`"),
            ledger_row("`example/two` `api.json`"),
        ]
        lines = [
            record_line(source="`schemas.md:{row1}`"),
            record_line(candidate="`example/two` `api.json`", source="`schemas.md:{row1}`"),
        ]
        result = self.gate_over(ledger, lines)
        self.assertEqual(result.returncode, 1)
        self.assertIn("does not name example/one:openapi.yaml", result.stderr)

    def test_a_missing_source_citation_fails(self) -> None:
        result = self.gate_over(*self.one(source="the schemas ledger"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("no `<region>.md:<line>` source citation", result.stderr)

    def test_a_citation_that_is_not_a_table_row_fails(self) -> None:
        result = self.gate_over(*self.one(source="`schemas.md:1`"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("is not a table row", result.stderr)

    def test_a_verdict_outside_the_two_words_fails(self) -> None:
        result = self.gate_over(*self.one(verdict="maybe"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("'maybe'", result.stderr)

    def test_a_verdict_with_no_reason_fails(self) -> None:
        result = self.gate_over(*self.one(why="yes"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("carries no reason", result.stderr)

    def test_a_ref_with_no_fetch_url_fails(self) -> None:
        result = self.gate_over(*self.one(ref=f"commit `{SHA}`"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("names no fetch URL", result.stderr)

    def test_a_ref_with_no_fingerprint_fails(self) -> None:
        result = self.gate_over(
            *self.one(ref=f"commit `{SHA}`, at `https://example.test/openapi.yaml`")
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("fingerprint", result.stderr)

    def test_an_unpinned_ref_fails(self) -> None:
        result = self.gate_over(
            *self.one(
                ref="at `https://example.test/openapi.yaml` (1,024 bytes, MD5 `"
                + "a" * 32
                + "`)"
            )
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("40-character commit", result.stderr)

    def test_no_immutable_ref_passes_when_it_says_why(self) -> None:
        result = self.gate_over(
            *self.one(
                ref="no immutable ref — SwaggerHub republishes a version in place,"
                " so the bytes can change without the address changing; fetched at"
                " `https://example.test/swagger.json` (1,024 bytes, MD5 `"
                + "a" * 32
                + "`)"
            )
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_a_fern_check_recorded_as_not_run_fails(self) -> None:
        result = self.gate_over(
            *self.one(checked="`fern check` not run — the licence blocks it first")
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("records `fern check` as `not run`", result.stderr)

    def test_a_generate_recorded_as_not_run_fails(self) -> None:
        result = self.gate_over(
            *self.one(
                generated="`fern generate --group python-sdk --preview` not run —"
                " the same licence bar"
            )
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("as `not run`", result.stderr)

    def test_a_fern_run_with_no_exit_status_fails(self) -> None:
        result = self.gate_over(
            *self.one(checked="`fern check` at CLI 5.114.1 → `All checks passed`")
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("carries no `fern check` exit status", result.stderr)

    def test_a_missing_generate_command_fails(self) -> None:
        result = self.gate_over(*self.one(generated="**exit 0**, 12 `.py` files"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("names no `fern generate", result.stderr)

    def test_an_unknown_coverage_row_fails(self) -> None:
        result = self.gate_over(*self.one(declares="`format-ipv7` = **1**"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("format-ipv7", result.stderr)
        self.assertIn("no region file carries", result.stderr)

    def test_declaring_nothing_must_say_so(self) -> None:
        result = self.gate_over(*self.one(declares="—"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("does not say `none`", result.stderr)

    def test_a_short_row_fails(self) -> None:
        ledger, lines = self.one()
        result = self.gate_over(ledger, [lines[0].replace(" | none declared |", " |", 1)])
        self.assertEqual(result.returncode, 1)
        self.assertIn("cells, not 9", result.stderr)


class TheRecordIsWhereTheGateSaysItIs(unittest.TestCase):
    def test_a_record_with_no_table_fails(self) -> None:
        root = Path(tempfile.mkdtemp(prefix="licence-rescreening-probe-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        (root / "docs").mkdir(parents=True)
        (root / RECORD).write_text("# probe\n\nno table here\n", encoding="utf-8")
        (root / "scripts").mkdir()
        script = root / "scripts" / SCRIPT.name
        script.write_text(SCRIPT.read_text(encoding="utf-8"), encoding="utf-8")
        result = run_gate(root, script)
        self.assertEqual(result.returncode, 1)
        self.assertIn("records nothing", result.stderr)

    def test_the_region_keys_it_validates_against_are_the_real_ones(self) -> None:
        keys = load_gate().region_keys(REPO)
        self.assertGreater(len(keys), 300, "the region walk found almost no keys")
        self.assertEqual(
            keys["parameter-style-spacedelimited-query-scalar"], "parameters"
        )
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

#!/usr/bin/env python3
"""Boundary tests for `just fixtures-coverage` (`just test-fixtures-coverage`).

The recipe's whole value is that its numbers are *honest*, so these drive the
real thing rather than a stand-in: the real `scripts/fixtures-coverage.sh`, the
real `cargo nextest` selection boundary, the real instrumented `cargo llvm-cov`
run over the real filesystem, and the real spawned `crozier` binary. Nothing is
mocked. The end-to-end cases pass a SCOPE so they measure two or three tests
instead of the whole corpus; that is the same code path the unscoped recipe runs.
"""

from __future__ import annotations

import atexit
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "fixtures-coverage.sh"
REPORTER = REPO / "scripts" / "fixtures-coverage-report.py"

# Vendored (never fetched) goldens, so the scoped runs stay offline.
OFFLINE_GOLDEN = "query_parameters_matches_fern_output_byte_for_byte"
JOURNEY = "help_lists_generate"
UNIT = "wrap::tests::flat_atom_is_verbatim"
OFFLINE_SCOPE = (
    f"test(={OFFLINE_GOLDEN}) or test(={JOURNEY}) or test(={UNIT})"
)


def load_reporter():
    spec = importlib.util.spec_from_file_location("fixtures_coverage_report", REPORTER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


reporter = load_reporter()


def nextest_list(expression: str) -> set[tuple[str, str]]:
    """(binary id, test name) cargo-nextest actually selects — the real boundary.

    Keyed on the binary too: `generation.rs` and `e2e.rs` share some test names,
    and collapsing them would make the tiers look like they overlap.
    """
    listing = subprocess.run(
        ["cargo", "nextest", "list", "--locked", "-E", expression],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    selected = set()
    for line in listing.splitlines():
        if line.strip():
            binary, name = line.split(maxsplit=1)
            selected.add((binary, name))
    return selected


def tier_expressions() -> dict[str, str]:
    """The tier filters as the recipe defines them, read back out of the script.

    Parsing the script rather than restating the expressions here is the point:
    if someone edits a filter, these tests re-derive it and the partition
    assertions below fail on the new one instead of silently testing the old.
    """
    source = SCRIPT.read_text(encoding="utf-8")
    found = dict(re.findall(r"^(\w+)_expr=\"\$\(scoped '([^']+)'\)\"$", source, re.M))
    assert found.keys() == {"golden", "journey", "unit"}, found
    return found


@unittest.skipIf(os.name == "nt", "the coverage recipe is a POSIX shell script")
class TierSelectionTests(unittest.TestCase):
    """The three tiers must partition the suite — no test counted twice or lost."""

    def test_tiers_partition_the_whole_suite(self) -> None:
        expressions = tier_expressions()
        golden = nextest_list(expressions["golden"])
        journeys = nextest_list(expressions["journey"])
        unit = nextest_list(expressions["unit"])
        everything = nextest_list("all()")

        self.assertTrue(golden, "the golden tier selected no tests")
        self.assertTrue(journeys, "the journey tier selected no tests")
        self.assertTrue(unit, "the non-e2e tier selected no tests")
        self.assertEqual(set(), golden & journeys, "a test is in two e2e tiers")
        self.assertEqual(set(), (golden | journeys) & unit, "an e2e test is also non-e2e")
        self.assertEqual(
            everything,
            golden | journeys | unit,
            "the three tiers do not cover every test cargo-nextest runs",
        )

    def test_the_golden_tier_is_exactly_the_committed_byte_match_tests(self) -> None:
        golden = {name for _binary, name in nextest_list(tier_expressions()["golden"])}
        # Both vendored byte-for-byte goldens and a representative corpus golden.
        self.assertIn(OFFLINE_GOLDEN, golden)
        self.assertIn("exhaustive_matches_fern_output_byte_for_byte", golden)
        self.assertIn("frankfurter_matches_fern_output", golden)
        # Deliberately NOT golden: the runtime-behavior comparison is a wire test,
        # not a byte comparison against a committed golden, and the CalorieNinjas
        # boundary asserts a Fern *failure* — there is no golden to reach.
        self.assertNotIn("crozier_matches_fern_runtime_behavior", golden)
        self.assertNotIn(
            "calorieninjas_reproduces_the_exact_known_fern_failure_boundary", golden
        )
        for name in golden:
            self.assertIn("matches_fern_output", name)


@unittest.skipIf(os.name == "nt", "the coverage recipe is a POSIX shell script")
class RecipeEndToEndTests(unittest.TestCase):
    """Drive the real recipe: real llvm-cov, real subprocess, real report."""

    def run_recipe(self, *args: str, env: dict[str, str] | None = None):
        out = Path(self.enterContext(tempfile.TemporaryDirectory())) / "out"
        return self.run_script("--no-fetch", "--out", str(out), *args, env=env), out

    def run_script(self, *args: str, env: dict[str, str] | None = None):
        return subprocess.run(
            [str(SCRIPT), *args], cwd=REPO, capture_output=True, text=True, env=env
        )

    def run_reporter(self, out: Path, *args: str):
        """The reporter as its own process, over exports a real run produced."""
        return subprocess.run(
            [
                sys.executable,
                str(REPORTER),
                "--repo-root",
                str(REPO),
                "--golden-tier",
                "golden-only",
                *args,
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
        )

    def scoped_run(self):
        """The one scoped recipe run every export-reading case shares."""
        completed, out = _scoped_run()
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        return completed, out

    def scoped_exports(self) -> Path:
        completed, out = self.scoped_run()
        self.report = completed.stdout
        return out

    def tier_args(self, out: Path, *names: str) -> list[str]:
        return [
            arg
            for name in names
            for arg in ("--tier", f"{name}={out / f'{name}.json'}=1=selection")
        ]

    def test_scoped_run_reports_three_tiers_and_proves_subprocess_coverage(self) -> None:
        completed, out = self.scoped_run()
        report = completed.stdout

        for tier in ("golden-only", "all-e2e", "non-e2e"):
            self.assertIn(tier, report, f"the {tier} tier is missing from the report")
        self.assertIn("#[cfg(test)] excluded", report)

        # src/main.rs exists only inside the spawned binary, so a non-zero figure
        # there is the proof that subprocess profiles were captured, not assumed.
        proof = _subprocess_proof(report)
        self.assertGreater(proof["golden-only"], 0, report)
        self.assertGreater(proof["all-e2e"], proof["golden-only"], report)
        self.assertEqual(0, proof["non-e2e"], report)

        # Quiet on success: the report is the only thing on stdout, and cargo's
        # build/test scaffolding stays in the log file.
        self.assertNotIn("Compiling", completed.stdout)
        self.assertNotIn("Compiling", completed.stderr)
        self.assertIn("exports in", completed.stderr)
        self.assertTrue((out / "golden-only.json").is_file())

    def test_cfg_test_regions_are_excluded_from_the_denominator(self) -> None:
        completed, out = self.scoped_run()

        reported = _reported_region_total(completed.stdout, "src/emit.rs")
        tiers = {
            name: reporter.load_tier(out / f"{name}.json", REPO)
            for name in ("golden-only", "all-e2e", "non-e2e")
        }
        raw = {r for tier in tiers.values() for r in tier.get("src/emit.rs", {})}
        reporter.drop_test_regions(tiers, REPO)
        kept = {r for tier in tiers.values() for r in tier.get("src/emit.rs", {})}

        self.assertEqual(len(kept), reported, "the printed denominator is not the filtered one")
        self.assertGreater(len(raw) - len(kept), 1000, "cfg(test) exclusion did nothing")
        # Independent of the reporter's scanner: emit.rs ends in an inline
        # `mod tests`, so nothing at or below that line may survive the filter.
        marker = _mod_tests_line(REPO / "src" / "emit.rs")
        self.assertEqual([], [r for r in kept if r.line_start >= marker])

    def test_the_blind_spot_block_is_the_journeys_minus_the_goldens(self) -> None:
        """The block the recipe exists to produce, checked against the exports."""
        out = self.scoped_exports()
        block = self.report.split("golden blind spots")[1]
        self.assertIn("src/main.rs", block)

        tiers = {
            name: reporter.load_tier(out / f"{name}.json", REPO)
            for name in ("golden-only", "all-e2e", "non-e2e")
        }
        reporter.drop_test_regions(tiers, REPO)
        reached = {
            name: {
                (path, region)
                for path, counts in tier.items()
                for region, count in counts.items()
                if count > 0
            }
            for name, tier in tiers.items()
        }
        expected = (reached["all-e2e"] | reached["non-e2e"]) - reached["golden-only"]
        self.assertTrue(expected, "the scoped run should leave the goldens blind somewhere")
        self.assertIn(f"total {len(expected)} region(s)", block)
        for path, count in re.findall(r"^  (\S+)\s+(\d+)\s+\(", block, re.M):
            self.assertEqual(
                len({r for f, r in expected if f == path}),
                int(count),
                f"the blind-spot count for {path} is not the measured one",
            )

    def test_no_blind_spots_renders_as_such(self) -> None:
        """Handing every tier the same export must report nothing blind, not crash."""
        out = self.scoped_exports()
        completed = self.run_reporter(
            out,
            *[
                arg
                for name in ("golden-only", "all-e2e", "non-e2e")
                for arg in ("--tier", f"{name}={out / 'golden-only.json'}=1=selection")
            ],
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("(none — every region any tier reaches, a golden reaches too)", completed.stdout)

    def test_the_subprocess_proof_refuses_a_tier_that_never_spawned_the_binary(self) -> None:
        """non-e2e genuinely never runs the binary, so demanding proof of it must fail."""
        out = self.scoped_exports()
        completed = self.run_reporter(
            out,
            "--subprocess-tier",
            "non-e2e",
            *self.tier_args(out, "golden-only", "all-e2e", "non-e2e"),
        )
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("was NOT captured", completed.stderr)
        self.assertIn("LLVM_PROFILE_FILE", completed.stderr)

    def test_a_malformed_coverage_export_is_refused_not_trusted(self) -> None:
        out = self.scoped_exports()
        broken = out / "broken.json"
        broken.write_text('{"data": [{"functions": [{"regions": [[1, 1]]}]}]}', encoding="utf-8")
        completed = self.run_reporter(
            out,
            "--tier",
            f"golden-only={broken}=1=selection",
        )
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("is not the llvm-cov export", completed.stderr)

    def test_the_argument_parser_refuses_bad_invocations(self) -> None:
        for args, expected in (
            (("--out",), "--out needs a directory"),
            (("--nonsense",), "unknown argument '--nonsense'"),
            (("one", "two"), "more than one SCOPE expression"),
        ):
            with self.subTest(args=args):
                completed = self.run_script(*args)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(expected, completed.stderr)
        helped = self.run_script("--help")
        self.assertEqual(0, helped.returncode)
        self.assertIn("Usage: scripts/fixtures-coverage.sh", helped.stderr)

    def test_an_unresolvable_filter_expression_names_the_tier(self) -> None:
        completed, _ = self.run_recipe("test(=unclosed")
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("could not resolve", completed.stderr)
        self.assertIn("cargo nextest list --help", completed.stderr)

    def test_a_tier_that_selects_nothing_fails_with_a_next_action(self) -> None:
        completed, _ = self.run_recipe(f"test(={JOURNEY})")
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("matched no tests", completed.stderr)
        self.assertIn("Widen the SCOPE", completed.stderr)

    def test_a_missing_generation_dependency_fails_with_a_next_action(self) -> None:
        env = dict(os.environ)
        stripped = [
            entry
            for entry in env.get("PATH", "").split(os.pathsep)
            if not (Path(entry) / "ruff").exists()
        ]
        env["PATH"] = os.pathsep.join(stripped)
        if shutil.which("ruff", path=env["PATH"]):  # pragma: no cover - defensive
            self.skipTest("ruff is still resolvable after stripping PATH")
        completed, _ = self.run_recipe(OFFLINE_SCOPE, env=env)
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("ruff is not on PATH", completed.stderr)
        self.assertIn("just bootstrap", completed.stderr)

    def test_an_unfetched_corpus_is_a_hard_failure_not_a_silent_skip(self) -> None:
        """The whole point of CROZIER_REQUIRE_CORPUS: a skip would shrink the denominator."""
        cached = REPO / ".local" / "corpus" / "frankfurter"
        if not cached.is_dir():
            self.skipTest("run scripts/fetch-corpus.sh first: no frankfurter spec cached")
        hidden = cached.with_name("frankfurter.hidden-by-fixtures-coverage-test")
        self.assertFalse(hidden.exists(), f"stale {hidden} from an interrupted run")
        cached.rename(hidden)
        self.addCleanup(hidden.rename, cached)

        completed, _ = self.run_recipe(
            f"test(=frankfurter_matches_fern_output) or test(={JOURNEY}) or test(={UNIT})"
        )
        self.assertEqual(1, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("golden-only tier failed", completed.stderr)
        self.assertIn("CROZIER_REQUIRE_CORPUS", completed.stderr)
        self.assertIn("just test-corpus-match", completed.stderr)


class CfgTestSpanTests(unittest.TestCase):
    """The span scanner decides the denominator, so it gets its own hostile cases."""

    def test_spans_over_the_real_crate_end_on_a_closing_brace(self) -> None:
        seen = 0
        for path in sorted((REPO / "src").glob("*.rs")):
            source = path.read_text(encoding="utf-8")
            lines = source.splitlines()
            spans = reporter.cfg_test_spans(source)
            markers = [n for n, line in enumerate(lines, 1) if line.strip() == "#[cfg(test)]"]
            self.assertEqual(
                markers,
                [m for m in markers if any(s.start <= m <= s.end for s in spans)],
                f"{path.name}: a #[cfg(test)] item was not bounded by any span",
            )
            for span in spans:
                seen += 1
                self.assertEqual("#[cfg(test)]", lines[span.start - 1].strip())
                self.assertEqual("}", lines[span.end - 1].strip(), f"{path.name}:{span.end}")
        self.assertGreater(seen, 10, "the crate should have many #[cfg(test)] items")

    def test_braces_inside_raw_strings_and_comments_do_not_close_the_span(self) -> None:
        source = textwrap.dedent(
            '''\
            fn production() {}

            #[cfg(test)]
            mod tests {
                const TEMPLATE: &str = r#"
            }
            def f(): return {"a": 1}
            "#;
                /* nested /* block */ comment with } */
                const BRACE: char = '}';
                const ESCAPED: char = '\\'';
                fn borrow<'a>(value: &'a str) -> &'a str { value }
            }

            fn after() {}
            '''
        )
        self.assertEqual(
            [reporter.Span(3, 13)],
            reporter.cfg_test_spans(source),
            "the scanner closed the test module on a brace it should have skipped",
        )

    def test_an_unbounded_test_item_is_refused(self) -> None:
        with self.assertRaises(SystemExit) as raised:
            reporter.cfg_test_spans("#[cfg(test)]\nmod tests {\n    fn f() {}\n")
        self.assertIn("unbalanced braces", str(raised.exception))

    def test_an_unrecognized_test_conditional_attribute_is_refused(self) -> None:
        source = "#[cfg(all(test, feature = \"x\"))]\nmod tests {}\n"
        with self.assertRaises(SystemExit) as raised:
            reporter.cfg_test_spans(source)
        self.assertIn("does not recognize", str(raised.exception))


_SCOPED: tuple | None = None


def _scoped_run():
    """One offline-scoped run of the real recipe, shared by every case that reads
    its exports — the recipe is deterministic here, and re-running it per test
    would triple this file's contribution to `just check`."""
    global _SCOPED
    if _SCOPED is None:
        directory = tempfile.TemporaryDirectory()
        atexit.register(directory.cleanup)
        out = Path(directory.name) / "out"
        completed = subprocess.run(
            [str(SCRIPT), "--no-fetch", "--out", str(out), OFFLINE_SCOPE],
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        _SCOPED = (completed, out)
    return _SCOPED


def _subprocess_proof(report: str) -> dict[str, int]:
    """Parse the report's closing subprocess-coverage block."""
    tail = report.split("subprocess coverage proof")[-1]
    return {
        tier: int(count)
        for tier, count in re.findall(r"^\s+(\S+)\s+(\d+) region\(s\) covered$", tail, re.M)
    }


def _reported_region_total(report: str, path: str) -> int:
    """The golden-only region denominator the report printed for one file."""
    match = re.search(rf"^{re.escape(path)}\s+golden-only\s+\d+/(\d+)", report, re.M)
    assert match, f"no golden-only row for {path} in the report"
    return int(match.group(1))


def _mod_tests_line(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.strip() == "#[cfg(test)]" and lines[index + 1].strip() == "mod tests {":
            return index + 1
    raise AssertionError(f"{path} has no inline `mod tests`")


if __name__ == "__main__":
    unittest.main(verbosity=1, buffer=False, argv=[sys.argv[0], *sys.argv[1:]])

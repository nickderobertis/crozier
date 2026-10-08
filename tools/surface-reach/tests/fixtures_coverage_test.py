#!/usr/bin/env python3
"""Boundary tests for `just fixtures-coverage` (`just test-fixtures-coverage`).

The recipe's whole value is that its numbers are *honest*, so these drive the
real thing rather than a stand-in: the real `tools/surface-census/fixtures-coverage.sh`, the
real `cargo nextest` selection boundary, the real instrumented `cargo llvm-cov`
run over the real filesystem, and the real spawned `crozier` binary. Nothing is
mocked. The end-to-end cases pass a SCOPE so they measure two or three tests
instead of the whole corpus; that is the same code path the unscoped recipe runs.
"""

from __future__ import annotations

import atexit
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

# Every child these tests start has its output decoded as UTF-8, so a Python
# child writes UTF-8 too, whatever the platform locale (cp1252 on Windows).
os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "surface-census" / "fixtures-coverage.sh"
REPORTER = REPO / "tools" / "surface-census" / "fixtures-coverage-report.py"

# Vendored (never fetched) goldens, so the scoped runs stay offline.
OFFLINE_GOLDEN = "med_anvisa_price_matches_fern_output"
JOURNEY = "help_lists_generate"
UNIT = "wrap::tests::flat_atom_is_verbatim"
OFFLINE_SCOPE = f"test(={OFFLINE_GOLDEN}) or test(={JOURNEY}) or test(={UNIT})"


def load_reporter():
    spec = importlib.util.spec_from_file_location("fixtures_coverage_report", REPORTER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


reporter = load_reporter()


def nextest_list(expression: str, env: dict[str, str] | None = None) -> set[tuple[str, str]]:
    """(binary id, test name) cargo-nextest actually selects — the real boundary.

    Keyed on the binary too: `generation.rs` and `e2e.rs` share some test names,
    and collapsing them would make the tiers look like they overlap.

    `--color never` because this parses the listing: `CARGO_TERM_COLOR=always`
    (release.yml sets it; a developer's shell may too) otherwise wraps every
    name in ANSI escapes, and no plain test name would match.
    """
    listing = subprocess.run(
        ["cargo", "nextest", "list", "--workspace", "--locked", "--color", "never", "-E", expression],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
        env=env,
        encoding="utf-8",
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
        # Publisher byte-match goldens and their generator-setting variant.
        self.assertIn(OFFLINE_GOLDEN, golden)
        self.assertIn("marimo_client_class_name_matches_fern_output", golden)
        self.assertIn("frankfurter_matches_fern_output", golden)
        # Deliberately NOT golden: the runtime-behavior comparison is a wire test,
        # not a byte comparison against a committed golden, and the CalorieNinjas
        # boundary asserts a Fern *failure* — there is no golden to reach.
        self.assertNotIn("sdk_env_crozier_matches_fern_runtime_behavior", golden)
        self.assertNotIn("calorieninjas_reproduces_the_exact_known_fern_failure_boundary", golden)
        for name in golden:
            self.assertIn("matches_fern_output", name)

    def test_the_selection_reads_the_same_with_colour_forced(self) -> None:
        # release.yml's re-gate exports CARGO_TERM_COLOR=always; the listing
        # this suite parses must not change under it.
        expression = f"test(={OFFLINE_GOLDEN}) or test(={UNIT})"
        coloured = nextest_list(expression, env={**os.environ, "CARGO_TERM_COLOR": "always"})
        plain = nextest_list(expression, env={**os.environ, "CARGO_TERM_COLOR": "never"})
        self.assertEqual(plain, coloured)
        self.assertIn(OFFLINE_GOLDEN, {name for _binary, name in coloured})


@unittest.skipIf(os.name == "nt", "the coverage recipe is a POSIX shell script")
class RecipeEndToEndTests(unittest.TestCase):
    """Drive the real recipe: real llvm-cov, real subprocess, real report."""

    def run_recipe(self, *args: str, env: dict[str, str] | None = None):
        out = Path(self.enterContext(tempfile.TemporaryDirectory())) / "out"
        return self.run_script("--no-fetch", "--out", str(out), *args, env=env), out

    def run_script(self, *args: str, env: dict[str, str] | None = None):
        return subprocess.run([str(SCRIPT), *args], cwd=REPO, capture_output=True, text=True, env=env, encoding="utf-8")

    def reporter_process(self, *args: str):
        """The reporter as its own process, exactly as the recipe invokes it."""
        return subprocess.run(
            [sys.executable, str(REPORTER), "--repo-root", str(REPO), *args],
            cwd=REPO,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    def run_reporter(self, *args: str):
        """The reporter with golden-only as the golden tier, as the recipe runs it."""
        return self.reporter_process("--golden-tier", "golden-only", *args)

    def scoped_run(self):
        """The one scoped recipe run every export-reading case shares."""
        completed, out = _scoped_run()
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        return completed, out

    def scoped_report(self) -> str:
        """The report the shared scoped run wrote beside its exports."""
        _completed, out = self.scoped_run()
        return (out / "report.txt").read_text(encoding="utf-8")

    def tier_args(self, out: Path, *names: str, export: str | None = None) -> list[str]:
        return [
            arg
            for name in names
            for arg in (
                "--tier",
                json.dumps(
                    {
                        "name": name,
                        "export": str(out / f"{export or name}.json"),
                        "tests": 1,
                        "selection": "selection",
                    }
                ),
            )
        ]

    def test_scoped_run_reports_three_tiers_and_proves_subprocess_coverage(self) -> None:
        completed, out = self.scoped_run()
        report = self.scoped_report()

        for tier in ("golden-only", "all-e2e", "non-e2e"):
            self.assertIn(tier, report, f"the {tier} tier is missing from the report")
        self.assertIn("#[cfg(test)] excluded", report)

        # src/main.rs exists only inside the spawned binary, so a non-zero figure
        # there is the proof that subprocess profiles were captured, not assumed.
        proof = _subprocess_proof(report)
        self.assertGreater(proof["golden-only"], 0, report)
        self.assertGreater(proof["all-e2e"], proof["golden-only"], report)
        self.assertEqual(0, proof["non-e2e"], report)

        # Quiet on success: one line naming the report, which is written beside
        # the exports; cargo's build/test scaffolding stays in the log file.
        self.assertEqual("", completed.stdout)
        self.assertEqual(
            [f"fixtures-coverage: wrote the report to {out / 'report.txt'} (per-tier llvm-cov exports beside it)"],
            completed.stderr.splitlines(),
        )
        self.assertTrue((out / "golden-only.json").is_file())

    def test_cfg_test_regions_are_excluded_from_the_denominator(self) -> None:
        _completed, out = self.scoped_run()

        reported = _reported_region_total(self.scoped_report(), "src/emit.rs")
        tiers = {name: reporter.load_tier(out / f"{name}.json", REPO) for name in ("golden-only", "all-e2e", "non-e2e")}
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
        _completed, out = self.scoped_run()
        block = self.scoped_report().split("golden blind spots")[1]
        self.assertIn("src/main.rs", block)

        tiers = {name: reporter.load_tier(out / f"{name}.json", REPO) for name in ("golden-only", "all-e2e", "non-e2e")}
        reporter.drop_test_regions(tiers, REPO)
        reached = {
            name: {(path, region) for path, counts in tier.items() for region, count in counts.items() if count > 0}
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
        _report, out = self.scoped_run()
        completed = self.run_reporter(
            *self.tier_args(out, "golden-only", "all-e2e", "non-e2e", export="golden-only"),
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("(none — every region any tier reaches, a golden reaches too)", completed.stdout)

    def test_the_subprocess_proof_refuses_a_tier_that_never_spawned_the_binary(self) -> None:
        """non-e2e genuinely never runs the binary, so demanding proof of it must fail."""
        _report, out = self.scoped_run()
        completed = self.run_reporter(
            "--subprocess-tier",
            "non-e2e",
            *self.tier_args(out, "golden-only", "all-e2e", "non-e2e"),
        )
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("was NOT captured", completed.stderr)
        self.assertIn("LLVM_PROFILE_FILE", completed.stderr)

    def test_a_malformed_coverage_export_is_refused_not_trusted(self) -> None:
        _report, out = self.scoped_run()
        broken = out / "broken.json"
        broken.write_text('{"data": [{"functions": [{"regions": [[1, 1]]}]}]}', encoding="utf-8", newline="\n")
        completed = self.run_reporter(
            "--tier",
            json.dumps({"name": "golden-only", "export": str(broken), "tests": 1, "selection": "s"}),
        )
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("is not the llvm-cov export", completed.stderr)

    def test_an_export_whose_records_are_not_llvm_values_is_refused_before_aggregation(self) -> None:
        """Every field the report reads is checked before it is used, so a malformed
        record ends in the export refusal rather than a traceback or a skewed count."""
        source = str(REPO / "src" / "main.rs")
        good = [1, 1, 1, 2, 3, 0, 0, 0]
        cases = {
            "function not an object": [7],
            "filename not a string": [{"filenames": [7], "regions": [good]}],
            "region not a list": [{"filenames": [source], "regions": [5]}],
            "coordinate not an integer": [{"filenames": [source], "regions": [["1", 1, 1, 2, 3, 0, 0, 0]]}],
            "coordinate a boolean": [{"filenames": [source], "regions": [[True, 1, 1, 2, 3, 0, 0, 0]]}],
            "count not an integer": [{"filenames": [source], "regions": [[1, 1, 1, 2, "3", 0, 0, 0]]}],
            "count negative": [{"filenames": [source], "regions": [[1, 1, 1, 2, -1, 0, 0, 0]]}],
            "kind not an integer": [{"filenames": [source], "regions": [[1, 1, 1, 2, 3, 0, 0, None]]}],
            "zero line": [{"filenames": [source], "regions": [[0, 1, 1, 2, 3, 0, 0, 0]]}],
            "reversed span": [{"filenames": [source], "regions": [[5, 1, 2, 9, 3, 0, 0, 0]]}],
        }
        with tempfile.TemporaryDirectory() as scratch:
            for label, functions in cases.items():
                with self.subTest(label):
                    broken = Path(scratch) / "broken.json"
                    broken.write_text(json.dumps({"data": [{"functions": functions}]}), encoding="utf-8")
                    completed = self.run_reporter(
                        "--tier",
                        json.dumps({"name": "golden-only", "export": str(broken), "tests": 1, "selection": "s"}),
                    )
                    self.assertEqual(1, completed.returncode, completed.stdout + completed.stderr)
                    self.assertNotIn("Traceback", completed.stderr)
                    self.assertIn("is not the llvm-cov export", completed.stderr)
                    self.assertIn("update tools/surface-census/fixtures-coverage-report.py", completed.stderr)
            readable = Path(scratch) / "readable.json"
            readable.write_text(
                json.dumps({"data": [{"functions": [{"filenames": [source], "regions": [good]}]}]}), encoding="utf-8"
            )
            self.assertEqual({"src/main.rs": {reporter.Region(1, 1, 1, 2): 3}}, reporter.load_tier(readable, REPO))

    def test_a_malformed_tier_argument_is_refused(self) -> None:
        for spec, expected in (
            ("golden-only=x.json=1=s", "--tier is not JSON"),
            ('{"name": "golden-only"}', "needs exactly the fields"),
            (
                json.dumps({"name": "g", "export": "x", "tests": "many", "selection": "s"}),
                "must be a int",
            ),
            (
                json.dumps({"name": "g", "export": "x", "tests": 0, "selection": "s"}),
                "must be a positive count",
            ),
        ):
            with self.subTest(spec=spec):
                completed = self.run_reporter("--tier", spec)
                self.assertEqual(2, completed.returncode, completed.stdout)
                self.assertIn(expected, completed.stderr)
        twice = json.dumps({"name": "golden-only", "export": "x", "tests": 1, "selection": "s"})
        completed = self.run_reporter("--tier", twice, "--tier", twice)
        self.assertEqual(2, completed.returncode, completed.stdout)
        self.assertIn("--tier 'golden-only' is declared twice", completed.stderr)

    def test_a_tier_name_that_matches_no_tier_is_refused(self) -> None:
        """A typo'd --subprocess-tier would retire the proof without saying so."""
        _report, out = self.scoped_run()
        tiers = self.tier_args(out, "golden-only", "all-e2e", "non-e2e")

        typo = self.reporter_process("--golden-tier", "golden-only", "--subprocess-tier", "goldenonly", *tiers)
        self.assertEqual(2, typo.returncode, typo.stdout)
        self.assertIn("names no declared tier", typo.stderr)

        absent = self.reporter_process("--golden-tier", "not-a-tier", *tiers)
        self.assertEqual(2, absent.returncode, absent.stdout)
        self.assertIn("is not one of the declared tiers", absent.stderr)

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
        self.assertIn("Usage: tools/surface-census/fixtures-coverage.sh", helped.stderr)

    def test_an_unusable_output_directory_fails_with_a_next_action(self) -> None:
        base = Path(self.enterContext(tempfile.TemporaryDirectory()))
        blocking = base / "a-file"
        blocking.write_text("in the way\n", encoding="utf-8")
        uncreatable = self.run_script("--out", str(blocking / "out"), OFFLINE_SCOPE)
        self.assertEqual(1, uncreatable.returncode, uncreatable.stdout)
        self.assertIn(f"cannot create the output directory {blocking / 'out'}", uncreatable.stderr)
        self.assertIn("pass a writable --out DIR, then re-run", uncreatable.stderr)

        out = base / "out"
        (out / "run.log").mkdir(parents=True)
        unwritable = self.run_script("--out", str(out), OFFLINE_SCOPE)
        self.assertEqual(1, unwritable.returncode, unwritable.stdout)
        self.assertIn(f"cannot write the run log {out / 'run.log'}", unwritable.stderr)
        self.assertIn("or pass another --out DIR, then re-run", unwritable.stderr)

    def test_a_missing_python3_fails_with_how_to_install_it(self) -> None:
        # Every executable on PATH except python3, linked into one directory, so
        # bash, cargo and its subcommands still resolve.
        shadow = Path(self.enterContext(tempfile.TemporaryDirectory())) / "bin"
        shadow.mkdir()
        for entry in os.environ.get("PATH", "").split(os.pathsep):
            directory = Path(entry)
            if not directory.is_dir():
                continue
            for candidate in directory.iterdir():
                if candidate.name.startswith("python3") or (shadow / candidate.name).exists():
                    continue
                if candidate.is_file() and os.access(candidate, os.X_OK):
                    (shadow / candidate.name).symlink_to(candidate)
        env = {**os.environ, "PATH": str(shadow)}
        if shutil.which("python3", path=env["PATH"]):  # pragma: no cover - defensive
            self.skipTest("python3 is still resolvable on the shadow PATH")
        completed, _ = self.run_recipe(OFFLINE_SCOPE, env=env)
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("python3 is not on PATH", completed.stderr)
        self.assertIn("Install Python 3", completed.stderr)
        self.assertIn("then re-run", completed.stderr)

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
        stripped = [entry for entry in env.get("PATH", "").split(os.pathsep) if not (Path(entry) / "ruff").exists()]
        env["PATH"] = os.pathsep.join(stripped)
        if shutil.which("ruff", path=env["PATH"]):  # pragma: no cover - defensive
            self.skipTest("ruff is still resolvable after stripping PATH")
        completed, _ = self.run_recipe(OFFLINE_SCOPE, env=env)
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("ruff is not on PATH", completed.stderr)
        self.assertIn("just bootstrap", completed.stderr)

    @unittest.skipIf(os.name == "nt", "the failing cargo stand-in is a POSIX shell script")
    def test_a_coverage_tool_that_fails_reports_its_own_error_and_both_remedies(self) -> None:
        real = shutil.which("cargo")
        self.assertIsNotNone(real)
        with tempfile.TemporaryDirectory() as scratch:
            stand_in = Path(scratch) / "cargo"
            stand_in.write_text(
                "#!/bin/sh\n"
                'if [ "$1" = llvm-cov ]; then echo "error: the llvm-tools component is broken" >&2; exit 101; fi\n'
                f'exec "{real}" "$@"\n',
                encoding="utf-8",
            )
            stand_in.chmod(0o755)
            env = {**os.environ, "PATH": f"{scratch}{os.pathsep}{os.environ['PATH']}"}
            completed, _ = self.run_recipe(OFFLINE_SCOPE, env=env)
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("cargo-llvm-cov did not answer --version", completed.stderr)
        self.assertIn("run 'just bootstrap' if it is not installed", completed.stderr)
        self.assertIn("'cargo llvm-cov --version' said:\nerror: the llvm-tools component is broken", completed.stderr)

    def test_a_report_it_cannot_write_fails_naming_it_and_keeps_the_exports(self) -> None:
        """Measurement done, the report's own write failing still fails the run, saying where to look."""
        out = Path(self.enterContext(tempfile.TemporaryDirectory())) / "out"
        (out / "report.txt").mkdir(parents=True)
        completed = self.run_script("--no-fetch", "--out", str(out), OFFLINE_SCOPE)
        self.assertNotEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn(f"rendering the report into {out / 'report.txt'} failed", completed.stderr)
        self.assertIn(f"The per-tier llvm-cov exports are in {out}", completed.stderr)
        self.assertNotIn("wrote the report", completed.stderr)
        for tier in ("golden-only", "all-e2e", "non-e2e"):
            self.assertTrue((out / f"{tier}.json").is_file(), f"the {tier} export is gone")

    def test_a_missing_committed_corpus_is_a_hard_failure(self) -> None:
        """The committed-source preflight refuses missing inputs before measurement.

        The source goes missing from a scratch copy of the script, the checker and
        the committed corpus, never from the checkout: Nx runs the byte-match and
        census suites that read it beside this one.
        """
        root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        fixtures = REPO / "tests" / "fixtures"
        for relative in (
            "tools/surface-census/fixtures-coverage.sh",
            "tools/corpus/corpus_sources.py",
            "tools/corpus/corpus_remote_ref_pins.py",
        ):
            (root / relative).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / relative, root / relative)
        for entry in fixtures.iterdir():
            if entry.is_file():
                (root / "tests" / "fixtures").mkdir(parents=True, exist_ok=True)
                shutil.copy2(entry, root / "tests" / "fixtures" / entry.name)
        shutil.copytree(fixtures / "corpus-sources", root / "tests" / "fixtures" / "corpus-sources")
        checked = subprocess.run(
            [sys.executable, str(root / "tools/corpus/corpus_sources.py"), "check"],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(
            0, checked.returncode, f"the copied corpus does not pass as the checkout's does:\n{checked.stderr}"
        )
        shutil.rmtree(root / "tests" / "fixtures" / "corpus-sources" / "frankfurter")

        out = Path(self.enterContext(tempfile.TemporaryDirectory())) / "out"
        completed = subprocess.run(
            [
                str(root / "tools/surface-census/fixtures-coverage.sh"),
                "--no-fetch",
                "--out",
                str(out),
                f"test(=frankfurter_matches_fern_output) or test(={JOURNEY}) or test(={UNIT})",
            ],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(1, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("recorded but missing", completed.stderr)
        self.assertIn("frankfurter", completed.stderr)
        self.assertFalse(out.exists() and any(out.glob("*.json")), "a tier was measured past the refusal")


class CfgTestSpanTests(unittest.TestCase):
    """The span scanner decides the denominator, so it gets its own hostile cases."""

    def test_spans_over_the_real_crate_end_on_a_closing_brace(self) -> None:
        markers_seen = 0
        spans_seen = 0
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
            markers_seen += len(markers)
            for span in spans:
                spans_seen += 1
                self.assertEqual("#[cfg(test)]", lines[span.start - 1].strip())
                self.assertEqual("}", lines[span.end - 1].strip(), f"{path.name}:{span.end}")
        # Non-vacuity guard. Every assertion above quantifies over what this scan
        # found, so a crate with no `#[cfg(test)]` item would satisfy all of them
        # by leaving nothing to check. Requiring at least one marker (read off the
        # source, not off the scanner) means the scanner had real work, and a
        # scanner that then returned nothing fails the marker-bounded assertEqual.
        # Deliberately not a literal count: any legitimate removal of test-only
        # code moves that number without saying anything about the scanner.
        self.assertGreater(markers_seen, 0, "no #[cfg(test)] item was found to scan")
        self.assertGreater(spans_seen, 0, "the scanner returned no span for the crate")

    def test_braces_inside_raw_strings_and_comments_do_not_close_the_span(self) -> None:
        source = textwrap.dedent(
            """\
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
            """
        )
        self.assertEqual(
            [reporter.Span(3, 13)],
            reporter.cfg_test_spans(source),
            "the scanner closed the test module on a brace it should have skipped",
        )

    def test_a_brace_inside_a_string_spanning_lines_does_not_close_the_span(self) -> None:
        source = textwrap.dedent(
            """\
            #[cfg(test)]
            mod tests {
                const MESSAGE: &str = "first line
            } still inside the string \\" and its escaped quote
            last line";
            }

            fn after() {}
            """
        )
        self.assertEqual(
            [reporter.Span(1, 6)],
            reporter.cfg_test_spans(source),
            "the scanner closed the test module on a brace inside a multi-line string",
        )

    def test_an_unbounded_test_item_is_refused(self) -> None:
        with self.assertRaises(SystemExit) as raised:
            reporter.cfg_test_spans("#[cfg(test)]\nmod tests {\n    fn f() {}\n")
        self.assertIn("unbalanced braces", str(raised.exception))

    def test_an_unrecognized_test_conditional_attribute_is_refused(self) -> None:
        source = '#[cfg(all(test, feature = "x"))]\nmod tests {}\n'
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
            encoding="utf-8",
        )
        _SCOPED = (completed, out)
    return _SCOPED


def _subprocess_proof(report: str) -> dict[str, int]:
    """Parse the report's closing subprocess-coverage block."""
    tail = report.split("subprocess coverage proof")[-1]
    return {tier: int(count) for tier, count in re.findall(r"^\s+(\S+)\s+(\d+) region\(s\) covered$", tail, re.M)}


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

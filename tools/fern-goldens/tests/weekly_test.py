"""`tools/fern-goldens/weekly.py`'s offline phases: the plan it makes over the
real reference inventory and timing table, the pair it resolves (over a
stood-in `curl`), how it reads crozier's own reports, and the assembly's
accounting. The journeys that drive the real `git`, the recipe and crozier end
to end are `tools/fern-goldens-weekly/tests/weekly_journeys_test.py`'s.
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
import unittest.mock
from collections.abc import Callable
from pathlib import Path
from typing import Any

os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "fern-goldens" / "weekly.py"


def load():
    import importlib.util

    spec = importlib.util.spec_from_file_location("weekly", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["weekly"] = module
    spec.loader.exec_module(module)
    return module


weekly = load()


class RealPlanTests(unittest.TestCase):
    """The plan the weekly run makes of the finished tree's whole inventory."""

    @classmethod
    def setUpClass(cls) -> None:
        os.environ.pop(weekly.ROOT_ENV, None)
        cls.plan = weekly.make_plan(REPO, "", weekly.Pair("1.0.0", "1.0.0"))
        cls.inventory = weekly.inventory(REPO)

    def planned(self) -> list[tuple[str, str]]:
        return [entry.key() for shard in self.plan.shards for entry in shard.items]

    def shard_of(self) -> dict[tuple[str, str], int]:
        return {entry.key(): shard.index for shard in self.plan.shards for entry in shard.items}

    def test_every_item_of_every_family_is_planned_once(self) -> None:
        expected = [(family, item) for family, items in self.inventory.items() for item in items]
        self.assertEqual(sorted(expected), sorted(self.planned()))
        self.assertEqual(len(expected), len(set(self.planned())))
        self.assertTrue(self.plan.complete)
        self.assertEqual(
            {family: len(items) for family, items in self.inventory.items()},
            {family: entry.items for family, entry in self.plan.families.items()},
        )
        # Every family the recipe defines, so a Fern change to any reference is seen.
        self.assertEqual(set(weekly.load_references(REPO).FAMILY), set(self.plan.families))

    def test_the_shard_count_is_the_fewest_that_fit_the_budget(self) -> None:
        limit = weekly.shard_limit_seconds()
        loads = [shard.seconds for shard in self.plan.shards]
        self.assertTrue(all(load <= limit / 60 * 60 + 0.1 for load in loads), (loads, limit))
        count = len(loads)
        total = sum(loads)
        weights = self.unit_weights()
        bound = max(1, math.ceil(total / limit))
        self.assertGreaterEqual(count, bound, "fewer shards than the total allows under the limit")
        # Every count from the arithmetic lower bound up to one fewer than the
        # plan's overflows a shard when packed, so the plan is the fewest the
        # packer can fit. Where the packer fits the bound itself, the plan is it.
        for fewer in range(bound, count):
            longest = max(sum(weights[i] for i in group) for group in weekly.pack(weights, fewer))
            self.assertGreater(longest, limit, f"{fewer} shard(s) would have fitted")
        if max(sum(weights[i] for i in group) for group in weekly.pack(weights, bound)) <= limit:
            self.assertEqual(bound, count, "the packer fits the lower bound, so the plan must use it")
        self.assertLessEqual(self.plan.estimate.minutes, weekly.BUDGET_MINUTES)
        for shard in self.plan.shards:
            self.assertLess(shard.minutes, weekly.SHARD_TIMEOUT_MINUTES)

    def unit_weights(self) -> list[float]:
        table, default = weekly.timings(REPO)
        return [sum(table.get(key, default) for key in unit) for unit in weekly.units(REPO, self.inventory)]

    def test_twice_the_inventory_plans_more_shards_not_longer_ones(self) -> None:
        weights = self.unit_weights()
        limit = weekly.shard_limit_seconds()
        count, bins = weekly.shard_count(weights, limit)
        doubled, doubled_bins = weekly.shard_count(weights * 2, limit)
        self.assertGreater(doubled, count)
        longest = max(sum((weights * 2)[i] for i in group) for group in doubled_bins)
        self.assertLessEqual(longest, limit)
        self.assertEqual(sorted(i for group in doubled_bins for i in group), list(range(2 * len(weights))))
        self.assertEqual(len(bins), count)

    def test_items_that_depend_on_each_other_share_a_shard(self) -> None:
        shard = self.shard_of()
        for item in self.inventory["overlays"]:
            with self.subTest(overlay=item):
                self.assertEqual(shard[("corpus", item.split("/")[0])], shard[("overlays", item)])
        module = weekly.load_references(REPO)
        handwritten = (REPO / module.HANDWRITTEN).resolve()
        measured = (REPO / module.MEASUREMENTS).resolve()
        probed = (REPO / module.PROBE_EXPECTED).resolve()
        overlaid = {"handwritten": 0, "measurements": 0, "probes": 0}
        for name, case in module.cases().items():
            base = case.overlay.base.resolve() if case.overlay and case.overlay.base else None
            if base is not None and base.is_relative_to(handwritten):
                owner = ("handwritten", base.relative_to(handwritten).parts[0])
            elif base is not None and base.is_relative_to(measured):
                inner = base.relative_to(measured).as_posix()
                owner = ("measurements", max((c for c in module.cases() if inner.startswith(f"{c}/")), key=len))
            elif base is not None and base.is_relative_to(probed):
                owner = ("probes", base.relative_to(probed).parts[0])
            else:
                continue
            with self.subTest(case=name):
                self.assertEqual(shard[owner], shard[("measurements", name)])
                planned = [entry.key() for entry in self.plan.shards[shard[owner]].items]
                self.assertLess(planned.index(owner), planned.index(("measurements", name)), "its base first")
            overlaid[owner[0]] += 1
        # The real inventory overlays both kinds of base.
        self.assertGreater(overlaid["handwritten"], 10)
        self.assertGreater(overlaid["measurements"], 0)
        for family in weekly.SHARED_TABLE_FAMILIES:
            with self.subTest(family=family):
                self.assertEqual(1, len({shard[(family, item)] for item in self.inventory[family]}))
        literals = [item for item in self.inventory["measurements"] if item.startswith("parameter-literals/")]
        self.assertEqual(1, len({shard[("measurements", item)] for item in literals}))
        # Within a shard a golden generates before the overlay reduced against it.
        for planned in self.plan.shards:
            order = [entry.key() for entry in planned.items]
            for index, (family, item) in enumerate(order):
                if family == "overlays":
                    self.assertIn(("corpus", item.split("/")[0]), order[:index])

    def test_an_untimed_item_is_planned_at_the_corpus_rate(self) -> None:
        table, default = weekly.timings(REPO)
        corpus = [seconds for (family, _item), seconds in table.items() if family == "corpus"]
        self.assertTrue(corpus, "the table is seeded with corpus timings")
        self.assertAlmostEqual(sum(corpus) / len(corpus), default)
        handwritten = self.plan.families["handwritten"]
        self.assertAlmostEqual(handwritten.seconds, round(handwritten.items * default, 1), delta=1)

    def test_the_budget_the_planner_sizes_against_is_the_registered_one(self) -> None:
        budgets = (REPO / ".github/budgets.yaml").read_text(encoding="utf-8")
        entry = budgets.split("id: crozier-fern-goldens-weekly-minutes", 1)[1].split("\n  - id:", 1)[0]
        self.assertIn(f"threshold: {weekly.BUDGET_MINUTES:g}\n", entry)


class OverlayBaseTests(unittest.TestCase):
    def test_a_measurement_overlaying_a_tree_no_family_writes_stops_the_plan(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            (root / "tools/fern-goldens").mkdir(parents=True)
            (root / "tools/fern-goldens/fern-references.py").write_bytes(
                (REPO / "tools/fern-goldens/fern-references.py").read_bytes()
            )
            case = root / "docs/fern-measurements/group/case"
            base = root / "docs/elsewhere/fern-expected"
            base.mkdir(parents=True)
            case.mkdir(parents=True)
            (case / "openapi.yml").write_text("openapi: 3.0.3\n", encoding="utf-8")
            (root / "docs/fern-measurements/cases.tsv").write_text(
                "case\tdocument\tenum_type\tlayout\toverlay\n"
                "group/case\tdocs/fern-measurements/group/case/openapi.yml\tpython-enums\tpackaged\t"
                "fern-expected:docs/elsewhere/fern-expected\n",
                encoding="utf-8",
            )
            with self.assertRaises(weekly.WeeklyError) as raised:
                weekly.units(root, {"measurements": ["group/case"]})
        self.assertIn("case group/case overlays", str(raised.exception))
        self.assertIn("which no hand-written fixture, measured probe or measurement case writes", str(raised.exception))

    def test_a_measurement_overlaying_a_measured_probe_shares_the_probes_unit(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            (root / "tools/fern-goldens").mkdir(parents=True)
            (root / "tools/fern-goldens/fern-references.py").write_bytes(
                (REPO / "tools/fern-goldens/fern-references.py").read_bytes()
            )
            (root / "docs/openapi-surface/probe-expected/sample-probe").mkdir(parents=True)
            (root / "docs/openapi-surface/probes").mkdir(parents=True)
            (root / "docs/openapi-surface/probes/sample-probe.yml").write_text("openapi: 3.0.3\n", encoding="utf-8")
            (root / "docs/fern-measurements").mkdir(parents=True)
            (root / "docs/fern-measurements/cases.tsv").write_text(
                "case\tdocument\tenum_type\tlayout\toverlay\n"
                "group/case\tdocs/openapi-surface/probes/sample-probe.yml\tliterals\tpackaged\t"
                "fern-expected:docs/openapi-surface/probe-expected/sample-probe\n",
                encoding="utf-8",
            )
            grouped = weekly.units(root, {"measurements": ["group/case"], "probes": ["sample-probe"]})
        unit = next(group for group in grouped if ("measurements", "group/case") in group)
        self.assertIn(("probes", "sample-probe"), unit)
        self.assertLess(unit.index(("probes", "sample-probe")), unit.index(("measurements", "group/case")))


class SubsetTests(unittest.TestCase):
    def test_a_subset_plans_exactly_what_it_names(self) -> None:
        made = weekly.make_plan(REPO, "handwritten,corpus:anchore.io", None)
        planned = [entry.key() for shard in made.shards for entry in shard.items]
        inventory = weekly.inventory(REPO)
        self.assertEqual(
            sorted([("corpus", "anchore.io"), *(("handwritten", item) for item in inventory["handwritten"])]),
            sorted(planned),
        )
        self.assertFalse(made.complete)

    def test_an_unknown_family_or_item_is_refused(self) -> None:
        for spec, message in (
            ("handwriten", "no reference family 'handwriten'"),
            ("corpus:no-such-row", "no corpus item 'no-such-row'"),
            ("corpus:../x", "is no `family` or `family:item`"),
            ("a b", "is no `family` or `family:item`"),
        ):
            with self.subTest(spec=spec), self.assertRaises(weekly.WeeklyError) as raised:
                weekly.make_plan(REPO, spec, None)
            self.assertIn(message, str(raised.exception))


@unittest.skipIf(os.name == "nt", "the weekly workflow runs its scripts on Linux")
class ResolveTests(unittest.TestCase):
    """`resolve` over a copy of the real metadata and checks table, with a
    stood-in `curl` answering npm and Docker Hub."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "repo"
        for path in (
            "tools/fern-goldens/weekly.py",
            "tools/fern-goldens/fern-goldens",
            "tools/corpus/corpus_remote_ref_pins.py",
            "assets/scaffolding/metadata.json",
            "tests/fixtures/fern-pair-checks.tsv",
        ):
            (self.root / path).parent.mkdir(parents=True, exist_ok=True)
            (self.root / path).write_bytes((REPO / path).read_bytes())
        self.bin = Path(self.temporary.name) / "bin"
        self.bin.mkdir()
        curl = self.bin / "curl"
        curl.write_text(
            textwrap.dedent(
                """\
                #!/usr/bin/env python3
                import json, os, sys
                url = next(arg for arg in sys.argv if arg.startswith("https://"))
                if os.environ.get("FAIL") and os.environ["FAIL"] in url:
                    print("curl: (6) Could not resolve host", file=sys.stderr)
                    sys.exit(6)
                if "registry.npmjs.org" in url:
                    print(json.dumps({"versions": {v: {} for v in os.environ["NPM"].split(",")}}))
                else:
                    print(json.dumps({"results": [{"name": v} for v in os.environ["TAGS"].split(",")], "next": None}))
                """
            ),
            encoding="utf-8",
        )
        curl.chmod(0o755)
        record = json.loads((REPO / "assets/scaffolding/metadata.json").read_text(encoding="utf-8"))
        self.certified = (record["cliVersion"], record["generatorVersion"])

    def resolve(self, *args: str, **env: str) -> tuple[subprocess.CompletedProcess[str], dict[str, str]]:
        outputs = Path(self.temporary.name) / "outputs"
        outputs.unlink(missing_ok=True)
        environment = {
            **os.environ,
            "PATH": f"{self.bin}{os.pathsep}{os.environ['PATH']}",
            weekly.ROOT_ENV: str(self.root),
            "NPM": "9.0.1,10.2.0,10.10.0,11.0.0-rc.1",
            "TAGS": "4.9.0,4.10.0,4.11.0-rc.1,latest",
            **env,
        }
        result = subprocess.run(
            [
                sys.executable,
                str(self.root / "tools/fern-goldens/weekly.py"),
                "resolve",
                *args,
                "--github-output",
                str(outputs),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=environment,
            check=False,
        )
        values = (
            dict(line.split("=", 1) for line in outputs.read_text(encoding="utf-8").splitlines())
            if outputs.exists()
            else {}
        )
        return result, values

    def test_the_schedule_resolves_the_newest_stable_cli_and_generator(self) -> None:
        result, values = self.resolve("--ref", "refs/heads/main", "--token-present")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(
            ("10.10.0", "4.10.0", "true", "true"),
            (values["cli"], values["generator"], values["run"], values["complete"]),
        )
        self.assertIn(
            "Checking Fern CLI 10.10.0 / fern-python-sdk 4.10.0 over the whole reference inventory", result.stdout
        )

    def test_a_dispatch_pins_either_version_exactly(self) -> None:
        _result, values = self.resolve("--ref", "refs/heads/main", "--token-present", "--cli-version", "9.0.1")
        self.assertEqual(("9.0.1", "4.10.0"), (values["cli"], values["generator"]))
        _result, values = self.resolve("--ref", "refs/heads/main", "--token-present", "--generator-version", "4.9.0")
        self.assertEqual(("10.10.0", "4.9.0"), (values["cli"], values["generator"]))
        refused, _values = self.resolve("--ref", "refs/heads/main", "--token-present", "--cli-version", "10.x")
        self.assertEqual(1, refused.returncode)
        self.assertIn("--cli-version '10.x' is no exact stable version", refused.stderr)

    def test_the_certified_or_an_already_checked_pair_ends_green_with_nothing_to_do(self) -> None:
        cli, generator = self.certified
        result, values = self.resolve(
            "--ref", "refs/heads/main", "--cli-version", cli, "--generator-version", generator
        )
        self.assertEqual((0, "false"), (result.returncode, values["run"]), result.stderr)
        self.assertIn("is the certified pair already; nothing to check", result.stdout)
        checks = self.root / "tests/fixtures/fern-pair-checks.tsv"
        checks.write_text(checks.read_text(encoding="utf-8") + "10.10.0\t4.10.0\t2026-10-12\tmatch\n", encoding="utf-8")
        result, values = self.resolve("--ref", "refs/heads/main")
        self.assertEqual((0, "false"), (result.returncode, values["run"]), result.stderr)
        self.assertIn("was checked on 2026-10-12 and crozier matched it", result.stdout)

    def test_a_complete_run_needs_main_and_the_token_and_a_subset_needs_neither(self) -> None:
        branch, _values = self.resolve("--ref", "refs/heads/feature", "--token-present")
        self.assertEqual(1, branch.returncode)
        self.assertIn("runs from refs/heads/main, not refs/heads/feature", branch.stderr)
        tokenless, values = self.resolve("--ref", "refs/heads/main")
        self.assertEqual((1, {}), (tokenless.returncode, values))
        self.assertIn("RELEASE_PLZ_TOKEN is not set", tokenless.stderr)
        subset, values = self.resolve("--ref", "refs/heads/feature", "--items", "probes")
        self.assertEqual((0, "false", "true"), (subset.returncode, values["complete"], values["run"]), subset.stderr)

    def test_a_subset_with_line_breaks_reaches_the_outputs_as_one_line(self) -> None:
        result, values = self.resolve("--ref", "refs/heads/feature", "--items", "corpus:anchore.io,\nhandwritten\n")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(
            {
                "run": "true",
                "complete": "false",
                "cli": "10.10.0",
                "generator": "4.10.0",
                "items": "corpus:anchore.io,handwritten",
            },
            values,
        )

    def test_an_unreachable_registry_is_named(self) -> None:
        result, _values = self.resolve("--ref", "refs/heads/main", "--token-present", FAIL="registry.npmjs.org")
        self.assertEqual(1, result.returncode)
        self.assertIn("could not read https://registry.npmjs.org/fern-api", result.stderr)


class ReportTests(unittest.TestCase):
    """How the decision reads `report_fixture_diffs`' own verdict (`just
    fixtures-diff`). `fern_goldens_git_test.py` holds these to the strings that
    reporter prints, since only that project may read crozier-e2e's source."""

    SUMMARY = (
        "\n{g} comparison generation failure(s) across the reported corpora.\n"
        "{p} comparison processing failure(s) across the reported corpora.\n\n{d} differing file(s) across the reported corpora.\n"
    )

    def report(self, body: str, d: int = 0, g: int = 0, p: int = 0) -> str:
        return f"=== anchore.io ===\n{body}" + self.SUMMARY.format(d=d, g=g, p=p)

    def test_each_verdict(self) -> None:
        regression = "--- src/fern/client.py [REGRESSION — not in `unmatched`] ---\n  Normalized text differs\n"
        residual = "--- reference.md ---\n  Normalized text differs\n"
        for name, code, output, verdict in (
            ("no difference", 0, self.report("  no differences.\n"), "pass"),
            ("an unmatched residual only", 0, self.report(residual, d=1), "pass"),
            ("a regression", 0, self.report(regression, d=1), "reject"),
            ("a crozier generation failure", 0, self.report("  Crozier generation failed: boom\n", g=1), "reject"),
            (
                "a comparison it could not process",
                0,
                self.report("  Comparison processing failed: ledger\n", p=1),
                "cannot-run",
            ),
            (
                "a processing failure beside a regression",
                0,
                self.report(regression + "  Comparison processing failed: ledger\n", d=1, p=1),
                "cannot-run",
            ),
            (
                "an unregistered corpus",
                0,
                self.report("  Comparison setup failed: not registered\n", p=1),
                "cannot-run",
            ),
            ("no summaries", 0, "=== anchore.io ===\n", "cannot-run"),
            ("a crashed reporter", 101, self.report("  no differences.\n"), "cannot-run"),
        ):
            with self.subTest(name):
                self.assertEqual(verdict, weekly.read_report(code, output))


class GateTableTests(unittest.TestCase):
    def test_the_committed_gates_are_crozier_s_own_comparisons(self) -> None:
        gates = weekly.gates(REPO)
        families = set(weekly.load_references(REPO).FAMILY)
        self.assertEqual(families, {family for gate in gates for family in gate.families})
        commands = {gate.command for gate in gates}
        self.assertEqual(
            {
                "just fixtures-diff {item}",
                "cargo nextest run --locked --no-fail-fast --status-level fail --final-status-level fail -p crozier-e2e",
                "cargo nextest run --locked --no-fail-fast --status-level fail --final-status-level fail -p crozier --test refusal_registry",
                "python3 tools/fern-refusals/fern-refusals.py check",
            },
            commands,
        )
        justfile = (REPO / "justfile").read_text(encoding="utf-8")
        self.assertIn('fixtures-diff corpus="" file="":', justfile)
        self.assertTrue((REPO / "tests/refusal_registry.rs").is_file())
        self.assertTrue((REPO / "tools/fern-refusals/fern-refusals.py").is_file())
        corpus = next(gate for gate in gates if gate.per_item)
        self.assertEqual(("corpus",), corpus.families)
        self.assertEqual("fixtures-report", corpus.verdict)

    def test_a_malformed_row_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            (root / "tools/fern-goldens").mkdir(parents=True)
            for row, message in (
                ("corpus\teach\texit:0/1\ttrue", "scope is item or family"),
                ("corpus\titem\texit:zero\ttrue", "is fixtures-report or exit:PASS/REJECT"),
            ):
                (root / weekly.GATES).write_text("family\tscope\tverdict\tcommand\n" + row + "\n", encoding="utf-8")
                with self.subTest(row=row), self.assertRaises(weekly.WeeklyError) as raised:
                    weekly.gates(root)
                self.assertIn(message, str(raised.exception))


class AssemblyTests(unittest.TestCase):
    """The assembly's accounting over shard results written as the shard phase
    writes them."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.scratch = Path(self.temporary.name)
        self.root = self.scratch / "repo"
        (self.root / "assets/scaffolding").mkdir(parents=True)
        stand_in = '{"cliVersion": "1.0.0"}'  # certified-pair: stand-in
        (self.root / "assets/scaffolding/metadata.json").write_text(stand_in, encoding="utf-8")
        self.pair = weekly.Pair("2.0.0", "3.0.0")
        shards = tuple(
            weekly.PlannedShard(index, 1.0, 4.02, (weekly.PlannedItem("corpus", item, 1.0),))
            for index, item in enumerate(("a", "b"))
        )
        plan = weekly.Plan(
            complete=True,
            items="",
            base="a" * 40,
            pair=self.pair,
            budget_minutes=weekly.BUDGET_MINUTES,
            shard_limit_minutes=94.5,
            default_seconds=1.0,
            families={"corpus": weekly.FamilyTotal(2, 2.0)},
            units=2,
            shards=shards,
            estimate=weekly.wall_clock([1.0, 1.0]),
        )
        (self.scratch / "plan.json").write_text(json.dumps(plan.to_json()), encoding="utf-8")

    def shard(self, index: int, item: str, written: list[str], status: str = "ok") -> None:
        directory = self.scratch / "artifacts" / f"fern-goldens-shard-{index}"
        for path in written:
            (directory / "files" / path).parent.mkdir(parents=True, exist_ok=True)
            (directory / "files" / path).write_text(f"{item}\n", encoding="utf-8")
        record = {
            "schema_version": 3,
            "index": index,
            "pair": self.pair.to_json(),
            "base": "a" * 40,
            "items": [
                {
                    "family": "corpus",
                    "item": item,
                    "status": status,
                    "detail": "boom",
                    "seconds": 4.25,
                    "changed": written,
                    "log": "logs/x",
                }
            ],
            "written": written,
            "deleted": [],
        }
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "result.json").write_text(json.dumps(record), encoding="utf-8")

    def assemble(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "assemble",
                "--plan",
                str(self.scratch / "plan.json"),
                "--shards",
                str(self.scratch / "artifacts"),
                "--output",
                str(self.scratch / "bundle"),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, weekly.ROOT_ENV: str(self.root)},
            check=False,
        )

    def test_every_shard_combined_with_the_measured_seconds(self) -> None:
        self.shard(0, "a", ["tests/fixtures/a/expected/x.py"])
        self.shard(1, "b", ["tests/fixtures/b/expected/x.py"])
        result = self.assemble()
        self.assertEqual(0, result.returncode, result.stderr)
        bundle = self.scratch / "bundle"
        self.assertEqual("a\n", (bundle / "files/tests/fixtures/a/expected/x.py").read_text(encoding="utf-8"))
        self.assertEqual("b\n", (bundle / "files/tests/fixtures/b/expected/x.py").read_text(encoding="utf-8"))
        timings = (bundle / "files" / weekly.TIMINGS).read_text(encoding="utf-8")
        self.assertTrue(timings.startswith("# Seconds each Fern reference"))
        self.assertIn("family\titem\tseconds\ncorpus\ta\t4.2\ncorpus\tb\t4.2\n", timings)
        metadata = json.loads((bundle / "files" / weekly.METADATA).read_text(encoding="utf-8"))
        self.assertEqual(("2.0.0", "3.0.0"), (metadata["cliVersion"], metadata["generatorVersion"]))

    def test_two_shards_writing_one_file_is_a_failure(self) -> None:
        self.shard(0, "a", ["docs/shared.tsv"])
        self.shard(1, "b", ["docs/shared.tsv"])
        result = self.assemble()
        self.assertEqual(1, result.returncode)
        self.assertIn("docs/shared.tsv was written by shards 0 and 1", result.stderr)

    def test_a_shard_whose_files_disagree_with_its_items_is_a_failure(self) -> None:
        self.shard(0, "a", ["tests/fixtures/a/x.py"])
        self.shard(1, "b", [])
        stray = self.scratch / "artifacts/fern-goldens-shard-1/files/tests/fixtures/b/stray.py"
        stray.parent.mkdir(parents=True)
        stray.write_text("unlisted\n", encoding="utf-8")
        result = self.assemble()
        self.assertEqual(1, result.returncode)
        self.assertIn("shard 1's files disagree with what its items wrote", result.stderr)
        self.assertIn("tests/fixtures/b/stray.py", result.stderr)

    def test_a_result_no_planned_shard_accounts_for_is_a_failure(self) -> None:
        self.shard(0, "a", [])
        self.shard(1, "b", [])
        self.shard(7, "a", [])
        result = self.assemble()
        self.assertEqual(1, result.returncode)
        self.assertIn("shard 7 uploaded a result the plan has no shard for", result.stderr)

    @unittest.skipIf(os.name == "nt", "symbolic links need privileges on Windows")
    def test_a_symbolic_link_in_an_artifact_is_a_failure(self) -> None:
        self.shard(0, "a", ["tests/fixtures/a/x.py"])
        self.shard(1, "b", [])
        carried = self.scratch / "artifacts/fern-goldens-shard-0/files/tests/fixtures/a/x.py"
        carried.unlink()
        carried.symlink_to("/etc/hostname")
        result = self.assemble()
        self.assertEqual(1, result.returncode)
        self.assertIn("tests/fixtures/a/x.py is a symbolic link", result.stderr)

    def test_a_shard_listing_a_file_it_does_not_carry_is_a_failure(self) -> None:
        self.shard(0, "a", ["tests/fixtures/a/x.py"])
        self.shard(1, "b", [])
        (self.scratch / "artifacts/fern-goldens-shard-0/files/tests/fixtures/a/x.py").unlink()
        result = self.assemble()
        self.assertEqual(1, result.returncode)
        self.assertIn("shard 0 lists tests/fixtures/a/x.py but its artifact does not carry it", result.stderr)


def small_plan(**changes: object) -> weekly.Plan:
    """A two-shard plan of two corpus items, as the plan phase records one."""
    plan = weekly.Plan(
        complete=True,
        items="",
        base="a" * 40,
        pair=weekly.Pair("2.0.0", "3.0.0"),
        budget_minutes=weekly.BUDGET_MINUTES,
        shard_limit_minutes=94.5,
        default_seconds=1.0,
        families={"corpus": weekly.FamilyTotal(2, 2.0)},
        units=2,
        shards=tuple(
            weekly.PlannedShard(index, 1.0, 4.02, (weekly.PlannedItem("corpus", item, 1.0),))
            for index, item in enumerate(("a", "b"))
        ),
        estimate=weekly.wall_clock([1.0, 1.0]),
    )
    return weekly.replace(plan, **changes)


class ArtifactTests(unittest.TestCase):
    """Every artifact a phase reads is refused, naming the fault, when it is
    not what the phase that writes it writes."""

    def test_a_plan_is_refused_for_each_fault(self) -> None:
        good = small_plan().to_json()
        weekly.Plan.from_json(good, "plan.json")
        faults: list[tuple[str, object, str]] = []

        # A mutation of the plan's JSON record, whose values are of every JSON type
        # (hence `Any`: each mutation reaches into whichever field it corrupts).
        def fault(message: str, change: Callable[[dict[str, Any]], object]) -> None:
            record = json.loads(json.dumps(good))
            change(record)
            faults.append((message, record, message))

        fault("`base` must be a commit's full name or null", lambda r: r.update(base="main"))
        fault("is no family or item name", lambda r: r["shards"][0]["items"][0].update(item="../escape"))
        fault("is no family or item name", lambda r: r["shards"][0]["items"][0].update(family="/abs"))
        fault("plans an item twice", lambda r: r["shards"][1]["items"].append(r["shards"][0]["items"][0]))
        fault("do not hold the 2 corpus item(s) it counts", lambda r: r["shards"][1].update(items=[]))
        fault(
            "a shard holds an item of no family it counts",
            lambda r: (
                r["families"].update(corpus={"items": 1, "seconds": 1})
                or r["shards"][1]["items"][0].update(family="probes")
            ),
        )
        fault("shards must be numbered from 0 in order", lambda r: r["shards"][1].update(index=5))
        fault("must be a non-negative number", lambda r: r["estimate"].update(minutes=float("nan")))
        fault("no plan of this tool's schema", lambda r: r.update(schema_version=1))
        fault("`complete` must say whether it plans the whole inventory", lambda r: r.update(items="probes"))
        fault(
            "`complete` must say whether it plans the whole inventory",
            lambda r: r.update(families={}, shards=[]),
        )
        for message, record, expected in faults:
            with self.subTest(message), self.assertRaises(weekly.WeeklyError) as raised:
                weekly.Plan.from_json(record, "plan.json")
            self.assertIn(expected, str(raised.exception))

    def test_a_shard_result_or_bundle_naming_a_path_outside_the_checkout_is_refused(self) -> None:
        item = {
            "family": "corpus",
            "item": "a",
            "status": "ok",
            "detail": "",
            "seconds": 1.0,
            "changed": [],
            "log": "x",
        }
        shard = {
            "schema_version": 3,
            "index": 0,
            "pair": {"cli": "2.0.0", "generator": "3.0.0"},
            "base": None,
            "items": [item],
            "written": [],
            "deleted": [],
        }
        for key, value in (
            ("written", ["../outside"]),
            ("deleted", ["/etc/passwd"]),
            ("written", [".git/config"]),
            ("written", ["tests/fixtures/a\0/x.py"]),
        ):
            with self.subTest(path=value), self.assertRaises(weekly.WeeklyError) as raised:
                weekly.ShardResult.from_json({**shard, key: value}, "result.json")
            self.assertIn("is no path inside the repository", str(raised.exception))
        with self.assertRaises(weekly.WeeklyError) as raised:
            weekly.ShardResult.from_json({**shard, "items": [{**item, "status": "skipped"}]}, "result.json")
        self.assertIn("status 'skipped' is none of", str(raised.exception))
        bundle = {
            "schema_version": 3,
            "pair": shard["pair"],
            "base": None,
            "complete": True,
            "items": [item],
            "deleted": ["a/../../b"],
            "failures": [],
        }
        with self.assertRaises(weekly.WeeklyError):
            weekly.Bundle.from_json(bundle, "bundle.json")
        for faulty, message in (
            ({**bundle, "deleted": [], "failures": [{"why": "x"}]}, "`failures` must be a list of strings"),
            ({**bundle, "deleted": [], "items": [{**item, "shard": "0"}]}, "`shard` must be int"),
            ({**bundle, "deleted": [], "items": [{**item, "shard": -1}]}, "`shard` must be a shard's index"),
        ):
            with self.subTest(message), self.assertRaises(weekly.WeeklyError) as raised:
                weekly.Bundle.from_json(faulty, "bundle.json")
            self.assertIn(message, str(raised.exception))

    def test_a_phase_reading_a_faulty_artifact_fails_naming_it(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            plan = Path(scratch) / "plan.json"
            record = small_plan().to_json()
            record["shards"][0]["items"][0]["item"] = "../escape"
            plan.write_text(json.dumps(record), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "assemble",
                    "--plan",
                    str(plan),
                    "--shards",
                    scratch,
                    "--output",
                    str(Path(scratch) / "out"),
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertIn("'../escape' is no family or item name", result.stderr)


class EstimateTests(unittest.TestCase):
    def test_more_shards_than_the_concurrent_allowance_run_in_waves(self) -> None:
        seconds = [600.0] * 25 + [1200.0]
        estimate = weekly.wall_clock(seconds)
        self.assertEqual(2, estimate.waves)
        # Each wave lasts as long as its longest shard; the longest leads the first.
        first = weekly.JOB_SETUP_MINUTES + 1200 / 60
        second = weekly.JOB_SETUP_MINUTES + 600 / 60
        self.assertAlmostEqual(first + second, estimate.stages["shards"])
        self.assertAlmostEqual(sum(estimate.stages.values()), estimate.minutes, places=1)
        self.assertEqual(round(first, 2), estimate.longest_shard_minutes)


class TimingTableTests(unittest.TestCase):
    def results(self) -> list[weekly.ItemResult]:
        return [
            weekly.ItemResult("corpus", "a", weekly.Status.OK, "", 7.5, (), "x"),
            weekly.ItemResult("corpus", "b", weekly.Status.FAILED, "boom", 99.0, (), "x"),
        ]

    def write(self, plan: weekly.Plan) -> str:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            weekly.write_tsv(
                root / weekly.TIMINGS,
                weekly.TIMINGS_HEADER,
                [["corpus", "a", "1.0"], ["corpus", "b", "2.0"], ["corpus", "gone", "3.0"]],
            )
            destination = root / "out.tsv"
            weekly.write_timings(root, plan, self.results(), destination)
            return destination.read_text(encoding="utf-8").split("family\titem\tseconds\n", 1)[1]

    def test_a_complete_run_drops_items_no_longer_planned_and_keeps_an_unmeasured_row(self) -> None:
        self.assertEqual("corpus\ta\t7.5\ncorpus\tb\t2.0\n", self.write(small_plan()))

    def test_a_subset_run_keeps_every_row_it_did_not_measure(self) -> None:
        self.assertEqual("corpus\ta\t7.5\ncorpus\tb\t2.0\ncorpus\tgone\t3.0\n", self.write(small_plan(complete=False)))

    def test_a_malformed_row_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            for rows, message in (
                ([["corpus", "a", "nan"]], "finite, non-negative"),
                ([["corpus", "a", "-1"]], "finite, non-negative"),
                ([["corpus", "a", "1"], ["corpus", "a", "2"]], "has two rows"),
            ):
                weekly.write_tsv(root / weekly.TIMINGS, weekly.TIMINGS_HEADER, rows)
                with self.subTest(rows=rows), self.assertRaises(weekly.WeeklyError) as raised:
                    weekly.timings(root)
                self.assertIn(message, str(raised.exception))


# The artifacts each weekly phase writes, byte for byte, at SCHEMA_VERSION 3: a
# change to what they emit must move this golden (and, when an old reader would
# misread it, the version) in the same change. Regenerate with
# CROZIER_UPDATE_WEEKLY_GOLDEN=1 after a deliberate contract change.
CONTRACT_GOLDEN = REPO / "tools/fern-goldens/tests/golden/weekly-v3"


def contract_artifacts() -> dict[str, dict[str, object]]:
    """One of each artifact, as the phases build them: a plan, a shard result
    and a bundle carrying an `ok` and a `refusal-changed` item, and a diff
    decision with a populated `refusals_changed`."""
    pair = weekly.Pair("2.0.0", "3.0.0")
    # Literal budget and estimate, so a retuned budget or overhead moves the
    # planner's tests, not this contract.
    stages = {"plan": 5.0, "shards": 4.02, "assembly": 6.0, "decision": 34.0, "publication": 5.0}
    plan = small_plan(budget_minutes=180.0, estimate=weekly.Estimate(54.02, stages, 1, 4.0, 6.0, 4.02))
    unsettled = (
        "unsettled: recorded: the check stage exits 1 and the generation 1, with `FATAL ERROR: JavaScript heap "
        "out of memory`, at Fern CLI 1.0.0 / fern-python-sdk 1.0.0; now: unsettled: `fern check` and `fern "
        "generate` ran past the probe's 900-second bound (check exit timeout, generate exit timeout), printing no "
        "diagnostic matching the template; a run cut short says nothing about whether Fern refuses given more "
        "time or memory"
    )
    items = (
        weekly.ItemResult(
            "corpus", "a", weekly.Status.OK, "", 1.5, ("tests/fixtures/a/expected/x.py",), "corpus/a.log"
        ),
        weekly.ItemResult(
            "refusals",
            "heap-exhausted",
            weekly.Status.REFUSAL_CHANGED,
            unsettled,
            1800.2,
            ("docs/openapi-surface/fern-refusals/probe-logs/heap-exhausted.check.log",),
            "refusals/heap-exhausted.log",
        ),
    )
    shard = weekly.ShardResult(0, pair, plan.base, items, tuple(path for i in items for path in i.changed), ())
    bundle = weekly.Bundle(pair, plan.base, True, tuple(weekly.replace(item, shard=0) for item in items), (), ())
    decision = weekly.Decision(pair, True, "b" * 64)
    decision.refusals_changed.append(weekly.RefusalChange("heap-exhausted", unsettled))
    decision.gates.append(
        weekly.GateRun("crozier compare", "refusals", "heap-exhausted", weekly.Verdict.PASS, 1, "reports/r.txt")
    )
    return {
        "plan.json": plan.to_json(),
        "result.json": shard.to_json(),
        "bundle.json": bundle.to_json(),
        "decision.json": decision.to_json(),
    }


class ContractGoldenTests(unittest.TestCase):
    """What the phases write is the committed version-3 contract, and the
    phases that read it accept the golden as written."""

    def test_each_artifact_serializes_to_the_committed_golden(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            for name, record in contract_artifacts().items():
                written = Path(scratch) / name
                weekly.write_json(written, record)
                golden = CONTRACT_GOLDEN / name
                if os.environ.get("CROZIER_UPDATE_WEEKLY_GOLDEN"):
                    golden.parent.mkdir(parents=True, exist_ok=True)
                    golden.write_bytes(written.read_bytes())
                with self.subTest(name):
                    self.assertEqual(
                        golden.read_text(encoding="utf-8"),
                        written.read_text(encoding="utf-8"),
                        f"{name} no longer serializes as the committed contract; if that is deliberate, bump "
                        "SCHEMA_VERSION when an old reader would misread it and regenerate with "
                        "CROZIER_UPDATE_WEEKLY_GOLDEN=1",
                    )

    def test_the_golden_is_read_back_by_each_phase_unchanged(self) -> None:
        def golden(name: str) -> dict[str, Any]:
            # A JSON object whose fields each reader validates: `Any` is json's own value type.
            return json.loads((CONTRACT_GOLDEN / name).read_text(encoding="utf-8"))

        self.assertEqual(weekly.SCHEMA_VERSION, golden("result.json")["schema_version"])
        self.assertEqual(golden("plan.json"), weekly.Plan.from_json(golden("plan.json"), "plan").to_json())
        shard = weekly.ShardResult.from_json(golden("result.json"), "result")
        self.assertEqual(golden("result.json"), shard.to_json())
        self.assertEqual(weekly.Status.REFUSAL_CHANGED, shard.items[1].status)
        bundle = weekly.Bundle.from_json(golden("bundle.json"), "bundle")
        self.assertEqual(golden("bundle.json"), bundle.to_json())
        read = weekly.RecordedDecision.from_json(golden("decision.json"), "decision")
        self.assertEqual(weekly.Outcome.DIFF, read.outcome)
        self.assertEqual((weekly.RefusalChange("heap-exhausted", bundle.items[1].detail),), read.refusals_changed)


class DecisionRecordTests(unittest.TestCase):
    """The decision the publication job reads back is the one written."""

    def test_known_changed_is_omitted_when_empty_and_round_trips_when_populated(self) -> None:
        pair = weekly.Pair("5.170.0", "5.42.0")
        empty = weekly.Decision(pair, True, "digest")
        self.assertNotIn("known_changed", empty.to_json())
        self.assertEqual((), weekly.RecordedDecision.from_json(empty.to_json(), "decision").known_changed)

        populated = weekly.Decision(pair, True, "digest")
        change = weekly.KnownFailureChange("calorieninjas.com", "Fern generates it", "tests/fixtures/…")
        populated.known_changed.append(change)
        record = json.loads(json.dumps(populated.to_json()))
        self.assertEqual([vars(change)], record["known_changed"])
        read = weekly.RecordedDecision.from_json(record, "decision")
        self.assertEqual((weekly.Outcome.DIFF, (change,)), (read.outcome, read.known_changed))

        for message, mutate in (
            ("`known_changed` must be list", lambda r: r.update(known_changed={})),
            ("`detail` must be str", lambda r: r["known_changed"][0].pop("detail")),
            ("is no family or item name", lambda r: r["known_changed"][0].update(item="../x")),
            ("a match changes no known failure", lambda r: r.update(outcome="match")),
        ):
            broken = json.loads(json.dumps(record))
            mutate(broken)
            with self.subTest(message), self.assertRaises(weekly.WeeklyError) as raised:
                weekly.RecordedDecision.from_json(broken, "decision")
            self.assertIn(message, str(raised.exception))

    def test_refusals_changed_is_omitted_when_empty_and_round_trips_when_populated(self) -> None:
        pair = weekly.Pair("5.170.0", "5.42.0")
        empty = weekly.Decision(pair, True, "digest")
        self.assertNotIn("refusals_changed", empty.to_json())
        self.assertEqual((), weekly.RecordedDecision.from_json(empty.to_json(), "decision").refusals_changed)

        populated = weekly.Decision(pair, True, "digest")
        change = weekly.RefusalChange("heap-exhausted", "unsettled: recorded: …; now: …")
        populated.refusals_changed.append(change)
        record = json.loads(json.dumps(populated.to_json()))
        self.assertEqual([vars(change)], record["refusals_changed"])
        read = weekly.RecordedDecision.from_json(record, "decision")
        self.assertEqual((weekly.Outcome.DIFF, (change,)), (read.outcome, read.refusals_changed))

        for message, mutate in (
            ("`refusals_changed` must be list", lambda r: r.update(refusals_changed={})),
            ("`detail` must be str", lambda r: r["refusals_changed"][0].pop("detail")),
            ("a match changes no known failure or refusal", lambda r: r.update(outcome="match")),
        ):
            broken = json.loads(json.dumps(record))
            mutate(broken)
            with self.subTest(message), self.assertRaises(weekly.WeeklyError) as raised:
                weekly.RecordedDecision.from_json(broken, "decision")
            self.assertIn(message, str(raised.exception))


class RefusalChangeTests(unittest.TestCase):
    """The report `fern-refusals.py probe --changes` writes is read at the shard's
    boundary: a change it states names its outcome, record and new result, and
    anything else fails the item rather than pass as a change."""

    def read(self, text: str | None, item: str = "heap-exhausted") -> str | None:
        with tempfile.TemporaryDirectory() as scratch:
            path = Path(scratch) / "probe.heap-exhausted.changes.jsonl"
            if text is not None:
                path.write_text(text, encoding="utf-8")
            return weekly.refusal_change(path, item)

    def test_a_reported_change_is_one_line_and_no_report_is_no_change(self) -> None:
        line = {
            "class": "heap-exhausted",
            "outcome": "unsettled",
            "recorded": "the check stage …",
            "now": "unsettled: …",
        }
        other = {**line, "class": "other"}
        text = json.dumps(other) + "\n" + json.dumps(line) + "\n"
        self.assertEqual("unsettled: recorded: the check stage …; now: unsettled: …", self.read(text))
        self.assertIsNone(self.read(None))
        self.assertIsNone(self.read(""))
        self.assertIsNone(self.read(json.dumps(other) + "\n"))

    def test_a_malformed_report_is_refused(self) -> None:
        line = {"class": "heap-exhausted", "outcome": "generates", "recorded": "r", "now": "n"}
        for message, text in (
            ("is no JSON object", "not json\n"),
            ("is no JSON object", "[1]\n"),
            ("`now` must be str", json.dumps({**line, "now": 3})),
            ("`recorded` must be str", json.dumps({key: value for key, value in line.items() if key != "recorded"})),
            ("a change is one of generates, refuses-otherwise, unsettled", json.dumps({**line, "outcome": "vanished"})),
            ("a change is one of", json.dumps({**line, "now": ""})),
        ):
            with self.subTest(text=text), self.assertRaises(weekly.WeeklyError) as raised:
                self.read(text)
            self.assertIn(message, str(raised.exception))
        # A report that is there but cannot be read is no "no change".
        with tempfile.TemporaryDirectory() as scratch, self.assertRaises(weekly.WeeklyError) as raised:
            weekly.refusal_change(Path(scratch), "heap-exhausted")
        self.assertIn("cannot read", str(raised.exception))


class TitleTests(unittest.TestCase):
    def test_the_pull_request_title_is_a_conventional_commit_naming_both_versions(self) -> None:
        decision = weekly.Decision(weekly.Pair("5.170.0", "5.42.0"), True, "digest")
        self.assertEqual(
            "test(fern-goldens): regenerate at Fern CLI 5.170.0 / fern-python-sdk 5.42.0", decision.title()
        )
        self.assertEqual(decision.title(), decision.to_json()["title"])


class BodyTests(unittest.TestCase):
    def decision(self, reports: list[str]) -> weekly.Decision:
        decision = weekly.Decision(weekly.Pair("2.0.0", "3.0.0"), True, "digest")
        decision.failing["corpus"] = [weekly.FailingItem(f"item-{n}", report) for n, report in enumerate(reports)]
        return decision

    def bundle(self) -> weekly.Bundle:
        item = weekly.ItemResult("corpus", "a", weekly.Status.OK, "", 1.0, (), "x")
        return weekly.Bundle(weekly.Pair("2.0.0", "3.0.0"), None, True, (item,), (), ())

    def test_a_report_holding_a_fence_is_fenced_longer(self) -> None:
        text = weekly.body(self.decision(["before\n````\nafter"]), self.bundle(), weekly.Pair("1.0.0", "1.0.0"))
        self.assertIn("`````text\nbefore\n````\nafter\n`````", text)

    def test_long_reports_and_bodies_are_truncated_and_say_where_the_rest_is(self) -> None:
        one = weekly.body(self.decision(["x" * 20000]), self.bundle(), weekly.Pair("1.0.0", "1.0.0"))
        self.assertIn("… (truncated; the decision artifact holds the whole report)", one)
        self.assertLess(len(one), weekly.REPORT_LIMIT + 2000)
        many = weekly.body(self.decision(["y" * 5000] * 400), self.bundle(), weekly.Pair("1.0.0", "1.0.0"))
        self.assertLessEqual(len(many), weekly.BODY_LIMIT + 5000)

    def test_a_changed_known_failure_is_a_diff_whose_long_report_is_truncated(self) -> None:
        decision = weekly.Decision(weekly.Pair("2.0.0", "3.0.0"), True, "digest")
        decision.known_changed.append(weekly.KnownFailureChange("gamma", "Fern generates it", "z" * 20000))
        self.assertEqual(weekly.Outcome.DIFF, decision.outcome)
        text = weekly.body(decision, self.bundle(), weekly.Pair("1.0.0", "1.0.0"))
        self.assertIn("Fern decided 1 registered known failure(s) otherwise", text)
        self.assertIn("- corpus `gamma`: Fern generates it", text)
        self.assertIn("… (truncated; the bundle carries the whole file)", text)
        self.assertLess(len(text), weekly.REPORT_LIMIT + 2000)

    def test_the_run_is_linked_when_the_workflow_names_it(self) -> None:
        with unittest.mock.patch.dict(
            os.environ,
            {"GITHUB_RUN_ID": "77", "GITHUB_REPOSITORY": "owner/crozier", "GITHUB_SERVER_URL": "https://github.com"},
        ):
            text = weekly.body(self.decision(["r"]), self.bundle(), weekly.Pair("1.0.0", "1.0.0"))
        self.assertIn("Run: https://github.com/owner/crozier/actions/runs/77", text)


class GitHubListingTests(unittest.TestCase):
    def listing(self, stdout: str) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess(["gh"], 0, stdout, "")

    def test_only_a_json_list_of_objects_is_a_listing(self) -> None:
        self.assertEqual([], weekly.gh_objects(self.listing("[]\n"), "labels"))
        self.assertEqual([{"name": "x"}], weekly.gh_objects(self.listing('[{"name": "x"}]'), "labels"))
        for stdout, message in (("", "printed no JSON"), ("{}", "no list of objects"), ("[1]", "no list of objects")):
            with self.subTest(stdout=stdout), self.assertRaises(weekly.WeeklyError) as raised:
                weekly.gh_objects(self.listing(stdout), "labels")
            self.assertIn(message, str(raised.exception))


class PublicationGuardTests(unittest.TestCase):
    """`publish` refuses, before any remote step, what it must never publish."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.scratch = Path(self.temporary.name)
        self.bundle = self.scratch / "bundle"
        (self.bundle / "files").mkdir(parents=True)
        (self.bundle / "files/x.txt").write_text("x\n", encoding="utf-8")
        record = {
            "schema_version": 3,
            "pair": {"cli": "2.0.0", "generator": "3.0.0"},
            "base": None,
            "complete": True,
            "items": [],
            "deleted": [],
            "failures": [],
        }
        (self.bundle / "bundle.json").write_text(json.dumps(record), encoding="utf-8")
        self.decision = self.scratch / "decision"
        self.decision.mkdir()

    def publish(
        self, outcome: str = "match", *, digest: str | None = None, checked_on: str = "2026-10-19"
    ) -> subprocess.CompletedProcess[str]:
        record = {
            "schema_version": 3,
            "outcome": outcome,
            "complete": True,
            "pair": {"cli": "2.0.0", "generator": "3.0.0"},
            "bundle": digest or weekly.bundle_digest(self.bundle),
            "title": "test(fern-goldens): regenerate",
        }
        (self.decision / "decision.json").write_text(json.dumps(record), encoding="utf-8")
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "publish",
                "--bundle",
                str(self.bundle),
                "--decision",
                str(self.decision),
                "--repo",
                "owner/crozier",
                "--checked-on",
                checked_on,
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, weekly.ROOT_ENV: str(self.scratch), "GH_TOKEN": "token"},
            check=False,
        )

    def test_a_failed_decision_another_bundle_or_a_bad_date_is_refused(self) -> None:
        for (outcome, digest, checked_on), message in (
            (("failure", None, "2026-10-19"), "the decision is 'failure'"),
            (("match", "0" * 64, "2026-10-19"), "made over another bundle"),
            (("match", None, "19/10/2026"), "is no YYYY-MM-DD date"),
        ):
            with self.subTest(message):
                result = self.publish(outcome, digest=digest, checked_on=checked_on)
                self.assertEqual(1, result.returncode)
                self.assertIn(message, result.stderr)

    def test_a_file_changed_after_the_decision_breaks_its_binding(self) -> None:
        digest = weekly.bundle_digest(self.bundle)
        (self.bundle / "files/x.txt").write_text("changed\n", encoding="utf-8")
        result = self.publish(digest=digest)
        self.assertEqual(1, result.returncode)
        self.assertIn("made over another bundle", result.stderr)


if __name__ == "__main__":
    unittest.main()

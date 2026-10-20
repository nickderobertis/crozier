"""`tools/fern-goldens/weekly.py`'s offline phases: the plan it makes over the
real reference inventory and timing table, the pair it resolves (over a
stood-in `curl`), how it reads crozier's own reports, and the assembly's
accounting. The journeys that drive the real `git`, the recipe and crozier end
to end are `tools/fern-goldens-git/tests/weekly_git_test.py`'s.
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
from pathlib import Path

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
        return [(entry["family"], entry["item"]) for shard in self.plan["shards"] for entry in shard["items"]]

    def shard_of(self) -> dict[tuple[str, str], int]:
        return {
            (entry["family"], entry["item"]): shard["index"]
            for shard in self.plan["shards"]
            for entry in shard["items"]
        }

    def test_every_item_of_every_family_is_planned_once(self) -> None:
        expected = [(family, item) for family, items in self.inventory.items() for item in items]
        self.assertEqual(sorted(expected), sorted(self.planned()))
        self.assertEqual(len(expected), len(set(self.planned())))
        self.assertTrue(self.plan["complete"])
        self.assertEqual(
            {family: len(items) for family, items in self.inventory.items()},
            {family: entry["items"] for family, entry in self.plan["families"].items()},
        )
        # Every family the recipe defines, so a Fern change to any reference is seen.
        self.assertEqual(set(weekly.references(REPO).FAMILY), set(self.plan["families"]))

    def test_the_shard_count_is_the_fewest_that_fit_the_budget(self) -> None:
        limit = weekly.shard_limit_seconds()
        loads = [shard["seconds"] for shard in self.plan["shards"]]
        self.assertTrue(all(load <= limit / 60 * 60 + 0.1 for load in loads), (loads, limit))
        count = len(loads)
        total = sum(loads)
        weights = self.unit_weights()
        if count > 1:
            # One fewer cannot hold the total, or cannot be packed under the limit.
            fewer = weekly.pack(weights, count - 1)
            self.assertTrue(
                total > (count - 1) * limit or max(sum(weights[i] for i in group) for group in fewer) > limit,
                f"{count - 1} shard(s) would have fitted",
            )
        self.assertEqual(max(1, math.ceil(total / limit)), count, "the packing reached the lower bound")
        self.assertLessEqual(self.plan["estimate"]["minutes"], weekly.BUDGET_MINUTES)
        for shard in self.plan["shards"]:
            self.assertLess(shard["minutes"], weekly.SHARD_TIMEOUT_MINUTES)

    def unit_weights(self) -> list[float]:
        table, default = weekly.timings(REPO)
        return [
            sum(table.get(tuple(key.split("\t")), default) for key in unit)
            for unit in weekly.units(REPO, self.inventory)
        ]

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
        module = weekly.references(REPO)
        handwritten = (REPO / module.HANDWRITTEN).resolve()
        overlaid = 0
        for name, case in module.cases().items():
            base = case.overlay.base if case.overlay else None
            if base is not None and base.resolve().is_relative_to(handwritten):
                fixture = base.resolve().relative_to(handwritten).parts[0]
                with self.subTest(case=name):
                    self.assertEqual(shard[("handwritten", fixture)], shard[("measurements", name)])
                overlaid += 1
        self.assertGreater(overlaid, 10)
        for family in weekly.SHARED_TABLE_FAMILIES:
            with self.subTest(family=family):
                self.assertEqual(1, len({shard[(family, item)] for item in self.inventory[family]}))
        literals = [item for item in self.inventory["measurements"] if item.startswith("parameter-literals/")]
        self.assertEqual(1, len({shard[("measurements", item)] for item in literals}))
        # Within a shard a golden generates before the overlay reduced against it.
        for planned in self.plan["shards"]:
            order = [(entry["family"], entry["item"]) for entry in planned["items"]]
            for index, (family, item) in enumerate(order):
                if family == "overlays":
                    self.assertIn(("corpus", item.split("/")[0]), order[:index])

    def test_an_untimed_item_is_planned_at_the_corpus_rate(self) -> None:
        table, default = weekly.timings(REPO)
        corpus = [seconds for (family, _item), seconds in table.items() if family == "corpus"]
        self.assertTrue(corpus, "the table is seeded with corpus timings")
        self.assertAlmostEqual(sum(corpus) / len(corpus), default)
        handwritten = self.plan["families"]["handwritten"]
        self.assertAlmostEqual(handwritten["seconds"], round(handwritten["items"] * default, 1), delta=1)

    def test_the_budget_the_planner_sizes_against_is_the_registered_one(self) -> None:
        budgets = (REPO / ".github/budgets.yaml").read_text(encoding="utf-8")
        entry = budgets.split("id: crozier-fern-goldens-weekly-minutes", 1)[1].split("\n  - id:", 1)[0]
        self.assertIn(f"threshold: {weekly.BUDGET_MINUTES:g}\n", entry)


class SubsetTests(unittest.TestCase):
    def test_a_subset_plans_exactly_what_it_names(self) -> None:
        made = weekly.make_plan(REPO, "handwritten,corpus:anchore.io", None)
        planned = [(entry["family"], entry["item"]) for shard in made["shards"] for entry in shard["items"]]
        inventory = weekly.inventory(REPO)
        self.assertEqual(
            sorted([("corpus", "anchore.io"), *(("handwritten", item) for item in inventory["handwritten"])]),
            sorted(planned),
        )
        self.assertFalse(made["complete"])

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

    def test_an_unreachable_registry_is_named(self) -> None:
        result, _values = self.resolve("--ref", "refs/heads/main", "--token-present", FAIL="registry.npmjs.org")
        self.assertEqual(1, result.returncode)
        self.assertIn("could not read https://registry.npmjs.org/fern-api", result.stderr)


class ReportTests(unittest.TestCase):
    """How the decision reads `report_fixture_diffs`' own verdict (`just
    fixtures-diff`). `weekly_git_test.py` holds these to the strings that
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
                "a ledger the comparison rejects",
                0,
                self.report("  Comparison processing failed: ledger\n", p=1),
                "reject",
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
        families = set(weekly.references(REPO).FAMILY)
        self.assertEqual(families, {family for gate in gates for family in gate.families})
        commands = {gate.command for gate in gates}
        self.assertEqual(
            {
                "just fixtures-diff {item}",
                "cargo nextest run --locked --no-fail-fast -p crozier-e2e",
                "cargo nextest run --locked --no-fail-fast -p crozier --test refusal_registry",
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
        self.plan = {
            "schema_version": 1,
            "complete": True,
            "items": "",
            "base": "abc",
            "pair": {"cli": "2.0.0", "generator": "3.0.0"},
            "families": {"corpus": {"items": 2, "seconds": 2}},
            "shards": [
                {"index": 0, "items": [{"family": "corpus", "item": "a", "seconds": 1}]},
                {"index": 1, "items": [{"family": "corpus", "item": "b", "seconds": 1}]},
            ],
        }
        (self.scratch / "plan.json").write_text(json.dumps(self.plan), encoding="utf-8")

    def shard(self, index: int, item: str, written: list[str], status: str = "ok") -> None:
        directory = self.scratch / "artifacts" / f"fern-goldens-shard-{index}"
        for path in written:
            (directory / "files" / path).parent.mkdir(parents=True, exist_ok=True)
            (directory / "files" / path).write_text(f"{item}\n", encoding="utf-8")
        record = {
            "schema_version": 1,
            "index": index,
            "pair": self.plan["pair"],
            "base": "abc",
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

    def test_a_shard_listing_a_file_it_does_not_carry_is_a_failure(self) -> None:
        self.shard(0, "a", ["tests/fixtures/a/x.py"])
        self.shard(1, "b", [])
        (self.scratch / "artifacts/fern-goldens-shard-0/files/tests/fixtures/a/x.py").unlink()
        result = self.assemble()
        self.assertEqual(1, result.returncode)
        self.assertIn("shard 0 lists tests/fixtures/a/x.py but its artifact does not carry it", result.stderr)


if __name__ == "__main__":
    unittest.main()

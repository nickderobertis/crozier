"""`output-insensitive-remeasure.py`, run as a process over a scratch checkout.

Fern and crozier are stand-in executables at the subprocess boundary the script
drives (as the weekly journeys stand Fern in): each writes a tree derived from
the document it is given, so two documents with the same `info.title` generate
the same tree and two that differ do not. A document titled `Broken` makes the
stand-in Fern exit 1, one titled `Slow` makes it outlast a short `--timeout`, and
one titled `Flat` makes it exit 0 without a packaged SDK. The stand-in crozier
writes nothing for `Empty`, exits 1 for `Unbuildable` and outlasts the timeout
for `Stalled`. Only the stand-in
crozier reads `info.summary`, so a document differing there alone moves crozier
and not Fern. Each stand-in appends one line per run to `<name>.calls` beside it.
"""

from __future__ import annotations

import csv
import dataclasses
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from types import ModuleType
from typing import Any

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools/surface-census/output-insensitive-remeasure.py"
FIXTURE_RECIPE = REPO / "tools/fern-goldens/generate-fern-fixture.sh"
COLUMNS = ("key", "context", "search_record", "fern_comparison", "crozier_comparison")
PAIR = {"cliVersion": "9.9.9", "generatorVersion": "8.8.8"}  # certified-pair: stand-in
POSIX_ONLY = unittest.skipIf(os.name == "nt", "the stand-in generators are POSIX executables")

FERN = textwrap.dedent(
    """\
    #!{python}
    import json, pathlib, sys, yaml
    args = sys.argv[1:]
    out = pathlib.Path(args[args.index("--output") + 1]) / "fern-python-sdk"
    config = json.loads(pathlib.Path("fern.config.json").read_text())
    assert config == {{"organization": "fern", "version": "9.9.9"}}, config  # certified-pair: stand-in
    assert "version: 8.8.8" in pathlib.Path("generators.yml").read_text()
    document = next(pathlib.Path("openapi").iterdir())
    title = yaml.safe_load(document.read_text())["info"]["title"]
    with pathlib.Path(__file__).with_name("fern.calls").open("a") as calls:
        calls.write(title + "\\n")
    if title == "Broken":
        sys.exit(1)
    if title == "Slow":
        import time
        time.sleep(30)
    if title == "Flat":
        out.mkdir(parents=True)
        (out / "client.py").write_text(title)
        sys.exit(0)
    (out / "src" / "fern").mkdir(parents=True)
    (out / "src" / "fern" / "title.py").write_text(title)
    """
)
CROZIER = textwrap.dedent(
    """\
    #!{python}
    import json, pathlib, sys, yaml
    args = sys.argv[1:]
    out = pathlib.Path(args[args.index("--output") + 1])
    info = yaml.safe_load(pathlib.Path(args[args.index("--spec") + 1]).read_text())["info"]
    title = info["title"]
    with pathlib.Path(__file__).with_name("crozier.calls").open("a") as calls:
        calls.write(title + "\\n")
    if title == "Unbuildable":
        sys.exit(1)
    if title == "Stalled":
        import time
        time.sleep(30)
    out.mkdir(parents=True)
    if title != "Empty":
        (out / "src" / "fern").mkdir(parents=True)
        (out / "src" / "fern" / "title.py").write_text(title + info.get("summary", ""))
    """
)
STALE = '{"stale": true}\n'


def document(title: str, **info: str) -> dict[str, object]:
    return {"openapi": "3.0.3", "info": {"title": title, "version": "1", **info}, "paths": {}}


def load(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class RemeasureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        (self.root / "assets/scaffolding").mkdir(parents=True)
        (self.root / "assets/scaffolding/metadata.json").write_text(json.dumps(PAIR), encoding="utf-8")
        self.surface = self.root / "docs/openapi-surface"
        self.surface.mkdir(parents=True)
        with (self.surface / "output-insensitive.tsv").open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle, delimiter="\t", lineterminator="\n").writerow(COLUMNS)
        for name, before, after in (("steady", "Lanterns", "Lanterns"), ("moving", "Lanterns", "Beacons")):
            self.add_feature(name, before, after)
        self.tools = self.root / "stand-ins"
        self.tools.mkdir()
        for name, body in (("fern", FERN), ("crozier", CROZIER)):
            path = self.tools / name
            path.write_text(body.format(python=sys.executable), encoding="utf-8")
            path.chmod(0o755)

    def add_row(self, key: str, folder: Path, name: str) -> str:
        """A row citing `folder/README.md` and the records `name` spells with
        `{generator}` as `fern` and `crozier`."""
        (folder / "README.md").write_text(f"`{key}`\n", encoding="utf-8")
        fern, crozier = (name.format(generator=generator) for generator in ("fern", "crozier"))
        for record in (fern, crozier):
            (folder / record).write_text(STALE, encoding="utf-8")
        relative = folder.relative_to(self.root).as_posix()
        with (self.surface / "output-insensitive.tsv").open("a", encoding="utf-8") as handle:
            handle.write(f"{key}\t-\t{relative}/README.md\t{relative}/{fern}\t{relative}/{crozier}\n")
        return f"{relative}/{fern}"

    def add_feature(self, name: str, before: str | dict[str, object], after: str | dict[str, object]) -> str:
        """A feature search's attribution: its own folder, `before.json` and `after.json`
        (a title, or a whole document)."""
        folder = self.surface / f"witness-search-unproven-features/{name}-attribution"
        folder.mkdir(parents=True)
        for side, content in (("before", before), ("after", after)):
            body = document(content) if isinstance(content, str) else content
            (folder / f"{side}.json").write_text(json.dumps(body), encoding="utf-8")
        return self.add_row(f"{name}-key", folder, "{generator}-comparison.json")

    def add_control(self, control: object, *, stem: str = "harbour-combo-lit") -> str:
        """A combination search's control beside its from-scratch document, as an
        edit record or as the ablated document itself."""
        folder = self.surface / "witness-search-operation-combinations-lanterns"
        (folder / "removal-controls").mkdir(parents=True, exist_ok=True)
        source = "openapi: 3.0.3\ninfo:\n  title: Lanterns\n  version: '1'\n  description: Lit nightly.\n"
        source += "  x-a/b: slash\n  x-c~d: tilde\npaths: {}\ntags: [{name: one}, {name: two}]\n"
        (folder / "removal-controls/harbour.yml").write_text(source, encoding="utf-8")
        (folder / f"removal-controls/{stem}.json").write_text(json.dumps(control), encoding="utf-8")
        return self.add_row(stem, folder, f"{stem}-{{generator}}.json")

    def ablations(self, stem: str) -> list[Path]:
        """The after documents the re-measure derived from edit records named `stem`."""
        return sorted((self.root / "logs/output-insensitive-remeasure/ablations").glob(f"*-{stem}.after.json"))

    def ablation(self, stem: str) -> Path:
        (path,) = self.ablations(stem)
        return path

    def edits(self, *edits: object, fixture: str = "harbour") -> dict[str, object]:
        return {"key": "combo-lit", "fixture": fixture, "edits": list(edits)}

    def run_script(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--root",
                str(self.root),
                "--fern",
                str(self.tools / "fern"),
                "--crozier",
                str(self.tools / "crozier"),
                *args,
            ],
            capture_output=True,
            text=True,
            env={**os.environ, "ONEPIPELINE_NODE_SCRATCH_DIR": str(self.root / "logs")},
            check=False,
        )

    # A comparison record read back from disk: JSON whose shape is what each test asserts.
    def read(self, record: str) -> dict[str, Any]:
        return json.loads((self.root / record).read_text(encoding="utf-8"))

    def feature_record(self, name: str, generator: str) -> dict[str, Any]:
        return self.read(
            f"docs/openapi-surface/witness-search-unproven-features/{name}-attribution/{generator}-comparison.json"
        )

    @POSIX_ONLY
    def test_a_record_whose_trees_differ_is_refused_and_a_steady_one_is_rewritten_at_the_pair(self) -> None:
        result = self.run_script()
        self.assertEqual(1, result.returncode, result.stderr)
        for generator in ("fern", "crozier"):
            steady = self.feature_record("steady", generator)
            self.assertEqual(
                (generator, "9.9.9", "8.8.8"),
                (steady["generator"], steady["fern_cli_version"], steady["fern_python_sdk_version"]),
            )
            self.assertEqual(steady["before"], steady["after"])
            self.assertEqual(["src/fern/title.py"], list(steady["before"]))
            self.assertEqual({"stale": True}, self.feature_record("moving", generator))
            self.assertIn(
                f"moving-attribution/fern-comparison.json: {generator} moves src/fern/title.py", result.stderr
            )
        self.assertIn("removed moving-key at -", result.stderr)
        table = (self.surface / "output-insensitive.tsv").read_text(encoding="utf-8")
        self.assertIn("steady-key", table)
        self.assertNotIn("moving-key", table)
        self.assertEqual(0, self.run_script().returncode)
        # What it writes is what output-insensitive.py accepts at this pair.
        reader = load("output_insensitive", REPO / "tools/surface-census/output-insensitive.py")
        self.assertEqual(
            ([], {("steady-key", "-")}), (reader.read_records(self.root)[1], reader.read_records(self.root)[0])
        )

    @POSIX_ONLY
    def test_a_difference_in_one_generator_alone_removes_the_disposition(self) -> None:
        self.add_feature("summarised", document("Lanterns", summary="Lit"), document("Lanterns"))
        result = self.run_script()
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertIn("summarised-attribution/fern-comparison.json: crozier moves src/fern/title.py", result.stderr)
        self.assertNotIn("summarised-attribution/fern-comparison.json: fern moves", result.stderr)
        self.assertIn("removed summarised-key at -", result.stderr)
        self.assertEqual({"stale": True}, self.feature_record("summarised", "fern"))

    @POSIX_ONLY
    def test_a_document_two_controls_share_is_generated_once_and_each_ablation_apart(self) -> None:
        records = [
            self.add_control(self.edits({"pointer": "/info/description", "edit": "deleted it"})),
            self.add_control(self.edits({"pointer": "/tags/1", "edit": "deleted it"}), stem="harbour-combo-tags"),
        ]
        result = self.run_script(*(argument for record in records for argument in ("--only", record)))
        self.assertEqual(0, result.returncode, result.stderr)
        for name in ("fern", "crozier"):
            self.assertEqual(3, len((self.tools / f"{name}.calls").read_text().splitlines()), name)
        self.assertNotEqual(
            self.ablation("harbour-combo-lit").read_text(), self.ablation("harbour-combo-tags").read_text()
        )

    @POSIX_ONLY
    def test_an_escaped_pointer_deletes_the_key_it_spells(self) -> None:
        record = self.add_control(
            self.edits(
                {"pointer": "/info/x-a~1b", "edit": "deleted the slash key"},
                {"pointer": "/info/x-c~0d", "edit": "deleted the tilde key"},
            )
        )
        result = self.run_script("--only", record)
        self.assertEqual(0, result.returncode, result.stderr)
        after = json.loads(self.ablation("harbour-combo-lit").read_text())
        self.assertNotIn("x-a/b", after["info"])
        self.assertNotIn("x-c~d", after["info"])
        self.assertEqual("Lit nightly.", after["info"]["description"])

    @POSIX_ONLY
    def test_a_generator_that_fails_or_stalls_keeps_its_record_and_row(self) -> None:
        for name, title, reason in (
            ("flat", "Flat", "without a packaged SDK"),
            ("unbuildable", "Unbuildable", "crozier exited 1"),
            ("stalled", "Stalled", "timed out after 2 seconds"),
        ):
            with self.subTest(name):
                self.add_feature(name, title, title)
                record = (
                    f"docs/openapi-surface/witness-search-unproven-features/{name}-attribution/fern-comparison.json"
                )
                result = self.run_script("--timeout", "2", "--only", record)
                self.assertEqual(1, result.returncode, result.stderr)
                self.assertIn(f"{name}-attribution/fern-comparison.json: ", result.stderr)
                self.assertIn(reason, result.stderr)
                for generator in ("fern", "crozier"):
                    self.assertEqual({"stale": True}, self.feature_record(name, generator))
                self.assertIn(f"{name}-key", (self.surface / "output-insensitive.tsv").read_text(encoding="utf-8"))

    def test_a_table_whose_header_is_not_the_shared_columns_is_refused(self) -> None:
        table = self.surface / "output-insensitive.tsv"
        table.write_text(table.read_text(encoding="utf-8").replace("search_record", "search", 1), encoding="utf-8")
        result = self.run_script()
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("expected columns", result.stderr)

    def test_a_record_with_no_documents_beside_it_is_refused(self) -> None:
        folder = self.surface / "witness-search-schema-combinations-orphans"
        (folder / "removal-controls").mkdir(parents=True)
        record = self.add_row("combo-orphan", folder, "orphan-combo-x-{generator}.json")
        result = self.run_script("--only", record)
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("orphan-combo-x-fern.json: no before/after documents resolve beside it", result.stderr)

    def test_an_unbuilt_crozier_is_a_usage_error(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root), "--crozier", str(self.root / "missing/crozier")],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("missing/crozier is not built; run `cargo build --release --locked`", result.stderr)

    @POSIX_ONLY
    def test_a_generation_past_the_timeout_keeps_that_record_and_measures_the_rest(self) -> None:
        self.add_feature("slow", "Slow", "Slow")
        result = self.run_script("--timeout", "2")
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertIn("slow-attribution/fern-comparison.json: ", result.stderr)
        self.assertIn("timed out after 2 seconds", result.stderr)
        self.assertEqual({"stale": True}, self.feature_record("slow", "fern"))
        self.assertIn("slow-key", (self.surface / "output-insensitive.tsv").read_text(encoding="utf-8"))
        self.assertEqual("9.9.9", self.feature_record("steady", "fern")["fern_cli_version"])

    def test_a_fern_command_or_timeout_that_cannot_run_is_a_usage_error(self) -> None:
        for args, reason in (
            (("--fern", ""), "--fern names no command"),
            (("--fern", "'unclosed"), "is no command"),
            (("--timeout", "0"), "--timeout is a positive number of seconds"),
        ):
            with self.subTest(args=args):
                result = self.run_script(*args)
                self.assertEqual(2, result.returncode, result.stderr)
                self.assertIn(reason, result.stderr)

    @POSIX_ONLY
    def test_a_generator_failure_keeps_that_record_and_its_row_and_measures_the_rest(self) -> None:
        self.add_feature("broken", "Broken", "Broken")
        self.add_feature("empty", "Empty", "Empty")
        result = self.run_script()
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertIn("broken-attribution/fern-comparison.json: fern exited 1", result.stderr)
        self.assertIn("empty-attribution/fern-comparison.json: ", result.stderr)
        self.assertIn("holds no generated file", result.stderr)
        for name in ("broken", "empty"):
            for generator in ("fern", "crozier"):
                self.assertEqual({"stale": True}, self.feature_record(name, generator))
        table = (self.surface / "output-insensitive.tsv").read_text(encoding="utf-8")
        self.assertIn("broken-key", table)
        self.assertIn("empty-key", table)
        self.assertEqual("9.9.9", self.feature_record("steady", "fern")["fern_cli_version"])

    def test_a_record_whose_documents_do_not_resolve_is_refused_before_any_generation(self) -> None:
        (self.surface / "witness-search-unproven-features/steady-attribution/after.json").unlink()
        result = self.run_script()
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("steady-attribution/fern-comparison.json: a fern record is named `*-fern.json`", result.stderr)
        self.assertEqual({"stale": True}, self.feature_record("moving", "fern"))
        self.assertFalse(any((self.root / "logs").rglob("*.fern.log")))

    def test_a_row_that_is_incomplete_or_names_evidence_outside_the_documentation_is_refused(self) -> None:
        table = self.surface / "output-insensitive.tsv"
        original = table.read_text(encoding="utf-8")
        for broken, reason in (
            (original + "half-key\t-\t\t\t\n", "a row fills every column"),
            (
                original.replace("docs/openapi-surface/witness-search-unproven-features/steady", "../steady", 1),
                "invalid evidence path",
            ),
        ):
            with self.subTest(reason=reason):
                table.write_text(broken, encoding="utf-8")
                result = self.run_script()
                self.assertEqual(2, result.returncode, result.stderr)
                self.assertIn(reason, result.stderr)
                self.assertEqual({"stale": True}, self.feature_record("steady", "fern"))
        table.write_text(original, encoding="utf-8")
        (self.root / "assets/scaffolding/metadata.json").write_text('["no", "pair"]', encoding="utf-8")
        result = self.run_script()
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("names no certified pair", result.stderr)

    @POSIX_ONLY
    def test_an_edit_record_is_measured_as_its_document_with_each_pointer_deleted(self) -> None:
        record = self.add_control(
            self.edits(
                {"pointer": "/info/description", "edit": "deleted the description"},
                {"pointer": "/tags/1", "edit": "deleted the second tag"},
            )
        )
        result = self.run_script("--only", record)
        self.assertEqual(0, result.returncode, result.stderr)
        rewritten = self.read(record)
        self.assertEqual(rewritten["before"], rewritten["after"])
        after = json.loads(self.ablation("harbour-combo-lit").read_text())
        self.assertNotIn("description", after["info"])
        self.assertEqual([{"name": "one"}], after["tags"])
        self.assertEqual("Lanterns", after["info"]["title"])

    def test_an_edit_record_that_does_not_describe_deletions_it_can_make_is_refused(self) -> None:
        deletion = {"pointer": "/info/description", "edit": "deleted the description"}
        for name, control, reason in (
            (
                "renamed",
                self.edits({**deletion, "edit": "renamed the description"}),
                "is not a deletion at a JSON pointer",
            ),
            (
                "unpointed",
                self.edits({**deletion, "pointer": "info/description"}),
                "is not a deletion at a JSON pointer",
            ),
            ("scalar", self.edits("deleted everything"), "is not a deletion at a JSON pointer"),
            ("absent", self.edits({**deletion, "pointer": "/info/summary"}), "/info/summary names nothing"),
            ("bad-escape", self.edits({**deletion, "pointer": "/info/a~2b"}), "is not a deletion at a JSON pointer"),
            (
                "trailing-tilde",
                self.edits({**deletion, "pointer": "/info/description~"}),
                "is not a deletion at a JSON pointer",
            ),
            ("negative", self.edits({**deletion, "pointer": "/tags/-1"}), "/tags/-1 names nothing"),
            ("past-the-end", self.edits({**deletion, "pointer": "/tags/2/name"}), "/tags/2/name names nothing"),
            ("other-fixture", self.edits(deletion, fixture="quay"), "names its fixture 'harbour'"),
            ("no-edits", self.edits(), "names its fixture 'harbour' and at least one edit"),
            ("list", [deletion], "names its fixture 'harbour' and at least one edit"),
        ):
            with self.subTest(name):
                record = self.add_control(control, stem=f"harbour-combo-{name}")
                result = self.run_script("--only", record)
                self.assertEqual(2, result.returncode, result.stderr)
                self.assertIn(reason, result.stderr)
                self.assertEqual({"stale": True}, self.read(record))
                with (self.surface / "output-insensitive.tsv").open(encoding="utf-8") as handle:
                    rows = handle.read().splitlines()
                (self.surface / "output-insensitive.tsv").write_text(
                    "\n".join(line for line in rows if not line.startswith(f"harbour-combo-{name}\t")) + "\n",
                    encoding="utf-8",
                )

    @POSIX_ONLY
    def test_a_control_that_is_itself_the_ablated_document_is_measured_as_written(self) -> None:
        record = self.add_control(document("Lanterns"))
        result = self.run_script("--only", record)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("9.9.9", self.read(record)["fern_cli_version"])
        self.assertEqual([], self.ablations("harbour-combo-lit"))

    @POSIX_ONLY
    def test_a_corpus_source_control_is_measured_against_its_after_document(self) -> None:
        source = self.root / "tests/fixtures/corpus-sources/quayside/openapi.yaml"
        source.parent.mkdir(parents=True)
        source.write_text("openapi: 3.0.3\ninfo: {title: Quays, version: '1'}\npaths: {}\n", encoding="utf-8")
        folder = self.surface / "witness-search-schema-combinations-quays"
        (folder / "removal-controls").mkdir(parents=True)
        after = "openapi: 3.1.0\ninfo: {title: Quays, version: '1'}\npaths: {}\n"
        (folder / "removal-controls/quayside-after.yml").write_text(after, encoding="utf-8")
        record = self.add_row("combo-quay", folder, "quayside-version-removal-{generator}.json")
        result = self.run_script("--only", record)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(["src/fern/title.py"], list(self.read(record)["after"]))

    @POSIX_ONLY
    def test_two_searches_filing_a_control_under_one_stem_are_measured_apart(self) -> None:
        records = [self.add_control(self.edits({"pointer": "/info/description", "edit": "deleted it"}))]
        other = self.surface / "witness-search-schema-combinations-lanterns"
        (other / "removal-controls").mkdir(parents=True)
        source = "openapi: 3.0.3\ninfo:\n  title: Beacons\n  version: '1'\n  description: Lit nightly.\npaths: {}\n"
        (other / "removal-controls/harbour.yml").write_text(source, encoding="utf-8")
        control = self.edits({"pointer": "/info/description", "edit": "deleted it"})
        (other / "removal-controls/harbour-combo-lit.json").write_text(json.dumps(control), encoding="utf-8")
        records.append(self.add_row("harbour-combo-lit-beacons", other, "harbour-combo-lit-{generator}.json"))
        result = self.run_script(*(argument for record in records for argument in ("--only", record)))
        self.assertEqual(0, result.returncode, result.stderr)
        titles = sorted(json.loads(path.read_text())["info"]["title"] for path in self.ablations("harbour-combo-lit"))
        self.assertEqual(["Beacons", "Lanterns"], titles)
        self.assertNotEqual(self.read(records[0])["after"], self.read(records[1])["after"])

    def test_a_row_with_a_malformed_or_repeated_key_is_refused(self) -> None:
        table = self.surface / "output-insensitive.tsv"
        original = table.read_text(encoding="utf-8")
        steady = next(line for line in original.splitlines() if line.startswith("steady-key\t"))
        for broken, reason in (
            (original.replace("steady-key\t", "Steady_Key\t", 1), "'Steady_Key' is no census key"),
            (original + steady + "\n", "steady-key at - is filed twice"),
        ):
            with self.subTest(reason=reason):
                table.write_text(broken, encoding="utf-8")
                result = self.run_script()
                self.assertEqual(2, result.returncode, result.stderr)
                self.assertIn(reason, result.stderr)
                self.assertEqual({"stale": True}, self.feature_record("steady", "fern"))

    def test_a_pair_that_is_not_two_releases_is_refused(self) -> None:
        for name, pair in (
            ("empty", {"cliVersion": "", "generatorVersion": "8.8.8"}),  # certified-pair: stand-in
            ("multiline", {"cliVersion": "9.9.9\n", "generatorVersion": "8.8.8"}),  # certified-pair: stand-in
            ("partial", {"cliVersion": "9.9.9", "generatorVersion": "8.8"}),  # certified-pair: stand-in
        ):
            with self.subTest(name):
                (self.root / "assets/scaffolding/metadata.json").write_text(json.dumps(pair), encoding="utf-8")
                result = self.run_script()
                self.assertEqual(2, result.returncode, result.stderr)
                self.assertIn("is no MAJOR.MINOR.PATCH release", result.stderr)

    def test_a_log_directory_that_cannot_be_made_is_a_usage_error(self) -> None:
        blocker = self.root / "not-a-directory"
        blocker.write_text("", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root), "--crozier", str(self.tools / "crozier")],
            capture_output=True,
            text=True,
            env={**os.environ, "ONEPIPELINE_NODE_SCRATCH_DIR": str(blocker)},
            check=False,
        )
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("cannot create the log directory", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    @POSIX_ONLY
    @unittest.skipIf(hasattr(os, "geteuid") and os.geteuid() == 0, "root writes through read-only modes")
    def test_a_record_or_table_that_cannot_be_written_is_reported_not_a_traceback(self) -> None:
        steady = self.surface / "witness-search-unproven-features/steady-attribution/fern-comparison.json"
        steady.chmod(0o444)
        self.addCleanup(steady.chmod, 0o644)
        table = self.surface / "output-insensitive.tsv"
        table.chmod(0o444)
        self.addCleanup(table.chmod, 0o644)
        result = self.run_script()
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn("steady-attribution/fern-comparison.json was not written", result.stderr)
        self.assertIn("output-insensitive.tsv was not rewritten, so no row was removed", result.stderr)
        self.assertNotIn("removed moving-key", result.stderr)
        self.assertIn("moving-key", table.read_text(encoding="utf-8"))

    def test_an_unknown_only_record_is_a_usage_error(self) -> None:
        result = self.run_script("--only", "docs/openapi-surface/nowhere-fern.json")
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("--only names no record", result.stderr)


class RowContractTests(unittest.TestCase):
    def test_the_row_record_is_the_shared_table_s_columns_in_order(self) -> None:
        remeasure = load("remeasure_row", SCRIPT)
        reader = load("output_insensitive_columns", REPO / "tools/surface-census/output-insensitive.py")
        self.assertEqual(reader.COLUMNS, tuple(field.name for field in dataclasses.fields(remeasure.Row)))


class WorkspaceDriftTests(unittest.TestCase):
    """The workspace Fern re-measures in is the packaged python-enums workspace
    `generate-fern-fixture.sh` scaffolds for a golden; this holds the two to one
    shape, so a change to the fixture recipe fails here until the re-measure follows."""

    def test_the_generators_yml_is_the_fixture_recipe_s_with_its_options_unset(self) -> None:
        recipe = FIXTURE_RECIPE.read_text(encoding="utf-8")
        template = re.search(r'cat > "\$workdir/fern/generators.yml" <<YAML\n(.*?)\nYAML\n', recipe, re.S)
        self.assertIsNotNone(template, "generate-fern-fixture.sh writes generators.yml from a heredoc")
        assert template is not None
        rendered = (
            template.group(1)
            .replace("${api_path}", "openapi/{name}")
            .replace("${audiences_block}", "")
            .replace("${FERN_PYTHON_VERSION}", "{version}")
            .replace("${client_class_name_block}${default_max_retries_block}", "")
            .replace("${pydantic_config_block}", "          pydantic_config:\n            enum_type: python_enums\n")
        )
        module = load("remeasure", SCRIPT)
        self.assertEqual(rendered + "\n", module.GENERATORS_YML)
        self.assertIn('{ "organization": "${ORGANIZATION:-fern}", "version": "${FERN_CLI_VERSION}" }', recipe)
        self.assertIn('export FERN_TOKEN="${FERN_TOKEN:-preview-only-no-publish}"', recipe)
        self.assertIn("run_fern --local --preview --output", recipe)


if __name__ == "__main__":
    unittest.main()

"""`output-insensitive-remeasure.py`, run as a process over a scratch checkout.

Fern and crozier are stand-in executables at the subprocess boundary the script
drives (as the weekly journeys stand Fern in): each writes a tree derived from
the document it is given, so two documents with the same `info.title` generate
the same tree and two that differ do not. A document titled `Broken` makes the
stand-in Fern exit 1, and one titled `Empty` makes the stand-in crozier write
nothing.
"""

from __future__ import annotations

import csv
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
    assert config == {{"organization": "fern", "version": "9.9.9"}}, config
    assert "version: 8.8.8" in pathlib.Path("generators.yml").read_text()
    document = next(pathlib.Path("openapi").iterdir())
    title = yaml.safe_load(document.read_text())["info"]["title"]
    if title == "Broken":
        sys.exit(1)
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
    title = yaml.safe_load(pathlib.Path(args[args.index("--spec") + 1]).read_text())["info"]["title"]
    out.mkdir(parents=True)
    if title != "Empty":
        (out / "src" / "fern").mkdir(parents=True)
        (out / "src" / "fern" / "title.py").write_text(title)
    """
)
STALE = '{"stale": true}\n'


def document(title: str, **info: str) -> dict[str, Any]:
    return {"openapi": "3.0.3", "info": {"title": title, "version": "1", **info}, "paths": {}}


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

    def add_feature(self, name: str, before: str, after: str) -> str:
        """A feature search's attribution: its own folder, `before.json` and `after.json`."""
        folder = self.surface / f"witness-search-unproven-features/{name}-attribution"
        folder.mkdir(parents=True)
        (folder / "before.json").write_text(json.dumps(document(before)), encoding="utf-8")
        (folder / "after.json").write_text(json.dumps(document(after)), encoding="utf-8")
        return self.add_row(f"{name}-key", folder, "{generator}-comparison.json")

    def add_control(self, control: object, *, stem: str = "harbour-combo-lit") -> str:
        """A combination search's control beside its from-scratch document, as an
        edit record or as the ablated document itself."""
        folder = self.surface / "witness-search-operation-combinations-lanterns"
        (folder / "removal-controls").mkdir(parents=True, exist_ok=True)
        source = "openapi: 3.0.3\ninfo:\n  title: Lanterns\n  version: '1'\n  description: Lit nightly.\n"
        source += "paths: {}\ntags: [{name: one}, {name: two}]\n"
        (folder / "removal-controls/harbour.yml").write_text(source, encoding="utf-8")
        (folder / f"removal-controls/{stem}.json").write_text(json.dumps(control), encoding="utf-8")
        return self.add_row(stem, folder, f"{stem}-{{generator}}.json")

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
        after = json.loads(
            (self.root / "logs/output-insensitive-remeasure/ablations/harbour-combo-lit.after.json").read_text()
        )
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
        self.assertFalse(
            (self.root / "logs/output-insensitive-remeasure/ablations/harbour-combo-lit.after.json").exists()
        )

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

    def test_an_unknown_only_record_is_a_usage_error(self) -> None:
        result = self.run_script("--only", "docs/openapi-surface/nowhere-fern.json")
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("--only names no record", result.stderr)


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
        spec = importlib.util.spec_from_file_location("remeasure", SCRIPT)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        self.assertEqual(rendered + "\n", module.GENERATORS_YML)
        self.assertIn('{ "organization": "${ORGANIZATION:-fern}", "version": "${FERN_CLI_VERSION}" }', recipe)
        self.assertIn('export FERN_TOKEN="${FERN_TOKEN:-preview-only-no-publish}"', recipe)
        self.assertIn("run_fern --local --preview --output", recipe)


if __name__ == "__main__":
    unittest.main()

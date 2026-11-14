"""`output-insensitive-remeasure.py`, run as a process over a scratch checkout.

Fern and crozier are stand-in executables at the subprocess boundary the script
drives (as the weekly journeys stand Fern in): each writes a tree derived from
the document it is given, so two documents with the same `info.title` generate
the same tree and two that differ do not.
"""

from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools/surface-census/output-insensitive-remeasure.py"
COLUMNS = ("key", "context", "search_record", "fern_comparison", "crozier_comparison")
PAIR = {"cliVersion": "9.9.9", "generatorVersion": "8.8.8"}  # certified-pair: stand-in

# Writes `<output>/fern-python-sdk/src/fern/title.py` holding the document's title.
FERN = textwrap.dedent(
    """\
    #!{python}
    import json, pathlib, sys
    args = sys.argv[1:]
    out = pathlib.Path(args[args.index("--output") + 1]) / "fern-python-sdk"
    config = json.loads(pathlib.Path("fern.config.json").read_text())
    assert config == {{"organization": "fern", "version": "9.9.9"}}, config
    assert "version: 8.8.8" in pathlib.Path("generators.yml").read_text()
    document = next(pathlib.Path("openapi").iterdir())
    (out / "src" / "fern").mkdir(parents=True)
    (out / "src" / "fern" / "title.py").write_text(json.loads(document.read_text())["info"]["title"])
    """
)
CROZIER = textwrap.dedent(
    """\
    #!{python}
    import json, pathlib, sys
    args = sys.argv[1:]
    out = pathlib.Path(args[args.index("--output") + 1])
    title = json.loads(pathlib.Path(args[args.index("--spec") + 1]).read_text())["info"]["title"]
    (out / "src" / "fern").mkdir(parents=True)
    (out / "src" / "fern" / "title.py").write_text(title)
    """
)


def document(title: str) -> str:
    return json.dumps({"openapi": "3.0.3", "info": {"title": title, "version": "1"}, "paths": {}})


class RemeasureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        (self.root / "assets/scaffolding").mkdir(parents=True)
        (self.root / "assets/scaffolding/metadata.json").write_text(json.dumps(PAIR), encoding="utf-8")
        self.surface = self.root / "docs/openapi-surface"
        rows = []
        for name, before, after in (("steady", "Lanterns", "Lanterns"), ("moving", "Lanterns", "Beacons")):
            folder = self.surface / f"witness-search-unproven-features/{name}-attribution"
            folder.mkdir(parents=True)
            (folder / "before.json").write_text(document(before), encoding="utf-8")
            (folder / "after.json").write_text(document(after), encoding="utf-8")
            (folder / "README.md").write_text(f"`{name}-key`\n", encoding="utf-8")
            for generator in ("fern", "crozier"):
                (folder / f"{generator}-comparison.json").write_text('{"stale": true}\n', encoding="utf-8")
            relative = folder.relative_to(self.root).as_posix()
            rows.append(
                {
                    "key": f"{name}-key",
                    "context": "-",
                    "search_record": f"{relative}/README.md",
                    "fern_comparison": f"{relative}/fern-comparison.json",
                    "crozier_comparison": f"{relative}/crozier-comparison.json",
                }
            )
        with (self.surface / "output-insensitive.tsv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, COLUMNS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        self.tools = self.root / "stand-ins"
        self.tools.mkdir()
        for name, body in (("fern", FERN), ("crozier", CROZIER)):
            path = self.tools / name
            path.write_text(body.format(python=sys.executable), encoding="utf-8")
            path.chmod(0o755)

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

    def record(self, name: str, generator: str) -> dict[str, Any]:
        path = self.surface / f"witness-search-unproven-features/{name}-attribution/{generator}-comparison.json"
        return json.loads(path.read_text(encoding="utf-8"))

    @unittest.skipIf(os.name == "nt", "the stand-in generators are POSIX executables")
    def test_a_record_whose_trees_differ_is_refused_and_a_steady_one_is_rewritten_at_the_pair(self) -> None:
        result = self.run_script()
        self.assertEqual(1, result.returncode, result.stderr)
        for generator in ("fern", "crozier"):
            steady = self.record("steady", generator)
            self.assertEqual(
                (generator, "9.9.9", "8.8.8"),
                (steady["generator"], steady["fern_cli_version"], steady["fern_python_sdk_version"]),
            )
            self.assertEqual(steady["before"], steady["after"])
            self.assertEqual(["src/fern/title.py"], list(steady["before"]))
            # The moving record is never restated.
            self.assertEqual({"stale": True}, self.record("moving", generator))
            self.assertIn(
                f"moving-attribution/fern-comparison.json: {generator} moves src/fern/title.py", result.stderr
            )
        self.assertIn("removed moving-key at -", result.stderr)
        table = (self.surface / "output-insensitive.tsv").read_text(encoding="utf-8")
        self.assertIn("steady-key", table)
        self.assertNotIn("moving-key", table)
        # Run again: the steady record alone remains and is rewritten cleanly.
        again = self.run_script()
        self.assertEqual(0, again.returncode, again.stderr)

    @unittest.skipIf(os.name == "nt", "the stand-in generators are POSIX executables")
    def test_a_record_whose_documents_do_not_resolve_is_refused_before_any_generation(self) -> None:
        (self.surface / "witness-search-unproven-features/steady-attribution/after.json").unlink()
        result = self.run_script()
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("steady-attribution/fern-comparison.json: a fern record is named `*-fern.json`", result.stderr)
        self.assertEqual({"stale": True}, self.record("moving", "fern"))
        self.assertFalse((self.root / "logs").exists() and any((self.root / "logs").rglob("*.log")))

    def test_an_unknown_only_record_is_a_usage_error(self) -> None:
        result = self.run_script("--only", "docs/openapi-surface/nowhere-fern.json")
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertIn("--only names no record", result.stderr)


if __name__ == "__main__":
    unittest.main()

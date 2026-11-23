"""`tools/fern-goldens/fern-references.py` driven the way a maintainer runs it: as a
subprocess over a scratch repository, with a stand-in `fern` on PATH and a
stand-in release crozier whose `internal-strip` drops comment lines.

The stand-in `fern` builds its output from the workspace the tool scaffolds: it
records `fern.config.json` and `generators.yml`, emits `core/enum.py` only when
`generators.yml` asks for `python_enums`, fetches any URL the document names,
and refuses a document carrying `x-stub-refuse` the way Fern prints a refusal.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType

os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[3]
TOOL = REPO / "tools" / "fern-goldens" / "fern-references.py"

STUB_FERN = r"""#!/usr/bin/env python3
import json, os, re, sys, urllib.request
from pathlib import Path
workspace = Path.cwd()
config = (workspace / "fern.config.json").read_text()
generators = (workspace / "generators.yml").read_text()
document = (workspace / "openapi" / "openapi.yml").read_text()
with open(os.environ["FERN_STUB_LOG"], "a") as log:
    log.write(json.dumps({"argv": sys.argv[1:], "config": json.loads(config), "generators": generators, "token": os.environ.get("FERN_TOKEN")}) + "\n")
if sys.argv[1] == "check":
    if "x-stub-refuse" in document:
        print("[sdk] 1 error\n    [error]\n        path: openapi\n        issue: Stub refused the document")
        sys.exit(1)
    print("All checks passed")
    sys.exit(0)
if "x-stub-crash" in document:
    print("Traceback (most recent call last):\n    raise KeyError(key)\n  KeyError: 'type_:Probe'")
    sys.exit(1)
if "x-stub-empty" in document:
    print("[api]: python-sdk Finished.")
    sys.exit(0)
if "x-stub-error-line" in document:
    print("Error: the definition could not be read")
    sys.exit(1)
if "x-stub-failed-to" in document:
    print("[api]: python-sdk Failed to load the API definition")
    sys.exit(1)
if "x-stub-silent" in document:
    print("[api]: python-sdk something went sideways")
    sys.exit(1)
if "x-stub-refuse" in document:
    print(f"[api]: python-sdk Generator logs here: /tmp/tmp-stub-1\n[api]: python-sdk {workspace}\n                  [error] Stub refused the document")
    sys.exit(1)
if "x-stub-partial" in document:
    partial = Path(sys.argv[sys.argv.index("--output") + 1]) / "fern-python-sdk" / "src" / "fern" if "--preview" in sys.argv else workspace.parent / "generated" / "python"
    partial.mkdir(parents=True)
    (partial / "client.py").write_text("PARTIAL = 1\n")
    print("[api]: python-sdk wrote some files\n                  [error] Stub refused the document")
    sys.exit(1)
if "--preview" in sys.argv:
    root = Path(sys.argv[sys.argv.index("--output") + 1]) / "fern-python-sdk"
    package = root / "src" / "fern"
else:
    root = workspace.parent / "generated" / "python"
    package = root
version = re.search(r"version: (\S+)", generators).group(1)
package.mkdir(parents=True)
(package / "client.py").write_text("# a comment Fern writes\nCLIENT = 1\n")
if "x-stub-raw-client" in document:
    (package / "raw_client.py").write_text("# a comment Fern writes\nRAW = 1\n")
(package / "core").mkdir()
if "enum_type: python_enums" in generators:
    (package / "core" / "enum.py").write_text("ENUM = 1\n")
else:
    (package / "literal.py").write_text("LITERAL = 1\n")
for audience in re.findall(r"^      - (\w+)$", generators, re.M):
    (package / f"audience_{audience}.py").write_text("AUDIENCE = 1\n")
for url in re.findall(r"http://127\.0\.0\.1:\d+/\S+?\.yml", document):
    # llmlint: ignore[async_typed_clients_at_boundaries] This stands in for Fern's own resolver fetching a remote $ref, inside an executable stub script; it reads one loopback URL the tool under test serves and has no client boundary to type.
    (package / "remote.txt").write_text(urllib.request.urlopen(url).read().decode())
(root / ".fern").mkdir(parents=True, exist_ok=True)
metadata = {
    "cliVersion": json.loads(config)["version"],
    # A case may have this stand-in record another generator, as a tree the store refuses.
    "generatorName": os.environ.get("FERN_STAND_IN_GENERATOR", "fernapi/fern-python-sdk"),
    "generatorVersion": version,
}
if "enum_type: python_enums" in generators:
    metadata["generatorConfig"] = {"pydantic_config": {"enum_type": "python_enums"}}
(root / ".fern" / "metadata.json").write_text(json.dumps(metadata))
print(f"[api]: python-sdk Wrote files to {root}")
"""

# A delegated script: records what it was run with, then exits as told.
STUB_DELEGATE = r"""#!/usr/bin/env python3
import json, os, sys
from pathlib import Path
with open(os.environ["DELEGATE_LOG"], "a") as log:
    log.write(json.dumps({"script": Path(sys.argv[0]).name, "argv": sys.argv[1:], "cli": os.environ.get("FERN_CLI_VERSION")}) + "\n")
print("delegate ran")
if os.environ.get("DELEGATE_CHANGES") and "--changes" in sys.argv:
    # What `fern-refusals.py probe --changes` writes for a probe whose outcome changed.
    Path(sys.argv[sys.argv.index("--changes") + 1]).write_text(os.environ["DELEGATE_CHANGES"], encoding="utf-8")
sys.exit(int(os.environ.get("DELEGATE_EXIT", "0")))
"""

STUB_CROZIER = r"""#!/usr/bin/env python3
import sys
assert sys.argv[1] == "internal-strip"
sys.stdout.write("".join(l for l in open(sys.argv[2]) if not l.startswith("#")))
"""

# A stand-in pair the scratch repository certifies, never the real one, so each
# assertion shows the tool read the pair from the scratch metadata.json.
CLI, SDK, OLD = "9.8.7", "6.5.4", "1.0.0"
METADATA = {"cliVersion": CLI, "generatorName": "fernapi/fern-python-sdk", "generatorVersion": SDK}
EVIDENCE = f'fern_cli_version = "{OLD}"\nfern_python_sdk_version = "{OLD}"\ndigest = "{{}}"\n\n[[covers]]\nkey = "k"\n'


def tree_digest(tree: Path) -> str:
    """Contract A's canonical stream, computed independently of the tool."""
    digest = hashlib.sha256()
    for path in sorted((p for p in tree.rglob("*") if p.is_file()), key=lambda p: p.relative_to(tree).as_posix()):
        data = path.read_bytes()
        digest.update(f"{path.relative_to(tree).as_posix()}\0{len(data)}\0".encode() + data)
    return digest.hexdigest()


@unittest.skipIf(os.name == "nt", "the stand-in tools are POSIX executables")
class FernReferencesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="fern-references-test-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        self.write("assets/scaffolding/metadata.json", json.dumps(METADATA))
        bin_dir = self.root / "stub-bin"
        self.write("stub-bin/fern", STUB_FERN, executable=True)
        self.write("target/release/crozier", STUB_CROZIER, executable=True)
        self.log = self.root / "fern-calls.jsonl"
        self.env = {
            **os.environ,
            "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
            "FERN_STUB_LOG": str(self.log),
            "CROZIER_FERN_REFERENCES_ROOT": str(self.root),
            # The certified-tree store this run publishes into, never the host's.
            "XDG_CACHE_HOME": str(self.root / "cache"),
        }
        # The tool loads golden_overlay.py and certified_tree.py from beside itself.
        self.tool = self.root / "tools/fern-goldens/fern-references.py"
        self.tool.parent.mkdir(parents=True)
        shutil.copy2(TOOL, self.tool)
        shutil.copy2(REPO / "tools/fern-goldens/golden_overlay.py", self.tool.parent / "golden_overlay.py")
        shutil.copy2(REPO / "tools/fern-goldens/certified_tree.py", self.tool.parent / "certified_tree.py")

    def write(self, path: str, text: str, *, executable: bool = False) -> Path:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        if executable:
            target.chmod(0o755)
        return target

    def run_tool(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.tool), *args],
            env=self.env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

    def install_delegates(self, *scripts: str) -> None:
        """Stand a recording stub in at each named script's path."""
        self.env["DELEGATE_LOG"] = str(self.root / "delegate-calls.jsonl")
        for script in scripts:
            self.write(script, STUB_DELEGATE, executable=True)

    def delegate_calls(self) -> list[dict]:
        """What each stand-in script was run with, in order."""
        log = self.root / "delegate-calls.jsonl"
        if not log.is_file():
            return []
        return [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines()]

    def load_tool(self):
        spec = importlib.util.spec_from_file_location("fern_references_under_test", self.tool)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module

    def calls(self) -> list[dict]:
        if not self.log.is_file():
            return []
        return [json.loads(line) for line in self.log.read_text(encoding="utf-8").splitlines()]

    def handwritten(self, name: str, document: str = "openapi: 3.0.3\n", evidence: str = "") -> Path:
        fixture = self.root / "docs/openapi-surface/handwritten" / name
        self.write(f"docs/openapi-surface/handwritten/{name}/openapi.yml", document)
        self.write(f"docs/openapi-surface/handwritten/{name}/evidence.toml", evidence or EVIDENCE.format("0" * 64))
        self.write(f"docs/openapi-surface/handwritten/{name}/fern-expected/src/fern/stale.py", "STALE = 1\n")
        return fixture

    def test_a_hand_written_fixture_is_regenerated_at_the_certified_pair_with_its_evidence(self) -> None:
        top_level = EVIDENCE.format("0" * 64).replace("\n[[covers]]", 'audiences = ["public"]\n\n[[covers]]')
        fixture = self.handwritten("alpha", evidence=top_level)
        self.handwritten("beta")
        self.assertEqual(self.run_tool("list", "handwritten").stdout, "alpha\nbeta\n")

        result = self.run_tool("generate", "handwritten", "alpha")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"handwritten: 1 regenerated, 0 failed at Fern CLI {CLI}", result.stdout)
        tree = fixture / "fern-expected"
        self.assertFalse((tree / "src/fern/stale.py").exists())
        self.assertEqual((tree / "src/fern/client.py").read_text(encoding="utf-8"), "CLIENT = 1\n")
        self.assertTrue((tree / "src/fern/core/enum.py").is_file())
        self.assertTrue((tree / "src/fern/audience_public.py").is_file())
        evidence = (fixture / "evidence.toml").read_text(encoding="utf-8")
        self.assertIn(f'fern_cli_version = "{CLI}"\nfern_python_sdk_version = "{SDK}"\n', evidence)
        self.assertIn(f'digest = "{tree_digest(tree)}"', evidence)
        self.assertIn('[[covers]]\nkey = "k"\n', evidence)
        (call,) = self.calls()
        self.assertEqual(call["config"], {"organization": "fern", "version": CLI})
        self.assertIn(f"version: {SDK}", call["generators"])
        # Only the named item ran: beta keeps its stale tree.
        self.assertTrue((self.root / "docs/openapi-surface/handwritten/beta/fern-expected/src/fern/stale.py").exists())

    def test_a_hand_written_fixture_keeps_the_generator_settings_its_tree_records(self) -> None:
        self.handwritten("delta")
        self.write(
            "docs/openapi-surface/handwritten/delta/fern-expected/.fern/metadata.json",
            json.dumps(
                {
                    "generatorConfig": {
                        "client_class_name": "FernApi",
                        "pydantic_config": {"enum_type": "python_enums", "extra_fields": "allow"},
                    }
                }
            ),
        )
        result = self.run_tool("generate", "handwritten", "delta")
        self.assertEqual(result.returncode, 0, result.stderr)
        (call,) = self.calls()
        self.assertIn("client_class_name: FernApi", call["generators"])
        self.assertIn("enum_type: python_enums\n            extra_fields: allow", call["generators"])
        # A client class name and extra fields shape the tree but not the key.
        self.assert_store_holds_nothing()

    def test_a_class_or_audience_name_yaml_reads_as_no_string_is_refused_before_fern_runs(self) -> None:
        for label, audiences, metadata, message in (
            ("audience null", '["public", "null"]', None, "audiences must be a list of audience labels"),
            ("audience Off", '["Off"]', None, "audiences must be a list of audience labels"),
            ("class True", "[]", {"client_class_name": "True"}, "is no Python class name YAML reads as a string"),
            ("class yes", "[]", {"client_class_name": "yes"}, "is no Python class name YAML reads as a string"),
        ):
            with self.subTest(label):
                evidence = EVIDENCE.format("0" * 64).replace("\n[[covers]]", f"audiences = {audiences}\n\n[[covers]]")
                fixture = self.handwritten("omicron", evidence=evidence)
                (fixture / "fern-expected/.fern/metadata.json").unlink(missing_ok=True)
                if metadata is not None:
                    self.write(
                        "docs/openapi-surface/handwritten/omicron/fern-expected/.fern/metadata.json",
                        json.dumps({"generatorConfig": metadata}),
                    )
                result = self.run_tool("generate", "handwritten", "omicron")
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn(message, result.stderr)
                self.assertEqual(self.calls(), [])
                self.assertTrue((fixture / "fern-expected/src/fern/stale.py").is_file())

    def test_the_reserved_names_are_the_fixture_script_s(self) -> None:
        """The workspace both scripts write must be the same, so they refuse the same spellings."""
        script = (REPO / "tools/fern-goldens/generate-fern-fixture.sh").read_text(encoding="utf-8")
        body = re.search(r"yaml_keyword\(\) \{.*?\n    ([a-z|]+)\) return 0 ;;", script, re.S)
        assert body is not None, "generate-fern-fixture.sh's yaml_keyword lost its case list"
        spec = importlib.util.spec_from_file_location("fern_references_keywords", TOOL)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        # Its dataclasses resolve their module by name while it loads.
        sys.modules[spec.name] = module
        self.addCleanup(sys.modules.pop, spec.name, None)
        spec.loader.exec_module(module)
        self.assertEqual(set(body.group(1).split("|")), set(module.YAML_KEYWORDS))

    def test_an_explicit_version_overrides_the_certified_pair(self) -> None:
        self.handwritten("alpha")
        result = self.run_tool("generate", "handwritten", "--version", "7.0.0", "--cli-version", "8.0.0")
        self.assertEqual(result.returncode, 0, result.stderr)
        (call,) = self.calls()
        self.assertEqual(call["config"]["version"], "8.0.0")
        self.assertIn("version: 7.0.0", call["generators"])

    def test_a_literals_measurement_is_an_overlay_of_its_base_with_its_complete_tree_digest(self) -> None:
        base = self.handwritten("gamma") / "fern-expected"
        self.write("docs/openapi-surface/handwritten/gamma/fern-expected/src/fern/client.py", "CLIENT = 1\n")
        (base / "src/fern/stale.py").unlink()
        self.write("docs/openapi-surface/handwritten/gamma/fern-expected/src/fern/core/enum.py", "ENUM = 1\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "union-literals/gamma\tdocs/openapi-surface/handwritten/gamma/openapi.yml\tliterals\tpackaged\t"
            "fern-expected:docs/openapi-surface/handwritten/gamma/fern-expected\n",
        )

        result = self.run_tool("generate", "measurements")

        self.assertEqual(result.returncode, 0, result.stderr)
        tree = self.root / "docs/fern-measurements/union-literals/gamma/fern-expected"
        # The complete tree Fern wrote: the base minus what it omits, plus the overlay.
        complete = Path(tempfile.mkdtemp(prefix="complete-"))
        self.addCleanup(shutil.rmtree, complete, ignore_errors=True)
        shutil.copytree(base, complete, dirs_exist_ok=True)
        (complete / "src/fern/core/enum.py").unlink()
        shutil.copytree(tree, complete, dirs_exist_ok=True)
        (complete / ".crozier-overlay.json").unlink()
        self.assertEqual(
            sorted(p.relative_to(tree).as_posix() for p in tree.rglob("*") if p.is_file()),
            [".crozier-overlay.json", ".fern/metadata.json", "src/fern/literal.py"],
        )
        manifest = json.loads((tree / ".crozier-overlay.json").read_text(encoding="utf-8"))
        self.assertEqual(
            manifest,
            {
                "fern_python_sdk_version": SDK,
                "fern_cli_version": CLI,
                "enum_type": "literals",
                "base": "fern-expected",
                "digest": tree_digest(complete),
                "removed": ["src/fern/core/enum.py"],
            },
        )
        (call,) = self.calls()
        self.assertNotIn("enum_type", call["generators"])

    def test_a_pair_adoption_remeasures_each_output_insensitive_comparison_record(self) -> None:
        """Issue #865: each comparison record `output-insensitive.tsv` cites is an
        item, re-measured through `output-insensitive-remeasure.py --only`; one
        whose trees moved fails its item, and the pair is the certified one."""
        surface = "docs/openapi-surface/witness-search-x"
        self.write(
            "docs/openapi-surface/output-insensitive.tsv",
            "key\tcontext\tsearch_record\tfern_comparison\tcrozier_comparison\n"
            f"k\tc\t{surface}/README.md\t{surface}/a/fern-comparison.json\t{surface}/a/crozier-comparison.json\n"
            f"k\td\t{surface}/README.md\t{surface}/b/fern-comparison.json\t{surface}/b/crozier-comparison.json\n",
        )
        for record in ("a/fern", "a/crozier", "b/fern"):
            self.write(f"{surface}/{record}-comparison.json", "{}\n")
        self.install_delegates("tools/surface-census/output-insensitive-remeasure.py")

        listed = self.run_tool("list", "output-insensitive")
        self.assertEqual(
            (0, f"{surface}/a/fern-comparison.json\n{surface}/b/fern-comparison.json\n"),
            (listed.returncode, listed.stdout),
        )
        checked = self.run_tool("check", "output-insensitive")
        self.assertEqual(1, checked.returncode)
        self.assertIn(
            f"output-insensitive {surface}/b/fern-comparison.json: its crozier comparison record", checked.stderr
        )

        done = self.run_tool("generate", "output-insensitive", f"{surface}/a/fern-comparison.json")
        self.assertEqual(0, done.returncode, done.stderr)
        [call] = self.delegate_calls()
        self.assertEqual("output-insensitive-remeasure.py", call["script"])
        self.assertEqual(["--root", str(self.root), "--only", f"{surface}/a/fern-comparison.json"], call["argv"])

        self.env["DELEGATE_EXIT"] = "1"
        moved = self.run_tool("generate", "output-insensitive", f"{surface}/a/fern-comparison.json")
        self.assertEqual(1, moved.returncode)
        self.assertIn("output-insensitive-remeasure.py --root", moved.stderr)
        self.assertIn("exited 1; see .local/fern-references/output-insensitive/", moved.stderr)
        pinned = self.run_tool("generate", "output-insensitive", "--version", "1.2.3")
        self.assertEqual(2, pinned.returncode)
        self.assertIn("output-insensitive cannot take --version", pinned.stderr)

    def test_the_pair_variable_is_the_one_witness_screen_reads(self) -> None:
        """The pair `generate witness-screens` names is read by `witness_screen.py` under one name."""
        spec = importlib.util.spec_from_file_location(
            "witness_screen_pair_name", REPO / "tools/witness-search/witness_screen.py"
        )
        assert spec is not None and spec.loader is not None
        screen = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = screen
        spec.loader.exec_module(screen)
        self.assertEqual(screen.PAIR_ENV, self.load_tool().WITNESS_PAIR_ENV)

    def test_a_pair_adoption_labels_and_rescreens_each_witness_measured_at_a_pair(self) -> None:
        """Issue #865: every filed candidate whose latest screen ran Fern at a pair
        is an item. Its generation labels earlier-pair screens `historical`, then
        re-screens it in its own ledger at the pair it generates, keeping its
        disposition; history, an unmeasured row and a Fern-less record are none."""
        pins = {"fern_cli": OLD, "generator": "fernapi/fern-python-sdk", "generator_version": OLD}
        commit = "c" * 40
        rows = [
            {
                "repository": "acme/shop",
                "commit": commit,
                "path": "openapi.yaml",
                "sha256": "d" * 64,
                "disposition": "witness-found",
                "measured": {"fern": {"pins": pins}},
            },
            {
                "repository": "acme/old",
                "commit": commit,
                "path": "a.yaml",
                "disposition": "not-owed",
                "historical": "measured at an earlier certified pair",
                "measured": {"fern": {"pins": pins}},
            },
            {"repository": "acme/bare", "commit": commit, "path": "b.yaml", "disposition": "rejected"},
            {
                "repository": "acme/unrun",
                "commit": commit,
                "path": "c.yaml",
                "disposition": "rejected",
                "measured": {"fern": {"outcome": "not-run"}},
            },
        ]
        self.write(
            "docs/openapi-surface/witness-search-x/acme-screen/screens.jsonl",
            "".join(json.dumps(row) + "\n" for row in rows),
        )
        stub = STUB_DELEGATE.replace(
            '"cli": os.environ.get("FERN_CLI_VERSION")',
            f'"pair": os.environ.get("{self.load_tool().WITNESS_PAIR_ENV}")',
        )
        self.env["DELEGATE_LOG"] = str(self.root / "delegate-calls.jsonl")
        self.write("tools/witness-search/witness_screen.py", stub, executable=True)
        item = f"witness-search-x/acme-screen/acme/shop/{commit}/openapi.yaml"

        listed = self.run_tool("list", "witness-screens")
        self.assertEqual((0, f"{item}\n"), (listed.returncode, listed.stdout))
        self.assertEqual(0, self.run_tool("check", "witness-screens").returncode)

        done = self.run_tool("generate", "witness-screens", item)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn(f"witness-screens: 1 regenerated, 0 failed at Fern CLI {CLI}", done.stdout)
        evidence = str(self.root / "docs/openapi-surface")
        ledger = f"{evidence}/witness-search-x/acme-screen/screens.jsonl"
        self.assertEqual(
            [
                ["historical", "--evidence-root", evidence],
                [
                    "screen",
                    "--ledger",
                    ledger,
                    "--repository",
                    "acme/shop",
                    "--commit",
                    commit,
                    "--path",
                    "openapi.yaml",
                    "--evidence-root",
                    evidence,
                    "--sha256",
                    "d" * 64,
                    "--disposition",
                    "witness-found",
                ],
            ],
            [call["argv"] for call in self.delegate_calls()],
        )
        self.assertEqual({f"{CLI}/{SDK}"}, {call["pair"] for call in self.delegate_calls()})

        self.env["DELEGATE_EXIT"] = "1"
        refused = self.run_tool("generate", "witness-screens", item)
        self.assertEqual(1, refused.returncode)
        self.assertIn("`witness_screen.py historical` exited 1", refused.stderr)
        unknown = self.run_tool("generate", "witness-screens", f"witness-search-x/acme-screen/acme/old/{commit}/a.yaml")
        self.assertEqual(2, unknown.returncode)
        self.assertIn("no witness-screens item", unknown.stderr)

        # A row naming part of a candidate is refused, never skipped.
        with (self.root / "docs/openapi-surface/witness-search-x/acme-screen/screens.jsonl").open("a") as ledger:
            ledger.write(json.dumps({"repository": "acme/half", "path": "d.yaml"}) + "\n")
        broken = self.run_tool("check", "witness-screens")
        self.assertEqual(1, broken.returncode)
        self.assertIn("screens.jsonl:5 names a candidate without a whole repository, commit and path", broken.stderr)
        ledger = self.root / "docs/openapi-surface/witness-search-x/acme-screen/screens.jsonl"
        ledger.write_text(json.dumps({**rows[0], "sha256": 7}) + "\n", encoding="utf-8")
        typed = self.run_tool("check", "witness-screens")
        self.assertEqual(1, typed.returncode)
        self.assertIn("carries a sha256 or disposition that is no string", typed.stderr)

    def test_every_committed_measurement_tree_is_an_item_and_an_unregistered_one_fails_the_check(self) -> None:
        """Issue #961: a committed Fern tree under docs/fern-measurements/ that no
        `cases.tsv` row regenerates fails `check`, naming it, rather than staying at
        its old pair through a weekly regeneration that skips it; once registered,
        a variant kept as a tree beside its case (`<case>/expected-literals/`) is
        regenerated in place, and the case's own tree and evidence are untouched."""
        case = "docs/fern-measurements/handed-off/client-structure/init-order"
        self.write(f"{case}/openapi.yml", "openapi: 3.0.3\n")
        self.write(f"{case}/README.md", "evidence\n")
        for tree in ("fern-expected", "expected-literals"):
            self.write(f"{case}/{tree}/.fern/metadata.json", json.dumps({**METADATA, "cliVersion": OLD}))
            self.write(f"{case}/{tree}/src/fern/client.py", "OLD = 1\n")
        header = "case\tdocument\tenum_type\tlayout\toverlay\n"
        registered = f"handed-off/client-structure/init-order\t{case}/openapi.yml\tpython-enums\tpackaged\t-\n"
        self.write("docs/fern-measurements/cases.tsv", header + registered)

        checked = self.run_tool("check", "measurements")
        self.assertEqual(checked.returncode, 1, checked.stderr)
        self.assertIn(
            f"measurements {case}/expected-literals: a committed Fern tree no docs/fern-measurements/cases.tsv "
            "row regenerates",
            checked.stderr,
        )
        self.assertNotIn(f"{case}/fern-expected:", checked.stderr)
        self.assertEqual([], self.calls(), "check ran Fern")

        variant = (
            f"handed-off/client-structure/init-order/expected-literals\t{case}/openapi.yml\tliterals\tpackaged\t-\n"
        )
        self.write("docs/fern-measurements/cases.tsv", header + registered + variant)
        checked = self.run_tool("check", "measurements")
        self.assertEqual(checked.returncode, 0, checked.stderr)
        listed = self.run_tool("list", "measurements")
        self.assertIn("handed-off/client-structure/init-order/expected-literals", listed.stdout.split())

        result = self.run_tool("generate", "measurements", "handed-off/client-structure/init-order/expected-literals")
        self.assertEqual(result.returncode, 0, result.stderr)
        literals = self.root / case / "expected-literals"
        self.assertEqual((literals / "src/fern/client.py").read_text(encoding="utf-8"), "CLIENT = 1\n")
        self.assertTrue((literals / "src/fern/literal.py").is_file())
        self.assertEqual(CLI, json.loads((literals / ".fern/metadata.json").read_text(encoding="utf-8"))["cliVersion"])
        self.assertFalse((literals / "fern-expected").exists(), "the variant was written beside itself, not in place")
        self.assertEqual(
            "OLD = 1\n", (self.root / case / "fern-expected/src/fern/client.py").read_text(encoding="utf-8")
        )
        self.assertEqual("evidence\n", (self.root / case / "README.md").read_text(encoding="utf-8"))

    def test_a_triage_cause_directory_is_a_measurement_case(self) -> None:
        """Issue #823: the recorded triage layout's upper-case cause directories, and
        their literals trees, regenerate like any other case."""
        cause = "docs/fern-measurements/handed-off/union-modelling/R9"
        self.write(f"{cause}/openapi.yml", "openapi: 3.0.3\n")
        header = "case\tdocument\tenum_type\tlayout\toverlay\n"
        self.write(
            "docs/fern-measurements/cases.tsv",
            header
            + f"handed-off/union-modelling/R9\t{cause}/openapi.yml\tpython-enums\tpackaged\t-\n"
            + f"handed-off/union-modelling/R9/literals\t{cause}/openapi.yml\tliterals\tpackaged\t-\n",
        )

        listed = self.run_tool("list", "measurements")
        self.assertEqual(listed.returncode, 0, listed.stderr)
        self.assertIn("handed-off/union-modelling/R9/literals", listed.stdout.split())

        result = self.run_tool("generate", "measurements", "handed-off/union-modelling/R9/literals")

        self.assertEqual(result.returncode, 0, result.stderr)
        tree = self.root / cause / "literals/fern-expected"
        self.assertEqual((tree / "src/fern/client.py").read_text(encoding="utf-8"), "CLIENT = 1\n")
        self.assertTrue((tree / "src/fern/literal.py").is_file())
        self.assertFalse((self.root / cause / "fern-expected").exists(), "only the named case regenerates")

        # Traversal, an absolute path and a duplicate (even one differing only in
        # case) stay refused, before Fern runs.
        before = len(self.calls())
        for name in ("../R9", "/R9", "handed-off/../R9", "handed-off/union-modelling/r9"):
            with self.subTest(name=name):
                self.write(
                    "docs/fern-measurements/cases.tsv",
                    header
                    + f"handed-off/union-modelling/R9\t{cause}/openapi.yml\tpython-enums\tpackaged\t-\n"
                    + f"{name}\t{cause}/openapi.yml\tliterals\tpackaged\t-\n",
                )
                refused = self.run_tool("generate", "measurements")
                self.assertEqual(refused.returncode, 1, refused.stdout)
                self.assertIn(f"row {name!r}: a case is a unique relative path", refused.stderr)
        self.assertEqual(len(self.calls()), before)

    def assert_store_holds_nothing(self) -> None:
        """The host's certified-tree store (this test's scratch cache) kept no entry."""
        store = self.root / "cache/crozier/certified-trees"
        self.assertEqual([], sorted(path.relative_to(store).as_posix() for path in store.glob("*/*/*")))

    def store_entry(self, document: str, mode: str) -> Path:
        digest = hashlib.sha256((self.root / document).read_bytes()).hexdigest()
        return self.root / "cache/crozier/certified-trees" / f"fern-{CLI}_python-{SDK}" / digest / mode

    def find_entry(self, document: str, mode: str) -> subprocess.CompletedProcess[str]:
        """The store's own reader, `certified_tree.py find`, as another measurement asks it."""
        return subprocess.run(
            [
                sys.executable,
                str(self.tool.with_name("certified_tree.py")),
                "find",
                str(self.root / document),
                *("--enum-type", mode, "--cli", CLI, "--generator", SDK),
            ],
            env=self.env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

    def test_a_certified_generation_keeps_its_untouched_tree_reusable(self) -> None:
        """Issue #813: the tree Fern wrote is published to the host's certified-tree
        store, keyed by document digest, pair and enum mode, before the scratch
        workspace is removed — and an entry already there is kept and stays readable."""
        document = "docs/fern-measurements/kept/omega/openapi.yml"
        self.write(document, "openapi: 3.0.3\ninfo: {title: omega}\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            f"kept/omega\t{document}\tpython-enums\tpackaged\t-\n"
            f"kept/omega-literals\t{document}\tliterals\tpackaged\t-\n",
        )
        self.assertNotEqual(self.find_entry(document, "python-enums").returncode, 0)

        result = self.run_tool("generate", "measurements")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("certified-tree store", result.stderr)
        for mode, directory, kept in (
            ("python-enums", "python_enums", "core/enum.py"),
            ("literals", "literals", "literal.py"),
        ):
            with self.subTest(mode=mode):
                entry = self.store_entry(document, directory)
                found = self.find_entry(document, mode)
                self.assertEqual(found.returncode, 0, found.stderr)
                self.assertEqual(found.stdout.strip(), str(entry))
                # Untouched: the comment the committed tree has stripped is still there.
                self.assertEqual(
                    (entry / "tree/src/fern/client.py").read_text(encoding="utf-8"),
                    "# a comment Fern writes\nCLIENT = 1\n",
                )
                self.assertTrue((entry / "tree/src/fern" / kept).is_file())
                self.assertEqual((entry / "document.sha256").read_text(encoding="utf-8"), entry.parent.name + "\n")
                self.assertEqual((entry / "exit-code").read_text(encoding="utf-8"), "0\n")
                self.assertIn("Wrote files to <workspace>", (entry / "fern.log").read_text(encoding="utf-8"))
        committed = self.root / "docs/fern-measurements/kept/omega/fern-expected/src/fern/client.py"
        self.assertEqual(committed.read_text(encoding="utf-8"), "CLIENT = 1\n")
        # Assembled beside its name and renamed in: no stage is left behind.
        staged = [p.name for p in self.store_entry(document, "python_enums").parent.iterdir() if p.name.startswith(".")]
        self.assertEqual(staged, [])

        # An entry in the store's existing shape (a screen's, carrying screen.json)
        # is read as it is and never replaced by a later generation.
        earlier = self.store_entry(document, "python_enums")
        shutil.rmtree(earlier)
        self.write(str((earlier / "tree/src/fern/client.py").relative_to(self.root)), "EARLIER = 1\n")
        for name, text in (("document.sha256", earlier.parent.name + "\n"), ("exit-code", "0\n"), ("fern.log", "")):
            self.write(str((earlier / name).relative_to(self.root)), text)
        self.write(str((earlier / "screen.json").relative_to(self.root)), '{"check_exit": "0"}\n')
        again = self.run_tool("generate", "measurements", "kept/omega")
        self.assertEqual(again.returncode, 0, again.stderr)
        self.assertEqual((earlier / "tree/src/fern/client.py").read_text(encoding="utf-8"), "EARLIER = 1\n")
        self.assertTrue((earlier / "screen.json").is_file())
        self.assertEqual(self.find_entry(document, "python-enums").stdout.strip(), str(earlier))

    def publish(self, document: str, tree: Path, mode: str = "python-enums") -> subprocess.CompletedProcess[str]:
        """The store's own writer, `certified_tree.py publish`, as a generation calls it."""
        return subprocess.run(
            [
                sys.executable,
                str(self.tool.with_name("certified_tree.py")),
                "publish",
                str(self.root / document),
                str(tree),
                "--enum-type",
                mode,
            ],
            env=self.env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

    def test_a_tree_that_does_not_describe_its_key_is_refused_with_the_fix(self) -> None:
        """Only an untouched python-sdk tree recording exactly the pair and enum mode is kept."""
        document = "docs/fern-measurements/kept/tau/openapi.yml"
        self.write(document, "openapi: 3.0.3\ninfo: {title: tau}\n")
        tree = self.root / "tree"
        self.write("tree/src/fern/client.py", "CLIENT = 1\n")
        whole = {
            "cliVersion": CLI,
            "generatorName": "fernapi/fern-python-sdk",
            "generatorVersion": SDK,
            "generatorConfig": {"pydantic_config": {"enum_type": "python_enums"}},
        }
        for metadata, says in (
            ("not json", "is no Fern metadata record"),
            ("[]", "is no JSON object"),
            (json.dumps({**whole, "generatorName": "fernapi/fern-typescript-sdk"}), "not fernapi/fern-python-sdk"),
            (json.dumps({**whole, "cliVersion": "v9"}), "records no exact cliVersion and generatorVersion"),
            (json.dumps({**whole, "generatorConfig": {"client_class_name": "Acme"}}), "the store keys a tree"),
        ):
            with self.subTest(says=says):
                self.write("tree/.fern/metadata.json", metadata)
                refused = self.publish(document, tree)
                self.assertEqual(refused.returncode, 1, refused.stdout)
                self.assertIn(says, refused.stderr)
                self.assertIn("regenerate with the certified pair", refused.stderr)
                self.assertNotEqual(self.find_entry(document, "python-enums").returncode, 0)
        # A tree holding only its provenance record is no SDK Fern wrote.
        self.write("tree/.fern/metadata.json", json.dumps(whole))
        bare = self.root / "bare"
        self.write("bare/.fern/metadata.json", json.dumps(whole))
        refused = self.publish(document, bare)
        self.assertEqual(refused.returncode, 1, refused.stdout)
        self.assertIn("holds no generated file beside its .fern/ record", refused.stderr)
        # An entry left incomplete (an interrupted copy: no records, or an empty
        # tree) is never read and never silently kept: publication names it and
        # how to clear it.
        entry = self.store_entry(document, "python_enums")
        (entry / "tree").mkdir(parents=True)
        self.assertNotEqual(self.find_entry(document, "python-enums").returncode, 0)
        refused = self.publish(document, tree)
        self.assertEqual(refused.returncode, 1, refused.stdout)
        self.assertIn("is incomplete (its records cannot be read", refused.stderr)
        self.assertIn("remove that directory", refused.stderr)
        for name, text in (("document.sha256", entry.parent.name + "\n"), ("exit-code", "0\n")):
            self.write(str((entry / name).relative_to(self.root)), text)
        refused = self.publish(document, tree)
        self.assertIn("records a successful generation but holds no generated tree/", refused.stderr)
        # A refused generation's record (its status, no SDK) stays a readable entry.
        self.write(str((entry / "exit-code").relative_to(self.root)), "1\n")
        self.assertEqual(self.find_entry(document, "python-enums").stdout.strip(), str(entry))
        # Records that do not describe the entry make it no entry, to find and to publish.
        for name, text, says in (
            ("document.sha256", "0" * 64 + "\n", "its document.sha256 reads"),
            ("exit-code", "killed\n", "its exit-code reads 'killed', no exit status"),
        ):
            with self.subTest(record=name):
                saved = (entry / name).read_text(encoding="utf-8")
                self.write(str((entry / name).relative_to(self.root)), text)
                self.assertNotEqual(self.find_entry(document, "python-enums").returncode, 0)
                refused = self.publish(document, tree)
                self.assertEqual(refused.returncode, 1, refused.stdout)
                self.assertIn(says, refused.stderr)
                self.write(str((entry / name).relative_to(self.root)), saved)
        shutil.rmtree(entry)
        kept = self.publish(document, tree)
        self.assertEqual(kept.returncode, 0, kept.stderr)
        self.assertEqual(self.find_entry(document, "python-enums").stdout.strip(), str(entry))
        # A caller's extra records are plain names, never the entry's own.
        store = self.load_tool().certified_tree_store()
        with self.assertRaisesRegex(ValueError, "must be plain file names"):
            store.publish(self.root / document, tree, store.EnumMode.LITERALS, records={"tree": "x"})

    def test_a_flat_tree_never_answers_for_the_packaged_key(self) -> None:
        """Issue #886: a regeneration that installed its modules at the tree root is
        refused before it can win first-wins publication, and a flat entry already
        cached under the key is neither found nor kept: publication names the
        directory to remove, after which the packaged tree publishes."""
        document = "docs/fern-measurements/kept/psi/openapi.yml"
        self.write(document, "openapi: 3.0.3\ninfo: {title: psi}\n")
        metadata = json.dumps(
            {
                "cliVersion": CLI,
                "generatorName": "fernapi/fern-python-sdk",
                "generatorVersion": SDK,
                "generatorConfig": {"pydantic_config": {"enum_type": "python_enums"}},
            }
        )
        for name in ("client.py", "raw_client.py", "core/enum.py", "README.md", ".fern/metadata.json"):
            self.write(f"flat/{name}", metadata if name.endswith(".json") else "X = 1\n")
        refused = self.publish(document, self.root / "flat")
        self.assertEqual(refused.returncode, 1, refused.stdout)
        self.assertIn("is not the packaged SDK the store's key names", refused.stderr)
        self.assertIn("Python modules at its root (client.py, raw_client.py), the flat layout", refused.stderr)
        self.assertIn("regenerate with the certified pair", refused.stderr)
        self.assertNotEqual(self.find_entry(document, "python-enums").returncode, 0)
        # Neither is a tree with no source package under src/.
        self.write("readme-only/README.md", "# psi\n")
        self.write("readme-only/.fern/metadata.json", metadata)
        refused = self.publish(document, self.root / "readme-only")
        self.assertIn("no source package under src/", refused.stderr)

        # A flat entry cached before this rule: never read, never kept.
        entry = self.store_entry(document, "python_enums")
        shutil.copytree(self.root / "flat", entry / "tree")
        for name, text in (("document.sha256", entry.parent.name + "\n"), ("exit-code", "0\n"), ("fern.log", "")):
            self.write(str((entry / name).relative_to(self.root)), text)
        self.assertNotEqual(self.find_entry(document, "python-enums").returncode, 0)
        self.write("packaged/src/fern/client.py", "CLIENT = 1\n")
        self.write("packaged/.fern/metadata.json", metadata)
        refused = self.publish(document, self.root / "packaged")
        self.assertEqual(refused.returncode, 1, refused.stdout)
        self.assertIn(f"the entry already at {entry} is incomplete", refused.stderr)
        self.assertIn("its tree/ is not the packaged SDK the key names", refused.stderr)
        self.assertIn("remove that directory", refused.stderr)
        shutil.rmtree(entry)
        published = self.publish(document, self.root / "packaged")
        self.assertEqual(published.returncode, 0, published.stderr)
        self.assertEqual(self.find_entry(document, "python-enums").stdout.strip(), str(entry))
        self.assertTrue((entry / "tree/src/fern/client.py").is_file())

    def test_the_store_lives_under_the_home_cache_unless_an_absolute_xdg_cache_home_moves_it(self) -> None:
        """XDG_CACHE_HOME places the store only when absolute, as XDG asks; otherwise ~/.cache."""
        document = "docs/fern-measurements/kept/phi/openapi.yml"
        self.write(document, "openapi: 3.0.3\ninfo: {title: phi}\n")
        self.write("tree/src/fern/client.py", "CLIENT = 1\n")
        self.write(
            "tree/.fern/metadata.json",
            json.dumps(
                {
                    "cliVersion": CLI,
                    "generatorName": "fernapi/fern-python-sdk",
                    "generatorVersion": SDK,
                    "generatorConfig": {"pydantic_config": {"enum_type": "python_enums"}},
                }
            ),
        )
        home = self.root / "home"
        digest = hashlib.sha256((self.root / document).read_bytes()).hexdigest()
        expected = home / ".cache/crozier/certified-trees" / f"fern-{CLI}_python-{SDK}" / digest / "python_enums"
        for xdg in (None, "relative/cache"):
            with self.subTest(xdg=xdg):
                saved = dict(self.env)
                self.env.pop("XDG_CACHE_HOME", None)
                self.env["HOME"] = str(home)
                if xdg is not None:
                    self.env["XDG_CACHE_HOME"] = xdg
                try:
                    published = self.publish(document, self.root / "tree")
                    found = self.find_entry(document, "python-enums")
                finally:
                    self.env = saved
                self.assertEqual(published.returncode, 0, published.stderr)
                self.assertEqual((published.stdout.strip(), found.stdout.strip()), (str(expected), str(expected)))
                self.assertFalse((Path.cwd() / "relative").exists(), "a relative XDG_CACHE_HOME is ignored")

    def test_a_tree_the_store_refuses_leaves_the_golden_generated_and_names_why(self) -> None:
        """A generation whose tree does not describe the store's key is still a golden."""
        document = "docs/fern-measurements/kept/chi/openapi.yml"
        self.write(document, "openapi: 3.0.3\ninfo: {title: chi}\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            f"case\tdocument\tenum_type\tlayout\toverlay\nkept/chi\t{document}\tpython-enums\tpackaged\t-\n",
        )
        self.env["FERN_STAND_IN_GENERATOR"] = "fernapi/fern-typescript-sdk"
        try:
            result = self.run_tool("generate", "measurements")
        finally:
            self.env.pop("FERN_STAND_IN_GENERATOR")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("fern-references: not kept in the certified-tree store:", result.stderr)
        self.assertIn("records generator 'fernapi/fern-typescript-sdk', not fernapi/fern-python-sdk", result.stderr)
        self.assertTrue((self.root / "docs/fern-measurements/kept/chi/fern-expected/src/fern/client.py").is_file())
        self.assert_store_holds_nothing()

    def test_an_unwritable_store_leaves_the_golden_generated_and_names_the_fix(self) -> None:
        """A store write failure costs only the reuse: the reference tree is still written."""
        if os.name == "nt" or os.geteuid() == 0:
            self.skipTest("a read-only directory is enforced only for a non-root POSIX user")
        document = "docs/fern-measurements/kept/upsilon/openapi.yml"
        self.write(document, "openapi: 3.0.3\ninfo: {title: upsilon}\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            f"case\tdocument\tenum_type\tlayout\toverlay\nkept/upsilon\t{document}\tpython-enums\tpackaged\t-\n",
        )
        store = self.root / "cache/crozier/certified-trees"
        store.mkdir(parents=True)
        store.chmod(0o500)
        try:
            result = self.run_tool("generate", "measurements")
        finally:
            store.chmod(0o700)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("could not keep the untouched tree in", result.stderr)
        self.assertIn("free space or fix its permissions", result.stderr)
        self.assertTrue((self.root / "docs/fern-measurements/kept/upsilon/fern-expected/src/fern/client.py").is_file())
        self.assertNotEqual(self.find_entry(document, "python-enums").returncode, 0)
        recovered = self.run_tool("generate", "measurements")
        self.assertEqual(recovered.returncode, 0, recovered.stderr)
        self.assertEqual(self.find_entry(document, "python-enums").returncode, 0)

    def test_a_generation_the_store_key_cannot_describe_is_not_kept(self) -> None:
        """Audiences shape Fern's output but are no part of the store's key, so a
        generation under them publishes nothing; the regeneration itself is unchanged."""
        self.handwritten(
            "sigma", evidence=EVIDENCE.format("0" * 64).replace("\n[[covers]]", "audiences = ['public']\n\n[[covers]]")
        )

        result = self.run_tool("generate", "handwritten", "sigma")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(
            (self.root / "docs/openapi-surface/handwritten/sigma/fern-expected/src/fern/audience_public.py").is_file()
        )
        self.assertFalse((self.root / "cache/crozier/certified-trees").exists())

    def test_a_flat_measurement_runs_tokenless_into_the_module_tree(self) -> None:
        self.write("docs/fern-measurements/clients/delta/openapi.yml", "openapi: 3.0.3\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "clients/delta-flat\tdocs/fern-measurements/clients/delta/openapi.yml\tpython-enums\tflat\t-\n",
        )
        self.write(
            "docs/fern-measurements/clients/delta-flat/evidence.md",
            f"Fern CLI {OLD} with fernapi/fern-python-sdk {OLD}.\n\nCanonical tree SHA-256: `{'0' * 64}`\n",
        )
        result = self.run_tool("generate", "measurements", "clients/delta-flat")
        self.assertEqual(result.returncode, 0, result.stderr)
        tree = self.root / "docs/fern-measurements/clients/delta-flat/fern-expected"
        self.assertEqual(
            (tree.parent / "evidence.md").read_text(encoding="utf-8"),
            f"Fern CLI {CLI} with fernapi/fern-python-sdk {SDK}.\n\nCanonical tree SHA-256: `{tree_digest(tree)}`\n",
        )
        self.assertTrue((tree / "client.py").is_file())
        self.assertFalse((tree / "src").exists())
        (call,) = self.calls()
        self.assertNotIn("--preview", call["argv"])
        # The flat layout is no part of the store's key, so nothing is kept.
        self.assert_store_holds_nothing()

    def test_a_refused_measurement_rewrites_its_refusal_record_at_the_pair(self) -> None:
        self.write("docs/fern-measurements/lowering/epsilon/openapi.yml", "openapi: 3.0.3\nx-stub-refuse: true\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "lowering/epsilon\tdocs/fern-measurements/lowering/epsilon/openapi.yml\tpython-enums\tpackaged\t-\n",
        )
        record = self.write("docs/fern-measurements/lowering/epsilon/fern-refusal.txt", f"fern CLI {OLD}: refused\n")
        result = self.run_tool("generate", "measurements", "lowering/epsilon")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            record.read_text(encoding="utf-8"),
            f"fern_cli_version: {CLI}\nfern_python_sdk_version: {SDK}\n"
            "generate_exit: 1\ndiagnostic: Stub refused the document\noutput_tree: none\n",
        )
        self.assertFalse((record.parent / "fern-expected").exists())

    def test_a_failed_generation_that_wrote_a_partial_tree_is_recorded_as_a_refusal(self) -> None:
        """Fern exiting non-zero after writing some files is a refusal: the record says
        so with no output tree, and no partial tree is installed as a reference."""
        refusal = (
            f"fern_cli_version: {CLI}\nfern_python_sdk_version: {SDK}\n"
            "generate_exit: 1\ndiagnostic: Stub refused the document\noutput_tree: none\n"
        )
        self.write("docs/fern-measurements/lowering/eta/openapi.yml", "openapi: 3.0.3\nx-stub-partial: true\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "lowering/eta\tdocs/fern-measurements/lowering/eta/openapi.yml\tpython-enums\tpackaged\t-\n",
        )
        record = self.write("docs/fern-measurements/lowering/eta/fern-refusal.txt", f"fern CLI {OLD}: refused\n")
        result = self.run_tool("generate", "measurements", "lowering/eta")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(record.read_text(encoding="utf-8"), refusal)
        self.assertFalse((record.parent / "fern-expected").exists())

        # A probe whose committed reference is a tree: the partial run replaces it with the record.
        self.write("docs/openapi-surface/probes/half.yml", "openapi: 3.0.3\nx-stub-partial: true\n")
        self.write("docs/openapi-surface/probe-expected/half/src/fern/client.py", "CLIENT = 1\n")
        self.manifest(f"half\ttree\tgenerates\tdocs/openapi-surface/probe-expected/half\t—\t{'a' * 64}")
        result = self.run_tool("generate", "probes", "half")
        self.assertEqual(result.returncode, 1)
        self.assertIn("changed form (refusal now)", result.stderr)
        expected = self.root / "docs/openapi-surface/probe-expected"
        self.assertFalse((expected / "half").exists())
        written = (expected / "half.fern-refusal.txt").read_text(encoding="utf-8")
        self.assertEqual(written, refusal)
        [row] = (expected / "MANIFEST.tsv").read_text(encoding="utf-8").splitlines()[1:]
        self.assertEqual(
            ["docs/openapi-surface/probe-expected/half.fern-refusal.txt", hashlib.sha256(written.encode()).hexdigest()],
            [row.split("\t")[3], row.split("\t")[5]],
        )

    def test_a_refused_measurement_fern_now_generates_installs_its_tree_and_fails(self) -> None:
        self.write("docs/fern-measurements/lowering/zeta/openapi.yml", "openapi: 3.0.3\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "lowering/zeta\tdocs/fern-measurements/lowering/zeta/openapi.yml\tpython-enums\tpackaged\t-\n",
        )
        record = self.write("docs/fern-measurements/lowering/zeta/fern-refusal.txt", f"fern CLI {OLD}: refused\n")
        result = self.run_tool("generate", "measurements", "lowering/zeta")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Fern now generates lowering/zeta", result.stderr)
        self.assertFalse(record.exists())
        self.assertTrue((record.parent / "fern-expected" / "src" / "fern" / "client.py").is_file())

    def test_a_refusal_log_beside_its_document_is_rewritten_at_the_pair(self) -> None:
        self.write("docs/fern-measurements/bodies/overlap/station.openapi.yml", "openapi: 3.0.3\nx-stub-refuse: true\n")
        log = self.write("docs/fern-measurements/bodies/overlap/station.fern.log", f"Fern CLI {OLD}\n")
        self.write("docs/fern-measurements/cases.tsv", "case\tdocument\tenum_type\tlayout\toverlay\n")
        self.assertIn("bodies/overlap/station\n", self.run_tool("list", "measurements").stdout)
        result = self.run_tool("generate", "measurements", "bodies/overlap/station")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = log.read_text(encoding="utf-8")
        self.assertTrue(text.startswith(f"Fern CLI {CLI}, python-sdk {SDK}\ncheck exit: 1\n"), text)
        self.assertIn("generate exit: 1", text)
        self.assertIn("Stub refused the document", text)

    def test_a_refusal_log_fern_now_generates_from_fails_naming_it(self) -> None:
        self.write("docs/fern-measurements/bodies/overlap/station.openapi.yml", "openapi: 3.0.3\n")
        log = self.write("docs/fern-measurements/bodies/overlap/station.fern.log", f"Fern CLI {OLD}\n")
        self.write("docs/fern-measurements/cases.tsv", "case\tdocument\tenum_type\tlayout\toverlay\n")
        result = self.run_tool("generate", "measurements", "bodies/overlap/station")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Fern now generates bodies/overlap/station", result.stderr)
        self.assertIn("generate exit: 0", log.read_text(encoding="utf-8"))

    def test_a_pinned_run_rewrites_its_log_raw_client_and_record(self) -> None:
        probe = self.write("docs/fern-measurements/repairs/probe.yaml", "openapi: 3.0.3\nx-stub-raw-client: true\n")
        record = self.write(
            "docs/fern-measurements/repairs/measurement.json",
            json.dumps({"probe": "probe.yaml", "fern_cli": OLD, "generator": OLD, "generate_diagnostic": "old"}),
        )
        self.write("docs/fern-measurements/cases.tsv", "case\tdocument\tenum_type\tlayout\toverlay\n")
        self.assertIn("repairs\n", self.run_tool("list", "measurements").stdout)
        result = self.run_tool("generate", "measurements", "repairs")
        self.assertEqual(result.returncode, 0, result.stderr)
        case = record.parent
        self.assertEqual(
            (case / "fern-raw_client.py.txt").read_text(encoding="utf-8"), "# a comment Fern writes\nRAW = 1\n"
        )
        measured = json.loads(record.read_text(encoding="utf-8"))
        self.assertEqual((measured["fern_cli"], measured["generator"]), (CLI, SDK))
        self.assertEqual((measured["check_exit"], measured["generate_exit"]), ("0", "0"))
        self.assertEqual(measured["sha256"], hashlib.sha256(probe.read_bytes()).hexdigest())
        self.assertNotIn("generate_diagnostic", measured)
        self.assertEqual(measured["check_diagnostic"], "All checks passed")
        self.assertEqual(measured["check_log_sha256"], hashlib.sha256(b"All checks passed\n").hexdigest())
        generated = b"[api]: python-sdk Wrote files to <workspace>/preview/fern-python-sdk\n"
        self.assertEqual(measured["generate_log_sha256"], hashlib.sha256(generated).hexdigest())
        self.assertEqual(measured["generate_python_files"], 3, "client.py, raw_client.py and core/enum.py")
        self.assertTrue((case / "fern.log").read_text(encoding="utf-8").startswith(f"Fern CLI {CLI}, python-sdk {SDK}"))

    def test_a_corpus_row_routes_through_fern_goldens_and_a_vendored_fixture_through_its_script(self) -> None:
        self.install_delegates("tools/fern-goldens/fern-goldens", "tools/fern-goldens/generate-fern-fixture.sh")
        self.write("tests/fixtures/CORPUS.md", "| # | name |\n|---|---|\n| 1 | `alpha` |\n")
        self.write("tests/fixtures/alpha/expected/src/x.py", "X = 1\n")
        self.write("tests/fixtures/beta/openapi.yml", "openapi: 3.0.3\n")
        self.write("tests/fixtures/beta/expected/src/x.py", "X = 1\n")
        self.write("tests/fixtures/gamma/openapi.yml", "openapi: 3.0.3\n")
        self.write("tests/fixtures/gamma/expected-flat/__init__.py", "")
        self.write("tests/fixtures/flat-goldens.txt", "alpha\ngamma\n")

        result = self.run_tool("generate", "corpus")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            sorted((call["script"], tuple(call["argv"]), call["cli"]) for call in self.delegate_calls()),
            [
                ("fern-goldens", ("generate", "--version", SDK, "--fixture", "alpha"), CLI),
                ("generate-fern-fixture.sh", ("--layout", "flat", "gamma", SDK), CLI),
                ("generate-fern-fixture.sh", ("beta", SDK), CLI),
            ],
        )
        self.assertEqual(self.calls(), [], "a delegated family runs no Fern of its own")

    def test_a_delegated_corpus_failure_names_its_log_and_the_rest_still_run(self) -> None:
        self.install_delegates("tools/fern-goldens/generate-fern-fixture.sh")
        self.env["DELEGATE_EXIT"] = "3"
        for fixture in ("beta", "delta"):
            self.write(f"tests/fixtures/{fixture}/openapi.yml", "openapi: 3.0.3\n")
            self.write(f"tests/fixtures/{fixture}/expected/src/x.py", "X = 1\n")
        self.write("tests/fixtures/CORPUS.md", "")
        self.write("tests/fixtures/flat-goldens.txt", "")

        result = self.run_tool("generate", "corpus")

        self.assertEqual(result.returncode, 1)
        self.assertIn("corpus: 0 regenerated, 2 failed", result.stdout)
        self.assertIn("`generate-fern-fixture.sh beta", result.stderr)
        self.assertIn("exited 3; see .local/fern-references/corpus/beta.log", result.stderr)
        self.assertEqual(len(self.delegate_calls()), 2)
        log = self.root / ".local/fern-references/corpus/beta.log"
        self.assertEqual(log.read_text(encoding="utf-8"), "delegate ran\n")

    def test_each_overlay_kind_runs_the_overlay_script_with_its_setting_and_the_cli(self) -> None:
        self.install_delegates("tools/fern-goldens/fern-overlay-goldens.sh")
        self.write("tests/fixtures/alpha/openapi.yml", "openapi: 3.0.3\n")
        self.write("tests/fixtures/alpha/expected/src/x.py", "X = 1\n")
        self.write("tests/fixtures/alpha/expected-literals/.crozier-overlay.json", "{}\n")
        self.write(
            "tests/fixtures/alpha/expected-default-max-retries/.crozier-overlay.json",
            json.dumps({"default_max_retries": 5}),
        )

        result = self.run_tool("generate", "overlays", "--cli-version", "8.0.0")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            sorted((tuple(call["argv"]), call["cli"]) for call in self.delegate_calls()),
            [
                (("--jobs", "1", "--default-max-retries", "5", "alpha"), "8.0.0"),
                (("--jobs", "1", "--enum-type", "literals", "alpha"), "8.0.0"),
            ],
        )

    def test_an_overlay_with_a_malformed_retry_count_is_refused_before_it_runs(self) -> None:
        self.install_delegates("tools/fern-goldens/fern-overlay-goldens.sh")
        for retries in ("-1", '"5"', "true"):
            with self.subTest(retries=retries):
                self.write(
                    "tests/fixtures/alpha/expected-default-max-retries/.crozier-overlay.json",
                    f'{{"default_max_retries": {retries}}}',
                )
                result = self.run_tool("generate", "overlays")
                self.assertEqual(result.returncode, 1)
                self.assertIn("default_max_retries must be a non-negative integer", result.stderr)
        self.assertEqual(self.delegate_calls(), [])

    def test_a_refusal_class_and_a_finding_run_fern_refusals_one_generation_at_a_time(self) -> None:
        self.install_delegates("tools/fern-refusals/fern-refusals.py")
        self.write("docs/fern-refusals/classes.tsv", "class\tstatus\nzeta\trefuse\n")
        self.write("docs/fern-refusals/zeta/probe.yml", "openapi: 3.0.3\n")
        self.write("docs/fern-refusals/findings.tsv", "finding\tkind\tprobe\neta\tgenerates\tdocs/eta.yml\n")
        self.write("docs/eta.yml", "openapi: 3.0.3\n")

        result = self.run_tool("generate", "refusals")

        self.assertEqual(result.returncode, 0, result.stderr)
        changes = self.root / ".local/fern-references/refusals/probe.zeta.changes.jsonl"
        # The tool names the report under its resolved root (macOS's /var is /private/var).
        self.assertEqual(
            sorted(tuple(call["argv"]) for call in self.delegate_calls()),
            [("finding", "--jobs", "1", "eta"), ("probe", "--jobs", "1", "--changes", str(changes.resolve()), "zeta")],
        )
        # A probe that no longer reproduces its recorded refusal is reported, not failed;
        # the report a previous run left is gone before the probe runs.
        reported = '{"class": "zeta", "outcome": "generates"}\n'
        changes.write_text(reported, encoding="utf-8")
        self.env.update(DELEGATE_EXIT="3", DELEGATE_CHANGES=reported)
        changed = self.run_tool("generate", "refusals", "zeta")
        self.assertEqual(changed.returncode, 0, changed.stderr)
        self.assertIn("refusals zeta: Fern no longer reproduces the recorded refusal, which is kept", changed.stderr)
        self.assertEqual(reported, changes.read_text(encoding="utf-8"))
        # A changed exit whose report is lost, or names another class, fails the item.
        for written in ("", '{"class": "other"}\n'):
            with self.subTest(written=written):
                changes.write_text(reported, encoding="utf-8")
                self.env["DELEGATE_CHANGES"] = written
                lost = self.run_tool("generate", "refusals", "zeta")
                self.assertEqual(lost.returncode, 1)
                self.assertIn("exited 3, which reports a changed refusal, but", lost.stderr)
        self.env.pop("DELEGATE_CHANGES")
        self.env["DELEGATE_EXIT"] = "4"
        failed = self.run_tool("generate", "refusals", "zeta")
        self.assertEqual(failed.returncode, 1)
        self.assertIn("exited 4; see .local/fern-references/refusals/probe.zeta.log", failed.stderr)

    def test_a_registry_table_without_its_name_column_is_refused(self) -> None:
        self.write("docs/fern-refusals/classes.tsv", "name\tstatus\nzeta\trefuse\n")
        self.write("docs/fern-refusals/findings.tsv", "finding\nfindings\n")
        result = self.run_tool("list", "refusals")
        self.assertEqual(result.returncode, 1)
        self.assertIn("docs/fern-refusals/classes.tsv has no `class` column", result.stderr)

    def test_an_unrecognised_generator_failure_keeps_its_log_and_the_reference(self) -> None:
        self.write("docs/openapi-surface/probes/odd.yml", "openapi: 3.0.3\nx-stub-silent: true\n")
        kept = self.write("docs/openapi-surface/probe-expected/odd/src/fern/client.py", "KEPT = 1\n")
        self.manifest(f"odd\tabsent-tree\tdiscards\tdocs/openapi-surface/probe-expected/odd\t—\t{'a' * 64}")

        result = self.run_tool("generate", "probes", "odd")

        self.assertEqual(result.returncode, 1)
        self.assertIn("printing no diagnostic this tool recognises", result.stderr)
        log = self.root / ".local/fern-references/probes/odd.generate.log"
        self.assertIn("something went sideways", log.read_text(encoding="utf-8"))
        self.assertEqual(kept.read_text(encoding="utf-8"), "KEPT = 1\n")
        self.assertFalse((self.root / "docs/openapi-surface/probe-expected/odd.fern-refusal.txt").exists())

    def test_an_install_refuses_a_stale_backup_and_restores_the_prior_tree_on_failure(self) -> None:
        tool = self.load_tool()
        destination = self.root / "docs/openapi-surface/handwritten/alpha/fern-expected"
        self.write("docs/openapi-surface/handwritten/alpha/fern-expected/client.py", "PRIOR = 1\n")
        backup = destination.parent / f".{destination.name}.backup.{os.getpid()}"
        backup.mkdir()
        with self.assertRaisesRegex(tool.ReferenceError, "a stale backup blocks the install"):
            tool.install(self.root / "staged", destination)
        backup.rmdir()
        with self.assertRaises(OSError):
            tool.install(self.root / "never-staged", destination)
        self.assertEqual((destination / "client.py").read_text(encoding="utf-8"), "PRIOR = 1\n")
        self.assertFalse(backup.exists())

    def test_a_malformed_certified_pair_is_refused_naming_the_file(self) -> None:
        self.handwritten("alpha")
        for record in ('{"cliVersion": null, "generatorVersion": "5.42.0"}', '["5.163.1"]', '{"cliVersion": 5}'):
            with self.subTest(record=record):
                self.write("assets/scaffolding/metadata.json", record)
                result = self.run_tool("generate", "handwritten")
                self.assertEqual(result.returncode, 1)
                self.assertIn(
                    "must be an object whose cliVersion and generatorVersion are exact versions", result.stderr
                )
        self.assertEqual(self.calls(), [])

    def test_a_tree_recording_malformed_generator_settings_is_not_regenerated(self) -> None:
        self.handwritten("delta")
        metadata = "docs/openapi-surface/handwritten/delta/fern-expected/.fern/metadata.json"
        for config, reason in (
            ({"pydantic_config": "allow"}, "must be objects"),
            ({"client_class_name": "9Lives"}, "is no Python class name"),
            ({"client_class_name": "class"}, "is no Python class name"),
            ({"pydantic_config": {"extra_fields": "sometimes"}}, "is none of allow, ignore, forbid"),
        ):
            with self.subTest(config=config):
                self.write(metadata, json.dumps({"generatorConfig": config}))
                result = self.run_tool("generate", "handwritten", "delta")
                self.assertEqual(result.returncode, 1)
                self.assertIn(reason, result.stderr)
        self.assertEqual(self.calls(), [])

    def test_a_pinned_run_whose_probe_leaves_its_case_is_refused(self) -> None:
        self.write("docs/fern-measurements/cases.tsv", "case\tdocument\tenum_type\tlayout\toverlay\n")
        self.write("docs/fern-measurements/outside.yaml", "openapi: 3.0.3\n")
        for probe in ("../outside.yaml", "missing.yaml", None):
            with self.subTest(probe=probe):
                self.write("docs/fern-measurements/repairs/measurement.json", json.dumps({"probe": probe}))
                result = self.run_tool("generate", "measurements", "repairs")
                self.assertEqual(result.returncode, 1)
                self.assertIn(
                    "must be an object whose `probe` names a file in docs/fern-measurements/repairs", result.stderr
                )
        self.assertEqual(self.calls(), [])

    def test_a_measurement_case_or_departure_naming_an_unknown_mode_is_refused(self) -> None:
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\nbodies/x\tdocs/x.yml\tpython_enums\tpackaged\t-\n",
        )
        listed = self.run_tool("list", "measurements")
        self.assertEqual(listed.returncode, 1)
        self.assertIn("enum_type is one of python-enums, literals", listed.stderr)
        self.write("docs/departures/evidence/casing/openapi.yml", "openapi: 3.0.3\n")
        for settings in ({"layout": "sideways"}, {"organization": "Acme Corp"}, ["literals"]):
            with self.subTest(settings=settings):
                self.write("docs/departures/evidence/casing/fern-reference.json", json.dumps(settings))
                result = self.run_tool("generate", "departure-evidence", "casing")
                self.assertEqual(result.returncode, 1)
                self.assertIn("docs/departures/evidence/casing/fern-reference.json", result.stderr)
        self.assertEqual(self.calls(), [])

    def test_a_version_override_a_family_cannot_honour_is_refused(self) -> None:
        self.install_delegates("tools/fern-goldens/fern-overlay-goldens.sh", "tools/fern-refusals/fern-refusals.py")
        self.write("tests/fixtures/alpha/expected-literals/.crozier-overlay.json", "{}\n")
        self.write("docs/fern-refusals/classes.tsv", "class\tstatus\nzeta\trefuse\n")
        self.write("docs/fern-refusals/findings.tsv", "finding\tkind\n")
        for family, flag in (("overlays", "--version"), ("refusals", "--version"), ("refusals", "--cli-version")):
            with self.subTest(family=family, flag=flag):
                result = self.run_tool("generate", family, flag, "7.0.0")
                self.assertEqual(result.returncode, 2)
                self.assertIn(f"{family} cannot take {flag}", result.stderr)
        self.assertEqual(self.delegate_calls(), [])

    def test_an_aliased_row_a_known_failure_and_a_flat_golden_over_another_spec_route_by_row(self) -> None:
        self.install_delegates("tools/fern-goldens/fern-goldens", "tools/fern-goldens/generate-fern-fixture.sh")
        self.write(
            "tests/fixtures/CORPUS.md",
            "| # | name |\n|---|---|\n| 1 | `museum.local` | | \n| 2 | `broken` |\n| 3 | `delta` |\n",
        )
        self.write("tests/fixtures/corpus-aliases.tsv", "# row\tfixture\nmuseum.local\tmuseum\n")
        self.write("tests/fixtures/museum/expected/src/x.py", "X = 1\n")
        self.write("tests/fixtures/broken/known-fern-failure.json", "{}\n")
        self.write("tests/fixtures/delta/expected/src/x.py", "X = 1\n")
        self.write("tests/fixtures/delta/openapi.yml", "openapi: 3.0.3\n")
        self.write("tests/fixtures/delta-flat-spec/expected-flat/__init__.py", "")
        self.write("tests/fixtures/flat-goldens.txt", "delta-flat-spec|delta\n")

        result = self.run_tool("generate", "corpus", "museum", "broken", "delta-flat-spec")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            sorted((call["script"], tuple(call["argv"])) for call in self.delegate_calls()),
            [
                ("fern-goldens", ("generate", "--version", SDK, "--fixture", "broken")),
                ("fern-goldens", ("generate", "--version", SDK, "--fixture", "museum.local")),
                ("generate-fern-fixture.sh", ("--layout", "flat", "delta-flat-spec", SDK)),
            ],
        )

    def test_a_failed_strip_leaves_the_committed_reference_and_no_staging(self) -> None:
        fixture = self.handwritten("alpha")
        self.write(
            "target/release/crozier", "#!/usr/bin/env python3\nimport sys\nsys.exit('cannot strip')\n", executable=True
        )

        result = self.run_tool("generate", "handwritten", "alpha")

        self.assertEqual(result.returncode, 1)
        self.assertIn("crozier internal-strip failed on client.py: cannot strip", result.stderr)
        self.assertEqual((fixture / "fern-expected/src/fern/stale.py").read_text(encoding="utf-8"), "STALE = 1\n")
        self.assertEqual([p.name for p in fixture.iterdir() if p.name.startswith(".")], [])

    def test_a_refusal_fern_now_generates_from_is_written_and_reported_for_a_decision(self) -> None:
        self.write("docs/openapi-surface/probes/thawed.yml", "openapi: 3.0.3\n")
        record = self.write("docs/openapi-surface/probe-expected/thawed.fern-refusal.txt", "old\n")
        self.manifest(
            f"thawed\trefusal\trefuses\tdocs/openapi-surface/probe-expected/thawed.fern-refusal.txt\t—\t{'a' * 64}"
        )

        result = self.run_tool("generate", "probes", "thawed")

        self.assertEqual(result.returncode, 1)
        self.assertIn("changed form (tree now)", result.stderr)
        self.assertFalse(record.exists())
        tree = self.root / "docs/openapi-surface/probe-expected/thawed"
        self.assertTrue((tree / "src/fern/client.py").is_file())
        row = (
            (self.root / "docs/openapi-surface/probe-expected/MANIFEST.tsv").read_text(encoding="utf-8").splitlines()[1]
        )
        self.assertEqual(row.split("\t")[3:], ["docs/openapi-surface/probe-expected/thawed", "—", tree_digest(tree)])

    def test_a_control_fern_now_refuses_flags_the_row_it_controls(self) -> None:
        self.write("docs/openapi-surface/probes/shape.yml", "openapi: 3.0.3\n")
        self.write("docs/openapi-surface/probes/plain.yml", "openapi: 3.0.3\nx-stub-refuse: true\n")
        self.write("docs/openapi-surface/probe-expected/plain/src/fern/client.py", "CLIENT = 1\n")
        self.manifest(
            f"shape\tdifferential\tignores\tdocs/openapi-surface/probe-expected/shape\tplain\t{'a' * 64}",
            f"plain\tabsent-tree\tmeasured\tdocs/openapi-surface/probe-expected/plain\t—\t{'b' * 64}",
        )

        result = self.run_tool("generate", "probes", "plain")

        self.assertEqual(result.returncode, 1)
        self.assertIn("row(s) plain, shape need their form and verdict decided", result.stderr)

    def test_malformed_family_records_are_refused_before_fern_runs(self) -> None:
        self.write("docs/x.yml", "openapi: 3.0.3\n")
        header = "case\tdocument\tenum_type\tlayout\toverlay\n"
        for rows, reason in (
            ("a/b\tdocs/x.yml\tliterals\tpackaged\tfern-expected\n", "its overlay 'fern-expected'"),
            ("a/b\tdocs/x.yml\tliterals\tpackaged\texpected:../outside\n", "its overlay 'expected:../outside'"),
            ("a/b\t../outside.yml\tliterals\tpackaged\t-\n", "is no path of this repository"),
            ("a/b\tdocs/x.yml\tliterals\tpackaged\t-\na/b\tdocs/x.yml\tliterals\tflat\t-\n", "unique"),
        ):
            with self.subTest(rows=rows):
                self.write("docs/fern-measurements/cases.tsv", header + rows)
                result = self.run_tool("list", "measurements")
                self.assertEqual(result.returncode, 1)
                self.assertIn(reason, result.stderr)
        self.write("docs/fern-measurements/cases.tsv", header)
        self.write("docs/fern-measurements/parameter-literals/certified-trees.json", '["alpha"]')
        self.assertIn("must map hand-written fixture names", self.run_tool("list", "measurements").stderr)
        self.write("docs/fern-refusals/classes.tsv", "class\tstatus\nzeta\n")
        self.write("docs/fern-refusals/findings.tsv", "finding\n")
        self.assertIn("classes.tsv:2 has 1 cells for 2 columns", self.run_tool("list", "refusals").stderr)
        self.write("docs/fern-refusals/classes.tsv", "class\tstatus\n../../escape\trefuse\n")
        self.assertIn("is no lower-case name", self.run_tool("list", "refusals").stderr)
        self.handwritten(
            "alpha", evidence=EVIDENCE.format("0" * 64).replace("\n[[covers]]", "audiences = 'public'\n\n[[covers]]")
        )
        self.assertIn("audiences must be a list of audience labels", self.run_tool("generate", "handwritten").stderr)
        self.assertEqual(self.calls(), [])

    def test_a_missing_fern_or_release_crozier_names_its_fix_and_keeps_the_reference(self) -> None:
        fixture = self.handwritten("alpha")
        empty = self.root / "no-fern-bin"
        empty.mkdir()
        missing = subprocess.run(
            [sys.executable, str(self.tool), "generate", "handwritten", "alpha"],
            env={**self.env, "PATH": str(empty)},
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(missing.returncode, 1, missing.stderr)
        self.assertIn("`fern` is not on PATH; run `just setup-fern`", missing.stderr)
        (self.root / "target/release/crozier").unlink()
        unbuilt = self.run_tool("generate", "handwritten", "alpha")
        self.assertEqual(unbuilt.returncode, 1)
        self.assertIn("build crozier first: cargo build --release", unbuilt.stderr)
        self.assertEqual((fixture / "fern-expected/src/fern/stale.py").read_text(encoding="utf-8"), "STALE = 1\n")

    def test_an_error_line_or_a_failed_to_line_is_the_recorded_refusal_diagnostic(self) -> None:
        self.write("docs/openapi-surface/probes/unread.yml", "openapi: 3.0.3\nx-stub-error-line: true\n")
        self.write("docs/openapi-surface/probes/unloaded.yml", "openapi: 3.0.3\nx-stub-failed-to: true\n")
        self.manifest(
            f"unread\trefusal\trefuses\tdocs/openapi-surface/probe-expected/unread.fern-refusal.txt\t—\t{'a' * 64}",
            f"unloaded\trefusal\trefuses\tdocs/openapi-surface/probe-expected/unloaded.fern-refusal.txt\t—\t{'b' * 64}",
        )
        result = self.run_tool("generate", "probes")
        self.assertEqual(result.returncode, 0, result.stderr)
        expected = self.root / "docs/openapi-surface/probe-expected"
        self.assertIn(
            "diagnostic: the definition could not be read\n",
            (expected / "unread.fern-refusal.txt").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "diagnostic: Failed to load the API definition\n",
            (expected / "unloaded.fern-refusal.txt").read_text(encoding="utf-8"),
        )

    def test_an_overlay_over_no_base_records_its_label_without_a_digest(self) -> None:
        self.write("docs/fern-measurements/union-literals/omega/openapi.yml", "openapi: 3.0.3\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "union-literals/omega\tdocs/fern-measurements/union-literals/omega/openapi.yml\tliterals\tpackaged\texpected:-\n",
        )
        result = self.run_tool("generate", "measurements", "union-literals/omega")
        self.assertEqual(result.returncode, 0, result.stderr)
        overlay = json.loads(
            (self.root / "docs/fern-measurements/union-literals/omega/fern-expected/.crozier-overlay.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            (overlay["base"], overlay["enum_type"], overlay["fern_cli_version"]), ("expected", "literals", CLI)
        )
        self.assertNotIn("digest", overlay)

    def test_usage_errors_exit_two_and_a_bad_manifest_name_is_refused(self) -> None:
        self.handwritten("alpha")
        self.assertEqual(self.run_tool("generate", "handwritten", "nosuch").returncode, 2)
        bad_version = self.run_tool("generate", "handwritten", "--version", "latest")
        self.assertEqual(bad_version.returncode, 2)
        self.assertIn("invalid Fern version 'latest'", bad_version.stderr)
        self.manifest(f"../escape\tabsent-tree\tdiscards\tdocs/openapi-surface/probe-expected/x\t—\t{'a' * 64}")
        listed = self.run_tool("list", "probes")
        self.assertEqual(listed.returncode, 1)
        self.assertIn("no plain file stem", listed.stderr)
        self.assertEqual(self.calls(), [])

    def test_a_packaged_run_replaces_an_inherited_token_and_a_flat_run_drops_it(self) -> None:
        self.env["FERN_TOKEN"] = "an-inherited-credential"
        self.handwritten("alpha")
        self.write("docs/fern-measurements/clients/delta/openapi.yml", "openapi: 3.0.3\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "clients/delta-flat\tdocs/fern-measurements/clients/delta/openapi.yml\tpython-enums\tflat\t-\n",
        )
        self.assertEqual(self.run_tool("generate", "handwritten", "alpha").returncode, 0)
        self.assertEqual(self.run_tool("generate", "measurements", "clients/delta-flat").returncode, 0)
        packaged, flat = self.calls()
        self.assertEqual(packaged["token"], "preview-only-no-publish")
        self.assertIsNone(flat["token"])

    def test_the_version_grammar_is_the_one_the_delegated_scripts_apply(self) -> None:
        tool = self.load_tool()
        store = tool.certified_tree_store()
        # The store keys entries by the same enum modes the tool generates.
        self.assertEqual({mode.value for mode in tool.EnumMode}, {mode.value for mode in store.EnumMode})
        samples = (
            "5.41.3",
            "10.0.12",
            "1.2.3-rc.1",
            "1.2.3-beta-2",
            "1.2.3-",
            "1.2.3-.",
            "1.2.3-a..b",
            "1.2",
            "v1.2.3",
        )
        for sample in samples:
            with self.subTest(sample=sample):
                shell = subprocess.run(
                    ["bash", "-c", 'source "$0" && valid_fern_version "$1"', str(REPO / "scripts/lib.sh"), sample],
                    check=False,
                )
                self.assertEqual(shell.returncode == 0, bool(tool.VERSION.fullmatch(sample)))
                # The certified-tree store keys entries by the same grammar.
                self.assertEqual(shell.returncode == 0, bool(store.VERSION.fullmatch(sample)))

    # llmlint: ignore[shell_test_tiers_stay_split] Serving a case's own documents on 127.0.0.1 is the behaviour under test (the tool hands Fern a loopback URL for a remote $ref); the socket never leaves the host, so this stays in the offline tier, which forbids external network rather than loopback.
    def test_a_remote_reference_is_served_from_the_documents_directory(self) -> None:
        self.write(
            "docs/fern-measurements/remote/case/documents/openapi.yml",
            "openapi: 3.0.3\nx-ref: '@REMOTE_URL@/models.yml'\n",
        )
        self.write("docs/fern-measurements/remote/case/documents/models.yml", "Served: true\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "remote/case\tdocs/fern-measurements/remote/case/documents/openapi.yml\tpython-enums\tpackaged\t-\n",
        )
        result = self.run_tool("generate", "measurements")
        self.assertEqual(result.returncode, 0, result.stderr)
        served = self.root / "docs/fern-measurements/remote/case/fern-expected/src/fern/remote.txt"
        self.assertEqual(served.read_text(encoding="utf-8"), "Served: true\n")
        # Fern read the remote ref from a scratch port the store's key does not name.
        self.assert_store_holds_nothing()

    def test_a_parameter_literals_claim_is_re_measured_with_its_metadata_and_digest(self) -> None:
        for name, files in (
            ("holds", {"src/fern/client.py": "CLIENT = 1\n", "src/fern/literal.py": "LITERAL = 1\n"}),
            ("broken", {"src/fern/client.py": "CLIENT = 2\n", "src/fern/literal.py": "LITERAL = 1\n"}),
        ):
            self.handwritten(name)
            shutil.rmtree(self.root / f"docs/openapi-surface/handwritten/{name}/fern-expected")
            for rel, text in {**files, "src/fern/core/enum.py": "ENUM = 1\n", ".fern/metadata.json": "{}"}.items():
                self.write(f"docs/openapi-surface/handwritten/{name}/fern-expected/{rel}", text)
        self.write(
            "docs/fern-measurements/parameter-literals/certified-trees.json",
            json.dumps({"broken": "0" * 64, "holds": "0" * 64}),
        )
        self.write("docs/fern-measurements/cases.tsv", "case\tdocument\tenum_type\tlayout\toverlay\n")
        self.assertIn("parameter-literals/holds\n", self.run_tool("list", "measurements").stdout)

        result = self.run_tool("generate", "measurements", "parameter-literals/holds", "parameter-literals/broken")

        self.assertEqual(result.returncode, 1)
        self.assertIn("broken: the literals tree no longer equals the python-enums tree", result.stderr)
        literals = self.root / "docs/fern-measurements/parameter-literals"
        metadata = json.loads((literals / "metadata.json").read_text(encoding="utf-8"))
        self.assertEqual((metadata["cliVersion"], metadata["generatorVersion"]), (CLI, SDK))
        digests = json.loads((literals / "certified-trees.json").read_text(encoding="utf-8"))
        self.assertNotEqual(digests["holds"], "0" * 64)
        self.assertEqual(digests["broken"], "0" * 64)
        generators = self.calls()[0]["generators"]
        self.assertIn("client_class_name: FernApi", generators)
        self.assertIn("extra_fields: allow", generators)
        self.assertNotIn("enum_type", generators)

    def test_a_parameter_literals_claim_retired_to_parameter_lowering_is_re_measured_from_there(self) -> None:
        """A claim whose hand-written proof moved into a parameter-lowering case
        (as observatory-client-headers did) reads that case's document and
        python-enums tree, and records the literals tree's digest."""
        case = self.root / "docs/fern-measurements/parameter-lowering/retired"
        self.write("docs/fern-measurements/parameter-lowering/retired/openapi.yml", "openapi: 3.0.3\nx-retired: 1\n")
        tree = {"src/fern/client.py": "CLIENT = 1\n", "src/fern/literal.py": "LITERAL = 1\n"}
        for rel, text in {**tree, "src/fern/core/enum.py": "ENUM = 1\n", ".fern/metadata.json": "{}"}.items():
            self.write(f"docs/fern-measurements/parameter-lowering/retired/fern-expected/{rel}", text)
        self.write("docs/fern-measurements/parameter-literals/certified-trees.json", json.dumps({"retired": "0" * 64}))
        # The python-enums tree is a committed tree of its own case, as every
        # parameter-lowering case's is.
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "parameter-lowering/retired\tdocs/fern-measurements/parameter-lowering/retired/openapi.yml\t"
            "python-enums\tpackaged\t-\n",
        )
        self.assertFalse((self.root / "docs/openapi-surface/handwritten/retired").exists())
        clean = self.run_tool("check", "measurements")
        self.assertEqual(0, clean.returncode, clean.stderr)
        self.assertNotIn("parameter-literals/retired", clean.stderr)

        result = self.run_tool("generate", "measurements", "parameter-literals/retired")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(1, len(self.calls()), "one Fern generation, over the parameter-lowering document")
        literals = self.root / "docs/fern-measurements/parameter-literals"
        digests = json.loads((literals / "certified-trees.json").read_text(encoding="utf-8"))
        self.assertNotEqual("0" * 64, digests["retired"])
        metadata = json.loads((literals / "metadata.json").read_text(encoding="utf-8"))
        self.assertEqual((metadata["cliVersion"], metadata["generatorVersion"]), (CLI, SDK))

        # With neither home holding its document, check and generate both name
        # the hand-written path, before Fern starts.
        (case / "openapi.yml").unlink()
        checked = self.run_tool("check", "measurements")
        self.assertEqual(1, checked.returncode)
        self.assertIn("docs/openapi-surface/handwritten/retired/openapi.yml does not exist", checked.stderr)
        self.assertEqual(1, len(self.calls()), "Fern ran only for the regeneration")

    def test_a_parameter_literals_case_with_its_own_metadata_refreshes_that_file_alone(self) -> None:
        self.handwritten("own")
        shutil.rmtree(self.root / "docs/openapi-surface/handwritten/own/fern-expected")
        for rel, text in {
            "src/fern/client.py": "CLIENT = 1\n",
            "src/fern/literal.py": "LITERAL = 1\n",
            "src/fern/core/enum.py": "ENUM = 1\n",
            ".fern/metadata.json": "{}",
        }.items():
            self.write(f"docs/openapi-surface/handwritten/own/fern-expected/{rel}", text)
        literals = self.root / "docs/fern-measurements/parameter-literals"
        self.write("docs/fern-measurements/parameter-literals/certified-trees.json", json.dumps({"own": "0" * 64}))
        shared = self.write("docs/fern-measurements/parameter-literals/metadata.json", '{"shared": true}\n')
        own = self.write("docs/fern-measurements/parameter-literals/own.metadata.json", "{}\n")
        self.write("docs/fern-measurements/cases.tsv", "case\tdocument\tenum_type\tlayout\toverlay\n")

        result = self.run_tool("generate", "measurements", "parameter-literals/own")

        self.assertEqual(result.returncode, 0, result.stderr)
        measured = json.loads(own.read_text(encoding="utf-8"))
        self.assertEqual((measured["cliVersion"], measured["generatorVersion"]), (CLI, SDK))
        self.assertEqual(shared.read_text(encoding="utf-8"), '{"shared": true}\n')
        self.assertNotEqual(
            json.loads((literals / "certified-trees.json").read_text(encoding="utf-8"))["own"], "0" * 64
        )

    def test_a_measurement_case_restates_its_evidence_toml_from_the_tree_it_reduces(self) -> None:
        base = self.handwritten("kappa") / "fern-expected"
        self.write("docs/fern-measurements/union-literals/kappa/openapi.yml", "openapi: 3.0.3\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "union-literals/kappa\tdocs/fern-measurements/union-literals/kappa/openapi.yml\tliterals\tpackaged\t"
            f"fern-expected:{base.relative_to(self.root).as_posix()}\n",
        )
        evidence = self.write("docs/fern-measurements/union-literals/kappa/evidence.toml", EVIDENCE.format("0" * 64))

        result = self.run_tool("generate", "measurements", "union-literals/kappa")

        self.assertEqual(result.returncode, 0, result.stderr)
        tree = evidence.parent / "fern-expected"
        text = evidence.read_text(encoding="utf-8")
        self.assertIn(f'fern_cli_version = "{CLI}"\nfern_python_sdk_version = "{SDK}"\n', text)
        self.assertIn(f'digest = "{tree_digest(tree)}"', text)
        self.assertIn('[[covers]]\nkey = "k"\n', text)

    def test_evidence_missing_a_provenance_line_stops_before_the_tree_is_replaced(self) -> None:
        fixture = self.handwritten(
            "lambda", evidence=f'fern_cli_version = "{OLD}"\ndigest = "x"\n\n[[covers]]\nkey = "k"\n'
        )

        result = self.run_tool("generate", "handwritten", "lambda")

        self.assertEqual(result.returncode, 1)
        self.assertIn("has no single `fern_python_sdk_version` line to restate", result.stderr)
        self.assertEqual(self.calls(), [], "Fern never ran")
        self.assertEqual((fixture / "fern-expected/src/fern/stale.py").read_text(encoding="utf-8"), "STALE = 1\n")
        self.assertIn(f'fern_cli_version = "{OLD}"', (fixture / "evidence.toml").read_text(encoding="utf-8"))

    def test_a_failed_generation_keeps_each_family_s_committed_reference(self) -> None:
        refuse = "openapi: 3.0.3\nx-stub-refuse: true\n"
        fixture = self.handwritten("alpha", document=refuse)
        evidence_before = (fixture / "evidence.toml").read_text(encoding="utf-8")
        self.write("docs/fern-measurements/cases.tsv", "case\tdocument\tenum_type\tlayout\toverlay\n")
        self.write("docs/fern-measurements/repairs/probe.yaml", refuse)
        record = self.write("docs/fern-measurements/repairs/measurement.json", json.dumps({"probe": "probe.yaml"}))
        log = self.write("docs/fern-measurements/repairs/fern.log", "prior log\n")
        raw = self.write("docs/fern-measurements/repairs/fern-raw_client.py.txt", "PRIOR = 1\n")
        literals = "docs/fern-measurements/parameter-literals"
        digests = self.write(f"{literals}/certified-trees.json", json.dumps({"alpha": "0" * 64}))
        metadata = self.write(f"{literals}/metadata.json", "{}\n")
        self.write("docs/departures/evidence/casing/openapi.yml", refuse)
        self.write("docs/departures/evidence/casing/fern-reference.json", "{}")
        reference = self.write("docs/departures/evidence/casing/fern-reference/client.py", "PRIOR = 1\n")
        before = {path: path.read_text(encoding="utf-8") for path in (record, log, raw, digests, metadata, reference)}

        for family, item in (
            ("handwritten", "alpha"),
            ("measurements", "repairs"),
            ("measurements", "parameter-literals/alpha"),
            ("departure-evidence", "casing"),
        ):
            with self.subTest(family=family, item=item):
                result = self.run_tool("generate", family, item)
                self.assertEqual(result.returncode, 1)
                self.assertIn("fern generate exited 1", result.stderr)
        self.assertEqual((fixture / "fern-expected/src/fern/stale.py").read_text(encoding="utf-8"), "STALE = 1\n")
        self.assertEqual((fixture / "evidence.toml").read_text(encoding="utf-8"), evidence_before)
        self.assertEqual({path: path.read_text(encoding="utf-8") for path in before}, before)

    def test_a_generation_that_exits_zero_with_no_tree_keeps_the_reference(self) -> None:
        fixture = self.handwritten("nu", document="openapi: 3.0.3\nx-stub-empty: true\n")
        evidence = (fixture / "evidence.toml").read_text(encoding="utf-8")

        result = self.run_tool("generate", "handwritten", "nu")

        self.assertEqual(result.returncode, 1)
        self.assertIn("fern generate exited 0 with no tree", result.stderr)
        self.assertEqual((fixture / "fern-expected/src/fern/stale.py").read_text(encoding="utf-8"), "STALE = 1\n")
        self.assertEqual((fixture / "evidence.toml").read_text(encoding="utf-8"), evidence)

    def test_a_case_note_with_no_pair_to_restate_stops_before_fern_runs(self) -> None:
        self.write("docs/fern-measurements/clients/mu/openapi.yml", "openapi: 3.0.3\n")
        self.write(
            "docs/fern-measurements/cases.tsv",
            "case\tdocument\tenum_type\tlayout\toverlay\n"
            "clients/mu\tdocs/fern-measurements/clients/mu/openapi.yml\tpython-enums\tpackaged\t-\n",
        )
        reference = self.write("docs/fern-measurements/clients/mu/fern-expected/client.py", "KEPT = 1\n")
        for label, note, message in (
            ("no pair", "Measured some time ago.\n", "states no Fern CLI and fern-python-sdk version to restate"),
            (
                "a malformed digest",
                f"Fern CLI {CLI} with `fernapi/fern-python-sdk` {SDK}.\n\nCanonical tree SHA-256: `abc123`.\n",
                "names a canonical tree SHA-256 that is no 64-digit digest",
            ),
        ):
            with self.subTest(label):
                path = self.write("docs/fern-measurements/clients/mu/evidence.md", note)
                result = self.run_tool("generate", "measurements", "clients/mu")
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stderr)
                self.assertEqual(self.calls(), [])
                self.assertEqual(path.read_text(encoding="utf-8"), note)
                self.assertEqual(reference.read_text(encoding="utf-8"), "KEPT = 1\n")

    def test_a_departure_note_s_tree_is_regenerated_under_its_recorded_settings(self) -> None:
        self.write("docs/departures/evidence/casing/openapi.yml", "openapi: 3.0.3\n")
        self.write(
            "docs/departures/evidence/casing/fern-reference.json",
            json.dumps({"layout": "flat", "organization": "LanternHarbor"}),
        )
        self.write("docs/departures/evidence/casing/fern-reference/stale.py", "STALE = 1\n")
        self.write("docs/departures/evidence/notree.md", "prose\n")
        self.assertEqual(self.run_tool("list", "departure-evidence").stdout, "casing\n")

        result = self.run_tool("generate", "departure-evidence")

        self.assertEqual(result.returncode, 0, result.stderr)
        tree = self.root / "docs/departures/evidence/casing/fern-reference"
        self.assertTrue((tree / "client.py").is_file())
        self.assertFalse((tree / "stale.py").exists())
        (call,) = self.calls()
        self.assertEqual(call["config"], {"organization": "LanternHarbor", "version": CLI})
        self.assertNotIn("--preview", call["argv"])
        # A non-default organization is no part of the key, packaged layout or not.
        self.write("docs/departures/evidence/casing/fern-reference.json", json.dumps({"organization": "LanternHarbor"}))
        packaged = self.run_tool("generate", "departure-evidence")
        self.assertEqual(packaged.returncode, 0, packaged.stderr)
        self.assert_store_holds_nothing()

    def manifest(self, *rows: str) -> None:
        self.write(
            "docs/openapi-surface/probe-expected/MANIFEST.tsv",
            "key\tform\tverdict\tartifact\tcontrol\tdigest\n" + "".join(f"{row}\n" for row in rows),
        )

    def test_a_probe_tree_and_a_refusal_record_are_each_rewritten_with_their_digest(self) -> None:
        self.write("docs/openapi-surface/probes/kept.yml", "openapi: 3.0.3\n")
        self.write("docs/openapi-surface/probes/refused.yml", "openapi: 3.0.3\nx-stub-refuse: true\n")
        self.manifest(
            f"kept\tabsent-tree\tdiscards\tdocs/openapi-surface/probe-expected/kept\t—\t{'a' * 64}",
            f"refused\trefusal\trefuses\tdocs/openapi-surface/probe-expected/refused.fern-refusal.txt\t—\t{'b' * 64}",
        )
        self.assertEqual(self.run_tool("list", "probes").stdout, "kept\nrefused\n")

        result = self.run_tool("generate", "probes")

        self.assertEqual(result.returncode, 0, result.stderr)
        expected = self.root / "docs/openapi-surface/probe-expected"
        record = (expected / "refused.fern-refusal.txt").read_text(encoding="utf-8")
        self.assertEqual(
            record,
            f"fern_cli_version: {CLI}\nfern_python_sdk_version: {SDK}\ngenerate_exit: 1\n"
            "diagnostic: Stub refused the document\noutput_tree: none\n",
        )
        rows = (expected / "MANIFEST.tsv").read_text(encoding="utf-8").splitlines()
        self.assertEqual(rows[1].split("\t")[5], tree_digest(expected / "kept"))
        self.assertEqual(rows[2].split("\t")[5], hashlib.sha256(record.encode()).hexdigest())

    def test_a_crashed_generator_s_exception_is_the_refusal_diagnostic(self) -> None:
        self.write("docs/openapi-surface/probes/crashed.yml", "openapi: 3.0.3\nx-stub-crash: true\n")
        self.manifest(
            f"crashed\trefusal\tcrashes\tdocs/openapi-surface/probe-expected/crashed.fern-refusal.txt\t—\t{'c' * 64}"
        )
        result = self.run_tool("generate", "probes")
        self.assertEqual(result.returncode, 0, result.stderr)
        record = (self.root / "docs/openapi-surface/probe-expected/crashed.fern-refusal.txt").read_text(
            encoding="utf-8"
        )
        self.assertIn("diagnostic: KeyError: 'type_:Probe'\n", record)

    def test_a_probe_whose_outcome_changes_form_is_written_and_reported_for_a_decision(self) -> None:
        self.write("docs/openapi-surface/probes/turned.yml", "openapi: 3.0.3\nx-stub-refuse: true\n")
        self.write("docs/openapi-surface/probe-expected/turned/src/fern/client.py", "CLIENT = 1\n")
        self.manifest(f"turned\tabsent-tree\tdiscards\tdocs/openapi-surface/probe-expected/turned\t—\t{'a' * 64}")

        result = self.run_tool("generate", "probes", "turned")

        self.assertEqual(result.returncode, 1)
        self.assertIn("changed form (refusal now)", result.stderr)
        self.assertIn("need their form and verdict decided", result.stderr)
        expected = self.root / "docs/openapi-surface/probe-expected"
        self.assertFalse((expected / "turned").exists())
        self.assertIn("turned.fern-refusal.txt", (expected / "MANIFEST.tsv").read_text(encoding="utf-8"))

    def test_an_authored_probe_keeps_its_log_and_a_refused_one_fails_naming_the_registry(self) -> None:
        self.write("docs/openapi-surface/authored-probes/1-ok/openapi.yml", "openapi: 3.0.3\n")
        self.write("docs/openapi-surface/authored-probes/2-no/openapi.yml", "openapi: 3.0.3\nx-stub-refuse: 1\n")

        result = self.run_tool("generate", "authored-probes")

        self.assertEqual(result.returncode, 1)
        self.assertIn("authored-probes: 1 regenerated, 1 failed", result.stdout)
        self.assertIn("2-no: Fern now refuses 2-no", result.stderr)
        case = self.root / "docs/openapi-surface/authored-probes/1-ok"
        log = (case / "fern.log").read_text(encoding="utf-8")
        self.assertTrue(log.startswith(f"Fern CLI {CLI}, python-sdk {SDK}\ncheck exit: 0\nAll checks passed\n\n"))
        self.assertIn("\ngenerate exit: 0\n[api]: python-sdk Wrote files to <workspace>/preview/fern-python-sdk\n", log)
        self.assertTrue((case / "fern-expected/src/fern/client.py").is_file())
        refused = (self.root / "docs/openapi-surface/authored-probes/2-no/fern.log").read_text(encoding="utf-8")
        self.assertIn("generate exit: 1\n[api]: python-sdk Generator logs here: <tmp>\n", refused)

    def test_an_unknown_item_is_refused_before_fern_runs(self) -> None:
        self.handwritten("alpha")
        result = self.run_tool("generate", "handwritten", "nosuch")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "no handwritten item nosuch; `fern-references.py list handwritten` names the family", result.stderr
        )
        self.assertEqual(self.calls(), [])

    def test_a_missing_certified_pair_names_how_to_restore_it(self) -> None:
        self.handwritten("alpha")
        (self.root / "assets/scaffolding/metadata.json").unlink()
        result = self.run_tool("generate", "handwritten")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("git checkout -- assets/scaffolding/metadata.json", result.stderr)

    def test_the_corpus_and_overlay_families_list_their_committed_goldens(self) -> None:
        for path in (
            "tests/fixtures/alpha/expected/src/x.py",
            "tests/fixtures/beta/expected-flat/__init__.py",
            "tests/fixtures/alpha/expected-literals/.crozier-overlay.json",
            "tests/fixtures/alpha/expected-default-max-retries/.crozier-overlay.json",
            "tests/fixtures/gamma/openapi.yml",
            "tests/fixtures/delta/known-fern-failure.json",
        ):
            self.write(path, "{}\n")
        self.assertEqual(self.run_tool("list", "corpus").stdout, "alpha\nbeta\ndelta\n")
        self.assertEqual(
            self.run_tool("list", "overlays").stdout,
            "alpha/expected-default-max-retries\nalpha/expected-literals\n",
        )

    def test_the_refusal_family_names_classes_findings_and_rerunnable_evidence(self) -> None:
        self.write(
            "docs/fern-refusals/classes.tsv",
            "class\tfamily\tfern_stage\tfern_exit\tdiagnostic\tdocuments\tstatus\tcrozier_diagnostic\tpopulation_strict\n"
            "zeta\tnames\tcheck\t1\tx\t0\tunevaluated\t—\t—\n",
        )
        self.write(
            "docs/fern-refusals/findings.tsv",
            "finding\tkind\tcheck_exit\tgenerate_exit\tdiagnostic\tprobe\neta\tgenerates\t0\t0\t—\tp.yml\n",
        )
        self.write("docs/fern-refusals/zeta/evidence/rerun.yml", "openapi: 3.0.3\n")
        self.write("docs/fern-refusals/zeta/evidence/rerun.pinned-fern.log", "old\n")
        self.write("docs/fern-refusals/zeta/evidence/orphan.pinned-fern.log", "old\n")
        self.assertEqual(self.run_tool("list", "refusals").stdout, "zeta\nfindings/eta\nzeta/evidence/rerun\n")

        result = self.run_tool("generate", "refusals", "zeta/evidence/rerun")

        self.assertEqual(result.returncode, 0, result.stderr)
        log = (self.root / "docs/fern-refusals/zeta/evidence/rerun.pinned-fern.log").read_text(encoding="utf-8")
        self.assertTrue(log.startswith(f"Fern CLI {CLI}, python-sdk {SDK}\ncheck exit: 0\n"))
        self.assertEqual((self.root / "docs/fern-refusals/zeta/evidence/orphan.pinned-fern.log").read_text(), "old\n")


# The parts of the real tree `fern-references.py check` reads. A golden tree is
# read only for its existence and its `.fern/metadata.json` or overlay manifest,
# so a copy carries just those of it.
INVENTORY = (
    "assets/scaffolding/metadata.json",
    "tests/fixtures",
    "docs/fern-measurements",
    "docs/openapi-surface/handwritten",
    "docs/openapi-surface/probes",
    "docs/openapi-surface/probe-expected",
    "docs/openapi-surface/authored-probes",
    "docs/openapi-surface/fern-refusals/findings",
    "docs/fern-refusals",
    "docs/departures/evidence",
)
GOLDEN_TREES = {
    "expected",
    "expected-flat",
    "expected-literals",
    "expected-default-max-retries",
    "fern-expected",
    "fern-reference",
}
TREE_MARKERS = (".fern/metadata.json", ".crozier-overlay.json")

# Loaded by every Python the check starts: a socket connection is recorded and
# ends the run.
GUARD = r"""
import os, socket

def _refuse(*args, **kwargs):
    with open(os.environ["CHECK_NETWORK"], "a", encoding="utf-8") as handle:
        handle.write(f"connect {args[1:] or kwargs}\n")
    raise SystemExit("inventory check guard: a network connection was attempted")

socket.socket.connect = _refuse
socket.socket.connect_ex = _refuse
socket.create_connection = _refuse
"""
RECORDING_TOOL = '#!/bin/sh\necho "$(basename "$0") $*" >> "$CHECK_TOOL_CALLS"\nexit 97\n'


def copy_inventory(destination: Path) -> None:
    """The inventory files of the real tree, each golden tree as its directory
    and marker files."""
    for relative in INVENTORY:
        source = REPO / relative
        if source.is_file():
            (destination / relative).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination / relative)
            continue
        for directory, names, files in os.walk(source):
            here = Path(directory)
            target = destination / here.relative_to(REPO)
            target.mkdir(parents=True, exist_ok=True)
            is_tree = here.name in GOLDEN_TREES or here.parent.name == "probe-expected"
            if is_tree:
                for marker in TREE_MARKERS:
                    if (here / marker).is_file():
                        (target / marker).parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(here / marker, target / marker)
                names.clear()
                continue
            for name in files:
                shutil.copy2(here / name, target / name)


def load_tool(root: Path) -> ModuleType:
    """`fern-references.py` over `root`, to name the items a broken copy breaks."""
    previous = os.environ.get("CROZIER_FERN_REFERENCES_ROOT")
    os.environ["CROZIER_FERN_REFERENCES_ROOT"] = str(root)
    try:
        spec = importlib.util.spec_from_file_location("fern_references_inventory", TOOL)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        # Its dataclasses resolve their module through sys.modules as they are made.
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        if previous is None:
            del os.environ["CROZIER_FERN_REFERENCES_ROOT"]
        else:
            os.environ["CROZIER_FERN_REFERENCES_ROOT"] = previous


@unittest.skipIf(os.name == "nt", "the stand-in tools are POSIX executables")
class InventoryCheckTests(unittest.TestCase):
    """`fern-references.py check` driven as a subprocess over a copy of the real
    inventory: the copy as committed passes, and each broken copy, one input of
    one kind moved away or made unrestatable, fails naming its item. Every run
    has a recording `fern` and `docker` first on PATH and a `sitecustomize`
    refusing socket connections, and asserts neither was reached."""

    root: Path
    guard: Path
    module: ModuleType
    scratch: tempfile.TemporaryDirectory[str]

    @classmethod
    def setUpClass(cls) -> None:
        cls.scratch = tempfile.TemporaryDirectory(prefix="fern-references-inventory-")
        # Resolved, as the tool resolves its root: macOS's temporary directory
        # is a symbolic link (/var -> /private/var), so an unresolved root never
        # contains the paths the tool reports.
        cls.root = Path(cls.scratch.name).resolve() / "repo"
        copy_inventory(cls.root)
        cls.guard = Path(cls.scratch.name) / "guard"
        (cls.guard / "site").mkdir(parents=True)
        (cls.guard / "site/sitecustomize.py").write_text(GUARD, encoding="utf-8")
        (cls.guard / "bin").mkdir()
        for tool in ("fern", "docker"):
            (cls.guard / "bin" / tool).write_text(RECORDING_TOOL, encoding="utf-8")
            (cls.guard / "bin" / tool).chmod(0o755)
        cls.module = load_tool(cls.root)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.scratch.cleanup()

    def run_tool(self, *args: str) -> subprocess.CompletedProcess[str]:
        calls, network = self.guard / "tool-calls.log", self.guard / "network.log"
        result = subprocess.run(
            [sys.executable, str(TOOL), *args],
            env={
                **os.environ,
                "PATH": f"{self.guard / 'bin'}{os.pathsep}{os.environ['PATH']}",
                "PYTHONPATH": str(self.guard / "site"),
                "CROZIER_FERN_REFERENCES_ROOT": str(self.root),
                "CHECK_TOOL_CALLS": str(calls),
                "CHECK_NETWORK": str(network),
            },
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertFalse(calls.exists(), calls.read_text(encoding="utf-8") if calls.exists() else "")
        self.assertFalse(network.exists(), network.read_text(encoding="utf-8") if network.exists() else "")
        return result

    def broken(self, path: Path, change: str | None = None) -> None:
        """Break one input of the copy for this test: move it away, or rewrite
        it as `change` says; the copy is restored once the test ends."""
        self.asides = getattr(self, "asides", 0) + 1
        aside = Path(self.scratch.name) / "aside" / self.id() / str(self.asides)
        aside.parent.mkdir(parents=True, exist_ok=True)
        if path.is_dir():
            path.rename(aside)
            self.addCleanup(aside.rename, path)
            return
        shutil.copy2(path, aside)
        self.addCleanup(shutil.copy2, aside, path)
        if change is None:
            path.unlink()
        else:
            path.write_text(change, encoding="utf-8")

    def assert_names(self, family: str, item: str, reason: str) -> str:
        result = self.run_tool("check")
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertEqual("", result.stdout, "every diagnostic goes to stderr")
        lines = [line for line in result.stderr.splitlines() if line.startswith(f"{family} {item}: ")]
        self.assertEqual(1, len(lines), result.stderr)
        self.assertIn(reason, lines[0])
        self.assertIn("broken item(s)", result.stderr)
        return lines[0]

    def case_with_own_document(self) -> str:
        cases = self.module.cases()
        documents = [row.document for row in cases.values()]
        return next(
            name
            for name, row in cases.items()
            if row.document.is_relative_to(self.root / "docs/fern-measurements")
            and documents.count(row.document) == 1
            and row.overlay is None
        )

    def test_the_copy_as_committed_has_no_broken_item(self) -> None:
        result = self.run_tool("check")
        self.assertEqual((0, ""), (result.returncode, result.stdout), result.stderr)
        self.assertNotIn("broken item", result.stderr)
        named = self.run_tool("check", "measurements", "refusals")
        self.assertEqual((0, ""), (named.returncode, named.stdout), named.stderr)

    def test_a_cases_row_whose_document_is_gone(self) -> None:
        case = self.case_with_own_document()
        self.broken(self.module.cases()[case].document)
        self.assert_names("measurements", case, "does not exist")

    def test_a_cases_row_whose_overlay_base_tree_moved(self) -> None:
        case, row = next(
            (name, row)
            for name, row in self.module.cases().items()
            if row.overlay is not None and row.overlay.base is not None
        )
        self.broken(row.overlay.base)
        self.assert_names("measurements", case, "its overlay base tree")

    def test_a_parameter_literals_claim_whose_hand_written_document_is_gone(self) -> None:
        case = next(
            name
            for name in self.module.parameter_literal_cases()
            if (self.root / "docs/openapi-surface/handwritten" / name / "openapi.yml").is_file()
        )
        self.broken(self.root / "docs/openapi-surface/handwritten" / case / "openapi.yml")
        self.assert_names("measurements", f"parameter-literals/{case}", "certified-trees.json names it")

    def test_a_hand_written_fixture_whose_document_is_gone(self) -> None:
        name = self.module.list_handwritten()[0]
        self.broken(self.root / "docs/openapi-surface/handwritten" / name / "openapi.yml")
        self.assert_names("handwritten", name, f"docs/openapi-surface/handwritten/{name}/openapi.yml does not exist")

    def test_a_refusal_log_whose_document_is_gone(self) -> None:
        item, logged = next(iter(self.module.refusal_logs().items()))
        self.broken(logged.document)
        self.assert_names("measurements", item, "is beside its log")

    def test_a_pinned_run_whose_probe_is_gone(self) -> None:
        case, record = next(iter(self.module.pinned_runs().items()))
        self.broken(self.module.pinned_run(record).probe)
        self.assert_names("measurements", case, "must be an object whose `probe` names a file")

    def test_a_probe_whose_document_is_gone(self) -> None:
        documents = {row.document for row in self.module.cases().values()}
        probe = next(
            name
            for name in self.module.list_probes()
            if self.root / "docs/openapi-surface/probes" / f"{name}.yml" not in documents
        )
        self.broken(self.root / "docs/openapi-surface/probes" / f"{probe}.yml")
        self.assert_names("probes", probe, "MANIFEST.tsv names it")

    def test_an_authored_probe_whose_document_is_gone(self) -> None:
        case = self.module.list_authored()[0]
        self.broken(self.root / "docs/openapi-surface/authored-probes" / case / "openapi.yml")
        self.assert_names("authored-probes", case, "its document")

    def test_a_refusal_class_whose_registered_probe_is_gone(self) -> None:
        name = self.module.registry_column(self.module.REGISTRY / "classes.tsv", "class")[0]
        self.broken(self.root / "docs/fern-refusals" / name / "probe.yml")
        self.assert_names("refusals", name, "classes.tsv names the class")

    def test_a_finding_whose_registered_probe_is_gone(self) -> None:
        name = self.module.registry_column(self.module.REGISTRY / "findings.tsv", "finding")[0]
        self.broken(self.module.finding_probe(name))
        self.assert_names("refusals", f"findings/{name}", "findings.tsv names it")

    def test_a_departure_whose_document_is_gone(self) -> None:
        case = self.module.list_departure_evidence()[0]
        self.broken(self.root / "docs/departures/evidence" / case / "openapi.yml")
        self.assert_names("departure-evidence", case, "its document")

    def test_a_corpus_row_whose_committed_specification_is_gone(self) -> None:
        rows, sources = self.module.corpus_rows(), self.module.corpus_sources()
        fixture = next(fixture for fixture in self.module.list_corpus() if sources.get(rows.get(fixture, "")))
        self.broken(self.root / sources[rows[fixture]][0])
        self.assert_names("corpus", fixture, "its committed specification")

    def test_an_evidence_toml_with_no_single_restatable_pair_line(self) -> None:
        name = self.module.list_handwritten()[0]
        evidence = self.root / "docs/openapi-surface/handwritten" / name / "evidence.toml"
        text = evidence.read_text(encoding="utf-8")
        self.broken(evidence, re.sub(r'(?m)^fern_python_sdk_version = "[^"]*"\n', "", text))
        self.assert_names("handwritten", name, "has no single `fern_python_sdk_version` line to restate")

    def note_case(self, digest: bool) -> tuple[str, Path]:
        for name in self.module.cases():
            note = self.root / "docs/fern-measurements" / name / "evidence.md"
            if note.is_file() and (not digest or "Canonical tree SHA-256" in note.read_text(encoding="utf-8")):
                return name, note
        raise AssertionError("the inventory has no measurement evidence note")

    def test_an_evidence_note_stating_no_restatable_pair(self) -> None:
        name, note = self.note_case(digest=False)
        # The pair stated across a line break, as gauge-public-fields once did.
        wrapped = re.sub(r"(fernapi/fern-python-sdk`?:?) ", "\\1\n", note.read_text(encoding="utf-8"))
        self.broken(note, wrapped)
        self.assert_names("measurements", name, "states no Fern CLI and fern-python-sdk version to restate")

    def test_an_evidence_note_naming_a_malformed_digest(self) -> None:
        name, note = self.note_case(digest=True)
        malformed = re.sub(r"(Canonical tree SHA-256: `)[0-9a-f]{64}", "\\1abc123", note.read_text(encoding="utf-8"))
        self.broken(note, malformed)
        self.assert_names("measurements", name, "is no 64-digit digest")

    def test_an_evidence_toml_naming_a_malformed_digest(self) -> None:
        name = self.module.list_handwritten()[0]
        evidence = self.root / "docs/openapi-surface/handwritten" / name / "evidence.toml"
        text = evidence.read_text(encoding="utf-8")
        self.broken(evidence, re.sub(r'(?m)^digest = "[0-9a-f]{64}"$', 'digest = "abc123"', text))
        self.assert_names("handwritten", name, "`digest` 'abc123' is no 64-digit digest")

    def test_an_evidence_toml_naming_a_malformed_version(self) -> None:
        name = self.module.list_handwritten()[0]
        evidence = self.root / "docs/openapi-surface/handwritten" / name / "evidence.toml"
        text = evidence.read_text(encoding="utf-8")
        self.broken(evidence, re.sub(r'(?m)^fern_cli_version = "[^"]*"$', 'fern_cli_version = "5.163"', text))
        self.assert_names("handwritten", name, "`fern_cli_version` '5.163' is no release version")

    def test_an_evidence_note_naming_a_malformed_version(self) -> None:
        name, note = self.note_case(digest=False)
        malformed = re.sub(
            r"(fernapi/fern-python-sdk`?:? [0-9]+\.[0-9]+\.[0-9]+)", "\\1x", note.read_text(encoding="utf-8")
        )
        self.broken(note, malformed)
        self.assert_names("measurements", name, "which is no release version")

    def break_document(self, fixture: str) -> None:
        """Move away every document `vendored_spec` could read for `fixture`."""
        while (document := self.module.vendored_spec(fixture)).is_file():
            self.broken(document)

    def test_a_committed_corpus_row_with_no_registered_source(self) -> None:
        rows, committed = self.module.corpus_rows(), self.module.committed_rows()
        fixture = next(fixture for fixture in self.module.list_corpus() if rows.get(fixture) in committed)
        registry = self.root / self.module.CORPUS_SOURCES
        text = registry.read_text(encoding="utf-8")
        kept = "".join(line for line in text.splitlines(keepends=True) if not line.startswith(f"{rows[fixture]}\t"))
        self.broken(registry, kept)
        self.assert_names("corpus", fixture, "records no file of it")

    def test_a_corpus_row_whose_flat_golden_document_is_gone(self) -> None:
        rows, flats = self.module.corpus_rows(), self.module.flat_goldens()
        fixture = next(fixture for fixture in self.module.list_corpus() if fixture in rows and fixture not in flats)
        spec = next(spec for flat, spec in flats.items() if spec != flat)
        listing = self.root / self.module.FIXTURES / "flat-goldens.txt"
        self.broken(listing, listing.read_text(encoding="utf-8") + f"{fixture}|{spec}\n")
        self.break_document(spec)
        self.assert_names("corpus", fixture, "the document its flat golden is generated from")

    def test_a_vendored_packaged_fixture_whose_document_is_gone(self) -> None:
        fixtures, rows = self.root / self.module.FIXTURES, self.module.corpus_rows()
        fixture = next(f for f in self.module.list_corpus() if f not in rows and (fixtures / f / "expected").is_dir())
        self.broken(fixtures / fixture / "openapi.yml")
        self.assert_names("corpus", fixture, "its document")

    def test_a_flat_fixture_outside_the_corpus_whose_document_is_gone(self) -> None:
        fixtures, rows, flats = self.root / self.module.FIXTURES, self.module.corpus_rows(), self.module.flat_goldens()
        fixture = next(
            f
            for f in self.module.list_corpus()
            if f not in rows and f in flats and not (fixtures / f / "expected").is_dir()
        )
        self.break_document(flats[fixture])
        self.assert_names("corpus", fixture, "the document its flat golden is generated from")

    def recorded_overlay(self) -> str:
        return next(item for item in self.module.list_overlays() if item.endswith("/expected-default-max-retries"))

    def test_an_overlay_whose_manifest_is_no_json(self) -> None:
        item = self.recorded_overlay()
        self.broken(self.root / self.module.FIXTURES / item / self.module.OVERLAY_MANIFEST, "{")
        self.assert_names("overlays", item, "cannot read")

    def test_an_overlay_whose_base_golden_is_gone(self) -> None:
        item = self.recorded_overlay()
        self.broken(self.root / self.module.FIXTURES / item.partition("/")[0] / "expected")
        self.assert_names("overlays", item, "the golden it is reduced against")

    def test_an_overlay_outside_the_corpus_whose_document_is_gone(self) -> None:
        rows = self.module.corpus_rows()
        item = next(item for item in self.module.list_overlays() if item.partition("/")[0] not in rows)
        self.break_document(item.partition("/")[0])
        self.assert_names("overlays", item, "its document")

    def test_a_family_whose_listing_fails_is_named_and_the_later_families_still_checked(self) -> None:
        classes = self.root / self.module.REGISTRY / "classes.tsv"
        text = classes.read_text(encoding="utf-8")
        self.broken(classes, text.replace("class\t", "kind\t", 1))
        case = self.module.list_departure_evidence()[0]
        self.broken(self.root / "docs/departures/evidence" / case / "openapi.yml")
        self.assert_names("refusals", "(its listing)", "has no `class` column")
        self.assert_names("departure-evidence", case, "its document")

    def test_generate_refuses_a_broken_item_with_the_line_check_prints_before_fern_starts(self) -> None:
        case = self.case_with_own_document()
        self.broken(self.module.cases()[case].document)
        line = self.assert_names("measurements", case, "does not exist")
        refused = self.run_tool("generate", "measurements", case)
        self.assertEqual(1, refused.returncode, refused.stderr)
        self.assertIn(f"fern-references: {line}\n", refused.stderr)
        self.assertIn("0 regenerated, 1 failed", refused.stdout)


if __name__ == "__main__":
    unittest.main()

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
(root / ".fern" / "metadata.json").write_text(json.dumps({"cliVersion": json.loads(config)["version"], "generatorVersion": version}))
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
        }
        # The tool loads golden_overlay.py from beside itself.
        self.tool = self.root / "tools/fern-goldens/fern-references.py"
        self.tool.parent.mkdir(parents=True)
        shutil.copy2(TOOL, self.tool)
        shutil.copy2(REPO / "tools/fern-goldens/golden_overlay.py", self.tool.parent / "golden_overlay.py")

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
        self.write("docs/fern-refusals/findings.tsv", "finding\tkind\neta\tgenerates\n")

        result = self.run_tool("generate", "refusals")

        self.assertEqual(result.returncode, 0, result.stderr)
        changes = self.root / ".local/fern-references/refusals/probe.zeta.changes.jsonl"
        self.assertEqual(
            sorted(tuple(call["argv"]) for call in self.delegate_calls()),
            [("finding", "--jobs", "1", "eta"), ("probe", "--jobs", "1", "--changes", str(changes), "zeta")],
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
        for record in ('{"cliVersion": null, "generatorVersion": "5.41.3"}', '["5.163.1"]', '{"cliVersion": 5}'):
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
            ("a/b\tdocs/missing.yml\tliterals\tpackaged\t-\n", "is no file of this repository"),
            ("a/b\t../outside.yml\tliterals\tpackaged\t-\n", "is no file of this repository"),
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


if __name__ == "__main__":
    unittest.main()

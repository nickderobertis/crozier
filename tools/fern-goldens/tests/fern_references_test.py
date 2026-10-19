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
import json
import os
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
    log.write(json.dumps({"argv": sys.argv[1:], "config": json.loads(config), "generators": generators}) + "\n")
if sys.argv[1] == "check":
    if "x-stub-refuse" in document:
        print("[sdk] 1 error\n    [error]\n        path: openapi\n        issue: Stub refused the document")
        sys.exit(1)
    print("All checks passed")
    sys.exit(0)
if "x-stub-crash" in document:
    print("Traceback (most recent call last):\n    raise KeyError(key)\n  KeyError: 'type_:Probe'")
    sys.exit(1)
if "x-stub-refuse" in document:
    print(f"[api]: python-sdk Generator logs here: /tmp/tmp-stub-1\n[api]: python-sdk {workspace}\n                  [error] Stub refused the document")
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
(package / "core").mkdir()
if "enum_type: python_enums" in generators:
    (package / "core" / "enum.py").write_text("ENUM = 1\n")
else:
    (package / "literal.py").write_text("LITERAL = 1\n")
for audience in re.findall(r"^      - (\w+)$", generators, re.M):
    (package / f"audience_{audience}.py").write_text("AUDIENCE = 1\n")
for url in re.findall(r"http://127\.0\.0\.1:\d+/\S+?\.yml", document):
    (package / "remote.txt").write_text(urllib.request.urlopen(url).read().decode())
(root / ".fern").mkdir(parents=True, exist_ok=True)
(root / ".fern" / "metadata.json").write_text(json.dumps({"cliVersion": json.loads(config)["version"], "generatorVersion": version}))
print(f"[api]: python-sdk Wrote files to {root}")
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
        fixture = self.handwritten("alpha", evidence=EVIDENCE.format("0" * 64) + 'audiences = ["public"]\n')
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

    def test_an_explicit_version_overrides_the_certified_pair(self) -> None:
        self.handwritten("alpha")
        result = self.run_tool("generate", "handwritten", "--version", "7.0.0", "--cli-version", "8.0.0")
        self.assertEqual(result.returncode, 0, result.stderr)
        (call,) = self.calls()
        self.assertEqual(call["config"]["version"], "8.0.0")
        self.assertIn("version: 7.0.0", call["generators"])

    def test_a_literals_measurement_is_an_overlay_of_its_base_with_the_base_digest(self) -> None:
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
                "digest": tree_digest(base),
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
        result = self.run_tool("generate", "measurements", "clients/delta-flat")
        self.assertEqual(result.returncode, 0, result.stderr)
        tree = self.root / "docs/fern-measurements/clients/delta-flat/fern-expected"
        self.assertTrue((tree / "client.py").is_file())
        self.assertFalse((tree / "src").exists())
        (call,) = self.calls()
        self.assertNotIn("--preview", call["argv"])

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

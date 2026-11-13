#!/usr/bin/env python3
"""The cold-registry build hands its artifacts to a job's later steps, over crozier's real source.

A scratch checkout holds crozier's and its e2e suite's real sources, so the real
entry points run unchanged: the cold build, `crozier:build`, the e2e suite's build,
the corpus recipe and the offline proof's own case. Each edit below is a real
change to `src/lib.rs`. This scratch tree's compiles are this test's fixture.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
COPIED = (
    "Cargo.toml",
    "Cargo.lock",
    "rust-toolchain.toml",
    ".cargo",
    "src",
    "templates",
    "assets",
    "crates/crozier-e2e",
    "tests/support",
    "tests/nested-discriminator/golden",
    "tests/corpus_match/match.sh",
    "tests/corpus_match/corpus_offline_test.py",
    "pool-maintenance",
    "tools/ci",
    "tools/ci-journeys",
    "tools/github-action",
    "README.md",
    "LICENSE",
    "NOTICE",
    "licenses",
)
CASE = "OfflineCorpusRecipes.test_warmed_build_needs_no_network_from_a_cold_registry"
EMBED = re.compile(r'include_(?:str|bytes)!\(\s*"([^"]+)"')


def project_command(project: str, target: str) -> list[str]:
    """A target's own cargo command, split as a shell would."""
    data = json.loads((REPO / project / "project.json").read_text(encoding="utf-8"))
    return [word.strip('"') for word in re.findall(r'"[^"]*"|\S+', data["targets"][target]["options"]["command"])]


def copy_into(root: Path, relative: str) -> None:
    source, destination = REPO / relative, root / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns("target", "__pycache__"))
    else:
        shutil.copy2(source, destination)


def workspace_members() -> set[str]:
    """Every member the root manifest declares: cargo reads each one to load the workspace at all."""
    manifest = tomllib.loads((REPO / "Cargo.toml").read_text(encoding="utf-8"))
    return {member for member in manifest["workspace"]["members"] if member != "."}


def embedded_by_the_suite() -> set[str]:
    """Every committed file the e2e suite compiles in."""
    found: set[str] = set()
    for source in [*(REPO / "crates/crozier-e2e").rglob("*.rs"), *(REPO / "tests/support").rglob("*.rs")]:
        for literal in EMBED.findall(source.read_text(encoding="utf-8")):
            resolved = (source.parent / literal).resolve()
            if resolved.is_relative_to(REPO) and resolved.is_file():
                found.add(resolved.relative_to(REPO).as_posix())
    return found


@unittest.skipUnless(sys.platform == "linux" and platform.machine() in {"x86_64", "aarch64"}, "uses Linux seccomp")
class ColdRegistryHandoff(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        for relative in sorted({*COPIED, *workspace_members(), *embedded_by_the_suite()}):
            if not (self.root / relative).exists():
                copy_into(self.root, relative)
        self.env = {
            **{key: value for key, value in os.environ.items() if key != "CARGO_TARGET_DIR"},
            "CARGO_HOME": str(self.root / "cold-home"),
            "CROZIER_COLD_REGISTRY_HANDOFF": "1",
            "RUSTC_WRAPPER": "",
        }
        self.script = self.root / "tests/corpus_match/corpus_offline_test.py"
        self.record = self.root / "target/cold-registry-handoff.json"

    def run_in_scratch(self, *command: str) -> subprocess.CompletedProcess[str]:
        run = subprocess.run(command, cwd=self.root, env=self.env, capture_output=True, text=True)
        self.assertEqual(0, run.returncode, f"{' '.join(command)}\n{run.stdout[-2000:]}\n{run.stderr[-4000:]}")
        return run

    def compiled(self, *command: str) -> set[str]:
        """Which crozier and e2e targets this build compiled rather than reused."""
        names: set[str] = set()
        for line in self.run_in_scratch(*command).stdout.splitlines():
            message = json.loads(line) if line.startswith("{") else {}
            is_ours = message.get("reason") == "compiler-artifact" and message["target"]["name"] in {"crozier", "e2e"}
            if is_ours and not message["fresh"]:
                names.add(f"{message['target']['name']}:{message['target']['kind'][0]}")
        return names

    def crozier_build(self) -> set[str]:
        return self.compiled(*project_command("crates/crozier-e2e", "build-replay"), "--message-format=json")

    def suite_build(self) -> set[str]:
        return self.compiled(
            *project_command("crates/crozier-e2e", "test"), "--no-run", "--cargo-message-format", "json"
        )

    def proof(self) -> str:
        return self.run_in_scratch(sys.executable, str(self.script), CASE).stderr

    def edit_source(self, value: int) -> None:
        with (self.root / "src/lib.rs").open("a", encoding="utf-8") as handle:
            handle.write(f"\npub const COLD_HANDOFF_PROBE_{value}: u8 = {value};\n")

    def edit_suite_only(self, value: int) -> None:
        """A change the e2e suite's own build sees and crozier's library and binary do not."""
        with (self.root / "crates/crozier-e2e/tests/e2e.rs").open("a", encoding="utf-8") as handle:
            handle.write(f"\n#[test]\nfn cold_handoff_probe_{value}() {{}}\n")

    def binary_digest(self) -> str:
        return hashlib.sha256((self.root / "target/e2e/crozier").read_bytes()).hexdigest()

    def test_later_steps_reuse_the_denied_build_and_a_changed_source_is_rebuilt_or_rejected(self) -> None:
        self.run_in_scratch(sys.executable, str(self.script), "--cold-registry-build")
        self.assertTrue(self.record.is_file(), "the cold build recorded nothing to hand off")
        self.assertTrue((self.root / "cold-home/registry/src").is_dir(), "the job's own CARGO_HOME holds the registry")
        built = self.binary_digest()

        # Handoff: every real later entry point reuses what the denied build left.
        self.assertEqual(set(), self.crozier_build())
        self.assertEqual(set(), self.suite_build())
        listed = self.root / "listed.txt"
        self.run_in_scratch("env", f"CORPUS_MATCH_LIST={listed}", "bash", "tests/corpus_match/match.sh")
        self.assertIn("swagger_petstore_flat_matches_fern", listed.read_text(encoding="utf-8"))
        self.assertEqual(built, self.binary_digest())
        self.assertIn("is the one made with sockets denied", self.proof())
        self.assertEqual(set(), self.crozier_build(), "the proof's own run compiled nothing")

        # A second cold-registry step only builds the binary: the record stands.
        recorded = self.record.read_bytes()
        self.run_in_scratch(sys.executable, str(self.script), "--cold-registry-build")
        self.assertEqual(recorded, self.record.read_bytes())

        # A changed source reaching the proof first is compiled there, with sockets denied.
        self.edit_source(1)
        self.assertIn("rebuilt a changed input with sockets denied", self.proof())
        self.assertNotEqual(recorded, self.record.read_bytes())
        self.assertEqual(set(), self.crozier_build())

        # A mixed result whose reused artifacts are all the recorded ones holds: the
        # rebuilt suite ran denied, and the library and binary it reuses were recorded.
        proven = json.loads(self.record.read_text(encoding="utf-8"))["artifacts"]
        self.edit_suite_only(1)
        self.assertIn("rebuilt a changed input with sockets denied", self.proof())
        updated = json.loads(self.record.read_text(encoding="utf-8"))["artifacts"]
        library = next(path for path in proven if path.endswith(".rlib"))
        self.assertEqual(proven[library], updated[library])

        # One reaching a normal build first is compiled with sockets up, so the proof
        # rejects the handoff and does the cold build itself.
        self.edit_source(2)
        self.assertEqual({"crozier:lib", "crozier:bin"}, self.crozier_build())
        self.assertEqual({"e2e:test"}, self.suite_build())
        unrecorded = self.record.read_bytes()
        self.assertIn("rejected the handoff", self.proof())
        self.assertEqual(unrecorded, self.record.read_bytes())

        # Dirtying only the suite now makes the denied run report both: the suite rebuilt,
        # the library and binary fresh from that sockets-up build. The rebuild proves
        # nothing about those, so the whole result is rejected and nothing is recorded.
        self.edit_suite_only(2)
        mixed = self.proof()
        self.assertIn("rejected the handoff", mixed)
        self.assertNotIn("rebuilt a changed input with sockets denied", mixed)
        self.assertRegex(mixed, r"rejected the handoff; [1-9]\d* artifact\(s\) rebuilt with sockets denied, but")
        self.assertIn("libcrozier", mixed)
        self.assertEqual(unrecorded, self.record.read_bytes())


if __name__ == "__main__":
    unittest.main()

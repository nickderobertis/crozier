#!/usr/bin/env python3
"""The uv workspace's own invariants, read from the committed manifests.

* The tooling ruff the lock resolves is exactly `.ruff-version`: `uv run` puts
  the workspace venv first on PATH, and crozier shells out to the first `ruff`
  there, so another version would change what a tooling suite's
  `crozier generate` emits.
* The root manifest is still the maturin-built `crozier` distribution, and uv
  never builds or installs it into the tooling venv.
* Every project directory the coverage paths name is a workspace member with its own
  manifest beside its project.json, that project declares the four uniform
  Python targets the gate runs, and the coverage aggregate depends on its
  `test`.
"""

from __future__ import annotations

import json
import tomllib
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
ROOT_MANIFEST = tomllib.loads((REPO / "pyproject.toml").read_text(encoding="utf-8"))
LOCK = tomllib.loads((REPO / "uv.lock").read_text(encoding="utf-8"))
PYTHON_TARGETS = ("format", "lint", "typecheck", "test")


def measured_directories() -> list[str]:
    """Each tooling project's directory: the first path of its coverage `paths` entry."""
    return [entries[0].rstrip("/") for entries in ROOT_MANIFEST["tool"]["coverage"]["paths"].values()]


class TheToolingRuffIsTheGenerationRuff(unittest.TestCase):
    def test_the_lock_resolves_the_ruff_version_file(self) -> None:
        pinned = (REPO / ".ruff-version").read_text(encoding="utf-8").strip()
        locked = [package["version"] for package in LOCK["package"] if package["name"] == "ruff"]
        self.assertEqual(
            [pinned],
            locked,
            "uv.lock's ruff must equal .ruff-version: set `ruff==<.ruff-version>` in the root pyproject.toml's "
            "dev group, then `uv lock`",
        )
        self.assertIn(f"ruff=={pinned}", ROOT_MANIFEST["dependency-groups"]["dev"])


class TheRootManifestIsStillTheCrozierDistribution(unittest.TestCase):
    def test_maturin_builds_crozier_and_uv_leaves_it_alone(self) -> None:
        self.assertEqual("maturin", ROOT_MANIFEST["build-system"]["build-backend"])
        self.assertEqual("crozier", ROOT_MANIFEST["project"]["name"])
        self.assertEqual("bin", ROOT_MANIFEST["tool"]["maturin"]["bindings"])
        self.assertIs(False, ROOT_MANIFEST["tool"]["uv"]["package"])
        # The tooling's dependencies live in a dependency group, never in the
        # published distribution's metadata.
        self.assertNotIn("dependencies", ROOT_MANIFEST["project"])


class EveryMeasuredProjectIsAWorkspaceProject(unittest.TestCase):
    def test_coverage_sources_are_members_with_the_uniform_targets(self) -> None:
        members = ROOT_MANIFEST["tool"]["uv"]["workspace"]["members"]
        sources = measured_directories()
        self.assertTrue(sources)
        for source in sources:
            with self.subTest(source=source):
                self.assertIn(source, members)
                manifest = tomllib.loads((REPO / source / "pyproject.toml").read_text(encoding="utf-8"))
                # Publishes nothing, so the typed-packaging rule has nothing to hold.
                self.assertNotIn("build-system", manifest)
                self.assertIs(False, manifest["tool"]["uv"]["package"])
                project = json.loads((REPO / source / "project.json").read_text(encoding="utf-8"))
                self.assertIn("lang:python", project["tags"])
                self.assertNotIn("tier:promoted", project["tags"])
                for target in PYTHON_TARGETS:
                    self.assertIn(target, project["targets"])

    def test_the_coverage_aggregate_depends_on_every_measured_project(self) -> None:
        aggregate = json.loads((REPO / "tools" / "python-workspace" / "project.json").read_text(encoding="utf-8"))
        measured = {
            json.loads((REPO / source / "project.json").read_text(encoding="utf-8"))["name"]
            for source in measured_directories()
        }
        self.assertEqual(measured - {aggregate["name"]}, set(aggregate["implicitDependencies"]))
        self.assertEqual(["^test", "test"], aggregate["targets"]["coverage"]["dependsOn"])


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""The offline corpus journey leaves a cache it found as it found it.

`corpus_offline_test.py` moves the ignored corpus cache aside while it runs the
real recipes with sockets denied; when a recipe fails, the original cache must
come back untouched and nothing the failed recipe wrote may survive. This drives
the real journey over a synthetic root whose recipe fails after writing.

Run: `just test-corpus-offline` (the `corpus-match` project's `test-offline`).
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

# Every child these tests start has its output decoded as UTF-8, so a Python
# child writes UTF-8 too, whatever the platform locale (cp1252 on Windows).
os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[2]


class OfflineCacheRecovery(unittest.TestCase):
    def test_offline_recipe_failure_restores_the_original_cache(self) -> None:
        spec = importlib.util.spec_from_file_location(
            "offline_cache_recovery", REPO / "tests/corpus_match/corpus_offline_test.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if getattr(module.OfflineCorpusRecipes, "__unittest_skip__", False):
            self.skipTest(module.OfflineCorpusRecipes.__unittest_skip_why__)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cache = root / ".local/corpus"
            cache.mkdir(parents=True)
            marker = cache / "original.txt"
            marker.write_text("original cached bytes", encoding="utf-8", newline="\n")
            (root / "justfile").write_text(
                "test-corpus-match:\n    mkdir -p .local/corpus/generated\n    false\n\nsurface-census:\n    true\n",
                encoding="utf-8",
                newline="\n",
            )
            # The warm step fetches locked crates: give the root a package with
            # none, so it succeeds offline and the failing recipe is reached. The
            # root carries no census fallback, so there is no parser to warm.
            (root / "Cargo.toml").write_text(
                '[package]\nname = "synthetic"\nversion = "0.0.0"\n', encoding="utf-8", newline="\n"
            )
            (root / "src").mkdir()
            (root / "src/lib.rs").write_text("", encoding="utf-8", newline="\n")
            subprocess.run(["cargo", "generate-lockfile", "--offline"], cwd=root, check=True, capture_output=True)
            # At its real path, so the copy reads the synthetic root as its repository.
            script = root / "tests/corpus_match/corpus_offline_test.py"
            script.parent.mkdir(parents=True)
            shutil.copy2(REPO / "tests/corpus_match/corpus_offline_test.py", script)
            completed = subprocess.run(
                [sys.executable, str(script), "OfflineCorpusRecipes.test_real_recipes_without_network_or_cache"],
                cwd=root,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            self.assertEqual(1, completed.returncode, completed.stdout + completed.stderr)
            self.assertIn("mkdir -p .local/corpus/generated", completed.stderr)
            self.assertNotIn("Directory not empty", completed.stderr)
            self.assertEqual("original cached bytes", marker.read_text(encoding="utf-8"))
            self.assertFalse((cache / "generated").exists())


if __name__ == "__main__":
    unittest.main()

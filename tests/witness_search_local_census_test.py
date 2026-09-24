#!/usr/bin/env python3
"""End-to-end coverage of complete local-tree selector evidence."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts/witness-search-local-census.py"


class LocalCensusTest(unittest.TestCase):
    def test_real_tree_reports_zeroes_and_declarations_per_document(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            documents = root / "documents"
            documents.mkdir()
            contract = root / "keys.md"
            contract.write_text(
                "| key | selector |\n|---|---|\n"
                "| `array` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf` |\n",
                encoding="utf-8",
            )
            hit = json.dumps({
                "openapi": "3.0.0", "info": {"title": "hit", "version": "1"},
                "paths": {}, "components": {"schemas": {"Shape": {"oneOf": [
                    {"type": "array", "items": {"anyOf": [{"type": "string"}]}}
                ]}}},
            }).encode()
            miss = json.dumps({
                "openapi": "3.0.0", "info": {"title": "miss", "version": "1"},
                "paths": {}, "components": {"schemas": {"Shape": {"type": "string"}}},
            }).encode()
            (documents / "hit.json").write_bytes(hit)
            (documents / "miss.json").write_bytes(miss)
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--contract", str(contract),
                 "--documents", f"local={documents}", "--all-documents"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = list(csv.DictReader(io.StringIO(completed.stdout), dialect="excel-tab"))
            self.assertEqual(len(rows), 2)
            by_name = {row["document"]: row for row in rows}
            self.assertEqual(by_name["hit.json"]["count"], "1")
            self.assertEqual(by_name["miss.json"]["count"], "0")
            self.assertEqual(by_name["hit.json"]["sha256"], hashlib.sha256(hit).hexdigest())
            self.assertEqual(by_name["miss.json"]["sha256"], hashlib.sha256(miss).hexdigest())


if __name__ == "__main__":
    unittest.main()

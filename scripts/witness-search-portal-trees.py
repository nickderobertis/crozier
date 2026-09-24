#!/usr/bin/env python3
"""Extract and inventory JSON/YAML files from pinned vendor portal archives."""

from __future__ import annotations

import argparse
import csv
import hashlib
import tarfile
from pathlib import Path


def extract(plan: Path, archives: Path, tree: Path, manifest: Path) -> None:
    with plan.open(encoding="utf-8", newline="") as handle:
        sources = list(csv.DictReader(handle, dialect="excel-tab"))
    rows = []
    for source in sources:
        repository, revision = source["repository"], source["pinned_ref"]
        if len(revision) != 40:
            continue
        archive = archives / f"{repository.replace('/', '--')}.tar.gz"
        if not archive.is_file():
            raise FileNotFoundError(f"missing pinned archive {archive}")
        with tarfile.open(archive, "r:gz") as handle:
            for member in handle:
                if not member.isfile() or Path(member.name).suffix.lower() not in {".json", ".yaml", ".yml"}:
                    continue
                parts = Path(member.name).parts
                if len(parts) < 2 or ".." in parts[1:]:
                    raise ValueError(f"unsafe archive path {member.name}")
                relative = Path(*parts[1:])
                stream = handle.extractfile(member)
                if stream is None:
                    raise ValueError(f"cannot read archive member {member.name}")
                body = stream.read()
                output = tree / repository.replace("/", "--") / relative
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(body)
                rows.append((repository, revision, relative.as_posix(),
                             hashlib.sha256(body).hexdigest(), str(len(body))))
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", encoding="utf-8", newline="") as output:
        writer = csv.writer(output, dialect="excel-tab", lineterminator="\n")
        writer.writerow(("repository", "revision", "path", "sha256", "bytes"))
        writer.writerows(sorted(rows))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--archives", type=Path, required=True)
    parser.add_argument("--tree", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    extract(args.plan, args.archives, args.tree, args.manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Extract and inventory JSON/YAML files from pinned vendor portal archives."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import tarfile
from pathlib import Path, PurePosixPath

REPOSITORY = re.compile(r"[A-Za-z0-9-]+/[A-Za-z0-9._-]+")
COMMIT = re.compile(r"[0-9a-f]{40}")


def pinned(source: dict[str, str]) -> bool:
    """Whether a plan row is pinned; a pinned row must name owner/name at a full commit.

    A row whose `pinned_ref` is not commit-length records why no immutable ref
    exists, and is not extracted."""
    repository, revision = source["repository"], source["pinned_ref"]
    if repository is None or revision is None:
        raise ValueError(f"plan row {source!r} lacks a repository or pinned_ref cell")
    if len(revision) != 40:
        return False
    if not COMMIT.fullmatch(revision):
        raise ValueError(f"{repository}: pinned_ref {revision!r} is not a full lowercase hexadecimal commit SHA")
    if not REPOSITORY.fullmatch(repository) or repository.split("/")[1] in {".", ".."}:
        raise ValueError(f"pinned repository {repository!r} is not a GitHub owner/name")
    return True


def member_path(name: str) -> PurePosixPath:
    """The archive member's path below its top-level directory, refused if it could escape it.

    Tar names are POSIX paths on every host; an absolute name, a `..`
    component, a backslash or a drive-like `:` would leave the extraction root
    on some platform of the release matrix."""
    posix = PurePosixPath(name)
    parts = posix.parts
    if ("\\" in name or posix.is_absolute() or len(parts) < 2
            or any(part == ".." or ":" in part for part in parts)):
        raise ValueError(f"unsafe archive path {name}")
    return PurePosixPath(*parts[1:])


def extract(plan: Path, archives: Path, tree: Path, manifest: Path) -> None:
    with plan.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, dialect="excel-tab")
        if not {"repository", "pinned_ref"} <= set(reader.fieldnames or ()):
            raise ValueError(f"{plan}: expected repository and pinned_ref columns")
        sources = list(reader)
    rows = []
    for source in sources:
        if not pinned(source):
            continue
        repository, revision = source["repository"], source["pinned_ref"]
        archive = archives / f"{repository.replace('/', '--')}.tar.gz"
        if not archive.is_file():
            raise FileNotFoundError(f"missing pinned archive {archive}")
        with tarfile.open(archive, "r:gz") as handle:
            for member in handle:
                if not member.isfile() or PurePosixPath(member.name).suffix.lower() not in {".json", ".yaml", ".yml"}:
                    continue
                relative = member_path(member.name)
                stream = handle.extractfile(member)
                if stream is None:
                    raise ValueError(f"cannot read archive member {member.name}")
                body = stream.read()
                output = tree / repository.replace("/", "--") / Path(*relative.parts)
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
    try:
        extract(args.plan, args.archives, args.tree, args.manifest)
    except (OSError, ValueError, tarfile.TarError) as error:
        print(f"witness-search-portal-trees: {error}; check the plan and pinned archives before retrying", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

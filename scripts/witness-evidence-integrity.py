#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo crate driven by `just`, with no Nx workspace (no nx.json or project.json anywhere); this checker sits in scripts/ beside witness-search-github.py, whose committed evidence it verifies, and tests/witness_search_github_test.py drives it.
"""Verify that the retained historical evidence preserves its records and joins.

The baseline records anonymous group memberships by ledger position, never by
input locator or content digest. Later appended evidence is outside this pinned
historical prefix; changes within it must preserve the measured profile.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import json
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
BASELINE = REPO / "docs/openapi-surface/opaque-history-profile.json"
PROFILE_VERSION = 1
Location = tuple[str | int, ...]


def fingerprint(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def profile(
    files: dict[str, int],
    include: Callable[[dict[str, Any], Location], bool],
    root: Path = REPO,
) -> dict[str, Any]:
    counts = {}
    nodes = []
    subjects = []

    def visit(value: Any, location: Location, context: dict[str, Any]) -> None:
        if isinstance(value, list):
            for i, item in enumerate(value):
                visit(item, (*location, i), context)
        elif isinstance(value, dict):
            context = {
                **context,
                **{k: value[k] for k in ("key", "source") if k in value},
            }
            if isinstance(value.get("candidate"), str):
                subjects.append((location, value, context))
            if (
                isinstance(value.get("path"), str)
                and isinstance(value.get("repository"), (str, dict))
                and include(value, location)
            ):
                IDENTITY.validate_opaque_values(value)
                name = IDENTITY.candidate_name(value)
                nodes.append(
                    (location, value, context, name, IDENTITY.candidate_revision(value))
                )
            for key, item in value.items():
                visit(item, (*location, key), context)

    for file in files:
        relative = Path(file)
        if (
            relative.is_absolute()
            or ".." in relative.parts
            or not file.startswith("docs/openapi-surface/")
        ):
            raise ValueError(
                f"invalid historical ledger path {file!r}; restore the baseline from git"
            )
        lines = (root / relative).read_text(encoding="utf-8").splitlines()
        if len(lines) < files[file]:
            raise ValueError(
                f"{file}: historical prefix needs {files[file]} records, found {len(lines)}; restore the ledger from git"
            )
        lines = lines[: files[file]]
        counts[file] = len(lines)
        for line, text in enumerate(lines, 1):
            visit(json.loads(text), (file, line), {})
    groups = collections.defaultdict(list)
    blobs = collections.defaultdict(list)
    digests = collections.defaultdict(list)
    verdicts = collections.defaultdict(list)
    locators = {
        kind: collections.defaultdict(list)
        for kind in ("path", "revision", "blob", "digest")
    }
    screens = {}
    candidates = []
    for location, value, context, name, revision in nodes:
        locators["path"][name].append((*location, "path"))
        locators["revision"][revision].append((*location, "revision"))
        for field in ("blob", "sha"):
            if value.get(field):
                locators["blob"][value[field]].append((*location, field))
        if value.get("sha256"):
            locators["digest"][value["sha256"]].append((*location, "sha256"))
        file = location[0]
        directory = str(Path(file).parent)
        key = context.get("key", "")
        groups[(directory, key, name, revision)].append(location)
        blob = value.get("blob") or value.get("sha")
        if blob:
            blobs[(directory, key, name, blob)].append(location)
        if value.get("sha256"):
            digests[(directory, name, value["sha256"])].append(location)
        verdicts[file].append(
            {
                k: value[k]
                for k in (
                    "key",
                    "selector_count",
                    "selector_counts",
                    "disposition",
                    "status",
                    "license",
                    "ref",
                    "fern",
                )
                if k in value
            }
        )
        if "fern" in value:
            for screen_key in value.get("keys") or [key]:
                screens[(directory, screen_key, name, value.get("sha256", ""))] = (
                    location
                )
        elif Path(file).name.startswith("candidates") and value.get(
            "selector_count", 0
        ):
            candidates.append(
                (location, (directory, key, name, value.get("sha256", "")))
            )
    edges = sorted(
        (location, screens[key]) for location, key in candidates if key in screens
    )
    superseded = []
    for location, value, context, name, revision in nodes:
        if value.get("supersedes"):
            group = (
                str(Path(location[0]).parent),
                context.get("key", ""),
                name,
                value["supersedes"],
            )
            superseded.extend((location, prior) for prior in groups.get(group, ()))

    names = {name for _, _, _, name, _ in nodes}
    subject_edges = []
    subject_verdicts = []
    for location, value, context in subjects:
        name, separator, revision = value["candidate"].rpartition("@")
        name = IDENTITY.normalize_repo(name)
        if not separator or name not in names:
            continue
        group = (str(Path(location[0]).parent), context.get("key", ""), name, revision)
        subject_edges.extend((location, target) for target in groups.get(group, ()))
        subject_verdicts.append(
            (location, {key: item for key, item in value.items() if key != "candidate"})
        )

    def memberships(groups: dict[Any, list[Location]]) -> dict[str, Any]:
        members = sorted(sorted(group, key=str) for group in groups.values())
        return {
            "groups": len(members),
            "sizes": {
                str(size): count
                for size, count in sorted(
                    collections.Counter(len(group) for group in members).items()
                )
            },
            "memberships": fingerprint(members),
        }

    return {
        "version": PROFILE_VERSION,
        "record_counts": counts,
        "node_counts": dict(
            sorted(collections.Counter(n[0][0] for n in nodes).items())
        ),
        "revision_groups": memberships(groups),
        "locator_groups": {
            kind: memberships(values) for kind, values in locators.items()
        },
        "blob_groups": memberships(blobs),
        "digest_groups": memberships(digests),
        "screen_joins": {"pairs": len(edges), "memberships": fingerprint(edges)},
        "supersedes_joins": {
            "pairs": len(superseded),
            "memberships": fingerprint(sorted(superseded)),
        },
        "subject_joins": {
            "pairs": len(subject_edges),
            "memberships": fingerprint(sorted(subject_edges)),
        },
        "subject_verdicts": {
            "count": len(subject_verdicts),
            "multiset": fingerprint(sorted(subject_verdicts, key=str)),
        },
        "verdicts": {
            file: {
                "count": len(rows),
                "multiset": fingerprint(
                    sorted(rows, key=lambda r: json.dumps(r, sort_keys=True))
                ),
            }
            for file, rows in sorted(verdicts.items())
        },
    }


def opaque_path(row: dict[str, Any], _location: Location) -> bool:
    return row["path"].startswith(IDENTITY.OPAQUE_PREFIX.split(":", 1)[0] + ":")


spec = importlib.util.spec_from_file_location(
    "witness_integrity_index", REPO / "scripts/witness-search-github-index.py"
)
if spec is None or spec.loader is None:
    raise SystemExit(
        "witness-evidence-integrity: cannot load the identity contract; restore it from git"
    )
IDENTITY = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = IDENTITY
spec.loader.exec_module(IDENTITY)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args(argv)
    try:
        expected = json.loads(args.baseline.read_text(encoding="utf-8"))
        if not isinstance(expected, dict):
            raise ValueError(
                "profile must be a JSON object; restore the baseline from git"
            )
        if (
            type(expected.get("version")) is not int
            or expected["version"] != PROFILE_VERSION
        ):
            raise ValueError(
                f"unsupported profile version {expected.get('version')}; restore version {PROFILE_VERSION} evidence from git"
            )
        files = expected.get("record_counts")
        if (
            not isinstance(files, dict)
            or not files
            or any(
                not isinstance(name, str) or type(count) is not int or count < 1
                for name, count in files.items()
            )
        ):
            raise ValueError(
                "record_counts must map ledger paths to positive integers; restore the baseline from git"
            )
        measured = profile(files, opaque_path, args.root)
        changed = sorted(
            key
            for key in set(expected) | set(measured)
            if expected.get(key) != measured.get(key)
        )
        if changed:
            raise ValueError(
                f"historical evidence changed in {', '.join(changed)}; restore the retained records and joins"
            )
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(
            f"witness-evidence-integrity: {error}; repair the baseline or ledger and rerun",
            file=sys.stderr,
        )
        return 1
    print("witness-evidence-integrity: historical records and joins preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

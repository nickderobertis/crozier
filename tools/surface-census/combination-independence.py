#!/usr/bin/env python3
"""Read source-checked three-document proofs of independent combination handling."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import tomllib
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from types import ModuleType

MANIFEST = Path("docs/openapi-surface/combination-independence.toml")


class Feature(StrEnum):
    FIRST = "first"
    SECOND = "second"


class Mode(StrEnum):
    PYTHON_ENUMS = "python_enums"
    LITERALS = "literals"


class Case(StrEnum):
    FIRST = "first"
    SECOND = "second"
    BOTH = "both"


@dataclass(frozen=True)
class Condition:
    feature: Feature
    handler: str
    condition: str


@dataclass(frozen=True)
class Document:
    document: Path
    trees: dict[Mode, Path]


@dataclass(frozen=True)
class IndependenceProof:
    key: str
    modes: tuple[Mode, ...]
    conditions: tuple[Condition, ...]
    documents: dict[Case, Document]


def reach_reader() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "independence_reach_reader", Path(__file__).with_name("golden-reach.py")
    )
    if spec is None or spec.loader is None:
        raise ValueError("cannot load golden-reach.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def relative_path(value: object) -> Path:
    if (
        not isinstance(value, str)
        or value.startswith("/")
        or ":" in value
        or "\\" in value
        or any(part in {"", ".", ".."} for part in value.split("/"))
    ):
        raise ValueError(f"expected a repository-relative path, got {value!r}")
    return Path(value)


def read_records(root: Path) -> tuple[dict[str, IndependenceProof], list[str]]:
    """Validate manifest v1 before any source or subprocess is used as evidence."""
    records: dict[str, IndependenceProof] = {}
    failures = []
    reach = reach_reader()
    try:
        raw = tomllib.loads((root / MANIFEST).read_text(encoding="utf-8"))
        if (
            set(raw) != {"schema_version", "combinations"}
            or type(raw["schema_version"]) is not int
            or raw["schema_version"] != 1
        ):
            raise ValueError("expected schema_version = 1 and combinations")
        if not isinstance(raw["combinations"], list):
            raise ValueError("combinations must be an array")
        for index, row in enumerate(raw["combinations"], start=1):
            try:
                if not isinstance(row, dict) or set(row) != {"key", "modes", "conditions", "documents"}:
                    raise ValueError("each combination needs key, modes, conditions and documents")
                key = row["key"]
                if not isinstance(key, str) or not re.fullmatch(r"combo-[a-z0-9-]+", key) or key in records:
                    raise ValueError("key must be a unique combo-* key")
                if (
                    not isinstance(row["modes"], list)
                    or not isinstance(row["conditions"], list)
                    or not isinstance(row["documents"], dict)
                ):
                    raise ValueError("modes and conditions must be arrays; documents must be a table")
                modes = tuple(Mode(mode) for mode in row["modes"])
                if not modes or modes[0] != Mode.PYTHON_ENUMS or len(modes) != len(set(modes)):
                    raise ValueError("modes must start with python_enums, without duplicates")
                conditions = []
                for condition in row["conditions"]:
                    if not isinstance(condition, dict) or set(condition) != {"feature", "handler", "condition"}:
                        raise ValueError("each condition needs feature, handler and condition")
                    if not isinstance(condition["handler"], str) or not reach.HANDLER_SPEC.fullmatch(
                        condition["handler"]
                    ):
                        raise ValueError("condition handler must be path::function")
                    if not isinstance(condition["condition"], str) or not condition["condition"].strip():
                        raise ValueError("condition must quote non-empty Rust source")
                    conditions.append(
                        Condition(Feature(condition["feature"]), condition["handler"], condition["condition"])
                    )
                if {condition.feature for condition in conditions} != set(Feature):
                    raise ValueError("conditions must name both first and second features")
                if set(row["documents"]) != set(Case):
                    raise ValueError("documents must name first, second and both")
                documents = {}
                for label, document in row["documents"].items():
                    if not isinstance(document, dict) or set(document) != {"document", *modes}:
                        raise ValueError(f"{label} needs document and one complete certified tree per mode")
                    documents[Case(label)] = Document(
                        relative_path(document["document"]), {mode: relative_path(document[mode]) for mode in modes}
                    )
                records[key] = IndependenceProof(key, modes, tuple(conditions), documents)
            except (KeyError, TypeError, ValueError) as error:
                failures.append(f"{MANIFEST} combination {index}: {error}")
    except (OSError, UnicodeError, tomllib.TOMLDecodeError, ValueError) as error:
        failures.append(f"{MANIFEST}: {error}")
    return records, failures


def source_failures(root: Path, proof: IndependenceProof, handlers: list[str]) -> list[str]:
    """Hold every named handling function and its verbatim governing conditions."""
    reach = reach_reader()
    failures = []
    if {condition.handler for condition in proof.conditions} != set(handlers):
        failures.append(f"{proof.key}: independence conditions must cover exactly the audit's handling functions")
    for condition in proof.conditions:
        try:
            site = reach.resolve_site(condition.handler, root)
            lines = (root / site.file).read_text(encoding="utf-8").splitlines(keepends=True)
            if condition.condition not in "".join(lines[site.start - 1 : site.end]):
                failures.append(f"{proof.key}: `{condition.handler}` no longer contains `{condition.condition}`")
        except (OSError, UnicodeError, SystemExit) as error:
            failures.append(f"{proof.key}: condition handler `{condition.handler}` does not resolve: {error}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument(
        "--json", action="store_true", required=True, help="print validated records for the CLI e2e gate"
    )
    args = parser.parse_args()
    records, failures = read_records(args.repo_root)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(
        json.dumps(
            [
                {
                    "key": proof.key,
                    "modes": proof.modes,
                    "documents": {
                        label: {
                            "document": document.document.as_posix(),
                            **{mode: path.as_posix() for mode, path in document.trees.items()},
                        }
                        for label, document in proof.documents.items()
                    },
                }
                for proof in records.values()
            ]
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

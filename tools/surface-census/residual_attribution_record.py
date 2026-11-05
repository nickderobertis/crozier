"""Versioned, content-addressed measurements used by the offline reach restatement."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import NamedTuple, TypeAlias

import port_pins

RECORD = Path("docs/openapi-surface/residual-attribution.json")
VERSION = 1
REMEASURE = "just residual-attribution"
CONFIG_NAMES = ("crozier.yml", "crozier.yaml", ".crozier.yml", ".crozier.yaml")


FeatureKey: TypeAlias = str
FixtureName: TypeAlias = str
ContentDigest: TypeAlias = str
ArtifactPath: TypeAlias = str


class Fingerprints(NamedTuple):
    golden_digest: ContentDigest
    inputs_digest: ContentDigest


@dataclass(frozen=True)
class Attribution:
    key: FeatureKey
    fixture: FixtureName
    byte_matched: list[ArtifactPath]
    unmatched: list[ArtifactPath]
    golden_digest: ContentDigest
    inputs_digest: ContentDigest

    def cell(self) -> str:
        matched = ", ".join(f"`{name}`" for name in self.byte_matched) or "none"
        gaps = "; open gap: " + ", ".join(f"`{name}`" for name in self.unmatched) if self.unmatched else ""
        verdict = (
            "split" if self.byte_matched and self.unmatched else "byte-matched" if self.byte_matched else "open gap"
        )
        return f"| `{self.key}` | `{self.fixture}` | {matched}{gaps} | `{verdict}` |\n"


def content_digest(root: Path, paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths, key=lambda path: path.relative_to(root).as_posix()):
        for value in (path.relative_to(root).as_posix().encode(), path.read_bytes()):
            digest.update(len(value).to_bytes(8, "big"))
            digest.update(value)
    return digest.hexdigest()


def fingerprints(root: Path, fixture: FixtureName) -> Fingerprints:
    golden = root / "tests/fixtures" / fixture / "expected"
    sources = root / "tests/fixtures/corpus-sources" / fixture
    if not golden.is_dir() or not sources.is_dir():
        raise ValueError(f"{fixture}: missing golden output or source; re-measure with `{REMEASURE}`")
    outputs = [path for path in golden.rglob("*") if path.is_file()]
    inputs = [
        path for folder in ("src", "templates", "assets") for path in (root / folder).rglob("*") if path.is_file()
    ]
    inputs += [
        root / path
        for path in (
            "Cargo.toml",
            "Cargo.lock",
            "rust-toolchain.toml",
            ".ruff-version",
            ".cargo/config.toml",
            "build.rs",
            "pyproject.toml",
            "ruff.toml",
            ".ruff.toml",
            *CONFIG_NAMES,
            "tools/surface-census/residual-attribution.py",
            "tools/surface-census/openapi-surface-census.py",
            "tools/surface-census/residual_attribution_record.py",
            "tools/surface-census/port_pins.py",
        )
        if (root / path).is_file()
    ]
    inputs += [path for path in sources.rglob("*") if path.is_file()]
    registry = root / "crates/crozier-e2e/tests/e2e.rs"
    census = port_pins.census(Path(__file__).resolve().parents[2])
    registrations = census.golden_registrations(registry)
    if fixture not in registrations:
        raise ValueError(f"{fixture}: no golden registration; re-measure with `{REMEASURE}`")
    classified_inputs = json.dumps([content_digest(root, inputs), registrations[fixture].unmatched]).encode()
    return Fingerprints(content_digest(root, outputs), hashlib.sha256(classified_inputs).hexdigest())


def read(root: Path) -> dict[str, Attribution]:
    path = root / RECORD
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ValueError(f"{RECORD}: cannot read attribution ({error}); re-measure with `{REMEASURE}`") from error
    if (
        not isinstance(payload, dict)
        or set(payload) != {"version", "rows"}
        or type(payload.get("version")) is not int
        or payload.get("version") != VERSION
        or not isinstance(payload.get("rows"), list)
    ):
        raise ValueError(f"{RECORD}: unsupported record; re-measure with `{REMEASURE}`")
    rows: dict[str, Attribution] = {}
    for raw in payload["rows"]:
        if not isinstance(raw, dict) or set(raw) != set(Attribution.__dataclass_fields__):
            raise ValueError(f"{RECORD}: malformed attribution; re-measure with `{REMEASURE}`")
        if any(
            not isinstance(raw[name], str) or not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_.-]*", raw[name])
            for name in ("key", "fixture")
        ):
            raise ValueError(f"{RECORD}: invalid key or fixture; re-measure with `{REMEASURE}`")
        if any(
            not isinstance(raw[name], str) or not re.fullmatch(r"[0-9a-f]{64}", raw[name])
            for name in ("golden_digest", "inputs_digest")
        ):
            raise ValueError(f"{raw['key']}: invalid attribution digest; re-measure with `{REMEASURE}`")
        for name in ("byte_matched", "unmatched"):
            if not isinstance(raw[name], list) or any(
                not isinstance(item, str)
                or not re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*", item)
                or any(part in {".", ".."} for part in item.split("/"))
                for item in raw[name]
            ):
                raise ValueError(f"{raw['key']}: invalid attribution files; re-measure with `{REMEASURE}`")
            if len(raw[name]) != len(set(raw[name])):
                raise ValueError(f"{raw['key']}: duplicate attribution files; re-measure with `{REMEASURE}`")
        if set(raw["byte_matched"]) & set(raw["unmatched"]):
            raise ValueError(f"{raw['key']}: contradictory attribution files; re-measure with `{REMEASURE}`")
        row = Attribution(**raw)
        if row.key in rows:
            raise ValueError(f"{row.key}: duplicate attribution; re-measure with `{REMEASURE}`")
        rows[row.key] = row
    return rows


def write(root: Path, rows: dict[str, Attribution]) -> None:
    (root / RECORD).write_text(
        json.dumps({"version": VERSION, "rows": [asdict(rows[key]) for key in sorted(rows)]}, indent=2) + "\n",
        encoding="utf-8",
    )


def require(root: Path, key: str, fixture: str, rows: dict[str, Attribution]) -> Attribution:
    row = rows.get(key)
    if row is None:
        raise ValueError(f"{key}: no residual attribution for {fixture}; re-measure with `{REMEASURE}`")
    try:
        current = fingerprints(root, fixture)
    except (ValueError, OSError) as error:
        raise ValueError(
            f"{key}: cannot validate residual attribution for {fixture}: {error}; re-measure with `{REMEASURE}`"
        ) from error
    if row.fixture != fixture or (row.golden_digest, row.inputs_digest) != current:
        raise ValueError(
            f"{key}: stale residual attribution for {fixture} (golden output or generator inputs changed); re-measure with `{REMEASURE}`"
        )
    return row

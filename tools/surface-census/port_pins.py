"""Token-based drift checks for the census's explicit Rust port readings."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import io
import sys
from collections.abc import Sequence
from functools import lru_cache
from pathlib import Path
from typing import Any, NamedTuple, TypeAlias

import reach_store

PortName: TypeAlias = str
PythonPort: TypeAlias = str
RustFunction: TypeAlias = str
TokenDigest: TypeAlias = str


class PortPin(NamedTuple):
    name: PortName
    port: PythonPort
    rust: RustFunction
    confirm: str
    digest: TokenDigest

    def report(self) -> str:
        return (
            f"{self.port} mirrors {self.rust}: confirm {self.confirm}; "
            f"after re-reading, run `just census-repin --confirm-port {self.name}`"
        )


def census(root: Path) -> Any:
    path = root / "tools/surface-census/openapi-surface-census.py"
    spec = importlib.util.spec_from_file_location("port_pin_census", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=8)
def _parsed(path: str, source: bytes) -> reach_store.ParsedFile:
    return reach_store.parse(path, source)


def digest(root: Path, pin: PortPin) -> str:
    path, name = pin.rust.split("::", 1)
    parsed = _parsed(path, (root / path).read_bytes())
    units = [unit for unit in parsed.units if unit.key == name or unit.key.endswith("::" + name)]
    if len(units) != 1:
        raise ValueError(f"{pin.report()}: expected one Rust function, found {len(units)}")
    unit = units[0]
    # Length framing preserves token boundaries without making layout significant.
    stream = b"".join(
        len(raw).to_bytes(4, "big") + raw
        for token in parsed.tokens[unit.first : unit.last + 1]
        for raw in [token.text.encode("latin-1")]
    )
    return hashlib.sha256(stream).hexdigest()[:16]


def check_and_confirm(root: Path, confirmed: Sequence[str] = ()) -> list[str]:
    pins = census(root).PORT_PINS
    names = {pin.name for pin in pins}
    unknown = set(confirmed) - names
    if unknown:
        raise ValueError(f"unknown port(s) {', '.join(sorted(unknown))}; choose from {', '.join(sorted(names))}")
    actual: dict[str, str] = {}
    errors = []
    for pin in pins:
        try:
            actual[pin.name] = digest(root, pin)
        except (ValueError, OSError) as error:
            errors.append(f"{pin.report()}: {error}")
    if errors:
        return errors
    path = root / "tools/surface-census/openapi-surface-census.py"
    source = path.read_bytes()
    for pin in pins:
        if pin.name in confirmed:
            # The record's digest is the only rewritten field. Records may be formatted across lines.
            tree = ast.parse(source)
            calls = [
                node
                for node in ast.walk(tree)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "PortPin"
            ]
            call = next(node for node in calls if ast.literal_eval(node.args[0]) == pin.name)
            field = call.args[4]
            lines = source.splitlines(keepends=True)
            start = sum(len(line) for line in lines[: field.lineno - 1]) + field.col_offset
            assert field.end_lineno is not None and field.end_col_offset is not None
            end = sum(len(line) for line in lines[: field.end_lineno - 1]) + field.end_col_offset
            source = (
                source[:start]
                + source[start : start + 1]
                + actual[pin.name].encode()
                + source[start : start + 1]
                + source[end:]
            )
    if confirmed:
        path.write_bytes(source)
    return [pin.report() for pin in pins if pin.name not in confirmed and actual[pin.name] != pin.digest]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    try:
        failures = check_and_confirm(args.repo_root)
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        return 1
    for failure in failures:
        print(failure, file=sys.stderr)
    return int(bool(failures))


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())

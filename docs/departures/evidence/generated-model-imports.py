# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as escaped-field-alias-literal.py does; crozier-e2e runs it and reads this folder through its e2eReads input.
"""Import a generated SDK's type and validate a payload through it.

Usage: generated-model-imports.py ROOT MODULE:NAME PAYLOAD_JSON valid|invalid

ROOT is a generated tree's `src/` directory. The import and the validation run
in a child interpreter under a time limit, because an implicit recursive alias
can make pydantic v1 expand it without end rather than raise. Prints one JSON
line: `{"pydantic": version, "constructed": repr}` when the payload validates,
or `{"pydantic": version, "failed": reason}` when the import or the validation
raises (or `{"failed": "no result within …"}` past the limit). Exits 0 when the
outcome is the one expected, 1 when it is not, and 2 on a usage error, a ROOT
holding no generated package, or a child interpreter that ends without
reporting an outcome (a crash, not an SDK failure).
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

LIMIT_SECONDS = 30
TARGET = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*:[A-Za-z_][A-Za-z0-9_]*")

CHILD = """
import json, sys
import pydantic
module, name = sys.argv[1].split(":")
payload = json.loads(sys.argv[2])
try:
    target = getattr(__import__(module, fromlist=[name]), name)
    from fern.core.pydantic_utilities import parse_obj_as
    value = parse_obj_as(target, payload)
except Exception as error:
    print(json.dumps({"pydantic": pydantic.VERSION, "failed": type(error).__name__}))
else:
    print(json.dumps({"pydantic": pydantic.VERSION, "constructed": repr(value)}))
"""


@dataclass(frozen=True)
class Constructed:
    """The payload validated through the type: its repr."""

    pydantic: str
    constructed: str


@dataclass(frozen=True)
class Failed:
    """The import or the validation raised, or never finished."""

    pydantic: str | None
    failed: str


class UsageError(Exception):
    """An argument this script cannot run with; exits 2."""


def parse_outcome(stdout: str) -> Constructed | Failed:
    """The child's one JSON outcome line, held to its two shapes."""
    lines = stdout.strip().splitlines()
    if not lines:
        raise UsageError("the child interpreter reported no outcome")
    try:
        reported = json.loads(lines[-1])
    except json.JSONDecodeError as error:
        raise UsageError(f"the child interpreter reported no outcome: {lines[-1]}") from error
    match reported:
        case {"pydantic": str(version), "constructed": str(value), **rest} if not rest:
            return Constructed(pydantic=version, constructed=value)
        case {"pydantic": str(version), "failed": str(reason), **rest} if not rest:
            return Failed(pydantic=version, failed=reason)
        case _:
            raise UsageError(f"the child interpreter reported no outcome: {lines[-1]}")


def screen(root: Path, target: str, payload: str) -> Constructed | Failed:
    """Import `target` under `root` and validate `payload` in a child interpreter."""
    try:
        child = subprocess.run(
            [sys.executable, "-c", CHILD, target, payload],
            cwd=root,
            env={"PYTHONPATH": str(root), "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True,
            text=True,
            timeout=LIMIT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return Failed(pydantic=None, failed=f"no result within {LIMIT_SECONDS}s")
    if child.returncode != 0:
        tail = child.stderr.strip().splitlines()[-1:] or ["no output"]
        raise UsageError(f"the child interpreter exited {child.returncode}: {tail[0]}")
    return parse_outcome(child.stdout)


def main(argv: list[str]) -> int:
    try:
        if len(argv) != 4 or argv[3] not in ("valid", "invalid"):
            raise UsageError(__doc__.strip().splitlines()[2])
        root, target, payload, expected = Path(argv[0]), argv[1], argv[2], argv[3]
        if not TARGET.fullmatch(target):
            raise UsageError(f"{target!r} is no MODULE:NAME")
        try:
            json.loads(payload)
        except json.JSONDecodeError as error:
            raise UsageError(f"PAYLOAD_JSON is not JSON: {error}") from error
        if not (root / "fern" / "__init__.py").is_file():
            raise UsageError(f"{root} holds no generated `fern` package; pass a tree's src/ directory")
        outcome = screen(root, target, payload)
    except UsageError as error:
        print(f"generated-model-imports: {error}", file=sys.stderr)
        return 2
    print(json.dumps({key: value for key, value in asdict(outcome).items() if value is not None}))
    return 0 if isinstance(outcome, Constructed) == (expected == "valid") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

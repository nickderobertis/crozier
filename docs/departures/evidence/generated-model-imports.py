"""Import a generated SDK's type and validate a payload through it.

Usage: generated-model-imports.py ROOT MODULE:NAME PAYLOAD_JSON valid|invalid

ROOT is a generated tree's `src/` directory. The import and the validation run
in a child interpreter under a time limit, because an implicit recursive alias
can make pydantic v1 expand it without end rather than raise. Prints one JSON
line: `{"pydantic": version, "constructed": repr}` when the payload validates,
or `{"pydantic": version, "failed": reason}` when the import or the validation
raises or exceeds the limit. Exits 0 when the outcome is the one expected, 1
when it is not, and 2 on a usage error or a ROOT holding no generated package.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

LIMIT_SECONDS = 30

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


def main(argv: list[str]) -> int:
    if len(argv) != 4 or argv[3] not in ("valid", "invalid") or ":" not in argv[1]:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    root, target, payload, expected = Path(argv[0]), argv[1], argv[2], argv[3]
    if not (root / "fern" / "__init__.py").is_file():
        print(f"{root} holds no generated `fern` package; pass a tree's src/ directory", file=sys.stderr)
        return 2
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
        outcome = {"failed": f"no result within {LIMIT_SECONDS}s"}
    else:
        lines = child.stdout.strip().splitlines()
        outcome = json.loads(lines[-1]) if lines else {"failed": child.stderr.strip().splitlines()[-1:]}
    print(json.dumps(outcome))
    return 0 if ("constructed" in outcome) == (expected == "valid") else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

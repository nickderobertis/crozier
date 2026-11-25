"""Type-check every worked call a generated SDK documents against that SDK.

Usage: worked_examples_typecheck.py SDK_ROOT

SDK_ROOT is a generated packaged tree (its package under `src/`). Each client
method docstring's `Examples` block (sync and async) and each `reference.md`
usage block becomes its own module, and pyright checks them with `src/` on its
path, inferring the client's unannotated sub-client properties from their
bodies (mypy reads those as `Any` and checks nothing): an argument the method
does not take, a missing required one, or a value whose type its annotation
rejects is an error. Only the examples are reported, never the SDK's own
modules.

Exit 0 prints how many examples were checked; exit 1 prints pyright's report;
exit 2 reports a root holding no documented example.
"""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

EXAMPLES = "Examples\n        --------\n"
USAGE = re.compile(r"#### 🔌 Usage\n\n<dl>\n<dd>\n\n<dl>\n<dd>\n\n```python\n(.*?)```", re.S)


def docstring_examples(source: str) -> list[str]:
    """The example code of every function docstring in a client module, as Python
    evaluates the docstring, with its eight-space indent removed."""
    found = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node, clean=False) or ""
            if EXAMPLES in doc:
                body = doc.split(EXAMPLES, 1)[1]
                found.append("\n".join(line.removeprefix(" " * 8) for line in body.splitlines()) + "\n")
    return found


def examples(root: Path) -> list[str]:
    found = []
    for client in sorted((root / "src").rglob("client.py")):
        found.extend(docstring_examples(client.read_text(encoding="utf-8")))
    reference = root / "reference.md"
    if reference.is_file():
        found.extend(USAGE.findall(reference.read_text(encoding="utf-8")))
    return found


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    root = Path(argv[0]).resolve()
    snippets = examples(root) if (root / "src").is_dir() else []
    if not snippets:
        print(f"{root}: no documented worked example under src/ or in reference.md", file=sys.stderr)
        return 2
    with tempfile.TemporaryDirectory() as work:
        files = []
        for number, snippet in enumerate(snippets):
            path = Path(work) / f"example_{number}.py"
            path.write_text(snippet, encoding="utf-8")
            files.append(path.name)
        config = {"include": files, "extraPaths": [str(root / "src")], "typeCheckingMode": "basic"}
        (Path(work) / "pyrightconfig.json").write_text(json.dumps(config), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, "-m", "pyright", "--project", work, "--pythonpath", sys.executable],
            capture_output=True,
            text=True,
            check=False,
        )
    if result.returncode != 0:
        print(result.stdout + result.stderr)
        return 1
    print(f"{len(snippets)} worked examples type-check")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

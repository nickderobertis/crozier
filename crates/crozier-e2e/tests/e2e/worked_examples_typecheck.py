"""Type-check every worked call a generated SDK documents against that SDK.

Usage: worked_examples_typecheck.py SDK_ROOT

SDK_ROOT is a generated packaged tree (its package under `src/`). Each client
method docstring's `Examples` block (sync and async), each `reference.md` usage
block, and each `README.md` block that calls the client with its worked
arguments becomes its own module, named for where it came from
(`readme_0.py`), and pyright checks them with `src/` on its
path, inferring the client's unannotated sub-client properties from their
bodies (mypy reads those as `Any` and checks nothing): an argument the method
does not take, a missing required one, or a value whose type its annotation
rejects is an error. Only the examples are reported, never the SDK's own
modules.

Exit 0 prints how many examples were checked; exit 1 prints pyright's report on
stderr; exit 2 reports a root holding no documented example, also on stderr.
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
README_BLOCK = re.compile(r"^```python\n(.*?)^```$", re.S | re.M)


def readme_calls(text: str) -> list[str]:
    """The README blocks that construct the client and call it with worked
    arguments: the usage, async and environment sections. A fragment using a
    client constructed elsewhere (the exception and retry sections) or
    abbreviating its arguments as `...` (raw responses, timeouts, a custom
    client) documents no call to bind, and a streaming block's module-level
    `yield` is the certified pair's matched simplification, not a call either."""
    found = []
    for block in README_BLOCK.findall(text):
        try:
            tree = ast.parse(block)
        except SyntaxError:
            found.append(block)
            continue
        abbreviated = any(isinstance(node, ast.Constant) and node.value is Ellipsis for node in ast.walk(tree))
        streaming = any(isinstance(node, (ast.Yield, ast.YieldFrom)) for node in ast.walk(tree))
        constructs_client = any(
            isinstance(node, ast.Assign) and any(ast.unparse(target) == "client" for target in node.targets)
            for node in tree.body
        )
        calls_client = any(
            isinstance(node, ast.Call) and ast.unparse(node.func).startswith("client.") for node in ast.walk(tree)
        )
        if constructs_client and calls_client and not abbreviated and not streaming:
            found.append(block)
    return found


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


def reference_usages(text: str) -> list[str]:
    """Each `reference.md` usage block but a bare `client.<method>(...)`: an
    operation the pair works no example for (an `application/octet-stream`
    body's) is documented by that placeholder, its arguments abbreviated as the
    README's are, and so binds no call."""
    found = []
    for block in USAGE.findall(text):
        try:
            tree = ast.parse(block)
        except SyntaxError:
            found.append(block)
            continue
        placeholder = len(tree.body) == 1 and any(
            isinstance(node, ast.Constant) and node.value is Ellipsis for node in ast.walk(tree)
        )
        if not placeholder:
            found.append(block)
    return found


def examples(root: Path) -> list[tuple[str, str]]:
    """Each documented worked example as `(source, code)`, the source one of
    `docstring`, `reference` and `readme`."""
    found = []
    for client in sorted((root / "src").rglob("client.py")):
        found.extend(("docstring", code) for code in docstring_examples(client.read_text(encoding="utf-8")))
    reference = root / "reference.md"
    if reference.is_file():
        found.extend(("reference", code) for code in reference_usages(reference.read_text(encoding="utf-8")))
    readme = root / "README.md"
    if readme.is_file():
        found.extend(("readme", code) for code in readme_calls(readme.read_text(encoding="utf-8")))
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
        for number, (source, snippet) in enumerate(snippets):
            path = Path(work) / f"{source}_{number}.py"
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
        print(result.stdout + result.stderr, file=sys.stderr)
        return 1
    print(f"{len(snippets)} worked examples type-check")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

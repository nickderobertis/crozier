# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as body-query-parameter-value.py does; crozier-e2e reads this folder through its e2eReads input.
"""Evaluate a const argument's documented examples against the schema's const.

Imports the generated package, evaluates the value each client docstring
example and each README/reference.md example passes for one keyword exactly as
Python evaluates the example's source, binds each docstring call to the actual
generated method, and compares every value with the const the source document
declares for that property.

Exit 0 prints one JSON proof result; exit 1 means the proof or SDK import failed;
exit 2 reports invalid CLI arguments on stderr.
"""

from __future__ import annotations

import argparse
import ast
import enum
import importlib
import inspect
import json
import re
import sys
import textwrap
import typing
import warnings
from pathlib import Path
from types import ModuleType


class Expect(enum.Enum):
    """What the docstrings are expected to pass: Fern's certified fault, or its correction."""

    INVALID = "invalid"
    VALID = "valid"


def declared_const(document: Path, schema_name: str, keyword: str) -> str:
    spec = json.loads(document.read_text(encoding="utf-8"))
    const = spec["components"]["schemas"][schema_name]["properties"][keyword]["const"]
    assert isinstance(const, str)
    return const


def passed_arguments(code: str, method: str) -> dict[str, object]:
    """The keyword arguments the example passes, evaluated as Python would."""
    with warnings.catch_warnings():
        # Fern's `"\$…"` is an invalid escape sequence Python keeps verbatim.
        warnings.simplefilter("ignore", SyntaxWarning)
        tree = ast.parse(code)
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == method]
    assert len(calls) == 1, (method, len(calls))
    return {node.arg: ast.literal_eval(node.value) for node in calls[0].keywords if node.arg is not None}


def docstring_values(sdk: ModuleType, method: str, keyword: str) -> dict[str, object]:
    out = {}
    for name in ("FernApi", "AsyncFernApi"):
        function = getattr(getattr(sdk, name), method)
        doc = inspect.getdoc(function)
        assert doc is not None and "Examples\n--------\n" in doc, (name, method)
        arguments = passed_arguments(textwrap.dedent(doc.split("Examples\n--------\n", 1)[1]), method)
        inspect.signature(function).bind(None, **arguments)
        out[f"{name}.{method}"] = arguments[keyword]
    return out


def markdown_values(root: Path, method: str, keyword: str) -> dict[str, object]:
    out = {}
    for document in ("README.md", "reference.md"):
        text = (root / document).read_text(encoding="utf-8")
        for index, block in enumerate(re.findall(r"```python\n(.*?)```", text, flags=re.S)):
            if f".{method}(" in block and "..." not in block:
                out[f"{document}#{index}"] = passed_arguments(textwrap.dedent(block), method)[keyword]
    assert out, f"no Markdown example calls {method}"
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sdk_root", type=Path, help="the generated tree (holds README.md and src/)")
    parser.add_argument("document", type=Path, help="the OpenAPI document it was generated from, as JSON")
    parser.add_argument("--schema", required=True, help="the component schema declaring the const")
    parser.add_argument("--literal-type", required=True, help="the generated alias typing the property")
    parser.add_argument("--method", required=True)
    parser.add_argument("--keyword", required=True)
    parser.add_argument("--examples", type=Expect, choices=list(Expect), required=True)
    args = parser.parse_args()
    if not (args.sdk_root / "src" / "fern" / "__init__.py").is_file():
        parser.error("sdk_root must contain src/fern")
    const = declared_const(args.document, args.schema, args.keyword)
    sys.path.insert(0, str((args.sdk_root / "src").resolve()))
    sdk = importlib.import_module("fern")
    annotation = getattr(sdk, args.literal_type)
    literals = [value for member in typing.get_args(annotation) for value in typing.get_args(member)]
    assert literals == [const], (annotation, const)
    markdown = markdown_values(args.sdk_root, args.method, args.keyword)
    docstrings = docstring_values(sdk, args.method, args.keyword)
    assert all(value == const for value in markdown.values()), markdown
    if args.examples is Expect.INVALID:
        assert all(value != const for value in docstrings.values()), docstrings
    else:
        assert all(value == const for value in docstrings.values()), docstrings
    print(json.dumps({"const": const, "literal": literals, "docstrings": docstrings,
                      "markdown": markdown, "examples": args.examples.value}, sort_keys=True))


if __name__ == "__main__":
    main()

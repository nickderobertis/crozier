# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as body-query-parameter-value.py does; crozier-e2e reads this folder through its e2eReads input.
"""Validate every documented int64 example of a generated SDK against its schema.

Imports the generated package, evaluates the client docstring examples and the
README/reference.md examples of one operation, binds each docstring call to the
actual generated method, and checks every argument the source document declares
`format: int64` against the signed 64-bit bounds and the declared example.

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
from pathlib import Path
from types import ModuleType
from typing import Any

INT64 = (-(2**63), 2**63 - 1)


class Expect(enum.Enum):
    """What the examples are expected to be: Fern's certified fault, or its correction."""

    INVALID = "invalid"
    VALID = "valid"


def load_document(document: Path) -> Any:
    """The OpenAPI document, read as JSON or, failing a `.json` suffix, as YAML."""
    text = document.read_text(encoding="utf-8")
    if document.suffix == ".json":
        return json.loads(text)
    import yaml  # noqa: PLC0415 - only a YAML document needs the YAML reader

    return yaml.safe_load(text)


def int64_example(schema: dict[str, Any]) -> int | None:
    """A schema's declared example when the schema is an int64 integer."""
    example = schema.get("example")
    if schema.get("format") == "int64" and isinstance(example, int) and not isinstance(example, bool):
        return example
    return None


def declared_int64(document: Path, operation_id: str) -> dict[str, tuple[int, bool]]:
    """The operation's int64 examples by argument: its query parameters' and its
    body properties', each with whether the argument is a list of them (an array
    property whose items declare the example)."""
    spec = load_document(document)
    for item in spec["paths"].values():
        for operation in item.values():
            if not isinstance(operation, dict) or operation.get("operationId") != operation_id:
                continue
            declared: dict[str, tuple[int, bool]] = {}
            for parameter in operation.get("parameters", []):
                example = int64_example(parameter.get("schema", {}))
                if example is not None:
                    declared[parameter["name"]] = (example, False)
            schema = operation["requestBody"]["content"]["application/json"]["schema"]
            for name, prop in schema["properties"].items():
                example = int64_example(prop)
                if example is not None:
                    declared[name] = (example, False)
                elif prop.get("type") == "array" and (example := int64_example(prop.get("items", {}))) is not None:
                    declared[name] = (example, True)
            # A proof that checks no value proves nothing.
            assert declared, f"{operation_id} declares no int64 example to validate"
            return declared
    raise AssertionError(f"no operation {operation_id}")


def js_spelling(value: int) -> int:
    """The integer JavaScript's nearest double spells for `value` below 10^21."""
    shortest = repr(float(abs(value)))
    if "e" not in shortest:
        return int(float(value))
    digits, exponent = shortest.split("e")
    spelled = digits.replace(".", "").ljust(int(exponent) + 1, "0")
    return -int(spelled) if value < 0 else int(spelled)


def call_arguments(code: str, method: str) -> dict[str, Any]:
    tree = ast.parse(code)
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == method]
    assert len(calls) == 1, (method, len(calls))
    return {keyword.arg: ast.literal_eval(keyword.value) for keyword in calls[0].keywords
            if keyword.arg is not None}


def docstring_examples(sdk: ModuleType, method: str) -> dict[str, dict[str, Any]]:
    out = {}
    for name in ("FernApi", "AsyncFernApi"):
        function = getattr(getattr(sdk, name), method)
        doc = inspect.getdoc(function)
        assert doc is not None and "Examples\n--------\n" in doc, (name, method)
        code = textwrap.dedent(doc.split("Examples\n--------\n", 1)[1])
        arguments = call_arguments(code, method)
        inspect.signature(function).bind(None, **arguments)
        out[f"{name}.{method}"] = arguments
    return out


def markdown_examples(root: Path, method: str) -> dict[str, dict[str, Any]]:
    out = {}
    for document in ("README.md", "reference.md"):
        text = (root / document).read_text(encoding="utf-8")
        blocks = re.findall(r"```python\n(.*?)```", text, flags=re.S)
        for index, block in enumerate(blocks):
            if f".{method}(" in block and "..." not in block:
                out[f"{document}#{index}"] = call_arguments(textwrap.dedent(block), method)
    assert out, f"no Markdown example calls {method}"
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sdk_root", type=Path, help="the generated tree (holds README.md and src/)")
    parser.add_argument("document", type=Path, help="the OpenAPI document it was generated from")
    parser.add_argument("--operation-id", required=True)
    parser.add_argument("--method", required=True)
    parser.add_argument("--examples", type=Expect, choices=list(Expect), required=True)
    args = parser.parse_args()
    if not (args.sdk_root / "src" / "fern" / "__init__.py").is_file():
        parser.error("sdk_root must contain src/fern")
    declared = declared_int64(args.document, args.operation_id)
    sys.path.insert(0, str((args.sdk_root / "src").resolve()))
    sdk = importlib.import_module("fern")
    found = docstring_examples(sdk, args.method) | markdown_examples(args.sdk_root, args.method)
    verdicts: dict[str, dict[str, str]] = {}
    for where, arguments in found.items():
        verdicts[where] = {}
        for name, (example, listed) in declared.items():
            values = arguments[name] if listed else [arguments[name]]
            assert values, (where, name, "no element to validate")
            rounded = js_spelling(example)
            for value in values:
                in_range = INT64[0] <= value <= INT64[1]
                if INT64[0] <= rounded <= INT64[1]:
                    # A rounding that stays in range is a valid value, written by both.
                    assert value == rounded, (where, name, value, rounded)
                    verdicts[where][name] = "in range"
                elif args.examples is Expect.INVALID:
                    assert value == rounded and not in_range, (where, name, value)
                    verdicts[where][name] = f"{value} exceeds the int64 bounds {INT64}"
                else:
                    assert value == example and in_range, (where, name, value)
                    verdicts[where][name] = "the declared example, in range"
    print(json.dumps({"examples": args.examples.value, "verdicts": verdicts}, sort_keys=True))


if __name__ == "__main__":
    main()

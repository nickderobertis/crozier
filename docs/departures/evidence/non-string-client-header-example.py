# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as request-alias-reference-parameters.py does; crozier-e2e runs it and reads this folder through its e2eReads input.
"""Validate a docstring's client construction against the actual constructor.

Exit 0 prints one JSON proof result; exit 1 means the proof or SDK import failed;
exit 2 reports invalid CLI arguments on stderr.
"""

from __future__ import annotations

import argparse
import ast
import importlib
import inspect
import json
from pathlib import Path
import sys
import textwrap
import typing

import httpx
from pydantic import TypeAdapter, ValidationError

parser = argparse.ArgumentParser()
parser.add_argument("sdk", type=Path)
parser.add_argument("--expected", choices=("invalid", "valid"), required=True)
args = parser.parse_args()
if not (args.sdk / "fern" / "__init__.py").is_file():
    parser.error("sdk must contain the generated fern package")
sys.path.insert(0, str(args.sdk.resolve()))
sdk = importlib.import_module("fern")

# The measurement's three promoted headers: the two whose declared type is not
# a string, and the string one whose `YOUR_*` placeholder is correct.
TYPED = {"strict_mode": bool, "shift_number": int}
STRING = "tenant_code"


def construction(doc: str, class_name: str) -> dict[str, object]:
    """The keyword arguments the docstring example passes to `class_name`."""
    code = textwrap.dedent(doc.split("Examples\n--------\n", 1)[1])
    calls = [
        node
        for node in ast.walk(ast.parse(code))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == class_name
    ]
    assert len(calls) == 1, f"{len(calls)} constructions of {class_name}"
    return {keyword.arg or "": ast.literal_eval(keyword.value) for keyword in calls[0].keywords}


verdicts: dict[str, str] = {}
examples = {
    "FernApi": inspect.getdoc(sdk.FernApi),
    "AsyncFernApi": inspect.getdoc(sdk.AsyncFernApi),
    "BerthsClient.list_berths": inspect.getdoc(importlib.import_module("fern.berths.client").BerthsClient.list_berths),
}
for where, doc in examples.items():
    assert doc is not None, where
    class_name = "AsyncFernApi" if where.startswith("Async") else "FernApi"
    arguments = construction(doc, class_name)
    hints = typing.get_type_hints(getattr(sdk, class_name).__init__)
    assert arguments[STRING] == "YOUR_TENANT_CODE" and hints[STRING] is str, (where, arguments)
    for name, declared in TYPED.items():
        assert hints[name] is declared, (where, name, hints[name])
        value = arguments[name]
        try:
            TypeAdapter(declared).validate_python(value, strict=True)
        except ValidationError:
            assert args.expected == "invalid" and value == f"YOUR_{name.upper()}", (where, name, value)
            verdicts[f"{where} {name}"] = f"{value!r} rejected by the {declared.__name__} annotation"
        else:
            assert args.expected == "valid", (where, name, value)
            verdicts[f"{where} {name}"] = f"{value!r} has its declared type"

# The documented construction, sent: the headers each value puts on the wire.
sent: list[dict[str, str]] = []


def handle(request: httpx.Request) -> httpx.Response:
    sent.append({wire: request.headers[wire] for wire in ("X-Strict-Mode", "X-Tenant-Code", "X-Shift-Number")})
    return httpx.Response(200, json=[])


arguments = construction(examples["FernApi"] or "", "FernApi")
with httpx.Client(transport=httpx.MockTransport(handle)) as transport:
    client = sdk.FernApi(base_url="https://ledger.example.test", httpx_client=transport, **arguments)
    client.berths.list_berths(zone="north", codes=["C-100"])
print(json.dumps({"constructions": verdicts, "sent_headers": sent}, sort_keys=True))

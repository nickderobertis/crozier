# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as request-alias-reference-parameters.py does; crozier-e2e runs it and reads this folder through its e2eReads input.
"""Validate a docstring's client construction against the actual constructor.

The construction each docstring example writes is validated against the actual
constructor's annotations, then the client is constructed exactly as documented
and called through its public API over a socket to a local HTTP server, which
records the header values it receives.

Exit 0 prints one JSON proof result; exit 1 means the proof or SDK import failed;
exit 2 reports invalid CLI arguments on stderr.
"""

from __future__ import annotations

import argparse
import ast
import contextlib
import http.server
import importlib
import inspect
import json
from collections.abc import Iterator
from pathlib import Path
import sys
import textwrap
import threading
import typing

from pydantic import TypeAdapter, ValidationError

parser = argparse.ArgumentParser()
parser.add_argument("sdk", type=Path)
parser.add_argument("--expected", choices=("invalid", "valid"), required=True)
args = parser.parse_args()
if not (args.sdk / "fern" / "__init__.py").is_file():
    parser.error("sdk must contain the generated fern package")
sys.path.insert(0, str(args.sdk.resolve()))
sdk = importlib.import_module("fern")

# The measurement's promoted headers whose declared type is not a string, and
# the string one whose `YOUR_*` placeholder is correct.
TYPED = {"strict_mode": bool, "shift_number": int, "tide_metres": float}
STRING = "tenant_code"
WIRE = ("X-Strict-Mode", "X-Tenant-Code", "X-Shift-Number", "X-Tide-Metres")


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


@contextlib.contextmanager
def local_server() -> Iterator[tuple[str, list[dict[str, str]]]]:
    """A local HTTP server answering `[]`, and the headers of each request."""
    received: list[dict[str, str]] = []

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            received.append({wire: self.headers.get(wire, "") for wire in WIRE})
            body = b"[]"
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_: object) -> None:
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_address[1]}", received
    finally:
        server.shutdown()
        server.server_close()


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

# The documented construction, sent: the header values it puts on the wire.
documented = construction(examples["FernApi"] or "", "FernApi")
with local_server() as (base_url, received):
    # llmlint: ignore[async_typed_clients_at_boundaries] This journey proves the generated SDK's own synchronous client, the one its documented examples construct and call; the SDK under test, not this script, owns the HTTP boundary.
    sdk.FernApi(base_url=base_url, **documented).berths.list_berths(zone="north", codes=["C-100"])
print(json.dumps({"constructions": verdicts, "sent_headers": received}, sort_keys=True))

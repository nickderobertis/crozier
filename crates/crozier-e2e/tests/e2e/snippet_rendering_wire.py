"""Check a generated SDK's worked JSON-binary calls against the method they call.

Usage: snippet_rendering_wire.py SDK_SRC --expected {valid,invalid}. SDK_SRC is
the `src/` directory of an SDK generated from
`docs/fern-measurements/handed-off/snippet-rendering/json-binary-body-snippet/openapi.yml`
(crozier's, or the certified pair's `fern-expected/src`), with `reference.md`
beside it. For each of `replace_draft` and `replace_chart`, the `request` value
of the `reference.md` worked call and of the sync and async docstring examples is
validated strictly against the actual method's `request` annotation, then the
call is made through the public client over a socket to a local HTTP server,
which records the request it receives.

Exit 0 prints one JSON line (each example's verdict and each request sent);
exit 1 means a check failed; exit 2 reports invalid arguments or an SDK this
script cannot import.
"""

from __future__ import annotations

import argparse
import ast
import contextlib
import dataclasses
import http.server
import importlib
import inspect
import json
import re
import sys
import textwrap
import threading
import typing
from collections.abc import Iterator
from pathlib import Path

from pydantic import TypeAdapter, ValidationError

METHODS = ("replace_draft", "replace_chart")

parser = argparse.ArgumentParser()
parser.add_argument("sdk", type=Path)
parser.add_argument("--expected", choices=("invalid", "valid"), required=True)
args = parser.parse_args()
if not (args.sdk / "fern" / "__init__.py").is_file():
    parser.error("sdk must contain the generated fern package")
sys.path.insert(0, str(args.sdk.resolve()))
sdk = importlib.import_module("fern")
client_module = importlib.import_module("fern.patterns.client")
reference = (args.sdk.parent / "reference.md").read_text(encoding="utf-8")


def request_value(code: str, method: str) -> object:
    """The `request` argument of the one call of `method` in `code`."""
    calls = [
        node
        for node in ast.walk(ast.parse(code))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method
    ]
    assert len(calls) == 1, f"{len(calls)} calls of {method}"
    return ast.literal_eval(next(keyword.value for keyword in calls[0].keywords if keyword.arg == "request"))


examples: dict[str, str] = {}
for method in METHODS:
    blocks = [code for code in re.findall(r"```python\n(.*?)\n```", reference, re.DOTALL) if f".{method}(" in code]
    assert len(blocks) == 1, f"reference.md has {len(blocks)} worked calls of {method}"
    values = {"reference.md": request_value(blocks[0], method)}
    for prefix in ("", "Async"):
        function = getattr(getattr(client_module, f"{prefix}PatternsClient"), method)
        doc = inspect.getdoc(function)
        assert doc is not None
        values[f"{prefix}PatternsClient"] = request_value(textwrap.dedent(doc.split("Examples\n--------\n", 1)[1]), method)
        annotation = typing.get_type_hints(function)["request"]
        assert annotation is bytes, annotation
    for where, value in values.items():
        try:
            TypeAdapter(bytes).validate_python(value, strict=True)
        except ValidationError:
            assert args.expected == "invalid" and value == "string", (where, value)
            examples[f"{method} {where}"] = "plain string rejected by the bytes annotation"
        else:
            assert args.expected == "valid" and value == b"string", (where, value)
            examples[f"{method} {where}"] = "bytes example has its declared type"

@dataclasses.dataclass(frozen=True)
class Sent:
    """One request the local server received."""

    method: str
    path: str
    content_type: str
    body: str


@contextlib.contextmanager
def local_server() -> Iterator[tuple[str, list[Sent]]]:
    """A local HTTP server answering `204 No Content`, and what it received."""
    sent: list[Sent] = []

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_PUT(self) -> None:
            length = int(self.headers.get("content-length") or 0)
            sent.append(
                Sent(self.command, self.path, self.headers.get("content-type", ""), self.rfile.read(length).decode())
            )
            self.send_response(204)
            self.end_headers()

        def log_message(self, *_: object) -> None:
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_address[1]}", sent
    finally:
        server.shutdown()
        server.server_close()


with local_server() as (base_url, sent):
    client = sdk.FernApi(base_url=base_url)
    for method in METHODS:
        assert getattr(client.patterns, method)(pattern_id="twill-4", request=b"string") is None
assert [request.content_type for request in sent] == ["application/json"] * len(METHODS), sent
print(json.dumps({"examples": examples, "sent": [dataclasses.asdict(request) for request in sent]}, sort_keys=True))

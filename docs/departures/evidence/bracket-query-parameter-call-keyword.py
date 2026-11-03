# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as request-alias-reference-parameters.py does; crozier-e2e runs it and reads this folder through its e2eReads input.
"""Bind reference.md's worked calls for `[]` query parameters to the actual SDK.

Each worked call's keyword arguments are bound to the actual sync and async
methods; then each method is called with the argument it declares, through the
public client over a socket to a local HTTP server, which records the query
string it receives.

Exit 0 prints one JSON proof result; exit 1 means the proof or SDK import failed;
exit 2 reports invalid CLI arguments on stderr.
"""

from __future__ import annotations

import argparse
import ast
import asyncio
import contextlib
import http.server
import importlib
import inspect
import json
from collections.abc import Iterator
from pathlib import Path
import re
import sys
import threading
from urllib.parse import parse_qsl, urlsplit

parser = argparse.ArgumentParser()
parser.add_argument("sdk", type=Path)
parser.add_argument("--reference", type=Path, required=True)
parser.add_argument("--expected", choices=("invalid", "valid"), required=True)
args = parser.parse_args()
if not (args.sdk / "fern" / "__init__.py").is_file():
    parser.error("sdk must contain the generated fern package")
sys.path.insert(0, str(args.sdk.resolve()))
sdk = importlib.import_module("fern")

# The measurement's two operations taking a `[]` query parameter, and the wire
# name each call must send.
CALLS = {"list_berths": "codes[]", "release_berths": "ids[]"}
# The client headers every operation of the measurement requires.
HEADERS = {"strict_mode": True, "tenant_code": "harbour-7", "shift_number": 2, "tide_metres": 1.5}
reference = args.reference.read_text(encoding="utf-8")


def worked_call(method: str) -> dict[str, object]:
    """The keyword arguments of reference.md's worked call of `method`."""
    match = re.search(rf"^client\.berths\.{method}\(\n(.*?)^\)$", reference, re.MULTILINE | re.DOTALL)
    assert match, f"reference.md has no worked call of {method}"
    call = ast.parse(f"f(\n{match.group(1)})", mode="eval").body
    assert isinstance(call, ast.Call)
    return {keyword.arg or "": ast.literal_eval(keyword.value) for keyword in call.keywords}


@contextlib.contextmanager
def local_server() -> Iterator[tuple[str, list[list[tuple[str, str]]]]]:
    """A local HTTP server answering a `GET` with `[]` and a `DELETE` with
    `204 No Content`, and the query string of each request it received."""
    queries: list[list[tuple[str, str]]] = []

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            queries.append(parse_qsl(urlsplit(self.path).query))
            body = b"[]"
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_DELETE(self) -> None:
            queries.append(parse_qsl(urlsplit(self.path).query))
            self.send_response(204)
            self.end_headers()

        def log_message(self, *_: object) -> None:
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_address[1]}", queries
    finally:
        server.shutdown()
        server.server_close()


bindings: dict[str, str] = {}
with local_server() as (base_url, queries):
    for method, wire in CALLS.items():
        arguments = worked_call(method)
        keyword = next(name for name in arguments if name != "zone")
        for class_name in ("FernApi", "AsyncFernApi"):
            bound = getattr(getattr(sdk, class_name)(base_url=base_url, **HEADERS).berths, method)
            try:
                inspect.signature(bound).bind(**arguments)
            except TypeError as error:
                assert args.expected == "invalid", error
                assert "unexpected keyword argument" in str(error) and keyword in str(error), error
                bindings[f"{class_name}.{method}"] = str(error)
            else:
                assert args.expected == "valid", f"{class_name}.{method} bound {keyword}"
                bindings[f"{class_name}.{method}"] = f"{keyword} binds"
        # Either way the argument the generated method declares is the one sent
        # under the `[]` wire name.
        values = arguments[keyword]
        assert isinstance(values, list)
        extra = {"zone": arguments["zone"]} if "zone" in arguments else {}
        call = getattr(sdk.FernApi(base_url=base_url, **HEADERS).berths, method)
        call(**extra, **{wire.removesuffix("[]"): values})
        assert [pair for pair in queries[-1] if pair[0] == wire] == [(wire, value) for value in values], queries

    async def async_call() -> None:
        await sdk.AsyncFernApi(base_url=base_url, **HEADERS).berths.release_berths(ids=["B-7"])

    asyncio.run(async_call())
    assert queries[-1] == [("ids[]", "B-7")], queries
print(json.dumps({"bindings": bindings, "requests": len(queries)}, sort_keys=True))

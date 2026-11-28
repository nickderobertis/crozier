"""Drive a naming-acceptance measurement's generated SDK through its public client.

Usage: naming_acceptance_runtime.py JOURNEY SDK_SRC

JOURNEY is one of `colliding-request`, `colliding-responses`,
`colliding-control` (#944), `recursive-alias-dependents` (#922),
`aliased-discriminator` (#983) or `request-options-body-property` (#981);
SDK_SRC is
the generated SDK's `src/` directory. Each request goes over real HTTP to a
server this script runs on a free local port.

Exit status: 0 when the journey holds; 1 with the failing check's message;
2 on a usage error.
"""

from __future__ import annotations

import asyncio
import http.server
import importlib
import json
import pkgutil
import sys
import threading
import urllib.parse
from collections.abc import Callable
from pathlib import Path
from typing import Any, NamedTuple, TypedDict


class Recorded(NamedTuple):
    """One request the journey server received: its method, target and headers."""

    method: str
    target: str
    headers: dict[str, str]


class SdkOptions(TypedDict):
    """The `RequestOptions` keys these journeys pass to a generated client."""

    additional_headers: dict[str, str]
    max_retries: int


MAX_BODY = 1 << 20
"""The largest request body the journey server reads; an SDK request is far smaller."""


class Server:
    """A real HTTP server on a free local port, answering each path (its query
    string aside, where the whole target is not configured) with its configured
    JSON body, or bytes as a binary body, and recording every request body it
    receives (a form-encoded one as its fields), the headers each request
    carried, and every request's method, target and headers."""

    def __init__(self, bodies: dict[str, object]) -> None:
        self.received: list[object] = []
        self.headers: list[dict[str, str]] = []
        self.requests: list[Recorded] = []
        server = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                self._record("GET")
                self._answer()

            def do_POST(self) -> None:
                declared = self.headers.get("Content-Length") or "0"
                ascii_decimal = declared.isascii() and declared.isdecimal() and len(declared) <= 8
                if not ascii_decimal or int(declared) > MAX_BODY:
                    self.send_error(400, f"Content-Length must be 0..{MAX_BODY}, not {declared!r}")
                    return
                raw = self.rfile.read(int(declared))
                if (self.headers.get("Content-Type") or "").startswith("application/x-www-form-urlencoded"):
                    server.received.append(dict(urllib.parse.parse_qsl(raw.decode())))
                else:
                    server.received.append(json.loads(raw or b"null"))
                server.headers.append({key.lower(): value for key, value in self.headers.items()})
                self._record("POST")
                self._answer()

            def _record(self, method: str) -> None:
                server.requests.append(
                    Recorded(method, self.path, {key.lower(): value for key, value in self.headers.items()})
                )

            def _answer(self) -> None:
                body = bodies.get(self.path, bodies.get(self.path.split("?", 1)[0]))
                if body is None:
                    self.send_response(204)
                    self.end_headers()
                    return
                binary = isinstance(body, bytes)
                payload = body if isinstance(body, bytes) else json.dumps(body).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/octet-stream" if binary else "application/json")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *_args: object) -> None:
                pass

        self.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    @property
    def base_url(self) -> str:
        return f"http://127.0.0.1:{self.httpd.server_address[1]}"

    def client(self) -> Any:
        """The generated SDK's async client pointed at this server. Its class is
        imported from the SDK under test, generated at run time, so this script
        has no static type for it."""
        from fern import AsyncFernApi

        return AsyncFernApi(base_url=self.base_url)

    def close(self) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()


def colliding_request() -> None:
    """Each colliding component's own model builds the body, sent as declared."""
    from fern import KilnGlazeCoat, KilnGlazeCoat2

    server = Server({})
    try:
        asyncio.run(server.client().create_records(left=KilnGlazeCoat2(left="matte"), right=KilnGlazeCoat(right=3)))
    finally:
        server.close()
    if server.received != [{"left": {"left": "matte"}, "right": {"right": 3}}]:
        raise SystemExit(f"colliding-request: sent {server.received!r}")


def colliding_responses() -> None:
    """Each operation's declared response parses into its own component's class."""
    from fern import KilnGlazeCoat, KilnGlazeCoat2

    server = Server({"/left": {"left": "matte"}, "/right": {"right": 3}})
    try:
        api = server.client()
        left = asyncio.run(api.get_left())
        right = asyncio.run(api.get_right())
    finally:
        server.close()
    if not isinstance(left, KilnGlazeCoat2) or left.left != "matte":
        raise SystemExit(f"colliding-responses: get_left returned {left!r}")
    if not isinstance(right, KilnGlazeCoat) or right.right != 3:
        raise SystemExit(f"colliding-responses: get_right returned {right!r}")


def colliding_control() -> None:
    """The one component's response parses into its class."""
    from fern import KilnGlazeCoat

    server = Server({"/left": {"left": "matte"}})
    try:
        left = asyncio.run(server.client().get_left())
    finally:
        server.close()
    if not isinstance(left, KilnGlazeCoat) or left.left != "matte":
        raise SystemExit(f"colliding-control: get_left returned {left!r}")


def recursive_alias_dependents() -> None:
    """Every module imports, and the dependent model holds a recursive object."""
    import_every_module()
    from fern.types.fit_summary import FitSummary

    summary = FitSummary(report={"engine": "nuts", "inference_diagnostics": {"chains": [1, {"ok": True}]}})
    if summary.report.engine != "nuts":
        raise SystemExit(f"recursive-alias-dependents: built {summary!r}")


def aliased_discriminator() -> None:
    """Each variant of a union tagged by a wire key needing a Python alias
    (`schema`, field `schema_`) parses through the client into its own class."""
    from fern import QueryResponse_Graph, QueryResponse_Table

    server = Server(
        {"/queries/t": {"schema": "table", "rowCount": 3}, "/queries/g": {"schema": "graph", "nodes": ["a", "b"]}}
    )
    try:
        api = server.client()
        table = asyncio.run(api.get_query("t"))
        graph = asyncio.run(api.get_query("g"))
    finally:
        server.close()
    if not isinstance(table, QueryResponse_Table) or (table.schema_, table.row_count) != ("table", 3):
        raise SystemExit(f"aliased-discriminator: get_query('t') returned {table!r}")
    if not isinstance(graph, QueryResponse_Graph) or (graph.schema_, graph.nodes) != ("graph", ["a", "b"]):
        raise SystemExit(f"aliased-discriminator: get_query('g') returned {graph!r}")


def import_every_module() -> None:
    """Import every module of the generated `fern` package."""
    import fern

    for module in pkgutil.walk_packages(fern.__path__, "fern."):
        # `fern.version` reads the installed distribution's metadata, and this
        # journey runs the SDK from its source tree, uninstalled.
        if module.name != "fern.version":
            importlib.import_module(module.name)


def request_options_body_property() -> None:
    """A body property named `request_options` is sent as the caller's value,
    while the SDK's own options, `_request_options`, apply as options, through
    the sync, async and both raw clients alike."""
    from fern import AsyncFernApi, FernApi

    import_every_module()
    server = Server({"/dispatches": {"id": "d-1", "request_options": "express"}})
    options: SdkOptions = {"additional_headers": {"x-courier-trace": "t-1"}, "max_retries": 0}
    arguments: dict[str, Any] = {"request_options": "express", "kwargs_": "k", "self_": "s"}
    try:
        sync = FernApi(base_url=server.base_url).dispatches
        async_ = AsyncFernApi(base_url=server.base_url).dispatches
        results = [
            # llmlint: ignore-block[async_typed_clients_at_boundaries] #981 requires the generated sync client and its raw variant to be driven too; these two calls are that coverage, beside the async calls below.
            sync.create_dispatch(**arguments, _request_options=options),
            sync.with_raw_response.create_dispatch(**arguments, _request_options=options).data,
            # llmlint: ignore-end[async_typed_clients_at_boundaries]
            asyncio.run(async_.create_dispatch(**arguments, _request_options=options)),
            asyncio.run(async_.with_raw_response.create_dispatch(**arguments, _request_options=options)).data,
        ]
    finally:
        server.close()
    sent = {"request_options": "express", "kwargs": "k", "self": "s"}
    if server.received != [sent] * 4:
        raise SystemExit(f"request-options-body-property: sent {server.received!r}")
    traces = [headers.get("x-courier-trace") for headers in server.headers]
    if traces != ["t-1"] * 4:
        raise SystemExit(f"request-options-body-property: the options' header reached {traces!r}")
    if any(result.id != "d-1" or result.request_options != "express" for result in results):
        raise SystemExit(f"request-options-body-property: returned {results!r}")
    other_sources(options)


def other_sources(options: SdkOptions) -> None:
    """The other places an argument can take the name: a query parameter (on a
    paginated and on a binary-download operation), a header and a form field
    beside disabled retries each rename the SDK's options `_request_options`,
    while a path parameter is `request_options_` and leaves the SDK's options
    `request_options`. Each argument reaches the wire under its own name, and
    each operation's options reach it as options."""
    from fern import AsyncFernApi

    server = Server(
        {
            "/routes?page=1&request_options=by-query": {"routes": ["r-1"]},
            "/routes": {"routes": []},
            "/dispatches/d-1/manifest": b"manifest-bytes",
            "/labels": [{"id": "l-1"}],
            "/labels/express": {"id": "l-2"},
        }
    )

    async def drive() -> tuple[list[str], bytes, Any, Any]:
        api = AsyncFernApi(base_url=server.base_url)
        pager = await api.routes.list_routes(request_options="by-query", _request_options=options)
        routes = [route async for route in pager]
        chunks = [
            chunk
            async for chunk in api.dispatches.download_manifest(
                "d-1", request_options="by-query", _request_options=options
            )
        ]
        await api.dispatches.add_note("d-1", request_options="by-form", _request_options=options)
        labels = await api.labels.list_labels(request_options="by-header", _request_options=options)
        label = await api.labels.get_label(request_options_="express", request_options=options)
        return routes, b"".join(chunks), labels, label

    try:
        routes, manifest, labels, label = asyncio.run(drive())
    finally:
        server.close()
    if (
        routes != ["r-1"]
        or manifest != b"manifest-bytes"
        or [item.id for item in labels] != ["l-1"]
        or label.id != "l-2"
    ):
        raise SystemExit(f"request-options-body-property: returned {routes!r}, {manifest!r}, {labels!r}, {label!r}")
    targets = [(request.method, request.target.split("?", 1)) for request in server.requests]
    expected = [
        ("GET", ["/routes", "page=1&request_options=by-query"]),
        ("GET", ["/routes", "page=2&request_options=by-query"]),
        ("GET", ["/dispatches/d-1/manifest", "request_options=by-query"]),
        ("POST", ["/dispatches/d-1/notes"]),
        ("GET", ["/labels"]),
        ("GET", ["/labels/express"]),
    ]
    if targets != expected:
        raise SystemExit(f"request-options-body-property: requested {targets!r}")
    if server.received != [{"request_options": "by-form"}]:
        raise SystemExit(f"request-options-body-property: the form sent {server.received!r}")
    headers = [request.headers for request in server.requests]
    (listed,) = [request.headers for request in server.requests if request.target == "/labels"]
    if listed.get("request-options") != "by-header":
        raise SystemExit(f"request-options-body-property: the header went as {listed!r}")
    traces = [request.get("x-courier-trace") for request in headers]
    if traces != ["t-1"] * len(expected):
        raise SystemExit(f"request-options-body-property: the options' header reached {traces!r}")


JOURNEYS: dict[str, Callable[[], None]] = {
    "aliased-discriminator": aliased_discriminator,
    "colliding-request": colliding_request,
    "colliding-responses": colliding_responses,
    "colliding-control": colliding_control,
    "recursive-alias-dependents": recursive_alias_dependents,
    "request-options-body-property": request_options_body_property,
}


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in JOURNEYS:
        print(f"usage: {Path(sys.argv[0]).name} {{{','.join(JOURNEYS)}}} SDK_SRC", file=sys.stderr)
        raise SystemExit(2)
    source = Path(sys.argv[2]).resolve()
    if not (source / "fern" / "__init__.py").is_file():
        print(f"{source}: no generated `fern` package; pass the SDK's src/ directory", file=sys.stderr)
        raise SystemExit(2)
    sys.path.insert(0, str(source))
    import fern

    if Path(fern.__file__).resolve().parent != source / "fern":
        raise SystemExit(f"imported {fern.__file__}, not the SDK under {source}")
    JOURNEYS[sys.argv[1]]()
    print(f"{sys.argv[1]}: ok")


if __name__ == "__main__":
    main()

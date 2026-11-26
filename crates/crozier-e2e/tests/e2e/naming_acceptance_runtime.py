"""Drive a naming-acceptance measurement's generated SDK through its public client.

Usage: naming_acceptance_runtime.py JOURNEY SDK_SRC

JOURNEY is one of `colliding-request`, `colliding-responses`,
`colliding-control` (#944), `recursive-alias-dependents` (#922) or
`request-options-body-property` (#981); SDK_SRC is
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
from collections.abc import Callable
from pathlib import Path
from typing import Any

MAX_BODY = 1 << 20
"""The largest request body the journey server reads; an SDK request is far smaller."""


class Server:
    """A real HTTP server on a free local port, answering each path with its
    configured JSON body and recording every request body it receives, and the
    headers each request carried."""

    def __init__(self, bodies: dict[str, object]) -> None:
        self.received: list[object] = []
        self.headers: list[dict[str, str]] = []
        server = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                self._answer()

            def do_POST(self) -> None:
                declared = self.headers.get("Content-Length") or "0"
                ascii_decimal = declared.isascii() and declared.isdecimal() and len(declared) <= 8
                if not ascii_decimal or int(declared) > MAX_BODY:
                    self.send_error(400, f"Content-Length must be 0..{MAX_BODY}, not {declared!r}")
                    return
                server.received.append(json.loads(self.rfile.read(int(declared)) or b"null"))
                server.headers.append({key.lower(): value for key, value in self.headers.items()})
                self._answer()

            def _answer(self) -> None:
                body = bodies.get(self.path)
                if body is None:
                    self.send_response(204)
                    self.end_headers()
                    return
                payload = json.dumps(body).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
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
    options = {"additional_headers": {"x-courier-trace": "t-1"}, "max_retries": 0}
    arguments: dict[str, Any] = {"request_options": "express", "kwargs_": "k", "self_": "s"}
    try:
        sync = FernApi(base_url=server.base_url).dispatches
        async_ = AsyncFernApi(base_url=server.base_url).dispatches
        results = [
            sync.create_dispatch(**arguments, _request_options=options),
            sync.with_raw_response.create_dispatch(**arguments, _request_options=options).data,
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


JOURNEYS: dict[str, Callable[[], None]] = {
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

"""Drive a naming-acceptance measurement's generated SDK through its public client.

Usage: naming_acceptance_runtime.py JOURNEY SDK_SRC

JOURNEY is one of `colliding-request`, `colliding-responses`,
`colliding-control` (#944) or `recursive-alias-dependents` (#922); SDK_SRC is
the generated SDK's `src/` directory. Each request goes over real HTTP to a
server this script runs on a free local port.

Exit status: 0 when the journey holds; 1 with the failing check's message;
2 on a usage error.
"""

from __future__ import annotations

import http.server
import importlib
import json
import pkgutil
import sys
import threading
from collections.abc import Callable
from pathlib import Path
from typing import Any


class Server:
    """A real HTTP server on a free local port, answering each path with its
    configured JSON body and recording every request body it receives."""

    def __init__(self, bodies: dict[str, object]) -> None:
        self.received: list[object] = []
        server = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                self._answer()

            def do_POST(self) -> None:
                length = int(self.headers.get("Content-Length") or 0)
                server.received.append(json.loads(self.rfile.read(length) or b"null"))
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

    def client(self) -> Any:
        """The generated SDK's client pointed at this server. Its class is
        imported from the SDK under test, generated at run time, so this script
        has no static type for it."""
        from fern import FernApi

        return FernApi(base_url=f"http://127.0.0.1:{self.httpd.server_address[1]}")

    def close(self) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()


def colliding_request() -> None:
    """Each colliding component's own model builds the body, sent as declared."""
    from fern import KilnGlazeCoat, KilnGlazeCoat2

    server = Server({})
    try:
        server.client().create_records(left=KilnGlazeCoat2(left="matte"), right=KilnGlazeCoat(right=3))
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
        left = api.get_left()
        right = api.get_right()
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
        left = server.client().get_left()
    finally:
        server.close()
    if not isinstance(left, KilnGlazeCoat) or left.left != "matte":
        raise SystemExit(f"colliding-control: get_left returned {left!r}")


def recursive_alias_dependents() -> None:
    """Every module imports, and the dependent model holds a recursive object."""
    import fern

    for module in pkgutil.walk_packages(fern.__path__, "fern."):
        importlib.import_module(module.name)
    from fern.types.fit_summary import FitSummary

    summary = FitSummary(report={"engine": "nuts", "inference_diagnostics": {"chains": [1, {"ok": True}]}})
    if summary.report.engine != "nuts":
        raise SystemExit(f"recursive-alias-dependents: built {summary!r}")


JOURNEYS: dict[str, Callable[[], None]] = {
    "colliding-request": colliding_request,
    "colliding-responses": colliding_responses,
    "colliding-control": colliding_control,
    "recursive-alias-dependents": recursive_alias_dependents,
}


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in JOURNEYS:
        print(f"usage: {Path(sys.argv[0]).name} {{{','.join(JOURNEYS)}}} SDK_SRC", file=sys.stderr)
        raise SystemExit(2)
    sys.path.insert(0, sys.argv[2])
    JOURNEYS[sys.argv[1]]()
    print(f"{sys.argv[1]}: ok")


if __name__ == "__main__":
    main()

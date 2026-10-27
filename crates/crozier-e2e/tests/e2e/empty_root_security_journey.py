"""Drive RS-Server's generated SDK against a local HTTP server.

RS-Server declares root `security: []`, so its operations without their own
`security` need no credential. A client built without a key calls
`GET /catalog/_mgmt/ping` and sends no `x-api-key` header. A client built with
a key sends it on the secured `GET /storage/account/credentials`. Both run sync
and async.

Exit 0 prints one line per request; exit 1 means a journey or the SDK import
failed; exit 2 reports invalid CLI arguments on stderr.
"""

import argparse
import asyncio
import contextlib
import http.server
import importlib
import json
import sys
import threading
from collections.abc import Iterator
from pathlib import Path
from typing import NamedTuple

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("sdk_src", type=Path)
args = parser.parse_args()
if not (args.sdk_src / "fern" / "__init__.py").is_file():
    parser.error("sdk_src must contain the generated fern package")
sys.path.insert(0, str(args.sdk_src.resolve()))
sdk = importlib.import_module("fern")


class Received(NamedTuple):
    """One request the server received: its path and its `x-api-key` header."""

    path: str
    api_key: str | None


received: list[Received] = []


class Handler(http.server.BaseHTTPRequestHandler):
    """Answers every route with an empty JSON object and records its key header."""

    def do_GET(self) -> None:
        received.append(Received(self.path, self.headers.get("x-api-key")))
        body = b"{}"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        pass


@contextlib.contextmanager
def server() -> Iterator[str]:
    """A real HTTP server on a loopback port, for the SDK's own httpx client."""
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{httpd.server_address[1]}"
    finally:
        httpd.shutdown()
        httpd.server_close()


# llmlint: ignore-block[async_typed_clients_at_boundaries] The synchronous `FernApi` is half of the generated SDK under test, not this script's own choice of HTTP client, so the journey drives it and `AsyncFernApi` alike.
def journeys(base_url: str) -> None:
    anonymous = sdk.FernApi(base_url=base_url)
    keyed = sdk.FernApi(base_url=base_url, api_key="rs-key")
    assert anonymous.catalog_liveliness_readiness.ping_catalog_mgmt_ping_get() == {}
    assert keyed.osam_service.get_your_s3credentials() == {}

    async def run() -> None:
        anonymous = sdk.AsyncFernApi(base_url=base_url)
        keyed = sdk.AsyncFernApi(base_url=base_url, api_key="rs-key")
        assert await anonymous.catalog_liveliness_readiness.ping_catalog_mgmt_ping_get() == {}
        assert await keyed.osam_service.get_your_s3credentials() == {}

    asyncio.run(run())
    expected = [Received("/catalog/_mgmt/ping", None), Received("/storage/account/credentials", "rs-key")] * 2
    assert received == expected, received
    for request in received:
        print(f"{request.path} x-api-key={json.dumps(request.api_key)}")


# llmlint: ignore-end[async_typed_clients_at_boundaries]


try:
    with server() as base_url:
        journeys(base_url)
except Exception as error:
    print(f"empty-root-security: {type(error).__name__}: {error}", file=sys.stderr)
    sys.exit(1)

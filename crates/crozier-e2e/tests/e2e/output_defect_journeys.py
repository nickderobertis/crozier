"""Drive a generated SDK for one measured output defect against a local HTTP server.

`validation-error` takes the SDK of
docs/fern-measurements/output-defects/602-validation-error-shadowing and parses
a response that fails validation on each raw path (JSON, Server-Sent Events,
binary download), sync and async: each must raise the SDK's ParsingError.
`parameter-collision` takes the SDK of
docs/fern-measurements/output-defects/612-parameter-location-collision and
calls every method with each parameter that shares a name with another
location: each must reach the server under its own wire name.

Exit 0 prints one line per journey; exit 1 means a journey or the SDK import
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
from urllib.parse import parse_qs, urlsplit

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("case", choices=["validation-error", "parameter-collision"])
parser.add_argument("sdk_src", type=Path)
args = parser.parse_args()
if not (args.sdk_src / "fern" / "__init__.py").is_file():
    parser.error("sdk_src must contain the generated fern package")
sys.path.insert(0, str(args.sdk_src.resolve()))
sdk = importlib.import_module("fern")
ParsingError = importlib.import_module("fern.core.parse_error").ParsingError

INVALID_PROBLEM = json.dumps({"line": "not a line number", "rule": "serial-comma"}).encode()
received: list[dict[str, object]] = []


class Handler(http.server.BaseHTTPRequestHandler):
    """Answers each route with its canned response and records what arrived."""

    def do_GET(self) -> None:
        url = urlsplit(self.path)
        received.append({"path": url.path, "query": parse_qs(url.query), "headers": dict(self.headers.items())})
        status, body = 200, b"[]"
        if url.path.endswith("/problems/first"):
            body = INVALID_PROBLEM
        elif url.path.endswith(("/problems/live", "/annotated")):
            status, body = 422, INVALID_PROBLEM
        elif url.path.startswith("/branches/") and "/shelves/" in url.path:
            body = json.dumps({"code": url.path.rsplit("/", 1)[1]}).encode()
        self.send_response(status)
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


def expect_parsing_error(label: str, call: object) -> None:
    try:
        result = call() if callable(call) else call
        if hasattr(result, "__iter__") and not isinstance(result, (bytes, str)):
            for _ in result:
                pass
    except ParsingError as error:
        print(f"{label}: ParsingError(status_code={error.status_code}) caused by {type(error.cause).__name__}")
        return
    raise AssertionError(f"{label}: a response that fails validation raised no ParsingError")


async def expect_parsing_error_async(label: str, call: object) -> None:
    try:
        result = call()
        if hasattr(result, "__aiter__"):
            async for _ in result:
                pass
        else:
            await result
    except ParsingError as error:
        print(f"{label}: ParsingError(status_code={error.status_code}) caused by {type(error.cause).__name__}")
        return
    raise AssertionError(f"{label}: a response that fails validation raised no ParsingError")


def validation_error(base_url: str) -> None:
    client = sdk.FernApi(base_url=base_url)
    expect_parsing_error("sync JSON", lambda: client.get_first_problem("ms-1"))
    expect_parsing_error("sync event stream", lambda: client.follow_problems("ms-1"))
    expect_parsing_error("sync binary download", lambda: client.download_annotated("ms-1"))
    aclient = sdk.AsyncFernApi(base_url=base_url)

    async def run() -> None:
        await expect_parsing_error_async("async JSON", lambda: aclient.get_first_problem("ms-1"))
        await expect_parsing_error_async("async event stream", lambda: aclient.follow_problems("ms-1"))
        await expect_parsing_error_async("async binary download", lambda: aclient.download_annotated("ms-1"))

    asyncio.run(run())


def assert_request(index: int, path: str, query: dict[str, list[str]], headers: dict[str, str]) -> None:
    request = received[index]
    assert request["path"] == path, request
    assert request["query"] == query, request
    sent = {name.lower(): value for name, value in request["headers"].items()}
    for name, value in headers.items():
        assert sent.get(name.lower()) == value, (name, request)
    print(f"{request['path']} query={json.dumps(query, sort_keys=True)} headers={json.dumps(headers, sort_keys=True)}")


def parameter_collision(base_url: str) -> None:
    calls = [
        lambda client: client.get_shelf("central", "A-12", shelf="A-11"),
        lambda client: client.list_edition_scans("central", "first", edition="second"),
        lambda client: client.list_loans(patron="p-7", page_size=10),
    ]
    client = sdk.FernApi(base_url=base_url, branch="north", page_size=25)
    shelf = calls[0](client)
    assert shelf.code == "A-12", shelf
    for call in calls[1:]:
        call(client)
    aclient = sdk.AsyncFernApi(base_url=base_url, branch="north", page_size=25)

    async def run() -> None:
        for call in calls:
            await call(aclient)

    asyncio.run(run())
    for offset in (0, 3):
        client_headers = {"branch": "north", "Page-Size": "25"}
        assert_request(offset, "/branches/central/shelves/A-12", {"shelf": ["A-11"]}, client_headers)
        assert_request(
            offset + 1, "/branches/central/editions/first/scans", {}, {**client_headers, "edition": "second"}
        )
        assert_request(offset + 2, "/loans", {"patron": ["p-7"], "page_size": ["10"]}, client_headers)
    assert len(received) == 6, received


try:
    with server() as base_url:
        if args.case == "validation-error":
            validation_error(base_url)
        else:
            parameter_collision(base_url)
except Exception as error:
    print(f"{args.case}: {type(error).__name__}: {error}", file=sys.stderr)
    sys.exit(1)

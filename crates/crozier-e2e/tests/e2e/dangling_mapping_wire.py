"""Drive the dangling-mapping-target measurement's SDK through its real client.

Usage: dangling_mapping_wire.py SDK_SRC. SDK_SRC is a generated SDK's `src/`
directory holding the `fern` package for
docs/fern-measurements/emission-parity/dangling-mapping-target/openapi.yml,
whose `Reading` maps `METEOR` to a target naming no component while
`MeteorReading`, the member that carries the variant, tags itself `METEOR`.

Every request goes over a socket to a local HTTP server that answers with the
payload the journey chose and records what the client sent. The journey reads
a logbook entry whose reading is a meteor, as the member schema declares it,
expects it to parse into the `Reading_Meteor` wrapper with the meteor's own
fields, and posts it back, expecting the server to receive exactly that
payload. A star reading, whose mapping target names its component, makes the
same round trip as the control.

Exit 0 prints one line per step; exit 1 names the first step that failed; exit
2 reports invalid arguments or an SDK this script cannot import.
"""

import argparse
import contextlib
import http.server
import importlib
import json
import sys
import threading
from collections.abc import Iterator
from pathlib import Path
from typing import Any

METEOR = {"kind": "METEOR", "brightness": -3.5, "trail": {"degrees": 12.0, "colour": "green"}}
STAR = {"kind": "STAR", "magnitude": 1.25, "constellation": "Lyra"}


class Failure(Exception):
    """A step whose observed behaviour is not the one the measurement states."""


def check(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


class Server:
    """A local HTTP server answering every GET with `answer` and recording each POST body."""

    def __init__(self) -> None:
        self.answer: dict[str, Any] = {}
        self.received: list[Any] = []
        outer = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def log_message(self, *_: object) -> None:
                pass

            def reply(self, body: object) -> None:
                data = json.dumps(body).encode()
                self.send_response(200)
                self.send_header("content-type", "application/json")
                self.send_header("content-length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def do_GET(self) -> None:
                self.reply(outer.answer)

            def do_POST(self) -> None:
                length = int(self.headers.get("content-length", 0))
                outer.received.append(json.loads(self.rfile.read(length)))
                self.reply({"id": "posted"})

        self.httpd = http.server.HTTPServer(("127.0.0.1", 0), Handler)

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.httpd.server_port}"


@contextlib.contextmanager
def serving() -> Iterator[Server]:
    server = Server()
    thread = threading.Thread(target=server.httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield server
    finally:
        server.httpd.shutdown()
        server.httpd.server_close()


def round_trip(client: Any, server: Server, reading: dict[str, Any], wrapper: str) -> str:
    """Read a logbook entry holding `reading`, then post its reading back unchanged."""
    server.answer = {"id": "entry", "reading": reading}
    try:
        entry = client.get_reading("entry")
    except Exception as error:
        # Whatever the SDK raises while parsing is the observation.
        last = " | ".join(str(error).splitlines()[-3:])
        raise Failure(f"{reading['kind']}: reading the entry raised {type(error).__name__}: {last}") from error
    parsed = entry.reading
    check(type(parsed).__name__ == wrapper, f"{reading['kind']}: parsed as {type(parsed).__name__}, not {wrapper}")
    for wire, value in reading.items():
        if wire == "kind":
            continue
        field = getattr(parsed, wire, None)
        got = field.dict() if hasattr(field, "dict") else field
        got = {key: item for key, item in got.items() if item is not None} if isinstance(got, dict) else got
        check(got == value, f"{reading['kind']}: {wrapper}.{wire} is {got!r}, not {value!r}")
    client.record_reading(request=parsed)
    sent = server.received[-1]
    check(sent == reading, f"{reading['kind']}: posting it back sent {json.dumps(sent, sort_keys=True)}")
    return f"{reading['kind']}: parsed into {wrapper} and posted back as {json.dumps(sent, sort_keys=True)}"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("sdk_src", type=Path)
    arguments = parser.parse_args(argv)
    if not (arguments.sdk_src / "fern" / "__init__.py").is_file():
        print(f"{arguments.sdk_src} must contain the generated fern package", file=sys.stderr)
        return 2
    sys.path.insert(0, str(arguments.sdk_src))
    try:
        sdk = importlib.import_module("fern")
        client_class = sdk.FernApi
    except (ImportError, AttributeError) as error:
        print(f"cannot import the generated fern package's FernApi: {error}", file=sys.stderr)
        return 2
    with serving() as server:
        client = client_class(base_url=server.url)
        try:
            for reading, wrapper in ((STAR, "Reading_Star"), (METEOR, "Reading_Meteor")):
                print(round_trip(client, server, reading, wrapper))
        except Failure as failure:
            print(f"failed: {failure}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

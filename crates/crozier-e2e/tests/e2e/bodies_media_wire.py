"""Drive one generated SDK of a bodies-and-media measurement against a local server.

Usage: bodies_media_wire.py CAUSE SDK_SRC. CAUSE names a measurement under
`docs/fern-measurements/handed-off/bodies-media/` whose verdict rests on what
goes over the wire; SDK_SRC is a generated SDK's `src/` directory holding the
`fern` package (crozier's, or the certified pair's `fern-expected/src`). Every
call goes through the public client over a socket to a local HTTP server, which
records the request it receives and answers with the payload the step chose, so
each line reports what the SDK really sent or really returned.

Exit 0 prints one JSON line per step (`sent` for a request: its method, path,
`content-type` header and body or multipart parts; `returned` for a parsed
value); exit 1 names a step whose call failed; exit 2 reports invalid arguments
or an SDK this script cannot import.
"""

import argparse
import contextlib
import http.server
import importlib
import json
import sys
import threading
from collections.abc import Callable, Iterator
from email import policy
from email.parser import BytesParser
from pathlib import Path
from typing import Any, ClassVar

CAUSES = (
    "request-content-type-header",
    "media-type-recognition",
    "multipart-empty-body",
    "multipart-scalar-union-part-encoding",
    "streaming-detection",
    "geo-json-success-media",
)


class Recorder(http.server.BaseHTTPRequestHandler):
    """Records each request and answers with the response its path is given."""

    seen: ClassVar[list[dict[str, Any]]] = []
    answers: ClassVar[dict[str, tuple[int, str, bytes]]] = {}

    def _handle(self) -> None:
        length = int(self.headers.get("content-length") or 0)
        body = self.rfile.read(length) if length else b""
        self.seen.append(
            {
                "method": self.command,
                "path": self.path,
                "content-type": self.headers.get("content-type"),
                "body": body,
            }
        )
        status, content_type, payload = self.answers.get(self.path, (204, "", b""))
        self.send_response(status)
        if content_type:
            self.send_header("content-type", content_type)
        self.send_header("content-length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    do_GET = do_POST = do_PUT = _handle

    def log_message(self, format: str, *args: object) -> None:
        pass


@contextlib.contextmanager
def server(answers: dict[str, tuple[int, str, bytes]]) -> Iterator[str]:
    Recorder.seen = []
    Recorder.answers = answers
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Recorder)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{httpd.server_address[1]}"
    finally:
        httpd.shutdown()
        httpd.server_close()


def parts(content_type: str, body: bytes) -> dict[str, Any]:
    """A multipart body's parts: each name to its text, or its filename and type."""
    message = BytesParser(policy=policy.default).parsebytes(
        f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode() + body
    )
    found: dict[str, Any] = {}
    for part in message.iter_parts():
        name = part.get_param("name", header="content-disposition")
        filename = part.get_filename()
        payload = part.get_payload(decode=True) or b""
        found[name] = {"filename": filename, "content-type": part.get_content_type()} if filename else payload.decode()
    return found


def sent(step: str) -> None:
    request = Recorder.seen.pop()
    content_type = request["content-type"]
    body: Any = request["body"].decode() if request["body"] else None
    if content_type and content_type.startswith("multipart/form-data"):
        body = parts(content_type, request["body"])
        content_type = "multipart/form-data"
    line = {"method": request["method"], "path": request["path"], "content-type": content_type, "body": body}
    print(json.dumps({"step": step, "sent": line}, sort_keys=True))


def returned(step: str, value: Any) -> None:
    if hasattr(value, "model_dump"):
        value = {"class": type(value).__name__, **value.model_dump(mode="json", by_alias=True)}
    elif isinstance(value, list):
        value = [
            {"class": type(item).__name__, **item.model_dump(mode="json", by_alias=True)}
            if hasattr(item, "model_dump")
            else item
            for item in value
        ]
    print(json.dumps({"step": step, "returned": value}, sort_keys=True))


def steps(cause: str, client: Any) -> list[tuple[str, Callable[[], Any], dict[str, tuple[int, str, bytes]]]]:
    """Each step of `cause`: its name, the call, and what the server answers."""
    no_answer: dict[str, tuple[int, str, bytes]] = {}
    if cause == "request-content-type-header":
        bell = json.dumps({"name": "Great Tom", "note": "E flat"}).encode()
        return [
            ("tune_bell", lambda: client.bells.tune_bell("tenor", strike_note="D"), no_answer),
            ("inscribe_bell", lambda: client.bells.inscribe_bell("tenor", text="Laudo Deum"), no_answer),
            (
                "create_bell",
                lambda: client.bells.create_bell(name="Great Tom", note="E flat"),
                {"/bells": (201, "application/json", bell)},
            ),
            ("order_cast", lambda: client.casts.order_cast(request={"kind": "handbell", "octaves": 2}), no_answer),
            ("add_note", lambda: client.notes.add_note(text="Recast after the crack", author="Founder"), no_answer),
        ]
    if cause == "media-type-recognition":
        deposit = json.dumps({"species": "Malus sieversii", "grams": 12.5}).encode()
        vault = json.dumps({"vaultId": "north", "deposits": 3}).encode()
        return [
            (
                "record_deposit",
                lambda: client.deposits.record_deposit(species="Malus sieversii", grams=12.5),
                {"/deposits": (200, "application/json", deposit)},
            ),
            (
                "record_germination",
                lambda: client.deposits.record_germination("lot-7", sown=40, sprouted=31),
                no_answer,
            ),
            (
                "get_vault",
                lambda: client.vaults.get_vault("north"),
                {"/vaults/north": (200, "application/json", vault)},
            ),
        ]
    if cause == "multipart-empty-body":
        return [("advance_queue", lambda: client.queue.advance_queue(), no_answer)]
    if cause == "multipart-scalar-union-part-encoding":
        scan = ("map.tiff", b"II*\x00scan", "image/tiff")
        return [
            ("file_scan label", lambda: client.scans.file_scan(scan=scan, drawer="A-12"), no_answer),
            ("file_scan number", lambda: client.scans.file_scan(scan=scan, drawer=12), no_answer),
        ]
    if cause == "streaming-detection":
        events = b"".join(
            b"data: " + json.dumps({"patternId": "p-1", "rows": rows}).encode() + b"\n\n" for rows in (1, 2)
        )
        return [
            (
                "weave_pattern",
                lambda: list(client.patterns.weave_pattern(draft="1-2-3", incremental=True)),
                {"/patterns/weave": (200, "text/event-stream", events)},
            )
        ]
    if cause == "geo-json-success-media":
        feature = json.dumps(
            {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-122.4, 37.8]}, "name": "Ridge"}
        ).encode()
        return [
            (
                "get_trailhead",
                lambda: client.trailheads.get_trailhead("ridge"),
                {"/trailheads/ridge": (200, "application/geo+json", feature)},
            )
        ]
    raise AssertionError(cause)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cause", choices=CAUSES)
    parser.add_argument("sdk_src", type=Path)
    args = parser.parse_args()
    if not (args.sdk_src / "fern" / "__init__.py").is_file():
        parser.error(f"{args.sdk_src} must contain the generated fern package")
    # The SDK may be a committed golden tree; importing it must not write
    # bytecode beside its files.
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(args.sdk_src.resolve()))
    try:
        sdk = importlib.import_module("fern")
    except Exception as error:  # any import failure is the SDK's, reported as such
        print(f"cannot import the fern package from {args.sdk_src}: {error}", file=sys.stderr)
        return 2
    # Each step runs against its own server, answering with that step's payload.
    for index, (name, _, answers) in enumerate(steps(args.cause, None)):
        with server(answers) as url:
            _, call, _ = steps(args.cause, sdk.FernApi(base_url=url))[index]
            try:
                value = call()
            except Exception as error:  # the step names whatever the SDK raised
                print(f"{name}: the call raised {type(error).__name__}: {error}", file=sys.stderr)
                return 1
            sent(name)
            if value is not None:
                returned(name, value)
    return 0


if __name__ == "__main__":
    sys.exit(main())

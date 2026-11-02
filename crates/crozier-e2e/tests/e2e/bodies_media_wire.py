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
import dataclasses
import enum
import http.server
import importlib
import json
import sys
import threading
from collections.abc import Callable, Iterator
from email import policy
from email.parser import BytesParser
from pathlib import Path
from typing import Any, ClassVar, NamedTuple


class Cause(enum.StrEnum):
    """The measurements whose verdict rests on the wire."""

    CONTENT_TYPE_HEADER = "request-content-type-header"
    MEDIA_TYPE_RECOGNITION = "media-type-recognition"
    MULTIPART_EMPTY_BODY = "multipart-empty-body"
    MULTIPART_SCALAR_UNION = "multipart-scalar-union-part-encoding"
    STREAMING_DETECTION = "streaming-detection"
    GEO_JSON_SUCCESS = "geo-json-success-media"


class Answer(NamedTuple):
    """What the server answers one path with."""

    status: int
    content_type: str
    payload: bytes


NO_CONTENT = Answer(204, "", b"")


@dataclasses.dataclass(frozen=True)
class Recorded:
    """One request the server received."""

    method: str
    path: str
    content_type: str | None
    body: bytes


class Step(NamedTuple):
    """One call: its name, the call itself and the answers the server gives."""

    name: str
    call: Callable[[], Any]
    answers: dict[str, Answer]


class Recorder(http.server.BaseHTTPRequestHandler):
    """Records each request and answers with the response its path is given."""

    seen: ClassVar[list[Recorded]] = []
    answers: ClassVar[dict[str, Answer]] = {}

    def _handle(self) -> None:
        declared = self.headers.get("content-length") or "0"
        # A length that is no non-negative integer is refused rather than read,
        # which could wait for an end of stream the client never sends.
        if not declared.isdigit():
            self.send_error(400, f"invalid Content-Length {declared!r}")
            return
        length = int(declared)
        body = self.rfile.read(length) if length else b""
        self.seen.append(Recorded(self.command, self.path, self.headers.get("content-type"), body))
        answer = self.answers.get(self.path, NO_CONTENT)
        self.send_response(answer.status)
        if answer.content_type:
            self.send_header("content-type", answer.content_type)
        self.send_header("content-length", str(len(answer.payload)))
        self.end_headers()
        self.wfile.write(answer.payload)

    do_GET = do_POST = do_PUT = _handle

    def log_message(self, format: str, *args: object) -> None:
        pass


@contextlib.contextmanager
def server(answers: dict[str, Answer]) -> Iterator[str]:
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
    content_type = request.content_type
    body: Any = request.body.decode() if request.body else None
    if content_type and content_type.startswith("multipart/form-data"):
        body = parts(content_type, request.body)
        content_type = "multipart/form-data"
    line = {"method": request.method, "path": request.path, "content-type": content_type, "body": body}
    print(json.dumps({"step": step, "sent": line}, sort_keys=True))


def described(value: Any) -> Any:
    """A returned value as JSON: a model as its class and fields, a list item by item."""
    if hasattr(value, "model_dump"):
        return {"class": type(value).__name__, **value.model_dump(mode="json", by_alias=True)}
    if isinstance(value, list):
        return [described(item) for item in value]
    return value


def returned(step: str, value: Any) -> None:
    print(json.dumps({"step": step, "returned": described(value)}, sort_keys=True))


# llmlint: ignore[protocol_based_seams] The client is whichever generated SDK the journey imported at runtime, crozier's or the certified pair's; its interface is exactly what the measurement document generates, so no Protocol written here could state it beyond what importing the package already does.
def steps(cause: Cause, client: Any) -> list[Step]:
    """Each step of `cause`: its name, the call, and what the server answers."""
    match cause:
        case Cause.CONTENT_TYPE_HEADER:
            bell = json.dumps({"name": "Great Tom", "note": "E flat"}).encode()
            return [
                Step("tune_bell", lambda: client.bells.tune_bell("tenor", strike_note="D"), {}),
                Step("inscribe_bell", lambda: client.bells.inscribe_bell("tenor", text="Laudo Deum"), {}),
                Step(
                    "create_bell",
                    lambda: client.bells.create_bell(name="Great Tom", note="E flat"),
                    {"/bells": Answer(201, "application/json", bell)},
                ),
                Step("order_cast", lambda: client.casts.order_cast(request={"kind": "handbell", "octaves": 2}), {}),
                Step("add_note", lambda: client.notes.add_note(text="Recast after the crack", author="Founder"), {}),
            ]
        case Cause.MEDIA_TYPE_RECOGNITION:
            deposit = json.dumps({"species": "Malus sieversii", "grams": 12.5}).encode()
            vault = json.dumps({"vaultId": "north", "deposits": 3}).encode()
            return [
                Step(
                    "record_deposit",
                    lambda: client.deposits.record_deposit(species="Malus sieversii", grams=12.5),
                    {"/deposits": Answer(200, "application/json", deposit)},
                ),
                Step(
                    "record_germination",
                    lambda: client.deposits.record_germination("lot-7", sown=40, sprouted=31),
                    {},
                ),
                Step(
                    "get_vault",
                    lambda: client.vaults.get_vault("north"),
                    {"/vaults/north": Answer(200, "application/json", vault)},
                ),
            ]
        case Cause.MULTIPART_EMPTY_BODY:
            return [Step("advance_queue", lambda: client.queue.advance_queue(), {})]
        case Cause.MULTIPART_SCALAR_UNION:
            scan = ("map.tiff", b"II*\x00scan", "image/tiff")
            return [
                Step("file_scan label", lambda: client.scans.file_scan(scan=scan, drawer="A-12"), {}),
                Step("file_scan number", lambda: client.scans.file_scan(scan=scan, drawer=12), {}),
            ]
        case Cause.STREAMING_DETECTION:
            events = b"".join(
                b"data: " + json.dumps({"patternId": "p-1", "rows": rows}).encode() + b"\n\n" for rows in (1, 2)
            )
            return [
                Step(
                    "weave_pattern",
                    lambda: list(client.patterns.weave_pattern(draft="1-2-3", incremental=True)),
                    {"/patterns/weave": Answer(200, "text/event-stream", events)},
                )
            ]
        case Cause.GEO_JSON_SUCCESS:
            feature = json.dumps(
                {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-122.4, 37.8]}, "name": "Ridge"}
            ).encode()
            return [
                Step(
                    "get_trailhead",
                    lambda: client.trailheads.get_trailhead("ridge"),
                    {"/trailheads/ridge": Answer(200, "application/geo+json", feature)},
                )
            ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cause", type=Cause, choices=list(Cause))
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
    # A step's answers decide what the server replies, and the recorder holds
    # only the requests of the step in flight, so each step gets a server of its
    # own and a client bound to that server's address.
    for index, step in enumerate(steps(args.cause, None)):
        with server(step.answers) as url:
            # llmlint: ignore[async_typed_clients_at_boundaries] The synchronous `FernApi` is the generated SDK's public client under test, the one each measurement's runtime.txt records; driving an async client instead would test a different method.
            call = steps(args.cause, sdk.FernApi(base_url=url))[index].call
            try:
                value = call()
            except Exception as error:  # the step names whatever the SDK raised
                print(f"{step.name}: the call raised {type(error).__name__}: {error}", file=sys.stderr)
                return 1
            sent(step.name)
            if value is not None:
                returned(step.name, value)
    return 0


if __name__ == "__main__":
    sys.exit(main())

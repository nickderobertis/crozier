"""Drive the SDK generated from ingef/conquery's registered document through its real async client.

Usage: conquery_secondary_id_wire.py SDK_SRC. SDK_SRC is the `src/` directory of
an SDK generated from tests/fixtures/corpus-sources/ingef-conquery/openapi.yaml
(corpus row 3478), holding the `fern` package. That document's `Query` maps
`SECONDARY_ID_QUERY` to `#/components/schemas/secondary-Id-query`, which names
no component; `SecondaryIdQuery` is the member that tags itself so.

Every request goes over a socket to a local HTTP server that answers with the
payload the journey chose and records what the client sent. The journey reads an
execution status whose `query` is a `SECONDARY_ID_QUERY` as `SecondaryIdQuery`
declares it, expects it to parse into `Query_SecondaryIdQuery` carrying
`SecondaryIdQuery`'s fields, and posts that query back, expecting the server to
receive exactly the payload it sent. A `CONCEPT_QUERY`, whose mapping target
names its component, makes the same round trip as the control.

Exit 0 prints one line per step; exit 1 names the first step that failed; exit
2 reports invalid arguments or an SDK this script cannot import.
"""

import argparse
import asyncio
import contextlib
import http.server
import importlib
import json
import sys
import threading
from collections.abc import Generator
from pathlib import Path
from typing import Any, Literal, NewType, Protocol, TypedDict

ExecutionId = NewType("ExecutionId", str)
"""The `query` path parameter of `GET /queries/{query}`."""

DatasetId = NewType("DatasetId", str)
"""The `dataset` path parameter of `POST /datasets/{dataset}/queries`."""

EXECUTION = ExecutionId("dataset.execution")
DATASET = DatasetId("dataset")


class SecondaryIdQueryWire(TypedDict):
    """A `SecondaryIdQuery` on the wire: the member the dangling target stands for."""

    type: Literal["SECONDARY_ID_QUERY"]
    secondaryId: str
    dateAggregationMode: Literal["MERGE"]


class ConceptQueryWire(TypedDict):
    """A `ConceptQuery` on the wire: the control, whose mapping target names it."""

    type: Literal["CONCEPT_QUERY"]
    dateAggregationMode: Literal["MERGE"]


QueryWire = SecondaryIdQueryWire | ConceptQueryWire


class ExecutionStatusWire(TypedDict):
    """A `FullExecutionStatus` as the server answers it."""

    id: ExecutionId
    query: QueryWire


SECONDARY_ID: SecondaryIdQueryWire = {
    "type": "SECONDARY_ID_QUERY",
    "secondaryId": "dataset.sid",
    "dateAggregationMode": "MERGE",
}
CONCEPT: ConceptQueryWire = {"type": "CONCEPT_QUERY", "dateAggregationMode": "MERGE"}

# Each wire key the journey reads back off the parsed wrapper, by its Python name.
FIELD_NAMES = {"secondaryId": "secondary_id", "dateAggregationMode": "date_aggregation_mode"}


class ExecutionStatus(Protocol):
    """The part of a generated `FullExecutionStatus` the journey reads."""

    query: object


class QueryClient(Protocol):
    """The two operations of the generated `AsyncFernApi.query` the journey drives."""

    async def get_query_status(self, query: ExecutionId) -> ExecutionStatus: ...

    async def post_query(self, dataset: DatasetId, *, request: object) -> object: ...


class Failure(Exception):
    """A step whose observed behaviour is not the one the measurement states."""


def check(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


class Server:
    """A local HTTP server answering every GET with `answer` and recording each POST body."""

    def __init__(self) -> None:
        self.answer: ExecutionStatusWire | None = None
        self.received: list[Any] = []
        outer = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def log_message(self, format: str, *args: object) -> None:
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
                self.reply({"id": EXECUTION})

        self.httpd = http.server.HTTPServer(("127.0.0.1", 0), Handler)

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.httpd.server_port}"


@contextlib.contextmanager
def serving() -> Generator[Server]:
    server = Server()
    thread = threading.Thread(target=server.httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield server
    finally:
        server.httpd.shutdown()
        server.httpd.server_close()


def wire_value(value: object) -> object:
    """A parsed field's value as the wire spells it: an enum member by its value."""
    return getattr(value, "value", value)


async def round_trip(client: QueryClient, server: Server, query: QueryWire, wrapper: str) -> str:
    """Read an execution status holding `query`, then post its query back unchanged."""
    server.answer = {"id": EXECUTION, "query": query}
    try:
        status = await client.get_query_status(EXECUTION)
    except Exception as error:
        # Whatever the SDK raises while parsing is the observation.
        last = " | ".join(str(error).splitlines()[-3:])
        raise Failure(f"{query['type']}: reading the status raised {type(error).__name__}: {last}") from error
    parsed = status.query
    check(type(parsed).__name__ == wrapper, f"{query['type']}: parsed as {type(parsed).__name__}, not {wrapper}")
    for wire, value in query.items():
        if wire == "type":
            continue
        got = wire_value(getattr(parsed, FIELD_NAMES[wire], None))
        check(got == value, f"{query['type']}: {wrapper}.{FIELD_NAMES[wire]} is {got!r}, not {value!r}")
    await client.post_query(DATASET, request=parsed)
    sent = server.received[-1]
    check(sent == query, f"{query['type']}: posting it back sent {json.dumps(sent, sort_keys=True)}")
    return f"{query['type']}: parsed into {wrapper} and posted back as {json.dumps(sent, sort_keys=True)}"


async def journey(client: QueryClient, server: Server) -> None:
    """The `CONCEPT_QUERY` control's round trip, then the `SECONDARY_ID_QUERY` one."""
    for query, wrapper in ((CONCEPT, "Query_ConceptQuery"), (SECONDARY_ID, "Query_SecondaryIdQuery")):
        print(await round_trip(client, server, query, wrapper))


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
        client_class = sdk.AsyncFernApi
    except (ImportError, AttributeError) as error:
        print(f"cannot import the generated fern package's AsyncFernApi: {error}", file=sys.stderr)
        return 2
    with serving() as server:
        client: QueryClient = client_class(base_url=server.url, username="user", password="secret").query
        try:
            asyncio.run(journey(client, server))
        except Failure as failure:
            print(f"failed: {failure}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

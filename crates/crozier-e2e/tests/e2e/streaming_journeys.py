"""Drive a crozier-generated SDK's streaming methods, sync and async.

Usage: streaming_journeys.py <fixture> <generated SDK src directory>

Each journey serves real response bodies -- Server-Sent Events, newline-delimited
JSON or raw bytes -- through httpx's transport boundary to the generated client
of one streaming fixture. It checks what each method sends, what it yields or
returns, that a declared stream end stops it, and that an error status raises
`ApiError` with the next call recovering. Nothing of crozier's or of the
generated SDK is replaced: the clients are constructed with an `httpx` client
whose transport is the local handler. Prints `<fixture>: ok` and exits 0 when
every assertion holds.
"""

import asyncio
import json
import sys

import httpx

USAGE = "usage: streaming_journeys.py <fixture> <generated SDK src directory>"
if len(sys.argv) != 3:
    sys.exit(USAGE)
FIXTURE, SRC = sys.argv[1:]
sys.path.insert(0, SRC)

import fern  # noqa: E402 - importable once the SDK's src is on sys.path
from fern.core.api_error import ApiError  # noqa: E402

BASE = "https://stream.test"


def answer(*args, **kwargs):
    """A response built afresh for each request, as a server answers."""
    return lambda request: httpx.Response(*args, **kwargs)


def sse(*events):
    """A `text/event-stream` body: each event is `data` or `(event, data)`."""
    lines = []
    for event in events:
        name, data = event if isinstance(event, tuple) else (None, event)
        if name:
            lines.append(f"event: {name}")
        lines.append(f"data: {data if isinstance(data, str) else json.dumps(data)}")
        lines.append("")
    return answer(200, headers={"content-type": "text/event-stream"}, text="\n".join(lines) + "\n")


def json_lines(*lines):
    return answer(200, headers={"content-type": "application/json"}, text="\n".join(lines) + "\n")


def failure(request):
    return httpx.Response(400, json={"message": "rejected"})


class Wire:
    """The local transport: answers each request in turn and records it."""

    def __init__(self, *answers):
        self.answers = list(answers)
        self.sent = []

    def __call__(self, request):
        body = request.content
        self.sent.append(
            {
                "method": request.method,
                "path": request.url.path,
                "query": dict(request.url.params),
                "content_type": request.headers.get("content-type"),
                "json": json.loads(body) if body else None,
            }
        )
        return self.answers.pop(0)(request)


def sync_client(wire):
    return fern.FernApi(base_url=BASE, max_retries=0, httpx_client=httpx.Client(transport=httpx.MockTransport(wire)))


def async_client(wire):
    return fern.AsyncFernApi(
        base_url=BASE, max_retries=0, httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(wire))
    )


def both(call, *answers, collect=list):
    """Run `call(client)` with the sync client and then the async one, each against
    its own copy of `answers`; return both results and both wires."""
    sync_wire = Wire(*answers)
    sync_result = collect(call(sync_client(sync_wire)))

    async def drive():
        wire = Wire(*answers)
        result = call(async_client(wire))
        if hasattr(result, "__aiter__"):
            result = [chunk async for chunk in result]
        else:
            result = await result
        return result, wire

    async_result, async_wire = asyncio.run(drive())
    return (sync_result, sync_wire), (async_result, async_wire)


def raises_then_recovers(call, recovered, success):
    """A 400 raises `ApiError` carrying the body; the next call on the same client
    succeeds with `recovered(result)` true -- sync and async."""
    wire = Wire(failure, success)
    client = sync_client(wire)
    try:
        list(call(client))
    except ApiError as error:
        assert error.status_code == 400 and error.body == {"message": "rejected"}, error
    else:
        raise AssertionError("a 400 did not raise")
    assert recovered(list(call(client)))

    async def drive():
        wire = Wire(failure, success)
        client = async_client(wire)
        try:
            [chunk async for chunk in call(client)]
        except ApiError as error:
            assert error.status_code == 400 and error.body == {"message": "rejected"}, error
        else:
            raise AssertionError("a 400 did not raise (async)")
        assert recovered([chunk async for chunk in call(client)])

    asyncio.run(drive())


def terminator():
    events = sse({"step": "lint", "passed": True}, {"step": "test", "passed": False}, "[DONE]", {"step": "late"})
    call = lambda client: client.follow_build_log("b-1")
    for chunks, wire in both(call, events):
        # The declared terminator ends the stream; the event after it is never read.
        assert [(chunk.step, chunk.passed) for chunk in chunks] == [("lint", True), ("test", False)], chunks
        assert wire.sent[0]["path"] == "/builds/b-1/log", wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 2, events)


def sse_format():
    # `format: sse` over a JSON-only success: the body is decoded as events.
    events = sse({"pm25": 4.5, "pm10": 9.0}, {"pm25": 5.0})
    call = lambda client: client.subscribe_readings("s-7")
    for chunks, wire in both(call, events):
        assert [(chunk.pm25, chunk.pm10) for chunk in chunks] == [(4.5, 9.0), (5.0, None)], chunks
        assert wire.sent[0]["path"] == "/sensors/s-7/readings", wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 2, events)


def boolean():
    # `x-fern-streaming: true` streams JSON lines: a blank line and one that is
    # not JSON are skipped.
    lines = json_lines('{"level": "info", "message": "up"}', "", "not json", '{"level": "warn", "message": "slow"}')
    call = lambda client: client.tail_logs(service="api")
    for chunks, wire in both(call, lines):
        assert [(chunk.level, chunk.message) for chunk in chunks] == [("info", "up"), ("warn", "slow")], chunks
        assert wire.sent[0]["query"] == {"service": "api"}, wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 2, lines)


def event_dispatch():
    # Each event's `event` field selects the model its JSON `data` parses as; an
    # event no branch names is skipped.
    events = sse(
        ("departed", {"data": {"terminal": "North", "minutesLate": 3}}),
        ("docked", {"data": {"terminal": "nowhere"}}),
        ("arrived", {"data": {"terminal": "South"}}),
    )
    call = lambda client: client.watch_movements("r-2")
    for chunks, wire in both(call, events):
        assert [type(chunk).__name__ for chunk in chunks] == ["Departure", "Arrival"], chunks
        assert [chunk.data.terminal for chunk in chunks] == ["North", "South"], chunks
        assert chunks[0].data.minutes_late == 3, chunks
        assert wire.sent[0]["path"] == "/routes/r-2/movements", wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 2, events)


def const_tagged_union():
    # The inline const-tagged `oneOf` is a discriminated union on `trend`.
    events = sse({"trend": "flood", "height": 1.25}, {"trend": "ebb", "height": 0.5, "slack": True})
    call = lambda client: client.stations.follow_levels("st-1")
    for chunks, wire in both(call, events):
        assert [type(chunk).__name__ for chunk in chunks] == ["FollowLevelsResponse_Flood", "FollowLevelsResponse_Ebb"]
        assert (chunks[0].height, chunks[1].slack) == (1.25, True), chunks
        assert wire.sent[0]["path"] == "/stations/st-1/levels", wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 2, events)


def item_schema():
    # `itemSchema` types each event.
    events = sse({"altitude": 1200.5, "pressure": 880.0}, {"altitude": 1300.0})
    call = lambda client: client.stream_samples("bal-9")
    for chunks, wire in both(call, events):
        assert [(chunk.altitude, chunk.pressure) for chunk in chunks] == [(1200.5, 880.0), (1300.0, None)], chunks
        assert wire.sent[0]["path"] == "/balloons/bal-9/samples", wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 2, events)


def binary_download():
    # A binary event-stream schema downloads as bytes, not events.
    payload = b"RIFF\x00\x01frames-and-more-frames"
    download = answer(200, headers={"content-type": "text/event-stream"}, content=payload)
    call = lambda client: client.listen_live(channel=3)
    for chunks, wire in both(call, download):
        assert b"".join(chunks) == payload, chunks
        assert wire.sent[0]["query"] == {"channel": "3"}, wire.sent
    raises_then_recovers(call, lambda chunks: b"".join(chunks) == payload, download)


def ref_body_header():
    # Both halves fix the condition field. The JSON content-type the halves now
    # pass explicitly is the one httpx would send for `json=` anyway, so the
    # header is the byte golden's to prove; this proves the two halves end to end.
    events = sse({"hex": "#aa0000"}, {"hex": "#bb0000"})
    call = lambda client: client.blend_stream(pigments=["red"])
    for chunks, wire in both(call, events):
        assert [chunk.hex for chunk in chunks] == ["#aa0000", "#bb0000"], chunks
        assert wire.sent[0]["json"] == {"pigments": ["red"], "preview": True}, wire.sent
        assert wire.sent[0]["content_type"] == "application/json", wire.sent
    buffered = answer(200, json={"hex": "#cc0000"})
    for swatch, wire in both(lambda client: client.blend(pigments=["blue"]), buffered, collect=lambda x: x):
        assert swatch.hex == "#cc0000", swatch
        assert wire.sent[0]["json"] == {"pigments": ["blue"], "preview": False}, wire.sent
        assert wire.sent[0]["content_type"] == "application/json", wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 2, events)


def shared_body():
    # The shared body is flattened on all three methods, and no model of it is
    # exported, as Fern drops a body schema a buffered operation also posts.
    assert not hasattr(fern, "PlanRequestBody"), "the shared body model is exported"
    events = sse({"legs": 2}, {"legs": 3})
    call = lambda client: client.plan_stream(origin="Oslo", destination="Bergen")
    for chunks, wire in both(call, events):
        assert [chunk.legs for chunk in chunks] == [2, 3], chunks
        assert wire.sent[0]["json"] == {"origin": "Oslo", "destination": "Bergen", "progressive": True}, wire.sent
        assert wire.sent[0]["content_type"] == "application/json", wire.sent
    buffered = answer(200, json={"legs": 4})
    for method, progressive in (("plan", False), ("estimate_route", None)):
        call_buffered = lambda client: getattr(client, method)(origin="Oslo")
        for itinerary, wire in both(call_buffered, buffered, collect=lambda x: x):
            assert itinerary.legs == 4, itinerary
            expected = {"origin": "Oslo"} if progressive is None else {"origin": "Oslo", "progressive": progressive}
            assert wire.sent[0]["json"] == expected, wire.sent
            assert wire.sent[0]["content_type"] == "application/json", wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 2, events)


def union_body():
    # Each half takes its own alias of the component union and sends the member.
    import inspect

    from fern import Crate, EstimateRequest, EstimateStreamRequest

    for method, alias in ((fern.FernApi.estimate_stream, EstimateStreamRequest), (fern.FernApi.estimate, EstimateRequest)):
        assert inspect.signature(method).parameters["request"].annotation == alias, method
    events = sse({"cents": 1250})
    call = lambda client: client.estimate_stream(request=Crate(kilograms=2.5))
    for chunks, wire in both(call, events):
        assert [chunk.cents for chunk in chunks] == [1250], chunks
        assert wire.sent[0]["json"] == {"kilograms": 2.5}, wire.sent
    buffered = answer(200, json={"cents": 990})
    for estimate, wire in both(lambda client: client.estimate(request="TRK-1"), buffered, collect=lambda x: x):
        assert estimate.cents == 990, estimate
        assert wire.sent[0]["json"] == "TRK-1", wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 1, events)


def private_gpt():
    # A stream-condition without `format` streams JSON lines; the buffered half
    # returns the model; each sends its value of the condition.
    def completion(text):
        return {"id": "c-1", "object": "completion.chunk", "created": 1, "model": "private-gpt",
                "choices": [{"delta": {"content": text}, "index": 0}]}

    lines = json_lines(json.dumps(completion("Hel")), json.dumps(completion("lo")))
    completions = lambda client: client.contextual_completions
    call = lambda client: completions(client).prompt_completion_v1completions_post_stream(prompt="Hi")
    for chunks, wire in both(call, lines):
        assert [chunk.choices[0].delta.content for chunk in chunks] == ["Hel", "lo"], chunks
        assert wire.sent[0]["path"] == "/v1/completions", wire.sent
        assert wire.sent[0]["json"] == {"prompt": "Hi", "stream": True}, wire.sent
    buffered = answer(200, json={**completion("Hello"), "object": "completion"})
    call_buffered = lambda client: completions(client).prompt_completion(prompt="Hi")
    for result, wire in both(call_buffered, buffered, collect=lambda x: x):
        assert result.choices[0].delta.content == "Hello", result
        assert wire.sent[0]["json"] == {"prompt": "Hi", "stream": False}, wire.sent
    raises_then_recovers(call, lambda chunks: len(chunks) == 2, lines)


JOURNEYS = {
    "streaming-extension-terminator": terminator,
    "streaming-extension-sse-format": sse_format,
    "streaming-extension-boolean": boolean,
    "event-stream-event-dispatch": event_dispatch,
    "event-stream-const-tagged-union": const_tagged_union,
    "event-stream-item-schema": item_schema,
    "event-stream-binary-download": binary_download,
    "stream-condition-ref-body-header": ref_body_header,
    "stream-condition-shared-body": shared_body,
    "stream-condition-union-body": union_body,
    "zylon-private-gpt": private_gpt,
}

if FIXTURE not in JOURNEYS:
    sys.exit(f"{FIXTURE}: no streaming journey; choose one of {sorted(JOURNEYS)}\n{USAGE}")
JOURNEYS[FIXTURE]()
print(f"{FIXTURE}: ok")

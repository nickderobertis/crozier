"""Record the runtime ("wire") behavior of a generated Python SDK.

This is a *helper*, not a test module (pytest imports it for the journey list;
`test_wire.py` runs it as a subprocess to record each SDK's behavior and compares
the recordings). The generated client accepts an `httpx_client`, so each journey
injects one whose `httpx.MockTransport` captures the outgoing request and returns
a scripted response — exercising URL/method construction, header injection,
request-body serialization (field aliasing and `OMIT` filtering), query encoding,
typed pydantic deserialization, and typed error raising, for the sync and async
clients. It records, per journey, the request (method, URL, canonicalized headers,
body) and the outcome (the response model dumped to a dict, or the typed error's
class/status/body).

The SDK is imported *lazily* (inside `load_sdk`, from the path in `WIRE_SDK_SRC`)
so that importing this module to read `JOURNEY_NAMES` never touches a generated
`fern` package — the two SDKs under comparison are both named `fern` and cannot
coexist in one process, which is why the recording runs one SDK per subprocess.
The only third-party imports are the SDK's own runtime deps (`httpx`, `pydantic`).
A journey that cannot complete its structural contract (e.g. a declared 4xx that
fails to raise) raises, so a broken journey fails loudly instead of recording
nothing and matching trivially.
"""

import asyncio
import json
import os
import sys
from types import SimpleNamespace
from typing import Any, Protocol

import httpx

BASE_URL = "https://api.example.test"
TOKEN = "secret-token"


def load_sdk(src):
    """Put the generated SDK's `src/` on the path and import the symbols the
    journeys need. Deferred so this module is importable without an SDK present."""
    sys.path.insert(0, src)
    from fern import AsyncFernApi, FernApi
    from fern.errors.bad_request_error import BadRequestError

    return SimpleNamespace(FernApi=FernApi, AsyncFernApi=AsyncFernApi, BadRequestError=BadRequestError)


def _capture(status, payload):
    """A MockTransport that records the request it receives and replies with a
    scripted status + JSON body. Returns (transport, box) where box["request"]
    holds the captured httpx.Request after the call."""
    box = {}

    def handler(request):
        box["request"] = request
        return httpx.Response(status, json=payload)

    return httpx.MockTransport(handler), box


def _canonical_headers(headers):
    """Normalize request headers to the behavior we mean to compare, applied
    identically to both SDKs. Lower-case the names (httpx lookup is
    case-insensitive) and neutralize the one deliberate difference: crozier brands
    its SDK-identity headers `X-Crozier-*` where Fern uses `X-Fern-*` (otherwise
    identical values). Everything outside SDK identity — auth, content-type,
    and httpx's own headers — must match verbatim."""
    out = {}
    for name, value in headers.items():
        key = name.lower()
        for prefix in ("x-fern-", "x-crozier-"):
            if key.startswith(prefix):
                key = "x-sdk-" + key[len(prefix) :]
                break
        out[key] = value
    return out


def _body(request):
    """The request body as JSON when it is JSON, else the raw text, else None."""
    content = request.content
    if not content:
        return None
    try:
        return json.loads(content)
    except (ValueError, UnicodeDecodeError):
        return content.decode("utf-8", "replace")


def _request_record(request):
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": _canonical_headers(request.headers),
        "body": _body(request),
    }


def _dump(model):
    """Dump a generated pydantic model to a plain dict, on pydantic v1 or v2."""
    if hasattr(model, "model_dump"):
        return model.model_dump()
    return model.dict()


def _sync_client(sdk, status, payload, *, token=TOKEN):
    transport, box = _capture(status, payload)
    client = sdk.FernApi(base_url=BASE_URL, token=token, httpx_client=httpx.Client(transport=transport))
    return client, box


def _workspace_payload(name="Dispatch desk"):
    return {
        "customerId": "customer-a",
        "workspaceId": "workspace-a",
        "initialSetupComplete": True,
        "name": name,
        "slug": "dispatch-desk",
    }


def request_construction_and_response(sdk):
    """An inline object body aliases snake-case fields and omits unset fields;
    bearer auth and a typed response travel through the compiled SDK."""
    client, box = _sync_client(sdk, 200, _workspace_payload())
    result = client.workspace.create_workspace(
        name="Dispatch desk", anonymous_data_collection=False, security_updates=True
    )
    request = box["request"]
    assert request.method == "POST"
    assert request.url.path == "/v1/workspaces/create"
    assert _body(request) == {"name": "Dispatch desk", "anonymousDataCollection": False, "securityUpdates": True}
    assert request.headers["authorization"] == f"Bearer {TOKEN}"
    assert result.workspace_id == "workspace-a"
    return {
        "request": _request_record(request),
        "outcome": {"model": type(result).__name__, "data": _dump(result)},
    }


def no_auth_omits_authorization(sdk):
    """The API's optional bearer token may be absent; the request still runs."""
    client, box = _sync_client(sdk, 200, _workspace_payload(), token=None)
    result = client.workspace.get_workspace(workspace_id="workspace-a")
    assert "authorization" not in box["request"].headers
    return {
        "request": _request_record(box["request"]),
        "outcome": {"model": type(result).__name__, "data": _dump(result)},
    }


def typed_error_is_raised(sdk):
    """A declared 400 raises a typed exception containing a parsed error model."""
    client, box = _sync_client(
        sdk, 400, {"message": "invalid workspace", "exceptionClassName": "InvalidWorkspace"}, token=None
    )
    try:
        client.source_oauth.set_instancewide_source_oauth_params(params={}, source_definition_id="source-a")
    except sdk.BadRequestError as err:
        assert err.body.message == "invalid workspace"
        assert err.body.exception_class_name == "InvalidWorkspace"
        return {
            "request": _request_record(box["request"]),
            "outcome": {"error": type(err).__name__, "status": err.status_code, "body": _dump(err.body)},
        }
    raise AssertionError("expected BadRequestError for a 400 response, none raised")


def query_parameters_are_encoded(sdk):
    """Request options encode additional query parameters onto the URL."""
    client, box = _sync_client(sdk, 200, _workspace_payload())
    result = client.workspace.get_workspace(
        workspace_id="workspace-a",
        request_options={"additional_query_parameters": {"cursor": "dock & bay", "limit": 10}},
    )
    assert dict(box["request"].url.params) == {"cursor": "dock & bay", "limit": "10"}
    assert _body(box["request"]) == {"workspaceId": "workspace-a"}
    return {
        "request": _request_record(box["request"]),
        "outcome": {"model": type(result).__name__, "data": _dump(result)},
    }


def raw_response_exposes_underlying_http(sdk):
    """Raw response access preserves the parsed model and response headers."""
    client, box = _sync_client(sdk, 200, _workspace_payload())
    raw = client.workspace.with_raw_response.get_workspace(workspace_id="workspace-a")
    if not isinstance(raw.headers, dict):
        raise AssertionError(f"raw response headers should be a dict, got {type(raw.headers)}")
    assert raw.data.workspace_id == "workspace-a"
    return {
        "request": _request_record(box["request"]),
        "outcome": {"model": type(raw.data).__name__, "data": _dump(raw.data)},
    }


def async_request_and_response(sdk):
    """The async client aliases the same body fields and parses the response."""

    async def run():
        transport, box = _capture(200, _workspace_payload())
        client = sdk.AsyncFernApi(base_url=BASE_URL, token=TOKEN, httpx_client=httpx.AsyncClient(transport=transport))
        result = await client.workspace.create_workspace(name="Dispatch desk", security_updates=True)
        assert _body(box["request"]) == {"name": "Dispatch desk", "securityUpdates": True}
        assert result.workspace_id == "workspace-a"
        return {
            "request": _request_record(box["request"]),
            "outcome": {"model": type(result).__name__, "data": _dump(result)},
        }

    return asyncio.run(run())


def path_dot_segments_are_rejected(sdk):
    """A path parameter of `.` or `..` (or a segment of one, encoded or not)
    raises before any request is built; any other value is encoded as before."""
    from fern.core.jsonable_encoder import encode_path_param, quote_path_param

    observed = {}
    for function in (encode_path_param, quote_path_param):
        for value in ("..", ".", "a/../b", "%2e%2e", "dock.7", True):
            try:
                observed[f"{function.__name__}({value!r})"] = {"value": function(value)}
            except ValueError as err:
                observed[f"{function.__name__}({value!r})"] = {"error": type(err).__name__, "message": str(err)}
    for rejected in ("encode_path_param('..')", "quote_path_param('..')", "quote_path_param('.')"):
        if "error" not in observed[rejected]:
            raise AssertionError(f"{rejected} should raise ValueError, got {observed[rejected]}")
    return observed


def retry_after_header_values(sdk):
    """`retry-after-ms` is read as a number of milliseconds, fractions included;
    a value that is not a positive finite number falls back to `retry-after`. A
    429 carrying one is retried by the real client and then succeeds."""
    from fern.core.http_client import _parse_retry_after

    parsed = {}
    for value in ("1500", "1.5", "0", "-5", "inf", "nan", "soon"):
        headers = httpx.Headers({"retry-after-ms": value, "retry-after": "7"})
        parsed[value] = _parse_retry_after(headers)
    if parsed["1.5"] != 0.0015 or parsed["1500"] != 1.5 or parsed["soon"] != 7:
        raise AssertionError(f"retry-after-ms values parsed as {parsed}")

    replies = iter(
        [
            httpx.Response(429, headers={"retry-after-ms": "1.5"}, json={"message": "slow down"}),
            httpx.Response(200, json=_workspace_payload()),
        ]
    )
    requests = []

    def handler(request):
        requests.append(request)
        return next(replies)

    client = sdk.FernApi(
        base_url=BASE_URL, token=TOKEN, httpx_client=httpx.Client(transport=httpx.MockTransport(handler))
    )
    result = client.workspace.get_workspace(workspace_id="workspace-a", request_options={"max_retries": 1})
    if len(requests) != 2:
        raise AssertionError(f"a 429 with retry-after-ms should be retried once, saw {len(requests)} request(s)")
    return {
        "parsed": parsed,
        "requests": [_request_record(request) for request in requests],
        "outcome": {"model": type(result).__name__, "data": _dump(result)},
    }


def environment_proxy_mounts(sdk):
    """The environment's proxies become keepalive transport mounts, sync and
    async; a NO_PROXY host is a `None` mount that falls back to the default."""
    from fern.core.http_client import get_async_keepalive_proxy_mounts, get_keepalive_proxy_mounts

    names = ("HTTPS_PROXY", "HTTP_PROXY", "ALL_PROXY", "NO_PROXY", "https_proxy", "http_proxy", "all_proxy", "no_proxy")
    saved = {name: os.environ.pop(name) for name in names if name in os.environ}
    try:
        os.environ["HTTPS_PROXY"] = "http://proxy.example.test:3128"
        os.environ["NO_PROXY"] = "internal.example.test"
        mounts = {
            "sync": get_keepalive_proxy_mounts(),
            "async": get_async_keepalive_proxy_mounts(),
        }
    finally:
        for name in names:
            os.environ.pop(name, None)
        os.environ.update(saved)
    observed = {
        side: {pattern: None if transport is None else type(transport).__name__ for pattern, transport in found.items()}
        for side, found in mounts.items()
    }
    if observed["sync"].get("https://") != "HTTPTransport" or observed["async"].get("https://") != "AsyncHTTPTransport":
        raise AssertionError(f"HTTPS_PROXY should mount a keepalive transport, got {observed}")
    if "all://*internal.example.test" not in observed["sync"]:
        raise AssertionError(f"NO_PROXY should mount a bypass, got {observed}")
    return observed


def local_forward_refs_resolve(sdk):
    """`update_forward_refs` resolves a forward reference to a model passed as a
    local name, as a generated recursive or late-declared model does."""
    from fern.core.pydantic_utilities import UniversalBaseModel, update_forward_refs

    def declare():
        class Berth(UniversalBaseModel):
            name: str
            moored: "Vessel | None" = None

        class Vessel(UniversalBaseModel):
            hull: str

        return Berth, Vessel

    berth_type, vessel_type = declare()
    update_forward_refs(berth_type, Vessel=vessel_type)
    berth = berth_type(name="north", moored={"hull": "steel"})
    if type(berth.moored).__name__ != "Vessel":
        raise AssertionError(f"the forward reference did not resolve: {berth!r}")
    return {"model": type(berth).__name__, "data": _dump(berth)}


JOURNEYS = [
    request_construction_and_response,
    no_auth_omits_authorization,
    typed_error_is_raised,
    query_parameters_are_encoded,
    raw_response_exposes_underlying_http,
    async_request_and_response,
    path_dot_segments_are_rejected,
    retry_after_header_values,
    environment_proxy_mounts,
    local_forward_refs_resolve,
]
JOURNEY_NAMES = [journey.__name__ for journey in JOURNEYS]


# The header/body collision SDK: `docs/fern-measurements/bodies-responses/header-body-collision/`,
# whose operations each send a header and a body property under one wire name
# (`kilnToken`, `batchLabel`). The method renames the body argument, and each
# value must still reach its own place: the header's in the header, the body
# argument's in the JSON body.
HEADER_VALUE = "header-value"
BODY_VALUE = "body-value"


class CollisionSdk(Protocol):
    """What the collision journeys use of an SDK, Fern's or crozier's alike.

    Each member is a class of a generated package imported at run time from
    `WIRE_SDK_SRC`, which no checker can see when this module is checked, and
    the two SDKs under comparison declare them separately; so their types are
    `Any` here, and the journeys' own assertions check what each returns."""

    FernApi: Any
    AsyncFernApi: Any
    ApiError: Any


def load_collision_sdk(src) -> CollisionSdk:
    """Import the collision SDK's clients and error base from its `src/`."""
    sys.path.insert(0, src)
    from fern import AsyncFernApi, FernApi
    from fern.core.api_error import ApiError

    return SimpleNamespace(FernApi=FernApi, AsyncFernApi=AsyncFernApi, ApiError=ApiError)


def _collision_record(request, header):
    """The request, after checking each value reached its own wire place."""
    if request.headers.get(header) != HEADER_VALUE:
        raise AssertionError(f"{header} header carries {request.headers.get(header)!r}, not {HEADER_VALUE!r}")
    body = _body(request)
    if not isinstance(body, dict) or body.get(header) != BODY_VALUE:
        raise AssertionError(f"the JSON body's {header} is {body!r}, not {BODY_VALUE!r}")
    return _request_record(request)


def header_and_body_keep_their_values(sdk: CollisionSdk):
    """An optional header and a component body property sharing `kilnToken`, and
    a required header and an inline body property sharing `batchLabel`, each send
    the header argument as the header and the renamed body argument in the body."""
    transport, box = _capture(200, {"status": "ran"})
    client = sdk.FernApi(base_url=BASE_URL, httpx_client=httpx.Client(transport=transport))
    ran = client.actions.run_action(action="fire", kiln_token=HEADER_VALUE, run_action_request_kiln_token=BODY_VALUE)
    run = _collision_record(box["request"], "kilnToken")
    queued = client.actions.queue_action(
        action="cool", batch_label=HEADER_VALUE, queue_action_request_batch_label=BODY_VALUE
    )
    queue = _collision_record(box["request"], "batchLabel")
    return {"run": run, "run_status": ran.status, "queue": queue, "queue_status": queued.status}


def async_header_and_body_keep_their_values(sdk: CollisionSdk):
    """The async client binds both values the same way."""
    transport, box = _capture(200, {"status": "ran"})
    client = sdk.AsyncFernApi(base_url=BASE_URL, httpx_client=httpx.AsyncClient(transport=transport))

    async def go():
        ran = await client.actions.run_action(
            action="fire", kiln_token=HEADER_VALUE, run_action_request_kiln_token=BODY_VALUE
        )
        run = _collision_record(box["request"], "kilnToken")
        queued = await client.actions.queue_action(
            action="cool", batch_label=HEADER_VALUE, queue_action_request_batch_label=BODY_VALUE
        )
        return {
            "run": run,
            "run_status": ran.status,
            "queue": _collision_record(box["request"], "batchLabel"),
            "queue_status": queued.status,
        }

    return asyncio.run(go())


def collision_error_then_recovery(sdk: CollisionSdk):
    """A 400 raises the API error with the values sent in their places, and the
    next request on the same client succeeds."""
    calls = []

    def handler(request):
        calls.append(request)
        if len(calls) == 1:
            return httpx.Response(400, json={"detail": "rejected"})
        return httpx.Response(200, json={"status": "ran"})

    client = sdk.FernApi(base_url=BASE_URL, httpx_client=httpx.Client(transport=httpx.MockTransport(handler)))
    try:
        client.actions.run_action(action="fire", kiln_token=HEADER_VALUE, run_action_request_kiln_token=BODY_VALUE)
    except sdk.ApiError as error:
        failed = {"status": error.status_code, "body": error.body}
    else:
        raise AssertionError("a 400 did not raise")
    recovered = client.actions.run_action(
        action="fire", kiln_token=HEADER_VALUE, run_action_request_kiln_token=BODY_VALUE
    )
    return {
        "failed": failed,
        "failed_request": _collision_record(calls[0], "kilnToken"),
        "recovered": recovered.status,
        "recovered_request": _collision_record(calls[1], "kilnToken"),
    }


def shared_body_header_collision(sdk: CollisionSdk):
    """A nullable `Idempotency-Key` header beside a shared component body's
    `idempotency_key`, sync and async. Recorded as sent, without a verdict: the
    certified pair sends the header's variable as the body value (the
    `body-query-parameter-value` departure), and the test holds each SDK to what
    it is known to send."""
    transport, box = _capture(200, {"status": "ran"})
    client = sdk.FernApi(base_url=BASE_URL, httpx_client=httpx.Client(transport=transport))
    client.actions.run_action_batch(
        actions=["fire"], idempotency_key=HEADER_VALUE, action_batch_request_idempotency_key=BODY_VALUE
    )
    sync = _request_record(box["request"])
    transport, box = _capture(200, {"status": "ran"})
    async_client = sdk.AsyncFernApi(base_url=BASE_URL, httpx_client=httpx.AsyncClient(transport=transport))
    asyncio.run(
        async_client.actions.run_action_batch(
            actions=["fire"], idempotency_key=HEADER_VALUE, action_batch_request_idempotency_key=BODY_VALUE
        )
    )
    return {"sync": sync, "async": _request_record(box["request"])}


COLLISION_JOURNEYS = [
    header_and_body_keep_their_values,
    async_header_and_body_keep_their_values,
    collision_error_then_recovery,
    shared_body_header_collision,
]
COLLISION_JOURNEY_NAMES = [journey.__name__ for journey in COLLISION_JOURNEYS]


def record(src):
    """Run every journey against the SDK at `src` and return the recording dict."""
    sdk = load_sdk(src)
    return {journey.__name__: journey(sdk) for journey in JOURNEYS}


def record_collision(src):
    """Run every collision journey against the collision SDK at `src`."""
    sdk = load_collision_sdk(src)
    return {journey.__name__: journey(sdk) for journey in COLLISION_JOURNEYS}


def main():
    src = os.environ.get("WIRE_SDK_SRC")
    if not src:
        print("WIRE_SDK_SRC is not set (path to the generated SDK's src/ dir)", file=sys.stderr)
        sys.exit(2)
    recorders = {"": record, "header-body-collision": record_collision}
    selected = os.environ.get("WIRE_JOURNEYS", "")
    if selected not in recorders:
        print(
            f"WIRE_JOURNEYS={selected!r} names no journey set; use one of {sorted(name for name in recorders if name)}"
            " or leave it unset for the default journeys",
            file=sys.stderr,
        )
        sys.exit(2)
    recorder = recorders[selected]
    json.dump(recorder(src), sys.stdout, indent=2, sort_keys=True, default=str)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

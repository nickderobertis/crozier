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


JOURNEYS = [
    request_construction_and_response,
    no_auth_omits_authorization,
    typed_error_is_raised,
    query_parameters_are_encoded,
    raw_response_exposes_underlying_http,
    async_request_and_response,
]
JOURNEY_NAMES = [journey.__name__ for journey in JOURNEYS]


def record(src):
    """Run every journey against the SDK at `src` and return the recording dict."""
    sdk = load_sdk(src)
    return {journey.__name__: journey(sdk) for journey in JOURNEYS}


def main():
    src = os.environ.get("WIRE_SDK_SRC")
    if not src:
        print("WIRE_SDK_SRC is not set (path to the generated SDK's src/ dir)", file=sys.stderr)
        sys.exit(2)
    json.dump(record(src), sys.stdout, indent=2, sort_keys=True, default=str)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

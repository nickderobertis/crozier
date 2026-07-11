"""Record the runtime ("wire") behavior of a generated Python SDK.

Byte-matching Fern proves the generated *source* is right and `compileall`
proves it is valid Python; this proves the compiled client *behaves* right when
imported and called. Rather than hand-assert expected values, this driver
*records* what the client does and the Rust e2e harness (`tests/e2e.rs`) runs it
against **both** the committed Fern fixture SDK and the crozier-generated SDK and
asserts the two recordings are identical — so the expected behavior is derived
from Fern, not authored here. The only differences allowed are the deliberate,
non-behavioral ones the byte-diff already normalizes (crozier's `X-Crozier-*`
SDK-identity headers vs Fern's `X-Fern-*`), which this driver canonicalizes on
both sides exactly as `tests/e2e.rs::normalize_sdk_headers` does.

The generated client accepts an `httpx_client`, so each journey injects one whose
`httpx.MockTransport` captures the outgoing request and returns a scripted
response — exercising URL/method construction, header injection, request-body
serialization (field aliasing and `OMIT` filtering), query encoding, typed
pydantic deserialization, and typed error raising, for the sync and async
clients. It records, per journey, the request (method, URL, canonicalized
headers, body) and the outcome (the response model dumped to a dict, or the typed
error's class/status/body), then prints the whole recording as canonical JSON.

The SDK's `src/` directory is passed in `CROZIER_SDK_SRC`; the only third-party
imports are the SDK's own runtime dependencies (`httpx`, `pydantic`). A journey
that cannot complete its structural contract (e.g. a declared 4xx that fails to
raise) exits non-zero so a broken journey fails loudly instead of matching
trivially.
"""

import asyncio
import json
import os
import sys

_src = os.environ.get("CROZIER_SDK_SRC")
if not _src:
    print("CROZIER_SDK_SRC is not set (path to the generated SDK's src/ dir)", file=sys.stderr)
    sys.exit(2)
sys.path.insert(0, _src)

import httpx  # noqa: E402  (import after the generated src/ is on sys.path)

from fern import AsyncFernApi, FernApi  # noqa: E402
from fern.errors.bad_request_error import BadRequestError  # noqa: E402

BASE_URL = "https://api.example.test"
TOKEN = "secret-token"


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
    case-insensitive) and neutralize the deliberate SDK-identity differences the
    byte-diff also normalizes: drop the packaging `SDK-Name`/`SDK-Version` headers
    and rename the `X-Crozier-`/`X-Fern-` language header to a single canonical
    key. Everything else — auth, content-type, and httpx's own headers — must
    match verbatim."""
    out = {}
    for name, value in headers.items():
        key = name.lower()
        if key in ("x-fern-sdk-name", "x-crozier-sdk-name", "x-fern-sdk-version", "x-crozier-sdk-version"):
            continue
        if key in ("x-fern-language", "x-crozier-language"):
            key = "x-sdk-language"
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


def _sync_client(status, payload, *, token=TOKEN):
    transport, box = _capture(status, payload)
    client = FernApi(base_url=BASE_URL, token=token, httpx_client=httpx.Client(transport=transport))
    return client, box


def request_construction_and_response():
    """A POST with an inlined object body: URL/method, bearer auth + SDK-identity
    headers, body field-aliasing (`long_`->`long`, ...) with unset optionals
    filtered out, and the JSON response parsed into a pydantic model."""
    client, box = _sync_client(200, {"string": "world", "long": 7, "bool": False, "list": ["x"]})
    result = client.endpoints_object.endpoints_object_get_and_return_with_optional_field(
        string="hello", integer=1, long_=42, bool_=True, list_=["a", "b"]
    )
    return {
        "request": _request_record(box["request"]),
        "outcome": {"model": type(result).__name__, "data": _dump(result)},
    }


def no_auth_omits_authorization():
    """With no token the Authorization header is absent, but the SDK-identity
    headers are still sent — the unauthenticated path stays wired up."""
    client, box = _sync_client(200, True, token=None)
    result = client.noauth.postwithnoauth(request={"ping": 1})
    return {
        "request": _request_record(box["request"]),
        "outcome": {"model": type(result).__name__, "data": result},
    }


def typed_error_is_raised():
    """A declared 4xx becomes a generated typed exception whose `body` is the
    parsed error model, not a raw dict. Failing to raise is a hard error."""
    client, box = _sync_client(400, {"message": "bad thing"}, token=None)
    try:
        client.noauth.postwithnoauth(request={"ping": 1})
    except BadRequestError as err:
        return {
            "request": _request_record(box["request"]),
            "outcome": {"error": type(err).__name__, "status": err.status_code, "body": _dump(err.body)},
        }
    raise AssertionError("expected BadRequestError for a 400 response, none raised")


def query_parameters_are_encoded():
    """Keyword query args are encoded onto the URL, not the body."""
    client, box = _sync_client(200, {"items": [], "next": None})
    result = client.endpoints_pagination.endpoints_pagination_list_items(cursor="abc", limit=10)
    return {
        "request": _request_record(box["request"]),
        "outcome": {"model": type(result).__name__, "data": _dump(result)},
    }


def raw_response_exposes_underlying_http():
    """`.with_raw_response` returns the parsed data plus access to the response,
    without a second network round-trip."""
    client, box = _sync_client(200, {"string": "raw"})
    raw = client.endpoints_object.with_raw_response.endpoints_object_get_and_return_with_optional_field(string="s")
    if not isinstance(raw.headers, dict):
        raise AssertionError(f"raw response headers should be a dict, got {type(raw.headers)}")
    return {
        "request": _request_record(box["request"]),
        "outcome": {"model": type(raw.data).__name__, "data": _dump(raw.data)},
    }


def async_request_and_response():
    """The async client makes the same request and deserializes the same way."""

    async def run():
        transport, box = _capture(200, {"string": "async-world", "long": 9})
        client = AsyncFernApi(
            base_url=BASE_URL, token=TOKEN, httpx_client=httpx.AsyncClient(transport=transport)
        )
        result = await client.endpoints_object.endpoints_object_get_and_return_with_optional_field(
            string="hi", long_=1
        )
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


def main():
    recording = {}
    for journey in JOURNEYS:
        # A journey that raises is a hard failure (exit non-zero via the uncaught
        # exception) — it must never silently record nothing and match trivially.
        recording[journey.__name__] = journey()
    json.dump(recording, sys.stdout, indent=2, sort_keys=True, default=str)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

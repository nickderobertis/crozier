"""Runtime ("wire") behavior checks for a crozier-generated Python SDK.

Byte-matching Fern proves the *source* is right; this proves the generated
client *behaves* right when imported and called. It is the in-process analog of
Fern's own wire tests — Fern spins up a WireMock server in Docker and asserts,
via WireMock's admin API, that the SDK issued the expected HTTP request, then
checks the canned response deserializes. crozier does not emit that Docker/
WireMock tree (it is Fern generated output gated behind an Enterprise
`enable_wire_tests` flag, which none of the corpora set), so this driver does
the same job with `httpx.MockTransport`: the generated client accepts an
`httpx_client`, so we inject one whose transport captures the outgoing request
and returns a scripted response — exercising URL/method construction, auth and
SDK-identity header injection, request-body serialization (field aliasing and
`OMIT` filtering), query-parameter encoding, typed pydantic deserialization, and
typed error raising, for both the sync and async clients.

Run against an SDK generated from `tests/fixtures/exhaustive/openapi.yml` with
`--package-name fern`. The generated `src/` directory is passed in the
`CROZIER_SDK_SRC` environment variable; the only third-party imports are the
SDK's own runtime dependencies (`httpx`, `pydantic`). Exits non-zero, listing
every failure, if any journey does not behave as expected; the Rust e2e harness
(`tests/e2e.rs`) drives this and asserts success.
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
from fern.types.types_object_with_optional_field import TypesObjectWithOptionalField  # noqa: E402

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


def _sync_client(status, payload, *, token=TOKEN):
    transport, box = _capture(status, payload)
    client = FernApi(base_url=BASE_URL, token=token, httpx_client=httpx.Client(transport=transport))
    return client, box


def request_construction_and_response():
    """A POST with an inlined object body: URL/method, bearer auth + crozier's
    SDK-identity headers, body field-aliasing (`long_`->`long`, ...) with unset
    optionals filtered out, and the JSON response parsed into a pydantic model."""
    client, box = _sync_client(200, {"string": "world", "long": 7, "bool": False, "list": ["x"]})
    result = client.endpoints_object.endpoints_object_get_and_return_with_optional_field(
        string="hello", integer=1, long_=42, bool_=True, list_=["a", "b"]
    )

    req = box["request"]
    assert req.method == "POST", req.method
    assert str(req.url) == f"{BASE_URL}/object/get-and-return-with-optional-field", str(req.url)
    assert req.headers["Authorization"] == f"Bearer {TOKEN}", req.headers.get("Authorization")
    assert req.headers["X-Crozier-Language"] == "Python", req.headers.get("X-Crozier-Language")
    assert req.headers["X-Crozier-SDK-Name"] == "default_package_name", req.headers.get("X-Crozier-SDK-Name")
    assert req.headers["content-type"] == "application/json", req.headers.get("content-type")

    # Only the fields we passed are sent, under their wire (aliased) names; the
    # dozen other optional fields are dropped rather than sent as null.
    sent = json.loads(req.content)
    assert sent == {"string": "hello", "integer": 1, "long": 42, "bool": True, "list": ["a", "b"]}, sent

    # The 2xx JSON body is deserialized into the generated model, un-aliased.
    assert isinstance(result, TypesObjectWithOptionalField), type(result)
    assert result.string == "world"
    assert result.long_ == 7
    assert result.bool_ is False
    assert result.list_ == ["x"]


def no_auth_omits_authorization():
    """With no token, the Authorization header is absent but the SDK-identity
    headers are still sent — the unauthenticated path stays wired up."""
    client, box = _sync_client(200, True, token=None)
    client.noauth.postwithnoauth(request={"ping": 1})

    req = box["request"]
    assert "Authorization" not in req.headers, dict(req.headers)
    assert req.headers["X-Crozier-Language"] == "Python"
    assert json.loads(req.content) == {"ping": 1}


def typed_error_is_raised():
    """A declared 4xx becomes a generated typed exception whose `body` is the
    parsed error model, not a raw dict."""
    client, box = _sync_client(400, {"message": "bad thing"}, token=None)
    try:
        client.noauth.postwithnoauth(request={"ping": 1})
    except BadRequestError as err:
        assert err.status_code == 400, err.status_code
        assert err.body.message == "bad thing", err.body
    else:
        raise AssertionError("expected BadRequestError for a 400 response")


def query_parameters_are_encoded():
    """Keyword query args are encoded onto the URL, not the body."""
    client, box = _sync_client(200, {"items": [], "next": None})
    client.endpoints_pagination.endpoints_pagination_list_items(cursor="abc", limit=10)

    req = box["request"]
    assert req.method == "GET", req.method
    assert req.url.params.get("cursor") == "abc", str(req.url)
    assert req.url.params.get("limit") == "10", str(req.url)


def raw_response_exposes_underlying_http():
    """`.with_raw_response` returns the parsed data plus access to the response
    headers, without a second network round-trip."""
    client, box = _sync_client(200, {"string": "raw"})
    raw = client.endpoints_object.with_raw_response.endpoints_object_get_and_return_with_optional_field(string="s")

    assert isinstance(raw.data, TypesObjectWithOptionalField), type(raw.data)
    assert raw.data.string == "raw"
    assert isinstance(raw.headers, dict)


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
        req = box["request"]
        assert req.method == "POST", req.method
        assert req.headers["Authorization"] == f"Bearer {TOKEN}"
        assert isinstance(result, TypesObjectWithOptionalField), type(result)
        assert result.string == "async-world"
        assert result.long_ == 9

    asyncio.run(run())


JOURNEYS = [
    request_construction_and_response,
    no_auth_omits_authorization,
    typed_error_is_raised,
    query_parameters_are_encoded,
    raw_response_exposes_underlying_http,
    async_request_and_response,
]


def main():
    failures = []
    for journey in JOURNEYS:
        try:
            journey()
        except Exception as err:  # noqa: BLE001 — collect every failure, not just the first
            import traceback

            failures.append(f"{journey.__name__}: {err}\n{traceback.format_exc()}")

    if failures:
        print(f"{len(failures)}/{len(JOURNEYS)} runtime journey(s) failed:", file=sys.stderr)
        for failure in failures:
            print(f"\n--- {failure}", file=sys.stderr)
        sys.exit(1)

    print(f"runtime wire tests: {len(JOURNEYS)} journeys passed")


if __name__ == "__main__":
    main()

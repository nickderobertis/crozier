# llmlint: ignore[new_code_lands_in_a_project] This certified-output proof is invoked by the Cargo e2e SDK-environment gate; crozier uses Cargo and just, with no Nx projects.
"""Bind advertised arguments and execute actual flattened alias body methods.

Exit 0 prints one JSON proof result; exit 1 means the proof or SDK import failed;
exit 2 reports invalid CLI arguments on stderr.
"""

from __future__ import annotations

import argparse
import asyncio
import importlib
import inspect
import json
from pathlib import Path
import re
import sys

import httpx

parser = argparse.ArgumentParser()
parser.add_argument("sdk", type=Path)
parser.add_argument("--reference", type=Path, required=True)
parser.add_argument("--expected", choices=("invalid", "valid"), required=True)
args = parser.parse_args()
if not (args.sdk / "fern" / "__init__.py").is_file():
    parser.error("sdk must contain the generated fern package")
sys.path.insert(0, str(args.sdk.resolve()))
sdk = importlib.import_module("fern")
parameters = re.findall(r"\*\*([a-z_]+):\*\* `([^`]+)`", args.reference.read_text(encoding="utf-8"))
parameters = [(name, annotation) for name, annotation in parameters if name != "request_options"]
expected = [("request", "TitleAlias")] if args.expected == "invalid" else [("caption", "typing.Optional[str]"), ("ticket", "int")]
parameters.sort()
assert parameters == expected, parameters
results: dict[str, str] = {}
for class_name in ("FernApi", "AsyncFernApi"):
    method = getattr(getattr(sdk, class_name), "retitle_manifest")
    value = sdk.TitleAlias(ticket=7, caption="compass") if args.expected == "invalid" else "compass"
    try:
        (inspect.signature(method).bind_partial(None, request=value) if args.expected == "invalid" else inspect.signature(method).bind(None, ticket=7, caption="compass"))
    except TypeError as error:
        assert args.expected == "invalid" and "unexpected keyword argument" in str(error) and "request" in str(error)
        results[class_name] = str(error)
    else:
        assert args.expected == "valid"
        results[class_name] = "corrected caption binds"

requests: list[httpx.Request] = []


def handle(request: httpx.Request) -> httpx.Response:
    assert request.method == "PUT" and request.url.path == "/manifest"
    assert json.loads(request.read()) == {"caption": "compass", "ticket": 7}
    requests.append(request)
    return httpx.Response(204)


with httpx.Client(transport=httpx.MockTransport(handle)) as transport:
    client = sdk.FernApi(base_url="https://manifest.example.test", httpx_client=transport)
    try:
        client.retitle_manifest(ticket=7, request=sdk.TitleAlias(ticket=7, caption="compass"))
    except TypeError as error:
        assert "request" in str(error)
    else:
        raise AssertionError("the absent request argument unexpectedly bound")
    assert not requests
    assert client.retitle_manifest(ticket=7, caption="compass") is None


async def async_wire() -> None:
    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as transport:
        client = sdk.AsyncFernApi(base_url="https://manifest.example.test", httpx_client=transport)
        assert await client.retitle_manifest(ticket=7, caption="compass") is None


asyncio.run(async_wire())
assert len(requests) == 2
print(json.dumps({"bindings": results, "wire_requests": len(requests), "invalid_request_recovers": True}, sort_keys=True))

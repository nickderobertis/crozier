# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as request-alias-reference-parameters.py does; crozier-e2e runs it and reads this folder through its e2eReads input.
"""Bind reference.md's worked calls for `[]` query parameters to the actual SDK.

Exit 0 prints one JSON proof result; exit 1 means the proof or SDK import failed;
exit 2 reports invalid CLI arguments on stderr.
"""

from __future__ import annotations

import argparse
import ast
import asyncio
import importlib
import inspect
import json
from pathlib import Path
import re
import sys
from urllib.parse import parse_qsl

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

# The measurement's two operations taking a `[]` query parameter, and the wire
# name each call must send.
CALLS = {"list_berths": "codes[]", "release_berths": "ids[]"}
reference = args.reference.read_text(encoding="utf-8")


def worked_call(method: str) -> dict[str, object]:
    """The keyword arguments of reference.md's worked call of `method`."""
    match = re.search(rf"^client\.berths\.{method}\(\n(.*?)^\)$", reference, re.MULTILINE | re.DOTALL)
    assert match, f"reference.md has no worked call of {method}"
    call = ast.parse(f"f(\n{match.group(1)})", mode="eval").body
    assert isinstance(call, ast.Call)
    return {keyword.arg or "": ast.literal_eval(keyword.value) for keyword in call.keywords}


headers = {"strict_mode": True, "tenant_code": "harbour-7", "shift_number": 2}
requests: list[httpx.Request] = []


def handle(request: httpx.Request) -> httpx.Response:
    requests.append(request)
    return httpx.Response(200, json=[]) if request.method == "GET" else httpx.Response(204)


bindings: dict[str, str] = {}
for method, wire in CALLS.items():
    arguments = worked_call(method)
    keyword = next(name for name in arguments if name not in ("zone",))
    for class_name in ("FernApi", "AsyncFernApi"):
        client = getattr(sdk, class_name)(base_url="https://ledger.example.test", **headers)
        bound = getattr(client.berths, method)
        try:
            inspect.signature(bound).bind(**arguments)
        except TypeError as error:
            assert args.expected == "invalid", error
            assert "unexpected keyword argument" in str(error) and keyword in str(error), error
            bindings[f"{class_name}.{method}"] = str(error)
        else:
            assert args.expected == "valid", f"{class_name}.{method} bound {keyword}"
            bindings[f"{class_name}.{method}"] = f"{keyword} binds"
    # Either way the argument the generated method declares is the one sent
    # under the `[]` wire name.
    argument = wire.removesuffix("[]")
    values = next(iter(value for name, value in arguments.items() if name not in ("zone",)))
    with httpx.Client(transport=httpx.MockTransport(handle)) as transport:
        client = sdk.FernApi(base_url="https://ledger.example.test", httpx_client=transport, **headers)
        call = getattr(client.berths, method)
        extra = {"zone": arguments["zone"]} if "zone" in arguments else {}
        call(**extra, **{argument: values})
    sent = parse_qsl(requests[-1].url.query.decode())
    assert [pair for pair in sent if pair[0] == wire] == [(wire, value) for value in values], sent


async def async_wire() -> None:
    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as transport:
        client = sdk.AsyncFernApi(base_url="https://ledger.example.test", httpx_client=transport, **headers)
        await client.berths.release_berths(ids=["B-7"])
    assert parse_qsl(requests[-1].url.query.decode()) == [("ids[]", "B-7")]


asyncio.run(async_wire())
print(json.dumps({"bindings": bindings, "wire_requests": len(requests)}, sort_keys=True))

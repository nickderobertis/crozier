"""Assert each operation's declared header defaults on the requests its generated method sends.

Usage: declared_header_default_wire.py SDK_SRC SPEC_JSON. Every operation in
SPEC_JSON is called once through the generated client, with no arguments, on an
httpx.MockTransport that records the request; each header parameter declaring a
`schema.default` (an operation's own parameter overriding its path's) must
arrive with that default. Exit 0 prints one success line; exit 1 names each
operation whose sent header differs; exit 2 reports invalid CLI arguments.
"""

import argparse
import importlib
import json
import re
import sys
from pathlib import Path

import httpx

METHODS = ("get", "put", "post", "patch", "delete")

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("sdk_src", type=Path)
parser.add_argument("spec", type=Path)
args = parser.parse_args()
if not (args.sdk_src / "fern" / "client.py").is_file():
    parser.error("sdk_src must contain the generated fern package")
try:
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
except (OSError, ValueError) as error:
    parser.error(f"spec must be a readable JSON document: {error}")


def headers(parameters: list[dict]) -> dict[str, str]:
    return {
        parameter["name"]: parameter["schema"]["default"]
        for parameter in parameters
        if parameter.get("in") == "header" and "default" in parameter.get("schema", {})
    }


# (HTTP method, path, generated method name, {header: declared default}) per operation.
operations = [
    (
        verb.upper(),
        path,
        re.sub(r"(?<!^)(?=[A-Z])", "_", item[verb]["operationId"]).lower(),
        headers(item.get("parameters", [])) | headers(item[verb].get("parameters", [])),
    )
    for path, item in spec["paths"].items()
    for verb in METHODS
    if verb in item
]
if not any(declared for *_, declared in operations):
    parser.error("spec declares no header parameter default")

sys.path.insert(0, str(args.sdk_src.resolve()))
sdk = importlib.import_module("fern")
sent: list[httpx.Request] = []


def capture(request: httpx.Request) -> httpx.Response:
    sent.append(request)
    return httpx.Response(200, json=[])


client = sdk.FernApi(
    base_url="https://wire.example.net",
    httpx_client=httpx.Client(transport=httpx.MockTransport(capture)),
)
failures = []
for verb, path, method, declared in operations:
    count = len(sent)
    getattr(client, method)()
    if len(sent) != count + 1 or (sent[-1].method, sent[-1].url.path) != (verb, path):
        failures.append(f"{verb} {path}: {method}() did not send exactly its own request")
        continue
    for name, default in declared.items():
        value = sent[-1].headers.get(name)
        if value != default:
            failures.append(f"{verb} {path}: {method}() sent {name}: {value!r}, but the operation declares {default!r}")
if failures:
    print("\n".join(failures), file=sys.stderr)
    sys.exit(1)
print(f"{len(operations)} operation(s) sent their declared header defaults")

"""Assert each operation's declared header defaults on the requests its generated method sends.

Usage: declared_header_default_wire.py SDK_SRC SPEC_JSON. Every operation in
SPEC_JSON is called once through the generated client, with no arguments, on an
httpx.MockTransport that records the request; each header parameter declaring a
string `schema.default` (an operation's own parameter overriding its path's)
must arrive with that default. Exit 0 prints one success line; exit 1 names each
operation whose sent header differs; exit 2 reports invalid CLI arguments or a
document this script cannot read.
"""

import argparse
import importlib
import json
import re
import sys
from pathlib import Path
from typing import Any, NamedTuple

import httpx

METHODS = ("get", "put", "post", "patch", "delete")


class Operation(NamedTuple):
    verb: str
    path: str
    method: str
    defaults: dict[str, str]


class Malformed(ValueError):
    """The document has a shape this script does not read."""


def header_defaults(owner: dict[str, Any], where: str) -> dict[str, str]:
    """The string defaults `owner`'s header parameters declare, by header name."""
    parameters = owner.get("parameters", [])
    if not isinstance(parameters, list) or not all(isinstance(parameter, dict) for parameter in parameters):
        raise Malformed(f"{where}: parameters is not a list of objects")
    found = {}
    for parameter in parameters:
        schema = parameter.get("schema", {})
        if parameter.get("in") != "header" or not isinstance(schema, dict) or "default" not in schema:
            continue
        name, default = parameter.get("name"), schema["default"]
        if not isinstance(name, str) or not isinstance(default, str):
            raise Malformed(f"{where}: a header parameter's name or default is not a string")
        found[name] = default
    return found


def operations(spec: object) -> list[Operation]:
    """Every operation the document declares, with its effective header defaults."""
    paths = spec.get("paths") if isinstance(spec, dict) else None
    if not isinstance(paths, dict):
        raise Malformed("the document has no `paths` object")
    found = []
    for path, item in paths.items():
        if not isinstance(item, dict):
            raise Malformed(f"{path}: the path item is not an object")
        inherited = header_defaults(item, path)
        for verb in METHODS:
            operation = item.get(verb)
            if operation is None:
                continue
            where = f"{verb.upper()} {path}"
            if not isinstance(operation, dict) or not isinstance(operation.get("operationId"), str):
                raise Malformed(f"{where}: the operation has no string operationId")
            method = re.sub(r"(?<!^)(?=[A-Z])", "_", operation["operationId"]).lower()
            found.append(Operation(verb.upper(), path, method, inherited | header_defaults(operation, where)))
    return found


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("sdk_src", type=Path)
parser.add_argument("spec", type=Path)
args = parser.parse_args()
if not (args.sdk_src / "fern" / "client.py").is_file():
    parser.error("sdk_src must contain the generated fern package")
try:
    declared = operations(json.loads(args.spec.read_text(encoding="utf-8")))
except (OSError, ValueError) as error:
    parser.error(f"spec must be a readable OpenAPI JSON document: {error}")
if not any(operation.defaults for operation in declared):
    parser.error("spec declares no header parameter default")

sys.path.insert(0, str(args.sdk_src.resolve()))
sdk = importlib.import_module("fern")
sent: list[httpx.Request] = []


def capture(request: httpx.Request) -> httpx.Response:
    sent.append(request)
    return httpx.Response(200, json=[])


# llmlint: ignore[e2e_not_mocked] The emitted SDK is real; the local transport records the request it serializes and supplies only the external server response, as in the repository's SDK wire tier.
client = sdk.FernApi(
    base_url="https://wire.example.net",
    httpx_client=httpx.Client(transport=httpx.MockTransport(capture)),
)
failures = []
for operation in declared:
    count = len(sent)
    getattr(client, operation.method)()
    where = f"{operation.verb} {operation.path}: {operation.method}()"
    if len(sent) != count + 1 or (sent[-1].method, sent[-1].url.path) != (operation.verb, operation.path):
        failures.append(f"{where} did not send exactly its own request")
        continue
    for name, default in operation.defaults.items():
        value = sent[-1].headers.get(name)
        if value != default:
            failures.append(f"{where} sent {name}: {value!r}, but the operation declares {default!r}")
if failures:
    print("\n".join(failures), file=sys.stderr)
    sys.exit(1)
print(f"{len(declared)} operation(s) sent their declared header defaults")

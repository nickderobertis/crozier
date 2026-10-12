"""Assert each operation's declared header defaults on the requests its generated method sends.

Usage: declared_header_default_wire.py SDK_SRC SPEC_JSON. Every operation in
SPEC_JSON is called once through the generated client, with no arguments, on an
httpx.MockTransport that records the request; each header parameter declaring a
string `schema.default` (an operation's own parameter replacing its path's)
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
UNREAD = ("head", "options", "trace")


class Operation(NamedTuple):
    verb: str
    path: str
    method: str
    defaults: dict[str, str]


class Malformed(ValueError):
    """The document has a shape this script does not read."""


def header_parameters(owner: dict[str, Any], where: str) -> dict[str, dict[str, Any]]:
    """`owner`'s header parameters, by header name."""
    parameters = owner.get("parameters", [])
    if not isinstance(parameters, list) or not all(isinstance(parameter, dict) for parameter in parameters):
        raise Malformed(f"{where}: parameters is not a list of objects")
    if any("$ref" in parameter for parameter in parameters):
        raise Malformed(f"{where}: parameter references are not read")
    if not all(isinstance(parameter.get("in"), str) for parameter in parameters):
        raise Malformed(f"{where}: a parameter's `in` is not a string")
    headers = [parameter for parameter in parameters if parameter["in"] == "header"]
    if not all(isinstance(parameter.get("name"), str) for parameter in headers):
        raise Malformed(f"{where}: a header parameter's name is not a string")
    return {parameter["name"]: parameter for parameter in headers}


def declared_defaults(parameters: dict[str, dict[str, Any]], where: str) -> dict[str, str]:
    """The string default each effective header parameter declares, by header name."""
    found = {}
    for name, parameter in parameters.items():
        schema = parameter.get("schema", {})
        if not isinstance(schema, dict) or "$ref" in schema:
            raise Malformed(f"{where}: header {name}'s schema is not an inline object")
        if "default" not in schema:
            continue
        if not isinstance(schema["default"], str):
            raise Malformed(f"{where}: header {name}'s default is not a string")
        found[name] = schema["default"]
    return found


def operations(spec: object) -> list[Operation]:
    """Every operation the document declares, with the defaults of its effective header parameters.

    An operation's parameter replaces its path item's of the same name, as the
    OpenAPI Operation Object specifies, so a default the path declares does not
    survive an override that declares none.
    """
    paths = spec.get("paths") if isinstance(spec, dict) else None
    if not isinstance(paths, dict):
        raise Malformed("the document has no `paths` object")
    found = []
    for path, item in paths.items():
        if not isinstance(item, dict):
            raise Malformed(f"{path}: the path item is not an object")
        if unread := [verb.upper() for verb in UNREAD if verb in item]:
            raise Malformed(f"{path}: {', '.join(unread)} operations are not read")
        inherited = header_parameters(item, path)
        for verb in METHODS:
            operation = item.get(verb)
            if operation is None:
                continue
            where = f"{verb.upper()} {path}"
            if not isinstance(operation, dict) or not isinstance(operation.get("operationId"), str):
                raise Malformed(f"{where}: the operation has no string operationId")
            method = re.sub(r"(?<!^)(?=[A-Z])", "_", operation["operationId"]).lower()
            effective = inherited | header_parameters(operation, where)
            found.append(Operation(verb.upper(), path, method, declared_defaults(effective, where)))
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


# llmlint: ignore-block[e2e_not_mocked] The emitted SDK is real; the local transport records the request it serializes and supplies only the external server response, as in the repository's SDK wire tier.
client = sdk.FernApi(
    base_url="https://wire.example.net",
    httpx_client=httpx.Client(transport=httpx.MockTransport(capture)),
)
# llmlint: ignore-end[e2e_not_mocked]
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

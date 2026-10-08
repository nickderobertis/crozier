# llmlint: ignore[new_code_lands_in_a_project] This certified-output proof is invoked by the Cargo e2e SDK-environment gate; crozier uses Cargo and just, with no Nx projects.
"""Check example types against actual generated SDK annotations and JSON transport.

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
import re
import sys
import textwrap
import typing
from pathlib import Path

import httpx
from pydantic import TypeAdapter, ValidationError


def check(root: Path, group: str, method: str, expected: str) -> None:
    sys.path.insert(0, str(root))
    sdk = importlib.import_module("fern")
    module = importlib.import_module(f"fern.{group}.client")
    class_name = "VaultClient" if group == "vault" else "DepositoryClient"
    values: dict[str, str] = {}
    for prefix in ("", "Async"):
        function = getattr(getattr(module, prefix + class_name), method)
        annotation = typing.get_type_hints(function)["request"]
        assert annotation is bytes, annotation
        doc = inspect.getdoc(function)
        assert doc is not None
        tree = ast.parse(textwrap.dedent(doc.split("Examples\n--------\n", 1)[1]))
        calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
                 and isinstance(node.func, ast.Attribute) and node.func.attr == method]
        assert len(calls) == 1
        argument = next(keyword.value for keyword in calls[0].keywords if keyword.arg == "request")
        value = ast.literal_eval(argument)
        try:
            TypeAdapter(annotation).validate_python(value, strict=True)
        except ValidationError:
            assert expected == "invalid" and value == "string"
            values[prefix + class_name] = "plain string rejected by actual bytes annotation"
        else:
            assert expected == "valid" and value == b"string"
            values[prefix + class_name] = "bytes example has its declared type"
    reference = (root.parent / "reference.md").read_text(encoding="utf-8")
    advertised = []
    for code in re.findall(r"```python\n(.*?)\n```", reference, re.DOTALL):
        for node in ast.walk(ast.parse(code)):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method:
                argument = next(keyword.value for keyword in node.keywords if keyword.arg == "request")
                advertised.append(ast.literal_eval(argument))
    assert len(advertised) == 1
    assert advertised[0] == ("string" if expected == "invalid" else b"string")
    section = next(part for part in reference.split("<details>") if f">{method}</a>" in part)
    documented = "str" if expected == "invalid" else "bytes"
    assert f"**request:** `{documented}`" in section
    other = "bytes" if expected == "invalid" else "str"
    assert f"**request:** `{other}`" not in section
    readme = (root.parent / "README.md").read_text(encoding="utf-8")
    shown = []
    for code in re.findall(r"```python\n(.*?)\n```", readme, re.DOTALL):
        for node in ast.walk(ast.parse(code)):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == method:
                if any(isinstance(argument, ast.Constant) and argument.value is Ellipsis for argument in node.args):
                    continue
                argument = next(keyword.value for keyword in node.keywords if keyword.arg == "request")
                shown.append(ast.literal_eval(argument))
    assert len(shown) == (2 if group == "depository" else 0)
    assert all(value == ("string" if expected == "invalid" else b"string") for value in shown)
    recorded: list[httpx.Request] = []

    def transport(request: httpx.Request) -> httpx.Response:
        assert json.loads(request.read()) == "c3RyaW5n", request.read()
        recorded.append(request)
        return httpx.Response(204)

    arguments = {"locker": "north"} if group == "depository" else {}
    with httpx.Client(transport=httpx.MockTransport(transport)) as client:
        api = sdk.FernApi(base_url="http://examples.invalid", httpx_client=client)
        function = getattr(getattr(api, group), method)
        try:
            function(**arguments)
        except TypeError as error:
            assert "request" in str(error)
        else:
            raise AssertionError("a required request was silently omitted")
        assert not recorded
        function(request=b"string", **arguments)

    async def asynchronous() -> None:
        async with httpx.AsyncClient(transport=httpx.MockTransport(transport)) as client:
            api = sdk.AsyncFernApi(base_url="http://examples.invalid", httpx_client=client)
            await getattr(getattr(api, group), method)(request=b"string", **arguments)

    asyncio.run(asynchronous())
    assert len(recorded) == 2
    print(json.dumps({"examples": values, "wire": "sync/async bytes encoded as a base64 JSON string"}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sdk_src", type=Path)
    parser.add_argument("group", choices=("vault", "depository"))
    parser.add_argument("method", choices=("deposit_bundle", "deposit_parcel"))
    parser.add_argument("--examples", choices=("invalid", "valid"), required=True)
    args = parser.parse_args()
    if not (args.sdk_src / "fern/__init__.py").is_file():
        parser.error("sdk_src must contain the generated fern package")
    check(args.sdk_src, args.group, args.method, args.examples)

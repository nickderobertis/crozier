"""Bind generated examples and drive actual multipart methods at HTTP transport."""

from __future__ import annotations

import argparse
import ast
import asyncio
import importlib
import inspect
import json
import sys
import textwrap
from email import policy
from email.parser import BytesParser
from pathlib import Path
from types import ModuleType
from typing import Any, Callable

import httpx


def examples(sdk: ModuleType, method: str, expected: str) -> dict[str, str]:
    results: dict[str, str] = {}
    for name in ("FernApi", "AsyncFernApi"):
        function = getattr(getattr(sdk, name), method)
        doc = inspect.getdoc(function)
        assert doc is not None and "Examples\n--------\n" in doc
        tree = ast.parse(textwrap.dedent(doc.split("Examples\n--------\n", 1)[1]))
        namespace: dict[str, object] = {}
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                statement = ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[]))
                exec(compile(statement, "generated example imports", "exec"), namespace)
        calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
                 and isinstance(node.func, ast.Attribute) and node.func.attr == method]
        assert len(calls) == 1, (name, method, calls)
        call = calls[0]
        assert all(keyword.arg is not None for keyword in call.keywords)
        kwargs = {keyword.arg: eval(compile(ast.Expression(keyword.value), "generated value", "eval"), namespace)
                  for keyword in call.keywords}
        args = [eval(compile(ast.Expression(arg), "generated value", "eval"), namespace) for arg in call.args]
        try:
            inspect.signature(function).bind(None, *args, **kwargs)
        except TypeError as error:
            assert expected == "invalid" and "attachment" in str(error), (name, method, str(error))
            results[f"{name}.{method}"] = str(error)
        else:
            assert expected == "valid", (name, method, "the certified example unexpectedly binds")
            results[f"{name}.{method}"] = "example binds"
    return results


def wire(sdk: ModuleType, shape: str) -> None:
    recorded: list[httpx.Request] = []
    payload = b"cartography payload\x00\xff"
    file = ("payload.bin", payload, "application/octet-stream")
    method = "store_plan" if shape == "alias" else "store_survey"
    field = "plan" if shape == "alias" else "json"
    model = getattr(sdk, "PlanAlias" if shape == "alias" else "StoreSurveyRequestJson")

    def handle(request: httpx.Request) -> httpx.Response:
        recorded.append(request)
        content_type = request.headers["content-type"]
        assert content_type.startswith("multipart/form-data; boundary=")
        message = BytesParser(policy=policy.default).parsebytes(
            f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode() + request.read()
        )
        parts = {part.get_param("name", header="content-disposition"): part
                 for part in message.iter_parts()}
        if request.url.path == "/metadata":
            assert set(parts) == {"metadata"}
            encoded = parts["metadata"].get_payload(decode=True)
            assert isinstance(encoded, bytes) and json.loads(encoded) == {"bearing": 82}
        else:
            assert set(parts) == {field, "attachment"}
            encoded = parts[field].get_payload(decode=True)
            assert isinstance(encoded, bytes) and json.loads(encoded) == {"bearing": 73}
            assert parts["attachment"].get_filename() == "payload.bin"
            assert parts["attachment"].get_payload(decode=True) == payload
        return httpx.Response(204)

    def missing_file(function: Callable[..., Any]) -> None:
        before = len(recorded)
        try:
            function(**{field: model(bearing=73)})
        except TypeError as error:
            assert "attachment" in str(error)
        else:
            raise AssertionError("a required file was silently omitted")
        assert len(recorded) == before

    with httpx.Client(transport=httpx.MockTransport(handle)) as transport:
        client = getattr(sdk, "FernApi")(base_url="https://wire.example.test", httpx_client=transport)
        function = getattr(client, method)
        missing_file(function)
        assert function(**{field: model(bearing=73), "attachment": file}) is None
        if shape == "json":
            assert client.store_metadata(metadata=getattr(sdk, "StoreMetadataRequestMetadata")(bearing=82)) is None

    async def async_wire() -> None:
        async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as transport:
            client = getattr(sdk, "AsyncFernApi")(base_url="https://wire.example.test", httpx_client=transport)
            function = getattr(client, method)
            before = len(recorded)
            try:
                await function(**{field: model(bearing=73)})
            except TypeError as error:
                assert "attachment" in str(error)
            else:
                raise AssertionError("an async required file was silently omitted")
            assert len(recorded) == before
            assert await function(**{field: model(bearing=73), "attachment": file}) is None
            if shape == "json":
                value = getattr(sdk, "StoreMetadataRequestMetadata")(bearing=82)
                assert await client.store_metadata(metadata=value) is None

    asyncio.run(async_wire())
    assert len(recorded) == (2 if shape == "alias" else 4)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sdk_src", type=Path)
    parser.add_argument("shape", choices=("alias", "json"))
    parser.add_argument("--examples", choices=("invalid", "valid"), required=True)
    parser.add_argument("--wire", action="store_true")
    args = parser.parse_args()
    if not (args.sdk_src / "fern" / "__init__.py").is_file():
        parser.error("sdk_src must contain the generated fern package")
    sys.path.insert(0, str(args.sdk_src.resolve()))
    sdk = importlib.import_module("fern")
    if args.wire:
        wire(sdk, args.shape)
    results = examples(sdk, "store_plan" if args.shape == "alias" else "store_survey", args.examples)
    if args.shape == "json":
        results.update(examples(sdk, "store_metadata", "valid"))
    print(json.dumps({"shape": args.shape, "wire": args.wire, "examples": results}, sort_keys=True))


if __name__ == "__main__":
    main()

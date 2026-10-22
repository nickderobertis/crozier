"""Exercise the generated patisserie SDK's public constructors and wire boundary."""

import ast
import asyncio
import importlib
import inspect
import json
import re
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import ModuleType

import jsonschema
import pydantic
import yaml

sdk = Path(sys.argv[1])
sys.path.insert(0, str(sdk / "src"))
fern: ModuleType = importlib.import_module("fern")
AsyncFernApi = fern.AsyncFernApi
FernApi = fern.FernApi
Pastry = fern.Pastry
Pastry_Tart = fern.Pastry_Tart
TartOrder_Puff = fern.TartOrder_Puff
TartOrder_Shortcrust = fern.TartOrder_Shortcrust
ParsingError = importlib.import_module("fern.core.parse_error").ParsingError

document = yaml.safe_load(Path(sys.argv[2]).read_text())

validator = jsonschema.Draft202012Validator(
    {"$ref": "#/components/schemas/Pastry", "components": document["components"]}
)
inner_tag = document["components"]["schemas"]["TartOrder"]["discriminator"]["propertyName"]
assert inner_tag == sys.argv[3], "the runtime matrix must exercise distinct inner discriminators"
for schema_name in ["FruitTart", "CreamTart"]:
    schema = document["components"]["schemas"][schema_name]
    assert inner_tag in schema["required"] and inner_tag in schema["properties"]
    if inner_tag == "value":
        assert "crust" not in schema["required"] and "crust" not in schema["properties"]
v2 = pydantic.VERSION.startswith("2.")
parse = pydantic.TypeAdapter(Pastry).validate_python if v2 else lambda value: pydantic.parse_obj_as(Pastry, value)
assert list(inspect.signature(Pastry_Tart).parameters) == ["value", "kind"]
assert set(Pastry_Tart.model_fields if v2 else Pastry_Tart.__fields__) == {"value", "kind"}

cases = [
    (
        Pastry_Tart(value=TartOrder_Shortcrust(kind="tart", fruit="pear")),
        {"kind": "tart", inner_tag: "shortcrust", "fruit": "pear"},
    ),
    (
        Pastry_Tart(value=TartOrder_Puff(kind="tart", cream="vanilla")),
        {"kind": "tart", inner_tag: "puff", "cream": "vanilla"},
    ),
]
if inner_tag != "value":
    cases.append(
        (
            Pastry_Tart(value=TartOrder_Shortcrust(kind="tart", fruit="pear", value={"note": "ripe"})),
            {"kind": "tart", inner_tag: "shortcrust", "fruit": "pear", "value": {"note": "ripe"}},
        )
    )
for value, wire in cases:
    validator.validate(wire)
    assert value.dict() == wire
    assert json.loads(value.json()) == wire
    if v2:
        assert value.model_dump(mode="json", by_alias=True) == wire
        assert value.model_dump(by_alias=True) == wire
    validator.validate(json.loads(value.json()))
    assert (value.model_copy() if v2 else value.copy()).value == value.value
    assert parse(wire) == value
    assert parse({"kind": "tart", "value": wire}) == value

value, wire = cases[0]
for bad in [{**wire, inner_tag: "unknown"}, {"kind": "tart", inner_tag: "shortcrust"}]:
    try:
        parse(bad)
    except pydantic.ValidationError:
        pass
    else:
        raise AssertionError(f"invalid provider payload accepted: {bad}")
assert parse(wire) == value

sent = []
responses = iter([wire, {"kind": "tart", inner_tag: "unknown"}, wire] * 2)


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        assert self.path == "/orders"
        sent.append(json.loads(self.rfile.read(int(self.headers["Content-Length"]))))
        validator.validate(sent[-1])
        body = json.dumps(next(responses)).encode()
        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        pass


# llmlint: ignore-block[async_typed_clients_at_boundaries] This loopback compatibility journey must drive the generated synchronous SDK API; AsyncFernApi has its own journey below.
def calls(client):
    assert client.place_order(request=value) == value
    try:
        client.place_order(request=value)
    except ParsingError:
        pass
    else:
        raise AssertionError("invalid provider response accepted")
    assert client.place_order(request=value) == value


# llmlint: ignore-end[async_typed_clients_at_boundaries]


async def async_calls(base_url):
    client = AsyncFernApi(base_url=base_url)
    assert await client.place_order(request=value) == value
    try:
        await client.place_order(request=value)
    except ParsingError:
        pass
    else:
        raise AssertionError("invalid async provider response accepted")
    assert await client.place_order(request=value) == value


server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()
try:
    base_url = f"http://127.0.0.1:{server.server_port}"
    # llmlint: ignore[async_typed_clients_at_boundaries] Construct and drive the synchronous SDK API under test; the next call exercises its asynchronous counterpart.
    calls(FernApi(base_url=base_url))
    asyncio.run(async_calls(base_url))
finally:
    server.shutdown()
    server.server_close()
    thread.join()

assert sent == [wire] * 6
examples = 0
for block in re.findall(r"```python\n(.*?)```", (sdk / "README.md").read_text(), re.S):
    if "Pastry_Tart(" not in block:
        continue
    tree = ast.parse(block)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "Pastry_Tart":
            example = eval(compile(ast.Expression(node), "README constructor", "eval"), globals())  # noqa: S307 -- Execute constructors from the freshly generated SDK README, whose module is already imported.
            validator.validate(json.loads(example.json()))
            examples += 1
assert examples == 2, examples
print(f"Pydantic {pydantic.VERSION}: constructors, flat wire, recovery and README pass")

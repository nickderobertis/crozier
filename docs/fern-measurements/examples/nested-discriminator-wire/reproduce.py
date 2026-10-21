import json
import re
from pathlib import Path
import pydantic
import jsonschema
from fern import Pastry, Pastry_Tart, TartOrder_Shortcrust

s = Path(__file__).resolve().parent
doc = json.loads((s / "schema.json").read_text())
schema = {"$ref": "#/components/schemas/Pastry", "components": doc["components"]}
validator = jsonschema.Draft202012Validator(schema)
valid = {"kind": "tart", "crust": "shortcrust", "fruit": "pear"}
validator.validate(valid)
value = Pastry_Tart(value=TartOrder_Shortcrust(kind="tart", fruit="pear"))
wire = value.model_dump(mode="json", by_alias=True)
print("pydantic", pydantic.__version__)
print("valid provider payload:", json.dumps(valid, sort_keys=True))
print("certified SDK serializes:", json.dumps(wire, sort_keys=True))
errors = list(validator.iter_errors(wire))
assert errors
print("schema validation of certified SDK output fails:", errors[0].message)
try:
    pydantic.TypeAdapter(Pastry).validate_python(valid)
except pydantic.ValidationError as exc:
    print("certified SDK validation of valid provider payload fails:", str(exc))
else:
    raise AssertionError("expected the reference SDK to reject the valid flat payload")
readme = s / "fern-expected/README.md"
snippet = next(
    block
    for block in re.findall(r"```python\n(.*?)```", readme.read_text(), re.S)
    if "tart=," in block
)
try:
    compile(snippet, "certified README usage", "exec")
except SyntaxError as exc:
    print("certified README fails compilation:", exc)
else:
    raise AssertionError("expected the reference example syntax error")

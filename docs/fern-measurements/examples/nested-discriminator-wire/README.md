# Nested discriminator wire defect

This is the retained Fern runtime measurement for the nested-discriminator
flat-wire departure.
Crozier's runtime and golden journeys now exercise both mapping arms while
preserving the public wrapper constructors.

`openapi.yml` was authored from scratch. `fern-expected/` is the complete freshly
generated, comment-stripped output of Fern CLI 5.163.1 and Python SDK 5.41.3,
produced with the native `fern-references.py generate handwritten` pipeline.
Its native tree digest is
`bab02bcc092244e72bbd68eff3faf1b60400d72b0cdc980560e9d4e57ccb650c`.
The reproduction reads the canonical `openapi.yml` directly.

`runtime.txt` records an actual run with Pydantic 2.14.1. A provider's flat
payload validates against the source schema. Constructing the corresponding
SDK variant emits an extra `value` envelope that fails that schema, while the
SDK rejects the valid provider payload for missing `value`. Its README's
`tart=,` example also fails Python compilation. Crozier corrects the wire defect through the documented departure; byte-matched
public model declarations alone would not prove correct behavior.

To reproduce, change into this directory, install `./fern-expected`,
`jsonschema==4.26.0` and `PyYAML==6.0.3` in a disposable Python environment with
Pydantic 2.14.1, then run the command below there. It validates the positive
control and requires all three failures. The repair keeps Fern's public variant classes and `.value` constructors while
flattening the wire representation in both directions under Pydantic v1 and v2;
the generated README constructs the inner variant using `value=`.

```sh
python - <<'PY'
import json
import yaml
import re
from pathlib import Path
import pydantic
import jsonschema
from fern import Pastry, Pastry_Tart, TartOrder_Shortcrust

s = Path.cwd()
doc = yaml.safe_load((s / "openapi.yml").read_text())
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
PY
```

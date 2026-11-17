# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as bracket-query-parameter-call-keyword.py does; crozier-e2e runs it and reads this folder through its e2eReads input.
"""Import a generated model and hold its field aliases to the declared wire names.

The model is imported from the generated package. Each field's two aliases, its
serialization metadata and its pydantic alias, must be exactly one declared
wire name, as string data. A payload keyed by the declared names is then parsed
into the model, dumped by alias, and converted for the wire through the SDK's
own serializer, and each must carry every value under exactly its declared name.

Exit 0 prints one JSON proof result; exit 1 means the proof failed; exit 2
reports invalid CLI arguments on stderr.
"""

from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path
import sys
import typing

parser = argparse.ArgumentParser()
parser.add_argument("sdk", type=Path)
parser.add_argument("--model", required=True, help="module:Class, e.g. fern.types.beacon:Beacon")
parser.add_argument("--wire", action="append", required=True, help="a declared wire name (repeatable)")
parser.add_argument("--expected", choices=("invalid", "valid"), required=True)
args = parser.parse_args()
if not (args.sdk / "fern" / "__init__.py").is_file():
    parser.error("sdk must contain the generated fern package")
module_name, _, class_name = args.model.partition(":")
if not class_name:
    parser.error("--model must be module:Class")
sys.path.insert(0, str(args.sdk.resolve()))
wires: list[str] = args.wire

try:
    model = getattr(importlib.import_module(module_name), class_name)
except Exception as error:  # noqa: BLE001 - any import-time failure is the finding
    assert args.expected == "invalid", f"{args.model} failed to import: {error!r}"
    print(json.dumps({"import": f"{type(error).__name__} importing {module_name}"}, sort_keys=True))
    raise SystemExit(0) from None

from fern.core.serialization import (  # noqa: E402 - the package is importable only from here
    FieldMetadata,
    convert_and_respect_annotation_metadata,
)

hints = typing.get_type_hints(model, include_extras=True)
aliases: dict[str, tuple[object, object]] = {}
for name, field in model.model_fields.items():
    metadata = [item.alias for item in getattr(hints[name], "__metadata__", ()) if isinstance(item, FieldMetadata)]
    aliases[name] = (metadata[0] if metadata else name, field.alias or name)
# Each field's aliases, by the declared wire name they should both be.
by_wire = {pair[0]: name for name, pair in aliases.items() if pair[0] == pair[1] and pair[0] in wires}
mismatched = sorted(repr(pair) for pair in aliases.values() if pair[0] not in wires or pair[0] != pair[1])
if args.expected == "invalid":
    assert mismatched, "every alias is a declared wire name"
    print(json.dumps({"aliases not declared": mismatched}, sort_keys=True))
    raise SystemExit(0)
assert not mismatched and sorted(by_wire) == sorted(wires), (mismatched, by_wire)
assert all(isinstance(wire, str) for wire in by_wire), by_wire


def sample(name: str) -> object:
    """A value of the field's own type: an int field takes 7, any other a string."""
    return 7 if int in typing.get_args(hints[name].__origin__) else f"value of {name}"


payload = {wire: sample(name) for wire, name in by_wire.items()}
parsed = model.model_validate(payload)
assert all(getattr(parsed, name) == payload[wire] for wire, name in by_wire.items()), parsed
dumped = parsed.dict()
written = convert_and_respect_annotation_metadata(object_=dict(parsed), annotation=model, direction="write")
assert dumped == payload, dumped
assert written == payload, written
print(json.dumps({"round trip": sorted(payload)}, sort_keys=True))

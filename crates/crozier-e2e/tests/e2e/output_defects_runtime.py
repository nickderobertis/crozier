"""Drive one generated SDK of an output-defects measurement through its client.

Usage: output_defects_runtime.py CASE SDK_SRC SPEC_JSON. CASE is `615` (the
empty-composition-member document) or `617` (the annotated inherited-union
document); SDK_SRC is the generated SDK's `src/` directory holding the `fern`
package; SPEC_JSON is the measurement's `openapi.yml` as JSON. Every request goes
to an httpx.MockTransport that answers with the payload the journey chose, so
each step reads what the public client really sends and returns.

615 holds that a field composed of `$ref Kiln` and an empty `{}` member accepts
and returns `Kiln` itself, the class the package exports under that name, while
the described and constrained controls keep classes of their own. 617 holds that
each inherited variant parses through the annotated copy into that variant's
class with its discriminator value, and that each constructed variant is sent in
the wire shape the source schema validates.

Exit 0 prints one line per step; exit 1 names the first step that failed; exit
2 reports invalid arguments or an SDK or document this script cannot read.
"""

import argparse
import importlib
import json
import sys
import typing
from pathlib import Path
from typing import Any, Callable

import httpx

BASE_URL = "https://measurement.invalid"


class Failure(Exception):
    """A step whose observed behaviour is not the one the measurement states."""


def check(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


def resolve(schema: dict[str, Any], components: dict[str, Any]) -> tuple[str | None, dict[str, Any]]:
    reference = schema.get("$ref")
    if reference is None:
        return None, schema
    name = reference.rsplit("/", 1)[-1]
    return name, components[name]


def schema_errors(
    instance: Any, schema: dict[str, Any], components: dict[str, Any], at: str, dispatched: frozenset[str]
) -> list[str]:
    """The ways `instance` breaks `schema`, over the keywords these documents use.

    A `$ref` to a discriminator base is validated against the subtype its
    `mapping` names for the instance's tag, as the discriminator declares; the
    subtype's own `allOf` back to the base is then read as plain properties.
    """
    name, schema = resolve(schema, components)
    discriminator = schema.get("discriminator")
    if name is not None and discriminator and name not in dispatched:
        tag = instance.get(discriminator["propertyName"]) if isinstance(instance, dict) else None
        target = discriminator.get("mapping", {}).get(tag)
        if target is None:
            return [f"{at}: tag {tag!r} names no subtype of {name}"]
        return schema_errors(instance, {"$ref": target}, components, at, dispatched | {name})
    errors = []
    for member in schema.get("allOf", []):
        errors += schema_errors(instance, member, components, at, dispatched)
    kind = schema.get("type")
    accepted = {
        "object": lambda value: isinstance(value, dict),
        "string": lambda value: isinstance(value, str),
        "integer": lambda value: isinstance(value, int) and not isinstance(value, bool),
        "number": lambda value: isinstance(value, (int, float)) and not isinstance(value, bool),
    }
    if kind is not None and not accepted[kind](instance):
        return errors + [f"{at}: {instance!r} is not {kind}"]
    if isinstance(instance, dict):
        errors += [f"{at}: missing {key}" for key in schema.get("required", []) if key not in instance]
        for key, property_schema in schema.get("properties", {}).items():
            if key in instance:
                errors += schema_errors(instance[key], property_schema, components, f"{at}.{key}", dispatched)
    return errors


class Recorder:
    """An httpx transport answering every request with `reply`, keeping the bodies sent."""

    def __init__(self) -> None:
        self.sent: list[dict[str, Any]] = []
        self.reply: Any = None

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.sent.append(json.loads(request.content))
        return httpx.Response(200, json=self.reply)


def client(fern: Any, recorder: Recorder) -> Any:
    return fern.FernApi(base_url=BASE_URL, httpx_client=httpx.Client(transport=httpx.MockTransport(recorder)))


def empty_member_keeps_the_reference(fern: Any, spec: dict[str, Any], say: Callable[[str], None]) -> None:
    kiln_class = fern.Kiln
    hints = typing.get_type_hints(fern.Load)
    check(hints["kiln"] is kiln_class, f"Load.kiln is typed {hints['kiln']!r}, not the exported Kiln")
    check(
        typing.get_args(hints["overflow_kiln"])[0] is kiln_class,
        f"Load.overflow_kiln is typed {hints['overflow_kiln']!r}, not Optional[Kiln]",
    )
    say("Load.kiln and Load.overflow_kiln are typed with the exported Kiln")
    for control in ("LoadNotedKiln", "LoadReservedKiln"):
        check(getattr(fern, control) is not kiln_class, f"{control} is Kiln itself")
    say("the described and constrained controls export LoadNotedKiln and LoadReservedKiln")

    recorder = Recorder()
    loads = client(fern, recorder).loads
    payload = {
        "label": "bisque",
        "kiln": {"name": "Annex", "maxCone": 10},
        "overflowKiln": {"name": "Shed"},
        "notedKiln": {"name": "Log"},
        "reservedKiln": {"name": "Main", "reservedUntil": "2026-11-02"},
    }
    recorder.reply = payload
    sent_kiln = kiln_class(name="Annex", max_cone=10)
    load = loads.schedule_load(
        label="bisque",
        kiln=sent_kiln,
        overflow_kiln=kiln_class(name="Shed"),
        noted_kiln=fern.LoadNotedKiln(name="Log"),
        reserved_kiln=fern.LoadReservedKiln(name="Main", reserved_until="2026-11-02"),
    )
    check(recorder.sent[-1] == payload, f"schedule_load sent {recorder.sent[-1]!r}")
    errors = schema_errors(recorder.sent[-1], {"$ref": "#/components/schemas/Load"}, spec["components"]["schemas"], "body", frozenset())
    check(not errors, "; ".join(errors))
    say(f"schedule_load sent {json.dumps(recorder.sent[-1], sort_keys=True)}, which Load validates")
    for field in ("kiln", "overflow_kiln"):
        returned = getattr(load, field)
        check(type(returned) is kiln_class, f"returned Load.{field} is {type(returned).__name__}, not Kiln")
    check(load.kiln == sent_kiln, f"returned Load.kiln {load.kiln!r} differs from the Kiln sent")
    check(type(load.noted_kiln) is fern.LoadNotedKiln, f"noted_kiln parsed as {type(load.noted_kiln).__name__}")
    check(
        type(load.reserved_kiln) is fern.LoadReservedKiln,
        f"reserved_kiln parsed as {type(load.reserved_kiln).__name__}",
    )
    say("the returned Load holds Kiln at kiln and overflow_kiln, LoadNotedKiln and LoadReservedKiln at the controls")

    recorder.reply = payload
    destination = kiln_class(name="Annex")
    hints = typing.get_type_hints(type(loads).transfer_load)
    check(hints["destination"] is kiln_class, f"transfer_load's destination is typed {hints['destination']!r}")
    loads.transfer_load("load-7", destination=destination)
    check(recorder.sent[-1] == {"destination": {"name": "Annex"}}, f"transfer_load sent {recorder.sent[-1]!r}")
    say("transfer_load takes destination as Kiln and sends it unchanged")


def annotated_copy_keeps_the_variants(fern: Any, spec: dict[str, Any], say: Callable[[str], None]) -> None:
    schemas = spec["components"]["schemas"]
    variants = {
        "matte": ({"finish": "matte", "layers": 2, "tooth": 3}, {"layers": 2, "tooth": 3}),
        "gloss": ({"finish": "gloss", "layers": 1, "sheen": 0.8}, {"layers": 1, "sheen": 0.8}),
    }
    recorder = Recorder()
    pots = client(fern, recorder).pots
    for tag, (wire, arguments) in variants.items():
        suffix = tag.capitalize()
        parsed = fern.core.pydantic_utilities.parse_obj_as(fern.PotOuterCoat, wire)
        check(
            type(parsed).__name__ == f"PotOuterCoat_{suffix}",
            f"{wire!r} parsed through PotOuterCoat as {type(parsed).__name__}, not PotOuterCoat_{suffix}",
        )
        for exported in (f"PotOuterCoat_{suffix}", f"RecoatPotRequestCoat_{suffix}"):
            check(hasattr(fern, exported), f"the package exports no {exported}")
        copy_class = getattr(fern, f"PotOuterCoat_{suffix}")
        body_class = getattr(fern, f"RecoatPotRequestCoat_{suffix}")
        recorder.reply = {"potter": "Ines", "outerCoat": wire}
        pot = pots.record_pot(potter="Ines", outer_coat=copy_class(**arguments))
        sent = recorder.sent[-1]
        check(sent == {"potter": "Ines", "outerCoat": wire}, f"record_pot sent {sent!r}")
        errors = schema_errors(sent["outerCoat"], {"$ref": "#/components/schemas/Coat"}, schemas, "outerCoat", frozenset())
        check(not errors, "; ".join(errors))
        say(f"PotOuterCoat_{suffix} is sent as {json.dumps(sent['outerCoat'], sort_keys=True)}, which Coat validates")
        check(
            type(pot.outer_coat) is copy_class,
            f"outerCoat {wire!r} parsed as {type(pot.outer_coat).__name__}, not PotOuterCoat_{suffix}",
        )
        check(pot.outer_coat.finish == tag, f"PotOuterCoat_{suffix}.finish is {pot.outer_coat.finish!r}")
        say(f"outerCoat {json.dumps(wire, sort_keys=True)} parses as PotOuterCoat_{suffix} with finish {tag!r}")

        recorder.reply = {"potter": "Ines", "outerCoat": wire}
        pots.recoat_pot("pot-3", coat=body_class(**arguments))
        sent = recorder.sent[-1]
        check(sent == {"coat": wire}, f"recoat_pot sent {sent!r}")
        errors = schema_errors(sent["coat"], {"$ref": "#/components/schemas/Coat"}, schemas, "coat", frozenset())
        check(not errors, "; ".join(errors))
        say(f"RecoatPotRequestCoat_{suffix} is sent as {json.dumps(sent['coat'], sort_keys=True)}, which Coat validates")
        parsed = fern.core.pydantic_utilities.parse_obj_as(fern.RecoatPotRequestCoat, wire)
        check(type(parsed) is body_class, f"{wire!r} parsed as {type(parsed).__name__}, not RecoatPotRequestCoat_{suffix}")
        say(f"{json.dumps(wire, sort_keys=True)} parses as RecoatPotRequestCoat_{suffix}")


JOURNEYS = {"615": empty_member_keeps_the_reference, "617": annotated_copy_keeps_the_variants}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("case", choices=sorted(JOURNEYS))
    parser.add_argument("sdk_src", type=Path)
    parser.add_argument("spec", type=Path)
    args = parser.parse_args()
    if not (args.sdk_src / "fern" / "__init__.py").is_file():
        print(f"{args.sdk_src} must contain the generated fern package; pass the SDK's src/ directory", file=sys.stderr)
        return 2
    try:
        spec = json.loads(args.spec.read_text(encoding="utf-8"))
        spec["components"]["schemas"]
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f"cannot read {args.spec} as an OpenAPI document with components ({error}); pass the measurement as JSON", file=sys.stderr)
        return 2
    sys.path.insert(0, str(args.sdk_src.resolve()))
    fern = importlib.import_module("fern")
    importlib.import_module("fern.core.pydantic_utilities")
    try:
        JOURNEYS[args.case](fern, spec, print)
    except Failure as failure:
        print(f"{args.case}: {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

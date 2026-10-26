"""Drive one generated SDK of an output-defects measurement through its client.

Usage: output_defects_runtime.py CASE SDK_SRC SPEC_JSON. CASE is `615` (the
empty-composition-member document) or `617` (the annotated inherited-union
document); SDK_SRC is the generated SDK's `src/` directory holding the `fern`
package; SPEC_JSON is the measurement's `openapi.yml` as JSON. Every request goes
over a socket to a local HTTP server that answers with the payload the journey
chose, so each step reads what the public client really sends and returns.

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
import contextlib
import http.server
import importlib
import json
import sys
import threading
import typing
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import Any, NamedTuple

import pydantic

# The schemas each journey validates against; a document without them is not the measurement.
CASE_SCHEMAS = {"615": ("Load", "Kiln"), "617": ("Coat", "MatteCoat", "GlossCoat")}
# The names each journey reads off the generated package; an SDK without them is not this measurement's.
CASE_EXPORTS = {
    "615": ("FernApi", "Kiln", "Load", "LoadNotedKiln", "LoadReservedKiln"),
    "617": ("FernApi", "PotOuterCoat", "RecoatPotRequestCoat"),
}


class Failure(Exception):
    """A step whose observed behaviour is not the one the measurement states."""


def check(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


# The `type` values the walker reads, each with the instances it accepts.
ACCEPTED: dict[str, Callable[[Any], bool]] = {
    "object": lambda value: isinstance(value, dict),
    "string": lambda value: isinstance(value, str),
    "integer": lambda value: isinstance(value, int) and not isinstance(value, bool),
    "number": lambda value: isinstance(value, (int, float)) and not isinstance(value, bool),
}
REF_PREFIX = "#/components/schemas/"


def component_name(reference: Any, components: dict[str, Any]) -> str | None:
    """The component a local `$ref` names, or None for any other value."""
    if not isinstance(reference, str) or not reference.startswith(REF_PREFIX):
        return None
    name = reference.removeprefix(REF_PREFIX)
    return name if name in components else None


def all_of_cycle(components: dict[str, Any]) -> list[str] | None:
    """A chain of components each `allOf`-referencing the next back to the first, if any.

    The walker descends `allOf` without consuming the instance, so such a chain
    never ends; a discriminator's mapping is not an edge, because the walker
    dispatches each base once.
    """

    def references(schema: dict[str, Any]) -> list[str]:
        """The components `schema`'s `allOf` reaches before consuming the instance, nested members included."""
        found = []
        for member in schema.get("allOf", []):
            if (target := component_name(member.get("$ref"), components)) is not None:
                found.append(target)
            found += references(member)
        return found

    def edges(name: str) -> list[str]:
        return references(components[name])

    done: set[str] = set()

    def visit(name: str, path: list[str]) -> list[str] | None:
        if name in path:
            return [*path[path.index(name) :], name]
        if name in done:
            return None
        for target in edges(name):
            if (cycle := visit(target, [*path, name])) is not None:
                return cycle
        done.add(name)
        return None

    for name in components:
        if (cycle := visit(name, [])) is not None:
            return cycle
    return None


def shape_errors(schema: Any, components: dict[str, Any], at: str) -> list[str]:
    """Where `schema` is not a shape `schema_errors` can walk without failing."""
    if not isinstance(schema, dict):
        return [f"{at} is not an object"]
    errors = []
    if "$ref" in schema and component_name(schema["$ref"], components) is None:
        errors.append(f"{at}.$ref {schema['$ref']!r} names no component schema as {REF_PREFIX}<name>")
    if "type" in schema and not (isinstance(schema["type"], str) and schema["type"] in ACCEPTED):
        errors.append(f"{at}.type {schema['type']!r} is not one of {sorted(ACCEPTED)}")
    required = schema.get("required", [])
    if not (isinstance(required, list) and all(isinstance(key, str) for key in required)):
        errors.append(f"{at}.required is not a list of property names")
    members = schema.get("allOf", [])
    if not isinstance(members, list):
        errors.append(f"{at}.allOf is not a list")
    else:
        for index, member in enumerate(members):
            errors += shape_errors(member, components, f"{at}.allOf[{index}]")
    properties = schema.get("properties", {})
    if not isinstance(properties, dict):
        errors.append(f"{at}.properties is not an object")
    else:
        for key, value in properties.items():
            errors += shape_errors(value, components, f"{at}.properties.{key}")
    if "discriminator" in schema:
        discriminator = schema["discriminator"]
        mapping = discriminator.get("mapping", {}) if isinstance(discriminator, dict) else None
        if not isinstance(mapping, dict) or not isinstance(discriminator.get("propertyName"), str):
            errors.append(f"{at}.discriminator needs a string propertyName and an object mapping")
        else:
            for tag, target in mapping.items():
                errors += shape_errors({"$ref": target}, components, f"{at}.discriminator.mapping.{tag}")
    return errors


def resolve(schema: dict[str, Any], components: dict[str, Any]) -> tuple[str | None, dict[str, Any]]:
    reference = schema.get("$ref")
    if reference is None:
        return None, schema
    name = reference.removeprefix(REF_PREFIX)
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
    if kind is not None and not ACCEPTED[kind](instance):
        return [*errors, f"{at}: {instance!r} is not {kind}"]
    if isinstance(instance, dict):
        errors += [f"{at}: missing {key}" for key in schema.get("required", []) if key not in instance]
        for key, property_schema in schema.get("properties", {}).items():
            if key in instance:
                errors += schema_errors(instance[key], property_schema, components, f"{at}.{key}", dispatched)
    return errors


class Recorder:
    """What the local server answers with (`reply`) and the JSON bodies it received."""

    def __init__(self) -> None:
        self.sent: list[dict[str, Any]] = []
        self.reply: Any = None


@contextlib.contextmanager
def serving(recorder: Recorder) -> Iterator[str]:
    """A local HTTP server answering every request from `recorder`; yields its base URL."""

    class Handler(http.server.BaseHTTPRequestHandler):
        def answer(self) -> None:
            length = int(self.headers.get("Content-Length", "0"))
            recorder.sent.append(json.loads(self.rfile.read(length)))
            body = json.dumps(recorder.reply).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        do_POST = do_PUT = do_PATCH = answer

        def log_message(self, format: str, *args: Any) -> None:
            pass

    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{httpd.server_address[1]}"
    finally:
        httpd.shutdown()
        httpd.server_close()


class Variant(NamedTuple):
    """One inherited variant: its tag, its wire payload, and its constructor arguments."""

    tag: str
    wire: dict[str, Any]
    arguments: dict[str, Any]


# llmlint: ignore-block[async_typed_clients_at_boundaries] These calls are the subject under test, not a client this script owns: the generated SDK's synchronous FernApi is what the measurement's runtime.txt drives over Fern's tree, and its model typing is what #615 and #617 settle.
def empty_member_keeps_the_reference(
    fern: Any, spec: dict[str, Any], base_url: str, recorder: Recorder, say: Callable[[str], None]
) -> None:
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

    loads = fern.FernApi(base_url=base_url).loads
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
    errors = schema_errors(
        recorder.sent[-1], {"$ref": "#/components/schemas/Load"}, spec["components"]["schemas"], "body", frozenset()
    )
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


VARIANTS = (
    Variant("matte", {"finish": "matte", "layers": 2, "tooth": 3}, {"layers": 2, "tooth": 3}),
    Variant("gloss", {"finish": "gloss", "layers": 1, "sheen": 0.8}, {"layers": 1, "sheen": 0.8}),
)


def annotated_copy_keeps_the_variants(
    fern: Any, spec: dict[str, Any], base_url: str, recorder: Recorder, say: Callable[[str], None]
) -> None:
    schemas = spec["components"]["schemas"]
    pots = fern.FernApi(base_url=base_url).pots
    for tag, wire, arguments in VARIANTS:
        suffix = tag.capitalize()
        parsed = pydantic.TypeAdapter(fern.PotOuterCoat).validate_python(wire)
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
        errors = schema_errors(
            sent["outerCoat"], {"$ref": "#/components/schemas/Coat"}, schemas, "outerCoat", frozenset()
        )
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
        say(
            f"RecoatPotRequestCoat_{suffix} is sent as {json.dumps(sent['coat'], sort_keys=True)}, which Coat validates"
        )
        parsed = pydantic.TypeAdapter(fern.RecoatPotRequestCoat).validate_python(wire)
        check(
            type(parsed) is body_class, f"{wire!r} parsed as {type(parsed).__name__}, not RecoatPotRequestCoat_{suffix}"
        )
        say(f"{json.dumps(wire, sort_keys=True)} parses as RecoatPotRequestCoat_{suffix}")


# llmlint: ignore-end[async_typed_clients_at_boundaries]


JOURNEYS = {"615": empty_member_keeps_the_reference, "617": annotated_copy_keeps_the_variants}


def read_spec(path: Path, case: str) -> dict[str, Any]:
    """The measurement document, or ValueError naming what it lacks or what the walker cannot read."""
    spec = json.loads(path.read_text(encoding="utf-8"))
    components = spec.get("components") if isinstance(spec, dict) else None
    schemas = components.get("schemas") if isinstance(components, dict) else None
    if not isinstance(schemas, dict):
        raise ValueError("components.schemas is not an object")
    missing = [name for name in CASE_SCHEMAS[case] if not isinstance(schemas.get(name), dict)]
    if missing:
        raise ValueError(f"components.schemas lacks {', '.join(missing)}")
    errors = [error for name, schema in schemas.items() for error in shape_errors(schema, schemas, name)]
    if errors:
        raise ValueError("; ".join(errors))
    if (cycle := all_of_cycle(schemas)) is not None:
        raise ValueError(f"allOf references cycle through {' -> '.join(cycle)}")
    return spec


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
        spec = read_spec(args.spec, args.case)
    except (OSError, ValueError) as error:
        print(
            f"cannot read {args.spec} as the {args.case} measurement document ({error}); pass the measurement as JSON",
            file=sys.stderr,
        )
        return 2
    sys.path.insert(0, str(args.sdk_src.resolve()))
    try:
        fern = importlib.import_module("fern")
    except Exception as error:  # any import failure means the SDK input is unusable
        print(f"cannot import the fern package under {args.sdk_src} ({error!r}); regenerate the SDK", file=sys.stderr)
        return 2
    absent = [name for name in CASE_EXPORTS[args.case] if not hasattr(fern, name)]
    if absent:
        print(
            f"the fern package under {args.sdk_src} exports no {', '.join(absent)}; "
            f"pass the SDK generated from the {args.case} measurement",
            file=sys.stderr,
        )
        return 2
    recorder = Recorder()
    try:
        with serving(recorder) as base_url:
            JOURNEYS[args.case](fern, spec, base_url, recorder, say=print)
    except Failure as failure:
        print(f"{args.case}: {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

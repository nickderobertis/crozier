# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as int64-example-rounded-out-of-range.py does; crozier-e2e reads this folder through its e2eReads input.
"""Validate one worked-example value Fern writes, and crozier's, against its schema.

Reads the keyword argument ARGUMENT from one line of Fern's committed tree and
from the same place in crozier's generated tree, and validates each value
against the schema at POINTER in the source document SOURCE with jsonschema
(format assertions on): an OpenAPI 3.1 document under Draft 2020-12, a 3.0 one
under Draft 4, whose `exclusiveMinimum: true` it shares.

Exit 0 prints both verdicts when Fern's value is rejected and crozier's is
accepted; exit 1 prints them when not; exit 2 reports invalid input on stderr.
"""

from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path
from typing import Any

import jsonschema
import referencing


class InputError(ValueError):
    """An argument or file the validation cannot read."""


def load_document(path: Path) -> dict[str, Any]:
    """The source document, read as JSON, or as YAML where PyYAML is present."""
    text = path.read_text(encoding="utf-8")
    try:
        document = json.loads(text)
    except json.JSONDecodeError:
        try:
            import yaml  # noqa: PLC0415 - only a YAML document needs it
        except ImportError as error:
            raise InputError(f"{path} is not JSON, and PyYAML is not installed to read it") from error
        document = yaml.safe_load(text)
    if not isinstance(document, dict):
        raise InputError(f"{path} is not an OpenAPI document")
    return document


def line_value(place: str, argument: str) -> object:
    """The value `argument=` takes on the 1-based line `FILE:LINE`."""
    file, _, number = place.rpartition(":")
    if not file or not number.isdigit():
        raise InputError(f"{place} is not FILE:LINE")
    lines = Path(file).read_text(encoding="utf-8").splitlines()
    index = int(number) - 1
    if not 0 <= index < len(lines):
        raise InputError(f"{place} is past the end of {file}")
    text = lines[index].strip().removesuffix(",")
    try:
        call = ast.parse(f"f({text})", mode="eval").body
    except SyntaxError as error:
        raise InputError(f"{place} holds no keyword argument: {lines[index]!r}") from error
    if isinstance(call, ast.Call):
        for keyword in call.keywords:
            if keyword.arg == argument:
                return ast.literal_eval(keyword.value)
    raise InputError(f"{place} passes no {argument}=: {lines[index]!r}")


def verdict(document: dict[str, Any], pointer: str, value: object) -> str | None:
    """Why the schema at `pointer` rejects `value`, or `None` when it accepts it."""
    version = str(document.get("openapi", ""))
    validator_class = (
        jsonschema.Draft202012Validator if version.startswith("3.1") else jsonschema.Draft4Validator
    )
    specification = (
        referencing.jsonschema.DRAFT202012 if version.startswith("3.1") else referencing.jsonschema.DRAFT4
    )
    resource = referencing.Resource.from_contents(document, default_specification=specification)
    registry = referencing.Registry().with_resource("urn:source", resource)
    validator = validator_class(
        {"$ref": f"urn:source#{pointer}"},
        registry=registry,
        format_checker=validator_class.FORMAT_CHECKER,
    )
    error = jsonschema.exceptions.best_match(validator.iter_errors(value))
    return None if error is None else error.message


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("source", type=Path, help="the OpenAPI document both trees were generated from")
    parser.add_argument("pointer", help="the JSON pointer of the value's schema, e.g. /components/schemas/Id")
    parser.add_argument("fern", help="Fern's committed FILE:LINE")
    parser.add_argument("crozier", help="crozier's generated FILE:LINE")
    parser.add_argument("argument", help="the keyword argument whose value is validated")
    arguments = parser.parse_args(argv)
    try:
        document = load_document(arguments.source)
        values = {
            "fern": line_value(arguments.fern, arguments.argument),
            "crozier": line_value(arguments.crozier, arguments.argument),
        }
        verdicts = {side: verdict(document, arguments.pointer, value) for side, value in values.items()}
    except (InputError, OSError, referencing.exceptions.Unresolvable) as error:
        print(f"validate.py: {error}", file=sys.stderr)
        return 2
    for side, value in values.items():
        reason = verdicts[side]
        said = "accepted" if reason is None else f"rejected: {reason}"
        print(f"{side} {arguments.argument}={value!r}: {said}")
    return 0 if verdicts["fern"] is not None and verdicts["crozier"] is None else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

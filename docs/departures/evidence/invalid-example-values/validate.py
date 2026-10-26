# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as int64-example-rounded-out-of-range.py does; crozier-e2e reads this folder through its e2eReads input.
"""Validate one worked-example value Fern writes, and crozier's, against its schema.

Reads the keyword argument ARGUMENT from one line of Fern's committed tree and
from the same place in crozier's generated tree, and validates each value
against the schema at POINTER in the source document SOURCE with jsonschema
(format assertions on): an OpenAPI 3.1 document under Draft 2020-12, a 3.0 one
under Draft 4, whose `exclusiveMinimum: true` it shares. jsonschema asserts some
formats only with optional packages installed; for the formats crozier's
inventory reads (`date`, `date-time`, `time`, `uuid`, `email`, `uri`, `ipv4`,
`ipv6`, `hostname`) any it cannot assert is asserted here with the standard
library, by the RFC each format names.

Exit 0 prints both verdicts when Fern's value is rejected and crozier's is
accepted; exit 1 prints them when not; exit 2 reports invalid input on stderr.
"""

from __future__ import annotations

import argparse
import ast
import datetime
import ipaddress
import json
import re
import sys
import uuid
from pathlib import Path
from typing import Any

import jsonschema
import referencing


class InputError(ValueError):
    """An argument or file the validation cannot read."""


OPENAPI_VERSION = re.compile(r"3\.[01]\.\d+")


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
        try:
            document = yaml.safe_load(text)
        except yaml.YAMLError as error:
            raise InputError(f"{path} is neither JSON nor YAML: {error}") from error
    if not isinstance(document, dict) or not OPENAPI_VERSION.fullmatch(str(document.get("openapi", ""))):
        raise InputError(f"{path} is not an OpenAPI 3.0 or 3.1 document")
    return document


def schema_at(document: dict[str, Any], pointer: str) -> object:
    """The schema the JSON pointer names in `document`."""
    if not pointer.startswith("/"):
        raise InputError(f"{pointer} is not a JSON pointer")
    node: object = document
    for part in pointer.split("/")[1:]:
        key = part.replace("~1", "/").replace("~0", "~")
        match node:
            case dict() if key in node:
                node = node[key]
            case list() if key.isdigit() and int(key) < len(node):
                node = node[int(key)]
            case _:
                raise InputError(f"{pointer} names nothing in the document")
    if not isinstance(node, (dict, bool)):
        raise InputError(f"{pointer} names no schema")
    return node


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
                try:
                    return ast.literal_eval(keyword.value)
                except (ValueError, SyntaxError) as error:
                    raise InputError(f"{place} passes {argument}= no literal value: {lines[index]!r}") from error
    raise InputError(f"{place} passes no {argument}=: {lines[index]!r}")


HOSTNAME_LABEL = re.compile(r"(?!-)[A-Za-z0-9-]{1,63}(?<!-)")
SCHEME = re.compile(r"[A-Za-z][A-Za-z0-9+.-]*")
TIME = re.compile(r"(\d{2}):(\d{2}):(\d{2})(\.\d+)?([Zz]|[+-]\d{2}:\d{2})")


def is_hostname(value: str) -> bool:
    """RFC 1123: dot-separated labels of letters, digits and inner hyphens."""
    name = value.removesuffix(".")
    return 0 < len(name) <= 253 and all(HOSTNAME_LABEL.fullmatch(label) for label in name.split("."))


UNRESERVED = r"A-Za-z0-9\-._~"
SUB_DELIMS = r"!$&'()*+,;="
PCT_ENCODED = r"%[0-9A-Fa-f]{2}"
PCHAR = rf"(?:[{UNRESERVED}{SUB_DELIMS}:@]|{PCT_ENCODED})"
URI = re.compile(
    rf"[A-Za-z][A-Za-z0-9+.-]*:"
    rf"(?://(?:(?:[{UNRESERVED}{SUB_DELIMS}:]|{PCT_ENCODED})*@)?"
    rf"(?:\[[0-9A-Fa-f:.]+\]|(?:[{UNRESERVED}{SUB_DELIMS}]|{PCT_ENCODED})*)(?::[0-9]*)?)?"
    rf"(?:/?{PCHAR}*(?:/{PCHAR}*)*)"
    rf"(?:\?(?:{PCHAR}|[/?])*)?"
    rf"(?:#(?:{PCHAR}|[/?])*)?"
)


def is_uri(value: str) -> bool:
    """RFC 3986 `URI`: a scheme, then an optional authority whose host may be an
    IP literal in brackets, a path, query and fragment of unreserved,
    sub-delimiter and percent-encoded characters."""
    return URI.fullmatch(value) is not None


def is_time(value: str) -> bool:
    """RFC 3339 `full-time`, its numeric offset inside a day."""
    match = TIME.fullmatch(value)
    if match is None or int(match[1]) >= 24 or int(match[2]) >= 60 or int(match[3]) > 60:
        return False
    offset = match[5]
    return offset in ("Z", "z") or (int(offset[1:3]) < 24 and int(offset[4:6]) < 60)


def is_date_time(value: str) -> bool:
    """RFC 3339 `date-time`."""
    date, separator, time = value.partition("T") if "T" in value else value.partition("t")
    try:
        datetime.date.fromisoformat(date)
    except ValueError:
        return False
    return bool(separator) and len(date) == 10 and is_time(time)


def is_date(value: str) -> bool:
    """RFC 3339 `full-date`."""
    try:
        datetime.date.fromisoformat(value)
    except ValueError:
        return False
    return len(value) == 10


def is_uuid(value: str) -> bool:
    """RFC 4122's hyphenated form."""
    try:
        uuid.UUID(value)
    except ValueError:
        return False
    return len(value) == 36 and all(value[i] == "-" for i in (8, 13, 18, 23))


def is_ip(version: int):
    """An IP address of `version` in its textual form."""

    def check(value: str) -> bool:
        try:
            return ipaddress.ip_address(value).version == version
        except ValueError:
            return False

    return check


STANDARD_LIBRARY_FORMATS = {
    "date": is_date,
    "date-time": is_date_time,
    "time": is_time,
    "uuid": is_uuid,
    "uri": is_uri,
    "ipv4": is_ip(4),
    "ipv6": is_ip(6),
    "hostname": is_hostname,
}


def format_checker(validator_class: type) -> jsonschema.FormatChecker:
    """jsonschema's checker, with each in-scope format it cannot assert added."""
    checker = validator_class.FORMAT_CHECKER
    added = jsonschema.FormatChecker(list(checker.checkers))
    added.checkers = dict(checker.checkers)
    for name, check in STANDARD_LIBRARY_FORMATS.items():
        if name not in added.checkers:
            added.checks(name)(lambda value, check=check: not isinstance(value, str) or check(value))
    return added


def verdict(document: dict[str, Any], pointer: str, value: object) -> str | None:
    """Why the schema at `pointer` rejects `value`, or `None` when it accepts it."""
    schema = schema_at(document, pointer)
    version = str(document.get("openapi", ""))
    validator_class = (
        jsonschema.Draft202012Validator if version.startswith("3.1") else jsonschema.Draft4Validator
    )
    specification = (
        referencing.jsonschema.DRAFT202012 if version.startswith("3.1") else referencing.jsonschema.DRAFT4
    )
    resource = referencing.Resource.from_contents(document, default_specification=specification)
    registry = referencing.Registry().with_resource("urn:source", resource)
    try:
        validator_class.check_schema(schema)
    except jsonschema.exceptions.SchemaError as error:
        raise InputError(f"{pointer} is no valid schema: {error.message}") from error
    validator = validator_class(
        {"$ref": f"urn:source#{pointer}"},
        registry=registry,
        format_checker=format_checker(validator_class),
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
    except (
        InputError,
        OSError,
        referencing.exceptions.Unresolvable,
        jsonschema.exceptions.SchemaError,
        re.error,
    ) as error:
        print(f"validate.py: {error}", file=sys.stderr)
        return 2
    for side, value in values.items():
        reason = verdicts[side]
        said = "accepted" if reason is None else f"rejected: {reason}"
        print(f"{side} {arguments.argument}={value!r}: {said}")
    return 0 if verdicts["fern"] is not None and verdicts["crozier"] is None else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as int64-example-rounded-out-of-range.py does; crozier-e2e reads this folder through its e2eReads input.
"""Validate one worked-example value Fern writes, and crozier's, against its schema.

Reads the keyword argument ARGUMENT from one line of Fern's committed tree and
from the same place in crozier's generated tree, and validates each value
against the schema at POINTER in the source document SOURCE with jsonschema
(format assertions on): an OpenAPI 3.1 document under Draft 2020-12, a 3.0 one
under Draft 4, whose `exclusiveMinimum: true` it shares. Fern's place may be
`-` where Fern writes no value there, which no schema accepts.

A value is read as its wire JSON: a literal as it stands, bytes as the string of
their octets, a `datetime` constructor as its RFC 3339 string, and a model
constructor (`Name(field=…)`: a bare class name, keywords only) as an object of its keyword names,
each nested value read the same way, so a value reached through `$ref`, `allOf`,
`anyOf` or `oneOf` is validated whole. A line inside a docstring of a Python
file is read as the docstring renders it, its escapes applied, as `help()` shows
it and a reader copies it; a rendered line that is no Python is rejected.
jsonschema asserts some
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
import warnings
from pathlib import Path
from typing import Any, NamedTuple

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


TEMPORAL_CALLS = ("datetime.date.fromisoformat", "datetime.datetime.fromisoformat")


def temporal_literal(node: ast.expr) -> str | None:
    """The wire string a `datetime.date.fromisoformat("…")` or
    `datetime.datetime.fromisoformat("…")` argument stands for, or `None` for
    any other expression: a date as written, a date-time in its RFC 3339 `T` form."""
    if not (
        isinstance(node, ast.Call)
        and ast.unparse(node.func) in TEMPORAL_CALLS
        and len(node.args) == 1
        and not node.keywords
        and isinstance(node.args[0], ast.Constant)
        and isinstance(node.args[0].value, str)
    ):
        return None
    text = node.args[0].value
    return text.replace(" ", "T", 1) if ast.unparse(node.func).endswith("datetime.fromisoformat") else text


def wire_value(node: ast.expr) -> object:
    """The JSON value the expression `node` stands for on the wire."""
    if (temporal := temporal_literal(node)) is not None:
        return temporal
    match node:
        case ast.Call(func=ast.Name(), args=[], keywords=keywords) if all(
            keyword.arg is not None for keyword in keywords
        ):
            return {keyword.arg: wire_value(keyword.value) for keyword in keywords}
        case ast.List(elts=items) | ast.Tuple(elts=items):
            return [wire_value(item) for item in items]
        case ast.Dict(keys=keys, values=values) if all(isinstance(key, ast.Constant) for key in keys):
            return {ast.literal_eval(key): wire_value(value) for key, value in zip(keys, values, strict=True)}
    value = ast.literal_eval(node)
    return value.decode("latin-1") if isinstance(value, bytes) else value


class Span(NamedTuple):
    """A docstring's 0-based first and last source line, and whether it is raw."""

    first: int
    last: int
    raw: bool


def docstring_spans(text: str) -> list[Span]:
    """The span of each docstring in the Python source `text`; none where
    `text` is no Python."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    lines = text.splitlines()
    spans = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
            and node.end_lineno is not None
        ):
            prefix = lines[node.lineno - 1][node.col_offset :].split('"', 1)[0].split("'", 1)[0]
            spans.append(Span(node.lineno - 1, node.end_lineno - 1, "r" in prefix.lower()))
    return spans


def render_line(line: str) -> str:
    """The interior docstring line `line` as a non-raw docstring renders it; a
    line ending in a continuation backslash, which no single line renders, stays."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SyntaxWarning)
        try:
            return ast.literal_eval('"""' + line.replace('"""', '\\"""') + '"""')
        except (SyntaxError, ValueError):
            return line


def rendered(lines: list[str], text: str) -> list[str]:
    """`lines` with each interior line of a non-raw docstring as that docstring
    renders it. A rendered line keeps its place, so a `\\n` escape that renders a
    newline leaves a line holding one, which parses as no Python."""
    spans = docstring_spans(text)
    return [
        render_line(line)
        if "\\" in line and any(span.first < index < span.last and not span.raw for span in spans)
        else line
        for index, line in enumerate(lines)
    ]


def argument_text(lines: list[str], index: int) -> str:
    """The keyword argument opening on `lines[index]`, joined with the lines a
    bracket it leaves open continues onto: the formatted docstring writes a date
    as `day=datetime.date.fromisoformat(` with its string and `)` below it."""
    text = lines[index].strip()
    following = index + 1
    while text.count("(") + text.count("[") + text.count("{") > (
        text.count(")") + text.count("]") + text.count("}")
    ) and following < len(lines):
        text += lines[following].strip()
        following += 1
    return text.removesuffix(",")


def line_value(place: str, argument: str) -> object:
    """The value `argument=` takes on the 1-based line `FILE:LINE`, the lines an
    open bracket continues it onto included."""
    file, _, number = place.rpartition(":")
    if not file or not number.isdigit():
        raise InputError(f"{place} is not FILE:LINE")
    source = Path(file).read_text(encoding="utf-8")
    lines = source.splitlines()
    index = int(number) - 1
    if not 0 <= index < len(lines):
        raise InputError(f"{place} is past the end of {file}")
    shown = rendered(lines, source)
    text = argument_text(shown, index)
    try:
        call = ast.parse(f"f({text})", mode="eval").body
    except SyntaxError as error:
        if shown[index] != lines[index]:
            return Unrendered(shown[index])
        raise InputError(f"{place} holds no keyword argument: {lines[index]!r}") from error
    if isinstance(call, ast.Call):
        for keyword in call.keywords:
            if keyword.arg == argument:
                try:
                    return wire_value(keyword.value)
                except (ValueError, SyntaxError) as error:
                    raise InputError(f"{place} passes {argument}= no literal value: {lines[index]!r}") from error
    raise InputError(f"{place} passes no {argument}=: {lines[index]!r}")


class Absent:
    """Fern writes no value at this place."""

    def __repr__(self) -> str:
        return "(no value)"


class Unrendered(str):
    """A docstring line whose escapes render it as no Python."""

    def __repr__(self) -> str:
        return f"(renders as {str(self)!r})"


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
    if isinstance(value, Absent):
        return "no value is written"
    if isinstance(value, Unrendered):
        return "its docstring renders it as no Python literal"
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
    parser.add_argument("fern", help="Fern's committed FILE:LINE, or - where Fern writes no value")
    parser.add_argument("crozier", help="crozier's generated FILE:LINE")
    parser.add_argument("argument", help="the keyword argument whose value is validated")
    arguments = parser.parse_args(argv)
    try:
        document = load_document(arguments.source)
        values = {
            "fern": Absent() if arguments.fern == "-" else line_value(arguments.fern, arguments.argument),
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

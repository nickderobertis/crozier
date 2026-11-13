#!/usr/bin/env python3
"""The combination population screen: one counted, crozier-only verdict per candidate.

This module is the one authoritative statement of
`docs/openapi-surface/witness-search-combination-populations/screen.tsv`, the table
the four combination proof nodes generate from. It declares the table's columns
and admitted values ([`COLUMNS`], [`POPULATIONS`], [`STATUSES`], [`CONDITIONS`]),
reads it ([`read_screen`], which refuses a malformed or duplicate row and a row
whose `status` disagrees with its `licence` and `trigger`), and writes it: the
`screen` command computes each candidate's licence and trigger from the exact bytes
its `sha256` names, with crozier's own census and no Fern. Every consumer reads the
table through [`read_screen`].

The status rule ([`status_of`]):

* `licence` and `trigger` both `unread:<reason>` (the bytes could not be had) is
  `unfetchable:<reason>`;
* a `trigger` that is `partial:<condition>` or `absent` is `rejected-trigger`;
* an `exact` trigger is `certified-screen-pending` under an `admissible:` licence
  and `rejected-licence` under an `inadmissible:` one.

Anything else (a read trigger beside bytes the licence could not read, an exact
trigger whose licence was never read) is no row at all: the screen refuses to
write it and the reader refuses to read it.

The licence is read as `tools/witness-search/witness_screen.py` reads it: the
document's own `info.license` decides wherever it says anything, and only a
document that declares none falls back to its recorded grant — the corpus row's
for a registered document, the repository licence file at the pinned commit for
a GitHub, Sourcegraph or handed-off one, and none for an APIs.guru archive copy,
whose aggregation is no publisher grant. A licence file is read from the shared
response cache, and fetched (through the guarded raw lane, `--fetch-licence`)
only for a candidate whose trigger is exact, so a bounded screen fetches no
licence path the verdict does not need.

The exact bytes of every `certified-screen-pending` row are kept in the host cache
[`cache_root`] under their SHA-256; `cached <sha256>` prints that file's path.

Exit status: 0 when the command did what it says (`check` read a whole table,
`screen` wrote one, `acquire` finished or spent its budget, `cached` found the
bytes); 1 when it refused (a malformed table, manifest or document store, an exact
candidate whose licence evidence is not cached and `--fetch-licence` is off,
missing cached bytes); 2 on a usage error.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import concurrent.futures
import csv
import functools
import gzip
import hashlib
import importlib.util
import json
import math
import os
import re
import sys
import tempfile
import time
import urllib.parse
from collections import Counter
from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from types import ModuleType
from typing import IO, Any, Generic, NamedTuple, NoReturn, TypeVar

REPO = Path(__file__).resolve().parents[2]
RECORD = REPO / "docs" / "openapi-surface" / "witness-search-combination-populations"
TABLE = RECORD / "screen.tsv"
POPULATION = RECORD / "population.tsv"


class Population(StrEnum):
    """Where a candidate was read from: the table's `population` column."""

    REGISTERED = "registered"
    APIS_GURU = "apis-guru"
    GITHUB = "github"
    SOURCEGRAPH = "sourcegraph"
    ARCHIVE = "archive"
    HANDED_OFF = "handed-off"


POPULATIONS = tuple(Population)
PENDING = "certified-screen-pending"
STATUSES = (PENDING, "rejected-trigger", "rejected-licence", "unfetchable:<reason>")
SHA = re.compile(r"[0-9a-f]{64}")
COMMIT = re.compile(r"[0-9a-f]{40}")
CORPUS_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
# A cell's free text: one line, no tab, never empty or a placeholder.
PLACEHOLDER = re.compile(r"^(?:|-|TODO|TBD|\?|n/?a|none|null|placeholder)$", re.I)


class ScreenError(ValueError):
    """A screen table, manifest or document store that is not what this module writes."""


class LicenceNotCached(ScreenError):
    """An exact candidate's licence file is not in the shared response cache, and may not be fetched."""


def fail(message: str) -> NoReturn:
    raise SystemExit(f"population-screen: {message}")


def _load(name: str, path: Path) -> ModuleType:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(f"cannot load {path}; restore it from git")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def census() -> ModuleType:
    return _load("population_screen_census", REPO / "tools" / "surface-census" / "openapi-surface-census.py")


def witness_screen() -> ModuleType:
    return _load("population_screen_witness_screen", REPO / "tools" / "witness-search" / "witness_screen.py")


@functools.cache
def schema_children() -> tuple[tuple[str, str], ...]:
    """Each keyword under which a Schema Object holds further Schema Objects, with its container shape.

    Read off the census's own object model (`OBJECTS["schema"]`), so the trigger
    walk and the census's declaration walk descend through the same keywords.
    """
    module = census()
    return tuple(
        (keyword, child.container)
        for keyword, child in module.OBJECTS["schema"].fields.items()
        if child is not None and child.kind == "schema"
    )


def unescape(segment: str) -> str:
    return urllib.parse.unquote(segment).replace("~1", "/").replace("~0", "~")


def pointer_segments(reference: str) -> list[str] | None:
    """A local `#/...` reference's unescaped segments, or None for any other reference."""
    if not reference.startswith("#/"):
        return None
    return [unescape(part) for part in reference[2:].split("/")]


_ABSENT = object()


def resolve(document: Any, reference: str) -> Any:
    """What a local JSON pointer names in `document`, or `_ABSENT` when it names nothing."""
    segments = pointer_segments(reference)
    if segments is None:
        return _ABSENT
    node = document
    for segment in segments:
        match node:
            case dict() if segment in node:
                node = node[segment]
            case list() if segment.isdigit() and int(segment) < len(node):
                node = node[int(segment)]
            case _:
                return _ABSENT
    return node


def deref(document: Any, value: Any, depth: int = 0) -> Any:
    """`value` with its local references followed (a cycle or a dangling one is None)."""
    seen: set[str] = set()
    while isinstance(value, dict) and isinstance(value.get("$ref"), str):
        reference = value["$ref"]
        if reference in seen or len(seen) > 32:
            return None
        seen.add(reference)
        target = resolve(document, reference)
        if target is _ABSENT:
            return None
        value = target
    return value


def primary_type(schema: Any) -> str | None:
    """A schema's declared type, the first non-null one of a type list."""
    match schema.get("type") if isinstance(schema, dict) else None:
        case str() as value:
            return value
        case list() as values:
            return next((item for item in values if isinstance(item, str) and item != "null"), None)
        case _:
            return None


def declares_type(schema: Any, name: str) -> bool:
    value = schema.get("type") if isinstance(schema, dict) else None
    return value == name or (isinstance(value, list) and name in value)


def children(schema: dict[Any, Any]) -> Iterator[tuple[str, str, Any]]:
    """`(keyword, member, child)` for each Schema Object directly below `schema`."""
    module = census()
    for keyword, container in schema_children():
        match container, schema.get(keyword):
            case module.MAP, dict() as members:
                for member, child in members.items():
                    yield keyword, str(member), child
            case module.LIST | module.ONE, list() as members:  # a draft-04 tuple `items` too
                for index, child in enumerate(members):
                    yield keyword, str(index), child
            case module.ONE, dict() | bool() as child:
                yield keyword, "", child


class Operation(NamedTuple):
    url: str
    method: str
    node: dict[Any, Any]
    path_item: dict[Any, Any]


def operations(document: Any) -> Iterator[Operation]:
    """Every operation crozier generates a method for: those under `paths` and 3.1 `webhooks`, in document order.

    A callback's operations and an unreferenced `components.pathItems` entry are no
    SDK surface, so no trigger is read there.
    """
    for section in ("paths", "webhooks"):
        items = document.get(section) if isinstance(document, dict) else None
        if not isinstance(items, dict):
            continue
        for url, item in items.items():
            item = deref(document, item)
            if not isinstance(item, dict):
                continue
            # The operation methods the census walks, so both walks read the same operations.
            for method in census()._HTTP_METHODS:
                node = item.get(method)
                if isinstance(node, dict):
                    yield Operation(str(url), method, node, item)


def parameters(document: Any, operation: Operation) -> list[dict[Any, Any]]:
    """An operation's parameters with its Path Item's, references followed, the operation's winning."""
    found: dict[tuple[str, str], dict[Any, Any]] = {}
    for source in (operation.path_item.get("parameters"), operation.node.get("parameters")):
        for parameter in source if isinstance(source, list) else []:
            parameter = deref(document, parameter)
            # A parameter is named by its `name` and `in`; one missing either names nothing to place.
            if (
                isinstance(parameter, dict)
                and isinstance(parameter.get("name"), str)
                and isinstance(parameter.get("in"), str)
            ):
                found[(parameter["name"], parameter["in"])] = parameter
    return list(found.values())


def media_schemas(document: Any, holder: Any) -> Iterator[Any]:
    """The schema of each media type a Request Body or Response (followed through its reference) writes."""
    holder = deref(document, holder)
    content = holder.get("content") if isinstance(holder, dict) else None
    for media in content.values() if isinstance(content, dict) else []:
        if isinstance(media, dict) and "schema" in media:
            yield media["schema"]


def schema_roots(document: Any) -> Iterator[Any]:
    """Every Schema Object root the generated SDK reads, in document order: each component (schema, parameter,
    header, request body, response) and each one an `operations` operation writes. A callback's schemas are
    no SDK surface and are not walked."""
    components = document.get("components") if isinstance(document, dict) else None
    components = components if isinstance(components, dict) else {}
    schemas = components.get("schemas")
    yield from (schemas.values() if isinstance(schemas, dict) else [])
    for section in ("parameters", "headers"):
        entries = components.get(section)
        for entry in entries.values() if isinstance(entries, dict) else []:
            if isinstance(entry, dict):
                if "schema" in entry:
                    yield entry["schema"]
                yield from media_schemas(document, entry)
    for section in ("requestBodies", "responses"):
        entries = components.get(section)
        for entry in entries.values() if isinstance(entries, dict) else []:
            yield from media_schemas(document, entry)
            headers = entry.get("headers") if isinstance(entry, dict) else None
            for header in headers.values() if isinstance(headers, dict) else []:
                if isinstance(header, dict) and "schema" in header:
                    yield header["schema"]
    for operation in operations(document):
        for parameter in parameters(document, operation):
            if "schema" in parameter:
                yield parameter["schema"]
            yield from media_schemas(document, parameter)
        yield from media_schemas(document, operation.node.get("requestBody"))
        responses = operation.node.get("responses")
        for response in responses.values() if isinstance(responses, dict) else []:
            yield from media_schemas(document, response)
            response = deref(document, response)
            headers = response.get("headers") if isinstance(response, dict) else None
            for header in headers.values() if isinstance(headers, dict) else []:
                header = deref(document, header)
                if isinstance(header, dict) and "schema" in header:
                    yield header["schema"]


def all_schemas(document: Any) -> Iterator[dict[Any, Any]]:
    """Every Schema Object below a `schema_roots` root, each once, parents before children."""
    seen: set[int] = set()
    stack = list(reversed(list(schema_roots(document))))
    while stack:
        schema = stack.pop()
        if not isinstance(schema, dict) or id(schema) in seen:
            continue
        seen.add(id(schema))
        yield schema
        stack.extend(reversed([child for _keyword, _member, child in children(schema)]))


def placed(document: Any, keyword: str) -> Iterator[tuple[dict[Any, Any], Any]]:
    """`(parent, child)` for each schema written under `keyword` of another (each property, each member, …)."""
    for schema in all_schemas(document):
        for found, _member, child in children(schema):
            if found == keyword:
                yield schema, child


Check = Callable[[], bool]


@dataclass(frozen=True)
class Site:
    """One place a key's anchor holds, with its conditions in the order they are judged."""

    conditions: tuple[tuple[str, Check], ...]

    def progress(self) -> tuple[int, str]:
        """How many conditions hold before the first that does not, and that one's name ("" when all hold)."""
        for index, (name, holds) in enumerate(self.conditions):
            if not holds():
                return index, name
        return len(self.conditions), ""


def verdict(sites: Iterable[Site]) -> str:
    """`exact` where a site meets every condition, else `partial:<first unmet>` at the furthest site, else `absent`."""
    best: tuple[int, str] | None = None
    for site in sites:
        reached, unmet = site.progress()
        if not unmet:
            return "exact"
        if best is None or reached > best[0]:
            best = (reached, unmet)
    return "absent" if best is None else f"partial:{best[1]}"


COMPONENT_SCHEMAS = "#/components/schemas/"


def nested_component_pointer(reference: Any) -> bool:
    """A local `#/components/schemas/<head>/<tail…>` pointer: a head and at least one more segment."""
    return (
        isinstance(reference, str)
        and reference.startswith(COMPONENT_SCHEMAS)
        and "/" in reference[len(COMPONENT_SCHEMAS) :]
    )


def walks_to(document: Any, reference: str) -> bool:
    """Whether crozier's component-pointer walk reaches a schema at `reference`.

    The walk follows schema keywords only (`properties`, `$defs`, `items`,
    `additionalProperties` and composition members), as the census's
    `local_schema_pointer_target` mirrors it: a tail through any other key, such as
    `definitions`, is unresolved for crozier even where a plain JSON pointer
    resolves it.
    """
    components = document.get("components") if isinstance(document, dict) else None
    schemas = components.get("schemas") if isinstance(components, dict) else None
    return census().local_schema_pointer_target(reference, schemas if isinstance(schemas, dict) else {}) is not None


def unresolved_pointer_sites(document: Any, refs: Iterable[tuple[Any, list[tuple[str, Check]]]]) -> Iterator[Site]:
    """One site per `$ref` at a placement: the placement's own conditions, then the unresolved nested pointer."""
    for reference, placement in refs:
        yield Site(
            (
                *placement,
                ("pointer-not-a-nested-component-pointer", lambda r=reference: nested_component_pointer(r)),
                ("nested-pointer-resolves", lambda r=reference: not walks_to(document, r)),
            )
        )


def through_defs(reference: Any) -> bool:
    segments = pointer_segments(reference) if isinstance(reference, str) else None
    return bool(segments and reference.startswith(COMPONENT_SCHEMAS) and len(segments) > 4 and "$defs" in segments[3:])


def properties_before_defs(reference: str) -> bool:
    segments = pointer_segments(reference) or []
    tail = segments[3:]
    return "$defs" in tail and "properties" in tail[: tail.index("$defs")]


def defs_pointer_sites(document: Any, refs: Iterable[tuple[Any, list[tuple[str, Check]]]]) -> Iterator[Site]:
    for reference, placement in refs:
        yield Site(
            (
                *placement,
                ("pointer-not-through-a-defs-member", lambda r=reference: through_defs(r)),
                ("defs-pointer-does-not-resolve", lambda r=reference: walks_to(document, r)),
                ("defs-pointer-not-through-a-properties-segment", lambda r=reference: properties_before_defs(r)),
            )
        )


def ref_of(schema: Any) -> Any:
    return schema.get("$ref") if isinstance(schema, dict) else None


def property_refs(document: Any) -> Iterator[tuple[Any, list[tuple[str, Check]]]]:
    for _parent, child in placed(document, "properties"):
        if isinstance(ref_of(child), str):
            yield ref_of(child), []


def primary_array(schema: Any) -> bool:
    return primary_type(schema) == "array"


def declares_array(schema: Any) -> bool:
    return declares_type(schema, "array")


def array_item_refs(document: Any, primary: bool) -> Iterator[tuple[Any, list[tuple[str, Check]]]]:
    """Each `items` reference, with its owner's array type: its primary type, or any type it lists."""
    owner_is_array = primary_array if primary else declares_array
    for parent, child in placed(document, "items"):
        if isinstance(ref_of(child), str):
            yield ref_of(child), [("items-owner-not-type-array", functools.partial(owner_is_array, parent))]


def map_value_refs(document: Any) -> Iterator[tuple[Any, list[tuple[str, Check]]]]:
    for parent, child in placed(document, "additionalProperties"):
        if isinstance(ref_of(child), str):
            yield ref_of(child), [("map-owner-not-type-object", lambda p=parent: declares_type(p, "object"))]


def allof_refs(document: Any) -> Iterator[tuple[Any, list[tuple[str, Check]]]]:
    for _parent, child in placed(document, "allOf"):
        if isinstance(ref_of(child), str):
            yield ref_of(child), []


def request_refs(document: Any) -> Iterator[tuple[Any, list[tuple[str, Check]]]]:
    for operation in operations(document):
        for schema in media_schemas(document, operation.node.get("requestBody")):
            if isinstance(ref_of(schema), str):
                yield ref_of(schema), []


def response_refs(document: Any) -> Iterator[tuple[Any, list[tuple[str, Check]]]]:
    seen: set[int] = set()
    holders: list[Any] = []
    for operation in operations(document):
        responses = operation.node.get("responses")
        holders += list(responses.values()) if isinstance(responses, dict) else []
    components = document.get("components") if isinstance(document, dict) else None
    named = components.get("responses") if isinstance(components, dict) else None
    holders += list(named.values()) if isinstance(named, dict) else []
    for holder in holders:
        for schema in media_schemas(document, holder):
            if isinstance(ref_of(schema), str) and id(schema) not in seen:
                seen.add(id(schema))
                yield ref_of(schema), []


def null_member(document: Any, member: Any) -> bool:
    member = deref(document, member)
    if not isinstance(member, dict):
        return False
    kind = member.get("type")
    return kind == "null" or kind == ["null"] or member.get("enum") == [None]


def non_null_members(document: Any, members: Any) -> list[Any]:
    return [member for member in members if not null_member(document, member)] if isinstance(members, list) else []


def string_enum(schema: Any) -> list[str]:
    values = schema.get("enum") if isinstance(schema, dict) else None
    if isinstance(values, list) and values and all(isinstance(value, str) for value in values):
        return values
    return []


def single_tag(document: Any, schema: Any) -> str | None:
    """A property's one-valued string tag (`enum: [x]` or `const: x`), read through its reference."""
    schema = deref(document, schema)
    if not isinstance(schema, dict):
        return None
    if isinstance(schema.get("const"), str):
        return schema["const"]
    values = string_enum(schema)
    return values[0] if len(values) == 1 else None


def object_properties(document: Any, schema: Any, depth: int = 0) -> dict[Any, Any]:
    """A schema's own properties with its `allOf` members' merged in, references followed."""
    schema = deref(document, schema)
    if not isinstance(schema, dict) or depth > 16:
        return {}
    merged: dict[Any, Any] = {}
    for member in schema.get("allOf") if isinstance(schema.get("allOf"), list) else []:
        merged.update(object_properties(document, member, depth + 1))
    own = schema.get("properties")
    merged.update(own if isinstance(own, dict) else {})
    return merged


def tagged_members(document: Any, members: list[Any]) -> set[str]:
    """The property names every member tags with a one-valued string enum or const."""
    shared: set[str] | None = None
    for member in members:
        props = object_properties(document, member)
        names = {str(name) for name, value in props.items() if single_tag(document, value) is not None}
        shared = names if shared is None else shared & names
    return shared or set()


def required_names(document: Any, schema: Any, depth: int = 0) -> set[str]:
    """A schema's required names with its `allOf` members' merged in; an `allOf` cycle stops at `depth` 16."""
    schema = deref(document, schema)
    names: set[str] = set()
    if not isinstance(schema, dict) or depth > 16:
        return names
    for member in schema.get("allOf") if isinstance(schema.get("allOf"), list) else []:
        names |= required_names(document, member, depth + 1)
    required = schema.get("required")
    return names | ({str(name) for name in required} if isinstance(required, list) else set())


def unrequired_tag_sites(document: Any, keyword: str) -> Iterator[Site]:
    for schema in all_schemas(document):
        members = schema.get(keyword)
        if not isinstance(members, list):
            continue
        referenced = [member for member in members if isinstance(ref_of(member), str)]
        enum_tag = [
            member
            for member in referenced
            if any(string_enum(deref(document, value)) for value in object_properties(document, member).values())
        ]
        conditions: list[tuple[str, Check]] = [
            ("no-member-is-a-reference", lambda r=referenced: bool(r)),
            ("no-referenced-member-declares-a-string-enum-property", lambda e=enum_tag: bool(e)),
        ]
        if keyword == "oneOf":
            # Fern applies an explicit discriminator to `oneOf` alone; an inferred tag is read only without one.
            conditions.append(("union-declares-a-discriminator", lambda s=schema: "discriminator" not in s))
        conditions += [
            ("members-share-no-one-valued-tag-property", lambda m=members: bool(tagged_members(document, m))),
            (
                "every-member-requires-its-tag",
                lambda m=members: any(
                    tag not in required_names(document, member) for member in m for tag in tagged_members(document, m)
                ),
            ),
        ]
        yield Site(tuple(conditions))


def anyof_beside_properties_sites(document: Any) -> Iterator[Site]:
    for schema in all_schemas(document):
        members = schema.get("anyOf")
        if not isinstance(members, list):
            continue
        props = schema.get("properties")

        def shared(m: list[Any] = members, p: Any = props) -> bool:
            tags = tagged_members(document, m)
            return isinstance(p, dict) and any(name not in tags for name in p)

        yield Site(
            (
                ("no-properties-beside-anyof", lambda p=props: isinstance(p, dict) and bool(p)),
                ("a-member-is-a-reference", lambda m=members: all(not isinstance(ref_of(x), str) for x in m)),
                ("members-share-no-one-valued-tag-property", lambda m=members: bool(tagged_members(document, m))),
                ("no-property-beside-the-tag", shared),
            )
        )


def nullable_allof_sites(document: Any) -> Iterator[Site]:
    for schema in all_schemas(document):
        members = schema.get("allOf")
        if not isinstance(members, list):
            continue
        parents = [
            deref(document, member)
            for member in members
            if isinstance(ref_of(member), str)
            and isinstance(deref(document, member), dict)
            and deref(document, member).get("nullable") is True
        ]
        own: set[str] = set()
        if isinstance(schema.get("properties"), dict):
            own |= {str(name) for name in schema["properties"]}
        for member in members:
            if isinstance(member, dict) and "$ref" not in member and isinstance(member.get("properties"), dict):
                own |= {str(name) for name in member["properties"]}
        inherited = {str(name) for parent in parents for name in object_properties(document, parent)}
        yield Site(
            (
                ("not-type-object", lambda s=schema: primary_type(s) == "object"),
                ("no-allof-reference-to-a-nullable-parent", lambda p=parents: bool(p)),
                ("no-own-property-declared", lambda o=own: bool(o)),
                ("no-own-property-shares-a-nullable-parent-property-name", lambda o=own, i=inherited: bool(o & i)),
            )
        )


def property_anyof_composed_sites(document: Any) -> Iterator[Site]:
    for _parent, child in placed(document, "properties"):
        members = child.get("anyOf") if isinstance(child, dict) else None
        if not isinstance(members, list):
            continue
        yield Site(
            (
                (
                    "anyof-has-fewer-than-two-non-null-members",
                    lambda m=members: len(non_null_members(document, m)) >= 2,
                ),
                (
                    "no-anyof-member-is-a-oneof",
                    lambda m=members: any(isinstance(x, dict) and isinstance(x.get("oneOf"), list) for x in m),
                ),
            )
        )


def located(document: Any, location: str) -> Iterator[tuple[Operation, dict[Any, Any]]]:
    for operation in operations(document):
        for parameter in parameters(document, operation):
            if parameter.get("in") == location:
                yield operation, parameter


def header_array_sites(document: Any) -> Iterator[Site]:
    for _operation, parameter in located(document, "header"):
        schema = deref(document, parameter.get("schema"))
        items = schema.get("items") if isinstance(schema, dict) else None
        yield Site(
            (
                ("schema-not-type-array", lambda s=schema: declares_type(s, "array")),
                ("items-are-a-reference", lambda i=items: isinstance(i, dict) and "$ref" not in i),
                ("items-not-type-string", lambda i=items: primary_type(i) == "string"),
            )
        )


# The header parameters `src/ir.rs::global_headers` never promotes, compared in any
# case: `is_transport_managed_parameter`'s names and `is_promotion_reserved_header`'s.
# `tools/witness-search/tests/population_screen_test.py` holds this set to those
# functions' own lists.
TRANSPORT_MANAGED_HEADERS = frozenset(
    {"user-agent", "content-type", "origin", "cookie", "content-length", "content-disposition", "x-forwarded-for"}
)
PROMOTION_RESERVED_HEADERS = frozenset({"authorization"})


def api_key_headers(document: Any) -> set[str]:
    """The header names a declared `apiKey` scheme owns, spelled exactly (`is_auth_managed_header`)."""
    components = document.get("components") if isinstance(document, dict) else None
    schemes = components.get("securitySchemes") if isinstance(components, dict) else None
    names = set()
    for scheme in schemes.values() if isinstance(schemes, dict) else []:
        scheme = deref(document, scheme)
        if isinstance(scheme, dict) and scheme.get("type") == "apiKey" and scheme.get("in") == "header":
            names.add(str(scheme.get("name", "")))
    return names


def client_managed(name: Any, keys: set[str]) -> bool:
    """Whether the client owns a header `global_headers` would otherwise promote."""
    return str(name).lower() in TRANSPORT_MANAGED_HEADERS | PROMOTION_RESERVED_HEADERS or str(name) in keys


def header_default_sites(document: Any) -> Iterator[Site]:
    every = list(operations(document))
    keys = api_key_headers(document)
    for _operation, parameter in located(document, "header"):
        schema = deref(document, parameter.get("schema"))
        name = parameter.get("name")

        def on_every(n: Any = name) -> bool:
            return all(
                any(p.get("in") == "header" and p.get("name") == n for p in parameters(document, o)) for o in every
            )

        yield Site(
            (
                ("schema-declares-no-default", lambda s=schema: isinstance(s, dict) and "default" in s),
                ("default-not-a-string", lambda s=schema: isinstance(s.get("default"), str)),
                (
                    "required-header-not-type-string",
                    lambda p=parameter, s=schema: p.get("required") is not True or primary_type(s) == "string",
                ),
                ("header-is-client-managed", lambda n=name: not client_managed(n, keys)),
                ("header-not-on-every-operation", on_every),
            )
        )


def required_query_array_enum_sites(document: Any) -> Iterator[Site]:
    for _operation, parameter in located(document, "query"):
        schema = deref(document, parameter.get("schema"))
        items = schema.get("items") if isinstance(schema, dict) else None
        yield Site(
            (
                ("parameter-not-required", lambda p=parameter: p.get("required") is True),
                ("schema-not-primary-type-array", lambda s=schema: primary_type(s) == "array"),
                ("items-not-a-reference", lambda i=items: isinstance(ref_of(i), str)),
                ("items-target-declares-no-string-enum", lambda i=items: bool(string_enum(deref(document, i)))),
            )
        )


def tag_only_sites(document: Any) -> Iterator[Site]:
    for operation in operations(document):
        identifier, tags = operation.node.get("operationId"), operation.node.get("tags")
        if not isinstance(identifier, str) or not isinstance(tags, list) or not tags:
            continue
        yield Site(
            (
                (
                    "operation-id-not-its-first-tag-and-underscores",
                    lambda i=identifier, t=tags[0]: (
                        isinstance(t, str) and i.endswith("_") and i.rstrip("_").lower() == t.lower()
                    ),
                ),
            )
        )


def body_path_collision_sites(document: Any) -> Iterator[Site]:
    for operation in operations(document):
        if "requestBody" not in operation.node:
            continue
        path_names = {str(p.get("name")) for p in parameters(document, operation) if p.get("in") == "path"}
        body = [
            object_properties(document, schema) for schema in media_schemas(document, operation.node["requestBody"])
        ]
        yield Site(
            (
                ("no-path-parameter", lambda n=path_names: bool(n)),
                ("body-writes-no-object-properties", lambda b=body: any(b)),
                (
                    "no-body-property-named-as-a-path-parameter",
                    lambda b=body, n=path_names: any(str(name) in n for props in b for name in props),
                ),
            )
        )


def map_beside_oneof_sites(document: Any) -> Iterator[Site]:
    for schema in all_schemas(document):
        if not isinstance(schema.get("oneOf"), list):
            continue
        yield Site(
            (
                ("no-additional-properties-beside-oneof", lambda s=schema: "additionalProperties" in s),
                (
                    "additional-properties-neither-a-schema-nor-true",
                    lambda s=schema: isinstance(s["additionalProperties"], dict) or s["additionalProperties"] is True,
                ),
                ("properties-declared-beside-the-map", lambda s=schema: not s.get("properties")),
            )
        )


def success_union_sites(document: Any, keyword: str) -> Iterator[Site]:
    walker = census().Census(document, {})
    for operation in operations(document):
        _written, success = walker.success_entry(operation.node)
        content = success.get("content") if isinstance(success, dict) else None
        for media in content.values() if isinstance(content, dict) else []:
            schema = deref(document, media.get("schema") if isinstance(media, dict) else None)
            if not isinstance(schema, dict) or not isinstance(schema.get(keyword), list):
                continue
            yield Site(
                (
                    (
                        f"{keyword.lower()}-success-schema-not-nullable",
                        lambda s=schema: (
                            s.get("nullable") is True
                            or declares_type(s, "null")
                            or any(null_member(document, member) for member in s[keyword])
                        ),
                    ),
                )
            )


def query_inline_object_sites(document: Any) -> Iterator[Site]:
    for _operation, parameter in located(document, "query"):
        schema = parameter.get("schema")
        if not isinstance(schema, dict):
            continue
        yield Site(
            (
                ("schema-is-a-reference", lambda s=schema: "$ref" not in s),
                ("schema-not-primary-type-object", lambda s=schema: primary_type(s) == "object"),
                ("schema-declares-no-properties", lambda s=schema: bool(s.get("properties"))),
                ("parameter-not-required", lambda p=parameter: p.get("required") is True),
            )
        )


SiteFinder = Callable[[Any], Iterable[Site]]

# Each key's sites, read as its census selector and its earlier search's `needs`
# (or, for the five arm keys, its audit row) state the trigger.
SITES: dict[str, SiteFinder] = {
    "combo-allof-unresolved-nested-pointer": lambda d: unresolved_pointer_sites(d, allof_refs(d)),
    "combo-array-unresolved-nested-pointer": lambda d: unresolved_pointer_sites(d, array_item_refs(d, False)),
    "combo-map-unresolved-nested-pointer": lambda d: unresolved_pointer_sites(d, map_value_refs(d)),
    "combo-property-unresolved-nested-pointer": lambda d: unresolved_pointer_sites(d, property_refs(d)),
    "combo-request-unresolved-nested-pointer": lambda d: unresolved_pointer_sites(d, request_refs(d)),
    "combo-response-unresolved-nested-pointer": lambda d: unresolved_pointer_sites(d, response_refs(d)),
    "combo-array-defs-pointer": lambda d: defs_pointer_sites(d, array_item_refs(d, True)),
    "combo-property-defs-pointer": lambda d: defs_pointer_sites(d, property_refs(d)),
    "combo-anyof-beside-properties": anyof_beside_properties_sites,
    "combo-nullable-allof-parent-own-property": nullable_allof_sites,
    "combo-property-anyof-composed-sibling": property_anyof_composed_sites,
    "combo-unrequired-tag-anyof-reference": lambda d: unrequired_tag_sites(d, "anyOf"),
    "combo-unrequired-tag-oneof-reference": lambda d: unrequired_tag_sites(d, "oneOf"),
    "combo-header-array-accepted-placements": header_array_sites,
    "combo-header-string-default": header_default_sites,
    "combo-required-query-array-enum-items": required_query_array_enum_sites,
    "combo-tag-only-operation-id": tag_only_sites,
    "combo-body-property-named-as-path-param": body_path_collision_sites,
    "combo-map-beside-oneof": map_beside_oneof_sites,
    "combo-success-anyof-nullable": lambda d: success_union_sites(d, "anyOf"),
    "combo-success-oneof-nullable": lambda d: success_union_sites(d, "oneOf"),
    "combo-query-param-inline-object": query_inline_object_sites,
}
KEYS = tuple(SITES)

_POINTER = ("pointer-not-a-nested-component-pointer", "nested-pointer-resolves")
_DEFS = (
    "pointer-not-through-a-defs-member",
    "defs-pointer-does-not-resolve",
    "defs-pointer-not-through-a-properties-segment",
)
_TAG = (
    "no-member-is-a-reference",
    "no-referenced-member-declares-a-string-enum-property",
    "members-share-no-one-valued-tag-property",
    "every-member-requires-its-tag",
)
# Every condition a key's `partial:` verdict may name, in the order its sites judge
# them: the reader admits no other, and the suite holds each site to this order.
CONDITIONS: dict[str, tuple[str, ...]] = {
    "combo-allof-unresolved-nested-pointer": _POINTER,
    "combo-array-unresolved-nested-pointer": ("items-owner-not-type-array", *_POINTER),
    "combo-map-unresolved-nested-pointer": ("map-owner-not-type-object", *_POINTER),
    "combo-property-unresolved-nested-pointer": _POINTER,
    "combo-request-unresolved-nested-pointer": _POINTER,
    "combo-response-unresolved-nested-pointer": _POINTER,
    "combo-array-defs-pointer": ("items-owner-not-type-array", *_DEFS),
    "combo-property-defs-pointer": _DEFS,
    "combo-anyof-beside-properties": (
        "no-properties-beside-anyof",
        "a-member-is-a-reference",
        "members-share-no-one-valued-tag-property",
        "no-property-beside-the-tag",
    ),
    "combo-nullable-allof-parent-own-property": (
        "not-type-object",
        "no-allof-reference-to-a-nullable-parent",
        "no-own-property-declared",
        "no-own-property-shares-a-nullable-parent-property-name",
    ),
    "combo-property-anyof-composed-sibling": (
        "anyof-has-fewer-than-two-non-null-members",
        "no-anyof-member-is-a-oneof",
    ),
    "combo-unrequired-tag-anyof-reference": _TAG,
    "combo-unrequired-tag-oneof-reference": (*_TAG[:2], "union-declares-a-discriminator", *_TAG[2:]),
    "combo-header-array-accepted-placements": (
        "schema-not-type-array",
        "items-are-a-reference",
        "items-not-type-string",
    ),
    "combo-header-string-default": (
        "schema-declares-no-default",
        "default-not-a-string",
        "required-header-not-type-string",
        "header-is-client-managed",
        "header-not-on-every-operation",
    ),
    "combo-required-query-array-enum-items": (
        "parameter-not-required",
        "schema-not-primary-type-array",
        "items-not-a-reference",
        "items-target-declares-no-string-enum",
    ),
    "combo-tag-only-operation-id": ("operation-id-not-its-first-tag-and-underscores",),
    "combo-body-property-named-as-path-param": (
        "no-path-parameter",
        "body-writes-no-object-properties",
        "no-body-property-named-as-a-path-parameter",
    ),
    "combo-map-beside-oneof": (
        "no-additional-properties-beside-oneof",
        "additional-properties-neither-a-schema-nor-true",
        "properties-declared-beside-the-map",
    ),
    "combo-success-anyof-nullable": ("anyof-success-schema-not-nullable",),
    "combo-success-oneof-nullable": ("oneof-success-schema-not-nullable",),
    "combo-query-param-inline-object": (
        "schema-is-a-reference",
        "schema-not-primary-type-object",
        "schema-declares-no-properties",
        "parameter-not-required",
    ),
}


def trigger(key: str, document: Any) -> str:
    """The key's trigger verdict over one parsed document: `exact`, `partial:<condition>` or `absent`."""
    if key not in SITES:
        raise ScreenError(f"{key!r} is no combination key this screen knows; pass one of {', '.join(KEYS)}")
    return verdict(SITES[key](document))


@functools.cache
def _compiled(selectors: tuple[str, ...]) -> dict[str, Any]:
    module = census()
    return {selector: module.compile_conjunction(selector) for selector in selectors if selector in module.CONJUNCTIONS}


@dataclass(frozen=True)
class Selectors:
    """Each key's census selector, as `docs/openapi-surface/witness-search-keys.tsv` derives it."""

    by_key: dict[str, str]

    @classmethod
    def read(cls, path: Path = REPO / "docs" / "openapi-surface" / "witness-search-keys.tsv") -> Selectors:
        rows: dict[str, str] = {}
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            if not {"key", "selector"} <= set(reader.fieldnames or ()):
                raise ScreenError(f"{path} names no key and selector columns; regenerate it with its own script")
            for number, row in enumerate(reader, 2):
                key, selector = row.get("key"), row.get("selector")
                if not isinstance(key, str) or not key or not isinstance(selector, str) or not selector:
                    raise ScreenError(f"{path}:{number} is no key with its selector; regenerate it with its own script")
                if key in rows:
                    raise ScreenError(f"{path}:{number} names {key} a second time; regenerate it with its own script")
                if key in KEYS and (error := census().selector_error(selector)) is not None:
                    raise ScreenError(f"{path}:{number}: {key}'s selector is none the census reads ({error})")
                rows[key] = selector
        missing = [key for key in KEYS if key not in rows]
        if missing:
            raise ScreenError(f"{path} names no selector for {missing}; regenerate it with its own script")
        return cls({key: rows[key] for key in KEYS})

    def declarations(self, document: Any) -> dict[str, int]:
        """Each key's census declaration count over one parsed document (0 off OpenAPI 3)."""
        module = census()
        version = document.get("openapi") if isinstance(document, dict) else None
        if not isinstance(version, str) or not version.startswith("3."):
            return dict.fromkeys(KEYS, 0)
        compiled = _compiled(tuple(sorted(set(self.by_key.values()))))
        counts = module.census_document(document, conjunctions=compiled)
        return {key: counts.get(selector, 0) for key, selector in self.by_key.items()}


class ScreenRow(NamedTuple):
    """One row of the table: a candidate document, screened for one key."""

    key: str
    population: Population
    document: str
    source: str
    sha256: str
    licence: str
    trigger: str
    status: str


COLUMNS = ScreenRow._fields


def _reason(text: str) -> str | None:
    """A cell's reason, or None when it says nothing (empty, a placeholder or padded)."""
    return None if PLACEHOLDER.match(text.strip()) or text != text.strip() else text


class LicenceKind(StrEnum):
    ADMISSIBLE = "admissible"
    INADMISSIBLE = "inadmissible"
    UNREAD = "unread"


class TriggerKind(StrEnum):
    EXACT = "exact"
    PARTIAL = "partial"
    ABSENT = "absent"
    UNREAD = "unread"


class StatusKind(StrEnum):
    PENDING = PENDING
    REJECTED_TRIGGER = "rejected-trigger"
    REJECTED_LICENCE = "rejected-licence"
    UNFETCHABLE = "unfetchable"


# The kinds a cell names with a reason after `:`; every other kind is the cell alone.
REASONED = frozenset(
    {
        LicenceKind.ADMISSIBLE,
        LicenceKind.INADMISSIBLE,
        LicenceKind.UNREAD,
        TriggerKind.PARTIAL,
        TriggerKind.UNREAD,
        StatusKind.UNFETCHABLE,
    }
)


KindT = TypeVar("KindT", bound=StrEnum)


@dataclass(frozen=True)
class Verdict(Generic[KindT]):
    """One `licence`, `trigger` or `status` cell, parsed: its kind and the reason it gives."""

    kind: KindT
    reason: str = ""

    def __str__(self) -> str:
        return f"{self.kind}:{self.reason}" if self.kind in REASONED else str(self.kind)

    @staticmethod
    def parse(cell: str, kinds: type[KindT]) -> Verdict[KindT] | None:
        """The verdict a cell names among `kinds`, or None when it names none of them (or no reason it owes)."""
        head, colon, rest = cell.partition(":")
        if head not in {kind.value for kind in kinds}:
            return None
        kind = kinds(head)
        if kind in REASONED:
            reason = _reason(rest) if colon else None
            return None if reason is None else Verdict(kind, reason)
        return None if colon else Verdict(kind)


def status_verdict(licence: Verdict[LicenceKind], trigger: Verdict[TriggerKind]) -> Verdict[StatusKind]:
    """The status the rule gives a licence and a trigger, or raise `ScreenError` for a pair no row may carry."""
    match trigger.kind, licence.kind:
        case TriggerKind.UNREAD, LicenceKind.UNREAD:
            return Verdict(StatusKind.UNFETCHABLE, trigger.reason)
        case TriggerKind.UNREAD, _:
            raise ScreenError("a trigger left unread beside a licence that was read: unread bytes leave both unread")
        case TriggerKind.PARTIAL | TriggerKind.ABSENT, _:
            return Verdict(StatusKind.REJECTED_TRIGGER)
        case TriggerKind.EXACT, LicenceKind.ADMISSIBLE:
            return Verdict(StatusKind.PENDING)
        case TriggerKind.EXACT, LicenceKind.INADMISSIBLE:
            return Verdict(StatusKind.REJECTED_LICENCE)
        case _:
            raise ScreenError(
                f"an exact trigger whose licence {str(licence)!r} was never decided: read its licence evidence"
            )


def status_of(licence: str, trigger_cell: str) -> str:
    """The status cell the rule gives a row's licence and trigger cells, or raise `ScreenError` for a pair no row may carry."""
    parsed_trigger = Verdict.parse(trigger_cell, TriggerKind)
    if parsed_trigger is None:
        raise ScreenError(f"trigger {trigger_cell!r} is none of exact, partial:<condition>, absent, unread:<reason>")
    parsed_licence = Verdict.parse(licence, LicenceKind)
    if parsed_licence is None:
        raise ScreenError(f"licence {licence!r} is none of admissible:<grant>, inadmissible:<reason>, unread:<reason>")
    return str(status_verdict(parsed_licence, parsed_trigger))


def source_failure(population: str, source: str) -> str | None:
    if population == "registered":
        return None if source == "-" else "a registered document's source is `-` (its bytes are in the tree)"
    # raw.githubusercontent.com/<owner>/<repo>/<commit>/<path>: the revision segment is a full commit SHA.
    parts = urllib.parse.urlsplit(source)
    segments = parts.path.split("/")[1:]
    if (
        parts.scheme != "https"
        or parts.netloc != "raw.githubusercontent.com"
        or parts.query
        or parts.fragment
        or len(segments) < 4
        or not COMMIT.fullmatch(segments[2])
        or not witness_screen().repository_name("/".join(segments[:2]))
        or not witness_screen().repository_path(urllib.parse.unquote("/".join(segments[3:])))
    ):
        return f"source {source!r} is no raw.githubusercontent.com URL pinned at a full commit SHA"
    return None


def document_failure(population: str, document: str) -> str | None:
    if PLACEHOLDER.match(document) or "\t" in document or document != document.strip():
        return "document is empty, a placeholder or padded"
    if population == "registered" and not CORPUS_NAME.fullmatch(document):
        return f"registered document {document!r} is no corpus row name"
    if population in ("github", "sourcegraph") and len([p for p in document.split("/") if p]) < 3:
        return f"{population} document {document!r} is no `owner/repo/path`"
    return None


def row_failures(row: ScreenRow) -> list[str]:
    """Why one row is not one this module writes; empty when it is whole."""
    wrong = []
    if row.key not in KEYS:
        wrong.append(f"key {row.key!r} is none of the {len(KEYS)} combination keys")
    if row.population not in POPULATIONS:
        wrong.append(f"population {row.population!r} is none of {', '.join(POPULATIONS)}")
    for failure in (
        document_failure(row.population, row.document),
        source_failure(row.population, row.source) if row.population in POPULATIONS else None,
    ):
        if failure:
            wrong.append(failure)
    licence = Verdict.parse(row.licence, LicenceKind)
    trigger = Verdict.parse(row.trigger, TriggerKind)
    status = Verdict.parse(row.status, StatusKind)
    unfetchable = status is not None and status.kind is StatusKind.UNFETCHABLE
    if not (SHA.fullmatch(row.sha256) or (unfetchable and row.sha256 == "-")):
        wrong.append(f"sha256 {row.sha256!r} is no SHA-256 (`-` only on an unfetchable row that never had one)")
    if licence is None:
        wrong.append(f"licence {row.licence!r} is none of admissible:<grant>, inadmissible:<reason>, unread:<reason>")
    if trigger is None:
        wrong.append(f"trigger {row.trigger!r} is none of exact, partial:<condition>, absent, unread:<reason>")
    elif trigger.kind is TriggerKind.PARTIAL and trigger.reason not in CONDITIONS.get(row.key, ()):
        wrong.append(f"trigger {row.trigger!r} names no condition of {row.key}'s screen")
    if licence is not None and trigger is not None:
        try:
            expected = status_verdict(licence, trigger)
        except ScreenError as error:
            wrong.append(str(error))
        else:
            if row.status != str(expected):
                wrong.append(
                    f"status {row.status!r} disagrees with its licence and trigger, which give {str(expected)!r}"
                )
            if unfetchable and licence.reason != trigger.reason:
                wrong.append("an unfetchable row's licence and trigger name the same reason the bytes were not had")
    return wrong


def read_screen(path: Path = TABLE) -> list[ScreenRow]:
    """Every row of a screen table, refusing a malformed table, a malformed or duplicate row."""
    try:
        text = path.read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise ScreenError(f"{path}: cannot be read as UTF-8 ({error}); regenerate it with `screen`") from error
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    if not lines or tuple(lines[0].split("\t")) != COLUMNS:
        raise ScreenError(f"{path}: its header is not {'/'.join(COLUMNS)}; regenerate it with `screen`")
    rows: list[ScreenRow] = []
    seen: dict[tuple[str, str, str], int] = {}
    for number, line in enumerate(lines[1:], 2):
        cells = line.split("\t")
        if len(cells) != len(COLUMNS) or "\r" in line:
            raise ScreenError(f"{path}:{number}: {len(cells)} cells, not the {len(COLUMNS)} columns")
        if cells[1] not in POPULATIONS:
            raise ScreenError(f"{path}:{number}: population {cells[1]!r} is none of {', '.join(POPULATIONS)}")
        row = ScreenRow(cells[0], Population(cells[1]), *cells[2:])
        wrong = row_failures(row)
        if wrong:
            raise ScreenError(f"{path}:{number}: " + "; ".join(wrong))
        identity = (row.key, row.population, row.document)
        if identity in seen:
            raise ScreenError(f"{path}:{number}: duplicates line {seen[identity]}'s ({', '.join(identity)})")
        seen[identity] = number
        rows.append(row)
    return rows


def pending_counts(rows: Iterable[ScreenRow]) -> Counter[str]:
    """Each key's `certified-screen-pending` candidates: the named census a still-open row cites."""
    return Counter(row.key for row in rows if row.status == PENDING)


def render(rows: Iterable[ScreenRow]) -> str:
    ordered = sorted(rows, key=lambda row: (row.key, POPULATIONS.index(row.population), row.document))
    return "\t".join(COLUMNS) + "\n" + "".join("\t".join(row) + "\n" for row in ordered)


def cache_root() -> Path:
    """`${XDG_CACHE_HOME:-$HOME/.cache}/crozier/witness-populations`: exact bytes named by their SHA-256."""
    base = os.environ.get("XDG_CACHE_HOME") or ""
    root = Path(base) if os.path.isabs(base) else Path.home() / ".cache"
    return root / "crozier" / "witness-populations"


def store(data: bytes, root: Path | None = None) -> Path:
    """Keep `data` under its own digest, atomically; the path it is kept at."""
    root = root or cache_root()
    digest = hashlib.sha256(data).hexdigest()
    path = root / digest
    if path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest:
        return path
    root.mkdir(parents=True, exist_ok=True)
    partial = root / f".{digest}.{os.getpid()}.part"
    partial.write_bytes(data)
    partial.replace(path)
    return path


def cached(sha256: str, root: Path | None = None) -> bytes | None:
    """The kept bytes `sha256` names, or None when they are missing or no longer carry that digest."""
    path = (root or cache_root()) / sha256
    try:
        data = path.read_bytes()
    except OSError:
        return None
    return data if hashlib.sha256(data).hexdigest() == sha256 else None


class EvidenceKind(StrEnum):
    """Where a candidate's licence is read when its document declares no `info.license`."""

    CORPUS = "corpus"  # the corpus row's recorded grant
    CORPUS_AGGREGATION = "corpus-aggregation"  # the same, for a row copied from an aggregation
    REPOSITORY = "repository"  # the repository licence file at the pinned commit
    AGGREGATION = "aggregation"  # an aggregation's copy: no publisher grant
    NO_PUBLISHER_GRANT = "no-publisher-grant"  # an APIs.guru archive copy
    NONE = "-"


@dataclass(frozen=True)
class Evidence:
    """A manifest row's `evidence` cell, parsed."""

    kind: EvidenceKind
    grant: str = ""
    repository: str = ""
    commit: str = ""

    @classmethod
    def parse(cls, text: str) -> Evidence:
        kind, colon, rest = text.partition(":")
        match kind:
            case "corpus" | "corpus-aggregation" if rest:
                return cls(EvidenceKind(kind), grant=rest)
            case "repository" | "aggregation":
                found = re.fullmatch(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([0-9a-f]{40})", rest)
                if found and witness_screen().repository_name(found.group(1)):
                    return cls(EvidenceKind(kind), repository=found.group(1), commit=found.group(2))
            case "no-publisher-grant" | "-" if not colon:
                return cls(EvidenceKind(kind))
        raise ScreenError(
            f"evidence {text!r} is none of corpus:<grant>, corpus-aggregation:<grant>, "
            "repository:<owner>/<repo>@<commit>, aggregation:<owner>/<repo>@<commit>, no-publisher-grant or -"
        )


class Entry(NamedTuple):
    """One manifest row: a candidate document, its licence evidence and the keys it owes a row for."""

    population: Population
    document: str
    source: str
    sha256: str
    # `corpus:<recorded grant>` (`corpus-aggregation:<recorded grant>` for a row sourced from an aggregation),
    # `repository:<owner>/<repo>@<commit>`, `aggregation:<owner>/<repo>@<commit>`
    # (an aggregation's copy), `no-publisher-grant` (an APIs.guru archive copy) or `-`.
    evidence: str
    # The keys an earlier named census already lists it for, `;`-joined, or `-`.
    keys: str
    # Why its bytes could not be had, or `-`.
    unfetchable: str

    def forced(self) -> list[str]:
        return [] if self.keys == "-" else self.keys.split(";")

    def licence_evidence(self) -> Evidence:
        return Evidence.parse(self.evidence)


MANIFEST_COLUMNS = Entry._fields


def read_manifest(path: Path) -> list[Entry]:
    seen: dict[tuple[str, str], int] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        header = next(reader, None)
        if tuple(header or ()) != MANIFEST_COLUMNS:
            raise ScreenError(f"{path}: its header is not {'/'.join(MANIFEST_COLUMNS)}")
        entries = []
        for number, cells in enumerate(reader, 2):
            if len(cells) != len(MANIFEST_COLUMNS) or any(not cell for cell in cells):
                raise ScreenError(f"{path}:{number}: {len(cells)} cells, every one filled, not {len(MANIFEST_COLUMNS)}")
            if cells[0] not in POPULATIONS:
                raise ScreenError(f"{path}:{number}: population {cells[0]!r} is none of {', '.join(POPULATIONS)}")
            entry = Entry(Population(cells[0]), *cells[1:])
            wrong = entry_failures(entry)
            if (entry.population, entry.document) in seen:
                wrong.append(f"duplicates line {seen[(entry.population, entry.document)]}'s candidate")
            if wrong:
                raise ScreenError(f"{path}:{number}: " + "; ".join(wrong))
            seen[(entry.population, entry.document)] = number
            entries.append(entry)
    return entries


def entry_failures(entry: Entry) -> list[str]:
    """Why one manifest row is not a candidate the screen can read; empty when it is."""
    if entry.population not in POPULATIONS:
        return [f"population {entry.population!r} is none of {', '.join(POPULATIONS)}"]
    wrong = [
        failure
        for failure in (
            document_failure(entry.population, entry.document),
            source_failure(entry.population, entry.source),
        )
        if failure
    ]
    unfetchable = entry.unfetchable != "-"
    if not (SHA.fullmatch(entry.sha256) or (unfetchable and entry.sha256 == "-")):
        wrong.append(f"sha256 {entry.sha256!r} is no SHA-256 (`-` only beside an unfetchable reason)")
    try:
        entry.licence_evidence()
    except ScreenError as error:
        wrong.append(str(error))
    unknown = [key for key in entry.forced() if key not in KEYS]
    if unknown:
        wrong.append(f"keys {unknown} are no combination keys")
    if unfetchable and PLACEHOLDER.match(entry.unfetchable.strip()):
        wrong.append("an unfetchable reason that says nothing")
    return wrong


def write_manifest(path: Path, entries: Iterable[Entry]) -> None:
    ordered = sorted(set(entries), key=lambda e: (POPULATIONS.index(e.population), e.document, e.sha256))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\t".join(MANIFEST_COLUMNS) + "\n" + "".join("\t".join(entry) + "\n" for entry in ordered),
        encoding="utf-8",
        newline="\n",
    )


def registered_files(root: Path = REPO) -> dict[str, Path]:
    """Each registered corpus row's committed source document, as `corpus-sources.tsv` records it."""
    files: dict[str, list[Path]] = {}
    with (root / "tests" / "fixtures" / "corpus-sources.tsv").open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("#") or not line.strip():
                continue
            name, relative, *_rest = line.rstrip("\n").split("\t")
            if not witness_screen().repository_path(relative) or not (root / relative).resolve().is_relative_to(
                root.resolve()
            ):
                raise ScreenError(
                    f"{root / 'tests/fixtures/corpus-sources.tsv'}: {name}'s source {relative!r} is no path inside the "
                    "repository; restore the manifest from git"
                )
            files.setdefault(name, []).append(root / relative)
    chosen = {}
    for name, paths in files.items():
        # The row's own document: the one directly in its directory, named as the corpus publishes it.
        top = [path for path in paths if path.parent.name == name and path.stem == "openapi"]
        chosen[name] = (top or paths)[0]
    return chosen


class CorpusRow(NamedTuple):
    number: str
    name: str
    source: str
    grant: str


def corpus_rows(root: Path = REPO) -> dict[str, CorpusRow]:
    """Each committed corpus row of `CORPUS.md`: its number, name, source URL and recorded licence."""
    rows = {}
    for line in (root / "tests" / "fixtures" / "CORPUS.md").read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) >= 9 and cells[1].isdigit() and cells[7] in ("committed", "link-ok"):
            name = cells[2].strip("` ")
            rows[name] = CorpusRow(cells[1], name, cells[4], cells[6])
    return rows


def corpus_grants(root: Path = REPO) -> dict[str, str]:
    """Each committed corpus row's recorded licence (the `license` cell of `CORPUS.md`)."""
    return {name: row.grant for name, row in corpus_rows(root).items()}


# The repositories that redistribute other publishers' descriptions: their own
# licence is an aggregation's grant, never a publisher's.
AGGREGATIONS = ("APIs-guru/openapi-directory", "jentic/jentic-public-apis")
# A corpus row's source URL naming one of them, or the APIs.guru service that serves the first.
AGGREGATION_SOURCE = re.compile(
    r"^https://(?:raw\.githubusercontent\.com/(?P<repository>"
    + "|".join(re.escape(name) for name in AGGREGATIONS)
    + r")/|api\.apis\.guru/)",
    re.I,
)


def is_aggregation(repository: str) -> bool:
    return repository.lower() in {name.lower() for name in AGGREGATIONS}


def aggregator(source: str) -> str | None:
    """The aggregation a corpus row's source URL copies its document from, or None for a publisher's."""
    match = AGGREGATION_SOURCE.match(source)
    if match is None:
        return None
    return match.group("repository") or "APIs.guru (api.apis.guru)"


def registered_bytes(document: str, root: Path = REPO) -> bytes | None:
    path = registered_files(root).get(document)
    return path.read_bytes() if path is not None and path.is_file() else None


LicenceFetch = Callable[[str, str, str], tuple[int, bytes] | None]
LICENCE_FETCH_ATTEMPTS = 4
LICENCE_FETCH_BACKOFF_S = 15.0
# A recorded grant that is only an aggregation's: the corpus spells it this way.
AGGREGATION_GRANT = re.compile(r"\baggregat", re.I)


def cell_text(text: str) -> str:
    return " ".join(str(text).split()).replace("\t", " ")[:200]


def licence_verdict(
    document: Any,
    entry: Entry,
    exact: bool,
    fetch_file: LicenceFetch,
) -> str:
    """One candidate's licence cell, read as `witness_screen.py` reads a licence.

    `fetch_file(repository, commit, name)` answers a licence file's `(status, bytes)`,
    or None when it is not cached and may not be fetched; it is asked only for a
    document that declares no `info.license`, and only where the trigger is exact.
    """
    screen = witness_screen()
    declared = screen.licence_of(document)
    families = screen.admissible_families()
    if declared is screen.MALFORMED:
        return "inadmissible:info.license is there but is no License Object"
    if declared:
        family = screen.recognise(declared)
        if family in families:
            return f"admissible:{family} (info.license '{cell_text(declared)}')"
        return f"inadmissible:info.license '{cell_text(declared)}' names no grant the corpus rule admits"
    evidence = entry.licence_evidence()
    match evidence.kind:
        case EvidenceKind.CORPUS | EvidenceKind.CORPUS_AGGREGATION:
            family = screen.recognise(evidence.grant)
            # A row copied from an aggregation stands on the aggregation's grant unless it records a publisher's.
            copied = evidence.kind is EvidenceKind.CORPUS_AGGREGATION and not re.search(
                r"\bpublisher", evidence.grant, re.I
            )
            if copied or AGGREGATION_GRANT.search(evidence.grant):
                # An aggregation's grant without a publisher grant does not pass the licence
                # screen: the ruling corpus rows 223 and 224 were withdrawn on.
                return (
                    "inadmissible:grants nothing: no info.license, and the corpus row records only an "
                    "aggregation's grant, which is no publisher grant"
                )
            if family in families:
                return f"admissible:{family} (the corpus row's recorded grant: {cell_text(evidence.grant)})"
            return (
                f"inadmissible:no info.license, and the corpus row's recorded grant {cell_text(evidence.grant)!r} "
                "is none admitted"
            )
        case EvidenceKind.NO_PUBLISHER_GRANT:
            return (
                "inadmissible:grants nothing: no info.license, and an APIs.guru archive copy carries no publisher grant"
            )
        case EvidenceKind.AGGREGATION:
            return (
                f"inadmissible:grants nothing: no info.license, and {evidence.repository} redistributes it as an "
                "aggregation, whose grant is no publisher grant"
            )
        case EvidenceKind.NONE:
            return "inadmissible:grants nothing: no info.license and no recorded repository to read a licence file at"
    if not exact:
        return "unread:no info.license, and its repository licence file is read only for an exact trigger"
    repository, commit = evidence.repository, evidence.commit
    for name in screen.LICENCE_FILES:
        answer = fetch_file(repository, commit, name)
        if answer is None:
            raise LicenceNotCached(
                f"{entry.population} {entry.document}: {name} at {repository}@{commit} is not cached; "
                "re-run `screen` with --fetch-licence to read it through the guarded raw lane"
            )
        status, data = answer
        match status:
            case 200:
                lines = [line for line in data.decode("utf-8", "replace").splitlines() if line.strip()]
                family = screen.recognise("\n".join(lines[: screen.LICENCE_HEAD_LINES]))
                if family in families:
                    return f"admissible:{family} ({name} at {commit})"
                return f"inadmissible:no info.license, and {name} at {commit} names no grant the corpus rule admits"
            case 404:
                continue
            case _:
                # Only a 404 says the file is not there: any other answer read nothing either way.
                raise ScreenError(
                    f"{name} at {repository}@{commit} answered HTTP {status}, which says nothing about whether it is "
                    "there; re-run `screen --fetch-licence` once it answers"
                )
    return "inadmissible:grants nothing: no info.license and no licence file at the pinned commit"


def parse(data: bytes, scratch: Path) -> Any:
    return witness_screen().read_document(data, scratch)


def entry_bytes(entry: Entry, root: Path, store_root: Path) -> bytes | None:
    if entry.population == "registered":
        return registered_bytes(entry.document, root)
    return cached(entry.sha256, store_root) if SHA.fullmatch(entry.sha256) else None


def screen_entry(
    entry: Entry,
    selectors: Selectors,
    *,
    root: Path,
    store_root: Path,
    scratch: Path,
    fetch_file: LicenceFetch,
    discover: bool,
) -> list[ScreenRow]:
    """Every row one candidate owes: each key an earlier census lists it for, and each its bytes declare."""
    keys = list(dict.fromkeys(entry.forced()))
    if entry.unfetchable != "-":
        reason = cell_text(entry.unfetchable)
        return [
            ScreenRow(
                key,
                entry.population,
                entry.document,
                entry.source,
                entry.sha256,
                f"unread:{reason}",
                f"unread:{reason}",
                f"unfetchable:{reason}",
            )
            for key in keys
        ]
    data = entry_bytes(entry, root, store_root)
    if data is None or hashlib.sha256(data).hexdigest() != entry.sha256:
        raise ScreenError(
            f"{entry.population} {entry.document}: no bytes carrying sha256 {entry.sha256} are in the store; "
            "acquire them first (`acquire`), or record the entry as unfetchable"
        )
    try:
        document = parse(data, scratch)
    except Exception as error:  # the census reader's own refusal, whatever its type
        reason = cell_text(f"the exact bytes do not parse ({type(error).__name__})")
        return [
            ScreenRow(
                key,
                entry.population,
                entry.document,
                entry.source,
                entry.sha256,
                f"unread:{reason}",
                f"unread:{reason}",
                f"unfetchable:{reason}",
            )
            for key in keys
        ]
    if discover:
        declared = selectors.declarations(document)
        keys += [key for key in KEYS if declared[key] > 0 and key not in keys]
    rows = []
    for key in keys:
        verdict_cell = trigger(key, document)
        licence = licence_verdict(document, entry, verdict_cell == "exact", fetch_file)
        row = ScreenRow(
            key,
            entry.population,
            entry.document,
            entry.source,
            entry.sha256,
            licence,
            verdict_cell,
            status_of(licence, verdict_cell),
        )
        wrong = row_failures(row)
        if wrong:
            raise ScreenError(f"{entry.population} {entry.document} {key}: " + "; ".join(wrong))
        if row.status == PENDING:
            store(data, store_root)
        rows.append(row)
    return rows


def raw_licence_fetcher(evidence: Path | None, live: bool) -> LicenceFetch:
    """A licence-file reader: the shared response cache first, the guarded raw lane only when `live`."""
    github = _load("population_screen_github", REPO / "tools" / "witness-search" / "witness-search-github.py")
    raw_base = github.checked_service_url(
        os.environ.get("CROZIER_RAW_GITHUB_URL", github.RAW_GITHUB_URL),
        "CROZIER_RAW_GITHUB_URL",
        "raw.githubusercontent.com",
    )
    acquirer = None

    def fetch(repository: str, commit: str, name: str) -> tuple[int, bytes] | None:
        nonlocal acquirer
        url = f"{raw_base.rstrip('/')}/{repository}/{commit}/{urllib.parse.quote(name)}"
        hit = github.cache_lookup("GET", url, {"User-Agent": "crozier-witness-search"})
        if hit is not None:
            return hit.status, hit.body()
        if not live or evidence is None:
            return None
        if acquirer is None:
            acquirer = github.Acquirer(evidence, cache=cache_root() / "acquirer", raw_github_url=raw_base)
        # A transient network failure (a name lookup, a reset) is retried with backoff
        # rather than costing the whole screen; one that persists is refused, naming it.
        for attempt in range(LICENCE_FETCH_ATTEMPTS):
            try:
                # llmlint: ignore[async_typed_clients_at_boundaries] AGENTS.md keeps the witness tooling stdlib-only and synchronous so it runs installless; a licence file is read only for an exact candidate, one paced raw-lane request at a time, which an async client would not speed up.
                return acquirer.raw_github_get(url, "witness-populations", f"{repository}:{name}")
            except OSError as error:
                if attempt + 1 == LICENCE_FETCH_ATTEMPTS:
                    raise ScreenError(
                        f"{name} at {repository}@{commit} could not be read after {LICENCE_FETCH_ATTEMPTS} attempts "
                        f"({error}); re-run `screen --fetch-licence` once the network answers"
                    ) from error
                time.sleep(LICENCE_FETCH_BACKOFF_S * 2**attempt)
        raise AssertionError  # unreachable: the last attempt returns or raises

    return fetch


class Job(NamedTuple):
    """One worker's candidate: the entry, the repository it is read under, the store and whether to discover keys."""

    entry: Entry
    root: Path
    store_root: Path
    discover: bool


def _screen_job(job: Job) -> tuple[list[ScreenRow], Entry | None]:
    """One entry's rows, read with cache-only licence evidence; the entry back when its licence needs a fetch."""
    entry, root, store_root, discover = job
    selectors = Selectors.read(root / "docs" / "openapi-surface" / "witness-search-keys.tsv")
    with tempfile.TemporaryDirectory(prefix="population-screen-") as scratch:
        try:
            rows = screen_entry(
                entry,
                selectors,
                root=root,
                store_root=store_root,
                scratch=Path(scratch),
                fetch_file=raw_licence_fetcher(None, live=False),
                discover=discover,
            )
        except LicenceNotCached:
            return [], entry
    return rows, None


def run_screen(
    entries: list[Entry],
    *,
    root: Path = REPO,
    store_root: Path | None = None,
    fetch_file: LicenceFetch,
    discover: bool = True,
    workers: int = 1,
) -> list[ScreenRow]:
    """Every row the manifest's candidates owe.

    Candidates are read in `workers` processes with cache-only licence evidence;
    one whose exact trigger needs a licence file the cache lacks is screened again
    here with `fetch_file`, which may fetch it.
    """
    store_root = store_root or cache_root()
    jobs = [Job(entry, root, store_root, discover) for entry in entries]
    if workers > 1:
        with concurrent.futures.ProcessPoolExecutor(workers) as pool:
            results = list(pool.map(_screen_job, jobs, chunksize=4))
    else:
        results = [_screen_job(job) for job in jobs]
    rows: list[ScreenRow] = [row for found, _later in results for row in found]
    later = [entry for _found, entry in results if entry is not None]
    selectors = Selectors.read(root / "docs" / "openapi-surface" / "witness-search-keys.tsv")
    with tempfile.TemporaryDirectory(prefix="population-screen-") as scratch:
        for entry in later:
            rows += screen_entry(
                entry,
                selectors,
                root=root,
                store_root=store_root,
                scratch=Path(scratch),
                fetch_file=fetch_file,
                discover=discover,
            )
    seen: set[tuple[str, str, str]] = set()
    for row in rows:
        identity = (row.key, row.population, row.document)
        if identity in seen:
            raise ScreenError(f"two manifest entries screen {identity}: name each candidate once")
        seen.add(identity)
    return rows


# A code-search hit is pinned by its git blob, not yet by its content's SHA-256.
BLOB = re.compile(r"blob:([0-9a-f]{40})")


def blob_sha(data: bytes) -> str:
    """The git blob SHA-1 of `data`, which a code-search hit names."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()  # git's own identifier, not a security digest


def pinned_by(identity: Identity, data: bytes) -> bool:
    blob = BLOB.fullmatch(identity.pin)
    return blob_sha(data) == blob.group(1) if blob else hashlib.sha256(data).hexdigest() == identity.pin


class Identity(NamedTuple):
    """One document the acquisition plan would bring into the store, at its exact commit."""

    population: Population
    document: str
    repository: str
    commit: str
    path: str
    # The bytes it names: a 64-hex SHA-256, or `blob:<sha1>` for a code-search hit known only by its git blob.
    pin: str
    url: str
    rank: int

    def content_digest(self) -> str | None:
        """The SHA-256 the pin names, or None for a blob pin, whose content digest is learned on fetching."""
        return self.pin if SHA.fullmatch(self.pin) else None


IDENTITY_COLUMNS = Identity._fields


class Acquired(StrEnum):
    """How `acquire` had a planned identity's exact bytes, or why it did not (the ledger's `how`)."""

    RAW = "raw"  # fetched through the guarded raw lane
    STORE = "store"  # already kept in the store
    SHARED_CACHE = "shared-cache"  # recovered from the shared response cache
    DIGEST_DIFFERS = "digest-differs"  # fetched, but not the bytes the pin names


# The outcomes after which the store holds the identity's bytes.
HELD = frozenset({Acquired.RAW, Acquired.STORE, Acquired.SHARED_CACHE})
# A fetch the far end refused, with its HTTP status (0 when no answer came at all).
REFUSED_HTTP = re.compile(r"refused-http-(\d+)")


def acquisition_outcome(how: str) -> bool:
    """Whether `how` is an outcome `acquire` writes."""
    return how in {outcome.value for outcome in Acquired} or REFUSED_HTTP.fullmatch(how) is not None


# The populations whose documents the plan fetches at their exact commit.
ACQUIRED = ("github", "sourcegraph", "handed-off")


def cache_scan(responses: Path) -> dict[str, Path]:
    """Every exact document the shared response cache holds, by its SHA-256: raw bodies and base64 contents."""
    guard = _load("rate_limit_guard", REPO / "tools" / "witness-search" / "rate_limit_guard.py")
    found: dict[str, Path] = {}
    for _key, digest, body in guard.cached_bodies(responses):
        found.setdefault(digest, body)
        try:
            with body.open("rb") as handle:
                if handle.read(1) != b"{":
                    continue
            payload = json.loads(body.read_bytes())
        except (OSError, ValueError):
            continue
        if (
            isinstance(payload, dict)
            and payload.get("encoding") == "base64"
            and isinstance(payload.get("content"), str)
        ):
            try:
                data = base64.b64decode("".join(payload["content"].split()), validate=True)
            except binascii.Error:
                continue
            found.setdefault(hashlib.sha256(data).hexdigest(), body)
    return found


def body_bytes(path: Path, sha256: str) -> bytes | None:
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() == sha256:
        return data
    try:
        payload = json.loads(data)
    except ValueError:
        return None
    if not (
        isinstance(payload, dict) and payload.get("encoding") == "base64" and isinstance(payload.get("content"), str)
    ):
        return None
    try:
        decoded = base64.b64decode("".join(payload["content"].split()), validate=True)
    except binascii.Error:
        return None
    return decoded if hashlib.sha256(decoded).hexdigest() == sha256 else None


def acquire(
    identities: list[Identity],
    *,
    evidence: Path,
    budget_s: float,
    responses: Path,
    store_root: Path | None = None,
    raw_base: str | None = None,
    out: IO[str] = sys.stdout,
) -> Counter[str]:
    """Bring each identity's exact bytes into the store, cheapest first, until `budget_s` of live fetching is spent."""
    github = _load("population_screen_github", REPO / "tools" / "witness-search" / "witness-search-github.py")
    store_root = store_root or cache_root()
    raw_base = raw_base or github.checked_service_url(
        os.environ.get("CROZIER_RAW_GITHUB_URL", github.RAW_GITHUB_URL),
        "CROZIER_RAW_GITHUB_URL",
        "raw.githubusercontent.com",
    )
    acquirer = github.Acquirer(evidence, cache=store_root / "acquirer", raw_github_url=raw_base)
    scanned = cache_scan(responses) if responses.is_dir() else {}
    tally: Counter[str] = Counter()
    started = time.monotonic()
    ledger = evidence / "acquisitions.jsonl"
    evidence.mkdir(parents=True, exist_ok=True)
    for identity in sorted(identities, key=lambda i: (-i.rank, i.population, i.document, i.pin)):
        how = ""
        sha256 = identity.content_digest() or identity.pin
        if identity.content_digest() and cached(sha256, store_root) is not None:
            how = Acquired.STORE
        elif sha256 in scanned and (data := body_bytes(scanned[sha256], sha256)):
            store(data, store_root)
            how = Acquired.SHARED_CACHE
        elif time.monotonic() - started >= budget_s:
            tally["budget-spent"] += 1
            continue
        else:
            url = f"{raw_base.rstrip('/')}/{identity.repository}/{identity.commit}/{urllib.parse.quote(identity.path)}"
            try:
                # llmlint: ignore[async_typed_clients_at_boundaries] AGENTS.md keeps the witness tooling stdlib-only and synchronous so it runs installless; the raw lane is paced one request at a time, so an async client would not fetch the plan any faster.
                status, data = acquirer.raw_github_get(
                    url, "witness-populations", f"{identity.repository}:{identity.path}"
                )
            except OSError as error:
                status, data = 0, str(error).encode()
            if status == 200 and pinned_by(identity, data):
                sha256 = store(data, store_root).name
                how = Acquired.RAW
            else:
                how = f"refused-http-{status}" if status != 200 else Acquired.DIGEST_DIFFERS
        tally[how] += 1
        with ledger.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(
                json.dumps({**identity._asdict(), "how": how, "content_sha256": sha256}, sort_keys=True) + "\n"
            )
    print(
        "population-screen: acquire: " + ", ".join(f"{name} {count}" for name, count in sorted(tally.items())),
        file=out,
    )
    return tally


def open_text(path: Path) -> IO[str]:
    """`path` opened for reading as UTF-8 text, through gzip when it is a `.gz`."""
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8", newline="")
    return path.open(encoding="utf-8", newline="")


def read_identities(path: Path) -> list[Identity]:
    """An acquisition plan, plain or gzip-compressed (`.gz`)."""
    with open_text(path) as handle:
        reader = csv.reader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if tuple(next(reader, ())) != IDENTITY_COLUMNS:
            raise ScreenError(f"{path}: its header is not {'/'.join(IDENTITY_COLUMNS)}")
        rows = []
        for number, cells in enumerate(reader, 2):
            if len(cells) != len(IDENTITY_COLUMNS):
                raise ScreenError(f"{path}:{number}: not {len(IDENTITY_COLUMNS)} cells")
            if cells[0] not in ACQUIRED:
                raise ScreenError(f"{path}:{number}: population {cells[0]!r} is none of {', '.join(ACQUIRED)}")
            if not cells[7].isdigit():
                raise ScreenError(f"{path}:{number}: rank {cells[7]!r} is no whole number")
            identity = Identity(Population(cells[0]), *cells[1:7], rank=int(cells[7]))
            pinned = SHA.fullmatch(identity.pin) or BLOB.fullmatch(identity.pin)
            if not COMMIT.fullmatch(identity.commit) or not pinned:
                raise ScreenError(f"{path}:{number}: no full commit, or no SHA-256 or blob pin")
            if identity.population not in ACQUIRED or not witness_screen().repository_name(identity.repository):
                raise ScreenError(
                    f"{path}:{number}: {identity.population} {identity.repository!r} is no acquired population's "
                    f"`owner/name` repository ({', '.join(ACQUIRED)})"
                )
            if not witness_screen().repository_path(identity.path):
                raise ScreenError(f"{path}:{number}: {identity.path!r} is no path inside a repository")
            named = (
                f"{identity.repository}:{identity.path}@{identity.commit}"
                if identity.population == Population.HANDED_OFF
                else f"{identity.repository}/{identity.path}"
            )
            if identity.document != named:
                raise ScreenError(
                    f"{path}:{number}: document {identity.document!r} is not the {named!r} its repository, path and "
                    "commit name"
                )
            rows.append(identity)
    return rows


def positive_int(text: str) -> int:
    try:
        value = int(text)
    except ValueError:
        value = 0
    if value < 1:
        raise argparse.ArgumentTypeError(f"{text!r} is no positive whole number")
    return value


def budget_seconds(text: str) -> float:
    try:
        value = float(text)
    except ValueError:
        value = math.nan
    if not math.isfinite(value) or value < 0:
        raise argparse.ArgumentTypeError(f"{text!r} is no finite, non-negative number of seconds")
    return value


def sha256_arg(text: str) -> str:
    if not SHA.fullmatch(text):
        raise argparse.ArgumentTypeError(f"{text!r} is no 64-hex SHA-256")
    return text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check", help="read a screen table through the reader and print its counts")
    check.add_argument("table", type=Path, nargs="?", default=TABLE)
    screen = sub.add_parser("screen", help="screen every manifest candidate and write the table")
    screen.add_argument("--manifest", type=Path, default=POPULATION)
    screen.add_argument("--output", type=Path, default=TABLE)
    screen.add_argument("--store", type=Path, help="the document store; defaults to the host cache")
    screen.add_argument(
        "--evidence", type=Path, default=RECORD / "licences", help="where a live licence read logs its calls"
    )
    screen.add_argument("--fetch-licence", action="store_true", help="fetch an exact candidate's uncached licence file")
    screen.add_argument("--no-discover", action="store_true", help="screen only the keys the manifest names")
    screen.add_argument("--workers", type=positive_int, default=1)
    grab = sub.add_parser("acquire", help="bring identities' exact bytes into the store")
    grab.add_argument("--identities", type=Path, required=True)
    grab.add_argument("--evidence", type=Path, required=True)
    grab.add_argument("--budget-seconds", type=budget_seconds, default=3300.0)
    grab.add_argument("--store", type=Path)
    grab.add_argument(
        "--responses",
        type=Path,
        default=Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache") / "crozier" / "github-responses",
    )
    find = sub.add_parser("cached", help="print where a candidate's exact bytes are kept")
    find.add_argument("sha256", type=sha256_arg)
    find.add_argument("--store", type=Path)
    args = parser.parse_args(argv)
    try:
        match args.command:
            case "check":
                rows = read_screen(args.table)
                counts = Counter(row.status.split(":", 1)[0] for row in rows)
                print(
                    f"population-screen: {len(rows)} rows; " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
                )
            case "screen":
                rows = run_screen(
                    read_manifest(args.manifest),
                    store_root=args.store,
                    fetch_file=raw_licence_fetcher(args.evidence, args.fetch_licence),
                    discover=not args.no_discover,
                    workers=args.workers,
                )
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(render(rows), encoding="utf-8", newline="\n")
                read_screen(args.output)
                print(f"population-screen: wrote {len(rows)} rows, {sum(pending_counts(rows).values())} pending")
            case "acquire":
                acquire(
                    read_identities(args.identities),
                    evidence=args.evidence,
                    budget_s=args.budget_seconds,
                    responses=args.responses,
                    store_root=args.store,
                )
            case _:
                root = args.store or cache_root()
                if cached(args.sha256, root) is None:
                    fail(
                        f"no bytes carrying sha256 {args.sha256} are kept in {root}; re-fetch them from the row's source"
                    )
                print(root / args.sha256)
        return 0
    except ScreenError as error:
        fail(str(error))


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""The combination population screen, driven through its real CLI and its reader.

`tools/witness-search/population_screen.py screen` runs as a subprocess over
authored documents kept in a temporary store, each built to satisfy or to miss
one condition of a key's trigger, and its table is read back through
`read_screen`, the reader every consumer uses. A licence file and an acquired
document are served by a loopback server standing in for
raw.githubusercontent.com (the guarded raw lane's `CROZIER_RAW_GITHUB_URL`); no
other boundary is doubled. The committed table is read through the same reader,
and its registered rows, whose bytes are in the tree, are screened again.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, ClassVar

os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "witness-search" / "population_screen.py"
COMMIT = "a" * 40
MIT = {"title": "probe", "version": "1", "license": {"name": "MIT"}}


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SCREEN = load("population_screen_under_test", SCRIPT)


def document(*, info: dict[str, Any] | None = None, paths: Any = None, schemas: Any = None, **extra: Any) -> dict:
    body: dict[str, Any] = {"openapi": "3.1.0", "info": info or MIT, "paths": paths or {}}
    if schemas is not None:
        body["components"] = {"schemas": schemas}
    body.update(extra)
    return body


def get(response_schema: Any = None, **operation: Any) -> dict:
    responses: dict[str, dict[str, Any]] = {"200": {"description": "OK"}}
    if response_schema is not None:
        responses["200"]["content"] = {"application/json": {"schema": response_schema}}
    return {"responses": responses, **operation}


def holder(document_schemas: dict, holder_properties: dict) -> dict:
    return document(
        paths={"/holder": {"get": get({"$ref": "#/components/schemas/Holder"}, operationId="getHolder")}},
        schemas={"Holder": {"type": "object", "properties": holder_properties}, **document_schemas},
    )


NAMED = {
    "Named": {
        "type": "object",
        "properties": {"label": {"type": "string", "$defs": {"inner": {"type": "string"}}}},
        # A JSON pointer resolves through `definitions`; crozier's component-pointer walk does not.
        "definitions": {"inner": {"type": "string"}},
    }
}
POINTER_KEYS = (
    "combo-allof-unresolved-nested-pointer",
    "combo-array-unresolved-nested-pointer",
    "combo-map-unresolved-nested-pointer",
    "combo-property-unresolved-nested-pointer",
    "combo-request-unresolved-nested-pointer",
    "combo-response-unresolved-nested-pointer",
)


def pointers(ref: str, *, typed: bool = True) -> dict:
    """One document placing `ref` at each of the six unresolved-pointer placements."""
    return document(
        paths={
            "/holder": {
                "post": {
                    "operationId": "createHolder",
                    "requestBody": {"content": {"application/json": {"schema": {"$ref": ref}}}},
                    "responses": {
                        "200": {"description": "OK", "content": {"application/json": {"schema": {"$ref": ref}}}}
                    },
                }
            }
        },
        schemas={
            **NAMED,
            "Holder": {
                "type": "object",
                "properties": {
                    "ghost": {"$ref": ref},
                    "list": {**({"type": "array"} if typed else {}), "items": {"$ref": ref}},
                    "byName": {**({"type": "object"} if typed else {}), "additionalProperties": {"$ref": ref}},
                    "merged": {"allOf": [{"$ref": ref}]},
                },
            },
        },
    )


def tagged(names: list[str], *, required: bool, enum_values: int = 1, discriminator: bool = False) -> dict:
    variants = {}
    for name in names:
        values = [name.lower()] if enum_values == 1 else [name.lower(), f"{name.lower()}-other"]
        variants[name] = {
            "type": "object",
            "required": ["kind", "size"] if required else ["size"],
            "properties": {"kind": {"type": "string", "enum": values}, "size": {"type": "integer"}},
        }
    refs = [{"$ref": f"#/components/schemas/{name}"} for name in names]
    union: dict[str, Any] = {"oneOf": refs}
    anyof: dict[str, Any] = {"anyOf": refs}
    if discriminator:
        union["discriminator"] = {"propertyName": "kind"}
        anyof["discriminator"] = {"propertyName": "kind"}
    return holder(
        {**variants, "Union": union},
        {"one": {"$ref": "#/components/schemas/Union"}, "many": {"type": "array", "items": anyof}},
    )


def header(schema: dict, *, name: str = "X-Mode", required: bool = False, second_operation: bool = False) -> dict:
    parameter = {"name": name, "in": "header", "schema": schema, **({"required": True} if required else {})}
    paths = {"/probe": {"get": get(operationId="probe", parameters=[parameter])}}
    if second_operation:
        paths["/other"] = {"get": get(operationId="other")}
    return document(paths=paths)


def query(schema: dict, *, required: bool = True, schemas: dict | None = None) -> dict:
    parameter = {"name": "filter", "in": "query", "schema": schema, **({"required": True} if required else {})}
    return document(paths={"/items": {"get": get(operationId="listItems", parameters=[parameter])}}, schemas=schemas)


CASTE = {"Caste": {"type": "string", "enum": ["worker", "drone"]}}
PLAIN = {"Plain": {"type": "string"}}


def collision(
    body: dict, *, path_parameter: str = "name", path_level: bool = False, schemas: dict | None = None
) -> dict:
    parameter = {"name": path_parameter, "in": "path", "required": True, "schema": {"type": "string"}}
    operation: dict[str, Any] = {
        "operationId": "update",
        "requestBody": {"content": {"application/json": {"schema": body}}},
        "responses": {"204": {"description": "No Content"}},
    }
    item: dict[str, Any] = {"patch": operation}
    if path_level:
        item["parameters"] = [parameter]
    else:
        operation["parameters"] = [parameter]
    return document(paths={"/repos/{" + path_parameter + "}": item}, schemas=schemas)


def success(schema: dict, *, status: str = "200", schemas: dict | None = None) -> dict:
    return document(
        paths={
            "/value": {
                "get": {
                    "operationId": "value",
                    "responses": {
                        "400" if status != "400" else "200": {"description": "other"},
                        status: {"description": "it", "content": {"application/json": {"schema": schema}}},
                    },
                }
            }
        },
        schemas=schemas,
    )


A, B = {"$ref": "#/components/schemas/A"}, {"$ref": "#/components/schemas/B"}
AB = {
    "A": {"type": "object", "properties": {"a": {"type": "string"}}},
    "B": {"type": "object", "properties": {"b": {"type": "string"}}},
}
NULL = {"type": "null"}

# (case, document, {key: expected trigger}). A document often answers several keys.
CASES: list[tuple[str, dict, dict[str, str]]] = [
    ("pointer-exact", pointers("#/components/schemas/Named/properties/absent"), dict.fromkeys(POINTER_KEYS, "exact")),
    (
        "pointer-undeclared-head",
        pointers("#/components/schemas/Missing/properties/absent"),
        dict.fromkeys(POINTER_KEYS, "exact"),
    ),
    (
        "pointer-through-definitions",
        pointers("#/components/schemas/Named/definitions/inner"),
        dict.fromkeys(POINTER_KEYS, "exact"),
    ),
    (
        "pointer-resolves",
        pointers("#/components/schemas/Named/properties/label"),
        dict.fromkeys(POINTER_KEYS, "partial:nested-pointer-resolves"),
    ),
    (
        "pointer-flat",
        pointers("#/components/schemas/Named"),
        dict.fromkeys(POINTER_KEYS, "partial:pointer-not-a-nested-component-pointer"),
    ),
    (
        "pointer-untyped-owners",
        pointers("#/components/schemas/Named/properties/absent", typed=False),
        {
            "combo-array-unresolved-nested-pointer": "partial:items-owner-not-type-array",
            "combo-map-unresolved-nested-pointer": "partial:map-owner-not-type-object",
            "combo-property-unresolved-nested-pointer": "exact",
        },
    ),
    (
        "no-pointer",
        document(paths={"/a": {"get": get({"type": "string"})}}),
        {
            **dict.fromkeys(POINTER_KEYS, "absent"),
            "combo-array-defs-pointer": "absent",
            "combo-property-defs-pointer": "absent",
        },
    ),
    (
        "defs-exact",
        holder(
            NAMED,
            {
                "inner": {"$ref": "#/components/schemas/Named/properties/label/$defs/inner"},
                "names": {
                    "type": "array",
                    "items": {"$ref": "#/components/schemas/Named/properties/label/$defs/inner"},
                },
            },
        ),
        {"combo-array-defs-pointer": "exact", "combo-property-defs-pointer": "exact"},
    ),
    (
        "defs-top-level",
        holder(
            {"Named": {"type": "object", "$defs": {"inner": {"type": "string"}}}},
            {
                "inner": {"$ref": "#/components/schemas/Named/$defs/inner"},
                "names": {"type": "array", "items": {"$ref": "#/components/schemas/Named/$defs/inner"}},
            },
        ),
        dict.fromkeys(
            ("combo-array-defs-pointer", "combo-property-defs-pointer"),
            "partial:defs-pointer-not-through-a-properties-segment",
        ),
    ),
    (
        "defs-dangling",
        holder(
            NAMED,
            {
                "inner": {"$ref": "#/components/schemas/Named/properties/label/$defs/gone"},
                "names": {"type": "array", "items": {"$ref": "#/components/schemas/Named/properties/label/$defs/gone"}},
            },
        ),
        dict.fromkeys(
            ("combo-array-defs-pointer", "combo-property-defs-pointer"), "partial:defs-pointer-does-not-resolve"
        ),
    ),
    (
        "defs-none",
        holder(
            NAMED,
            {
                "inner": {"$ref": "#/components/schemas/Named/properties/label"},
                "names": {"type": "array", "items": {"$ref": "#/components/schemas/Named/properties/label"}},
            },
        ),
        dict.fromkeys(
            ("combo-array-defs-pointer", "combo-property-defs-pointer"), "partial:pointer-not-through-a-defs-member"
        ),
    ),
    (
        "defs-untyped-owner",
        holder(
            NAMED,
            {
                "names": {
                    "type": "object",
                    "items": {"$ref": "#/components/schemas/Named/properties/label/$defs/inner"},
                },
            },
        ),
        {"combo-array-defs-pointer": "partial:items-owner-not-type-array"},
    ),
    (
        "anyof-shared-base",
        holder(
            {
                "Pet": {
                    "anyOf": [
                        {
                            "type": "object",
                            "properties": {"kind": {"type": "string", "enum": ["cat"]}, "meow": {"type": "string"}},
                        },
                        {"type": "object", "properties": {"kind": {"type": "string", "enum": ["dog"]}}},
                    ],
                    "properties": {"kind": {"type": "string"}, "name": {"type": "string"}},
                }
            },
            {"pet": {"$ref": "#/components/schemas/Pet"}},
        ),
        {"combo-anyof-beside-properties": "exact"},
    ),
    (
        "anyof-referenced-members",
        holder(
            {**AB, "Pet": {"anyOf": [A, B], "properties": {"name": {"type": "string"}}}},
            {"pet": {"$ref": "#/components/schemas/Pet"}},
        ),
        {"combo-anyof-beside-properties": "partial:a-member-is-a-reference"},
    ),
    (
        "anyof-untagged-members",
        holder(
            {
                "Pet": {
                    "anyOf": [{"type": "object", "properties": {"a": {"type": "string"}}}, {"type": "string"}],
                    "properties": {"name": {"type": "string"}},
                }
            },
            {},
        ),
        {"combo-anyof-beside-properties": "partial:members-share-no-one-valued-tag-property"},
    ),
    (
        "anyof-tag-alone",
        holder(
            {
                "Pet": {
                    "anyOf": [{"properties": {"kind": {"const": "cat"}}}, {"properties": {"kind": {"const": "dog"}}}],
                    "properties": {"kind": {"type": "string"}},
                }
            },
            {},
        ),
        {"combo-anyof-beside-properties": "partial:no-property-beside-the-tag"},
    ),
    (
        "anyof-no-properties",
        holder({"Pet": {"anyOf": [{"type": "string"}, {"type": "integer"}]}}, {}),
        {"combo-anyof-beside-properties": "partial:no-properties-beside-anyof"},
    ),
    (
        "tag-unrequired",
        tagged(["Reflector", "Refractor"], required=False),
        {"combo-unrequired-tag-oneof-reference": "exact", "combo-unrequired-tag-anyof-reference": "exact"},
    ),
    (
        "tag-required",
        tagged(["Reflector", "Refractor"], required=True),
        dict.fromkeys(
            ("combo-unrequired-tag-oneof-reference", "combo-unrequired-tag-anyof-reference"),
            "partial:every-member-requires-its-tag",
        ),
    ),
    (
        "tag-discriminated",
        tagged(["Reflector", "Refractor"], required=False, discriminator=True),
        {
            "combo-unrequired-tag-oneof-reference": "partial:union-declares-a-discriminator",
            "combo-unrequired-tag-anyof-reference": "exact",
        },
    ),
    (
        "tag-many-valued",
        tagged(["Reflector", "Refractor"], required=False, enum_values=2),
        dict.fromkeys(
            ("combo-unrequired-tag-oneof-reference", "combo-unrequired-tag-anyof-reference"),
            "partial:members-share-no-one-valued-tag-property",
        ),
    ),
    (
        "tag-no-enum",
        holder(
            {**AB, "Union": {"oneOf": [A, B]}}, {"u": {"$ref": "#/components/schemas/Union"}, "v": {"anyOf": [A, B]}}
        ),
        dict.fromkeys(
            ("combo-unrequired-tag-oneof-reference", "combo-unrequired-tag-anyof-reference"),
            "partial:no-referenced-member-declares-a-string-enum-property",
        ),
    ),
    (
        "tag-inline",
        holder(
            {},
            {
                "u": {"oneOf": [{"type": "string"}, {"type": "integer"}]},
                "v": {"anyOf": [{"type": "string"}, {"type": "integer"}]},
            },
        ),
        dict.fromkeys(
            ("combo-unrequired-tag-oneof-reference", "combo-unrequired-tag-anyof-reference"),
            "partial:no-member-is-a-reference",
        ),
    ),
]


def nullable_parent(*, nullable: bool = True, typed: bool = True, own: dict | None = None) -> dict:
    members: list[dict[str, Any]] = [{"$ref": "#/components/schemas/FileMini"}]
    conflict: dict[str, Any] = {"allOf": members}
    if own is not None:
        members.append({"properties": own})
    if typed:
        conflict["type"] = "object"
    mini = {"type": "object", "properties": {"sha1": {"type": "string"}}, **({"nullable": True} if nullable else {})}
    return holder({"FileConflict": conflict, "FileMini": mini}, {"file": {"$ref": "#/components/schemas/FileConflict"}})


KEY_N = "combo-nullable-allof-parent-own-property"
KEY_C = "combo-property-anyof-composed-sibling"
KEY_HA = "combo-header-array-accepted-placements"
KEY_HD = "combo-header-string-default"
KEY_Q = "combo-required-query-array-enum-items"
KEY_O = "combo-query-param-inline-object"
KEY_T = "combo-tag-only-operation-id"
KEY_B = "combo-body-property-named-as-path-param"
KEY_M = "combo-map-beside-oneof"
KEY_SA = "combo-success-anyof-nullable"
KEY_SO = "combo-success-oneof-nullable"
CASES += [
    ("nullable-parent-collides", nullable_parent(own={"sha1": {"type": "string"}}), {KEY_N: "exact"}),
    (
        "nullable-parent-other-name",
        nullable_parent(own={"other": {"type": "string"}}),
        {KEY_N: "partial:no-own-property-shares-a-nullable-parent-property-name"},
    ),
    ("nullable-parent-no-own", nullable_parent(), {KEY_N: "partial:no-own-property-declared"}),
    (
        "parent-not-nullable",
        nullable_parent(nullable=False, own={"sha1": {"type": "string"}}),
        {KEY_N: "partial:no-allof-reference-to-a-nullable-parent"},
    ),
    (
        "nullable-parent-untyped",
        nullable_parent(typed=False, own={"sha1": {"type": "string"}}),
        {KEY_N: "partial:not-type-object"},
    ),
    (
        "anyof-composed",
        holder({}, {"note": {"anyOf": [{"oneOf": [{"type": "number"}, {"type": "string"}]}, {"type": "boolean"}]}}),
        {KEY_C: "exact"},
    ),
    (
        "anyof-composed-with-null",
        holder({}, {"note": {"anyOf": [{"oneOf": [{"type": "number"}, {"type": "string"}]}, NULL]}}),
        {KEY_C: "partial:anyof-has-fewer-than-two-non-null-members"},
    ),
    (
        "anyof-flat",
        holder({}, {"note": {"anyOf": [{"type": "string"}, {"type": "integer"}]}}),
        {KEY_C: "partial:no-anyof-member-is-a-oneof"},
    ),
    (
        "header-array",
        header({"type": "array", "items": {"type": "string"}}, required=True, second_operation=True),
        {KEY_HA: "exact", KEY_HD: "partial:schema-declares-no-default"},
    ),
    ("header-array-promoted", header({"type": "array", "items": {"type": "string"}}), {KEY_HA: "exact"}),
    (
        "header-array-ref-items",
        header({"type": "array", "items": {"$ref": "#/components/schemas/Plain"}}),
        {KEY_HA: "partial:items-are-a-reference"},
    ),
    (
        "header-array-integer-items",
        header({"type": "array", "items": {"type": "integer"}}),
        {KEY_HA: "partial:items-not-type-string"},
    ),
    (
        "header-string-default",
        header({"type": "string", "default": "all"}),
        {KEY_HD: "exact", KEY_HA: "partial:schema-not-type-array"},
    ),
    ("header-number-default", header({"type": "integer", "default": 5}), {KEY_HD: "partial:default-not-a-string"}),
    (
        "header-required-integer",
        header({"type": "integer", "default": "5"}, required=True),
        {KEY_HD: "partial:required-header-not-type-string"},
    ),
    (
        "header-client-managed",
        header({"type": "string", "default": "application/json"}, name="Accept"),
        {KEY_HD: "partial:header-is-client-managed"},
    ),
    (
        "header-on-one-operation",
        header({"type": "string", "default": "all"}, second_operation=True),
        {KEY_HD: "partial:header-not-on-every-operation"},
    ),
    ("no-header", document(paths={"/a": {"get": get()}}), {KEY_HA: "absent", KEY_HD: "absent"}),
    (
        "query-enum-array",
        query({"type": "array", "items": {"$ref": "#/components/schemas/Caste"}}, schemas=CASTE),
        {KEY_Q: "exact", KEY_O: "partial:schema-not-primary-type-object"},
    ),
    (
        "query-enum-array-optional",
        query({"type": "array", "items": {"$ref": "#/components/schemas/Caste"}}, required=False, schemas=CASTE),
        {KEY_Q: "partial:parameter-not-required"},
    ),
    ("query-scalar", query({"type": "string"}), {KEY_Q: "partial:schema-not-primary-type-array"}),
    (
        "query-inline-enum",
        query({"type": "array", "items": {"type": "string", "enum": ["a"]}}),
        {KEY_Q: "partial:items-not-a-reference"},
    ),
    (
        "query-plain-items",
        query({"type": "array", "items": {"$ref": "#/components/schemas/Plain"}}, schemas=PLAIN),
        {KEY_Q: "partial:items-target-declares-no-string-enum"},
    ),
    ("query-object", query({"type": "object", "properties": {"a": {"type": "string"}}}), {KEY_O: "exact"}),
    (
        "query-object-optional",
        query({"type": "object", "properties": {"a": {"type": "string"}}}, required=False),
        {KEY_O: "partial:parameter-not-required"},
    ),
    (
        "query-object-reference",
        query({"$ref": "#/components/schemas/Caste"}, schemas=CASTE),
        {KEY_O: "partial:schema-is-a-reference"},
    ),
    ("query-object-empty", query({"type": "object"}), {KEY_O: "partial:schema-declares-no-properties"}),
    ("no-query", document(paths={"/a": {"get": get()}}), {KEY_Q: "absent", KEY_O: "absent"}),
    (
        "tag-only-id",
        document(paths={"/search": {"get": get(operationId="Search_", tags=["Search"])}}),
        {KEY_T: "exact"},
    ),
    (
        "tag-method-id",
        document(paths={"/search": {"get": get(operationId="Search_list", tags=["Search"])}}),
        {KEY_T: "partial:operation-id-not-its-first-tag-and-underscores"},
    ),
    ("untagged-id", document(paths={"/search": {"get": get(operationId="Search_")}}), {KEY_T: "absent"}),
    ("body-names-path", collision({"type": "object", "properties": {"name": {"type": "string"}}}), {KEY_B: "exact"}),
    (
        "body-names-path-level",
        collision(
            {"$ref": "#/components/schemas/Repo"},
            path_level=True,
            schemas={"Repo": {"type": "object", "properties": {"name": {"type": "string"}}}},
        ),
        {KEY_B: "exact"},
    ),
    (
        "body-other-name",
        collision({"type": "object", "properties": {"title": {"type": "string"}}}),
        {KEY_B: "partial:no-body-property-named-as-a-path-parameter"},
    ),
    ("body-scalar", collision({"type": "string"}), {KEY_B: "partial:body-writes-no-object-properties"}),
    (
        "body-no-path",
        document(
            paths={
                "/repos": {
                    "post": {
                        "requestBody": {
                            "content": {"application/json": {"schema": {"type": "object", "properties": {"name": {}}}}}
                        },
                        "responses": {"204": {"description": "ok"}},
                    }
                }
            }
        ),
        {KEY_B: "partial:no-path-parameter"},
    ),
    (
        "map-oneof",
        holder(
            {},
            {
                "m": {"oneOf": [{"type": "string"}, {"type": "integer"}], "additionalProperties": {"type": "string"}},
                "t": {"oneOf": [{"type": "string"}], "additionalProperties": True},
            },
        ),
        {KEY_M: "exact"},
    ),
    (
        "map-oneof-true",
        holder({}, {"t": {"oneOf": [{"type": "string"}], "additionalProperties": True}}),
        {KEY_M: "exact"},
    ),
    (
        "closed-oneof",
        holder({}, {"m": {"oneOf": [{"type": "string"}], "additionalProperties": False}}),
        {KEY_M: "partial:additional-properties-neither-a-schema-nor-true"},
    ),
    (
        "map-oneof-properties",
        holder(
            {},
            {
                "m": {
                    "oneOf": [{"type": "string"}],
                    "additionalProperties": {"type": "string"},
                    "properties": {"a": {"type": "string"}},
                }
            },
        ),
        {KEY_M: "partial:properties-declared-beside-the-map"},
    ),
    (
        "oneof-alone",
        holder({}, {"m": {"oneOf": [{"type": "string"}]}}),
        {KEY_M: "partial:no-additional-properties-beside-oneof"},
    ),
    ("success-anyof-null", success({"anyOf": [A, NULL]}, schemas=AB), {KEY_SA: "exact", KEY_SO: "absent"}),
    (
        "success-oneof-nullable",
        success({"$ref": "#/components/schemas/U"}, schemas={**AB, "U": {"oneOf": [A, B], "nullable": True}}),
        {KEY_SO: "exact", KEY_SA: "absent"},
    ),
    (
        "success-unions-not-null",
        document(
            paths={
                "/a": {
                    "get": {
                        "responses": {
                            "200": {"description": "a", "content": {"application/json": {"schema": {"anyOf": [A, B]}}}}
                        }
                    }
                },
                "/b": {
                    "get": {
                        "responses": {
                            "200": {"description": "b", "content": {"application/json": {"schema": {"oneOf": [A, B]}}}}
                        }
                    }
                },
            },
            schemas=AB,
        ),
        {KEY_SA: "partial:anyof-success-schema-not-nullable", KEY_SO: "partial:oneof-success-schema-not-nullable"},
    ),
    ("error-anyof-null", success({"anyOf": [A, NULL]}, status="400", schemas=AB), {KEY_SA: "absent"}),
]


class _RawServer(ThreadingHTTPServer):
    files: dict[str, bytes]
    requests: list[str]


class _Raw(BaseHTTPRequestHandler):
    """raw.githubusercontent.com's exact-commit route, serving `server.files`."""

    server: _RawServer

    def log_message(self, format: str, *args: Any) -> None:
        pass

    def do_GET(self) -> None:
        self.server.requests.append(self.path)
        body = self.server.files.get(self.path)
        self.send_response(200 if body is not None else 404)
        body = body if body is not None else b"404: Not Found"
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


class ScreenHarness(unittest.TestCase):
    """A temporary store, host cache and loopback raw route for one test."""

    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory(prefix="population-screen-")
        self.addCleanup(scratch.cleanup)
        self.scratch = Path(scratch.name)
        self.store = self.scratch / "store"
        server = _RawServer(("127.0.0.1", 0), _Raw)
        server.files, server.requests = {}, []
        self.server = server
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        self.env = {
            **os.environ,
            "XDG_CACHE_HOME": str(self.scratch / "xdg"),
            "CROZIER_RAW_GITHUB_URL": f"http://127.0.0.1:{server.server_port}",
        }

    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            env=self.env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=REPO,
            timeout=600,
        )

    def entry(
        self, name: str, data: bytes, keys: list[str], *, evidence: str | None = None, unfetchable: str = "-"
    ) -> list[str]:
        digest = hashlib.sha256(data).hexdigest()
        if unfetchable == "-":
            SCREEN.store(data, self.store)
        repository = f"acme/{name}"
        return [
            "github",
            f"{repository}/openapi.json",
            f"https://raw.githubusercontent.com/{repository}/{COMMIT}/openapi.json",
            digest if unfetchable == "-" or data else "-",
            evidence or f"repository:{repository}@{COMMIT}",
            ";".join(keys) or "-",
            unfetchable,
        ]

    def manifest(self, rows: list[list[str]]) -> Path:
        path = self.scratch / "population.tsv"
        path.write_text(
            "\t".join(SCREEN.MANIFEST_COLUMNS) + "\n" + "".join("\t".join(row) + "\n" for row in rows), encoding="utf-8"
        )
        return path

    def screen(self, rows: list[list[str]], *extra: str) -> tuple[subprocess.CompletedProcess[str], Path]:
        output = self.scratch / "screen.tsv"
        done = self.run_cli(
            "screen",
            "--manifest",
            str(self.manifest(rows)),
            "--output",
            str(output),
            "--store",
            str(self.store),
            "--evidence",
            str(self.scratch / "evidence"),
            *extra,
        )
        return done, output


class TriggerConditionTests(ScreenHarness):
    def test_each_condition_met_and_missed_is_recorded_as_the_trigger_screen_reads_it(self) -> None:
        rows = [self.entry(name, json.dumps(body).encode(), sorted(expected)) for name, body, expected in CASES]
        done, output = self.screen(rows, "--no-discover", "--workers", "2")
        self.assertEqual(0, done.returncode, done.stderr)
        table = {(row.key, row.document.split("/")[1]): row for row in SCREEN.read_screen(output)}
        for name, _body, expected in CASES:
            for key, verdict in expected.items():
                with self.subTest(case=name, key=key):
                    row = table[(key, name)]
                    self.assertEqual(verdict, row.trigger)
                    self.assertEqual("admissible:MIT (info.license 'MIT')", row.licence)
                    self.assertEqual(
                        "certified-screen-pending" if verdict == "exact" else "rejected-trigger", row.status
                    )
        self.assertEqual(sum(len(expected) for _n, _b, expected in CASES), len(table))
        # Every condition each key's screen names is met and missed by some authored case.
        missed = {
            (key, verdict.split(":", 1)[1]) for _n, _b, e in CASES for key, verdict in e.items() if ":" in verdict
        }
        for key, conditions in SCREEN.CONDITIONS.items():
            for condition in conditions:
                with self.subTest(key=key, condition=condition):
                    self.assertIn((key, condition), missed)
            with self.subTest(key=key, met=True):
                self.assertTrue(any(e.get(key) == "exact" for _n, _b, e in CASES))

    def test_discovery_adds_every_key_the_census_finds_declared(self) -> None:
        body = json.dumps(CASES[0][1]).encode()
        done, output = self.screen([self.entry("pointer", body, ["combo-property-unresolved-nested-pointer"])])
        self.assertEqual(0, done.returncode, done.stderr)
        keys = {row.key for row in SCREEN.read_screen(output)}
        self.assertTrue(set(POINTER_KEYS) <= keys, keys)

    def test_the_authored_probes_each_read_exact_for_their_keys(self) -> None:
        with (REPO / "docs/openapi-surface/authored-probes/evidence-tiers.tsv").open(encoding="utf-8") as handle:
            probes = [row for row in csv.DictReader(handle, delimiter="\t") if row["tier"] == "open"]
        rows = [self.entry(row["case"], (REPO / row["source"]).read_bytes(), row["keys"].split(";")) for row in probes]
        # The probes declare no info.license: their licence file is served at the pinned commit.
        for row in probes:
            self.server.files[f"/acme/{row['case']}/{COMMIT}/LICENSE"] = b"MIT License\n"
        done, output = self.screen(rows, "--no-discover", "--fetch-licence")
        self.assertEqual(0, done.returncode, done.stderr)
        screened = SCREEN.read_screen(output)
        self.assertEqual(sum(len(row["keys"].split(";")) for row in probes), len(screened))
        for row in screened:
            with self.subTest(case=row.document, key=row.key):
                self.assertEqual(("exact", f"admissible:MIT (LICENSE at {COMMIT})"), (row.trigger, row.licence))


class LicenceScreenTests(ScreenHarness):
    EXACT = json.dumps(
        document(
            info={"title": "t", "version": "1"}, paths={"/search": {"get": get(operationId="Search_", tags=["Search"])}}
        )
    ).encode()

    def test_an_exact_candidate_without_info_license_reads_its_licence_file_only_when_fetching_is_allowed(self) -> None:
        rows = [self.entry("bare", self.EXACT, [KEY_T])]
        refused, _output = self.screen(rows, "--no-discover")
        self.assertEqual(1, refused.returncode)
        self.assertIn("LICENSE at acme/bare@" + COMMIT + " is not cached", refused.stderr)
        self.assertIn("--fetch-licence", refused.stderr)
        self.assertEqual([], self.server.requests, "a cache-only screen made a live request")
        self.server.files[f"/acme/bare/{COMMIT}/COPYING"] = b"Apache License\nVersion 2.0, January 2004\n"
        done, output = self.screen(rows, "--no-discover", "--fetch-licence")
        self.assertEqual(0, done.returncode, done.stderr)
        [row] = SCREEN.read_screen(output)
        self.assertEqual(
            (f"admissible:Apache-2.0 (COPYING at {COMMIT})", "certified-screen-pending"), (row.licence, row.status)
        )
        tried = [path.rsplit("/", 1)[1] for path in self.server.requests]
        self.assertEqual(list(SCREEN.witness_screen().LICENCE_FILES[: tried.index("COPYING") + 1]), tried)

    def test_a_document_licence_decides_and_no_licence_path_is_fetched(self) -> None:
        commercial = json.loads(self.EXACT)
        commercial["info"]["license"] = {"name": "Commercial"}
        partial = json.loads(self.EXACT)
        partial["paths"]["/search"]["get"]["operationId"] = "Search_list"
        rows = [
            self.entry("commercial", json.dumps(commercial).encode(), [KEY_T]),
            self.entry("partial", json.dumps(partial).encode(), [KEY_T]),
            self.entry("archived", self.EXACT, [KEY_T], evidence="no-publisher-grant"),
            self.entry(
                "registered-grant",
                self.EXACT,
                [KEY_T],
                evidence="corpus:MIT (repository LICENSE at the pinned revision)",
            ),
        ]
        done, output = self.screen(rows, "--no-discover", "--fetch-licence")
        self.assertEqual(0, done.returncode, done.stderr)
        got = {row.document.split("/")[1]: (row.licence, row.status) for row in SCREEN.read_screen(output)}
        self.assertEqual(
            {
                "commercial": (
                    "inadmissible:info.license 'Commercial' names no grant the corpus rule admits",
                    "rejected-licence",
                ),
                "partial": (
                    "unread:no info.license, and its repository licence file is read only for an exact trigger",
                    "rejected-trigger",
                ),
                "archived": (
                    "inadmissible:grants nothing: no info.license, and an APIs.guru archive copy carries no publisher grant",
                    "rejected-licence",
                ),
                "registered-grant": (
                    "admissible:MIT (the corpus row's recorded grant: MIT (repository LICENSE at the pinned revision))",
                    "certified-screen-pending",
                ),
            },
            got,
        )
        self.assertEqual([], self.server.requests)

    def test_bytes_never_had_or_that_do_not_parse_are_unfetchable_rows(self) -> None:
        rows = [
            self.entry("gone", b"", [KEY_T, KEY_B], unfetchable="HTTP 404 at the recorded commit"),
            self.entry("garbled", b'{"openapi": "3.0.3", "paths": {', [KEY_T]),
        ]
        done, output = self.screen(rows, "--no-discover")
        self.assertEqual(0, done.returncode, done.stderr)
        got = sorted(
            (row.document.split("/")[1], row.key, row.sha256, row.status) for row in SCREEN.read_screen(output)
        )
        garbled = hashlib.sha256(b'{"openapi": "3.0.3", "paths": {').hexdigest()
        self.assertEqual(
            [
                ("garbled", KEY_T, garbled, "unfetchable:the exact bytes do not parse (DocumentError)"),
                ("gone", KEY_B, "-", "unfetchable:HTTP 404 at the recorded commit"),
                ("gone", KEY_T, "-", "unfetchable:HTTP 404 at the recorded commit"),
            ],
            got,
        )

    def test_a_manifest_naming_bytes_the_store_lacks_is_refused_with_its_remedy(self) -> None:
        row = self.entry("lost", self.EXACT, [KEY_T])
        (self.store / row[3]).unlink()
        done, output = self.screen([row], "--no-discover")
        self.assertEqual(1, done.returncode)
        self.assertIn(f"no bytes carrying sha256 {row[3]} are in the store; acquire them first", done.stderr)
        self.assertFalse(output.exists())


GOOD = (
    "combo-tag-only-operation-id",
    "github",
    "acme/shop/openapi.json",
    f"https://raw.githubusercontent.com/acme/shop/{COMMIT}/openapi.json",
    "b" * 64,
    "admissible:MIT (info.license 'MIT')",
    "exact",
    "certified-screen-pending",
)


class ReaderTests(ScreenHarness):
    def table(self, *rows: tuple[str, ...], header: tuple[str, ...] = SCREEN.COLUMNS) -> Path:
        path = self.scratch / "table.tsv"
        path.write_text("\t".join(header) + "\n" + "".join("\t".join(row) + "\n" for row in rows), encoding="utf-8")
        return path

    def test_a_whole_table_is_read_and_counted(self) -> None:
        registered = (
            "combo-tag-only-operation-id",
            "registered",
            "bbci.co.uk",
            "-",
            "c" * 64,
            "admissible:MIT (info.license 'MIT')",
            "partial:operation-id-not-its-first-tag-and-underscores",
            "rejected-trigger",
        )
        unfetchable = (
            KEY_B,
            "handed-off",
            "acme/gone:openapi.yaml@" + COMMIT,
            GOOD[3],
            "-",
            "unread:HTTP 404",
            "unread:HTTP 404",
            "unfetchable:HTTP 404",
        )
        done = self.run_cli("check", str(self.table(GOOD, registered, unfetchable)))
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            "population-screen: 3 rows; certified-screen-pending 1, rejected-trigger 1, unfetchable 1\n", done.stdout
        )
        self.assertEqual(
            {"combo-tag-only-operation-id": 1}, dict(SCREEN.pending_counts(SCREEN.read_screen(self.table(GOOD))))
        )

    def test_each_malformed_or_duplicate_row_is_refused_naming_what_is_wrong(self) -> None:
        def changed(**cells: str) -> tuple[str, ...]:
            return tuple(cells.get(column, value) for column, value in zip(SCREEN.COLUMNS, GOOD, strict=True))

        for rows, message in (
            ((GOOD, GOOD), "duplicates line 2's"),
            ((changed(key="combo-nope"),), "key 'combo-nope' is none of the 22 combination keys"),
            ((changed(population="gitlab"),), "population 'gitlab' is none of"),
            ((changed(document="TODO"),), "document is empty, a placeholder or padded"),
            (
                (changed(source="https://raw.githubusercontent.com/acme/shop/main/openapi.json"),),
                "no https URL pinned at a full commit",
            ),
            ((changed(population="registered", document="shop"),), "a registered document's source is `-`"),
            ((changed(sha256="-"),), "is no SHA-256"),
            ((changed(licence="admissible:"),), "licence 'admissible:' is none of"),
            ((changed(licence="admissible:TODO"),), "licence 'admissible:TODO' is none of"),
            ((changed(trigger="partial:anything"),), "names no condition of combo-tag-only-operation-id's screen"),
            (
                (changed(status="rejected-licence"),),
                "disagrees with its licence and trigger, which give 'certified-screen-pending'",
            ),
            ((changed(licence="inadmissible:Commercial"),), "which give 'rejected-licence'"),
            (
                (changed(licence="unread:not read"),),
                "an exact trigger whose licence 'unread:not read' was never decided",
            ),
            ((changed(trigger="unread:gone"),), "a trigger left unread beside a licence that was read"),
            ((changed(licence="unread:a", trigger="unread:b", status="unfetchable:b"),), "name the same reason"),
            ((changed(trigger="maybe"),), "trigger 'maybe' is none of"),
            ((GOOD[:7],), "7 cells, not the 8 columns"),
            ((changed(document="acme/shop/x\t"),), "cells, not the 8 columns"),
        ):
            with self.subTest(message=message):
                path = self.table(*rows)
                with self.assertRaisesRegex(
                    SCREEN.ScreenError, message.replace("(", r"\(").replace(")", r"\)").replace("`", ".")
                ):
                    SCREEN.read_screen(path)
                done = self.run_cli("check", str(path))
                self.assertEqual(1, done.returncode)
                self.assertIn(f"{path}:", done.stderr)
        for header in (
            (*SCREEN.COLUMNS[:-1],),
            ("key", "population", "document", "sha256", "source", "licence", "trigger", "status"),
        ):
            with self.subTest(header=header), self.assertRaisesRegex(SCREEN.ScreenError, "its header is not"):
                SCREEN.read_screen(self.table(GOOD, header=header))


class AcquisitionTests(ScreenHarness):
    def identities(self, rows: list[tuple[str, ...]]) -> Path:
        path = self.scratch / "identities.tsv"
        path.write_text(
            "\t".join(SCREEN.IDENTITY_COLUMNS) + "\n" + "".join("\t".join(row) + "\n" for row in rows), encoding="utf-8"
        )
        return path

    def test_exact_bytes_come_from_the_store_the_shared_cache_or_the_guarded_raw_lane_and_a_mismatch_is_refused(
        self,
    ) -> None:
        kept, served, blob, wrong = (
            b"openapi: 3.0.3\n# kept\n",
            b"openapi: 3.0.3\n# served\n",
            b"openapi: 3.0.3\n# blob\n",
            b"x",
        )
        SCREEN.store(kept, self.store)
        self.server.files[f"/acme/served/{COMMIT}/openapi.yaml"] = served
        self.server.files[f"/acme/blob/{COMMIT}/openapi.yaml"] = blob
        self.server.files[f"/acme/wrong/{COMMIT}/openapi.yaml"] = wrong
        responses = self.scratch / "xdg" / "crozier" / "github-responses" / "ab"
        responses.mkdir(parents=True)
        shared = b"openapi: 3.0.3\n# shared\n"
        (responses / f"{'ab' * 32}.{hashlib.sha256(shared).hexdigest()}.body").write_bytes(shared)

        def row(name: str, data: bytes, rank: str, pin: str | None = None) -> tuple[str, ...]:
            return (
                "github",
                f"acme/{name}/openapi.yaml",
                f"acme/{name}",
                COMMIT,
                "openapi.yaml",
                pin or hashlib.sha256(data).hexdigest(),
                "",
                rank,
            )

        plan = self.identities(
            [
                row("kept", kept, "1"),
                row("served", served, "9"),
                row("blob", blob, "8", f"blob:{SCREEN.blob_sha(blob)}"),
                row("wrong", b"openapi: 3.0.3\n# pinned\n", "7"),
                row("missing", b"m", "6"),
                row("shared", shared, "0"),
            ]
        )
        evidence = self.scratch / "evidence"
        done = self.run_cli(
            "acquire",
            "--identities",
            str(plan),
            "--evidence",
            str(evidence),
            "--store",
            str(self.store),
            "--responses",
            str(responses.parent),
        )
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            "population-screen: acquire: digest-differs 1, raw 2, refused-http-404 1, shared-cache 1, store 1\n",
            done.stdout,
        )
        for data in (kept, served, blob, shared):
            self.assertEqual(data, SCREEN.cached(hashlib.sha256(data).hexdigest(), self.store))
        self.assertIsNone(SCREEN.cached(hashlib.sha256(wrong).hexdigest(), self.store))
        ledger = [
            json.loads(line) for line in (evidence / "acquisitions.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual(
            ["served", "blob", "wrong", "missing", "kept", "shared"], [r["document"].split("/")[1] for r in ledger]
        )
        calls = [
            json.loads(line) for line in (evidence / "raw-github-calls.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual(["served", "blob", "wrong", "missing"], [call["url"].split("/")[4] for call in calls])
        # A spent budget fetches nothing more and says how many it left.
        self.server.requests.clear()
        later = self.identities([row("later", b"later", "1")])
        done = self.run_cli(
            "acquire",
            "--identities",
            str(later),
            "--evidence",
            str(evidence),
            "--store",
            str(self.store),
            "--budget-seconds",
            "0",
            "--responses",
            str(responses.parent),
        )
        self.assertEqual(("population-screen: acquire: budget-spent 1\n", []), (done.stdout, self.server.requests))


class JourneyTests(ScreenHarness):
    def test_an_authored_population_screens_to_a_table_the_reader_accepts_and_its_exact_bytes_are_kept(self) -> None:
        exact = json.dumps(CASES[0][1]).encode()
        rejected = json.dumps(next(body for name, body, _e in CASES if name == "pointer-resolves")).encode()
        rows = [
            self.entry("exact", exact, []),
            self.entry("near", rejected, []),
            self.entry("gone", b"", [KEY_T], unfetchable="HTTP 404 at the recorded commit"),
        ]
        done, output = self.screen(rows)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertRegex(done.stdout, r"^population-screen: wrote \d+ rows, 6 pending\n$")
        check = self.run_cli("check", str(output))
        self.assertEqual(0, check.returncode, check.stderr)
        rows_read = SCREEN.read_screen(output)
        pending = [row for row in rows_read if row.status == "certified-screen-pending"]
        self.assertEqual(set(POINTER_KEYS), {row.key for row in pending})
        self.assertEqual({hashlib.sha256(exact).hexdigest()}, {row.sha256 for row in pending})
        # Only the exact candidate's bytes are kept in the host cache, retrieved by their digest.
        (self.store / hashlib.sha256(rejected).hexdigest()).unlink()
        kept = self.run_cli("cached", pending[0].sha256, "--store", str(self.store))
        self.assertEqual(0, kept.returncode, kept.stderr)
        self.assertEqual(exact, Path(kept.stdout.strip()).read_bytes())
        lost = self.run_cli("cached", hashlib.sha256(rejected).hexdigest(), "--store", str(self.store))
        self.assertEqual(1, lost.returncode)
        self.assertIn("re-fetch them from the row's source", lost.stderr)
        # The host cache defaults to ${XDG_CACHE_HOME}/crozier/witness-populations.
        SCREEN.store(exact, Path(self.env["XDG_CACHE_HOME"]) / "crozier" / "witness-populations")
        default = self.run_cli("cached", pending[0].sha256)
        self.assertEqual(0, default.returncode, default.stderr)


class CommittedTableTests(unittest.TestCase):
    rows: ClassVar[list[Any]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = SCREEN.read_screen(SCREEN.TABLE)

    def test_the_committed_table_reads_whole_through_the_reader(self) -> None:
        self.assertTrue(self.rows)
        self.assertEqual(
            set(SCREEN.KEYS) - {row.key for row in self.rows}, set(SCREEN.KEYS) - {row.key for row in self.rows}
        )

    def test_every_candidate_the_earlier_named_census_lists_has_a_row(self) -> None:
        build = load("witness_populations_build_under_test", REPO / "tools/witness-search/witness-populations-build.py")
        have = {(row.key, row.population, row.document) for row in self.rows}
        for (population, document), keys in build.earlier_rows().items():
            for key in keys:
                with self.subTest(key=key, population=population, document=document):
                    self.assertIn((key, population, document), have)

    def test_every_row_names_a_manifest_candidate_with_its_digest(self) -> None:
        entries = {(e.population, e.document): e for e in SCREEN.read_manifest(SCREEN.POPULATION)}
        for row in self.rows:
            with self.subTest(row=row[:3]):
                entry = entries[(row.population, row.document)]
                self.assertEqual((entry.source, entry.sha256), (row.source, row.sha256))

    def test_the_registered_rows_are_reproduced_from_the_bytes_in_the_tree(self) -> None:
        registered = [row for row in self.rows if row.population == "registered"]
        entries = {e.document: e for e in SCREEN.read_manifest(SCREEN.POPULATION) if e.population == "registered"}
        keys: dict[str, list[str]] = {}
        for row in registered:
            keys.setdefault(row.document, []).append(row.key)
        manifest = [entries[name]._replace(keys=";".join(sorted(found))) for name, found in sorted(keys.items())]
        with tempfile.TemporaryDirectory(prefix="population-screen-") as scratch:
            again = SCREEN.run_screen(
                manifest,
                store_root=Path(scratch),
                fetch_file=lambda *_args: None,
                discover=False,
                # In this process: a pool's workers cannot import the module this test loaded by path.
                workers=1,
            )
        self.assertEqual(sorted(registered), sorted(again))


if __name__ == "__main__":
    unittest.main()

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

import base64
import csv
import gzip
import hashlib
import importlib.util
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import unittest
import urllib.parse
from collections.abc import Sequence
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
GUARD = load("rate_limit_guard", REPO / "tools" / "witness-search" / "rate_limit_guard.py")


def cache_answer(root: Path, url: str, body: bytes) -> None:
    """Store `body` as the shared response cache's answer to `url`, through the guard's own writer."""
    saved = os.environ.get(GUARD.CACHE_DIR_ENV)
    os.environ[GUARD.CACHE_DIR_ENV] = str(root)
    try:
        assert GUARD.cache_store("GET", url, {"User-Agent": "crozier-witness-search"}, 200, None, body) is not None
    finally:
        if saved is None:
            os.environ.pop(GUARD.CACHE_DIR_ENV)
        else:
            os.environ[GUARD.CACHE_DIR_ENV] = saved


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
BUILD_OPAQUE = "screened-nonpublic-input:v2:" + "d" * 32 + ":1"
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


def header(
    schema: dict,
    *,
    name: str = "X-Mode",
    required: bool = False,
    second_operation: bool = False,
    api_key: str | None = None,
) -> dict:
    parameter = {"name": name, "in": "header", "schema": schema, **({"required": True} if required else {})}
    paths = {"/probe": {"get": get(operationId="probe", parameters=[parameter])}}
    if second_operation:
        paths["/other"] = {"get": get(operationId="other")}
    body = document(paths=paths)
    if api_key is not None:
        body["components"] = {"securitySchemes": {"key": {"type": "apiKey", "in": "header", "name": api_key}}}
    return body


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


# Two variants each inheriting the other through `allOf`: the requiredness walk stops at its depth bound.
CYCLIC = holder(
    {
        "A": {
            "type": "object",
            "allOf": [{"$ref": "#/components/schemas/B"}],
            "properties": {"kind": {"type": "string", "enum": ["a"]}},
        },
        "B": {
            "type": "object",
            "allOf": [{"$ref": "#/components/schemas/A"}],
            "properties": {"kind": {"type": "string", "enum": ["b"]}},
        },
        "Union": {"oneOf": [{"$ref": "#/components/schemas/A"}, {"$ref": "#/components/schemas/B"}]},
    },
    {"u": {"$ref": "#/components/schemas/Union"}},
)
CASES.append(("tag-cyclic-allof", CYCLIC, {"combo-unrequired-tag-oneof-reference": "exact"}))


MAP_ONEOF = {"oneOf": [{"type": "string"}, {"type": "integer"}], "additionalProperties": {"type": "string"}}
UNRESOLVED = {"$ref": "#/components/schemas/Named/properties/absent"}


def with_components(body: dict, **sections: Any) -> dict:
    body.setdefault("components", {}).update(sections)
    return body


# Triggers placed where only one walk reaches them (a referenced Path Item, a parameter an operation
# overrides, a component root, a reference chain, a reference cycle) or where none should (a webhook).
CASES += [
    (
        "webhook-operation",
        document(webhooks={"ping": {"post": get(operationId="Hooks_", tags=["Hooks"])}}),
        {"combo-tag-only-operation-id": "absent"},
    ),
    (
        "referenced-path-item",
        with_components(
            document(paths={"/repos/{name}": {"$ref": "#/components/pathItems/Repo"}}),
            pathItems={
                "Repo": collision({"type": "object", "properties": {"name": {"type": "string"}}})["paths"][
                    "/repos/{name}"
                ]
            },
        ),
        {"combo-body-property-named-as-path-param": "exact"},
    ),
    (
        "operation-overrides-path-item-parameter",
        document(
            paths={
                "/probe": {
                    "parameters": [{"name": "X-Mode", "in": "header", "schema": {"type": "string", "default": "all"}}],
                    "get": get(
                        operationId="probe",
                        parameters=[{"name": "X-Mode", "in": "header", "schema": {"type": "string"}}],
                    ),
                }
            }
        ),
        {"combo-header-string-default": "partial:schema-declares-no-default"},
    ),
    (
        "component-request-body",
        with_components(
            document(
                paths={
                    "/h": {
                        "post": {
                            "requestBody": {"$ref": "#/components/requestBodies/B"},
                            "responses": {"204": {"description": "ok"}},
                        }
                    }
                },
                schemas=NAMED,
            ),
            requestBodies={"B": {"content": {"application/json": {"schema": UNRESOLVED}}}},
        ),
        # The key's selector reads a request body the operation writes inline, not one it references.
        {"combo-request-unresolved-nested-pointer": "absent"},
    ),
    (
        "component-response",
        with_components(
            document(
                paths={"/h": {"get": {"responses": {"200": {"$ref": "#/components/responses/R"}}}}}, schemas=NAMED
            ),
            responses={"R": {"description": "ok", "content": {"application/json": {"schema": UNRESOLVED}}}},
        ),
        {"combo-response-unresolved-nested-pointer": "exact"},
    ),
    (
        "component-header-schema",
        with_components(document(), headers={"H": {"schema": MAP_ONEOF}}),
        {"combo-map-beside-oneof": "exact"},
    ),
    (
        "component-parameter-schema",
        with_components(document(), parameters={"P": {"name": "p", "in": "query", "schema": MAP_ONEOF}}),
        {"combo-map-beside-oneof": "exact"},
    ),
    (
        "component-response-header",
        with_components(document(), responses={"R": {"description": "ok", "headers": {"H": {"schema": MAP_ONEOF}}}}),
        {"combo-map-beside-oneof": "exact"},
    ),
    (
        "reference-chain",
        success(
            {"$ref": "#/components/schemas/A1"},
            schemas={**AB, "A1": {"$ref": "#/components/schemas/A2"}, "A2": {"anyOf": [A, NULL]}},
        ),
        {"combo-success-anyof-nullable": "exact"},
    ),
    # A callback's operations and an unreferenced component Path Item are no SDK surface: no trigger there.
    (
        "callback-operation",
        document(
            paths={
                "/subscribe": {
                    "post": get(
                        operationId="subscribe",
                        callbacks={
                            "event": {"{$request.body#/url}": {"post": get(operationId="Hooks_", tags=["Hooks"])}}
                        },
                    )
                }
            }
        ),
        {"combo-tag-only-operation-id": "absent"},
    ),
    (
        "unreferenced-path-item",
        with_components(document(), pathItems={"Hooks": {"get": get(operationId="Hooks_", tags=["Hooks"])}}),
        {"combo-tag-only-operation-id": "absent"},
    ),
    (
        "reference-cycle",
        success(
            {"$ref": "#/components/schemas/C1"},
            schemas={"C1": {"$ref": "#/components/schemas/C2"}, "C2": {"$ref": "#/components/schemas/C1"}},
        ),
        {"combo-success-anyof-nullable": "absent"},
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
        header({"type": "string", "default": "crozier"}, name="User-Agent"),
        {KEY_HD: "partial:header-is-client-managed"},
    ),
    (
        "header-reserved-authorization",
        header({"type": "string", "default": "Bearer x"}, name="authorization"),
        {KEY_HD: "partial:header-is-client-managed"},
    ),
    (
        "header-owned-by-api-key",
        header({"type": "string", "default": "k"}, name="X-Key", api_key="X-Key"),
        {KEY_HD: "partial:header-is-client-managed"},
    ),
    # A key scheme owns its header as spelled: another case is an ordinary header.
    (
        "header-beside-api-key",
        header({"type": "string", "default": "k"}, name="x-key", api_key="X-Key"),
        {KEY_HD: "exact"},
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
    # `properties` that is no mapping declares none, however non-empty it is.
    (
        "query-object-properties-list",
        query({"type": "object", "properties": ["x"]}),
        {KEY_O: "partial:schema-declares-no-properties"},
    ),
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
    # A path answered with this status instead of the file or a 404.
    statuses: dict[str, int]
    # Reset the first connection unanswered, as a transient network failure would.
    drop_first: bool = False


class _Raw(BaseHTTPRequestHandler):
    """raw.githubusercontent.com's exact-commit route, serving `server.files`."""

    server: _RawServer

    def log_message(self, format: str, *args: Any) -> None:
        pass

    def do_GET(self) -> None:
        self.server.requests.append(self.path)
        if self.server.drop_first and len(self.server.requests) == 1:
            # A connection the far end resets before answering: a transient network failure.
            self.close_connection = True
            return
        body = self.server.files.get(self.path)
        if self.path in self.server.statuses:
            self.send_response(self.server.statuses[self.path])
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
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
        server.files, server.requests, server.statuses = {}, [], {}
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
            "\t".join(SCREEN.MANIFEST_COLUMNS) + "\n" + "".join("\t".join(row) + "\n" for row in rows),
            encoding="utf-8",
            newline="\n",
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
            # An aggregation's grant is no publisher grant, whether the corpus recorded it or a copy sits in one.
            self.entry(
                "registered-aggregation",
                self.EXACT,
                [KEY_T],
                evidence="corpus:CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`)",
            ),
            self.entry("aggregated", self.EXACT, [KEY_T], evidence=f"aggregation:acme/aggregated@{COMMIT}"),
            self.entry(
                "malformed", self.EXACT.replace(b'"version": "1"}', b'"version": "1", "license": "MIT"}'), [KEY_T]
            ),
            # A row sourced from an aggregation stands on its grant unless the corpus recorded a publisher's.
            self.entry(
                "registered-copy",
                self.EXACT,
                [KEY_T],
                evidence="corpus-aggregation:CC0 (repository LICENSE at the pinned revision)",
            ),
            self.entry(
                "registered-copy-publisher",
                self.EXACT,
                [KEY_T],
                evidence="corpus-aggregation:Apache-2.0 (the publisher repository's pinned `LICENSE`)",
            ),
        ]
        self.server.files[f"/jentic/jentic-public-apis/{COMMIT}/LICENSE"] = b"CC0 1.0 Universal\n"
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
                "registered-aggregation": (
                    "inadmissible:grants nothing: no info.license, and the corpus row records only an aggregation's "
                    "grant, which is no publisher grant",
                    "rejected-licence",
                ),
                "registered-copy": (
                    "inadmissible:grants nothing: no info.license, and the corpus row records only an aggregation's "
                    "grant, which is no publisher grant",
                    "rejected-licence",
                ),
                "registered-copy-publisher": (
                    "admissible:Apache-2.0 (the corpus row's recorded grant: Apache-2.0 (the publisher repository's "
                    "pinned `LICENSE`))",
                    "certified-screen-pending",
                ),
                "malformed": ("inadmissible:info.license is there but is no License Object", "rejected-licence"),
                "aggregated": (
                    "inadmissible:grants nothing: no info.license, and acme/aggregated redistributes it as "
                    "an aggregation, whose grant is no publisher grant",
                    "rejected-licence",
                ),
            },
            got,
        )
        self.assertEqual([], self.server.requests)

    def test_a_cached_licence_file_decides_without_any_live_request(self) -> None:
        responses = self.scratch / "responses"
        self.env[GUARD.CACHE_DIR_ENV] = str(responses)
        cache_answer(responses, f"{self.env['CROZIER_RAW_GITHUB_URL']}/acme/kept/{COMMIT}/LICENSE", b"MIT License\n")
        done, output = self.screen([self.entry("kept", self.EXACT, [KEY_T])], "--no-discover")
        self.assertEqual(0, done.returncode, done.stderr)
        [row] = SCREEN.read_screen(output)
        self.assertEqual(
            (f"admissible:MIT (LICENSE at {COMMIT})", "certified-screen-pending"), (row.licence, row.status)
        )
        self.assertEqual([], self.server.requests)

    def test_a_licence_read_exhausting_every_filename_grants_nothing_and_another_failure_is_refused(self) -> None:
        rows = [
            self.entry("nothing", self.EXACT, [KEY_T]),
            self.entry("unrecorded", self.EXACT, [KEY_T], evidence="-"),
        ]
        done, output = self.screen(rows, "--no-discover", "--fetch-licence")
        self.assertEqual(0, done.returncode, done.stderr)
        got = {row.document.split("/")[1]: (row.licence, row.status) for row in SCREEN.read_screen(output)}
        self.assertEqual(
            {
                "nothing": (
                    "inadmissible:grants nothing: no info.license and no licence file at the pinned commit",
                    "rejected-licence",
                ),
                "unrecorded": (
                    "inadmissible:grants nothing: no info.license and no recorded repository to read a licence file at",
                    "rejected-licence",
                ),
            },
            got,
        )
        self.assertEqual(
            [f"/acme/nothing/{COMMIT}/{name}" for name in SCREEN.witness_screen().LICENCE_FILES], self.server.requests
        )
        self.server.statuses[f"/acme/broken/{COMMIT}/LICENSE"] = 500
        refused, _output = self.screen([self.entry("broken", self.EXACT, [KEY_T])], "--no-discover", "--fetch-licence")
        self.assertEqual(1, refused.returncode)
        self.assertIn(f"LICENSE at acme/broken@{COMMIT} answered HTTP 500", refused.stderr)

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

    def test_a_forced_candidate_that_is_no_openapi_3_document_is_never_screened_pending(self) -> None:
        # The exact trigger's paths and an MIT licence, under a Swagger 2.0 version: a census may force a key
        # onto any document it listed, and only an OpenAPI 3 document is screened for one.
        exact = {**json.loads(self.EXACT), "info": MIT}
        swagger = {"swagger": "2.0", **{name: value for name, value in exact.items() if name != "openapi"}}
        later = {**exact, "openapi": "4.0.0"}
        rows = [
            self.entry("swagger", json.dumps(swagger).encode(), [KEY_T]),
            self.entry("later", json.dumps(later).encode(), [KEY_T]),
            self.entry("exact", json.dumps(exact).encode(), [KEY_T]),
        ]
        done, output = self.screen(rows, "--no-discover")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(
            {
                "exact": "certified-screen-pending",
                "later": "unfetchable:the exact bytes are no OpenAPI 3 document (openapi '4.0.0')",
                "swagger": "unfetchable:the exact bytes are no OpenAPI 3 document (no `openapi` version)",
            },
            {row.document.split("/")[1]: row.status for row in SCREEN.read_screen(output)},
        )

    def test_a_manifest_naming_bytes_the_store_lacks_is_refused_with_its_remedy(self) -> None:
        row = self.entry("lost", self.EXACT, [KEY_T])
        (self.store / row[3]).unlink()
        done, output = self.screen([row], "--no-discover")
        self.assertEqual(1, done.returncode)
        self.assertIn(f"no bytes carrying sha256 {row[3]} are in the store; acquire them first", done.stderr)
        self.assertFalse(output.exists())


class ManifestTests(ScreenHarness):
    def test_a_malformed_or_duplicated_manifest_is_refused_before_any_screen(self) -> None:
        good = self.entry("good", json.dumps(CASES[0][1]).encode(), [KEY_T])
        for rows, header, message in (
            ([good], ("population", "document"), "its header is not"),
            ([[*good[:3], "x", *good[4:]]], None, "sha256 'x' is no SHA-256"),
            ([[*good[:4], "repository:../x@" + COMMIT, *good[5:]]], None, "evidence 'repository:../x@"),
            ([[*good[:5], "combo-nope", good[6]]], None, "keys ['combo-nope'] are no combination keys"),
            ([good, good], None, "duplicates line 2's candidate"),
            ([[*good[:4], f"repository:acme/other@{COMMIT}", *good[5:]]], None, "names another repository or commit"),
        ):
            with self.subTest(message=message):
                path = self.manifest(rows)
                if header is not None:
                    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
                    path.write_text("\t".join(header) + "\n" + "".join(lines[1:]), encoding="utf-8", newline="\n")
                output = self.scratch / "screen.tsv"
                done = self.run_cli(
                    "screen", "--manifest", str(path), "--output", str(output), "--store", str(self.store)
                )
                self.assertEqual(1, done.returncode)
                self.assertIn(message, done.stderr)
                self.assertFalse(output.exists())


class LicenceFetchTests(ScreenHarness):
    def test_a_transient_failure_is_retried_and_a_persistent_one_is_refused_naming_it(self) -> None:
        self.server.files[f"/acme/flaky/{COMMIT}/LICENSE"] = b"MIT License\n"
        self.server.drop_first = True
        saved = (
            SCREEN.LICENCE_FETCH_BACKOFF_S,
            os.environ.get("CROZIER_RAW_GITHUB_URL"),
            os.environ.get("XDG_CACHE_HOME"),
        )
        self.addCleanup(setattr, SCREEN, "LICENCE_FETCH_BACKOFF_S", saved[0])
        for name, value in (("CROZIER_RAW_GITHUB_URL", saved[1]), ("XDG_CACHE_HOME", saved[2])):
            self.addCleanup(lambda n=name, v=value: os.environ.pop(n, None) if v is None else os.environ.update({n: v}))
        SCREEN.LICENCE_FETCH_BACKOFF_S = 0.0
        os.environ["CROZIER_RAW_GITHUB_URL"] = self.env["CROZIER_RAW_GITHUB_URL"]
        os.environ["XDG_CACHE_HOME"] = self.env["XDG_CACHE_HOME"]
        fetch = SCREEN.raw_licence_fetcher(self.scratch / "evidence", live=True)
        self.assertEqual((200, b"MIT License\n"), fetch("acme/flaky", COMMIT, "LICENSE"))
        self.assertEqual([f"/acme/flaky/{COMMIT}/LICENSE"] * 2, self.server.requests)
        # Nothing listens at a closed port: every attempt fails, and the screen is refused, naming why.
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            closed = probe.getsockname()[1]
        os.environ["CROZIER_RAW_GITHUB_URL"] = f"http://127.0.0.1:{closed}"
        fetch = SCREEN.raw_licence_fetcher(self.scratch / "evidence-closed", live=True)
        with self.assertRaisesRegex(
            SCREEN.ScreenError, r"LICENSE at acme/gone@a{40} could not be read after 4 attempts"
        ):
            fetch("acme/gone", COMMIT, "LICENSE")


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
        path.write_text(
            "\t".join(header) + "\n" + "".join("\t".join(row) + "\n" for row in rows), encoding="utf-8", newline="\n"
        )
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
            f"https://raw.githubusercontent.com/acme/gone/{COMMIT}/openapi.yaml",
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
                "no raw.githubusercontent.com URL pinned at a full commit",
            ),
            (
                (changed(source=f"https://raw.githubusercontent.com/acme/shop/main/{COMMIT}/openapi.json"),),
                "no raw.githubusercontent.com URL pinned at a full commit",
            ),
            (
                (changed(source=f"https://example.com/acme/shop/{COMMIT}/openapi.json"),),
                "no raw.githubusercontent.com URL pinned at a full commit",
            ),
            ((changed(document="acme/shop/other.json"),), "is not the 'acme/shop/openapi.json' its source pins"),
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
        lost = (
            KEY_B,
            "github",
            f"sha256:{'a' * 64}",
            f"sha256:{'a' * 64}",
            "a" * 64,
            "unread:only its digest was recorded",
            "unread:only its digest was recorded",
            "unfetchable:only its digest was recorded",
        )
        self.assertEqual([lost], [tuple(row) for row in SCREEN.read_screen(self.table(lost))])
        for row, message in (
            ((*lost[:4], "b" * 64, *lost[5:]), "names another digest than sha256"),
            ((*lost[:3], f"sha256:{'b' * 64}", *lost[4:]), "name different digests"),
            ((lost[0], "registered", *lost[2:]), "is no corpus row name"),
            (
                (*lost[:5], "admissible:MIT (info.license 'MIT')", "exact", "certified-screen-pending"),
                "only an unfetchable row may carry it",
            ),
        ):
            with self.subTest(message=message), self.assertRaisesRegex(SCREEN.ScreenError, message):
                SCREEN.read_screen(self.table(row))
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
            "\t".join(SCREEN.IDENTITY_COLUMNS) + "\n" + "".join("\t".join(row) + "\n" for row in rows),
            encoding="utf-8",
            newline="\n",
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
        responses = self.scratch / "xdg" / "crozier" / "github-responses"
        shared = b"openapi: 3.0.3\n# shared\n"
        cache_answer(responses, f"https://raw.githubusercontent.com/acme/shared/{COMMIT}/openapi.yaml", shared)

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
            str(responses),
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
            str(responses),
        )
        self.assertEqual(("population-screen: acquire: budget-spent 1\n", []), (done.stdout, self.server.requests))


class AcquisitionRecoveryTests(ScreenHarness):
    def test_a_contents_answer_in_the_shared_cache_is_decoded_and_a_network_failure_is_ledgered(self) -> None:
        document = b"openapi: 3.0.3\n# encoded\n"
        responses = self.scratch / "responses"
        contents = json.dumps({"encoding": "base64", "content": base64.b64encode(document).decode()}).encode()
        cache_answer(
            responses, f"https://api.github.com/repos/acme/encoded/contents/openapi.yaml?ref={COMMIT}", contents
        )
        broken = json.dumps({"encoding": "base64", "content": "@@not base64@@"}).encode()
        cache_answer(responses, f"https://api.github.com/repos/acme/broken/contents/openapi.yaml?ref={COMMIT}", broken)
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            closed = probe.getsockname()[1]
        plan = self.scratch / "plan.tsv"
        plan.write_text(
            "\t".join(SCREEN.IDENTITY_COLUMNS)
            + "\n"
            + "\t".join(
                (
                    "github",
                    "acme/encoded/openapi.yaml",
                    "acme/encoded",
                    COMMIT,
                    "openapi.yaml",
                    hashlib.sha256(document).hexdigest(),
                    "",
                    "2",
                )
            )
            + "\n"
            + "\t".join(
                (
                    "github",
                    "acme/offline/openapi.yaml",
                    "acme/offline",
                    COMMIT,
                    "openapi.yaml",
                    hashlib.sha256(b"never served").hexdigest(),
                    "",
                    "1",
                )
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        evidence = self.scratch / "evidence"
        self.env["CROZIER_RAW_GITHUB_URL"] = f"http://127.0.0.1:{closed}"
        done = self.run_cli(
            "acquire",
            "--identities",
            str(plan),
            "--evidence",
            str(evidence),
            "--store",
            str(self.store),
            "--responses",
            str(responses),
        )
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual("population-screen: acquire: refused-http-0 1, shared-cache 1\n", done.stdout)
        self.assertEqual(document, SCREEN.cached(hashlib.sha256(document).hexdigest(), self.store))
        ledger = [
            json.loads(line) for line in (evidence / "acquisitions.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual(
            [("acme/encoded/openapi.yaml", "shared-cache"), ("acme/offline/openapi.yaml", "refused-http-0")],
            [(row["document"], row["how"]) for row in ledger],
        )

    def test_kept_bytes_that_no_longer_carry_their_digest_are_refused_and_fetched_again(self) -> None:
        document = b"openapi: 3.0.3\n# kept\n"
        digest = hashlib.sha256(document).hexdigest()
        self.store.mkdir(parents=True)
        (self.store / digest).write_bytes(b"openapi: 3.0.3\n# corrupted\n")
        lost = self.run_cli("cached", digest, "--store", str(self.store))
        self.assertEqual(1, lost.returncode)
        self.assertIn("re-fetch them from the row's source", lost.stderr)
        self.server.files[f"/acme/kept/{COMMIT}/openapi.yaml"] = document
        plan = self.scratch / "plan.tsv"
        identity = ("github", "acme/kept/openapi.yaml", "acme/kept", COMMIT, "openapi.yaml", digest, "", "1")
        plan.write_text(
            "\t".join(SCREEN.IDENTITY_COLUMNS) + "\n" + "\t".join(identity) + "\n", encoding="utf-8", newline="\n"
        )
        done = self.run_cli(
            "acquire",
            "--identities",
            str(plan),
            "--evidence",
            str(self.scratch / "evidence"),
            "--store",
            str(self.store),
            "--responses",
            str(self.scratch / "no-responses"),
        )
        self.assertEqual((0, "population-screen: acquire: raw 1\n"), (done.returncode, done.stdout), done.stderr)
        self.assertEqual(document, (self.store / digest).read_bytes())
        self.assertEqual(0, self.run_cli("cached", digest, "--store", str(self.store)).returncode)

    def test_a_plan_or_budget_the_lane_cannot_take_is_refused_before_any_request(self) -> None:
        plan = self.scratch / "plan.tsv"
        header = "\t".join(SCREEN.IDENTITY_COLUMNS) + "\n"
        for row, message in (
            (("gitlab", "a/b/c", "a/b", COMMIT, "c", "0" * 64, "", "1"), "is none of github, sourcegraph, handed-off"),
            (("github", "a/../c", "a/..", COMMIT, "c", "0" * 64, "", "1"), "is no acquired population's"),
            (("github", "a/b/c", "a/b", COMMIT, "../c", "0" * 64, "", "1"), "is no path inside a repository"),
            (("github", "a/b/c", "a/b", "main", "c", "0" * 64, "", "1"), "no full commit, or no SHA-256, blob or"),
            # A commit pin names the identity's own commit, never another.
            (
                ("github", "a/b/c", "a/b", COMMIT, "c", f"commit:{'b' * 40}", "", "1"),
                "no full commit, or no SHA-256, blob or own-commit pin",
            ),
        ):
            with self.subTest(message=message):
                plan.write_text(header + "\t".join(row) + "\n", encoding="utf-8", newline="\n")
                done = self.run_cli("acquire", "--identities", str(plan), "--evidence", str(self.scratch / "e"))
                self.assertEqual(1, done.returncode)
                self.assertIn(message, done.stderr)
                self.assertEqual([], self.server.requests)
        for budget in ("-1", "nan", "inf", "soon"):
            with self.subTest(budget=budget):
                done = self.run_cli(
                    "acquire",
                    "--identities",
                    str(plan),
                    "--evidence",
                    str(self.scratch / "e"),
                    "--budget-seconds",
                    budget,
                )
                self.assertEqual(2, done.returncode)
                self.assertIn("is no finite, non-negative number of seconds", done.stderr)
        done = self.run_cli("screen", "--manifest", str(plan), "--workers", "0")
        self.assertEqual((2, True), (done.returncode, "is no positive whole number" in done.stderr))


class ContractDriftTests(unittest.TestCase):
    def test_a_selector_file_the_census_cannot_read_is_refused(self) -> None:
        with tempfile.TemporaryDirectory(prefix="population-screen-") as scratch:
            path = Path(scratch) / "witness-search-keys.tsv"
            text = (REPO / "docs/openapi-surface/witness-search-keys.tsv").read_text(encoding="utf-8")
            path.write_text(
                text.replace("operation.operationId:tag-only&", "operation.operationId:no-such-predicate&", 1),
                encoding="utf-8",
                newline="\n",
            )
            with self.assertRaisesRegex(
                SCREEN.ScreenError, "combo-tag-only-operation-id's selector is none the census reads"
            ):
                SCREEN.Selectors.read(path)

    def test_each_site_judges_its_conditions_in_the_order_the_reader_declares(self) -> None:
        judged: dict[str, int] = dict.fromkeys(SCREEN.KEYS, 0)
        for name, body, _expected in CASES:
            for key, find in SCREEN.SITES.items():
                for site in find(body):
                    with self.subTest(case=name, key=key):
                        self.assertEqual(
                            SCREEN.CONDITIONS[key], tuple(condition for condition, _check in site.conditions)
                        )
                    judged[key] += 1
        self.assertEqual([], [key for key, count in judged.items() if not count])

    def test_an_exact_trigger_is_one_its_census_selector_declares(self) -> None:
        # The screen validates the condition the census selector states and more: it never reads a trigger
        # exact where the selector declares nothing, so a selector that moves fails here.
        selectors = SCREEN.Selectors.read()
        judged = 0
        for name, body, expected in CASES:
            declared = selectors.declarations(body)
            for key, verdict in expected.items():
                if verdict == "exact":
                    judged += 1
                    with self.subTest(case=name, key=key):
                        self.assertGreater(declared[key], 0)
        self.assertGreater(judged, len(SCREEN.KEYS))

    def test_the_header_policy_is_the_one_src_ir_rs_states(self) -> None:
        source = (REPO / "src" / "ir.rs").read_text(encoding="utf-8")

        def literals(function: str) -> set[str]:
            body = source.split(f"fn {function}(", 1)[1].split("\n}\n", 1)[0]
            return set(re.findall(r'"([A-Za-z-]+)"', body))

        managed = literals("is_transport_managed_header") | literals("is_transport_managed_parameter")
        self.assertEqual(managed, set(SCREEN.TRANSPORT_MANAGED_HEADERS))
        self.assertEqual(literals("is_promotion_reserved_header"), set(SCREEN.PROMOTION_RESERVED_HEADERS))


class FlowMappingTests(ScreenHarness):
    def test_a_yaml_flow_mapping_opening_like_json_is_read_as_the_yaml_it_is(self) -> None:
        body = (
            b"{openapi: 3.0.3, info: {title: t, version: '1', license: {name: MIT}}, paths: {/search: {get: "
            b"{operationId: Search_, tags: [Search], responses: {'200': {description: ok}}}}}}\n"
        )
        done, output = self.screen([self.entry("flow", body, [KEY_T])], "--no-discover")
        self.assertEqual(0, done.returncode, done.stderr)
        [row] = SCREEN.read_screen(output)
        self.assertEqual(("exact", "admissible:MIT (info.license 'MIT')"), (row.trigger, row.licence))


BUILD = load("witness_populations_build_under_test", REPO / "tools/witness-search/witness-populations-build.py")
RECORD_SCRIPT = REPO / "tools/witness-search/witness-populations-record.py"
BUILD_SCRIPT = REPO / "tools/witness-search/witness-populations-build.py"


class BuildHarness(ScreenHarness):
    """The builder over an authored repository tree: its ledgers, corpus, archive and handed-off record."""

    def setUp(self) -> None:
        super().setUp()
        self.root = self.scratch / "repo"
        surface = self.root / "docs" / "openapi-surface"
        surface.mkdir(parents=True)
        shutil.copy(REPO / "docs/openapi-surface/witness-search-keys.tsv", surface / "witness-search-keys.tsv")
        self.pointer = json.dumps(CASES[0][1]).encode()
        self.write(
            surface / "witness-search-github-code-search" / "candidates.jsonl",
            [
                {
                    "repository": "acme/pointers",
                    "path": "openapi.json",
                    "commit": "1" * 40,
                    "sha256": "e" * 64,
                    "key": "ref-pointer-unnamed-segment",
                    "selector": "schema.$ref:unnamed-segment",
                    "disposition": "declares",
                    "at": "2026-09-01T00:00:00+00:00",
                },
                {
                    "repository": "acme/pointers",
                    "path": "openapi.json",
                    "commit": "2" * 40,
                    "sha256": hashlib.sha256(self.pointer).hexdigest(),
                    "key": "oneof-anyof-variant",
                    "selector": "schema.oneOf>schema.anyOf",
                    "disposition": "does-not-declare",
                    "at": "2026-09-02T00:00:00+00:00",
                },
                {
                    "repository": "acme/swagger",
                    "path": "swagger.json",
                    "commit": "3" * 40,
                    "sha256": "f" * 64,
                    "key": "oneof-anyof-variant",
                    "selector": "schema.oneOf>schema.anyOf",
                    "disposition": "excluded-non-openapi-3",
                },
                {
                    "repository": "fern-api/fern",
                    "path": "openapi.json",
                    "commit": "4" * 40,
                    "sha256": "d" * 64,
                    "key": "oneof-anyof-variant",
                    "selector": "schema.oneOf>schema.anyOf",
                    "disposition": "declares",
                },
                {
                    "repository": "acme/hidden",
                    "path": BUILD_OPAQUE,
                    "commit": "5" * 40,
                    "sha256": "c" * 64,
                    "key": "oneof-anyof-variant",
                    "selector": "schema.oneOf>schema.anyOf",
                    "disposition": "declares",
                },
            ],
        )
        self.write(
            surface / "witness-search-sourcegraph" / "candidates.jsonl",
            [
                {
                    "repository": "github.com/jentic/jentic-public-apis",
                    "path": "apis/x/openapi.json",
                    "commit": "6" * 40,
                    "sha256": hashlib.sha256(self.pointer + b" ").hexdigest(),
                    "key": "oneof-anyof-variant",
                    "selector": "schema.oneOf>schema.anyOf",
                    "disposition": "does-not-declare",
                },
                {
                    "repository": "gitlab.com/acme/elsewhere",
                    "path": "openapi.json",
                    "commit": "7" * 40,
                    "sha256": "b" * 64,
                    "key": "oneof-anyof-variant",
                    "selector": "schema.oneOf>schema.anyOf",
                    "disposition": "declares",
                },
            ],
        )
        handed = self.root / "docs/fern-measurements/handed-off/documents.tsv"
        handed.parent.mkdir(parents=True)
        self.handed_bytes = json.dumps(CASES[2][1]).encode()
        handed.write_text(
            "document\tsha256\tsource\troot_causes\tstatus\tcorpus_row\tnote\n"
            f"acme/handed:openapi.json@{'8' * 40}\t{hashlib.sha256(self.handed_bytes).hexdigest()}\t-\t-\tdiffers\t-\t-\n"
            f"acme/lost:openapi.json@{'9' * 40}\t{'a' * 64}\t-\t-\tdiffers\t-\t-\n"
            f"(bytes only, no recorded provenance) —\t{'0' * 64}\t-\t-\trefused-by-ruling\t-\t-\n",
            encoding="utf-8",
            newline="\n",
        )
        fixtures = self.root / "tests" / "fixtures"
        (fixtures / "corpus-sources" / "sample-api").mkdir(parents=True)
        self.registered = json.dumps(CASES[1][1]).encode()
        (fixtures / "corpus-sources" / "sample-api" / "openapi.json").write_bytes(self.registered)
        (fixtures / "corpus-sources.tsv").write_text(
            "# header\nsample-api\ttests/fixtures/corpus-sources/sample-api/openapi.json\t"
            "https://raw.githubusercontent.com/acme/sample/" + "a" * 40 + "/openapi.json\t-\n",
            encoding="utf-8",
            newline="\n",
        )
        (fixtures / "CORPUS.md").write_text(
            "| # | name | method | source | pinned ref | license | decision | shapes |\n|---:|---|---|---|---|---|---|---|\n"
            "| 7 | `sample-api` | github-raw | https://raw.githubusercontent.com/acme/sample/"
            + "a" * 40
            + "/openapi.json | `aaaa` | MIT (repository LICENSE at the pinned revision) | committed | sample |\n",
            encoding="utf-8",
            newline="\n",
        )
        self.archive = self.scratch / "archive"
        archived = self.archive / "APIs" / "acme.local" / "1.0" / "openapi.json"
        archived.parent.mkdir(parents=True)
        archived.write_bytes(self.registered)
        manifest = surface / "witness-search-apis.guru" / "acquisition-manifest.tsv"
        manifest.parent.mkdir(parents=True)
        manifest.write_text(
            "walk\tdocument\trevision\tsha256\nAPIs-guru/openapi-directory\tAPIs/acme.local/1.0/openapi.json\t"
            f"{BUILD.ARCHIVE_REVISION}\t{hashlib.sha256(self.registered).hexdigest()}\n",
            encoding="utf-8",
            newline="\n",
        )
        census = surface / "witness-search-ledger-remainders" / "census.tsv"
        census.parent.mkdir(parents=True)
        census.write_text(
            "key\tsource\tdocument\tsha256\tdeclarations\tstatus\tneeds\n"
            f"combo-tag-only-operation-id\tregistered\tsample-api\t-\t1\tunscreened\t-\n"
            f"combo-map-beside-oneof\tapis-guru\tAPIs/acme.local/1.0/openapi.yaml\t-\t1\tunscreened\t-\n"
            f"combo-header-string-default\thanded-off\tacme/lost:openapi.json@{'9' * 40}\t-\t1\tunscreened\t-\n",
            encoding="utf-8",
            newline="\n",
        )
        for relative in BUILD.COMBINATION_CENSUSES:
            self.combination_census(relative, [])

    def combination_census(self, relative: str, rows: Sequence[tuple[str, ...]]) -> None:
        """One earlier combination search's census, in its own columns (the packed one in its own)."""
        path = self.root / "docs" / "openapi-surface" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == ".gz":
            header = ("key", "arm", "kind", "document", "sha256", "sites", "licence", "outcome")
            body = [
                (key, "-", "combination", document, digest, "-", "-", "outstanding") for key, document, digest in rows
            ]
            text = "\t".join(header) + "\n" + "".join("\t".join(row) + "\n" for row in body)
            path.write_bytes(gzip.compress(text.encode("utf-8")))
        else:
            header = ("key", "source", "document", "sites", "sha256", "screening")
            text = "\t".join(header) + "\n" + "".join("\t".join((*row[:3], "1", row[3], "-")) + "\n" for row in rows)
            path.write_text(text, encoding="utf-8", newline="\n")

    def write(self, path: Path, rows: list[dict[str, Any]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8", newline="\n")

    def build(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(BUILD_SCRIPT), "--root", str(self.root), *args],
            env=self.env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=REPO,
            timeout=600,
        )


class BuildTests(BuildHarness):
    def test_the_plan_is_each_public_openapi_identity_once_at_its_latest_commit_ranked(self) -> None:
        # A ledger line whose commit and digest are JSON numbers spelling 40 and 64 digits is no identity:
        # its fields are not the strings a pin is, however their decimal spelling reads.
        ledger = self.root / "docs/openapi-surface/witness-search-github-code-search/candidates.jsonl"
        with ledger.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(
                json.dumps(
                    {
                        "repository": "acme/numeric",
                        "path": "openapi.json",
                        "commit": int("1" * 40),
                        "sha256": int("2" * 64),
                        "key": "oneof-anyof-variant",
                        "selector": "schema.oneOf>schema.anyOf",
                        "disposition": "declares",
                    }
                )
                + "\n"
            )
        plan = self.scratch / "plan.tsv.gz"
        done = self.build("identities", "--output", str(plan))
        self.assertEqual((0, "witness-populations-build: 4 identities\n"), (done.returncode, done.stdout), done.stderr)
        rows = {row.document: row for row in SCREEN.read_identities(plan)}
        self.assertEqual(
            {
                "acme/pointers/openapi.json",
                "jentic/jentic-public-apis/apis/x/openapi.json",
                f"acme/handed:openapi.json@{'8' * 40}",
                f"acme/lost:openapi.json@{'9' * 40}",
            },
            set(rows),
        )
        pointer = rows["acme/pointers/openapi.json"]
        self.assertEqual(("2" * 40, hashlib.sha256(self.pointer).hexdigest()), (pointer.commit, pointer.pin))
        # A recorded pointer-shape declarer outranks a field-name match, and the handed-off documents lead.
        self.assertGreaterEqual(pointer.rank, 110)
        self.assertLess(rows["jentic/jentic-public-apis/apis/x/openapi.json"].rank, 100)
        self.assertEqual(1000, rows[f"acme/handed:openapi.json@{'8' * 40}"].rank)

    def test_the_manifest_names_every_population_with_its_evidence_and_refuses_bytes_the_record_does_not_hold(
        self,
    ) -> None:
        plan = self.scratch / "plan.tsv.gz"
        self.assertEqual(0, self.build("identities", "--output", str(plan)).returncode)
        SCREEN.store(self.pointer, self.store)
        SCREEN.store(self.handed_bytes, self.store)
        # A code-search hit is planned by its blob, and the acquisition ledger names the content it was had at.
        blobbed = json.dumps(CASES[3][1]).encode()
        SCREEN.store(blobbed, self.store)
        hits = self.scratch / "hits.tsv"
        blob = f"blob:{SCREEN.blob_sha(blobbed)}"
        hit = ("github", "acme/blobbed/openapi.json", "acme/blobbed", "b" * 40, "openapi.json", blob, "", "3")
        # A publisher-looking repository holding an archive document's exact bytes is a copy of the aggregation.
        mirror = (
            "github",
            "acme/mirror/openapi.json",
            "acme/mirror",
            "d" * 40,
            "openapi.json",
            hashlib.sha256(self.registered).hexdigest(),
            "",
            "1",
        )
        SCREEN.store(self.registered, self.store)
        hits.write_text(
            "\t".join(SCREEN.IDENTITY_COLUMNS) + "\n" + "\t".join(hit) + "\n" + "\t".join(mirror) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        ledger = self.scratch / "acquisitions.jsonl"
        self.write(
            ledger,
            [
                {
                    "population": "github",
                    "document": "acme/blobbed/openapi.json",
                    "how": "raw",
                    "commit": "b" * 40,
                    "sha256": blob,
                    "content_sha256": hashlib.sha256(blobbed).hexdigest(),
                }
            ],
        )
        output = self.scratch / "population.tsv"
        args = (
            "manifest",
            "--identities",
            str(plan),
            "--identities",
            str(hits),
            "--archive",
            str(self.archive),
            "--store",
            str(self.store),
            "--preflight",
            str(self.scratch / "none"),
            "--acquisitions",
            str(ledger),
            "--output",
            str(output),
        )
        done = self.build(*args)
        self.assertEqual(0, done.returncode, done.stderr)
        got = {(e.population, e.document): (e.evidence, e.keys, e.unfetchable) for e in SCREEN.read_manifest(output)}
        self.assertEqual(
            {
                ("registered", "sample-api"): (
                    "corpus:MIT (repository LICENSE at the pinned revision)",
                    "combo-tag-only-operation-id",
                    "-",
                ),
                ("apis-guru", "acme.local/1.0"): ("no-publisher-grant", "combo-map-beside-oneof", "-"),
                ("handed-off", f"acme/handed:openapi.json@{'8' * 40}"): (
                    f"repository:acme/handed@{'8' * 40}",
                    "-",
                    "-",
                ),
                ("handed-off", f"acme/lost:openapi.json@{'9' * 40}"): (
                    f"repository:acme/lost@{'9' * 40}",
                    "combo-header-string-default",
                    BUILD.HANDED_OFF_UNFETCHED,
                ),
                ("github", "acme/pointers/openapi.json"): (f"repository:acme/pointers@{'2' * 40}", "-", "-"),
                ("github", "acme/blobbed/openapi.json"): (f"repository:acme/blobbed@{'b' * 40}", "-", "-"),
                ("github", "acme/mirror/openapi.json"): (f"aggregation:acme/mirror@{'d' * 40}", "-", "-"),
            },
            got,
        )
        [blob_entry] = [e for e in SCREEN.read_manifest(output) if e.document == "acme/blobbed/openapi.json"]
        self.assertEqual(
            (
                hashlib.sha256(blobbed).hexdigest(),
                f"https://raw.githubusercontent.com/acme/blobbed/{'b' * 40}/openapi.json",
            ),
            (blob_entry.sha256, blob_entry.source),
        )
        # The archive copy is held to the digest the committed acquisition manifest records.
        (self.archive / "APIs" / "acme.local" / "1.0" / "openapi.json").write_bytes(b"{}")
        refused = self.build(*args)
        self.assertEqual(1, refused.returncode)
        self.assertIn("extract the pinned archive again", refused.stderr)
        (self.archive / "APIs" / "acme.local" / "1.0" / "openapi.json").write_bytes(self.registered)
        absent = self.build(*[str(self.scratch / "no-plan.tsv") if arg == str(hits) else arg for arg in args])
        self.assertEqual(1, absent.returncode)
        self.assertIn("is no file; pass the acquisition plans the manifest is built from", absent.stderr)

    def test_every_candidate_an_earlier_named_census_lists_is_acquired_and_owes_a_row(self) -> None:
        listed = json.dumps(CASES[3][1]).encode()
        undigested = json.dumps(CASES[0][1]).encode()
        handed = hashlib.sha256(self.handed_bytes).hexdigest()
        self.combination_census(
            "witness-search-operation-combinations-parameters/census.tsv",
            [
                (
                    KEY_HD,
                    "github-code-search",
                    f"acme/listed:openapi.json@{'a' * 40}",
                    hashlib.sha256(listed).hexdigest(),
                ),
                (KEY_M, "sourcegraph", f"github.com/acme/far:spec/openapi.yaml@{'b' * 40}", "1" * 64),
                (
                    KEY_O,
                    "registered",
                    "corpus-sources/sample-api/openapi.json",
                    hashlib.sha256(self.registered).hexdigest(),
                ),
                (KEY_O, "registered", "crozier-property-name/openapi.yml", "2" * 64),
                (KEY_HD, "apis.guru", "APIs/acme.local/1.0/openapi.json", hashlib.sha256(self.registered).hexdigest()),
            ],
        )
        # The earlier censuses name an archive document under the extracted tree's top directory, or as the
        # directory's own identity first of those sharing its bytes.
        archived = hashlib.sha256(self.registered).hexdigest()
        self.combination_census(
            "witness-search-interaction-operation-combinations/census.tsv",
            [
                (KEY_Q, "apis.guru", f"{BUILD.ARCHIVE_TREE}APIs/acme.local/1.0/openapi.json", archived),
                (KEY_N, "apis.guru", f"APIs/{BUILD.ARCHIVE_TREE}APIs/acme.local/1.0/openapi.json", archived),
                (
                    KEY_C,
                    "apis.guru",
                    f"{BUILD.ARCHIVE_REPOSITORY}:APIs/acme.local/1.0/openapi.json@{BUILD.ARCHIVE_REVISION}; "
                    f"acme/copy:APIs/acme.local/1.0/openapi.json@{'d' * 40}",
                    archived,
                ),
            ],
        )
        self.combination_census(
            "witness-search-operation-combinations/census.tsv.gz",
            [
                (KEY_SA, "(withheld)", handed),
                (KEY_SO, f"(withheld) [sha256:{'3' * 64}]", "3" * 64),
                (KEY_T, f"acme/undigested:openapi.json@{'c' * 40} (+1 identities, same bytes)", "-"),
                (KEY_T, f"screened-nonpublic-input:v2:{'4' * 32}:1", "-"),
            ],
        )
        census_plan = self.scratch / "census.tsv"
        done = self.build("census", "--output", str(census_plan))
        self.assertEqual(
            (0, "witness-populations-build: 3 census identities\n"), (done.returncode, done.stdout), done.stderr
        )
        self.assertEqual(
            {
                ("github", "acme/listed/openapi.json", hashlib.sha256(listed).hexdigest()),
                ("sourcegraph", "acme/far/spec/openapi.yaml", "1" * 64),
                ("github", "acme/undigested/openapi.json", f"commit:{'c' * 40}"),
            },
            {(i.population, i.document, i.pin) for i in SCREEN.read_identities(census_plan)},
        )
        # Through the real acquirer's raw lane: two documents served, the Sourcegraph one gone.
        self.server.files[f"/acme/listed/{'a' * 40}/openapi.json"] = listed
        self.server.files[f"/acme/undigested/{'c' * 40}/openapi.json"] = undigested
        evidence = self.scratch / "evidence"
        acquired = self.run_cli(
            "acquire",
            "--identities",
            str(census_plan),
            "--evidence",
            str(evidence),
            "--store",
            str(self.store),
            "--responses",
            str(self.scratch / "no-responses"),
        )
        self.assertEqual(0, acquired.returncode, acquired.stderr)
        self.assertEqual("population-screen: acquire: raw 2, refused-http-404 1\n", acquired.stdout)
        # A candidate the census lists that the bounded raw lane never reached: planned after the acquisition
        # ran, so it has no attempt, and still owes its row.
        self.combination_census(
            "witness-search-schema-combinations-models-unions-refs/census.tsv",
            [(KEY_SA, "github-code-search", f"acme/unreached:openapi.json@{'e' * 40}", "5" * 64)],
        )
        census_plan = self.scratch / "census-later.tsv"
        self.assertEqual(0, self.build("census", "--output", str(census_plan)).returncode)
        plan = self.scratch / "plan.tsv.gz"
        self.assertEqual(0, self.build("identities", "--output", str(plan)).returncode)
        SCREEN.store(self.handed_bytes, self.store)
        manifest = self.scratch / "population.tsv"
        built = self.build(
            "manifest",
            "--identities",
            str(plan),
            "--identities",
            str(census_plan),
            "--archive",
            str(self.archive),
            "--store",
            str(self.store),
            "--preflight",
            str(self.scratch / "none"),
            "--acquisitions",
            str(evidence / "acquisitions.jsonl"),
            "--search-evidence",
            str(self.scratch / "no-search"),
            "--output",
            str(manifest),
        )
        self.assertEqual(0, built.returncode, built.stderr)
        # Screened in this process, so a registered row reads its bytes from the authored tree.
        table = self.scratch / "screen.tsv"
        screened = SCREEN.run_screen(
            SCREEN.read_manifest(manifest),
            root=self.root,
            store_root=self.store,
            fetch_file=lambda *_args: None,
            discover=False,
        )
        table.write_text(SCREEN.render(screened), encoding="utf-8", newline="\n")
        rows = {(row.key, row.population, row.document): row for row in SCREEN.read_screen(table)}
        far = rows[(KEY_M, "sourcegraph", "acme/far/spec/openapi.yaml")]
        self.assertEqual(
            (
                "1" * 64,
                "unfetchable:fetched 1 time(s) at the recorded commit through the guarded raw lane, which gave HTTP 404",
            ),
            (far.sha256, far.status),
        )
        unreached = rows[(KEY_SA, "github", "acme/unreached/openapi.json")]
        self.assertEqual(
            (
                f"{BUILD.RAW}/acme/unreached/{'e' * 40}/openapi.json",
                "5" * 64,
                "unfetchable:listed by an earlier named census and never fetched: the guarded raw lane's budget "
                "was spent before it was reached",
            ),
            (unreached.source, unreached.sha256, unreached.status),
        )
        digest_only = rows[(KEY_SO, "github", f"sha256:{'3' * 64}")]
        self.assertEqual((f"sha256:{'3' * 64}", "3" * 64), (digest_only.source, digest_only.sha256))
        self.assertEqual(f"unfetchable:{BUILD.DIGEST_ONLY_SEARCHED}", digest_only.status)
        # The fetched ones are screened from their bytes, the commit-pinned one at the digest it was had at.
        for key, document, data in (
            (KEY_HD, "acme/listed/openapi.json", listed),
            (KEY_T, "acme/undigested/openapi.json", undigested),
        ):
            with self.subTest(document=document):
                row = rows[(key, "github", document)]
                self.assertEqual(hashlib.sha256(data).hexdigest(), row.sha256)
                self.assertFalse(row.status.startswith("unfetchable"), row)
        # A digest-only candidate takes the bytes held under its digest, whichever population holds them.
        self.assertEqual(handed, rows[(KEY_SA, "handed-off", f"acme/handed:openapi.json@{'8' * 40}")].sha256)
        self.assertIn((KEY_O, "registered", "sample-api"), rows)
        self.assertIn((KEY_HD, "apis-guru", "acme.local/1.0"), rows)
        for key in (KEY_Q, KEY_N, KEY_C):
            self.assertIn((key, "apis-guru", "acme.local/1.0"), rows)
        # Every candidate the censuses name owes its row; a hand-written fixture and a digestless
        # non-public input name nothing a row could carry.
        census = BUILD.named_census(BUILD.Tree(self.root))
        for (population, document), keys in census.listed.items():
            for key in keys:
                with self.subTest(key=key, population=population, document=document):
                    self.assertIn((key, population, document), rows)
        self.assertEqual({"crozier-property-name/openapi.yml (" + "2" * 64 + ")": {KEY_O}}, dict(census.authored))
        self.assertEqual([f"screened-nonpublic-input:v2:{'4' * 32}:1"], list(census.nonpublic))
        self.assertFalse([row for row in rows if "crozier-property-name" in row[2] or "nonpublic" in row[2]])

    def test_an_acquisition_record_outside_its_population_or_naming_held_bytes_by_a_pin_is_refused(self) -> None:
        plan = self.scratch / "plan.tsv.gz"
        self.assertEqual(0, self.build("identities", "--output", str(plan)).returncode)
        ledger = self.scratch / "acquisitions.jsonl"
        good = {
            "population": "github",
            "document": "acme/blobbed/openapi.json",
            "commit": "b" * 40,
            "pin": f"blob:{'c' * 40}",
            "how": "raw",
            "content_sha256": "d" * 64,
        }
        for record, accepted in (
            (good, True),
            # A refusal keeps the pin it asked for: no bytes were had to name.
            ({**good, "how": "refused-http-404", "content_sha256": good["pin"]}, True),
            ({**good, "population": "gitlab"}, False),
            ({**good, "content_sha256": good["pin"]}, False),
            ({**good, "how": "store", "content_sha256": f"commit:{'b' * 40}"}, False),
        ):
            with self.subTest(record=record):
                self.write(ledger, [record])
                done = self.build(
                    "manifest",
                    "--identities",
                    str(plan),
                    "--archive",
                    str(self.archive),
                    "--store",
                    str(self.store),
                    "--preflight",
                    str(self.scratch / "none"),
                    "--acquisitions",
                    str(ledger),
                    "--search-evidence",
                    str(self.scratch / "no-search"),
                    "--output",
                    str(self.scratch / "population.tsv"),
                )
                if accepted:
                    self.assertEqual(0, done.returncode, done.stderr)
                else:
                    self.assertEqual(1, done.returncode)
                    self.assertIn(f"{ledger}:1 is no acquisition record (an acquired population", done.stderr)

    def test_an_earlier_combination_census_in_a_form_the_builder_does_not_read_is_refused(self) -> None:
        for rows, message in (
            ([(KEY_T, "github-code-search", "acme/x/openapi.json", "1" * 64)], "is no form this builder reads"),
            ([(KEY_T, "github-code-search", f"acme/x:openapi.json@{'a' * 40}", "nope")], "names no SHA-256"),
        ):
            with self.subTest(message=message):
                self.combination_census("witness-search-interaction-schema-combinations/census.tsv", rows)
                refused = self.build("census", "--output", str(self.scratch / "census.tsv"))
                self.assertEqual(1, refused.returncode)
                self.assertIn(message, refused.stderr)
        (self.root / "docs/openapi-surface" / BUILD.COMBINATION_CENSUSES[0]).unlink()
        missing = self.build("census", "--output", str(self.scratch / "census.tsv"))
        self.assertEqual(1, missing.returncode)
        self.assertIn("restore the earlier combination search records from git", missing.stderr)

    def test_an_incomplete_archive_an_unmatched_earlier_candidate_or_malformed_provenance_is_refused(self) -> None:
        plan = self.scratch / "plan.tsv.gz"
        self.assertEqual(0, self.build("identities", "--output", str(plan)).returncode)
        args = (
            "manifest",
            "--identities",
            str(plan),
            "--archive",
            str(self.archive),
            "--store",
            str(self.store),
            "--preflight",
            str(self.scratch / "none"),
            "--output",
            str(self.scratch / "population.tsv"),
        )
        archived = self.archive / "APIs" / "acme.local" / "1.0" / "openapi.json"
        archived.unlink()
        incomplete = self.build(*args)
        self.assertEqual(1, incomplete.returncode)
        self.assertIn("lacks 1 of the 1 OpenAPI documents", incomplete.stderr)
        archived.write_bytes(self.registered)
        census = self.root / "docs/openapi-surface/witness-search-ledger-remainders/census.tsv"
        census.write_text(
            census.read_text(encoding="utf-8")
            + "combo-tag-only-operation-id\tregistered\tno-such-row\t-\t1\tunscreened\t-\n",
            encoding="utf-8",
            newline="\n",
        )
        unmatched = self.build(*args)
        self.assertEqual(1, unmatched.returncode)
        self.assertIn("the earlier named census lists candidates no population names", unmatched.stderr)
        handed = self.root / "docs/fern-measurements/handed-off/documents.tsv"
        handed.write_text(
            handed.read_text(encoding="utf-8") + f"acme/x:openapi.json@main\t{'1' * 64}\t-\t-\tdiffers\t-\t-\n",
            encoding="utf-8",
            newline="\n",
        )
        malformed = self.build("identities", "--output", str(plan))
        self.assertEqual(1, malformed.returncode)
        self.assertIn("'acme/x:openapi.json@main' is no repository:path@commit", malformed.stderr)
        handed.write_text(handed.read_text(encoding="utf-8").rsplit("\n", 2)[0] + "\n", encoding="utf-8", newline="\n")
        for path, line, message in (
            (handed, f"\t{'1' * 64}\t-\t-\tdiffers\t-\t-\n", "names no document and SHA-256 of its bytes"),
            (census, "combo-nope\tregistered\tsample-api\t-\t1\tunscreened\t-\n", "key 'combo-nope' is none of"),
            (
                census,
                "combo-tag-only-operation-id\tregistered\t\t-\t1\tunscreened\t-\n",
                "leaves its key, source or document empty",
            ),
            (self.root / "tests/fixtures/corpus-sources.tsv", "short-row\n", "names no row and source path"),
            (
                self.root / "docs/openapi-surface/witness-search-apis.guru/acquisition-manifest.tsv",
                f"APIs-guru/openapi-directory\tAPIs/acme.local/1.0/openapi.json\t{BUILD.ARCHIVE_REVISION}\t{'2' * 64}\n",
                "records APIs/acme.local/1.0/openapi.json a second time",
            ),
        ):
            with self.subTest(message=message):
                before = path.read_text(encoding="utf-8")
                path.write_text(before + line, encoding="utf-8", newline="\n")
                refused = self.build(*args)
                self.assertEqual(1, refused.returncode)
                self.assertIn(message, refused.stderr)
                self.assertNotIn("Traceback", refused.stderr)
                path.write_text(before, encoding="utf-8", newline="\n")
        # An acquisition manifest missing a column it is filtered on would silently record no archive document.
        archive_manifest = self.root / "docs/openapi-surface/witness-search-apis.guru/acquisition-manifest.tsv"
        before = archive_manifest.read_text(encoding="utf-8")
        archive_manifest.write_text(before.replace("walk\t", "walker\t", 1), encoding="utf-8", newline="\n")
        refused = self.build(*args)
        self.assertEqual(1, refused.returncode)
        self.assertIn("its header names no walk, document, revision and sha256 columns", refused.stderr)
        self.assertNotIn("Traceback", refused.stderr)
        archive_manifest.write_text(before, encoding="utf-8", newline="\n")

    def test_handed_off_bytes_are_recovered_from_the_tree_or_the_preflight_cache_into_an_empty_store(self) -> None:
        plan = self.scratch / "plan.tsv.gz"
        self.assertEqual(0, self.build("identities", "--output", str(plan)).returncode)
        # One handed-off document's bytes are committed as a corpus source, the other's are in a preflight run.
        handed = self.root / "docs/fern-measurements/handed-off/documents.tsv"
        lost = json.dumps(CASES[4][1]).encode()
        handed.write_text(
            handed.read_text(encoding="utf-8").replace("a" * 64, hashlib.sha256(lost).hexdigest()),
            encoding="utf-8",
            newline="\n",
        )
        committed = self.root / "tests/fixtures/corpus-sources/sample-api/handed.json"
        committed.write_bytes(self.handed_bytes)
        preflight = self.scratch / "preflight" / "run-1"
        preflight.mkdir(parents=True)
        (preflight / "source.json").write_bytes(lost)
        output = self.scratch / "population.tsv"
        done = self.build(
            "manifest",
            "--identities",
            str(plan),
            "--archive",
            str(self.archive),
            "--store",
            str(self.store),
            "--preflight",
            str(preflight.parent),
            "--output",
            str(output),
        )
        self.assertEqual(0, done.returncode, done.stderr)
        handed_off = {e.document: e for e in SCREEN.read_manifest(output) if e.population == "handed-off"}
        self.assertEqual(
            {f"acme/handed:openapi.json@{'8' * 40}": "-", f"acme/lost:openapi.json@{'9' * 40}": "-"},
            {document: entry.unfetchable for document, entry in handed_off.items()},
        )
        for data in (self.handed_bytes, lost):
            self.assertEqual(data, SCREEN.cached(hashlib.sha256(data).hexdigest(), self.store))

    def test_a_refused_download_and_an_unfetched_hit_stay_candidates_of_the_validated_table(self) -> None:
        plan = self.scratch / "plan.tsv.gz"
        self.assertEqual(0, self.build("identities", "--output", str(plan)).returncode)
        # The raw lane serves nothing: every planned download is refused with a 404.
        evidence = self.scratch / "acquisition"
        acquired = self.run_cli(
            "acquire",
            "--identities",
            str(plan),
            "--evidence",
            str(evidence),
            "--store",
            str(self.store),
            "--responses",
            str(self.scratch / "no-responses"),
        )
        self.assertEqual(0, acquired.returncode, acquired.stderr)
        self.assertIn("refused-http-404", acquired.stdout)
        # A code-search hit the search recorded for one key, never fetched.
        search = self.scratch / "search"
        self.write(
            search / "queries.jsonl",
            [
                {
                    "source": "github-code-search",
                    "key": "combo-property-defs-pointer",
                    "query": "q",
                    "outcome": "answered",
                    "results": [
                        {"repository": "acme/new", "path": "spec/openapi.yaml", "commit": "a" * 40, "sha": "b" * 40}
                    ],
                }
            ],
        )
        hits = self.scratch / "hits.tsv"
        replayed = self.build(
            "search", "--replay", "--evidence", str(search), "--identities", str(plan), "--output", str(hits)
        )
        self.assertEqual(0, replayed.returncode, replayed.stderr)
        manifest = self.scratch / "population.tsv"
        built = self.build(
            "manifest",
            "--identities",
            str(plan),
            "--identities",
            str(hits),
            "--archive",
            str(self.archive),
            "--store",
            str(self.store),
            "--preflight",
            str(self.scratch / "none"),
            "--acquisitions",
            str(evidence / "acquisitions.jsonl"),
            "--search-evidence",
            str(search),
            "--output",
            str(manifest),
        )
        self.assertEqual(0, built.returncode, built.stderr)
        # The acquired populations' part of the manifest: the screen reads a registered row's bytes in this repository.
        acquired_part = [entry for entry in SCREEN.read_manifest(manifest) if entry.population in SCREEN.ACQUIRED]
        SCREEN.write_manifest(manifest, acquired_part)
        table = self.scratch / "screen.tsv"
        screened = self.run_cli(
            "screen", "--manifest", str(manifest), "--output", str(table), "--store", str(self.store)
        )
        self.assertEqual(0, screened.returncode, screened.stderr)
        rows = {(row.population, row.document): row for row in SCREEN.read_screen(table)}
        refused = [row for (population, document), row in rows.items() if document == "acme/pointers/openapi.json"]
        self.assertTrue(refused, "the refused download left the table")
        for row in refused:
            self.assertEqual(hashlib.sha256(self.pointer).hexdigest(), row.sha256)
            self.assertTrue(row.status.startswith("unfetchable:fetched 1 time(s) at the recorded commit"), row.status)
            self.assertIn("HTTP 404", row.status)
            self.assertEqual((row.status.replace("unfetchable:", "unread:", 1),) * 2, (row.licence, row.trigger))
        keyed = {row.key for row in SCREEN.read_screen(table) if row.document == "acme/pointers/openapi.json"}
        self.assertEqual(set(BUILD.ledger_documents(BUILD.Tree(self.root))[0].keys), keyed)
        # A refused document whose recorded hits tie it to no key is a candidate of none.
        self.assertNotIn(("sourcegraph", "jentic/jentic-public-apis/apis/x/openapi.json"), rows)
        hit = rows[("github", "acme/new/spec/openapi.yaml")]
        self.assertEqual(("combo-property-defs-pointer", "-"), (hit.key, hit.sha256))
        self.assertIn("never fetched", hit.status)

    def test_bytes_the_ledger_had_at_another_commit_or_pin_are_not_attributed_to_the_plan(self) -> None:
        fetched = json.dumps(CASES[3][1]).encode()
        SCREEN.store(fetched, self.store)
        blob = f"blob:{SCREEN.blob_sha(fetched)}"
        hits = self.scratch / "hits.tsv"
        hit = ("github", "acme/moved/openapi.json", "acme/moved", "b" * 40, "openapi.json", blob, "", "3")
        hits.write_text(
            "\t".join(SCREEN.IDENTITY_COLUMNS) + "\n" + "\t".join(hit) + "\n", encoding="utf-8", newline="\n"
        )
        ledger = self.scratch / "acquisitions.jsonl"
        output = self.scratch / "population.tsv"
        args = (
            "manifest",
            "--identities",
            str(hits),
            "--archive",
            str(self.archive),
            "--store",
            str(self.store),
            "--preflight",
            str(self.scratch / "none"),
            "--acquisitions",
            str(ledger),
            "--output",
            str(output),
        )
        digest = hashlib.sha256(fetched).hexdigest()
        other = hashlib.sha256(self.registered).hexdigest()
        SCREEN.store(self.registered, self.store)
        for commit, pin, content in (
            ("c" * 40, blob, digest),
            ("b" * 40, "blob:" + "0" * 40, digest),
            ("b" * 40, blob, other),  # kept bytes that do not carry the planned blob
            ("b" * 40, blob, digest),
        ):
            with self.subTest(commit=commit, pin=pin, content=content):
                self.write(
                    ledger,
                    [
                        {
                            "population": "github",
                            "document": "acme/moved/openapi.json",
                            "commit": commit,
                            "sha256": pin,
                            "how": "raw",
                            "content_sha256": content,
                        }
                    ],
                )
                done = self.build(*args)
                self.assertEqual(0, done.returncode, done.stderr)
                attributed = (commit, pin, content) == ("b" * 40, blob, digest)
                documents = {e.document for e in SCREEN.read_manifest(output)}
                self.assertEqual(attributed, "acme/moved/openapi.json" in documents)

    def test_replay_plans_each_new_code_search_hit_by_its_blob_and_asks_nothing(self) -> None:
        plan = self.scratch / "plan.tsv.gz"
        self.assertEqual(0, self.build("identities", "--output", str(plan)).returncode)
        evidence = self.scratch / "search"
        self.write(
            evidence / "queries.jsonl",
            [
                {
                    "source": "github-code-search",
                    "key": "combo-property-defs-pointer",
                    "query": "q",
                    "outcome": "answered",
                    "results": [
                        {"repository": "acme/new", "path": "spec/openapi.yaml", "commit": "a" * 40, "sha": "b" * 40},
                        {"repository": "acme/pointers", "path": "openapi.json", "commit": "2" * 40, "sha": "c" * 40},
                        {"repository": "acme/mutable", "path": "openapi.yaml", "commit": "main", "sha": "d" * 40},
                    ],
                },
                {
                    "source": "sourcegraph",
                    "key": "combo-property-defs-pointer",
                    "query": "q",
                    "outcome": "answered",
                    "results": [],
                },
            ],
        )
        output = self.scratch / "hits.tsv"
        done = self.build(
            "search", "--replay", "--evidence", str(evidence), "--identities", str(plan), "--output", str(output)
        )
        self.assertEqual(0, done.returncode, done.stderr)
        [hit] = SCREEN.read_identities(output)
        self.assertEqual(("acme/new/spec/openapi.yaml", "blob:" + "b" * 40), (hit.document, hit.pin))
        self.assertGreaterEqual(hit.rank, 1)
        self.assertEqual([], self.server.requests)
        with gzip.open(evidence / "queries.jsonl.gz", "wt", encoding="utf-8") as handle:
            handle.write((evidence / "queries.jsonl").read_text(encoding="utf-8"))
        (evidence / "queries.jsonl").unlink()
        again = self.build(
            "search", "--replay", "--evidence", str(evidence), "--identities", str(plan), "--output", str(output)
        )
        self.assertEqual(0, again.returncode, again.stderr)
        self.assertEqual([hit], SCREEN.read_identities(output))
        live = self.build("search", "--evidence", str(evidence), "--identities", str(plan), "--output", str(output))
        self.assertEqual(2, live.returncode)
        self.assertIn("gunzip queries.jsonl.gz to resume it live", live.stderr)


class _ServiceServer(ThreadingHTTPServer):
    requests: list[str]
    # Answer code search with results naming no repository, and Sourcegraph with this status.
    malformed: bool = False
    sourcegraph_status: int = 200


class _Services(BaseHTTPRequestHandler):
    """GitHub's REST API (`/rate_limit`, `/search/code`) and Sourcegraph's stream search, on loopback."""

    server: _ServiceServer

    def log_message(self, format: str, *args: Any) -> None:
        pass

    def reply(self, body: bytes, kind: str, resource: str = "core") -> None:
        self.send_response(200)
        self.send_header("Content-Type", kind)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Ratelimit-Resource", resource)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        self.server.requests.append(self.path)
        route = urllib.parse.urlsplit(self.path).path
        match route:
            case "/rate_limit":
                bucket = {"limit": 10, "used": 1, "remaining": 9, "reset": int(time.time()) + 60}
                body = {"resources": {"code_search": bucket, "core": bucket}}
                self.reply(json.dumps(body).encode(), "application/json")
            case "/search/code" if self.server.malformed:
                body = {"total_count": 1, "incomplete_results": False, "items": [{"path": "openapi.yaml"}]}
                self.reply(json.dumps(body).encode(), "application/json", "code_search")
            case "/search/code":
                language = "yaml" if "YAML" in urllib.parse.unquote(self.path) else "json"
                item = {
                    "repository": {"full_name": "acme/found"},
                    "path": f"spec/openapi.{language}",
                    "sha": "e" * 40,
                    "url": f"http://127.0.0.1/repos/acme/found/contents/x?ref={'f' * 40}",
                }
                body = {"total_count": 1, "incomplete_results": False, "items": [item]}
                self.reply(json.dumps(body).encode(), "application/json", "code_search")
            case "/.api/search/stream" if self.server.sourcegraph_status != 200:
                self.send_response(self.server.sourcegraph_status)
                self.send_header("Content-Length", "0")
                self.end_headers()
            case "/.api/search/stream":
                matches = [{"repository": "github.com/acme/streamed", "path": "openapi.yaml", "commit": "a" * 40}]
                self.reply(
                    b"event: matches\ndata: "
                    + json.dumps(matches).encode()
                    + b"\n\nevent: progress\ndata: "
                    + json.dumps({"done": True, "matchCount": 1}).encode()
                    + b"\n\n",
                    "text/event-stream",
                )
            case _:
                self.reply(b"{}", "application/json")


class LiveSearchTests(BuildHarness):
    def services(self) -> _ServiceServer:
        services = _ServiceServer(("127.0.0.1", 0), _Services)
        services.requests = []
        threading.Thread(target=services.serve_forever, daemon=True).start()
        self.addCleanup(services.server_close)
        self.addCleanup(services.shutdown)
        base = f"http://127.0.0.1:{services.server_port}"
        self.env.update(CROZIER_GITHUB_API_URL=base, CROZIER_SOURCEGRAPH_URL=base, GITHUB_TOKEN="offline-test-token")
        return services

    def test_a_refused_search_is_reported_and_recorded_and_the_rest_of_the_search_goes_on(self) -> None:
        services = self.services()
        services.malformed, services.sourcegraph_status = True, 500
        plan = self.scratch / "plan.tsv.gz"
        self.assertEqual(0, self.build("identities", "--output", str(plan)).returncode)
        evidence, output = self.scratch / "search", self.scratch / "hits.tsv"
        args = (
            "search",
            "--evidence",
            str(evidence),
            "--identities",
            str(plan),
            "--output",
            str(output),
            "--key",
            "combo-property-defs-pointer",
            "--key",
            "combo-tag-only-operation-id",
        )
        done = self.build(*args)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn(
            "witness-populations-build: search stopped: GitHub search returned malformed results", done.stderr
        )
        self.assertIn("witness-populations-build: sourcegraph: Sourcegraph refused search", done.stderr)
        self.assertEqual([], SCREEN.read_identities(output))
        rows = [json.loads(line) for line in (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertIn(
            ("github-code-search", "combo-tag-only-operation-id", "not-queryable"),
            {(row["source"], row["key"], row["outcome"]) for row in rows},
        )
        self.assertIn(
            ("sourcegraph", "refused", 500), {(row["source"], row["outcome"], row.get("status")) for row in rows}
        )
        # The recorded refusal is the one Sourcegraph attempt: a later run does not ask again.
        services.requests.clear()
        self.assertEqual(0, self.build(*args).returncode)
        self.assertEqual([], [path for path in services.requests if path.startswith("/.api/search/stream")])

    def test_the_bounded_search_asks_each_key_once_records_what_it_cannot_ask_and_one_sourcegraph_query(self) -> None:
        services = self.services()
        plan = self.scratch / "plan.tsv.gz"
        self.assertEqual(0, self.build("identities", "--output", str(plan)).returncode)
        evidence, output = self.scratch / "search", self.scratch / "hits.tsv"
        args = (
            "search",
            "--evidence",
            str(evidence),
            "--identities",
            str(plan),
            "--output",
            str(output),
            "--key",
            "combo-property-defs-pointer",
            "--key",
            "combo-tag-only-operation-id",
        )
        done = self.build(*args)
        self.assertEqual(0, done.returncode, done.stderr)
        searched = [path for path in services.requests if path.startswith("/search/code")]
        streamed = [path for path in services.requests if path.startswith("/.api/search/stream")]
        self.assertEqual((2, 1), (len(searched), len(streamed)))
        lines = (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        recorded = sorted((row["source"], row["key"], row["outcome"]) for row in map(json.loads, lines))
        self.assertEqual(
            [("github-code-search", "combo-property-defs-pointer", "answered")] * 2
            + [
                ("github-code-search", "combo-tag-only-operation-id", "not-queryable"),
                ("sourcegraph", "combo-property-defs-pointer", "answered"),
            ],
            recorded,
        )
        self.assertEqual(
            {"acme/found/spec/openapi.yaml", "acme/found/spec/openapi.json"},
            {hit.document for hit in SCREEN.read_identities(output)},
        )
        services.requests.clear()
        again = self.build(*args)
        self.assertEqual(0, again.returncode, again.stderr)
        self.assertEqual([], [path for path in services.requests if not path.startswith("/rate_limit")])
        self.assertEqual(len(lines), len((evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()))


class RecordTests(unittest.TestCase):
    """The record's README, written from and checked against a copy of the committed evidence."""

    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory(prefix="witness-populations-record-")
        self.addCleanup(scratch.cleanup)
        self.record = Path(scratch.name) / "record"
        shutil.copytree(SCREEN.RECORD, self.record)

    def record_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(RECORD_SCRIPT), "--record", str(self.record), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=REPO,
            timeout=900,
        )

    def test_the_readme_is_written_from_its_evidence_and_a_stale_or_unreadable_record_is_refused(self) -> None:
        written = self.record_cli()
        self.assertEqual(0, written.returncode, written.stderr)
        readme = (self.record / "README.md").read_text(encoding="utf-8")
        rows = SCREEN.read_screen(self.record / "screen.tsv")
        for key, count in SCREEN.pending_counts(rows).items():
            self.assertIn(f"| `{key}` | `search-incomplete` | {count} |", readme)
        self.assertEqual(0, self.record_cli("--check").returncode)
        (self.record / "README.md").write_text(
            readme.replace("search-incomplete", "exhausted", 1), encoding="utf-8", newline="\n"
        )
        stale = self.record_cli("--check")
        self.assertEqual(1, stale.returncode)
        self.assertIn("is not what its evidence gives", stale.stderr)
        calls = self.record / "acquisition" / "raw-github-calls.jsonl"
        calls.write_text(calls.read_text(encoding="utf-8") + '{"at": "x"}\n', encoding="utf-8", newline="\n")
        malformed = self.record_cli("--check")
        self.assertEqual(1, malformed.returncode)
        self.assertRegex(malformed.stderr, r"raw-github-calls\.jsonl:\d+ is no record carrying at, status, url")
        calls.write_text(calls.read_text(encoding="utf-8").rsplit("\n", 2)[0] + "\n", encoding="utf-8", newline="\n")
        for log, line, message in (
            (
                self.record / "search" / "rate-limit-calls.jsonl",
                '{"at": "2026-11-13T00:00:00+00:00", "host": "github", "status": 200, "remaining": 11, "limit": 10}',
                r"rate-limit-calls\.jsonl:\d+ is no record carrying at, host, status",
            ),
            (
                self.record / "search" / "queries.jsonl",
                '{"source": "sourcegraph", "key": "combo-nope", "outcome": "answered"}',
                r"queries\.jsonl:1 is no record carrying source, key, outcome",
            ),
        ):
            with self.subTest(log=log.name):
                before = log.read_text(encoding="utf-8") if log.is_file() else None
                log.write_text((before or "") + line + "\n", encoding="utf-8", newline="\n")
                refused = self.record_cli("--check")
                self.assertEqual(1, refused.returncode)
                self.assertRegex(refused.stderr, message)
                if before is None:
                    log.unlink()
                else:
                    log.write_text(before, encoding="utf-8", newline="\n")
        (self.record / "acquisition" / "acquisitions.jsonl").unlink()
        missing = self.record_cli()
        self.assertEqual(1, missing.returncode)
        self.assertIn("acquisitions.jsonl is missing", missing.stderr)


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
        kept = self.run_cli("cached", pending[0].sha256, "--store", str(self.store))
        self.assertEqual(0, kept.returncode, kept.stderr)
        self.assertEqual(exact, Path(kept.stdout.strip()).read_bytes())
        lost = self.run_cli("cached", hashlib.sha256(b"never kept").hexdigest(), "--store", str(self.store))
        self.assertEqual(1, lost.returncode)
        self.assertIn("re-fetch them from the row's source", lost.stderr)
        SCREEN.store(exact, Path(self.env["XDG_CACHE_HOME"]) / "crozier" / "witness-populations")
        default = self.run_cli("cached", pending[0].sha256)
        self.assertEqual(0, default.returncode, default.stderr)


class CommittedTableTests(unittest.TestCase):
    rows: ClassVar[list[Any]]

    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = SCREEN.read_screen(SCREEN.TABLE)

    def test_the_committed_table_reads_whole_through_the_reader(self) -> None:
        self.assertEqual(set(SCREEN.KEYS), {row.key for row in self.rows})
        self.assertEqual(len(self.rows), len({(row.key, row.population, row.document) for row in self.rows}))

    def test_every_candidate_the_earlier_named_censuses_list_has_a_row(self) -> None:
        build = load("witness_populations_build_under_test", REPO / "tools/witness-search/witness-populations-build.py")
        have = {(row.key, row.population, row.document) for row in self.rows}
        census = build.named_census(build.Tree(REPO))
        self.assertGreaterEqual(sum(len(keys) for keys in build.earlier_rows(build.Tree(REPO)).values()), 749)
        for (population, document), keys in census.listed.items():
            for key in keys:
                with self.subTest(key=key, population=population, document=document):
                    self.assertIn((key, population, document), have)
        # A candidate named by digest alone owes a row of the bytes held under it, of the identity planned at
        # it, or of its own `sha256:<hex>`.
        by_digest: dict[str, set[tuple[str, str, str]]] = {}
        for row in self.rows:
            by_digest.setdefault(row.sha256, set()).add((row.key, row.population, row.document))
        planned: dict[str, set[tuple[str, str]]] = {}
        for name in ("identities.tsv.gz", "search-identities.tsv", "census-identities.tsv"):
            for identity in SCREEN.read_identities(SCREEN.RECORD / name):
                planned.setdefault(identity.pin, set()).add((identity.population, identity.document))
        for digest, (keys, _why) in census.digests.items():
            for key in keys:
                with self.subTest(key=key, digest=digest):
                    named = {(p, d) for k, p, d in by_digest.get(digest, set()) if k == key}
                    named |= {(p, d) for p, d in planned.get(digest, set()) if (key, p, d) in have}
                    self.assertTrue(named, f"no row of {key} carries the census's {digest}")

    def test_the_committed_readme_is_what_its_evidence_gives(self) -> None:
        done = subprocess.run(
            [sys.executable, str(RECORD_SCRIPT), "--check"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=REPO,
            timeout=900,
        )
        self.assertEqual(0, done.returncode, done.stderr)

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

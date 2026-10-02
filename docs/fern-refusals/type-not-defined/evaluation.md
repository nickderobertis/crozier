# type-not-defined: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was
made to qualify this class. Checks use CPython 3.12.3, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe output](evaluation-logs/probe.log) imports its package and client
but has **2 mypy errors**: both `parse_obj_as` calls in `api/raw_client.py`
pass a `typing.Never` special form for the bodyless 403. Failing `mypy`
disqualifies the class, so no wire journey was needed to decide it.

Three population representatives, from different publishers, fail too:

- [OGC API Maps, `0b075e70…`](evaluation-logs/population-ogcapi-maps.log)
  (tag `API`) **does not import**. The package's root `client.py` is a
  sub-package client (`from ..core.client_wrapper import …`), so
  `import fern` raises `ImportError`, and mypy reports 71 errors.
- [Provoly, `5d331361…`](evaluation-logs/population-provoly.log) imports
  but has **72 mypy errors** across three `raw_client.py` files.
- [SecurityScorecard, `958b17de…`](evaluation-logs/population-securityscorecard.log)
  imports, but mypy stops at 8 `Duplicate argument "customer_id"` errors.

The class is `refuse` in both modes.

## What pinned Fern refuses

All measurements use Fern CLI 5.67.1 with python-sdk 5.20.0, run with hand-written
controls. Two separate mechanisms print the phrase.

**An operation Fern files as `api.yml`.** Fern names a tag's definition file
by camel-casing the operation's first tag. When that name is `api`, the name
of the definition's root file, Fern cannot resolve any type or error the file
references. The tags `api`, `API`, `Api`, `Api_`, `_api`, `-api`, `api.` and
` API ` all fail. `ApI`, `aPI`, `api1`, `a pi`, `APIs`, `API Docs`, `error`,
`types`, `core`, `root` and `__package__` are accepted, and so is `api` as a
second tag. `x-fern-sdk-group-name` does not move the file: tag `api` with
group `users` still fails, and tag `users` with group `api` is accepted. An
`x-fern-ignore`d operation is accepted. Inside the file, these elements fail:

- any response whose status Fern names an error for. A one-operation-per-status
  [sweep](api-status-sweep-probe.yml) ([log](evaluation-logs/fern-api-status-sweep.log))
  measures that set as 400–426, 428–431, 444, 449–451 and 498–511. Every other
  status, `4XX` and a description-only `default` are skipped.
- the typed response, when its only media type is JSON and its schema names
  or declares a type: a `$ref` (object, enum, scalar alias or list alias), an
  enum or `const`, an object with properties, a map or list of those, `allOf`,
  or a `oneOf`/`anyOf` with two non-null members
  ([201 probe](api-response-probe.yml), [log](evaluation-logs/fern-api-response.log)).
  The typed response is `200` when it exists, else a sole 2xx, else `default`
  when there is no 2xx. A `200` string beside a `202` object is accepted.
- a query or path parameter whose schema declares a type. This holds for a
  path-item parameter, as in the [parameter probe](api-parameter-probe.yml)
  ([log](evaluation-logs/fern-api-parameter.log)), and for a `$ref`'d parameter.
- the request body when it declares a type: a JSON `$ref` to an enum or scalar
  alias ([body probe](api-body-probe.yml), [log](evaluation-logs/fern-api-body.log)),
  a JSON array of a type, or a JSON, form or multipart inline object with a
  type-declaring property.

**A union member that is also a request body.** A component union (`oneOf` or
`anyOf`, at least two members) where every member carries the same property
with one string value (`enum` of one or `const`) is discriminated by Fern on
that property. If one of its `$ref` members is also the entire
`application/json` body of an operation that is not ignored, Fern turns that
body into an inline request and the union's reference dangles
([probe](union-member-body-probe.yml), [log](evaluation-logs/fern-union-member-body.log)).
This applies whether the union is a property or a component, sits in an array,
uses `required` or not, has an explicit `discriminator` or not, and is
referenced from a request or a response. The Provoly document reduces to it:
with its unrelated duplicate `closeEvent` operation id renamed, it still fails
([log](evaluation-logs/fern-provoly-without-duplicate.log)).

## Accepted controls

Each control passes `fern check`, and Fern generates an SDK from it. crozier
generates byte-identical output from each one in both modes:

- [`api-file-accepted-control.yml`](api-file-accepted-control.yml)
  ([log](evaluation-logs/fern-api-file-accepted.log)) puts these under tag `api`:
  a cookie enum, a query of string arrays and integers, a JSON `$ref`-object
  body, an inline body of primitives, the skipped statuses (`302`, `427`, `432`,
  `460`, `520`, `599`, `4XX`, bare `default`), string/list/map/nullable/empty-object
  responses, a `text/plain` enum response, a `200` string beside a `202`
  object, and an ignored 403 operation.
- [`other-file-control.yml`](other-file-control.yml)
  ([log](evaluation-logs/fern-other-file.log)) carries the refused shapes (403,
  `$ref` response, `$ref` query) under the tags `people`, `a pi`, `APIs`, `ApI`,
  `api1`, `[people, api]` and none.
- [`group-name-control.yml`](group-name-control.yml)
  ([log](evaluation-logs/fern-group-name.log)) carries the same shapes with
  tag `people` and `x-fern-sdk-group-name: api`.
- [`union-member-control.yml`](union-member-control.yml)
  ([log](evaluation-logs/fern-union-member.log)) has body-referenced members in
  unions Fern does not discriminate. In one, a member has no enum. In another,
  the members use different property names. In a third, a member has two
  values. One has an explicit `discriminator` but no enums, and one has a
  single member.

A header with an inline enum is not part of this class. Fern lifts a header
that every operation shares to a global header and accepts it. Once another
operation lacks the header, it fails, so the detector leaves headers alone and
may miss a refusal there rather than over-refuse.

## Detector and evidence

`src/document_refusals/type_not_defined.rs` implements both rules from plain
OpenAPI and `x-fern-ignore`. It runs after the other structural checks, so a
document that another registered class already refuses keeps that class. With
`undefined_type_reference` disabled, the
[CLI journey failed](evaluation-logs/refusal-e2e-induced-red.log): crozier
wrote 40 files from the probe. The journey passes again once the detector is
restored. The journey covers the probe, the status sweep, response, parameter,
body and union probes, and two recoveries (tag `users`; a member without a
single value). It also checks the four controls for identical bytes in both
modes. I compared crozier's strict mode with Fern's check verdict on all 147
hand-written controls ([comparison](evaluation-logs/controls-comparison.log)).
Every control Fern refuses with this phrase is refused by this class. Every
control Fern accepts generates, except the header enum above, which the
existing `generator-missing-type` class refuses. The corpus
byte-match passes with `fern-strict` off and on (189/189 each).

[All six population documents](evaluation-logs/population-refusals.jsonl),
retrieved at their digests and run through the finished release build, are refused
in both modes: exit 1, no files, one class/element stderr line and the strict
cause when applicable. Three are refused by this class: OGC Maps (`GET /api
responses/406`), the RonasIT probe-shaped document (`POST /api/users
responses/403`) and Provoly
(`components/schemas/ProcedureWriteDto/properties/events/items/oneOf/0`). The
two SecurityScorecard bundles are refused first by `path-parameter-unreferenced`,
and OGC Processes by `object-extends-non-object`.

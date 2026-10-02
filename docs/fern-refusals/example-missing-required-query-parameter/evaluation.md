# example-missing-required-query-parameter: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was
made to qualify this class. Checks use CPython 3.12.3, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe output](evaluation-logs/probe.log) imports its package and client
and has **zero mypy errors**. Its [wire journey](evaluation-logs/probe.wire.log)
shows `get_collections(*, f: str)` taking the required parameter. It sends
`GET /collections?f=json` and parses the empty 204 as `None`. The probe alone
is valid and useful, because crozier never reads the `x-fern-examples` entry
Fern rejects.

Both population documents are OGC bundles from one publisher. Fern reaches
the class in them by a second route, its own generated examples (see below).

- [OGC API - Maps,
  `0b075e70eab691389aff5ac133deb2a60e6c01aefcb951d3db0dca059f95ae2f`](evaluation-logs/ogc-maps.log)
  **fails to import** `fern.client` ("attempted relative import beyond
  top-level package") and has **71 mypy errors**. The offending element is the
  optional `f` query enum. The `*RequestF` enum modules under `fern/types/`
  import `...core` from beyond the package, so mypy reports 16 missing
  return statements in their `visit` methods. The
  [wire log](evaluation-logs/ogc-maps.wire.log) shows those modules cannot be
  imported, so no call that types `f` can be made through the root client.
- [OGC API - Processes,
  `e145ad381fe4277ec2e558cd19b86af645e76479eab8ad5801eef63c976a7fae`](evaluation-logs/ogc-processes.log)
  gets **no SDK**. The baseline's loader rejects a schema in the document and
  exits 1.

The class is `refuse` in both modes. No generated SDK changes.

## When pinned Fern reports a required query parameter missing

Every case was run through pinned `fern check`. Each refused shape is a
`*-probe.yml` and each accepted near miss a `*-control.yml`; their logs are in
[`evaluation-logs/`](evaluation-logs/).

**From `x-fern-examples`.** Fern checks every entry of a non-empty
`x-fern-examples` list against the operation's required query parameters.

- An entry with a `query-parameters` map that lacks one is refused. So is an
  entry that sets one to `null` ([probe](required-null-value-probe.yml)). The
  same applies to any later entry ([probe](second-entry-omits-probe.yml)).
- An entry with only a `response` is checked as an empty map
  ([probe](response-only-example-probe.yml)). An entry with only a `name`, or
  with `query-parameters: null`, is not checked
  ([name only](no-query-parameters-key-control.yml),
  [null](query-parameters-null-control.yml)).
- Keys are wire names and case-sensitive
  ([wrong case](wrong-case-key-probe.yml)).
  `x-fern-parameter-name` does not change them
  ([SDK name refused](renamed-param-uses-sdk-name-probe.yml),
  [wire name accepted](renamed-param-uses-wire-name-control.yml)).
- Path Item parameters and component references count
  ([Path Item](path-level-required-omitted-probe.yml),
  [reference](ref-param-omitted-probe.yml)). A default does not excuse an
  omission ([probe](required-default-omitted-probe.yml)), and neither does an
  object, untyped or `content` schema
  ([object](required-object-omitted-probe.yml),
  [untyped](required-untyped-omitted-probe.yml),
  [content](required-content-param-omitted-probe.yml)).
- `nullable`, `type: [string, 'null']` and list parameters may be omitted
  ([nullable](required-nullable-omitted-control.yml),
  [3.1 null](required-31-null-union-omitted-control.yml),
  [list](required-array-omitted-control.yml)). So may optional, ignored and
  `x-fern-ignore`d parameters, and the parameters of ignored operations
  ([optional](optional-param-omitted-control.yml),
  [ignored parameter](ignored-param-omitted-control.yml),
  [ignored operation](ignored-operation-control.yml)).
- An empty list and a missing extension leave Fern's own complete example in
  force ([empty](empty-list-control.yml),
  [none](required-no-examples-control.yml),
  [parameter example](required-with-example-no-ext-control.yml)). Per the
  planner's ruling, `x-crozier-examples` is not read
  ([control](x-crozier-examples-omitted-control.yml)).

**From Fern's own example (the population's route).** Fern writes an
operation whose first tag is `API`, `Api` or `api` into a definition file
named `api.yml`, and its root definition replaces that file. The named type
of an optional query parameter there is lost ("Type … is not defined"), so
Fern's generated example omits the parameter. Fern then reports it as a
missing required one.

- This happens for an inline enum ([probe](api-tag-optional-enum-probe.yml),
  [lower case](api-tag-lower-optional-enum-probe.yml)), a referenced enum
  ([probe](api-tag-optional-ref-enum-probe.yml)), a list of enums
  ([probe](api-tag-optional-array-enum-probe.yml)) and a nullable enum
  ([probe](api-tag-nullable-enum-probe.yml)).
- Primitive and primitive-list parameters keep their types and are accepted
  ([string](api-tag-optional-string-control.yml),
  [list](api-tag-optional-array-string-control.yml)). So are the same enum
  under a later `API` tag, under another tag, or untagged
  ([later tag](api-second-tag-optional-enum-control.yml),
  [other tag](other-tag-optional-enum-control.yml),
  [untagged](untagged-optional-enum-control.yml)).
- A *required* enum under `API` makes Fern report only `type-not-defined`.

Every one of these probes also prints Fern's "Type … is not defined", the
`api.yml` mechanism the `type-not-defined` detector measures. On integration
this class's own `API`-tag predicate was removed in favour of that detector,
which refuses each tagged probe first, naming `GET /things parameter f`; the
CLI journey asserts that refusal, and every accepted control still generates.

Where a shape was not measured, the detector does not refuse. Every accepted
control generates identical bytes in both crozier modes.

The [CLI assertion failed with only the `x-fern-examples` predicate
disabled](evaluation-logs/refusal-e2e-induced-red.log), writing 36 files.
Before integration, with only the then `API`-tag predicate disabled, the
[same assertion failed on the tagged probe](evaluation-logs/api-tag-induced-red.log),
writing 40 files. Both passed again once restored. Giving `f` in the probe's
example recovers generation in both modes.

[Both population documents](evaluation-logs/population-refusals.jsonl) were
retrieved at their digests and run with the finished detector's release build.
Both were refused in both modes: exit 1, no files, one stderr line naming the
class and element, and the strict cause where it applies. Maps was refused as
this class (`GET /api tag API query parameter f`) before integration; the
final remeasurement in that log records the class that refuses it now. Processes hits the
registered `object-extends-non-object` refusal first.

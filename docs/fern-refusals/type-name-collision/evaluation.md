# type-name-collision

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe imports but reports one mypy error under the generated pyproject configuration. GET /a and GET /b parse their declared fields, but both exported response types use GetThingResponse, creating an ambiguous public identifier. This fails both the type-check and identifier bar.
[generate](evidence/type-name-collision.generate.log), [import](evidence/type-name-collision.import.log), [mypy](evidence/type-name-collision.mypy.log), [wire](evidence/type-name-collision.wire.log)

Retrievable population representative `5d331361f37ae9aa5c3184c8033a37158ea686373c7ec67b79ccdf68aae12114` (source locator in generation log):
The representative imports but reports 72 mypy errors under its own generated pyproject configuration. The zero-error bar fails. A baseline HTTP journey sends both declared close-event PUT routes and parses both 204 responses as None.
[generate](evidence/5d331361f37ae9aa5c3184c8033a37158ea686373c7ec67b79ccdf68aae12114.generate.log), [import](evidence/5d331361f37ae9aa5c3184c8033a37158ea686373c7ec67b79ccdf68aae12114.import.log), [mypy](evidence/5d331361f37ae9aa5c3184c8033a37158ea686373c7ec67b79ccdf68aae12114.mypy.log)

Population wire journey: [real SDK HTTP boundary](evidence/5d331361f37ae9aa5c3184c8033a37158ea686373c7ec67b79ccdf68aae12114.wire.log).

All 104 retrievable population documents refuse with exit 1 and no output under strict mode: [measurements](evidence/population-strict.log).

Pinned Fern controls: [type-collision-different-context.pinned-fern](evidence/type-collision-different-context.pinned-fern.log), [type-collision-nested-exact.pinned-fern](evidence/type-collision-nested-exact.pinned-fern.log), [type-collision-nested-snake.pinned-fern](evidence/type-collision-nested-snake.pinned-fern.log), [type-collision-root-camel.pinned-fern](evidence/type-collision-root-camel.pinned-fern.log), [type-collision-root-exact.pinned-fern](evidence/type-collision-root-exact.pinned-fern.log), [type-collision-root-snake.pinned-fern](evidence/type-collision-root-snake.pinned-fern.log), [type-collision-same-module.pinned-fern](evidence/type-collision-same-module.pinned-fern.log).

Integration with the `documents` family (refusals-documents) measured one
boundary of the namespaced-enum rule. A tag or SDK-group enum named like a root
schema is refused as already declared for a query parameter
([same values](evidence/namespaced-query-enum-same.pinned-fern.log),
[different](evidence/namespaced-query-enum-diff.pinned-fern.log),
[tag](evidence/namespaced-query-enum-same-tag.pinned-fern.log),
[tag, different](evidence/namespaced-query-enum-diff-tag.pinned-fern.log)),
but pinned Fern checks and generates a header parameter's
([same values](evidence/namespaced-header-enum-same.pinned-fern.log),
[different](evidence/namespaced-header-enum-diff.pinned-fern.log),
[tag](evidence/namespaced-header-enum-diff-tag.pinned-fern.log)), as the
`generator-missing-type` header controls also show. Header-parameter enums,
named with the IR's own request-context helpers, are therefore exempt from
both namespace rules; the [CLI journey fails with that exemption removed](evidence/namespaced-header-enum-induced-red.log).
A reserved-expansion route `{+accountId}` draws both an unreferenced path
parameter and the camelCase collision from [Fern](evidence/reserved-expansion-path.pinned-fern.log);
the document-family check names it first.

The detector also covers a declared type name (`x-fern-type-name` or
`x-crozier-type-name`) that two component schemas resolve to. Pinned Fern
merges the two into one type. It generates the merge when the schemas are the
same: the authored probe
[`376-350-declared-type-name-shared`](../../openapi-surface/authored-probes/376-350-declared-type-name-shared/)
holds Fern's tree, which crozier byte-matches. When they differ, its
`fern check` fails on the merged type's example: both components declaring the
name ([probe](evidence/376-350-declared-type-name-shared-differing.yml),
[pinned Fern](evidence/376-350-declared-type-name-shared-differing.pinned-fern.log)),
and one declaring a name the other holds as its key
([probe](evidence/376-350-declared-type-name-taken.yml),
[pinned Fern](evidence/376-350-declared-type-name-taken.pinned-fern.log)).
crozier refuses those two in both modes, naming both components.

The detector also covers an inline schema declaring a type name, which
crozier lifts into a type of that name. Fresh independently authored probes
were generated with CLI 5.67.1 and Python SDK 5.20.0 through
`tools/fern-goldens/generate-fern-fixture.sh` with its default settings. Pinned
Fern takes the declaration as the type already holding the name. An inline
enum declaring `Finish` beside an object component `Finish`
([probe](evidence/inline-declared-type-name-component.yml),
[pinned Fern](evidence/inline-declared-type-name-component.pinned-fern.log))
fails its check with `Expected example to be an object`. Two inline enums
declaring `Finish` with different values
([probe](evidence/inline-declared-type-name-inline.yml),
[pinned Fern](evidence/inline-declared-type-name-inline.pinned-fern.log))
fail with `"satin" is not a valid example for this enum`. These are name-only
faults: crozier refuses both in both modes, naming the operation, the type and
the schema already holding it, and never generates the inline schema under a
derived name. When the inline schema is the component's own
([probe](evidence/inline-declared-type-name-same.yml),
[pinned Fern](evidence/inline-declared-type-name-same.pinned-fern.log)),
Fern merges the two and generates; crozier references the component and
matches that tree. A distinct declared name beside the component
([probe](evidence/inline-declared-type-name-control.yml),
[pinned Fern](evidence/inline-declared-type-name-control.pinned-fern.log))
generates in both, and so does the hand-written `film-shot-planner` golden.

The detector also covers the request types of a `stream-condition` split. Pinned
Fern gives an operation declaring `x-fern-streaming`'s `stream-condition` two
methods, and it synthesizes a request type for each: `{Ctx}Request` and
`{Ctx}StreamRequest`. `Ctx` is the PascalCase of the SDK method name, or else
of the `operationId`. A component schema already holding either name is
`already declared in this file`. It does not matter whether the schema is the
operation's own body or any other component. These fresh probes show the
refusal at check and at generate:

- a body schema named `LookupRequest` for `operationId: lookup`
  ([probe](evidence/stream-split-request-name.yml),
  [pinned Fern](evidence/stream-split-request-name.pinned-fern.log));
- one named `LookupStreamRequest`
  ([probe](evidence/stream-split-stream-request-name.yml),
  [pinned Fern](evidence/stream-split-stream-request-name.pinned-fern.log));
- one named `FindRequest` for `x-fern-sdk-method-name: find`
  ([probe](evidence/stream-split-sdk-method-request-name.yml),
  [pinned Fern](evidence/stream-split-sdk-method-request-name.pinned-fern.log)).

The adjacent control checks and generates: the same `LookupRequest` body under
`x-fern-sdk-method-name: find`
([probe](evidence/stream-split-sdk-method-control.yml),
[pinned Fern](evidence/stream-split-sdk-method-control.pinned-fern.log)).
crozier byte-matches that control's tree. The fault is name-only: the document
is valid OpenAPI, and every operation, body and response in it would generate
if one name changed. Because the fault is only a name, crozier refuses it in both
modes, with `type-name-collision: POST /lookups stream-condition request type
LookupRequest collides with component schema "LookupRequest"`. It never
generates the split under a repaired name.

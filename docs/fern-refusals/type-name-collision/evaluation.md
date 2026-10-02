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
`x-crozier-type-name`) that two component schemas resolve to, measured on the
authored probes under
[`../../openapi-surface/authored-probes/`](../../openapi-surface/authored-probes/).
Pinned Fern merges the two into one type. It generates the merge when the
schemas are the same (`crozier-350-declared-type-name-shared`). When they
differ, its `fern check` fails on the merged type's example: both components
declaring the name (`-shared-differing`), and one declaring a name the other
holds as its key (`-taken`). crozier refuses those two in both modes, naming
both components, and byte-matches Fern's tree for the merge of the same schemas.

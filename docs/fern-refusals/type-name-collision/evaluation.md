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

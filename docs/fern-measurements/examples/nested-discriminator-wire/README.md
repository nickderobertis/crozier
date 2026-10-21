# Nested discriminator wire defect

Pending repair; this is not an admitted hand-written cover or a byte-match proof.
The manager separated its repair from the feature-proof work after the runtime
measurement below. Both nested mapping arms remain unproven.

`openapi.yml` was authored from scratch. `fern-expected/` is the complete freshly
generated, comment-stripped output of Fern CLI 5.163.1 and Python SDK 5.41.3,
produced with the native `fern-references.py generate handwritten` pipeline.
Its native tree digest is
`bab02bcc092244e72bbd68eff3faf1b60400d72b0cdc980560e9d4e57ccb650c`.
`schema.json` is the same source document decoded as JSON for the installless
schema reader; it is not a different measurement input.

`runtime.txt` records an actual run with Pydantic 2.14.1. A provider's flat
payload validates against the source schema. Constructing the corresponding
SDK variant emits an extra `value` envelope that fails that schema, while the
SDK rejects the valid provider payload for missing `value`. Its README's
`tart=,` example also fails Python compilation. Crozier currently shares the
wire defect; its matching model files do not prove correct behavior.

To reproduce in a disposable environment, install `./fern-expected` and
`jsonschema`, then run `python reproduce.py`. The script first validates the
positive control and then requires all three failures. The repair must keep
Fern's public variant classes and `.value` constructors while flattening the
wire representation in both directions, for Pydantic v1 and v2, and repair the
README example. No departure or coverage claim is made before that repair.

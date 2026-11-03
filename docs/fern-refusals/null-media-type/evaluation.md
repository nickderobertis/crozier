# null-media-type: refuse

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, by the user's design-review ruling `empty-sdk-refused`
(decided 2026-11-01): crozier refuses, in default and `fern-strict` modes,
every document the certified pair turns into an empty SDK, because an empty SDK
is useless and crozier refuses rather than writes one. This is an intended
departure from the pair's exit 0, recorded under
[Intended departures](../README.md#intended-departures).

The shape is a Media Type Object written as `null`: a `content` key with no
value, such as `image/png:` on its own line. A Media Type Object is required to
be an object, so the document is invalid OpenAPI, and the refusal rule's
valid-OpenAPI exception does not apply. The [probe record](fern-refusal.txt) is
the certified pair's false success over the [probe](probe.yml). Its check and
generation exit 0, its log reads `Failed to parse openapi document` and then
`Cannot read properties of null (reading 'schema')`, and it writes the 35-file
empty SDK, with no endpoint and no type. The committed shapes are measured at
this pair ([`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv)):

- `request-body-probe` is the same `null` under a request body's `text/plain`.
  The pair empties it the same way, though the property its importer fails to
  read there is `x-fern-sdk-method-name`, not `schema`, so the class's template
  leaves the property name open.
- `component-response-probe` and `component-request-body-probe` write the
  `null` in the `components.responses` or `components.requestBodies` entry an
  operation's `$ref` names. The pair empties both, with the same two phrases.
- `empty-media-type-control` writes `image/png: {}` instead, and the pair
  generates it (36 files).

crozier's detector (`null_media_type` in `src/document_refusals.rs`) reads the
`content` of every request body and response of an operation that is not
ignored. It reads the content where the operation writes it, or in the
`components.requestBodies` or `components.responses` entry the operation's
`$ref` names. It refuses the first `null` entry and names the pointer where
that entry is written. Those four forms are the ones the pair was measured on.
A component entry no operation reaches was not measured, so the detector
leaves it to generation. Before this detector, crozier read a `null` entry as
an empty Media Type Object and generated the whole SDK in both modes.

The population carries the class on no document. Its one real document,
`linux-automation/tacd`'s `openapi.yaml` at
`df3958c92643f7e0b06ef1830b9bc2a5e55ab24a` (SHA-256
`b5dacb83849e3ef5b20249f712ed19ac60838e5052ce0a4de3b6c69aed29bd8c`), is outside
the refusal population. The handed-off record
[`refusal-null-media-type`](../../fern-measurements/handed-off/empty-sdk-documents/refusal-null-media-type/README.md)
measures it: the certified pair, run on its exact bytes, writes the 35-file
empty SDK with the same phrase. crozier now refuses it in both modes with
`null-media-type: paths//v1/tac/display/content/get/responses/200/content/image/png`.
`crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs` holds the refusal of both
probes in both modes and the control's generation.

# Request bodies, forms and responses

Each case below is a from-scratch document measured against Fern CLI 5.216.0
with `fernapi/fern-python-sdk` 5.42.0 (its `fern-expected/.fern/metadata.json`
records both), registered in [`../cases.tsv`](../cases.tsv) so `just
fern-references measurements` regenerates it, and held whole by
[`crates/crozier-e2e/tests/e2e/bodies_responses.rs`](../../../crates/crozier-e2e/tests/e2e/bodies_responses.rs).
The `*-literals` directories beside them are older measurements with their own
`evidence.md`.

| case | ticket | what the certified pair does |
|---|---|---|
| `single-member-union-body` | #888 | A body naming a one-member `oneOf`/`anyOf` around an object component spreads the member's fields into keyword arguments; the union's model is still declared. |
| `inline-union-body-content-type` | #890 | An inline union body sends the JSON `content-type` only when its schema has a `title` or `description`, discriminated or not. Both enum modes (`expected-literals/`). |
| `titled-shared-single-body` | #892 | A titled component passed whole as `request` and posted by two operations keeps the header on its parameterless one. |
| `body-requiredness-shapes` | #903 | `anyOf: [free-form object, null]` is `Optional[...] = None` though required; an inline `oneOf` body is required though `required: false`. |
| `schemaless-error-media` | #913 | An error body reads its first declared media: no schema or `{}` is `typing.Any` though a typed media follows. |
| `inline-error-component-name` | #914 | An inline error object named as a component model already is declares nothing; the component's nested model stays. |
| `superseded-error-types` | #915 | A later inline error body replaces the earlier one's model; the earlier one's nested models stay declared. |
| `multipart-only-body-collision` | #916 | Two multipart-only components whose names collide on one class keep no model. |
| `composed-form-body` | #917 | A form body composed only of inline `allOf` members sends every member's field, multipart and urlencoded. |
| `multipart-binary-reference` | #918 | A part referencing a binary component, plain or nullable, is the `bytes` alias sent raw in `data=`. |
| `multipart-binary-required-part` | #918 | The same part required. Transport matches; every worked call passes the part as the `bytes` its `FormFile` annotation takes (`file=b"file"` in `README.md`, `reference.md` and `client.py`), where the certified pair passes the `str` `file="file"` — the [`binary-form-part-example`](../../departures/evidence/binary-form-part-example.md) departure. |
| `header-body-collision` | #926 | A body property whose argument name a header takes is renamed. Inlined bodies send it correctly in both generators; a shared component body is sent with the header's value by the certified pair, the catalogued [`body-query-parameter-value`](../../departures/evidence/body-query-parameter-value.md) departure, proven on the wire by `tests/runtime/test_header_body_collision.py`. |
| `request-convert-decision` | #938 | A nullable scalar alias body is sent raw; a map of a union alias goes through the converter. |
| `unknown-response-guard` | #939 | A success response naming a component declared `typing.Any` keeps the empty-body guard. |
| `non-component-ref-body` | #950 | A body `$ref` to a missing schema outside `components` is `typing.Any`, and the operation keeps its method. |

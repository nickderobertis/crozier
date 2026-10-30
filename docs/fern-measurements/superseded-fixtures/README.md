# Superseded hand-written fixtures

Authored documents, each with the complete tree the certified pair generated
from it, that were hand-written proofs until a registered real specification
proved the same shape. They no longer count as hand-written proofs (none
carries an `evidence.toml`), and are kept unchanged only because tests,
measurements or a departure's evidence read them as inputs.

| fixture | superseded as a proof of | by |
|---|---|---|
| `buoy-depth-response` | `response-without-description-blank-line`, and `response-description`'s `push_return_doc` arm | corpus row 4200, `amrc-acs-directory` |
| `event-stream-event-dispatch` | `media-type-event-stream-event-dispatch`, and `media-type-event-stream`'s `raw_stream_method` and `sse_event_dispatch` arms | corpus row 4207, `synthwerk-llm` |
| `gallery-plaque-groups` | `camel-case-tag-group-and-prefix` | corpus row 4206, `kompaz-web-frontend` |
| `kiln-form-mode` | `media-type-form-urlencoded`'s `hoist_form_object` arm | corpus row 4201, `ummaya-agent-delegation` |
| `multipart-request-name` | `request-body-content`'s `validate_ir` arm | corpus row 4204, `openparser-ocr` |
| `pottery-commission` | `allof-body-example-id-field-order` | corpus row 4205, `jobster-api` |
| `request-alias` | `request-body-content`'s `resolve_form_object_alias` arm | corpus row 4203, `openiap-opencore` |
| `request-example-nulls` | `request-example-nested-null` | corpus row 2801, `dystore-api` |

The search that found each witness is
[`witness-search-fixture-only-bodies-paths`](../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md).

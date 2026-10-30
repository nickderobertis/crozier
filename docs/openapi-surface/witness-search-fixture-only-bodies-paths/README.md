# Witness search for the fixture-only bodies, media and document-path shapes

A bounded search for real specifications that could replace the hand-written
proofs of the `bodies-media` and `document-paths` regions. A target is proven
here only by a registered corpus row whose complete certified-pair golden
(Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) crozier byte-matches
in both enum modes and that declares the feature, or whose instrumented run
executes the target's arm or interaction branch. Every other target ends
`exhausted` or `search-incomplete`, with what is outstanding named below and
every declarer, its site count and its screening outcome in
[`census.tsv`](census.tsv).

## Targets

Computed from base `1748b794688900b67e630cad6f606f421bb14b3a`: every `handwritten` row of `bodies-media.md` and
`document-paths.md` (combination rows included), no residual-only supplement (neither file has one), and every
arm-level cover of a `golden` row there that `handwritten-reach.tsv` listed.

| key | kind | region | cover at base | state now |
|---|---|---|---|---|
| `request-body-described-inline-scalar` | feature | `bodies-media` | `described-scalar-bodies` | proven: corpus row 4210 |
| `media-type-event-stream-binary-schema` | feature | `bodies-media` | `event-stream-binary-download` | exhausted |
| `media-type-event-stream-event-dispatch` | feature | `bodies-media` | `event-stream-event-dispatch` | proven: corpus row 4207 |
| `media-type-event-stream-inline-const-union` | feature | `bodies-media` | `event-stream-const-tagged-union` | exhausted |
| `media-type-event-stream-item-schema` | feature | `bodies-media` | `event-stream-item-schema` | search-incomplete |
| `response-contentless-200-with-created` | feature | `bodies-media` | `contentless-created-success` | proven: corpus row 4211 |
| `response-status-space-suffixed` | feature | `bodies-media` | `suffixed-status-keys` | search-incomplete |
| `get-request-body-union-member` | feature | `bodies-media` | `bakery-get-body-member` | search-incomplete |
| `allof-parent-request-body` | feature | `bodies-media` | `allof-parent-body-order` | search-incomplete |
| `request-example-nested-null` | feature | `bodies-media` | `request-example-nulls` | proven: corpus row 2801 |
| `request-example-deprecated-property` | feature | `bodies-media` | `request-example-deprecated` | search-incomplete |
| `enum-union-body-example-first-member-value` | feature | `bodies-media` | `enum-union-body-example-first-member-value` | search-incomplete |
| `multipart-inline-object-part-json-encoded` | feature | `bodies-media` | `multipart-inline-object-part-json-encoded` | search-incomplete |
| `multipart-part-encoding-charset-tuple` | feature | `bodies-media` | `multipart-part-encoding-charset-tuple` | search-incomplete |
| `patch-inline-nullable-unrequired-props-omit` | feature | `bodies-media` | `patch-inline-nullable-unrequired-props-omit` | proven: corpus row 4209 |
| `stream-error-status-raises-typed-error` | feature | `bodies-media` | `stream-error-status-raises-typed-error` | exhausted |
| `string-body-example-backslash-escaped` | feature | `bodies-media` | `string-body-example-backslash-escaped` | search-incomplete |
| `allof-body-example-id-field-order` | feature | `bodies-media` | `pottery-commission` | proven: corpus row 4205 |
| `binary-download-with-body-has-no-example` | feature | `bodies-media` | `seismic-trace-export` | search-incomplete |
| `example-imports-case-insensitive-order` | feature | `bodies-media` | `avionics-booking` | search-incomplete |
| `readme-multipart-file-params-listed-first` | feature | `bodies-media` | `poster-upload` | search-incomplete |
| `readme-multipart-optional-file-params` | feature | `bodies-media` | `passport-scan` | search-incomplete |
| `readme-streaming-snippet-omits-type-import` | feature | `bodies-media` | `weather-radar-stream` | search-incomplete |
| `response-without-description-blank-line` | feature | `bodies-media` | `buoy-depth-response` | proven: corpus row 4200 |
| `text-response-drops-request-example` | feature | `bodies-media` | `invoice-renderer` | search-incomplete |
| `multipart-optional-enum-part-plain-field` | feature | `bodies-media` | `transcript-format-part` | search-incomplete |
| `combo-inline-body-read-only-property` | combination | `bodies-media` | `harbor-relay-registration` | witness-blocked |
| `server-default-url-templated` | feature | `document-paths` | `harbour-pilot-regions` | exhausted |
| `server-name-several` | feature | `document-paths` | `orbit-ground-stations` | search-incomplete |
| `operation-servers-named` | feature | `document-paths` | `locker-archive-hosts` | search-incomplete |
| `operation-id-untagged-list-or-set` | feature | `document-paths` | `depot-bin-ledger` | search-incomplete |
| `operation-id-hyphenated-tag-method` | feature | `document-paths` | `ferry-berth-desk` | proven: corpus row 4208 |
| `operation-id-all-caps-tag-split-prefix` | feature | `document-paths` | `rfid-door-panel` | search-incomplete |
| `operation-empty-tag` | feature | `document-paths` | `lamp-room-log` | exhausted |
| `empty-path-segment-double-slash-kept` | feature | `document-paths` | `empty-path-segment-double-slash-kept` | search-incomplete |
| `group-path-ending-in-api-nested-package` | feature | `document-paths` | `group-path-ending-in-api-nested-package` | search-incomplete |
| `readme-endpoint-prefers-argless-non-get` | feature | `document-paths` | `greenhouse-vents` | search-incomplete |
| `readme-nested-group-post-preferred` | feature | `document-paths` | `water-pump-station` | search-incomplete |
| `camel-case-tag-group-and-prefix` | feature | `document-paths` | `gallery-plaque-groups` | proven: corpus row 4206 |
| `combo-body-property-named-as-path-param` | combination | `document-paths` | `beacon-signal-results` | search-incomplete |
| `combo-body-property-named-as-header-param` | combination | `document-paths` | `ferry-desk-header-collision` | search-incomplete |
| `combo-success-oneof-nullable` | combination | `document-paths` | `beacon-signal-results` | search-incomplete |
| `combo-success-anyof-nullable` | combination | `document-paths` | `beacon-signal-results` | search-incomplete |
| `response-description` | arm `src/emit.rs::push_return_doc[=None => \{\}]` | `bodies-media` | `buoy-depth-response` | proven: corpus row 4200 |
| `media-type-event-stream` | arm `src/emit.rs::raw_stream_method[StreamProtocol::Sse \{ terminator, events \} if !events\.is_empty\(\) => \{]` | `bodies-media` | `event-stream-event-dispatch` | proven: corpus row 4207 |
| `media-type-event-stream` | arm `src/ir.rs::sse_event_dispatch[if !discriminator\.mapping\.is_empty\(\) \{]` | `bodies-media` | `event-stream-event-dispatch` | proven: corpus row 4207 |
| `request-body-content` | arm `src/ir.rs::resolve_request_body[if let Some\(own\) = fields$]` | `bodies-media` | `inline-body-readonly-own-overlap` | search-incomplete |
| `request-body-content` | arm `src/ir.rs::resolve_request_body[if is_optional\(target\) \&\&]` | `bodies-media` | `json-request-shapes` | search-incomplete |
| `request-body-content` | arm `src/ir.rs::resolve_request_body[let own_count = fields\.len\(\)]` | `bodies-media` | `json-request-shapes` | search-incomplete |
| `media-type-form-urlencoded` | arm `src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | `bodies-media` | `kiln-form-mode` | proven: corpus row 4201 |
| `media-type-multipart` | arm `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | `bodies-media` | `multipart-alias-object` | search-incomplete |
| `media-type-multipart` | arm `src/emit.rs::Imports::json_module[=^ {12}self\.json_module_alias = true;$]` | `bodies-media` | `multipart-json-module` | search-incomplete |
| `request-body-content` | arm `src/name_refusals.rs::validate_ir[=body\.content\.len\(\) == 1]` | `bodies-media` | `multipart-request-name` | proven: corpus row 4204 |
| `request-body-content` | arm `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | `bodies-media` | `request-alias` | proven: corpus row 4203 |
| `request-body-content` | arm `src/ir.rs::request_media_variants[let mut view = op\.with_sdk_method_name]` | `bodies-media` | `request-media-methods` | exhausted |
| `request-body-content` | arm `src/openapi.rs::Operation::with_sdk_method_name` | `bodies-media` | `request-media-methods` | exhausted |
| `media-type-malformed-key` | arm `src/ir.rs::has_dispatchable_media[=^ {16}return true;$]` | `bodies-media` | `slashless-json-response` | search-incomplete |
| `media-type-multipart` | arm `src/ir.rs::nullable_enum_part[    member$]` | `bodies-media` | `transcript-format-part` | proven: corpus row 4202 |

Of the 58 targets, 16 are proven by a registered real witness, 7 read `exhausted`, 34 read `search-incomplete` and 1 reads `witness-blocked`.

## Populations read

Every population was read offline first; only the targets those left open
went to live GitHub code search. Each file was parsed with PyYAML 6.0.3's C
loader (JSON with the standard library), falling back to the census's own
reader, and each OpenAPI 3 document was censused by the repository's
unchanged `tools/surface-census/openapi-surface-census.py` evaluator.

| population | revision | files read | OpenAPI 3 | other version | unreadable |
|---|---|---:|---:|---:|---:|
| registered corpus (`tests/fixtures/`) | base `1748b794688900b67e630cad6f606f421bb14b3a` | 986 | 294 | 692 | 0 |
| APIs.guru `APIs-guru/openapi-directory` archive | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, archive SHA-256 `816adb9fb4e19dc9ab28d7ad95363de146251fb41164abdb86f953f9f400c644` | 4,138 | 1,970 | 2,168 | 0 |
| earlier GitHub code-search acquisitions (two retained copies) | identity snapshot SHA-256 `ecdfa0355116f4c28e5b0768997eedb070d2453aef9668fb77a56ad1817165b5` | 10,159 | 9,484 | 569 | 106 |
| earlier Sourcegraph acquisitions (two retained copies) | the same identity snapshot | 8,100 | 5,640 | 2,424 | 36 |
| shared GitHub response cache, bodies naming `openapi` | `${XDG_CACHE_HOME:-$HOME/.cache}/crozier/github-responses/` as read on 2026-10-29 | 1,577 | 1,566 | 3 | 8 |
| this search's live GitHub code-search results | each result at the commit GitHub indexed | 2,497 | 946 | 1,094 | 457 |

The populations overlap; 10,755 distinct OpenAPI 3 documents (by SHA-256) were
censused. A cache body names no request, so one with no recorded publisher,
path and revision in an earlier search's ledger or enumeration is counted but
cannot be registered. The earlier acquisitions' identities, and their
hash audit, are those the
[interaction search](../witness-search-interaction-operation-combinations/README.md#populations-read)
recorded.

## Live requests

Every live GitHub request this search made went through
`tools/witness-search/rate_limit_guard.py`, the shared response cache
consulted first; the guard's own ledgers are under
`.local/witness-search-fixture-only-bodies-paths/`. 26 query phrasings were
issued, up to their first three result pages, with 30 seconds between
code-search calls.

| bucket | live requests | answered from the cache |
|---|---:|---:|
| `code_search` | 52 | 4 |
| `core` (result contents, repository licences, source verification) | 3282 | 137 |

The guard logged one wait and two burn-rate probes; no secondary-limit refusal
occurred. One further request went outside the guard by mistake: a single
unauthenticated `GET https://api.github.com/repos/openiap/opencore` from a
shell command, whose answer was not used (the guarded lookup had already
recorded that repository's licence).

## How a declarer was screened

In this order, the first that applies deciding it:

1. a registered row, whose golden either shows the shape or, read here, does not;
2. this repository's own authored documents, and the generator vendor's own
   repositories (dropped unread);
3. a test, sample, example, fixture or mock resource by its path, under the
   manager's ruling that such generator and tooling material is not a
   real-world specification;
4. no redistribution grant under [`../../corpus-licensing.md`](../../corpus-licensing.md):
   the document's `info.license` and its repository's licence as GitHub's
   API reports it (the APIs.guru archive by `info.license` alone, a `jentic`
   aggregation by its CC0 grant);
5. a Fern refusal already measured at the certified pair in
   [`../fern-refusals/measurements.jsonl`](../fern-refusals/measurements.jsonl);
6. otherwise, generated by the certified pair under the shared generation lock
   and compared with crozier's output through `crozier compare` (the parity
   engine with every catalogued departure): a byte-match is registered, and a
   difference is recorded with the files it touches.

An arm's or combination's declarers are the documents whose instrumented
crozier run (the build `just golden-reach` measures with, through
`golden-reach-search.py`'s own probe) executes the arm, so a document the
census counts but whose run never takes the branch is recorded as not
reaching it. A probe ran over every document a necessary-condition prefilter
of the arm admitted: 1,266 documents.

## Detectors

| target | detector |
|---|---|
| `request-body-described-inline-scalar` | census `operation.requestBody:described-inline-scalar` |
| `media-type-event-stream-binary-schema` | census `operation.responses:event-stream-binary` |
| `media-type-event-stream-event-dispatch` | census `operation.responses:event-stream-event-dispatch` |
| `media-type-event-stream-inline-const-union` | census `operation.responses:event-stream-inline-const-union` |
| `media-type-event-stream-item-schema` | census `operation.responses:event-stream-item-schema-ref` |
| `response-contentless-200-with-created` | census `operation.responses:contentless-two-hundred-with-created` |
| `response-status-space-suffixed` | census `operation.responses:space-suffixed-status-key` |
| `get-request-body-union-member` | census `operation.requestBody:get-union-member` |
| `allof-parent-request-body` | census `mediaType.schema:allof-parent-body` |
| `request-example-nested-null` | census `mediaType.example:nested-null-member` |
| `request-example-deprecated-property` | census `mediaType.example:deprecated-property` |
| `enum-union-body-example-first-member-value` | census `schema.enum:string-valued`, then a JSON request body `oneOf`/`anyOf` whose first member is a string enum, with no `example` or `examples` |
| `multipart-inline-object-part-json-encoded` | census `requestBody.content`, then a `multipart/form-data` object with a `format: binary` part beside an inline object part declaring `properties` |
| `multipart-part-encoding-charset-tuple` | census `mediaType.encoding.contentType`, then a multipart `encoding.<part>.contentType` naming a `charset` |
| `patch-inline-nullable-unrequired-props-omit` | census `pathItem.patch`, then a PATCH inline JSON object body requiring nothing, every property `nullable: true` |
| `stream-error-status-raises-typed-error` | census `response.content`, then a `200` `text/event-stream` beside a `400` JSON body typed `string` |
| `string-body-example-backslash-escaped` | census `mediaType.example`, then a JSON request body typed `string` whose example holds a backslash |
| `allof-body-example-id-field-order` | census `schema.allOf`, then a JSON request body `$ref` to an `allOf` of a `$ref` base declaring `required` and `properties` and an inline member declaring both |
| `binary-download-with-body-has-no-example` | census `operation.requestBody`, then the first `POST`, its every `2xx` a JSON-like `format: binary` string, with a required JSON body requiring a property and an operation after it |
| `example-imports-case-insensitive-order` | census `schema.$ref`, then a JSON request body requiring a property `$ref` to a component named before `AsyncFernApi` byte-wise and after it ignoring case |
| `readme-multipart-file-params-listed-first` | census `requestBody.content`, then a `multipart/form-data` object requiring a scalar part declared before a required `format: binary` part |
| `readme-multipart-optional-file-params` | census `requestBody.content`, then the first operation's `multipart/form-data` object with a required and an optional `format: binary` part, neither with an `encoding.contentType` |
| `readme-streaming-snippet-omits-type-import` | census `operation.x-fern-streaming`, then the README's streaming call constructing a model |
| `response-without-description-blank-line` | census `operation.responses`, then a `2xx` response with JSON-like content and no `description` key |
| `text-response-drops-request-example` | census `mediaType.examples`, then a JSON request with named `examples` on an operation whose `2xx` content is exactly `text/plain` |
| `multipart-optional-enum-part-plain-field` | census `operation.requestBody:optional-nullable-enum-multipart-part` |
| `combo-inline-body-read-only-property` | census `requestBody.content>mediaType.schema>schema.properties>schema.readOnly`, and the instrumented crozier run executes `resolve_request_body`'s read-only retain predicate |
| `server-default-url-templated` | census `server.x-fern-default-url:templated` |
| `server-name-several` | census `server.x-fern-server-name:several-undescribed` |
| `operation-servers-named` | census `operation.servers:named-beside-document-server` |
| `operation-id-untagged-list-or-set` | census `operation.operationId:untagged-list-or-set` |
| `operation-id-hyphenated-tag-method` | census `operation.operationId:hyphenated-tag-method` |
| `operation-id-all-caps-tag-split-prefix` | census `operation.operationId:all-caps-tag-split-prefix` |
| `operation-empty-tag` | census `operation.tags:empty-string` |
| `empty-path-segment-double-slash-kept` | census `openapi.paths:several-template-expressions`, then a templated Paths key containing `//` |
| `group-path-ending-in-api-nested-package` | census `operation.x-fern-sdk-group-name`, then a group name of two segments, the last `api` |
| `readme-endpoint-prefers-argless-non-get` | census `pathItem.put`, then no `POST`, the first operation an argument-free `GET` and a later one an argument-free non-`GET`, and the README demonstrating that later one |
| `readme-nested-group-post-preferred` | census `operation.x-fern-sdk-group-name`, then every `POST` in a group name of two or more segments |
| `camel-case-tag-group-and-prefix` | census `operation.operationId:camel-case-tag-prefix` |
| `combo-body-property-named-as-path-param` | census `operation.requestBody&operation.requestBody:property-named-as-path-parameter`, and the instrumented run executes `rename_claimed_path_params`'s spread branch |
| `combo-body-property-named-as-header-param` | census `operation.requestBody&operation.requestBody:property-named-as-header-parameter` (a co-occurrence row: the declaration with a byte-matched golden) |
| `combo-success-oneof-nullable` | census `operation.context:success-nullable&operation.context:success-oneof`, and the instrumented run executes `build_endpoint`'s `Some(if dropped_null {` branch |
| `combo-success-anyof-nullable` | census `operation.context:success-anyof&operation.context:success-nullable`, and the instrumented run executes `build_endpoint`'s `Some(if dropped_null {` branch |
| `response-description` arm | the instrumented crozier run executes `src/emit.rs::push_return_doc[=None => \{\}]` |
| `media-type-event-stream` arm | the instrumented crozier run executes `src/emit.rs::raw_stream_method[StreamProtocol::Sse \{ terminator, events \} if !events\.is_empty\(\) => \{]` |
| `media-type-event-stream` arm | the instrumented crozier run executes `src/ir.rs::sse_event_dispatch[if !discriminator\.mapping\.is_empty\(\) \{]` |
| `request-body-content` arm | the instrumented crozier run executes `src/ir.rs::resolve_request_body[if let Some\(own\) = fields$]` |
| `request-body-content` arm | the instrumented crozier run executes `src/ir.rs::resolve_request_body[if is_optional\(target\) \&\&]` |
| `request-body-content` arm | the instrumented crozier run executes `src/ir.rs::resolve_request_body[let own_count = fields\.len\(\)]` |
| `media-type-form-urlencoded` arm | the instrumented crozier run executes `src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` |
| `media-type-multipart` arm | the instrumented crozier run executes `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` |
| `media-type-multipart` arm | the instrumented crozier run executes `src/emit.rs::Imports::json_module[=^ {12}self\.json_module_alias = true;$]` |
| `request-body-content` arm | the instrumented crozier run executes `src/name_refusals.rs::validate_ir[=body\.content\.len\(\) == 1]` |
| `request-body-content` arm | the instrumented crozier run executes `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` |
| `request-body-content` arm | the instrumented crozier run executes `src/ir.rs::request_media_variants[let mut view = op\.with_sdk_method_name]` |
| `request-body-content` arm | the instrumented crozier run executes `src/openapi.rs::Operation::with_sdk_method_name` |
| `media-type-malformed-key` arm | the instrumented crozier run executes `src/ir.rs::has_dispatchable_media[=^ {16}return true;$]` |
| `media-type-multipart` arm | the instrumented crozier run executes `src/ir.rs::nullable_enum_part[    member$]` |

## The real witnesses

Each is a registered corpus row whose complete certified-pair golden crozier byte-matches in both enum modes,
wired into the e2e gate as `<name>_matches_fern_output` and the literals overlay gate.

| target | witness |
|---|---|
| `request-example-nested-null` | corpus row 2801, `dystore-api` |
| `response-without-description-blank-line` | corpus row 4200, `amrc-acs-directory` |
| `allof-body-example-id-field-order` | corpus row 4205, `jobster-api` |
| `camel-case-tag-group-and-prefix` | corpus row 4206, `kompaz-web-frontend` |
| `media-type-event-stream-event-dispatch` | corpus row 4207, `synthwerk-llm` |
| `operation-id-hyphenated-tag-method` | corpus row 4208, `parcelis-api` |
| `patch-inline-nullable-unrequired-props-omit` | corpus row 4209, `blufiles-api` |
| `request-body-described-inline-scalar` | corpus row 4210, `tuxedo-dapp` |
| `response-contentless-200-with-created` | corpus row 4211, `osparc-director-v2` |
| `response-description` arm `src/emit.rs::push_return_doc[=None => \{\}]` | corpus row 4200, `amrc-acs-directory` |
| `media-type-event-stream` arm `src/emit.rs::raw_stream_method[StreamProtocol::Sse \{ terminator, events \} if !events\.is_empty\(\) => \{]` | corpus row 4207, `synthwerk-llm` |
| `media-type-event-stream` arm `src/ir.rs::sse_event_dispatch[if !discriminator\.mapping\.is_empty\(\) \{]` | corpus row 4207, `synthwerk-llm` |
| `media-type-form-urlencoded` arm `src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | corpus row 4201, `ummaya-agent-delegation` |
| `request-body-content` arm `src/name_refusals.rs::validate_ir[=body\.content\.len\(\) == 1]` | corpus row 4204, `openparser-ocr` |
| `request-body-content` arm `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | corpus row 4203, `openiap-opencore` |
| `media-type-multipart` arm `src/ir.rs::nullable_enum_part[    member$]` | corpus row 4202, `speech-ai-forge` |

## Verdicts

One line per open feature or combination target; `census.tsv` names every declarer and its screening outcome.

| key | verdict | declarers | outstanding |
|---|---|---:|---|
| `media-type-event-stream-binary-schema` | `exhausted` | 3 | every one of the 3 declarer(s) is decided and the live window was read whole |
| `media-type-event-stream-inline-const-union` | `exhausted` | 1 | every one of the 1 declarer(s) is decided and the live window was read whole |
| `media-type-event-stream-item-schema` | `search-incomplete` | 6 | GitHub reported 3604 results for `"text/event-stream" "itemSchema"` and its first 300 were read |
| `response-status-space-suffixed` | `search-incomplete` | 6 | 2 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv |
| `get-request-body-union-member` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `allof-parent-request-body` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `request-example-deprecated-property` | `search-incomplete` | 300 | 6 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv; no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `enum-union-body-example-first-member-value` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `multipart-inline-object-part-json-encoded` | `search-incomplete` | 37 | 11 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv; no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `multipart-part-encoding-charset-tuple` | `search-incomplete` | 6 | GitHub reported 418 results for `"multipart/form-data" "encoding:" "contentType:" "charset="` and its first 300 were read; GitHub reported 312 results for `"multipart/form-data" "\"encoding\"" "\"contentType\"" "charset="` and its first 300 were read |
| `stream-error-status-raises-typed-error` | `exhausted` | 0 | every one of the 0 declarer(s) is decided and the live window was read whole |
| `string-body-example-backslash-escaped` | `search-incomplete` | 0 | GitHub reported 135 results for `"requestBody:" "type: string" "example:" "\\n" "text/plain" path:openapi` and its first 133 were read |
| `binary-download-with-body-has-no-example` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `example-imports-case-insensitive-order` | `search-incomplete` | 2 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `readme-multipart-file-params-listed-first` | `search-incomplete` | 134 | 63 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv; no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `readme-multipart-optional-file-params` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `readme-streaming-snippet-omits-type-import` | `search-incomplete` | 57 | 8 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv |
| `text-response-drops-request-example` | `search-incomplete` | 6 | 1 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv |
| `multipart-optional-enum-part-plain-field` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `server-default-url-templated` | `exhausted` | 9 | every one of the 9 declarer(s) is decided and the live window was read whole |
| `server-name-several` | `search-incomplete` | 47 | 4 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv; GitHub reported 411 results for `"x-fern-server-name" "servers"` and its first 300 were read |
| `operation-servers-named` | `search-incomplete` | 8 | 1 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv; GitHub reported 303 results for `"x-fern-server-name" "operationId"` and its first 300 were read |
| `operation-id-untagged-list-or-set` | `search-incomplete` | 18 | 2 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv; no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `operation-id-all-caps-tag-split-prefix` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `operation-empty-tag` | `exhausted` | 10 | every one of the 10 declarer(s) is decided and the live window was read whole |
| `empty-path-segment-double-slash-kept` | `search-incomplete` | 3 | GitHub reported 683 results for `"paths:" "//{" path:openapi` and its first 300 were read |
| `group-path-ending-in-api-nested-package` | `search-incomplete` | 0 | GitHub reported 2692 results for `"x-fern-sdk-group-name" "api"` and its first 300 were read |
| `readme-endpoint-prefers-argless-non-get` | `search-incomplete` | 7 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `readme-nested-group-post-preferred` | `search-incomplete` | 3 | GitHub reported 1548 results for `"x-fern-sdk-group-name" "post"` and its first 300 were read |
| `combo-body-property-named-as-path-param` | `search-incomplete` | 1487 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `combo-body-property-named-as-header-param` | `search-incomplete` | 7 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `combo-success-oneof-nullable` | `search-incomplete` | 27 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `combo-success-anyof-nullable` | `search-incomplete` | 82 | 1 admissible declarer(s) not generated against the certified pair in this dispatch, each named in census.tsv; no live GitHub query phrasing reaches the shape, so only the acquired pools were read |

## Arm verdicts

One line per open arm; its declarers are the documents whose instrumented crozier run executes it.

| key | verdict | arm | declarers | outstanding |
|---|---|---|---:|---|
| `request-body-content` | `search-incomplete` | `src/ir.rs::resolve_request_body[if let Some\(own\) = fields$]` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `request-body-content` | `search-incomplete` | `src/ir.rs::resolve_request_body[if is_optional\(target\) \&\&]` | 8 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `request-body-content` | `search-incomplete` | `src/ir.rs::resolve_request_body[let own_count = fields\.len\(\)]` | 3 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `media-type-multipart` | `search-incomplete` | `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `media-type-multipart` | `search-incomplete` | `src/emit.rs::Imports::json_module[=^ {12}self\.json_module_alias = true;$]` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `media-type-malformed-key` | `search-incomplete` | `src/ir.rs::has_dispatchable_media[=^ {16}return true;$]` | 0 | GitHub reported 9344 results for `"content:" "json:" "schema:" "responses:" path:openapi language:YAML` and its first 300 were read |

## Exhausted arms

Open arms whose every declarer is decided and whose live window was read whole.

| key | verdict | arm | declarers | outstanding |
|---|---|---|---:|---|
| `request-body-content` | `exhausted` | `src/ir.rs::request_media_variants[let mut view = op\.with_sdk_method_name]` | 3 | every one of the 3 declarer(s) is decided and the live window was read whole |
| `request-body-content` | `exhausted` | `src/openapi.rs::Operation::with_sdk_method_name` | 3 | every one of the 3 declarer(s) is decided and the live window was read whole |

## Blocked witnesses

| key | candidate | files still mismatched | unrelated shapes |
|---|---|---|---|
| `combo-inline-body-read-only-property` | `webflow-v2` | 47 | registered, it declares and reaches the branch, and `WEBFLOW_V2.unmatched` still lists 47 files: collection-field union selection, worked examples and a query enum, none of them the read-only body |

## Renewed search

Every open target, and why no declarer this search found is registrable.

| key | outcome | why |
|---|---|---|
| `media-type-event-stream-binary-schema` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `media-type-event-stream-inline-const-union` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `media-type-event-stream-item-schema` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `response-status-space-suffixed` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `get-request-body-union-member` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `allof-parent-request-body` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `request-example-deprecated-property` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `enum-union-body-example-first-member-value` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `multipart-inline-object-part-json-encoded` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `multipart-part-encoding-charset-tuple` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `stream-error-status-raises-typed-error` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `string-body-example-backslash-escaped` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `binary-download-with-body-has-no-example` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `example-imports-case-insensitive-order` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `readme-multipart-file-params-listed-first` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `readme-multipart-optional-file-params` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `readme-streaming-snippet-omits-type-import` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `text-response-drops-request-example` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `multipart-optional-enum-part-plain-field` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `server-default-url-templated` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `server-name-several` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `operation-servers-named` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `operation-id-untagged-list-or-set` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `operation-id-all-caps-tag-split-prefix` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `operation-empty-tag` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `empty-path-segment-double-slash-kept` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `group-path-ending-in-api-nested-package` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `readme-endpoint-prefers-argless-non-get` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `readme-nested-group-post-preferred` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `combo-body-property-named-as-path-param` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `combo-body-property-named-as-header-param` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `combo-success-oneof-nullable` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `combo-success-anyof-nullable` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `request-body-content` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `media-type-multipart` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `media-type-malformed-key` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |

## Superseded fixtures

The hand-written fixtures a registered witness superseded leave
`docs/openapi-surface/handwritten/`. Those that tests, measurements or a
departure's evidence read as inputs are kept, bytes unchanged and without an
`evidence.toml`, under
[`../../fern-measurements/superseded-fixtures/`](../../fern-measurements/superseded-fixtures/README.md),
which lists the row that superseded each. `transcript-format-part` keeps its
feature-level cover and loses only its `nullable_enum_part` arm cover.

## Not counted as real witnesses

- Registered rows 3473 (`openapitools-csharp-allof`) and 3474
  (`swagger-parser-null-types`) declare `operation-id-untagged-list-or-set`,
  and their byte-matched goldens write the untagged `list` operation as an
  unsuffixed `def list(`. Both are generator test resources, synthetic in the
  way a hand-written fixture is, so under the manager's 2026-10-29 ruling they
  corroborate the fixture's shape but are not the real witness;
  `depot-bin-ledger` stays.
- `tamoss` (corpus row with a byte-matched golden) renders string request
  bodies whose examples hold a newline and quotes, escaped in its worked
  examples; none holds a backslash, so it does not declare
  `string-body-example-backslash-escaped`. None of the 15 documents with a
  newline-only string-body example does either.
- Documents in the generator vendor's own repositories that the live search
  returned were dropped unread under this repository's provenance rule, and
  documents from this repository itself are its own authored fixtures; both
  are counted in `census.tsv` without being screened.

## Arms reached outside the targets

Registering `speech-ai-forge` (corpus row 4202) also made the golden-only tier
execute `format-binary`'s `src/ir.rs::hoist_form_object[if nullable_binary]`
arm, whose only cover was `multipart-nullable-array`. The hand-written gate
retires a cover once a real specification reaches its arm, so that fixture
moved to the superseded fixtures too, and its three scenario-index proofs now
cite its retained trees as measurements.

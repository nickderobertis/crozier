# Witness search for the fixture-only bodies, media and document-path shapes

A bounded search for real specifications that could replace the hand-written
proofs of the `bodies-media` and `document-paths` regions. A target is proven
here only by a registered corpus row whose complete certified-pair golden
(Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) crozier byte-matches
in both enum modes and that declares the feature, or whose instrumented run
executes the target's arm or interaction branch. Every other target ends
`exhausted` or `search-incomplete`, with what is outstanding named below and
every declarer, its site count and its screening outcome in
[`census.tsv`](census.tsv). Where crozier differs from a declarer the
certified pair generates, the difference is not repaired here but handed off,
grouped by root cause under [Handed-off differences](#handed-off-differences),
and the target that declarer would prove reads `search-incomplete`.

The record names one commit of this repository: the base below, the parent of
this branch's first commit, which the target set was computed from. Every
other revision it, `census.tsv` or `handed-off.tsv` names (40-hex, or
abbreviated to seven in a `owner/repo:path@revision` cell) belongs to the repository
written beside it — the APIs.guru `openapi-directory` archive, or the
publisher in a `owner/repo:path@revision` declarer — and so does not resolve
in this repository; identities of this repository's own documents name the
base.

## Targets

Computed from base `1748b794688900b67e630cad6f606f421bb14b3a`: every `handwritten` row of `bodies-media.md` and
`document-paths.md` (combination rows included), no residual-only supplement (neither file has one), and every
arm-level cover of a `golden` row there that `handwritten-reach.tsv` listed.

| key | kind | region | cover at base | state now |
|---|---|---|---|---|
| `request-body-described-inline-scalar` | feature | `bodies-media` | `described-scalar-bodies` | proven: corpus row 4210 |
| `media-type-event-stream-binary-schema` | feature | `bodies-media` | `event-stream-binary-download` | search-incomplete |
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
| `operation-id-untagged-list-or-set` | feature | `document-paths` | `depot-bin-ledger` | proven: corpus row 4212 |
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
| `request-body-content` | arm `src/ir.rs::request_media_variants[let mut view = op\.with_sdk_method_name]` | `bodies-media` | `request-media-methods` | search-incomplete |
| `request-body-content` | arm `src/openapi.rs::Operation::with_sdk_method_name` | `bodies-media` | `request-media-methods` | search-incomplete |
| `media-type-malformed-key` | arm `src/ir.rs::has_dispatchable_media[=^ {16}return true;$]` | `bodies-media` | `slashless-json-response` | search-incomplete |
| `media-type-multipart` | arm `src/ir.rs::nullable_enum_part[    member$]` | `bodies-media` | `transcript-format-part` | proven: corpus row 4202 |

Of the 58 targets, 17 are proven by a registered real witness, 4 read `exhausted`, 36 read `search-incomplete` and 1 reads `witness-blocked`.

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
| the sibling operations-extensions search's live acquisitions, read 2026-10-30 (the 2,210 of its 2,706 documents no population above holds) | each result at the commit GitHub indexed | 2,210 | 267 | 1,042 | 901 |

The populations overlap; 11,022 distinct OpenAPI 3 documents (by SHA-256) were
censused. The sibling's documents were read from its worktree and copied out,
never written there, and re-screened before any further live search; none
yielded a registrable witness (`census.tsv` names each declarer). A cache body names no request, so one with no recorded publisher,
path and revision in an earlier search's ledger or enumeration is counted but
cannot be registered. The earlier acquisitions' identities, and their
hash audit, are those the
[interaction search](../witness-search-interaction-operation-combinations/README.md#populations-read)
recorded.

## Live requests

Every live GitHub request this search made but the one disclosed below went
through `tools/witness-search/rate_limit_guard.py`, the shared response cache
consulted first; the guard's own ledgers are under
`.local/witness-search-fixture-only-bodies-paths/`. 26 query phrasings were
issued, up to their first three result pages, with 30 seconds between
code-search calls.

| bucket | live requests | answered from the cache |
|---|---:|---:|
| `code_search` | 52 | 4 |
| `core` (result contents, repository licences, source verification) | 3287 | 138 |

The guard logged one wait, with the two readings it took while waiting, and
no secondary-limit refusal. The continuation that grouped the handed-off
differences screened no further candidate and made no GitHub request: it
re-compared the retained certified-pair trees offline. No Sourcegraph, Postman, SwaggerHub or GraphQL
request was made.

**One request went outside the guard, and is disclosed here.** At about
2026-10-30T03:32:05Z (seconds after the guarded source checks of corpus rows
4203 and 4204 at 03:31:38Z and 03:31:40Z), a shell command registering those
rows also ran `curl -s -o /dev/null -w '%{http_code}'
https://api.github.com/repos/openiap/opencore`: one unauthenticated `GET`,
added by mistake while checking a licence, whose body was discarded and never
cited. That repository's licence, MPL-2.0, comes from the guarded lookup of the
same URL recorded earlier in `rate-limit-calls.jsonl`. It cannot be guarded
after the fact and was not repeated; every GitHub request after it went
through the guard.

## How a declarer was screened

In this order, the first that applies deciding it:

1. a registered row, whose golden either shows the shape or, read here, does not;
2. this repository's own authored documents, and the generator vendor's own
   repositories (fetched with the other results, counted, and neither
   screened nor named);
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
   engine with every catalogued departure): a byte-match whose golden shows the
   shape is registered unless the target already has a witness, and a
   difference is recorded with the files it touches, and handed off under its
   root causes. An exit 0 whose log reads `Failed to parse openapi document`
   over the empty scaffold is the certified pair's refusal, not a generation. A candidate that was
   not generated says why in `census.tsv`: its target is already proven by a
   named corpus row; or it falls outside the manager's workload bound for this
   search (`readme-multipart-file-params-listed-first`'s 10 smallest declarers
   generated, the rest not), or the second screening pass's two-hour cap,
   begun at 2026-10-30T14:23:11Z. That pass generated all 48 of its candidates by 2026-10-30T15:50:34Z, so
   none was left at the cap.

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
| `operation-id-untagged-list-or-set` | corpus row 4212, `ollama-api` |
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
| `media-type-event-stream-binary-schema` | `search-incomplete` | 3 | every other declarer is decided and the live window was read whole; handed off: 2 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `webr0m/teldrive-nodejs:openapi/teldrive.openapi.yaml@22d9b87` (`example-presence`, `example-value-source`); `Hardonian/Reach:openapi/reach.openapi.yaml@beb7f7f` (`example-presence`) (see [Handed-off differences](#handed-off-differences)) |
| `media-type-event-stream-inline-const-union` | `exhausted` | 1 | every one of the 1 declarer(s) is decided and the live window was read whole |
| `media-type-event-stream-item-schema` | `search-incomplete` | 6 | GitHub reported 3604 results for `"text/event-stream" "itemSchema"` and its first 300 were read |
| `response-status-space-suffixed` | `search-incomplete` | 6 | every other declarer is decided and the live window was read whole; handed off: 2 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `halo-dev/halo:api-docs/openapi/v3_0/apis_uc.api_v1alpha1.json@ead7adf` (`schema-type-resolution`, `request-body-spread-vs-request`, `request-content-type-header`); `halo-dev/halo:api-docs/openapi/v3_0/apis_console.api_v1alpha1.json@ead7adf` (`schema-type-resolution`, `response-type-resolution`, `request-body-spread-vs-request`, `request-content-type-header`, `multipart-empty-body`) (see [Handed-off differences](#handed-off-differences)) |
| `get-request-body-union-member` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `allof-parent-request-body` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `request-example-deprecated-property` | `search-incomplete` | 302 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read; handed off: 2 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `konfig-sdks/openapi-examples:circleci/openapi.yaml@161ab49` (`example-value-source`); `ourofoundation/wrappers:nixtla/timegpt/timegpt-openapi.json@79688dd` (`example-float-repr`) (see [Handed-off differences](#handed-off-differences)) |
| `enum-union-body-example-first-member-value` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `multipart-inline-object-part-json-encoded` | `search-incomplete` | 39 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read; handed off: 5 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `konfig-dev/konfig:sdks/db/intermediate-fixed-specs/ironclad/openapi.yaml@bec3d36` (`auth-shape`, `union-modelling`, `init-import-order`, `description-source`, `example-enum-member`); `jentic/jentic-public-apis:apis/openapi/ironcladapp.com/ironclad/1/openapi.json@eb9d12a` (`auth-shape`, `union-modelling`, `orphan-type-emission`, `init-import-order`, `description-source`, `example-enum-member`); `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/meta/import/input-entry.json@eb9d12a` (`union-modelling`, `media-type-recognition`, `map-value-modelling`, `reference-body-param-doc`, `example-value-source`); `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/openapi.json@eb9d12a` (`union-modelling`, `media-type-recognition`, `map-value-modelling`, `example-value-source`); `landing-ai/ade-cli:openapi.json@d1995ff` (`description-source`) (see [Handed-off differences](#handed-off-differences)) |
| `multipart-part-encoding-charset-tuple` | `search-incomplete` | 6 | GitHub reported 418 results for `"multipart/form-data" "encoding:" "contentType:" "charset="` and its first 300 were read; GitHub reported 312 results for `"multipart/form-data" "\"encoding\"" "\"contentType\"" "charset="` and its first 300 were read |
| `stream-error-status-raises-typed-error` | `exhausted` | 0 | every one of the 0 declarer(s) is decided and the live window was read whole |
| `string-body-example-backslash-escaped` | `search-incomplete` | 1 | GitHub reported 135 results for `"requestBody:" "type: string" "example:" "\\n" "text/plain" path:openapi` and its first 133 were read |
| `binary-download-with-body-has-no-example` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `example-imports-case-insensitive-order` | `search-incomplete` | 2 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `readme-multipart-file-params-listed-first` | `search-incomplete` | 135 | 45 admissible declarer(s) left ungenerated by the manager's workload bound (the 10 smallest were generated), each named in census.tsv; no live GitHub query phrasing reaches the shape, so only the acquired pools were read; handed off: 9 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `EU-UPCAST/profile:openapi/openapi.yaml@3228f86` (`readme-endpoint-choice`); `resemble-ai/resemble-mcp:openapi/openapi.yml@6404fd4` (`reserved-name-suffix`, `example-value-source`); `Skyvern-AI/skyvern:docs/api-reference/openapi.json@b325eb1` (`untagged-operation-grouping`, `readme-endpoint-choice`, `example-value-source`); `ballerina-platform/openapi-connectors:openapi/azure.openai.finetunes/openapi.yaml@7c3840c` (`example-presence`); `clencyc/MozillaFestivalBackend:openapi.yaml@e70f015` (`readme-endpoint-choice`); `crystalshards/monorepo:apps/crystalshards/openapi.yml@f5c7a1d` (`union-modelling`, `init-import-order`, `example-value-source`); `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/meta/import/input-entry.json@eb9d12a` (`union-modelling`, `media-type-recognition`, `map-value-modelling`, `reference-body-param-doc`, `example-value-source`); `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/openapi.json@eb9d12a` (`union-modelling`, `media-type-recognition`, `map-value-modelling`, `example-value-source`); `GravitLauncher/Launcher:openapi.yaml@fef9bae` (`method-name-derivation`, `reserved-name-suffix`) (see [Handed-off differences](#handed-off-differences)) |
| `readme-multipart-optional-file-params` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `readme-streaming-snippet-omits-type-import` | `search-incomplete` | 60 | every other declarer is decided and the live window was read whole; handed off: 2 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `truefoundry/trueforge:docs/openapi.json@47fd7e8` (`allof-description-wrapper`); `truefoundry/trueforge:docs/openapi.json@a718e71` (`allof-description-wrapper`) (see [Handed-off differences](#handed-off-differences)) |
| `text-response-drops-request-example` | `search-incomplete` | 6 | every other declarer is decided and the live window was read whole; handed off: 4 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `ihulsbus/cookbook:docs/k8s/files/openapi.yaml@9be5a60` (`request-content-type-header`, `example-presence`, `example-value-source`); `TouK/nussknacker:docs-internal/api/nu-designer-openapi.yaml@2e8d326` (`union-modelling`, `response-type-resolution`, `request-content-type-header`, `reserved-name-suffix`, `init-import-order`, `example-value-source`); `marcelo-earth/generative-manim:api/public/openapi.yaml@f681cc7` (`streaming-detection`); `SeekStorm/SeekStorm:seekstorm_server/openapi/openapi.yml@50cb0dd` (`parameter-type-resolution`, `description-source`, `example-value-source`, `example-placeholder-shape`) (see [Handed-off differences](#handed-off-differences)) |
| `multipart-optional-enum-part-plain-field` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `server-default-url-templated` | `exhausted` | 9 | every one of the 9 declarer(s) is decided and the live window was read whole |
| `server-name-several` | `search-incomplete` | 47 | GitHub reported 411 results for `"x-fern-server-name" "servers"` and its first 300 were read; handed off: 4 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `tranphita/skyvern:fern/openapi/skyvern_openapi.json@efe6ae1` (`untagged-operation-grouping`); `CryptoTyson/n8n-skyvern:fern/openapi/skyvern_openapi.json@6fcaa74` (`untagged-operation-grouping`); `Skyvern-AI/skyvern:docs/api-reference/openapi.json@b325eb1` (`untagged-operation-grouping`, `readme-endpoint-choice`, `example-value-source`); `Skyvern-AI/skyvern:fern/openapi/skyvern_openapi.json@b325eb1` (`untagged-operation-grouping`, `type-placement`, `readme-endpoint-choice`) (see [Handed-off differences](#handed-off-differences)) |
| `operation-servers-named` | `search-incomplete` | 8 | GitHub reported 303 results for `"x-fern-server-name" "operationId"` and its first 300 were read; handed off: 1 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `resemble-ai/resemble-mcp:openapi/openapi.yml@6404fd4` (`reserved-name-suffix`, `example-value-source`) (see [Handed-off differences](#handed-off-differences)) |
| `operation-id-all-caps-tag-split-prefix` | `search-incomplete` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `operation-empty-tag` | `exhausted` | 10 | every one of the 10 declarer(s) is decided and the live window was read whole |
| `empty-path-segment-double-slash-kept` | `search-incomplete` | 4 | GitHub reported 683 results for `"paths:" "//{" path:openapi` and its first 300 were read |
| `group-path-ending-in-api-nested-package` | `search-incomplete` | 1 | GitHub reported 2692 results for `"x-fern-sdk-group-name" "api"` and its first 300 were read |
| `readme-endpoint-prefers-argless-non-get` | `search-incomplete` | 7 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read; handed off: 2 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `radio-aktywne/jasmine:openapi/numbat.yaml@9e8b7f6` (`union-modelling`, `parameter-type-resolution`, `response-type-resolution`, `method-name-derivation`); `radio-aktywne/magnolia:openapi/gecko.yaml@51d280e` (`union-modelling`, `parameter-type-resolution`, `response-type-resolution`, `method-name-derivation`) (see [Handed-off differences](#handed-off-differences)) |
| `readme-nested-group-post-preferred` | `search-incomplete` | 5 | GitHub reported 1548 results for `"x-fern-sdk-group-name" "post"` and its first 300 were read; handed off: 2 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/source/source.dat@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`); `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/import/output-bundle.json@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`) (see [Handed-off differences](#handed-off-differences)) |
| `combo-body-property-named-as-path-param` | `search-incomplete` | 1487 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `combo-body-property-named-as-header-param` | `search-incomplete` | 7 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `combo-success-oneof-nullable` | `search-incomplete` | 27 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `combo-success-anyof-nullable` | `search-incomplete` | 84 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read; handed off: 1 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `msgbyte/tianji:website/static/openapi.json@20124bb` (`union-modelling`, `response-type-resolution`, `map-value-modelling`, `method-name-derivation`) (see [Handed-off differences](#handed-off-differences)) |

## Arm verdicts

One line per open arm; its declarers are the documents whose instrumented crozier run executes it.

| key | verdict | arm | declarers | outstanding |
|---|---|---|---:|---|
| `request-body-content` | `search-incomplete` | `src/ir.rs::resolve_request_body[if let Some\(own\) = fields$]` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `request-body-content` | `search-incomplete` | `src/ir.rs::resolve_request_body[if is_optional\(target\) \&\&]` | 8 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `request-body-content` | `search-incomplete` | `src/ir.rs::resolve_request_body[let own_count = fields\.len\(\)]` | 3 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read; handed off: 2 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `codosseum-org/backend:openapi.yaml@a92699b` (`union-modelling`); `aldinokemal/go-whatsapp-web-multidevice:docs/openapi.yaml@831a851` (`method-name-derivation`, `example-value-source`) (see [Handed-off differences](#handed-off-differences)) |
| `media-type-multipart` | `search-incomplete` | `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `media-type-multipart` | `search-incomplete` | `src/emit.rs::Imports::json_module[=^ {12}self\.json_module_alias = true;$]` | 0 | no live GitHub query phrasing reaches the shape, so only the acquired pools were read |
| `media-type-malformed-key` | `search-incomplete` | `src/ir.rs::has_dispatchable_media[=^ {16}return true;$]` | 0 | GitHub reported 9344 results for `"content:" "json:" "schema:" "responses:" path:openapi language:YAML` and its first 300 were read |
| `request-body-content` | `search-incomplete` | `src/ir.rs::request_media_variants[let mut view = op\.with_sdk_method_name]` | 3 | every other declarer is decided and the live window was read whole; handed off: 2 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/source/source.dat@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`); `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/import/output-bundle.json@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`) (see [Handed-off differences](#handed-off-differences)) |
| `request-body-content` | `search-incomplete` | `src/openapi.rs::Operation::with_sdk_method_name` | 3 | every other declarer is decided and the live window was read whole; handed off: 2 admissible declarer(s) the certified pair generates differ from crozier, each stopped by the root causes named — `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/source/source.dat@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`); `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/import/output-bundle.json@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`) (see [Handed-off differences](#handed-off-differences)) |

## Blocked witnesses

| key | candidate | files still mismatched | unrelated shapes |
|---|---|---|---|
| `combo-inline-body-read-only-property` | `webflow-v2` | 47 | registered, it declares and reaches the branch, and `WEBFLOW_V2.unmatched` still lists 47 files: collection-field union selection, worked examples and a query enum, none of them the read-only body |
| `combo-inline-body-read-only-property` | `whatwatt-ch/whatwatt-go-documentation:openapi/api-clean.yaml@50340b0865809c2e6f831385ccfdc900af58981b` | 8 | admissible and generated by the certified pair, it declares the combination, and crozier differs from it in 8 file(s) under handed-off root causes (`orphan-type-emission`, `init-import-order`, `example-presence`), none of them the read-only body |
| `combo-inline-body-read-only-property` | `whatwatt-ch/whatwatt-go-documentation:openapi/api-complete-bundle.yaml@50340b0865809c2e6f831385ccfdc900af58981b` | 8 | admissible and generated by the certified pair, it declares the combination, and crozier differs from it in 8 file(s) under handed-off root causes (`orphan-type-emission`, `init-import-order`, `example-presence`), none of them the read-only body |
| `combo-inline-body-read-only-property` | `APIs-guru/openapi-directory:APIs/osf.io/2.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | 520 | admissible and generated by the certified pair, it declares the combination, and crozier differs from it in 520 file(s) under handed-off root causes (`media-type-recognition`, `orphan-type-emission`, `reference-section-title`, `snippet-rendering`), none of them the read-only body |

## Renewed search

Every open target, and why no declarer this search found is registrable.

| key | outcome | why |
|---|---|---|
| `media-type-event-stream-binary-schema` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `webr0m/teldrive-nodejs:openapi/teldrive.openapi.yaml@22d9b87` (`example-presence`, `example-value-source`); `Hardonian/Reach:openapi/reach.openapi.yaml@beb7f7f` (`example-presence`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `media-type-event-stream-inline-const-union` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `media-type-event-stream-item-schema` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `response-status-space-suffixed` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `halo-dev/halo:api-docs/openapi/v3_0/apis_uc.api_v1alpha1.json@ead7adf` (`schema-type-resolution`, `request-body-spread-vs-request`, `request-content-type-header`); `halo-dev/halo:api-docs/openapi/v3_0/apis_console.api_v1alpha1.json@ead7adf` (`schema-type-resolution`, `response-type-resolution`, `request-body-spread-vs-request`, `request-content-type-header`, `multipart-empty-body`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `get-request-body-union-member` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `allof-parent-request-body` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `request-example-deprecated-property` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `konfig-sdks/openapi-examples:circleci/openapi.yaml@161ab49` (`example-value-source`); `ourofoundation/wrappers:nixtla/timegpt/timegpt-openapi.json@79688dd` (`example-float-repr`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `enum-union-body-example-first-member-value` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `multipart-inline-object-part-json-encoded` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `konfig-dev/konfig:sdks/db/intermediate-fixed-specs/ironclad/openapi.yaml@bec3d36` (`auth-shape`, `union-modelling`, `init-import-order`, `description-source`, `example-enum-member`); `jentic/jentic-public-apis:apis/openapi/ironcladapp.com/ironclad/1/openapi.json@eb9d12a` (`auth-shape`, `union-modelling`, `orphan-type-emission`, `init-import-order`, `description-source`, `example-enum-member`); `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/meta/import/input-entry.json@eb9d12a` (`union-modelling`, `media-type-recognition`, `map-value-modelling`, `reference-body-param-doc`, `example-value-source`); `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/openapi.json@eb9d12a` (`union-modelling`, `media-type-recognition`, `map-value-modelling`, `example-value-source`); `landing-ai/ade-cli:openapi.json@d1995ff` (`description-source`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `multipart-part-encoding-charset-tuple` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `stream-error-status-raises-typed-error` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `string-body-example-backslash-escaped` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `binary-download-with-body-has-no-example` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `example-imports-case-insensitive-order` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `readme-multipart-file-params-listed-first` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `EU-UPCAST/profile:openapi/openapi.yaml@3228f86` (`readme-endpoint-choice`); `resemble-ai/resemble-mcp:openapi/openapi.yml@6404fd4` (`reserved-name-suffix`, `example-value-source`); `Skyvern-AI/skyvern:docs/api-reference/openapi.json@b325eb1` (`untagged-operation-grouping`, `readme-endpoint-choice`, `example-value-source`); `ballerina-platform/openapi-connectors:openapi/azure.openai.finetunes/openapi.yaml@7c3840c` (`example-presence`); `clencyc/MozillaFestivalBackend:openapi.yaml@e70f015` (`readme-endpoint-choice`); `crystalshards/monorepo:apps/crystalshards/openapi.yml@f5c7a1d` (`union-modelling`, `init-import-order`, `example-value-source`); `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/meta/import/input-entry.json@eb9d12a` (`union-modelling`, `media-type-recognition`, `map-value-modelling`, `reference-body-param-doc`, `example-value-source`); `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/openapi.json@eb9d12a` (`union-modelling`, `media-type-recognition`, `map-value-modelling`, `example-value-source`); `GravitLauncher/Launcher:openapi.yaml@fef9bae` (`method-name-derivation`, `reserved-name-suffix`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `readme-multipart-optional-file-params` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `readme-streaming-snippet-omits-type-import` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `truefoundry/trueforge:docs/openapi.json@47fd7e8` (`allof-description-wrapper`); `truefoundry/trueforge:docs/openapi.json@a718e71` (`allof-description-wrapper`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `text-response-drops-request-example` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `ihulsbus/cookbook:docs/k8s/files/openapi.yaml@9be5a60` (`request-content-type-header`, `example-presence`, `example-value-source`); `TouK/nussknacker:docs-internal/api/nu-designer-openapi.yaml@2e8d326` (`union-modelling`, `response-type-resolution`, `request-content-type-header`, `reserved-name-suffix`, `init-import-order`, `example-value-source`); `marcelo-earth/generative-manim:api/public/openapi.yaml@f681cc7` (`streaming-detection`); `SeekStorm/SeekStorm:seekstorm_server/openapi/openapi.yml@50cb0dd` (`parameter-type-resolution`, `description-source`, `example-value-source`, `example-placeholder-shape`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `multipart-optional-enum-part-plain-field` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `server-default-url-templated` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `server-name-several` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `tranphita/skyvern:fern/openapi/skyvern_openapi.json@efe6ae1` (`untagged-operation-grouping`); `CryptoTyson/n8n-skyvern:fern/openapi/skyvern_openapi.json@6fcaa74` (`untagged-operation-grouping`); `Skyvern-AI/skyvern:docs/api-reference/openapi.json@b325eb1` (`untagged-operation-grouping`, `readme-endpoint-choice`, `example-value-source`); `Skyvern-AI/skyvern:fern/openapi/skyvern_openapi.json@b325eb1` (`untagged-operation-grouping`, `type-placement`, `readme-endpoint-choice`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `operation-servers-named` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `resemble-ai/resemble-mcp:openapi/openapi.yml@6404fd4` (`reserved-name-suffix`, `example-value-source`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `operation-id-all-caps-tag-split-prefix` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `operation-empty-tag` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `empty-path-segment-double-slash-kept` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `group-path-ending-in-api-nested-package` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `readme-endpoint-prefers-argless-non-get` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `radio-aktywne/jasmine:openapi/numbat.yaml@9e8b7f6` (`union-modelling`, `parameter-type-resolution`, `response-type-resolution`, `method-name-derivation`); `radio-aktywne/magnolia:openapi/gecko.yaml@51d280e` (`union-modelling`, `parameter-type-resolution`, `response-type-resolution`, `method-name-derivation`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `readme-nested-group-post-preferred` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/source/source.dat@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`); `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/import/output-bundle.json@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `combo-body-property-named-as-path-param` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `combo-body-property-named-as-header-param` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `combo-success-oneof-nullable` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `combo-success-anyof-nullable` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `msgbyte/tianji:website/static/openapi.json@20124bb` (`union-modelling`, `response-type-resolution`, `map-value-modelling`, `method-name-derivation`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `request-body-content` | `none-registrable` | no declarer byte-matches yet: the admissible declarers the certified pair generates differ from crozier under handed-off root causes — `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/source/source.dat@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`); `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/import/output-bundle.json@c72e13e` (`type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling`); `codosseum-org/backend:openapi.yaml@a92699b` (`union-modelling`); `aldinokemal/go-whatsapp-web-multidevice:docs/openapi.yaml@831a851` (`method-name-derivation`, `example-value-source`) — and each becomes registrable once the handed-off repair of its causes lands (see [Handed-off differences](#handed-off-differences)) |
| `media-type-multipart` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |
| `media-type-malformed-key` | `none-registrable` | no declarer is both admissible and byte-matched by the certified pair with the shape shown; see `census.tsv` |

## Handed-off differences

Every candidate `census.tsv` recorded as differing from the certified pair was re-compared on 2026-10-30 with crozier built at this branch's commit `2dc89c1810b3dff315851aa31089caf70323dbe3` (crozier's own history), against the certified-pair tree the screening generated and retained for it, through `crozier compare` with every catalogued departure applied; each document's SHA-256 was re-verified first. All 58 still differ. None is repaired or departed in this record: the manager ruled that those repairs belong to a separate plan, so crozier's output for each is unchanged from this node's base, and no golden or Fern tree was edited. The 58 split three ways:

- 50 are handed off below, together with one more document crozier fails to read while the certified pair generates it (`JHUAPL-DTNMA/dtnma-tools`), 51 in all. One of them, `linux-automation/tacd`, is the certified pair's refusal (its exit 0 writes an empty SDK over a document it failed to parse) that crozier generates in both modes; it is handed off as a refusal-rule difference and is no witness route.
- 7 are no difference: the certified pair's exit 0 was a false success over a document it never parsed (`Failed to parse openapi document`), the class-A refusal the manager's Setu ruling names, and crozier refuses each in the same refusal class. They are listed under [The certified pair's false successes](#the-certified-pairs-false-successes).
- 1 is crozier's own refusal under the standing ruling that a body property named as a query parameter is a defect: [crozier's ruled refusal](#croziers-ruled-refusal).

A candidate below is stopped only by its root causes: each is admissible and declares its target, and becomes registrable once the handed-off repair of every cause it lists lands and a fresh certified-pair generation byte-matches. The full file list and first differing line pair of each document are in [`handed-off.tsv`](handed-off.tsv) beside this record.

### Root causes

Each states the rule crozier and the certified pair apply differently. A document counts under every cause its diff shows.

| root cause | rule | documents |
|---|---|---:|
| `refusal-null-media-type` | A Media Type Object written as `null` (`image/png:` with no value): the certified pair's parser fails on it (`Cannot read properties of null (reading 'schema')`) and exits 0 with an empty SDK, so it refuses the document; crozier reads the entry as empty and generates, in both default and `fern-strict` modes. | 1 |
| `bare-string-parameter-example` | A parameter `examples` map entry that is a bare string rather than an Example Object or Reference Object: the certified pair generates the document; crozier fails to read it (`invalid type: string ..., expected struct ParameterExample`) and writes nothing. | 1 |
| `untagged-operation-grouping` | An operation declaring `x-fern-sdk-method-name` without `x-fern-sdk-group-name`: the certified pair puts its method on the root client whatever its `tags`; crozier still groups it under its first tag, so the method, its inline types and the README's chosen call move package. | 4 |
| `type-placement` | Where an inline type lands: the certified pair writes a root-client method's inline types into root `types/` and an inline enum from a `components.parameters` entry shared across packages into each using operation's package; crozier writes the first into the tag package and hoists the second to root `types/`. | 3 |
| `inline-type-naming` | An operation split into two methods by per-media-type `x-fern-sdk-method-name`: the certified pair names the shared inline parameter and response types once, from the base operation (`TranscribeMediaRequest*`); crozier names a copy per split method (`TranscribeUrlMediaRequest*`). | 2 |
| `subpackage-order` | Nested sub-client order: the certified pair orders a group's children by the first operation that belongs directly to each child (children with only nested operations last); crozier orders them by the first descendant operation. | 2 |
| `environment-shape` | Several servers named with `x-fern-server-name` (on path items, or at the top level beside per-path servers): the certified pair builds a multi-URL environment class, keeps `environment` in the client wrapper and passes `base_url=...get_environment().<name>` per request; crozier writes a single-URL environment enum and a `base_url` client argument. | 2 |
| `auth-shape` | Security schemes: the certified pair prefixes `Bearer ` for an `apiKey` in header `Authorization` carrying `x-bearer-format: bearer` and emits one constructor argument for two `apiKey` schemes naming one header; crozier sends the raw key and duplicates the second header's argument, assignment and docstring entry. | 3 |
| `union-modelling` | oneOf/anyOf modelling: the certified pair infers a discriminated union from a property every variant declares as a single-member enum (inline or through `$ref`, required or not) but not from a `const`-only property, and collapses a union of identical or single primitive members (and a nullable multi-type array with `additionalProperties`) its own way; crozier infers the discriminant from `const` and not from single-member enums, and writes union aliases where the certified pair collapses (and the reverse for the multi-type `type` array). | 12 |
| `schema-type-resolution` | A schema declaring `type: array` with `items: {$ref}` and a stray `properties` map: the certified pair types it `List[Item]`; crozier models a new object type named after the property. | 2 |
| `allof-description-wrapper` | `allOf: [{$ref: X}, {description or nullable only}]`: the certified pair resolves it to X's own type (`str` for a string X) carrying X's description; crozier types such a parameter `typing.Any` and mints a new alias type for such a property. | 3 |
| `parameter-type-resolution` | Parameter and body element types: a query parameter `oneOf: [anyOf: [$ref X, string with contentSchema X], null]` is `Union[Optional[X], str]` in the certified pair and `Union[X, str]` in crozier; a tuple array (`items: false` with `prefixItems`) is `Sequence[Any]` in the certified pair and `Sequence[Optional[Any]]` in crozier. | 3 |
| `response-type-resolution` | Response typing: the certified pair types an operation from its first 2xx response (a schema-less one gives `typing.Any`), honours OAS 3.0 `nullable` and `anyOf [..., null]` on a response as `Optional`, hoists an inline string-enum or `const` response into a named enum, reads `*/*` before a schema-less `application/json` entry, and keeps an error class body `str`; crozier skips the schema-less 2xx, drops the response nullability, writes `Union[Literal[...], Any]`, prefers the schema-less entry and widens the error body to `typing.Any`, and its reference.md says `Iterator[str]` for a string SSE stream both clients type `Iterator[bytes]`. | 8 |
| `streaming-detection` | An operation with a 200 `application/json` response and a second 2xx `text/event-stream` response: the certified pair makes the whole method an SSE stream typed from the 200 schema (and adds a README Streaming section); crozier reads only the 200 and emits a plain call. | 1 |
| `media-type-recognition` | JSON media types: the certified pair treats a `text/json` or case-variant `Application/json` request body and a `*/*` response as JSON (spreading the body, typing the response from its schema); crozier recognises only lower-case `application/...json`, so it drops those bodies and types those responses `typing.Any`. | 4 |
| `map-value-modelling` | An inline `additionalProperties` schema: the certified pair hoists a named `<Parent>Value` model when the schema declares `type: object` (response maps included) and types a properties-only one `typing.Any`; crozier does the reverse. | 4 |
| `orphan-type-emission` | Which schemas get a model file: crozier writes types the certified pair does not (the JSON alternative's inline types beside a binary response, one of two identical once-referenced body components, inline read-only or dropped body properties) and omits component models referenced only by bytes-typed bodies, which the certified pair writes. | 5 |
| `request-body-spread-vs-request` | A component schema referenced once, as a `*/*` or multipart request body: the certified pair inlines it (no type file; reference.md lists the spread properties); crozier spreads it in the signature too but also writes the named model and documents `request: Model`. | 2 |
| `reference-body-param-doc` | reference.md's body parameter list: for a body `$ref` to an alias of an object the certified pair lists `request: <Alias>` where crozier lists the spread properties; for an octet-stream body beside JSON types it documents the bytes union where crozier documents the schema name. | 3 |
| `request-content-type-header` | The raw client's explicit `content-type` header: crozier adds `application/json` for a spread `*/*` body on an operation with a path parameter and for a named discriminated-union body, where the certified pair adds none; the certified pair keeps it for a vendor `+json` body, for a titled component body that is also a response, and for a described inline body offered as JSON and YAML, where crozier drops it. | 6 |
| `request-body-optionality` | A `required: false` JSON body whose schema is a property-less object: the certified pair keeps `request` required; crozier makes it `Optional[...] = None`. | 1 |
| `body-property-set` | An `allOf` body whose inline member also carries its own `anyOf` of required-only branches: the certified pair drops that member's properties and keeps the `$ref` base's; crozier merges them into the body. | 1 |
| `multipart-empty-body` | A multipart body referencing an object with no properties: the certified pair's raw client sends `data={}, files={}`; crozier sends only `files={}`. | 1 |
| `path-param-serialization` | A path parameter typed `oneOf: [string with pattern, integer]`: the certified pair serializes it through `convert_and_respect_annotation_metadata(..., annotation=<Alias>)`; crozier writes `encode_path_param(id)`. | 1 |
| `method-name-derivation` | Method names: the certified pair keeps a PascalCase operationId that starts with its tag whole (`PingPing` gives `ping_ping`), strips a lower-case tag prefix before `Info` (`appInfo` gives `info`), keeps a hyphenated leading segment that only starts with the tag, lower-cases a camelCase trailing segment unsplit, splits a summary's `robots.txt` at the dot and merges `e.g. a` into `ega`; crozier does the opposite in each case. | 6 |
| `reserved-name-suffix` | Name suffixing: the certified pair renames a path parameter `uuid` to `uuid_` on every operation, a property `dict` to `dict_`, and the later of two wire names sanitizing to one field name with `_`; crozier suffixes `uuid` only on operations without a JSON body and leaves the other two unsuffixed. | 3 |
| `init-import-order` | `__init__.py` export order: the certified pair orders the TYPE_CHECKING imports by module path (the root's `.client`, `.environment`, `.version` among the subpackages, and a union's module as one statement); crozier orders by exported name (client and environment first, version last). The catalogued `init-type-checking-import-order` departure absorbs only a pure permutation, so it stays unapplied where the same block also differs in names. | 7 |
| `description-source` | Docstring sources: the certified pair writes an empty class docstring for `description: ""`, takes a hoisted nullable inline object's docstring from the inner object, drops a description beside a `$ref` inside a `oneOf` member and keeps an `allOf` member's description on an alias; crozier treats the empty description as absent, uses the outer description, lifts the member's description and writes none for the alias. | 5 |
| `reference-section-title` | reference.md section titles: for operations grouped by a snake_case operationId prefix spelling a declared multi-word tag, the certified pair titles the section with the tag verbatim (`Draft Registrations`); crozier PascalCases the prefix. | 1 |
| `snippet-rendering` | README and reference.md usage snippets: the certified pair omits a client-level header argument from the client construction, names a query parameter whose wire name ends in `[]` `<name>_array`, and prints a free-form object body's top-level values unwrapped; crozier adds the argument, uses the signature name and wraps at the snippet width. | 2 |
| `readme-endpoint-choice` | The README's demonstrated call: the certified pair takes the first POST even when its body is multipart with a file part (required or a nullable optional one); crozier treats such a POST as ineligible and falls back to the next eligible operation. Where the grouping differs, the chosen call differs with it. | 5 |
| `example-presence` | Whether an operation gets a usage example: the certified pair writes one for an argument-less binary GET that declares error responses and for a multipart body whose only part is an optional file with a named example, and writes none (`client.x.y(...)` in reference.md) for a binary download declaring no error or a multipart body whose only part is a required file; crozier does the opposite in each case. | 7 |
| `example-value-source` | Worked-example values. The certified pair writes its own placeholder where crozier writes a declared example or a format or pattern constant: a multipart text part's or nested multipart object's property `example`, a binary download's query parameter `example`, a `$ref`'d date-time schema's `examples`, a top-level array body's media-type example (two synthesized items instead), a `format: uri` or pattern-only string, every path parameter of an operation where one has `schema: {}`, and a union-typed value (its first variant's required members). It writes a declared or derived value where crozier writes its own placeholder: an array body's or map property's schema-level `example`, an array query parameter's `example`, a media type's named example for an enum field, a declared example that mistypes its property (replaced by the type placeholder, `1000000` for `int64` and `uint64`), an integer's `maximum`, and a header's camelCased SDK name rather than its wire name. | 16 |
| `example-enum-member` | An array of `$ref`'d string enums whose enum schema declares `example`: the certified pair's worked example takes the first member; crozier takes the declared example. | 2 |
| `example-optional-members` | An optional query parameter whose `$ref`'d schema carries an `examples` array: the certified pair leaves it out of the worked example; crozier includes it. | 1 |
| `example-float-repr` | A declared float example needing 17 significant digits: the certified pair prints the parsed double's shortest round-trip spelling; crozier prints a neighbouring double (the last digit off by one), a precision loss in its float parse or print. | 1 |
| `example-placeholder-shape` | A body `{type: object, additionalProperties: {}}` whose named examples are arrays (they do not fit the schema): both synthesize, the certified pair as `{"string": {"key": "value"}}` and crozier as `{"key": "value"}`. | 1 |

Lines a catalogued departure explains (`multipart-object-required-file-example`, `init-type-checking-import-order`) still count as unexplained in a file another cause also changes, because a departure's rule admits only a file whose every other line matches; they clear with that cause, and are not counted as causes of their own.

### Handed-off documents

`(none: …)` marks a pair whose first differing line exists on one side only.

| document | sha256 | targets | root causes | files | first differing line pair |
|---|---|---|---|---:|---|
| `debezium/debezium-platform:openapi/openapi.yaml@20fd16bf12ac02e750bb770fc4b986afdf824507` | `043f3a5f2fe283197741850d02964865211d10e2af271aa9b344ee7a84507de6` | `response-description src/emit.rs::push_return_doc[=None => \{\}]`; `response-without-description-blank-line` | `example-value-source`, `example-optional-members` | 3 | `reference.md`: certified (none: crozier inserts the line), crozier `import datetime` |
| `EU-UPCAST/profile:openapi/openapi.yaml@3228f86284a88a634b3db5e6a36cce99db31800c` | `09c972eca3b36dae6158cb21cd947cbbdb2fbed4f169b3ce24c24f0bb77f0480` | `readme-multipart-file-params-listed-first` | `readme-endpoint-choice` | 1 | `README.md`: certified `client.generate_profile_for_local_file_with_selected_profiler_profile_generate_profile_post(`, crozier `client.get_available_profilers_profile_get_profilers_get()` |
| `truefoundry/trueforge:docs/openapi.json@47fd7e81f39e66289d9c62ba80c4e7f7b0370d64` | `09fcb1c253845987c65878aa01f03c3cc10eee0d438e1ab22907d453f00c3744` | `readme-streaming-snippet-omits-type-import` | `allof-description-wrapper` | 3 | `reference.md`: certified `` **name:** `str` — Sandbox environment name. ``, crozier `` **name:** `typing.Any` — Sandbox environment name. `` |
| `ihulsbus/cookbook:docs/k8s/files/openapi.yaml@9be5a607c9d09820928575972b1ab83aa90e14af` | `0ac7df49edfe6ef2faeed98cf12fd827871539cd70bddd85967acbef8ca85123` | `text-response-drops-request-example` | `request-content-type-header`, `example-presence`, `example-value-source` | 10 | `reference.md`: certified `from fern import FernApi`, crozier `client.image.update_image(...)` |
| `arawa/workspace:openapi.json@926f6093e68261c94f4dcd536b0c4451f2013ee8` | `0c8259f6f991dbd2985005b14731e7df52d59496a17249394fefcbaa2ef52689` | `patch-inline-nullable-unrequired-props-omit` | `snippet-rendering` | 2 | `README.md`: certified (none: crozier inserts the line), crozier `ocs_api_request="<OCS-APIRequest>",` |
| `tranphita/skyvern:fern/openapi/skyvern_openapi.json@efe6ae1c2088ed6aa1c09268e786fef4136070be` | `0f3a701b83bed92d75c832b566b4549e53683d1e9dafbd57fe79a68b09f18ac5` | `server-name-several` | `untagged-operation-grouping` | 27 | `README.md`: certified `client.run_task(`, crozier `client.agent.run_task(` |
| `CryptoTyson/n8n-skyvern:fern/openapi/skyvern_openapi.json@6fcaa74efb6160921f1c1ef9c8f39f47e242ea07` | `117c4acb2687f08da9f15bc02367f0d8dc144bbdbec5ab3fe933b4065f8b01f5` | `server-name-several` | `untagged-operation-grouping` | 30 | `README.md`: certified `client.run_task(`, crozier `client.agent.run_task(` |
| `msgbyte/tianji:website/static/openapi.json@20124bb953eae609b8b5c003cae48633af3e4207` | `1843a239e5d93eaa9c9906daffcb64748723b6bb155fa9bcb7f3bce53c5f6ce5` | `combo-success-anyof-nullable`; `operation-id-hyphenated-tag-method` | `union-modelling`, `response-type-resolution`, `map-value-modelling`, `method-name-derivation` | 79 | `reference.md`: certified `<details><summary><code>client.ai.<a href="src/fern/ai/client.py">classifysurvey</a>(...) -> AiClassifySurv…`, crozier `<details><summary><code>client.ai.<a href="src/fern/ai/client.py">classifysurvey</a>(...) -> typing.Union[t…` |
| `malach-it/boruta-server:boruta-web.openapi.json@9a32a89c224367a97e8f5af69031bcd8b867ddad` | `26683af54aab78eb9c65cb3640ce65121763d73ef657a81e47b150261f0c3b3b` | `media-type-form-urlencoded src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | `method-name-derivation`, `example-presence` | 3 | `reference.md`: certified `from fern import FernApi`, crozier (none: crozier omits the line) |
| `whatwatt-ch/whatwatt-go-documentation:openapi/api-clean.yaml@50340b0865809c2e6f831385ccfdc900af58981b` | `29ffa2656e29034f5243327dc6152d997d2852348e5c3763eb26ab4f118885a2` | `combo-inline-body-read-only-property` | `orphan-type-emission`, `init-import-order`, `example-presence` | 8 | `reference.md`: certified `client.maintenance.upload_firmware(...)`, crozier `from fern import FernApi` |
| `neo773/macgamingdb:openapi.json@71201d5ed52ab0991854f0eac0d153c076ed2907` | `2af442cee107b3b4ed4b22df18abb18280ef43dd3e1bff5a69743ef680666a81` | `operation-id-hyphenated-tag-method` | `response-type-resolution` | 7 | `reference.md`: certified `<details><summary><code>client.games.<a href="src/fern/games/client.py">game_get_prices</a>(...) -> typing.…`, crozier `<details><summary><code>client.games.<a href="src/fern/games/client.py">game_get_prices</a>(...) -> GameGet…` |
| `resemble-ai/resemble-mcp:openapi/openapi.yml@6404fd41b18fbf3509e0028c1f5e15c11822f3e0` | `48c5814b117a1009a89b28fc48628cfe70706b411297b385a644f3349fd8717a` | `operation-servers-named`; `readme-multipart-file-params-listed-first` | `reserved-name-suffix`, `example-value-source` | 5 | `reference.md`: certified `word="word",`, crozier `word="mounjaro",` |
| `whatwatt-ch/whatwatt-go-documentation:openapi/api-complete-bundle.yaml@50340b0865809c2e6f831385ccfdc900af58981b` | `4cd56f724b38b1766080f870f357c01f5ec3c093dceac5abd6ec7210fa28463a` | `combo-inline-body-read-only-property` | `orphan-type-emission`, `init-import-order`, `example-presence` | 8 | `reference.md`: certified `client.maintenance.upload_firmware(...)`, crozier `from fern import FernApi` |
| `opctl/opctl:api/openapi.yaml@4baed9bb9fd6ac1d3afcf03eb875586c4308d04e` | `57a79c2e7e2795285e22cdbe2fc79e57bf41167406d2fb8f205783f16b005952` | `request-body-content src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | `response-type-resolution`, `reference-body-param-doc` | 3 | `reference.md`: certified `` **request:** `AddAuthReq` ``, crozier `` **password:** `typing.Optional[str]` `` |
| `konfig-dev/konfig:sdks/db/intermediate-fixed-specs/ironclad/openapi.yaml@bec3d36b9a341f30707a4ab3d9de6c4154809ada` | `614a2b05e6528484e08ccc58d2f5a1df7cbdf00d6c7962a96a81a48c12bbdc59` | `multipart-inline-object-part-json-encoded` | `auth-shape`, `union-modelling`, `init-import-order`, `description-source`, `example-enum-member` | 18 | `reference.md`: certified `WebhookEventTypeValue.ALL`, crozier `WebhookEventTypeValue.WORKFLOW_LAUNCHED` |
| `konfig-sdks/openapi-examples:circleci/openapi.yaml@161ab49c45e45825ca3832945c59a3ba904321ba` | `63042193a4670a76bdb988512f38658aad1c4a56f3b312c3b57e5fc19f5d9af6` | `request-example-deprecated-property` | `example-value-source` | 4 | `reference.md`: certified `project_slug="project-slug",`, crozier `project_slug="gh/CircleCI-Public/api-preview-docs",` |
| `halo-dev/halo:api-docs/openapi/v3_0/apis_uc.api_v1alpha1.json@ead7adfb0ca1da810a6a080cf8aeed476668db64` | `6e341cacc7734304136d06c6289318ae4505b142aac6eb56ba5f863739c5c568` | `response-status-space-suffixed` | `schema-type-resolution`, `request-body-spread-vs-request`, `request-content-type-header` | 10 | `reference.md`: certified `` **reason_type_notifiers:** `typing.List[ReasonTypeNotifierRequest]` — notifier selections grouped by reason… ``, crozier `` **request:** `ReasonTypeNotifierCollectionRequest` `` |
| `wxpusher/wxpusher-docs:docs/openapi.yaml@9315920511645d7fbc9b6b31923294063460779c` | `791f79529655eed9761ae0f7d5cca3b86d483230072838af87240224e639d471` | `allof-body-example-id-field-order` | `body-property-set` | 6 | `README.md`: certified (none: crozier inserts the line), crozier `app_token="AT_xxx",` |
| `Skyvern-AI/skyvern:docs/api-reference/openapi.json@b325eb10b04ffd7004b9cc843031fdb6a8ebf442` | `7989ab3e2c034eeb9d5b29ed652d77737d3f0d79eaf4e9278c20aee612963749` | `readme-multipart-file-params-listed-first`; `server-name-several` | `untagged-operation-grouping`, `readme-endpoint-choice`, `example-value-source` | 70 | `README.md`: certified `client.scripts.run_script(`, crozier `client.agents.run_task(` |
| `core-ncsrd/katana:katana-swagger/swagger.json@2c55159fabe40a5b5428b213dba3b0fa791db846` | `7ddfc4202f397446b2a932fd41712c4b2bd62f7f828ef54e9a32a046a07a8d1e` | `response-contentless-200-with-created` | `media-type-recognition`, `request-content-type-header`, `init-import-order` | 7 | `reference.md`: certified `<details><summary><code>client.bootstrap_katana.<a href="src/fern/bootstrap_katana/client.py">configure_kat…`, crozier `<details><summary><code>client.bootstrap_katana.<a href="src/fern/bootstrap_katana/client.py">configure_kat…` |
| `halo-dev/halo:api-docs/openapi/v3_0/apis_console.api_v1alpha1.json@ead7adfb0ca1da810a6a080cf8aeed476668db64` | `7e48a5530dfce8d110f78a1fabd4cb186e93d3008ef4ae95ca0d15dc2325b173` | `response-status-space-suffixed` | `schema-type-resolution`, `response-type-resolution`, `request-body-spread-vs-request`, `request-content-type-header`, `multipart-empty-body` | 29 | `reference.md`: certified `` **before_name:** `typing.Optional[str]` — target next sibling Category metadata.name, or null to append ``, crozier `` **request:** `CategoryPositionRequest` `` |
| `gbyo/tilecast:docs/openapi.yaml@9b731f41de1c1387ebd7a7f74c3c783510aa67a0` | `832b9080645151da0612125abdb82afeb90c6dd0b33da87dcdcd5edc1d3178ce` | `response-contentless-200-with-created` | `request-body-optionality`, `example-value-source` | 3 | `reference.md`: certified `` **request:** `typing.Dict[str, typing.Any]` ``, crozier `` **request:** `typing.Optional[typing.Dict[str, typing.Any]]` `` |
| `TouK/nussknacker:docs-internal/api/nu-designer-openapi.yaml@2e8d32682f659b11fbb223ad189c1e77d5fafd7c` | `895f35189bd7aa82339426400a096442551c820801dd9f712854bfdae5b9b9a8` | `text-response-drops-request-example` | `union-modelling`, `response-type-resolution`, `request-content-type-header`, `reserved-name-suffix`, `init-import-order`, `example-value-source` | 66 | `reference.md`: certified `from fern import FernApi, NodeData_Enricher, ServiceRef, Parameter, Expression`, crozier `from fern import FernApi, NodeDataOutput, ServiceRef, Parameter, Expression, NodeTypes2` |
| `marcelo-earth/generative-manim:api/public/openapi.yaml@f681cc78a6b1cad8443b6af4b3a1adbfed9d3e0e` | `8e1e6b290365eee6b020b146c329b1bd2c1cb4fd3dd6e52be2fee2e72e5a6a30` | `text-response-drops-request-example` | `streaming-detection` | 4 | `README.md`: certified `- [Streaming](#streaming)`, crozier (none: crozier omits the line) |
| `ourofoundation/wrappers:nixtla/timegpt/timegpt-openapi.json@79688dd65e7fb2fb670ad30b01b5db5208c1d928` | `9165e7b94aa026f4924cc6bd8bc627719680fc028af864e0c2649168ded7705b` | `request-example-deprecated-property` | `example-float-repr` | 2 | `reference.md`: certified `0.9345407030264767,`, crozier `0.9345407030264768,` |
| `ballerina-platform/openapi-connectors:openapi/azure.openai.finetunes/openapi.yaml@7c3840c93e80c711a8b317f94339b3cb08c1521c` | `97a587f5a81f68ea2ef3bdf6f12599102c2a254348a6ee8cbf07fde9529943e7` | `readme-multipart-file-params-listed-first` | `example-presence` | 2 | `reference.md`: certified `client.files.getcontent(...)`, crozier `from fern import FernApi` |
| `codosseum-org/backend:openapi.yaml@a92699b50e5b57aefb8922525a27ed8bb8d7885f` | `9fa232be1ff3b0c9d753f4b6a91a55ce5bc2cdcb5a026ecf0bdf0254775257b1` | `request-body-content src/ir.rs::resolve_request_body[let own_count = fields\.len\(\)]` | `union-modelling` | 40 | `src/fern/__init__.py`: certified `SubscribeToGameEventsResponseItemData,`, crozier `SubscribeToGameEventsResponseItemEliminated,` |
| `Skyvern-AI/skyvern:fern/openapi/skyvern_openapi.json@b325eb10b04ffd7004b9cc843031fdb6a8ebf442` | `a61ee2be694a329a0c65609c7069eded7640fdf42a9c331c2a9eb28adb02834f` | `server-name-several` | `untagged-operation-grouping`, `type-placement`, `readme-endpoint-choice` | 67 | `README.md`: certified `client.scripts.run_script(`, crozier `client.agents.run_task(` |
| `jentic/jentic-public-apis:apis/openapi/ironcladapp.com/ironclad/1/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `a96f8580c841a37fa0196dfd24051d4375f9fe28bb413451c35d2cacca3c2caa` | `multipart-inline-object-part-json-encoded` | `auth-shape`, `union-modelling`, `orphan-type-emission`, `init-import-order`, `description-source`, `example-enum-member` | 19 | `reference.md`: certified `WebhookEventTypeValue.ALL`, crozier `WebhookEventTypeValue.WORKFLOW_LAUNCHED` |
| `confluentinc/schema-registry-sdk-go:api/openapi.yaml@77f22d67c4d6bfe86842da77f76a3f1d5b69da5b` | `aa65c204008962962222defeea2e801476d3aa6a932ef981b4728b95690b39b7` | `operation-id-untagged-list-or-set` | `response-type-resolution`, `map-value-modelling`, `orphan-type-emission`, `reference-body-param-doc`, `request-content-type-header`, `example-value-source` | 15 | `reference.md`: certified `"key": "{}"`, crozier `"key": "value"` |
| `NVIDIA-Omniverse/usd-content-agents:apps/texture_agent_service/openapi.yaml@a96faf9cb2f5c1f655fe0d60c0ccf57e3477b1aa` | `aa7d7c209003d2bf4ecca2f1b6dc0d5f856e3037210b66788407a78d1d68f4da` | `media-type-multipart src/ir.rs::nullable_enum_part[    member$]` | `readme-endpoint-choice` | 1 | `README.md`: certified `client.pipeline.upload_usd_immediate(`, crozier `client.pipeline.cancel_pipeline(` |
| `clencyc/MozillaFestivalBackend:openapi.yaml@e70f0150f414d216743311be79d005d900ab81f1` | `b2264b38f17b99bd722b94f94029916705be39cd6359b1b341bc8696f29e6092` | `readme-multipart-file-params-listed-first` | `readme-endpoint-choice` | 1 | `README.md`: certified `client.mock.create_story(`, crozier `client.mock.create_tile_gradient(` |
| `crystalshards/monorepo:apps/crystalshards/openapi.yml@f5c7a1de82d7d397a31e234189fc9f1edb844a80` | `b29a3a4e8ea20deeb6b100e53f180e431abb054443fcaeac1eeea032187eea1c` | `readme-multipart-file-params-listed-first` | `union-modelling`, `init-import-order`, `example-value-source` | 6 | `reference.md`: certified `name="name",`, crozier `name="my-awesome-shard",` |
| `aldinokemal/go-whatsapp-web-multidevice:docs/openapi.yaml@831a851e677f48e25aa671170daade586f798551` | `b52e7995b921c67666f972946b753a4dba3cd8344b4ce3873269aafea3e1d4fa` | `request-body-content src/ir.rs::resolve_request_body[let own_count = fields\.len\(\)]` | `method-name-derivation`, `example-value-source` | 7 | `reference.md`: certified `<details><summary><code>client.app.<a href="src/fern/app/client.py">info</a>() -> AppInfoResponse</code></s…`, crozier `<details><summary><code>client.app.<a href="src/fern/app/client.py">app_info</a>() -> AppInfoResponse</code…` |
| `linux-automation/tacd:openapi.yaml@df3958c92643f7e0b06ef1830b9bc2a5e55ab24a` | `b5dacb83849e3ef5b20249f712ed19ac60838e5052ce0a4de3b6c69aed29bd8c` | `response-description src/emit.rs::push_return_doc[=None => \{\}]`; `response-without-description-blank-line` | `refusal-null-media-type` | 56 | `README.md`: certified (none: crozier inserts the line), crozier `# Fern Python Library` |
| `SeekStorm/SeekStorm:seekstorm_server/openapi/openapi.yml@50cb0ddffe1e45eb574f927079d1bcffecf8980b` | `b73096c45484d5d8076a8e6ed80fd25cf2467acf9a8b717925937c5d9eaa0646` | `text-response-drops-request-example` | `parameter-type-resolution`, `description-source`, `example-value-source`, `example-placeholder-shape` | 6 | `reference.md`: certified (none: crozier inserts the line), crozier (a blank line) |
| `webr0m/teldrive-nodejs:openapi/teldrive.openapi.yaml@22d9b87d2955d3c9c2ce712b5a9d2aad1f94dd14` | `bb74a9e2c993403d2cdbfe25184ce341f23daf27c04a7f96904533a740c6c4f2` | `media-type-event-stream-binary-schema` | `example-presence`, `example-value-source` | 3 | `reference.md`: certified `track=1024,`, crozier `track=1,` |
| `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/meta/import/input-entry.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `bbf0beed6a8af9d7c05d18a099723f2049070e22af9c7527e313db5f51b4c041` | `multipart-inline-object-part-json-encoded`; `readme-multipart-file-params-listed-first`; `request-body-content src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | `union-modelling`, `media-type-recognition`, `map-value-modelling`, `reference-body-param-doc`, `example-value-source` | 20 | `README.md`: certified `name="name",`, crozier `name="my import task",` |
| `radio-aktywne/jasmine:openapi/numbat.yaml@9e8b7f6b965bff0ad7765a2d6db8a623bfd6660f` | `bf07beed1848ad54419a10565cd7b1b792362db3c93e26da1ca2437641ccff19` | `readme-endpoint-prefers-argless-non-get` | `union-modelling`, `parameter-type-resolution`, `response-type-resolution`, `method-name-derivation` | 23 | `README.md`: certified `client.ping.ping_ping()`, crozier `client.ping.ping()` |
| `jentic/jentic-public-apis:apis/openapi/runzero.com/main/4.0.250606.0/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `c2855984c82dbe7917762e7517435792ff651e47be9e4ecb91bdec6c35c70aa3` | `multipart-inline-object-part-json-encoded`; `readme-multipart-file-params-listed-first` | `union-modelling`, `media-type-recognition`, `map-value-modelling`, `example-value-source` | 20 | `README.md`: certified `name="name",`, crozier `name="my import task",` |
| `zalando-incubator/agentic-identity-broker:api/enduser/openapi.yaml@d500f36378dd914f8a516604a08525f737e8ddff` | `c7fb9242356484e677698b557588686e1d461e2f920fbd53042cea345357ceb6` | `media-type-form-urlencoded src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | `auth-shape`, `example-value-source` | 4 | `reference.md`: certified `grant_type=TokenExchangeRequestGrantType.CLIENT_CREDENTIALS,`, crozier `grant_type=TokenExchangeRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE,` |
| `APIs-guru/openapi-directory:APIs/osf.io/2.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `cdcf786527cbc25296204b370846686f3e76083f12c7a50e419b19aa53b03e5b` | `combo-inline-body-read-only-property` | `media-type-recognition`, `orphan-type-emission`, `reference-section-title`, `snippet-rendering` | 520 | `README.md`: certified `"data": {"attributes": {"title": "An Excellent Collection Title"}, "type": "collections"}`, crozier `"data": {` |
| `landing-ai/ade-cli:openapi.json@d1995ffef4e63a2a1c2774d9add93368889353c5` | `d11fa644f12445e8707b6eb8600cb2214fb30a5cfdf8346e1d43aab1f3b20164` | `multipart-inline-object-part-json-encoded` | `description-source` | 3 | `src/fern/extract/types/v2extract_get_job_response_result.py`: certified `` Result returned by V2ExtractOperationWorkflow — the ``/v2/extract`` ``, crozier `` Present once status is ``completed`` and ``output_save_url`` was not set. When ``output_save_url`` was set,… `` |
| `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/source/source.dat@c72e13e0f80e71997209aba985eff6ef34869cd7` | `dc3a906517cbde5e334ba386760ead5e1c36ec6756d5b9547b25cdcef96a2f5d` | `readme-nested-group-post-preferred`; `request-body-content src/ir.rs::request_media_variants[let mut view = op\.with_sdk_method_name]`; `request-body-content src/openapi.rs::Operation::with_sdk_method_name` | `type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling` | 126 | `reference.md`: certified `<details><summary><code>client.listen.v1.media.<a href="src/fern/listen/v1/media/client.py">transcribe_url<…`, crozier `<details><summary><code>client.listen.v1.media.<a href="src/fern/listen/v1/media/client.py">transcribe_url<…` |
| `JHUAPL-DTNMA/dtnma-tools:src/refdm/openapi.json@598da6c6793998ea1d845ec32f1e4107c0c4930a` | `de4dc81fea0801628868bb1cb1576f546e8498404f8ad4b94fd65b2bd0d3bef3` | `response-without-description-blank-line` | `bare-string-parameter-example` | every file | the whole SDK: the certified pair writes its tree; crozier writes no SDK |
| `truefoundry/trueforge:docs/openapi.json@a718e719347c44798ef3d3021a17678b6220640b` | `e259dee6c57f311f2a39344f5714d57d03218229dad1c291d5c5aebeace58f32` | `readme-streaming-snippet-omits-type-import` | `allof-description-wrapper` | 3 | `reference.md`: certified `` **name:** `str` — Sandbox environment name. ``, crozier `` **name:** `typing.Any` — Sandbox environment name. `` |
| `GravitLauncher/Launcher:openapi.yaml@fef9bae63da1afc0518d32e3333db20f409ab196` | `e883f6981ac00d25446ad4742052a00849cc9d008d38f1986d0ab2442d30ac19` | `readme-multipart-file-params-listed-first` | `method-name-derivation`, `reserved-name-suffix` | 3 | `reference.md`: certified `uuid_="uuid",`, crozier `uuid="d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",` |
| `radio-aktywne/magnolia:openapi/gecko.yaml@51d280e261cee506a6290a0fc8c9f78475c18069` | `f02e99f9ace84d4e8abe420d952516223cb130b172f6aac443b8b4f23a2ef522` | `readme-endpoint-prefers-argless-non-get` | `union-modelling`, `parameter-type-resolution`, `response-type-resolution`, `method-name-derivation` | 23 | `README.md`: certified `client.ping.ping_ping()`, crozier `client.ping.ping()` |
| `SiaFoundation/walletd:openapi.yml@aa523f95c5b2a106a3c0d9675205c90305d2d9d9` | `f03d7dc2f29f154955df2fa0910f62525d6222f67915022d12b0e5de7230f18d` | `request-body-described-inline-scalar` | `allof-description-wrapper`, `path-param-serialization`, `description-source`, `example-value-source` | 22 | `reference.md`: certified `height=1000000,`, crozier `height=1,` |
| `Hardonian/Reach:openapi/reach.openapi.yaml@beb7f7f9d28d4b123af2b2d52790225e796f0879` | `f36ad5db387d59597977a7bfd6c72d24470580cc5a61323b7b605cf53af589b2` | `media-type-event-stream-binary-schema` | `example-presence` | 2 | `reference.md`: certified `client.runs.get_run_events(...)`, crozier `from fern import FernApi` |
| `jentic/jentic-public-apis:apis/openapi/deepgram.com/main/1.0.0/meta/import/output-bundle.json@c72e13e0f80e71997209aba985eff6ef34869cd7` | `ffab94be1fc5a3db201bc8818eb57c0135620492ca5fb6ed2bff3c2c520f99a8` | `readme-nested-group-post-preferred`; `request-body-content src/ir.rs::request_media_variants[let mut view = op\.with_sdk_method_name]`; `request-body-content src/openapi.rs::Operation::with_sdk_method_name` | `type-placement`, `inline-type-naming`, `subpackage-order`, `environment-shape`, `union-modelling` | 126 | `reference.md`: certified `<details><summary><code>client.listen.v1.media.<a href="src/fern/listen/v1/media/client.py">transcribe_url<…`, crozier `<details><summary><code>client.listen.v1.media.<a href="src/fern/listen/v1/media/client.py">transcribe_url<…` |

### The certified pair's false successes

The certified pair exited 0 on each of these while its log reads `Failed to parse openapi document` and its tree is the 35-file empty scaffold, so it generated nothing from the document: a refusal, recorded as such rather than as a difference. crozier refuses each in the refusal class the certified pair's own error names.

| document | sha256 | targets | the certified pair's parse failure | crozier's refusal |
|---|---|---|---|---|
| `stripe/openapi:stripe--openapi/preview/openapi.spec3.sdk.json@58e06a3214ae1574600fba64d40b770e5da6d505` | `60caefaab927e1b1b4a42125a5309a50300bb17552c2f5f8794108e9a7d529d4` | `multipart-inline-object-part-json-encoded` | `Maximum call stack size exceeded` | `extension-reference-cycle` |
| `stripe/openapi:stripe--openapi/latest/openapi.spec3.sdk.json@58e06a3214ae1574600fba64d40b770e5da6d505` | `92363b86025d012852f648554372bf5fa6146af1472fb63f3c29d7c5fe6bd19a` | `multipart-inline-object-part-json-encoded` | `Maximum call stack size exceeded` | `extension-reference-cycle` |
| `beeequeue/arm-server:docs/openapi.yaml@86c9359fc9df49b9d42cf21dc67bdc99b1658fbf` | `79211321295936c435fd6781a48695018d2645aa2e2d5d539626eadb3eb0c17c` | `operation-id-hyphenated-tag-method` | `Failed to resolve #/$defs/400` | `unresolved-reference` |
| `jentic/jentic-public-apis:apis/openapi/pagerduty.com/pagerduty-api/2.0.0/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `84fcb3ada8922a0a9c2ffe8efa6a93e7c35998ccda9db5d0f42fd340a8b1a936` | `combo-body-property-named-as-path-param`; `combo-inline-body-read-only-property`; `request-example-deprecated-property` | `Failed to resolve #/components/requestBodies/OrchestrationCacheVariableDataPutResponse` | `unresolved-reference` |
| `jentic/jentic-public-apis:apis/openapi/pagerduty.com/pagerduty-api/2.0.0/meta/import/input-entry.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `a0f7d0ded3d88daa940ed8b6e8fd1534c9f2c12752457e7d5b71f4c5f0d3f2b0` | `combo-body-property-named-as-path-param`; `combo-inline-body-read-only-property`; `request-example-deprecated-property` | `Failed to resolve #/components/requestBodies/OrchestrationCacheVariableDataPutResponse` | `unresolved-reference` |
| `jentic/jentic-public-apis:apis/openapi/setu.co/main/1.0.0/meta/import/input-entry.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `be0196359ca1794934d5c9622d42d608da3426b1f993db7c91e995b7a54815f7` | `readme-multipart-file-params-listed-first`; `response-status-space-suffixed` | `Failed to resolve #/components/responses/BAD_REQUEST` | `unresolved-reference` |
| `jentic/jentic-public-apis:apis/openapi/setu.co/main/1.0.0/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `d2dc23e9de5690536e870a5719d6bd9d2afc25349a30ec1bcd06d05526370414` | `readme-multipart-file-params-listed-first`; `response-status-space-suffixed` | `Failed to resolve #/components/responses/BAD_REQUEST` | `unresolved-reference` |

### crozier's ruled refusal

| document | sha256 | targets | outcome |
|---|---|---|---|
| `neilthomas89440-crypto/inferna-next:docs/openapi.yaml@3c1bc6fde017130ac9335b2d4192d0400f956689` | `244423758c587aff156c4763e1491ab3ac6be494a9e3f447c8f244775b586ee1` | `readme-multipart-file-params-listed-first` | the certified pair generates it, and crozier refuses it (`request-property-name-collision`: the multipart body property `model` beside the query parameter `model` of `POST /v1/audio/transcriptions`); the standing ruling makes that collision a defect of the certified output, so the document is no witness either way |

### crozier failures never compared with the certified pair

The arm probe recorded these documents as `crozier refuses the document` before any certified-pair generation; each sits on a target a registered row already proves, so none was generated and none is a measured difference from the certified pair. crozier at `2dc89c1810b3dff315851aa31089caf70323dbe3` still fails on each, as below. The last is no refusal: crozier writes a call passing one keyword twice, which `ruff format` rejects, and that defect is recorded as a follow-up rather than repaired here.

| document | sha256 | target | crozier at the branch commit |
|---|---|---|---|
| `fossology/FOSSology.REST.dotnet:openapi/FOSSology REST API 1.6.2.yaml@b362ec94ddf8ab6da0f8606183dfc2bc79b157b9` | `7da1db69e60df38ffa4ae477eee68eab2e29932dad65de682d4d22bac71b9872` | `media-type-form-urlencoded src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | `request-property-name-collision`: PUT /users/{id} body property "id" collides with another request property; give the properties distinct declared names |
| `jentic/jentic-public-apis:apis/openapi/cloudbeds.com/main/v1.3/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `8724cc349f5f6c3835b0c45e8b17b15807ac17fed862354b479c584d08cb319c` | `media-type-form-urlencoded src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | `type-name-collision`: type PostCreateAllotmentBlockRequestAutoReleaseReleaseType is declared in namespaces "" and "allotment_blocks"; give the types distinct declared names |
| `konfig-dev/konfig:sdks/db/intermediate-fixed-specs/peach-payments/openapi.yaml@bec3d36b9a341f30707a4ab3d9de6c4154809ada` | `adc6eff9c74263a89fe32f9ed7fcffac14d86055a602d7cb9494934b4524f67c` | `media-type-form-urlencoded src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | `type-name-collision`: component schemas "PaymentType" and "paymentType" both declare type PaymentType; give them distinct names |
| `konfig-sdks/openapi-examples:peach-payments/openapi.yaml@161ab49c45e45825ca3832945c59a3ba904321ba` | `d7497fa8a725dfea1f77f5c50653f3ee1d9d866e27b1592b6f6c7911ea77f972` | `media-type-form-urlencoded src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | `type-name-collision`: component schemas "PaymentType" and "paymentType" both declare type PaymentType; give them distinct names |
| `prometheus/prometheus:web/api/v1/testdata/openapi_3.1_golden.yaml@ea954809ceafceb53ecfa295ab0947753929de9e` | `76fb085db4bfd0d30515cd7a45d345997bf9dfb1d3e6a51aa74c852574ccd437` | `media-type-form-urlencoded src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | `generator-lint-failure`: GET /query root method and sub-client query |
| `(bytes only, no recorded provenance)` | `072f630295a0a00fdf0b613dd33a7297686c489e247ceec447ad18d0e387eaab` | `media-type-multipart src/ir.rs::nullable_enum_part[    member$]` | `enum-value-unnameable`: #/components/schemas/SpecialEnum enum value "🚀"; declare a usable name with x-crozier-enum |
| `(bytes only, no recorded provenance)` | `60784093c680e6a4364097d78a1b8406b09a9c1656fbfe16c8491d75eb5a1fd6` | `media-type-multipart src/ir.rs::nullable_enum_part[    member$]` | `enum-value-unnameable`: #/components/schemas/SpecialEnum enum value "🚀"; declare a usable name with x-crozier-enum |
| `shikorism/tissue:openapi.yaml@34abc826977006d68ee8da515b40a57935fd8fcb` | `ba4127ea2b1b0d50a0f501286dbffa0e5c4297a7ea806a1f133169b962dab8e0` | `request-body-content src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | `generator-lint-failure`: POST /webhooks/checkin/{id} method name is empty |
| `OWASP/crAPI:services/chatbot/src/resources/crapi-openapi-spec.json@b5fc307f3e5f875809b095b771108ef342a33724` | `8d16b09f329e7372db703dc8a95d7ef2f7e53deb3ff19a75e604ec6d3b84e09b` | `request-body-content src/name_refusals.rs::validate_ir[=body\.content\.len\(\) == 1]` | `type-name-collision`: POST /community/api/v2/coupon/validate-coupon request type ValidateCouponRequest collides with another declaration; give the types distinct declared names |
| `lightning-rod-labs/lightningrod-python-sdk:openapi/openapi-docs.json@7e6a5d0f91ee29842f8f32c2ffea49ec397f1656` | `7d19c17a5221a635e78463a780a822f2593d6f126226c29255158ccce88e567c` | `request-body-content src/name_refusals.rs::validate_ir[=body\.content\.len\(\) == 1]` | `type-name-collision`: POST /v1/mpp/topup request type MppTopupRequest collides with another declaration; give the types distinct declared names |
| `api-platform/schema-generator:tests/e2e/openapi.yml@22635fbacac8011c73cdbbb5c20507c77c02d89d` | `978fbacd3483f78d34c90ff71bdc8429223ef8409e531b4960cb0c78dec31206` | `response-description src/emit.rs::push_return_doc[=None => \{\}]` | emits invalid Python: `ruff format` fails on `src/fern/review/client.py:76:181`, Duplicate keyword argument "book" |

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
  (`swagger-parser-null-types`) also declare `operation-id-untagged-list-or-set`
  and write the untagged `list` operation as an unsuffixed `def list(`. Both
  are generator test resources, so under the manager's 2026-10-29 ruling they
  only corroborate; the real witness is corpus row 4212, `ollama-api`, found by
  the second screening pass, which retired `depot-bin-ledger`.
- `tamoss` (corpus row with a byte-matched golden) renders string request
  bodies whose examples hold a newline and quotes, escaped in its worked
  examples; none holds a backslash, so it does not declare
  `string-body-example-backslash-escaped`. None of the 15 documents with a
  newline-only string-body example does either.
- Documents in the generator vendor's own repositories that the live search
  returned were counted but neither screened nor named, under this
  repository's provenance rule; documents from this repository itself are its
  own authored fixtures. Both appear in `census.tsv` with that outcome.

## Arms reached outside the targets

Registering `speech-ai-forge` (corpus row 4202) also made the golden-only tier
execute `format-binary`'s `src/ir.rs::hoist_form_object[if nullable_binary]`
arm, whose only cover was `multipart-nullable-array`. The hand-written gate
retires a cover once a real specification reaches its arm, so that fixture
moved to the superseded fixtures too, and its three scenario-index proofs now
cite its retained trees as measurements.

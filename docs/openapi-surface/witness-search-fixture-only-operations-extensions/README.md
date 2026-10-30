# Witness search for the fixture-only parameter, security and extension proofs

Every target of the region files [`parameters.md`](../parameters.md), [`security.md`](../security.md) and [`oas31-extensions.md`](../oas31-extensions.md) whose proof, at this node's base (`1748b7946`), was a hand-written fixture: their `handwritten` feature rows, their one `handwritten` combination row, and every arm-level hand-written cover of one of their `golden` rows that [`../handwritten-reach.tsv`](../handwritten-reach.tsv) listed. None of their `golden` rows rested on a residual-only supplement (the one supplement, `schema-example-null`, is a `schemas.md` row). Each target was searched once, against the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3), for a real specification whose complete golden crozier byte-matches.

**Outcome.** 6 feature targets now rest on a registered real witness and 3 arm targets are executed by one; 32 targets are `exhausted`; 23 remain `search-incomplete`, each with its reason below. Six corpus rows carry the witnesses: registered row 3001 `formbricks`, reused, and rows 4400 to 4404, added by this record.

## The targets

| key | kind | region | hand-written cover at the base |
|---|---|---|---|
| `client-header-date-format` | feature | `parameters.md` | `observatory-client-date` |
| `global-headers-extension` | feature | `parameters.md` | `observatory-client-headers`, `warehouse-header-token` |
| `nullable-array-query-explode-false` | feature | `parameters.md` | `observatory-nullable-query` |
| `nullable-query-array-items` | feature | `parameters.md` | `observatory-nullable-query` |
| `parameter-default-extension` | feature | `parameters.md` | `observatory-query-extensions` |
| `parameter-ignore-extension` | feature | `parameters.md` | `observatory-query-extensions` |
| `parameter-name-extension` | feature | `parameters.md` | `declared-rename-control`, `observatory-query-extensions` |
| `parameter-without-location` | feature | `parameters.md` | `observatory-unlocated-parameter` |
| `path-parameters-template-order-31` | feature | `parameters.md` | `observatory-route-order` |
| `query-date-union-oneof` | feature | `parameters.md` | `observatory-nullable-query` |
| `required-nullable-query-scalar` | feature | `parameters.md` | `observatory-nullable-query` |
| `sdk-variable-parameter-extension` | feature | `parameters.md` | `observatory-client-variable` |
| `sdk-variables-extension` | feature | `parameters.md` | `observatory-client-variable` |
| `query-array-items-union` | feature | `parameters.md` | `query-array-items-union` |
| `header-subset-string-default` | feature | `parameters.md` | `header-subset-string-default` |
| `literal-prefixed-integer-path-segment` | feature | `parameters.md` | `literal-prefixed-integer-path-segment` |
| `query-param-ref-to-enum-or-array-union-converted` | feature | `parameters.md` | `query-param-ref-to-enum-or-array-union-converted` |
| `required-param-and-body-defaults-ignored` | feature | `parameters.md` | `required-param-and-body-defaults-ignored` |
| `example-nested-array-two-items` | feature | `parameters.md` | `tram-route-query` |
| `query-anyof-const-member-example-as-enum-member` | feature | `parameters.md` | `ferry-slot-query` |
| `required-query-array-nullable-union-items` | feature | `parameters.md` | `sensor-batch-query` |
| `security-scheme-header-extension-named` | feature | `security.md` | `meter-reader-gateway` |
| `security-scheme-bearer-extension-named` | feature | `security.md` | `ski-lift-gates` |
| `security-scheme-basic-extension-named` | feature | `security.md` | `lock-keeper-vault` |
| `security-scheme-token-variable-name` | feature | `security.md` | `grid-valve-console` |
| `security-schemes-duplicate-api-key-header` | feature | `security.md` | `twin-key-relay` |
| `security-scheme-capitalised-http` | feature | `security.md` | `tide-gauge-sessions` |
| `operation-sdk-group-name-leading-underscore` | feature | `oas31-extensions.md` | `signal-box-relays` |
| `operation-sdk-group-name-without-method-name` | feature | `oas31-extensions.md` | `cargo-hold-pallets` |
| `operation-sdk-method-name-sequence` | feature | `oas31-extensions.md` | `locker-bank-claims` |
| `operation-idempotent-with-root-headers` | feature | `oas31-extensions.md` | `parcel-courier-desk` |
| `operation-retries-disabled` | feature | `oas31-extensions.md` | `parcel-courier-desk` |
| `operation-webhook-extension` | feature | `oas31-extensions.md` | `auction-house-bids` |
| `operation-pagination-offset` | feature | `oas31-extensions.md` | `ledger-records-offset` |
| `operation-pagination-boolean` | feature | `oas31-extensions.md` | `beacon-registry-pages` |
| `operation-group-types-beside-child-group` | feature | `oas31-extensions.md` | `dock-yard-bookings` |
| `webhook-inline-json-body-named` | feature | `oas31-extensions.md` | `courier-delivery-hooks` |
| `fern-streaming-boolean` | feature | `oas31-extensions.md` | `streaming-extension-boolean` |
| `fern-streaming-condition-ref-body-header` | feature | `oas31-extensions.md` | `stream-condition-ref-body-header` |
| `fern-streaming-condition-shared-body` | feature | `oas31-extensions.md` | `stream-condition-shared-body` |
| `fern-streaming-condition-union-body` | feature | `oas31-extensions.md` | `stream-condition-union-body` |
| `fern-streaming-format-over-json` | feature | `oas31-extensions.md` | `streaming-extension-sse-format` |
| `fern-streaming-terminator` | feature | `oas31-extensions.md` | `streaming-extension-terminator` |
| `base-path-extension` | feature | `oas31-extensions.md` | `base-path-client-argument`, `observatory-base-path` |
| `discriminated-extension` | feature | `oas31-extensions.md` | `greenhouse-undiscriminated-unions` |
| `discriminator-property-name-extension` | feature | `oas31-extensions.md` | `telescope-renamed-discriminant` |
| `combo-param-example-beside-ref-schema` | combination | `parameters.md` | `harbor-parcel-requests` |
| `parameter-in-path` | arm `src/ir.rs::lifted_client_path_parameters[\.map\(\x7cparameter\x7c ClientPathParameter \{]` | `parameters.md` | `base-path-client-argument` |
| `parameter-in-header` | arm `src/ir.rs::global_headers[Some\(default\) if count < total && py_type == HeaderType::Str => \{]` | `parameters.md` | `header-subset-string-default` |
| `http-dpop` | arm `src/ir.rs::auth_model[=_ => Auth::None,]` | `security.md` | `http-dpop-unrequired` |
| `http-mutual` | arm `src/ir.rs::auth_model[=_ => Auth::None,]` | `security.md` | `http-mutual-unrequired` |
| `http-negotiate` | arm `src/ir.rs::auth_model[=_ => Auth::None,]` | `security.md` | `http-negotiate-unrequired` |
| `parameter-schema` | arm `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*TypeRef::Optional\(element\) => \*element,]` | `parameters.md` | `nullable-query-union-items` |
| `parameter-in-header` | arm `src/ir.rs::header_py_type[=^\s*HeaderType::Date]` | `parameters.md` | `observatory-client-date` |
| `parameter-in-header` | arm `src/ir.rs::global_headers[for header in doc\.global_header_extensions]` | `parameters.md` | `observatory-client-headers` |
| `parameter-in-path` | arm `src/ir.rs::lifted_client_path_parameters[if let Some\(variable\) = parameter\.sdk_variable]` | `parameters.md` | `observatory-client-variable` |
| `parameter-in-query` | arm `src/emit.rs::method_params[if let Some\(default\) = &qp\.default]` | `parameters.md` | `observatory-query-extensions` |
| `parameter-style-form-query-object` | arm `src/emit.rs::append_request_call_args[\} else if qp\.convert \{]` | `parameters.md` | `ore-bin-screen` |
| `parameter-schema` | arm `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*element => element,]` | `parameters.md` | `query-array-items-union` |
| `parameter-schema` | arm `src/ir.rs::InlineHoister::hoist_param_enum[if let Some\(\(item, members\)\) = schema]` | `parameters.md` | `query-array-items-union` |
| `parameter-schema` | arm `src/ir.rs::InlineHoister::hoist_param_enum[if composition_admits_null\(item, members\) \{]` | `parameters.md` | `sensor-batch-query` |
| `fern-streaming-extension` | arm `src/ir.rs::declare_split_union_body[=tag_types\.push\(TagTypeDecl \{]` | `oas31-extensions.md` | `stream-condition-union-body` |
| `fern-streaming-extension` | arm `src/emit.rs::sse_end[=\x7cend\x7c format!]` | `oas31-extensions.md` | `streaming-extension-terminator` |
| `x-fern-or-crozier-ignore` | arm `src/openapi.rs::filter_ignored[for key in &ignored_schemas \{]` | `oas31-extensions.md` | `x-fern-ignore-schema` |

## The search

### Populations read

Every document was censused with the repository's census selectors and with this record's detectors (below), one pass per population, run on 2026-10-30:

- **The registered corpus** at this node's base: every `openapi.*` under `tests/fixtures/` (each committed corpus source and each vendored fixture document), 297 OpenAPI 3 documents of 995 JSON and YAML files, the three this record adds included.
- **The pinned APIs.guru archive**, `APIs-guru/openapi-directory` at `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, read from the archive response the shared GitHub response cache holds (SHA-256 `7a0bdff93afc94d373c7e596d24739cc8aff7d93c4e8b75a82e9c0cf7e0606a1`, the digest [`../witness-search-apis.guru/acquisitions.jsonl`](../witness-search-apis.guru/acquisitions.jsonl) records): 4138 JSON and YAML files, 1970 of them OpenAPI 3; no request was made.
- **The documents earlier searches acquired**: every document under the two pool worktrees' `.local/golden-reach-search/*/documents/` (the GitHub code search, Sourcegraph, jentic, vendor-portal and publisher-tree acquisitions), every body in the shared response cache under `${XDG_CACHE_HOME:-$HOME/.cache}/crozier/github-responses/`, and every source in the preflight cache beside it, de-duplicated by SHA-256: 7960 documents naming `openapi` in their first 20 KB, 7531 of them OpenAPI 3.
- **Live GitHub code search**, for the targets the acquired pools leave open: the 24 phrase queries in the table below, each window read to the end (none was truncated) by two drivers sharing the response cache, and every result fetched at its indexed commit over the exact-commit raw lane: 2706 files, 417 of them OpenAPI 3 (most of the rest are Fern definition and overrides files).

- **The documents a sibling search acquired**, re-screened at the manager's direction before any further live request: the fixture-only search of the bodies and paths region files fetched 2070 documents this record's pools did not already hold, 832 of them OpenAPI 3. Each new declarer of a target here is in [`census.tsv`](census.tsv) as `sibling-acquired`; none declares a target this record reads `exhausted` outside Fern's own repositories, and none was screened (no further request was made), so those of open targets are named `outstanding`.

Code search reads only each repository's default branch and only files it indexes, so a document on another branch, or one too large to index, is outside it. Sourcegraph, the vendor portals and the registries were not queried for these targets.

| family | query | reported | distinct results retrieved | OpenAPI 3 documents among them |
|---|---|---:|---:|---:|
| `scheme-dpop` | `"scheme: dpop"` | 67 | 67 | 39 |
| `scheme-mutual` | `"scheme: mutual"` | 204 | 207 | 43 |
| `scheme-negotiate` | `"scheme: negotiate"` | 232 | 283 | 46 |
| `x-crozier` | `"x-crozier"` | 272 | 287 | 12 |
| `x-fern-base-path` | `"x-fern-base-path"` | 147 | 151 | 11 |
| `x-fern-basic` | `"x-fern-basic"` | 23 | 23 | 2 |
| `x-fern-bearer` | `"x-fern-bearer"` | 45 | 45 | 7 |
| `x-fern-default` | `"x-fern-default"` | 685 | 1343 | 3 |
| `x-fern-discriminated` | `"x-fern-discriminated"` | 21 | 21 | 1 |
| `x-fern-global-headers` | `"x-fern-global-headers"` | 242 | 424 | 7 |
| `x-fern-header` | `"x-fern-header"` | 67 | 67 | 18 |
| `x-fern-idempotent` | `"x-fern-idempotent"` | 194 | 193 | 6 |
| `x-fern-ignore` | `"x-fern-ignore"` | 397 | 558 | 42 |
| `x-fern-pagination` | `"x-fern-pagination"` | 500 | 923 | 20 |
| `x-fern-parameter-name` | `"x-fern-parameter-name"` | 521 | 836 | 5 |
| `x-fern-property-name` | `"x-fern-property-name"` | 101 | 102 | 4 |
| `x-fern-retries` | `"x-fern-retries"` | 557 | 1147 | 3 |
| `x-fern-sdk-group-name` | `"x-fern-sdk-group-name"` | 2756 | 3490 | 115 |
| `x-fern-sdk-method-name` | `"x-fern-sdk-method-name"` | 2548 | 3229 | 122 |
| `x-fern-sdk-variable` | `"x-fern-sdk-variable"` | 364 | 768 | 1 |
| `x-fern-sdk-variables` | `"x-fern-sdk-variables"` | 298 | 625 | 1 |
| `x-fern-streaming` | `"x-fern-streaming"` | 587 | 1103 | 37 |
| `x-fern-token-variable-name` | `"x-fern-token-variable-name"` | 22 | 22 | 6 |
| `x-fern-webhook` | `"x-fern-webhook"` | 61 | 61 | 5 |

Every live request went through [`tools/witness-search/rate_limit_guard.py`](../../../tools/witness-search/rate_limit_guard.py), by way of `tools/witness-search/witness-search-github.py`'s acquirer and `tools/witness-search/witness_screen.py`; the probes, waits and cache hits are under `.local/witness-search-fixture-only-operations-extensions/`. Live requests per bucket: `code_search` 153, `core` 1, and 4042 on the exact-commit raw lane (`raw.githubusercontent.com`, paced rather than percentage-guarded). The shared response cache answered 5068 requests at no cost. No GraphQL, Postman or SwaggerHub route was used.

### The detectors

A target's census selector is the one [`../witness-search-keys.tsv`](../witness-search-keys.tsv) records for it. Where that selector is broader than the shape, or the target is an arm or a combination, the detector below is what the search ran; an arm's or a combination's declarer is a witness only when the instrumented crozier run over it executes the arm or the interaction branch.

| key | census selector | detector |
|---|---|---|
| `client-header-date-format` | `parameter.schema:promoted-date-header` | a header parameter typed `format: date` that crozier promotes to a client argument |
| `global-headers-extension` | `openapi.x-fern-global-headers` | a document-level `x-fern-global-headers` (or `x-crozier-global-headers`) |
| `nullable-array-query-explode-false` | `parameter.schema:nullable-array-explode-false` | an optional nullable query array with `style: form`, `explode: false` |
| `nullable-query-array-items` | `parameter.schema:nullable-array-items-oas-three-zero` | a query array whose inline scalar items are `nullable: true` (OAS 3.0) |
| `parameter-default-extension` | `parameter.x-fern-default` | a parameter declaring `x-fern-default` (either spelling) |
| `parameter-ignore-extension` | `parameter.x-fern-ignore` | a parameter declaring `x-fern-ignore: true` (either spelling) |
| `parameter-name-extension` | `parameter.x-fern-parameter-name` | a parameter declaring `x-fern-parameter-name` (either spelling) |
| `parameter-without-location` | `parameter.in:absent` | a Parameter Object with no `in` |
| `path-parameters-template-order-31` | `operation.parameters:path-order-oas-three-one` | an OAS 3.1 operation whose path parameters are declared out of template order, with no path-level path parameters |
| `query-date-union-oneof` | `parameter.schema:date-union-query-oneof` | an inline query `oneOf` of an integer and a `format: date` string |
| `required-nullable-query-scalar` | `parameter.schema:required-nullable-scalar-oas-three-zero` | a required query scalar declared `nullable: true` (OAS 3.0) |
| `sdk-variable-parameter-extension` | `parameter.x-fern-sdk-variable` | a path parameter naming a document SDK variable by `x-fern-sdk-variable` |
| `sdk-variables-extension` | `openapi.x-fern-sdk-variables` | a document-level `x-fern-sdk-variables` |
| `query-array-items-union` | `parameter.schema:query-items-union` | a query array whose inline items are a union |
| `header-subset-string-default` | `parameter.schema:subset-header-string-default` | a header with a string `default` riding at least three quarters but not all of the operations |
| `literal-prefixed-integer-path-segment` | `openapi.paths:templated-key` | a path segment of literal text then one `{param}` typed `integer` |
| `query-param-ref-to-enum-or-array-union-converted` | `schema.items` | an optional query parameter `$ref` to `oneOf [$ref E, array of $ref E]`, E a string enum |
| `required-param-and-body-defaults-ignored` | `schema.default` | an operation with a required integer query parameter carrying `default` and an inline JSON body whose required string property carries `default` |
| `example-nested-array-two-items` | `parameter.schema` | a required query parameter `$ref` to an object requiring an array of non-enum strings |
| `query-anyof-const-member-example-as-enum-member` | `parameter.schema` | a required query `anyOf`/`oneOf` of a plain string and a `const` or one-value enum member, defaulting to that value |
| `required-query-array-nullable-union-items` | `parameter.schema` | a required query array whose items are an `anyOf`/`oneOf` of `type: null` beside two or more other members |
| `security-scheme-header-extension-named` | `securityScheme.x-fern-header:named` | a header `apiKey` scheme whose `x-fern-header` names the credential |
| `security-scheme-bearer-extension-named` | `securityScheme.x-fern-bearer:named` | an http `bearer` scheme whose `x-fern-bearer` names the credential |
| `security-scheme-basic-extension-named` | `securityScheme.x-fern-basic:named-or-env` | an http `basic` scheme whose `x-fern-basic` names a credential or gives an `env` |
| `security-scheme-token-variable-name` | `securityScheme.x-fern-token-variable-name:bearer` | the http `bearer` scheme Fern names the credential from, declaring `x-fern-token-variable-name` |
| `security-schemes-duplicate-api-key-header` | `components.securitySchemes:duplicate-api-key-header` | two header `apiKey` schemes naming one header that stems to `api_key`, both offered |
| `security-scheme-capitalised-http` | `securityScheme.scheme:capitalised-http` | an http scheme whose `scheme` is `bearer` or `basic` spelled with a capital |
| `operation-sdk-group-name-leading-underscore` | `operation.x-fern-sdk-group-name:leading-underscore` | an SDK group segment starting with `_` beside a method name |
| `operation-sdk-group-name-without-method-name` | `operation.x-fern-sdk-group-name:without-method-name` | a non-blank SDK group name with no SDK method name |
| `operation-sdk-method-name-sequence` | `operation.x-fern-sdk-method-name:sequence` | an SDK method name written as a sequence |
| `operation-idempotent-with-root-headers` | `operation.x-fern-idempotent:with-root-headers` | an `x-fern-idempotent: true` operation in a document declaring `x-fern-idempotency-headers` |
| `operation-retries-disabled` | `operation.x-fern-retries:disabled` | an operation whose `x-fern-retries` is `{disabled: true}` |
| `operation-webhook-extension` | `operation.x-fern-webhook:true` | a path operation marked `x-fern-webhook: true` |
| `operation-pagination-offset` | `operation.x-fern-pagination:offset` | an operation whose pagination extension is the offset form |
| `operation-pagination-boolean` | `operation.x-fern-pagination:boolean-over-root` | an operation whose pagination extension is `true` beside a document-level contract |
| `operation-group-types-beside-child-group` | `operation.x-fern-sdk-group-name:types-beside-child-group` | an SDK group with hoisted types and a child group |
| `webhook-inline-json-body-named` | `openapi.webhooks:inline-json-body-named` | an OAS 3.1 webhook with an inline JSON payload, an SDK group and a method name |
| `fern-streaming-boolean` | `operation.x-fern-streaming` | `x-fern-streaming: true` |
| `fern-streaming-condition-ref-body-header` | `operation.x-fern-streaming` | a `stream-condition` over an unrequired `$ref` body with only optional properties and no parameter |
| `fern-streaming-condition-shared-body` | `operation.x-fern-streaming` | a `stream-condition` whose body schema another operation also posts |
| `fern-streaming-condition-union-body` | `operation.x-fern-streaming` | a `stream-condition` whose body is a component union |
| `fern-streaming-format-over-json` | `operation.x-fern-streaming` | `format: sse` without `stream-condition` over a JSON-only success |
| `fern-streaming-terminator` | `operation.x-fern-streaming` | an `x-fern-streaming` mapping with `terminator` |
| `base-path-extension` | `openapi.x-fern-base-path` | a document-level `x-fern-base-path` (either spelling) |
| `discriminated-extension` | `schema.x-fern-discriminated` | a schema declaring `x-fern-discriminated` |
| `discriminator-property-name-extension` | `schema.discriminator.x-fern-property-name` | a discriminator declaring `x-fern-property-name` |
| `combo-param-example-beside-ref-schema` | `parameter.example&parameter.schema>schema.$ref` | a Parameter Object writing `example` whose schema is a Reference Object, the instrumented crozier run executing `src/ir.rs::parameter_example_value`'s `declared_string` filter |
| `parameter-in-path` (`base-path-client-argument`) | `parameter.in=path` | an `x-fern-base-path` whose `parameters` lift a path placeholder, and the instrumented crozier run executes `src/ir.rs::lifted_client_path_parameters[\.map\(\x7cparameter\x7c ClientPathParameter \{]` |
| `parameter-in-header` (`header-subset-string-default`) | `parameter.in=header` | as `header-subset-string-default`, and the instrumented crozier run executes `src/ir.rs::global_headers[Some\(default\) if count < total && py_type == HeaderType::Str => \{]` |
| `http-dpop` (`http-dpop-unrequired`) | `securityScheme.scheme=dpop` | an http `dpop` scheme in a document with no supported scheme, required by no operation, and the instrumented crozier run executes `src/ir.rs::auth_model[=_ => Auth::None,]` |
| `http-mutual` (`http-mutual-unrequired`) | `securityScheme.scheme=mutual` | an http `mutual` scheme in a document with no supported scheme, required by no operation, and the instrumented crozier run executes `src/ir.rs::auth_model[=_ => Auth::None,]` |
| `http-negotiate` (`http-negotiate-unrequired`) | `securityScheme.scheme=negotiate` | an http `negotiate` scheme in a document with no supported scheme, required by no operation, and the instrumented crozier run executes `src/ir.rs::auth_model[=_ => Auth::None,]` |
| `parameter-schema` (`nullable-query-union-items`) | `parameter.schema` | an optional query array whose items are an `anyOf`/`oneOf` of `type: null` beside two or more members, and the instrumented crozier run executes `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*TypeRef::Optional\(element\) => \*element,]` |
| `parameter-in-header` (`observatory-client-date`) | `parameter.in=header` | as `client-header-date-format`, and the instrumented crozier run executes `src/ir.rs::header_py_type[=^\s*HeaderType::Date]` |
| `parameter-in-header` (`observatory-client-headers`) | `parameter.in=header` | as `global-headers-extension`, and the instrumented crozier run executes `src/ir.rs::global_headers[for header in doc\.global_header_extensions]` |
| `parameter-in-path` (`observatory-client-variable`) | `parameter.in=path` | as `sdk-variable-parameter-extension`, and the instrumented crozier run executes `src/ir.rs::lifted_client_path_parameters[if let Some\(variable\) = parameter\.sdk_variable]` |
| `parameter-in-query` (`observatory-query-extensions`) | `parameter.in=query` | as `parameter-default-extension`, and the instrumented crozier run executes `src/emit.rs::method_params[if let Some\(default\) = &qp\.default]` |
| `parameter-style-form-query-object` (`ore-bin-screen`) | `parameter.style=form` | a required query parameter whose schema resolves to an object with properties (an optional one is the `object-query-type-unsupported` refusal class), and the instrumented crozier run executes `src/emit.rs::append_request_call_args[\} else if qp\.convert \{]` |
| `parameter-schema` (`query-array-items-union`) | `parameter.schema` | as `query-array-items-union`, and the instrumented crozier run executes `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*element => element,]` |
| `parameter-schema` (`query-array-items-union`) | `parameter.schema` | as `query-array-items-union`, and the instrumented crozier run executes `src/ir.rs::InlineHoister::hoist_param_enum[if let Some\(\(item, members\)\) = schema]` |
| `parameter-schema` (`sensor-batch-query`) | `parameter.schema` | as `required-query-array-nullable-union-items`, and the instrumented crozier run executes `src/ir.rs::InlineHoister::hoist_param_enum[if composition_admits_null\(item, members\) \{]` |
| `fern-streaming-extension` (`stream-condition-union-body`) | `operation.x-fern-streaming` | as `fern-streaming-condition-union-body`, and the instrumented crozier run executes `src/ir.rs::declare_split_union_body[=tag_types\.push\(TagTypeDecl \{]` |
| `fern-streaming-extension` (`streaming-extension-terminator`) | `operation.x-fern-streaming` | as `fern-streaming-terminator`, and the instrumented crozier run executes `src/emit.rs::sse_end[=\x7cend\x7c format!]` |
| `x-fern-or-crozier-ignore` (`x-fern-ignore-schema`) | `schema.x-fern-ignore` | a `components.schemas` entry declaring `x-fern-ignore: true` (either spelling), and the instrumented crozier run executes `src/openapi.rs::filter_ignored[for key in &ignored_schemas \{]` |

### How a declarer was screened

[`census.tsv`](census.tsv) lists every declarer a detector counts, with its site count and outcome. A declarer is admissible under [`../../corpus-licensing.md`](../../corpus-licensing.md) through its own `info.license` or, declaring none, its repository's licence at the pinned commit. Each GitHub declarer took its licence, ref and Fern screens through `tools/witness-search/witness_screen.py` (licence-failing ones without the shared Fern lock, since that stage runs no Fern for them); each admissible one was generated by the certified pair and compared whole with crozier's output through `crozier compare`. A third-party copy of another publisher's description, a document a tool's own tests or examples carry, and a framework's example written to exercise an extension are refused as witnesses on provenance. Declarers in this repository's own fixtures, and in Fern's own repositories' test inputs, are excluded and not listed. A declarer an earlier record already decided keeps that decision, linked. Where the screening budget ran out, a declarer is named `outstanding` with what remains.

## Verdicts

The cover of each `search-incomplete` and `exhausted` key cites this table; a `golden` key's hand-written cover is retired.

| key | outcome | declarers | why |
|---|---|---|---|
| `client-header-date-format` | `search-incomplete` | 2 acquired | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `global-headers-extension` | `search-incomplete` | 3 GitHub | loonfs's own description (`loonfs/loonfs`, Apache-2.0) passes every screen, but crozier ignores `optional: true` on its `x-fern-global-headers`; honouring it amends `src/openapi.rs`'s frozen `GlobalHeaderExtension`, outside this node, so the candidate waits on that repair (drafted follow-up); the other declarers are copies or grant nothing |
| `nullable-array-query-explode-false` | `search-incomplete` | 1 APIs.guru | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `nullable-query-array-items` | `search-incomplete` | 18 acquired, 1 APIs.guru | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 9 declarer(s) outstanding |
| `parameter-default-extension` | `exhausted` | 0 | no real document declares it |
| `parameter-ignore-extension` | `exhausted` | 0 | no real document declares it |
| `parameter-name-extension` | `exhausted` | 2 acquired | its only declarers, two Cloudflare descriptions in the shared response cache, fail `fern check` (duplicate paths) by an earlier record |
| `parameter-without-location` | `search-incomplete` | 3 acquired, 1 GitHub | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `path-parameters-template-order-31` | `golden` | 109 acquired, 1 APIs.guru, 1 registered, 12 sibling | registered row 3001 `formbricks` declares it (3 operations) and its golden byte-matches |
| `query-date-union-oneof` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-nullable-query-scalar` | `search-incomplete` | 18 acquired, 1 APIs.guru | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 10 declarer(s) outstanding |
| `sdk-variable-parameter-extension` | `exhausted` | 0 | no real document declares it |
| `sdk-variables-extension` | `exhausted` | 0 | no real document declares it |
| `query-array-items-union` | `search-incomplete` | 16 acquired, 1 APIs.guru | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `header-subset-string-default` | `golden` | 12 acquired, 5 APIs.guru, 1 registered, 2 sibling | corpus row 4400 `notion-mcp-server` declares it and its golden byte-matches |
| `literal-prefixed-integer-path-segment` | `golden` | 17 acquired, 1 APIs.guru | corpus row 4404 `wiim-httpapi` declares it and its golden byte-matches |
| `query-param-ref-to-enum-or-array-union-converted` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-param-and-body-defaults-ignored` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `example-nested-array-two-items` | `search-incomplete` | 3 acquired | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 1 declarer(s) outstanding |
| `query-anyof-const-member-example-as-enum-member` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-query-array-nullable-union-items` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `security-scheme-header-extension-named` | `search-incomplete` | 13 GitHub | Persona's `persona-id/persona-openapi` (Apache 2.0, eight dated versions) is a multi-file description whose tree was not acquired in this dispatch; `darwin-studios/darwin-cli` passes every screen and differs in 10 files (drafted follow-up); a framework's examples are excluded |
| `security-scheme-bearer-extension-named` | `golden` | 2 acquired, 5 GitHub, 1 registered | corpus row 4402 `mcp-handle` declares it and its golden byte-matches |
| `security-scheme-basic-extension-named` | `golden` | 1 GitHub, 1 registered | corpus row 4401 `laposta` declares it and its golden byte-matches |
| `security-scheme-token-variable-name` | `exhausted` | 2 GitHub | its two declarers, Merge's `.mock` copies in `merge-api/merge-csharp-client`, name no grant the corpus rule admits |
| `security-schemes-duplicate-api-key-header` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `security-scheme-capitalised-http` | `golden` | 33 acquired, 6 GitHub, 5 sibling | corpus row 4403 `microsoft-adme-crs-converter` declares it and its golden byte-matches |
| `operation-sdk-group-name-leading-underscore` | `exhausted` | 1 GitHub | its one declarer, Seam's `seamapi/fake-seam-connect`, is refused by Fern (`fern check`: 41 errors) |
| `operation-sdk-group-name-without-method-name` | `exhausted` | 1 acquired, 4 GitHub | its declarers grant nothing (`SchematicHQ/schematic-fern-config`, `Inowu/wrestaurant-docs`, `qoretechnologies/qore`) or are a third-party copy of ElevenLabs' description |
| `operation-sdk-method-name-sequence` | `exhausted` | 0 | no real document declares it |
| `operation-idempotent-with-root-headers` | `exhausted` | 2 GitHub | its only declarers are a framework's conformance examples, written to exercise the extensions |
| `operation-retries-disabled` | `search-incomplete` | 1 GitHub | its one declarer, `loonfs/loonfs`, passes every screen and waits on the global-header repair above (drafted follow-up) |
| `operation-webhook-extension` | `exhausted` | 0 | no real document declares it |
| `operation-pagination-offset` | `exhausted` | 0 | no real document declares it |
| `operation-pagination-boolean` | `exhausted` | 0 | no real document declares it |
| `operation-group-types-beside-child-group` | `exhausted` | 1 GitHub | its one declarer, Seam's `seamapi/fake-seam-connect`, is refused by Fern (`fern check`: 41 errors) |
| `webhook-inline-json-body-named` | `exhausted` | 0 | no real document declares it |
| `fern-streaming-boolean` | `exhausted` | 1 acquired, 3 GitHub | its declarers are an aggregator's copies granting nothing (`api-evangelist/junction-com`) and a third-party copy of ElevenLabs' description |
| `fern-streaming-condition-ref-body-header` | `exhausted` | 0 | no real document declares it |
| `fern-streaming-condition-shared-body` | `exhausted` | 0 | no real document declares it |
| `fern-streaming-condition-union-body` | `exhausted` | 0 | no real document declares it |
| `fern-streaming-format-over-json` | `exhausted` | 2 GitHub | its declarers are a Fern documentation example and a web framework's example document |
| `fern-streaming-terminator` | `exhausted` | 5 GitHub | its declarers are a framework's examples and a Fern documentation example, written to exhibit the extension |
| `base-path-extension` | `exhausted` | 1 acquired, 1 GitHub | both declarers are refused by Fern: `danielkov/solder`'s example (`fern check` exit 1) and OpenRouter's description in `jentic/jentic-public-apis` (`type-name-collision`, an earlier record) |
| `discriminated-extension` | `exhausted` | 0 | no real document declares it |
| `discriminator-property-name-extension` | `exhausted` | 0 | no real document declares it |
| `combo-param-example-beside-ref-schema` | `search-incomplete` | 118 acquired, 13 APIs.guru, 6 GitHub, 5 registered, 5 sibling | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 125 declarer(s) outstanding |

## Arm verdicts

Each arm-level cover's verdict, naming the arm it covers.

| key | outcome | arm | fixture | why |
|---|---|---|---|---|
| `parameter-in-path` | `exhausted` | `src/ir.rs::lifted_client_path_parameters[\.map\(\x7cparameter\x7c ClientPathParameter \{]` | `base-path-client-argument` | no real document declares an `x-fern-base-path` whose `parameters` lift a placeholder |
| `http-dpop` | `exhausted` | `src/ir.rs::auth_model[=_ => Auth::None,]` | `http-dpop-unrequired` | every real DPoP declarer requires its only scheme, which Fern refuses (`Endpoint requires auth, but no auth is defined`, measured on `divyamohan1993/enterprise-sso-system`), so none reaches the arm |
| `http-mutual` | `exhausted` | `src/ir.rs::auth_model[=_ => Auth::None,]` | `http-mutual-unrequired` | its declarers, two `alexeit-315/rag-soc-core` documents, grant nothing |
| `http-negotiate` | `exhausted` | `src/ir.rs::auth_model[=_ => Auth::None,]` | `http-negotiate-unrequired` | no real document declares a negotiate scheme with no supported scheme beside it and no operation requiring it |
| `parameter-schema` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*TypeRef::Optional\(element\) => \*element,]` | `nullable-query-union-items` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `parameter-in-header` | `search-incomplete` | `src/ir.rs::header_py_type[=^\s*HeaderType::Date]` | `observatory-client-date` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `parameter-in-header` | `search-incomplete` | `src/ir.rs::global_headers[for header in doc\.global_header_extensions]` | `observatory-client-headers` | `loonfs/loonfs` would execute it once its global headers byte-match (drafted follow-up) |
| `parameter-in-path` | `exhausted` | `src/ir.rs::lifted_client_path_parameters[if let Some\(variable\) = parameter\.sdk_variable]` | `observatory-client-variable` | no real document declares `x-fern-sdk-variable` |
| `parameter-in-query` | `exhausted` | `src/emit.rs::method_params[if let Some\(default\) = &qp\.default]` | `observatory-query-extensions` | no real document declares `x-fern-default` |
| `parameter-style-form-query-object` | `search-incomplete` | `src/emit.rs::append_request_call_args[\} else if qp\.convert \{]` | `ore-bin-screen` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 60 declarer(s) outstanding |
| `parameter-schema` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_param_enum[if composition_admits_null\(item, members\) \{]` | `sensor-batch-query` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `fern-streaming-extension` | `exhausted` | `src/ir.rs::declare_split_union_body[=tag_types\.push\(TagTypeDecl \{]` | `stream-condition-union-body` | no real document declares a `stream-condition` over a union body |
| `fern-streaming-extension` | `exhausted` | `src/emit.rs::sse_end[=\x7cend\x7c format!]` | `streaming-extension-terminator` | no real document declares a `terminator` |
| `x-fern-or-crozier-ignore` | `search-incomplete` | `src/openapi.rs::filter_ignored[for key in &ignored_schemas \{]` | `x-fern-ignore-schema` | Fern's own `fern-api/docs` FAI description passes every screen and differs (Fern generates groups crozier omits), and the AssemblyAI description in `jentic/jentic-public-apis` is refused by crozier on an unresolved `links` reference: both wait on repairs (drafted follow-up) |

## Arms a real witness now executes

Their arm-level covers are retired: the instrumented run of the witness's golden test executes the arm, as [`../golden-reach.tsv`](../golden-reach.tsv) records.

| golden row | arm | retired cover | witness |
|---|---|---|---|
| `parameter-in-header` | `src/ir.rs::global_headers[Some\(default\) if count < total && py_type == HeaderType::Str => \{]` | `header-subset-string-default` | corpus row 4400 `notion-mcp-server` executes it |
| `parameter-schema` | `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*element => element,]` | `query-array-items-union` | corpus row 4402 `mcp-handle` executes it |
| `parameter-schema` | `src/ir.rs::InlineHoister::hoist_param_enum[if let Some\(\(item, members\)\) = schema]` | `query-array-items-union` | corpus row 4402 `mcp-handle` executes it |

## Renewed search

What became of each `search-incomplete` target's declarers: none is registrable on the finished tree.

| key | outcome | why |
|---|---|---|
| `client-header-date-format` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `global-headers-extension` | `none-registrable` | loonfs's own description (`loonfs/loonfs`, Apache-2.0) passes every screen, but crozier ignores `optional: true` on its `x-fern-global-headers`; honouring it amends `src/openapi.rs`'s frozen `GlobalHeaderExtension`, outside this node, so the candidate waits on that repair (drafted follow-up); the other declarers are copies or grant nothing |
| `nullable-array-query-explode-false` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `nullable-query-array-items` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 9 declarer(s) outstanding |
| `parameter-without-location` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `query-date-union-oneof` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-nullable-query-scalar` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 10 declarer(s) outstanding |
| `query-array-items-union` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `query-param-ref-to-enum-or-array-union-converted` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-param-and-body-defaults-ignored` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `example-nested-array-two-items` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 1 declarer(s) outstanding |
| `query-anyof-const-member-example-as-enum-member` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-query-array-nullable-union-items` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `security-scheme-header-extension-named` | `none-registrable` | Persona's `persona-id/persona-openapi` (Apache 2.0, eight dated versions) is a multi-file description whose tree was not acquired in this dispatch; `darwin-studios/darwin-cli` passes every screen and differs in 10 files (drafted follow-up); a framework's examples are excluded |
| `security-schemes-duplicate-api-key-header` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `operation-retries-disabled` | `none-registrable` | its one declarer, `loonfs/loonfs`, passes every screen and waits on the global-header repair above (drafted follow-up) |
| `combo-param-example-beside-ref-schema` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 125 declarer(s) outstanding |
| `parameter-schema` | `none-registrable` | no declarer of the arms this record searched for it executes them on a byte-matching golden |
| `parameter-in-header` | `none-registrable` | no declarer of the arms this record searched for it executes them on a byte-matching golden |
| `parameter-style-form-query-object` | `none-registrable` | no declarer of the arms this record searched for it executes them on a byte-matching golden |
| `x-fern-or-crozier-ignore` | `none-registrable` | no declarer of the arms this record searched for it executes them on a byte-matching golden |

## The real witnesses

Each witness is a publisher's or author's own document at an immutable commit,
under a grant the corpus rule admits, committed with its NOTICE entry and its
complete certified-pair golden, and gated by its corpus test. Crozier needed
three repairs to byte-match them, each with a unit test driving the touched
function on the triggering shape and an all-corpus check that no committed
golden moved: an inline union whose members tag `type` with a bare `const`
stays an ordinary union (Notion); a string example on a `boolean`, `integer`
or `number` schema is not a worked value (Laposta, measured against a
from-scratch probe under both the singular and the 3.1 array keyword); and a
nullable query array hoists its inline union item as the plain array does (MCP
Handle).

| key | witness | what its golden shows | comparison test |
|---|---|---|---|
| `path-parameters-template-order-31` | registered row 3001 `formbricks` (AGPL-3.0, Formbricks' own repository) | `get_team`, `update_team` and `delete_team` take `organization_id, id` in template order against the declared `[id, organizationId]` | `formbricks_matches_fern_output` |
| `header-subset-string-default` | row 4400 `notion-mcp-server`: `makenotion/notion-mcp-server` at `730ae781ba28beeaf0865025a3f2ed4c25ea2387` (MIT) | `Notion-Version`, defaulting to `2025-09-03` on 23 of 24 operations, is the client argument `notion_version: typing.Optional[typing.Literal["2025-09-03"]] = None` | `notion_mcp_server_matches_fern_output` |
| `security-scheme-basic-extension-named` | row 4401 `laposta`: `laposta/laposta-skill` at `a97773a9023708ab722e30f0e157a2b69fefc882` (MIT) | the basic credentials are the constructor arguments `api_key` and `leave_empty` | `laposta_matches_fern_output` |
| `security-scheme-bearer-extension-named` | row 4402 `mcp-handle`: `WeatherPal-AI/MCP-handle` at `9c59f16950d25e08c1058d8174e12b22861280d8` (Apache-2.0) | the bearer token is the constructor argument `api_key` | `mcp_handle_matches_fern_output` |
| `security-scheme-capitalised-http` | row 4403 `microsoft-adme-crs-converter`: `microsoft/adme-samples` at `df39d22ed32acfe80fcdbc5b554871b2c752a39a` (MIT), beside row 3004 | `scheme: Bearer` is the bearer `token` sent as `Authorization: Bearer …` | `microsoft_adme_crs_converter_matches_fern_output` |
| `literal-prefixed-integer-path-segment` | row 4404 `wiim-httpapi`: `cvdlinden/wiim-httpapi` at `3dce4a722aa2b30fdb06d720b58714e224d26eb6` (GPL-3.0) | `/setPlayerCmd:vol:{value}` is `set_player_cmd_vol(value: int)`, requesting `f"setPlayerCmd:vol:{encode_path_param(value)}"` | `wiim_httpapi_matches_fern_output` |

The arm witnesses are read off [`../golden-reach.tsv`](../golden-reach.tsv):
row 4400 executes `global_headers`' subset-default arm, and row 4402 executes
`hoist_param_enum`'s inline-union-item arms.

`fixture_only_real_witnesses_declare_their_shapes` in
[`../../../crates/crozier-e2e/tests/e2e/real_witnesses.rs`](../../../crates/crozier-e2e/tests/e2e/real_witnesses.rs)
holds each feature witness to its source and golden, so a regenerated golden or
a moved source that stops declaring the shape fails rather than leaving the
claim standing.

The superseded hand-written fixtures are retired: `observatory-route-order`,
`header-subset-string-default`, `lock-keeper-vault`, `ski-lift-gates`,
`tide-gauge-sessions` and `literal-prefixed-integer-path-segment`. The
three literals-mode measurements that read the security fixtures' documents
keep those documents beside their trees under
[`../../fern-measurements/clients-extensions/`](../../fern-measurements/clients-extensions/README.md);
the one that overlaid the path-segment fixture's tree is now a complete tree
of its own, and `observatory-route-order` leaves the parameter-literals
measurement's certified set.

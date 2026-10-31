# Witness search for the fixture-only parameter, security and extension proofs

Every target of the region files [`parameters.md`](../parameters.md), [`security.md`](../security.md) and [`oas31-extensions.md`](../oas31-extensions.md) whose proof, at this node's base (`1748b7946`), was a hand-written fixture: their `handwritten` feature rows, their one `handwritten` combination row, and every arm-level hand-written cover of one of their `golden` rows that [`../handwritten-reach.tsv`](../handwritten-reach.tsv) listed. None of their `golden` rows rested on a residual-only supplement (the one supplement, `schema-example-null`, is a `schemas.md` row). Each target was searched once, against the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3), for a real specification whose complete golden crozier byte-matches.

**Outcome.** 8 feature targets now rest on a registered real witness and 4 arm targets are executed by one; 32 targets are `exhausted`; 20 remain `search-incomplete`, each with its reason below. Seven corpus rows carry the witnesses: registered row 3001 `formbricks`, reused, and rows 4400 to 4405, added by this record.

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

Every live request went through [`tools/witness-search/rate_limit_guard.py`](../../../tools/witness-search/rate_limit_guard.py), by way of `tools/witness-search/witness-search-github.py`'s acquirer and `tools/witness-search/witness_screen.py`; the probes, waits and cache hits are under `.local/witness-search-fixture-only-operations-extensions/`. Live requests per bucket: `code_search` 153, `core` 1, and 4044 on the exact-commit raw lane (`raw.githubusercontent.com`, paced rather than percentage-guarded). The shared response cache answered 5071 requests at no cost. No GraphQL, Postman or SwaggerHub route was used.

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
| `global-headers-extension` | `golden` | 3 GitHub | corpus row 4405 `loonfs` declares it and its golden byte-matches, after the optional-header repair the manager authorized |
| `nullable-array-query-explode-false` | `search-incomplete` | 1 APIs.guru | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `nullable-query-array-items` | `search-incomplete` | 18 acquired, 1 APIs.guru | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 9 declarer(s) outstanding; the handed-off candidate unicourt (R4, R5) keeps it open ([handed-off differences](#handed-off-differences)) |
| `parameter-default-extension` | `exhausted` | 0 | no real document declares it |
| `parameter-ignore-extension` | `exhausted` | 0 | no real document declares it |
| `parameter-name-extension` | `exhausted` | 2 acquired | its only declarers, two Cloudflare descriptions in the shared response cache, fail `fern check` (duplicate paths) by an earlier record |
| `parameter-without-location` | `search-incomplete` | 3 acquired, 1 GitHub | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided; the handed-off candidates tacd (R1), AMRC cluster manager (R2) keep it open ([handed-off differences](#handed-off-differences)) |
| `path-parameters-template-order-31` | `golden` | 109 acquired, 1 APIs.guru, 1 registered, 12 sibling | registered row 3001 `formbricks` declares it (3 operations) and its golden byte-matches |
| `query-date-union-oneof` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-nullable-query-scalar` | `search-incomplete` | 18 acquired, 1 APIs.guru | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 10 declarer(s) outstanding; the handed-off candidate keyserv (R3) keeps it open ([handed-off differences](#handed-off-differences)) |
| `sdk-variable-parameter-extension` | `exhausted` | 0 | no real document declares it |
| `sdk-variables-extension` | `exhausted` | 0 | no real document declares it |
| `query-array-items-union` | `search-incomplete` | 16 acquired, 1 APIs.guru | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided; the handed-off candidate openaq (R6, R7) keeps it open ([handed-off differences](#handed-off-differences)) |
| `header-subset-string-default` | `golden` | 12 acquired, 5 APIs.guru, 1 registered, 2 sibling | corpus row 4400 `notion-mcp-server` declares it and its golden byte-matches |
| `literal-prefixed-integer-path-segment` | `golden` | 17 acquired, 1 APIs.guru | corpus row 4404 `wiim-httpapi` declares it and its golden byte-matches |
| `query-param-ref-to-enum-or-array-union-converted` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-param-and-body-defaults-ignored` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `example-nested-array-two-items` | `search-incomplete` | 3 acquired | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 1 declarer(s) outstanding |
| `query-anyof-const-member-example-as-enum-member` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-query-array-nullable-union-items` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `security-scheme-header-extension-named` | `search-incomplete` | 13 GitHub | Persona's `persona-id/persona-openapi` (Apache 2.0, eight dated versions) is a multi-file description whose tree was not acquired in this dispatch; `darwin-studios/darwin-cli` passes every screen and differs in 10 files (drafted follow-up); a framework's examples are excluded; the handed-off candidate darwin-cli (R9, R10) keeps it open ([handed-off differences](#handed-off-differences)) |
| `security-scheme-bearer-extension-named` | `golden` | 2 acquired, 5 GitHub, 1 registered | corpus row 4402 `mcp-handle` declares it and its golden byte-matches |
| `security-scheme-basic-extension-named` | `golden` | 1 GitHub, 1 registered | corpus row 4401 `laposta` declares it and its golden byte-matches |
| `security-scheme-token-variable-name` | `exhausted` | 2 GitHub | its two declarers, Merge's `.mock` copies in `merge-api/merge-csharp-client`, name no grant the corpus rule admits |
| `security-schemes-duplicate-api-key-header` | `search-incomplete` | 0 | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `security-scheme-capitalised-http` | `golden` | 33 acquired, 6 GitHub, 5 sibling | corpus row 4403 `microsoft-adme-crs-converter` declares it and its golden byte-matches |
| `operation-sdk-group-name-leading-underscore` | `exhausted` | 1 GitHub | its one declarer, Seam's `seamapi/fake-seam-connect`, is refused by Fern (`fern check`: 41 errors) |
| `operation-sdk-group-name-without-method-name` | `exhausted` | 1 acquired, 4 GitHub | its declarers grant nothing (`SchematicHQ/schematic-fern-config`, `Inowu/wrestaurant-docs`, `qoretechnologies/qore`) or are a third-party copy of ElevenLabs' description |
| `operation-sdk-method-name-sequence` | `exhausted` | 0 | no real document declares it |
| `operation-idempotent-with-root-headers` | `exhausted` | 2 GitHub | its only declarers are a framework's conformance examples, written to exercise the extensions |
| `operation-retries-disabled` | `golden` | 1 GitHub | corpus row 4405 `loonfs` declares it (7 operations) and its golden byte-matches |
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
| `parameter-in-path` | `exhausted` | `src/ir.rs::lifted_client_path_parameters[if let Some\(variable\) = parameter\.sdk_variable]` | `observatory-client-variable` | no real document declares `x-fern-sdk-variable` |
| `parameter-in-query` | `exhausted` | `src/emit.rs::method_params[if let Some\(default\) = &qp\.default]` | `observatory-query-extensions` | no real document declares `x-fern-default` |
| `parameter-style-form-query-object` | `search-incomplete` | `src/emit.rs::append_request_call_args[\} else if qp\.convert \{]` | `ore-bin-screen` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 60 declarer(s) outstanding; the handed-off candidate lolesports (R1) keeps it open ([handed-off differences](#handed-off-differences)) |
| `parameter-schema` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_param_enum[if composition_admits_null\(item, members\) \{]` | `sensor-batch-query` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `fern-streaming-extension` | `exhausted` | `src/ir.rs::declare_split_union_body[=tag_types\.push\(TagTypeDecl \{]` | `stream-condition-union-body` | no real document declares a `stream-condition` over a union body |
| `fern-streaming-extension` | `exhausted` | `src/emit.rs::sse_end[=\x7cend\x7c format!]` | `streaming-extension-terminator` | no real document declares a `terminator` |
| `x-fern-or-crozier-ignore` | `search-incomplete` | `src/openapi.rs::filter_ignored[for key in &ignored_schemas \{]` | `x-fern-ignore-schema` | Fern's own `fern-api/docs` FAI description passes every screen and differs (Fern generates groups crozier omits), and the AssemblyAI description in `jentic/jentic-public-apis` is refused by crozier on an unresolved `links` reference: both wait on repairs (drafted follow-up); the handed-off candidates Fern FAI (e82e728) (R12, R13), Fern FAI (6f9d392) (R12, R13), AssemblyAI bundle (R14) keep it open ([handed-off differences](#handed-off-differences)) |

## Arms a real witness now executes

Their arm-level covers are retired: the instrumented run of the witness's golden test executes the arm, as [`../golden-reach.tsv`](../golden-reach.tsv) records.

| golden row | arm | retired cover | witness |
|---|---|---|---|
| `parameter-in-header` | `src/ir.rs::global_headers[Some\(default\) if count < total && py_type == HeaderType::Str => \{]` | `header-subset-string-default` | corpus row 4400 `notion-mcp-server` executes it |
| `parameter-in-header` | `src/ir.rs::global_headers[for header in doc\.global_header_extensions]` | `observatory-client-headers` | corpus row 4405 `loonfs` executes it |
| `parameter-schema` | `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*element => element,]` | `query-array-items-union` | corpus row 4402 `mcp-handle` executes it |
| `parameter-schema` | `src/ir.rs::InlineHoister::hoist_param_enum[if let Some\(\(item, members\)\) = schema]` | `query-array-items-union` | corpus row 4402 `mcp-handle` executes it |

## Renewed search

What became of each `search-incomplete` target's declarers: none is registrable on the finished tree.

| key | outcome | why |
|---|---|---|
| `client-header-date-format` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `nullable-array-query-explode-false` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided |
| `nullable-query-array-items` | `none-registrable` | the search cannot finish: GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 9 declarer(s) outstanding; the handed-off candidate unicourt (R4, R5) keeps it open ([handed-off differences](#handed-off-differences)) |
| `parameter-without-location` | `none-registrable` | the search cannot finish: GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided; the handed-off candidates tacd (R1), AMRC cluster manager (R2) keep it open ([handed-off differences](#handed-off-differences)) |
| `query-date-union-oneof` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-nullable-query-scalar` | `none-registrable` | the search cannot finish: GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 10 declarer(s) outstanding; the handed-off candidate keyserv (R3) keeps it open ([handed-off differences](#handed-off-differences)) |
| `query-array-items-union` | `none-registrable` | the search cannot finish: GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); every declarer they hold is decided; the handed-off candidate openaq (R6, R7) keeps it open ([handed-off differences](#handed-off-differences)) |
| `query-param-ref-to-enum-or-array-union-converted` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-param-and-body-defaults-ignored` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `example-nested-array-two-items` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 1 declarer(s) outstanding |
| `query-anyof-const-member-example-as-enum-member` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `required-query-array-nullable-union-items` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `security-scheme-header-extension-named` | `none-registrable` | the search cannot finish: Persona's `persona-id/persona-openapi` (Apache 2.0, eight dated versions) is a multi-file description whose tree was not acquired in this dispatch; `darwin-studios/darwin-cli` passes every screen and differs in 10 files (drafted follow-up); a framework's examples are excluded; the handed-off candidate darwin-cli (R9, R10) keeps it open ([handed-off differences](#handed-off-differences)) |
| `security-schemes-duplicate-api-key-header` | `none-registrable` | no document in the populations read declares it, and GitHub code search has no phrase that selects the shape, so the public documents outside them cannot be enumerated |
| `combo-param-example-beside-ref-schema` | `none-registrable` | GitHub code search has no phrase that selects the shape, so the public documents outside the populations read cannot be enumerated; the declarers those populations hold are each decided or named outstanding in [`census.tsv`](census.tsv); 125 declarer(s) outstanding |
| `parameter-schema` | `none-registrable` | no declarer of the arms this record searched for it executes them on a byte-matching golden |
| `parameter-in-header` | `none-registrable` | no declarer of the arms this record searched for it executes them on a byte-matching golden |
| `parameter-style-form-query-object` | `none-registrable` | the search cannot finish: no declarer of the arms this record searched for it executes them on a byte-matching golden; the handed-off candidate lolesports (R1) keeps it open ([handed-off differences](#handed-off-differences)) |
| `x-fern-or-crozier-ignore` | `none-registrable` | the search cannot finish: no declarer of the arms this record searched for it executes them on a byte-matching golden; the handed-off candidates Fern FAI (e82e728) (R12, R13), Fern FAI (6f9d392) (R12, R13), AssemblyAI bundle (R14) keep it open ([handed-off differences](#handed-off-differences)) |

## Redundant divergent candidates

An admissible real declarer that the certified pair generates from, but
whose every target and arm a registered witness already proves, is not
registered; each divergence it shows is drafted as a follow-up with its
differing lines.

| candidate | screens | targets it would witness | already witnessed by | divergences (each a drafted follow-up) |
|---|---|---|---|---|
| `APIs-guru/openapi-directory:APIs/vtex.local/Marketplace-Protocol/1.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | licence passed (the aggregator's CC0), ref passed, Fern passed at 5.163.1 / 5.41.3; [measured record](vtex-marketplace-screen/screens.jsonl), filed `not-owed` | `header-subset-string-default` (7 sites) and its arm `src/ir.rs::global_headers[Some\(default\) if count < total && py_type == HeaderType::Str => \{]`; no other detector of this record fires on it | corpus row 4400 `notion-mcp-server` | crozier differs in 9 files and writes 3 more: worked calls order an optional query argument declared before a required one after it (`an`, `sc`); crozier exposes the required headers `content-length` and `x-forwarded-for`, which Fern drops; and crozier hoists models for untyped schemas that carry `items: {}` beside `properties`, which Fern types `List[Any]`. None touches the global header the target exercises |

## Handed-off differences

Every admissible declarer the certified pair generates from, where crozier's output differs, is handed off here at the manager's direction, not repaired in this record: a separate plan repairs each root cause, so crozier's output for these documents is unchanged by this record. The vtex Marketplace-Protocol differences are handed to the run's `vtex-output-parity` node, which is repairing them. Each document's files and first differing line pair are measured by `crozier compare` at this record's head against the certified pair's tree (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3); [`handed-off.tsv`](handed-off.tsv) lists every file each one touches.

### Root causes

Each is the rule crozier and the certified pair apply differently.

| root cause | rule |
|---|---|
| R1 | The certified pair's OpenAPI importer throws while reading the document (lolesports: `RangeError: Maximum call stack size exceeded` in its example builder; tacd: `TypeError: Cannot read properties of null (reading 'schema')`), logs `Failed to parse openapi document`, still exits 0, and writes an SDK skeleton with no groups, methods or types. crozier generates the document's whole SDK. |
| R2 | A path parameter declared without `required: true` (AMRC's shared `components.parameters.cluster`): the certified pair types it `typing.Optional[str]` and orders it among the optional arguments, so a binary-body operation lists `key` and the body before it in `reference.md`. crozier types every path parameter as a required `str`. |
| R3 | A schema that is `nullable: true` around a one-member `oneOf` naming a component: the certified pair keeps the component and makes it optional (a response returns `typing.Optional[CurrentKey]`; a request body is `request: typing.Optional[ProductCreateModify] = None`, and the component stays exported). crozier unwraps the member, returns it non-optional, and flattens a body into its properties. |
| R4 | A parameter that declares a schema `example` beside a parameter-level `examples` map: the certified pair works the call from the schema `example` (`attorney_id="ATTYgu01be2e4de654"`) and leaves out a parameter with no schema example. crozier takes the map's first value (`attorney_id="ATTYgr3ae043d84ebc"`, `q=""`). |
| R5 | An error response whose component is `nullable: true` (unicourt's `Exception`): the certified pair types the error body `typing.Optional[Exception]`. crozier types it `Exception`. |
| R6 | A parameter description that begins with a line break: the certified pair keeps a blank first line in the parameter's `reference.md` description. crozier drops it. |
| R7 | An operationId whose one-letter words are joined by runs of underscores (`…_mobile_generalized__z___x___y__pbf_get`): the certified pair names the derived request types `…ZxyPbfGet…`. crozier names them `…ZXYPbfGet…`. |
| R8 | An array whose `items` is `type: object` with a `oneOf` of inline members that declare no `type` (rd-alliance's `PatchRelation`): the certified pair hoists the item as a union (`PatchRelationItem` of `PatchRelationItemZero` and `PatchRelationItemOne`, with their `op` and `path` enums) and serializes the body through it. crozier leaves the item untyped, works it as `{"key": "value"}`, and passes the body as is. |
| R9 | A property whose inline `oneOf` names four components under a `discriminator` that gives only `propertyName` (darwin's `ActActionResponse.interaction`): the certified pair hoists it as `ActActionResponseInteraction`. crozier inlines a `typing.Union` of the four. |
| R10 | A discriminated union and its variants exported from `types/__init__.py`: the certified pair imports them in one parenthesized statement. crozier writes two `from .act_pay_request_source import …` statements. |
| R11 | An optional `type: array` query parameter whose declaration carries an `example` array (sumup's `users[]`, `statuses[]`, `payment_types[]`, `roles`): crozier works the example into the documented call and imports the enums its items name. The certified pair leaves the parameter out. |
| R12 | An operation whose JSON body `$ref`s a component marked `x-fern-ignore: true` (`CreateCodeRecordRequest`, `CreateDocumentRequest`): the certified pair keeps the operation with a `request: typing.Any` body passed whole. crozier finds the operation unemittable and writes no client for its group (`code`, `document`), only the group's `__init__.py`. |
| R13 | A query parameter `anyOf: [array of an inline string enum, null]` (`toggle_ask_ai`'s `locations`): the certified pair hoists the item enum as `ToggleAskAiRequestLocationsItem`. crozier types the item `typing.Union[typing.Literal["docs", "slack"], typing.Any]`. |
| R14 | A response `links` entry that `$ref`s an absent `#/components/links/…` entry: the certified pair ignores response links and generates. crozier refuses the document (`unresolved-reference`). |
| R15 | A binary-download operation (nextcloud's `core_avatar.get_avatar` and its kin): the certified pair's `reference.md` usage block is the bare `client.<group>.<method>(...)` line. crozier writes a worked client call. |
| R16 | A tag named `core`: both write that group's client into the package's runtime `core/` module. The certified pair keeps `core/__init__.py` as the runtime's export list and imports siblings as `.client_wrapper`; crozier's `core/__init__.py` is the group's, without the runtime's exports, and its group client imports `..core.client_wrapper`. |
| R17 | A worked call over an optional query parameter declared before a required one (vtex's `an`, `sc`): the certified pair keeps declaration order. crozier moves the optional argument after the required one. |
| R18 | Required `content-length` and `x-forwarded-for` header parameters: the certified pair drops them. crozier exposes them as arguments. |
| R19 | An untyped schema carrying `items: {}` beside `properties`: the certified pair types it `List[Any]`. crozier hoists a model for it. |

### Documents

| document | sha256 | targets it declares | files it touches | first differing line pair (certified pair, then crozier) | root cause | handed to |
|---|---|---|---|---|---|---|
| lolesports: `vickz84259/lolesports-api-docs:openapi.yaml@74027a7950c7e4629d3cab01ddd3990457a9956d` | `5737ba80e2e41e0bdf0f3e9079dcd757c16553d3f120b3f6d8bba6f3dc782d9c` | `parameter-style-form-query-object (ore-bin-screen)` | 6 differ (`README.md`, `reference.md`, `src/fern/__init__.py`, `src/fern/client.py` and 2 more); 208 only crozier writes (`src/fern/errors/__init__.py`, `src/fern/errors/not_found_error.py`, `src/fern/events/__init__.py`, `src/fern/events/client.py` and 204 more) | `README.md`: (no line) / `# Fern Python Library` | R1 | the repair plan |
| tacd: `linux-automation/tacd:openapi.yaml@df3958c92643f7e0b06ef1830b9bc2a5e55ab24a` | `b5dacb83849e3ef5b20249f712ed19ac60838e5052ce0a4de3b6c69aed29bd8c` | `parameter-without-location` | 4 differ (`README.md`, `reference.md`, `src/fern/__init__.py`, `src/fern/client.py`); 52 only crozier writes (`src/fern/dut_power/__init__.py`, `src/fern/dut_power/client.py`, `src/fern/dut_power/raw_client.py`, `src/fern/errors/__init__.py` and 48 more) | `README.md`: (no line) / `# Fern Python Library` | R1 | the repair plan |
| AMRC cluster manager: `AMRC-FactoryPlus/documentation:static/spec/cluster-manager.yaml@cfb2f488ff2f4b29c90235b12e9f8ed497772b59` | `be5e37894ab0582a6f6498609754319fcccdbbb140e7a055902d74534616fd8f` | `parameter-without-location`, `security-scheme-capitalised-http` | 3 differ (`reference.md`, `src/fern/client.py`, `src/fern/raw_client.py`) | `reference.md`: `` **cluster:** `typing.Optional[str]` — Cluster UUID `` / `` **cluster:** `str` — Cluster UUID `` | R2 | the repair plan |
| keyserv: `APIs-guru/openapi-directory:APIs/keyserv.solutions/1.4.5/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `7edd79beb9c490240ae09a653602cc5260ab66a422751d889ca7d63705b1552c` | `required-nullable-query-scalar` | 10 differ (`README.md`, `reference.md`, `src/fern/__init__.py`, `src/fern/keysapi/client.py` and 6 more); 1 only the certified pair writes (`src/fern/types/api_credentials.py`) | `README.md`: `from fern import FernApi, ProductCreateModify` / `from fern import FernApi` | R3 | the repair plan |
| unicourt: `APIs-guru/openapi-directory:APIs/unicourt.com/1.0.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `d8d536ea8daca766a98ec0db6599041cfdcc449b71f689df9046b88b9796a79d` | `nullable-query-array-items` | 37 differ (`reference.md`, `src/fern/attorney_analytics_api/client.py`, `src/fern/attorney_analytics_api/raw_client.py`, `src/fern/authentication_api/raw_client.py` and 33 more) | `reference.md`: `attorney_id="ATTYgu01be2e4de654",` / `attorney_id="ATTYgr3ae043d84ebc",` | R4, R5 | the repair plan |
| openaq: `APIs-guru/openapi-directory:APIs/openaq.local/2.0.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `468bf5eff16a3ec71979ee470a4e80f233c8f6ce67e93e118457fbe8e8efab91` | `query-array-items-union` | 18 differ (`reference.md`, `src/fern/__init__.py`, `src/fern/types/__init__.py`, `src/fern/types/get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_last_updated_from.py` and 14 more) | `reference.md`: (blank line) / (no line) | R6, R7 | the repair plan |
| rd-alliance catalog: `rd-alliance/metadata-catalog-v2:openapi.yaml@833c55f1ad8b6a19b77e8fc4f1d16133b8e5d624` | `c5da87bb95be6352daf5b5bda7b163916541e29123b94feb32e778f6367ad80a` | `literal-prefixed-integer-path-segment` | 11 differ (`reference.md`, `src/fern/__init__.py`, `src/fern/invrel/client.py`, `src/fern/invrel/raw_client.py` and 7 more); 12 only the certified pair writes (`src/fern/types/patch_inv_relation_item.py`, `src/fern/types/patch_inv_relation_item_one.py`, `src/fern/types/patch_inv_relation_item_one_op.py`, `src/fern/types/patch_inv_relation_item_zero.py` and 8 more) | `reference.md`: `from fern import FernApi, PatchRelationItemZero` / `from fern import FernApi` | R8 | the repair plan |
| darwin-cli: `darwin-studios/darwin-cli:openapi.json@0ae98a805869b7acabd737365c193b0afcbd0d7e` | `ee5e2a219e2f0911107a11eab0d98405e91f2b6d8fddf0f0d5730f445421a952` | `security-scheme-bearer-extension-named`, `security-scheme-header-extension-named` | 10 differ (`src/fern/__init__.py`, `src/fern/types/__init__.py`, `src/fern/types/act_action_response.py`, `src/fern/types/act_approve_action_response.py` and 6 more); 1 only the certified pair writes (`src/fern/types/act_action_response_interaction.py`) | `src/fern/__init__.py`: `ActActionResponseInteraction,` / (no line) | R9, R10 | the repair plan |
| sumup: `sumup/sumup-openapi:openapi.yaml@c359e2f1291fa81bb533298c5958ab95f0ba11c4` | `b1d4ab063c88dcadac6c303e5c7c6bf4fa90b823ba6b408c6437a712cc97c58f` | `security-scheme-capitalised-http` | 4 differ (`reference.md`, `src/fern/members/client.py`, `src/fern/memberships/client.py`, `src/fern/transactions/client.py`) | `reference.md`: `from fern import FernApi` / `from fern import FernApi, PaymentType, EntryMode` | R11 | the repair plan |
| Fern FAI (e82e728): `fern-api/docs:fern/apis/fai/openapi.json@e82e7289d69f082c6ee1d950bb7cb8d2c2d4b4a2` | `74ff1c45451650d7c723802727cea799f18174e9e72291777a5b81f013c678a4` | `x-fern-or-crozier-ignore (x-fern-ignore-schema)` | 7 differ (`reference.md`, `src/fern/__init__.py`, `src/fern/client.py`, `src/fern/settings/__init__.py` and 3 more); 5 only the certified pair writes (`src/fern/code/client.py`, `src/fern/code/raw_client.py`, `src/fern/document/client.py`, `src/fern/document/raw_client.py` and 1 more) | `reference.md`: `<details><summary><code>client.code.<a href="src/fern/code/client.py">create_code_record</a>(...) -> typing.List[CreateCodeRecordResponse]</code></summary>` / (no line) | R12, R13 | the repair plan |
| Fern FAI (6f9d392): `fern-api/docs:fern/apis/fai/openapi.json@6f9d392f0d7f48e9a86f3ead50ba72340567bd62` | `5aa6dbf5778778503f76e63dea7f13313434d0d883f25a93792190fba0a6f621` | `x-fern-or-crozier-ignore (x-fern-ignore-schema)` | 7 differ (`reference.md`, `src/fern/__init__.py`, `src/fern/client.py`, `src/fern/settings/__init__.py` and 3 more); 5 only the certified pair writes (`src/fern/code/client.py`, `src/fern/code/raw_client.py`, `src/fern/document/client.py`, `src/fern/document/raw_client.py` and 1 more) | `reference.md`: `<details><summary><code>client.code.<a href="src/fern/code/client.py">create_code_record</a>(...) -> typing.List[CreateCodeRecordResponse]</code></summary>` / (no line) | R12, R13 | the repair plan |
| AssemblyAI bundle: `jentic/jentic-public-apis:apis/openapi/assemblyai.com/main/1.3.4/meta/import/input-bundle.json@c72e13e0f80e71997209aba985eff6ef34869cd7` | `2011299d2095426af64fdf2209daa58c58152a09d34980717a048cf406b67a87` | `x-fern-or-crozier-ignore (x-fern-ignore-schema)` | 160 only the certified pair writes (`.fern/metadata.json`, `CONTRIBUTING.md`, `README.md`, `pyproject.toml` and 156 more) | `README.md`: `# Fern Python Library` / (crozier refuses the document: `unresolved-reference` at `paths//v2/transcript/post/responses/200/links/GetTranscriptById`) | R14 | the repair plan |
| nextcloud: `nextcloud/client-sdks:go/api/openapi.yaml@02bc7281ee36fe8862a61e94e12c91381c5866bf` | `adbf311837cc8d83ef91b6c826c003e0fa25b437abebe8f902180600109443b9` | `header-subset-string-default` | 9 differ (`reference.md`, `src/fern/core/__init__.py`, `src/fern/core/client.py`, `src/fern/core/raw_client.py` and 5 more) | `reference.md`: `client.core_avatar.get_avatar_dark(...)` / `from fern import FernApi` | R15, R16 | the repair plan |
| vtex Marketplace Protocol: `APIs-guru/openapi-directory:APIs/vtex.local/Marketplace-Protocol/1.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `748ff9ba7fba914537047a5198e24da9d32e64608cede2a67f9561cd53cee743` | `header-subset-string-default` | 9 differ (`reference.md`, `src/fern/__init__.py`, `src/fern/external_marketplace/__init__.py`, `src/fern/external_marketplace/client.py` and 5 more); 3 only crozier writes (`src/fern/external_marketplace/types/fulfillment_simulation_external_marketplace_response_logistics_info_item_item_metadata_items_item_assembly_options.py`, `src/fern/external_marketplace/types/fulfillment_simulation_external_marketplace_response_payment_data_installment_options.py`, `src/fern/external_marketplace/types/fulfillment_simulation_external_marketplace_response_payment_data_installment_options_installments.py`) | `reference.md`: `an="apiexamples",` / (no line) | R17, R18, R19 | the `vtex-output-parity` node |

### Declarers outside the handed-off set

- `swagger-api/swagger-parser:modules/swagger-parser-v3/src/test/resources/flattenArrayItems.yaml@69f6d78250b70d2ccfcd306ff0aa74353a698f2a` and `ballerina-platform/openapi-tools:openapi-cli/src/test/resources/generators/client/file_provider/swagger/openapi.yaml@ec1eec54e9404ce1e5fbe709b76187c588b512ab` are tools' own test documents, refused as witnesses on provenance, so they are not handed off. The certified pair still generates from both and crozier differs: swagger-parser's union members name components the document never defines, which the certified pair hoists as item aliases (`GetParametersRequestPagelimit`) where crozier writes `typing.Any`; ballerina's one untagged operation gets a `send_email` sub-client from the certified pair, where crozier puts it on the root client.
- `Ajey95/Insurance-Copilot:backend/mcp-bundles/notionhq-notion-mcp-server/scripts/notion-openapi.json@6332cd5dbc65dd8ad694b39a31c1691ade7f343b` (sha256 `2564039e86f4318021736368992591ef9768e9d8e7935999519b10186480153f`) now byte-matches its certified-pair tree after the Notion repair. It is a third-party copy of Notion's description, whose publisher's own copy is row 4400, so it is no witness.
- `jentic/jentic-public-apis:apis/openapi/assemblyai.com/main/1.3.4/meta/source/source.dat@c72e13e0f80e71997209aba985eff6ef34869cd7` is the raw source of the AssemblyAI bundle above, not a document as is; it carries the same unresolved `links` reference (R14).
- `axsys-org/shrine-extras:mounts/openrouter/openrouter.json@dc5116e8d71dd63ba7377bf5c3379b9511022616` is a copy of OpenRouter's description whose provenance is unproven, so it is not admissible; crozier refuses it (`example-not-enum-value`). The declarers [`census.tsv`](census.tsv) names only by sha256, which crozier refuses on an unresolved reference, were never licence-screened by the record that decided them, so their admissibility is undecided.


## The real witnesses

Each witness is a publisher's or author's own document at an immutable commit,
under a grant the corpus rule admits, committed with its NOTICE entry and its
complete certified-pair golden, and gated by its corpus test. Crozier needed
seven repairs to byte-match them, each with a unit test driving the touched
code on the triggering shape and an all-corpus check that no committed golden
moved: an inline union whose members tag `type` with a bare `const` stays an
ordinary union (Notion); a string example on a `boolean`, `integer` or
`number` schema is not a worked value (Laposta, measured against a
from-scratch probe under both the singular and the 3.1 array keyword); a
nullable query array hoists its inline union item as the plain array does (MCP
Handle); and, for LoonFS, an `optional: true` global header is
`Optional[str] = None` and left out of worked clients, the README's pagination
call carries its worked arguments, a download its media type makes under a
schema that is no `format: binary` string is worked without its optional
declared examples, and a discriminated variant's property naming a component
takes that component's example. The optional-header repair adds one
field, `optional: Option<bool>`, to `src/openapi.rs`'s `GlobalHeaderExtension`,
a change to that run-frozen interface the manager authorized; a document
without the key deserializes and generates as before.

| key | witness | what its golden shows | comparison test |
|---|---|---|---|
| `path-parameters-template-order-31` | registered row 3001 `formbricks` (AGPL-3.0, Formbricks' own repository) | `get_team`, `update_team` and `delete_team` take `organization_id, id` in template order against the declared `[id, organizationId]` | `formbricks_matches_fern_output` |
| `header-subset-string-default` | row 4400 `notion-mcp-server`: `makenotion/notion-mcp-server` at `730ae781ba28beeaf0865025a3f2ed4c25ea2387` (MIT) | `Notion-Version`, defaulting to `2025-09-03` on 23 of 24 operations, is the client argument `notion_version: typing.Optional[typing.Literal["2025-09-03"]] = None` | `notion_mcp_server_matches_fern_output` |
| `security-scheme-basic-extension-named` | row 4401 `laposta`: `laposta/laposta-skill` at `a97773a9023708ab722e30f0e157a2b69fefc882` (MIT) | the basic credentials are the constructor arguments `api_key` and `leave_empty` | `laposta_matches_fern_output` |
| `security-scheme-bearer-extension-named` | row 4402 `mcp-handle`: `WeatherPal-AI/MCP-handle` at `9c59f16950d25e08c1058d8174e12b22861280d8` (Apache-2.0) | the bearer token is the constructor argument `api_key` | `mcp_handle_matches_fern_output` |
| `security-scheme-capitalised-http` | row 4403 `microsoft-adme-crs-converter`: `microsoft/adme-samples` at `df39d22ed32acfe80fcdbc5b554871b2c752a39a` (MIT), beside row 3004 | `scheme: Bearer` is the bearer `token` sent as `Authorization: Bearer …` | `microsoft_adme_crs_converter_matches_fern_output` |
| `literal-prefixed-integer-path-segment` | row 4404 `wiim-httpapi`: `cvdlinden/wiim-httpapi` at `3dce4a722aa2b30fdb06d720b58714e224d26eb6` (GPL-3.0) | `/setPlayerCmd:vol:{value}` is `set_player_cmd_vol(value: int)`, requesting `f"setPlayerCmd:vol:{encode_path_param(value)}"` | `wiim_httpapi_matches_fern_output` |
| `global-headers-extension` | row 4405 `loonfs`: `loonfs/loonfs` at `1e9aebea7e6fca3ea5f32d33b066e39228131208` (Apache-2.0) | `Loonfs-Actor` and three siblings, marked `optional: true`, are `actor_id: typing.Optional[str] = None` and its kin, set only when given | `loonfs_matches_fern_output` |
| `operation-retries-disabled` | row 4405 `loonfs` | seven operations, `create_upload` among them, are sent with `max_retries` set to 0 | `loonfs_matches_fern_output` |

The arm witnesses are read off [`../golden-reach.tsv`](../golden-reach.tsv):
row 4400 executes `global_headers`' subset-default arm, row 4402
`hoist_param_enum`'s inline-union-item arms, and row 4405 `global_headers`'
loop over the declared extension headers.

`fixture_only_real_witnesses_declare_their_shapes` in
[`../../../crates/crozier-e2e/tests/e2e/real_witnesses.rs`](../../../crates/crozier-e2e/tests/e2e/real_witnesses.rs)
holds each feature witness to its source and golden, so a regenerated golden or
a moved source that stops declaring the shape fails rather than leaving the
claim standing.

The superseded hand-written fixtures are retired: `observatory-route-order`,
`header-subset-string-default`, `lock-keeper-vault`, `ski-lift-gates`,
`tide-gauge-sessions`, `literal-prefixed-integer-path-segment`,
`observatory-client-headers` and `warehouse-header-token`, and
`parcel-courier-desk` keeps only its idempotency cover. The last two whole
fixtures' documents and trees are inputs to other tests, so they stay measured
as [parameter-lowering](../../fern-measurements/parameter-lowering/README.md)
cases. The
three literals-mode measurements that read the security fixtures' documents
keep those documents beside their trees under
[`../../fern-measurements/clients-extensions/`](../../fern-measurements/clients-extensions/README.md);
the one that overlaid the path-segment fixture's tree is now a complete tree
of its own, and `observatory-route-order` leaves the parameter-literals
measurement's certified set.

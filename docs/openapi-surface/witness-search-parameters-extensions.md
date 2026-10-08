# Parameter extension and serialization witness search

## Witness search

The search is **search-incomplete**: it does not claim every public API was
queried. A census of the 243 registered golden sources before this change found
no declaration of the precise new lowering predicates below. The source bytes
and canonical census walker are committed; the additional registered AWS source
is described separately below. Handwritten fixtures prove behavior, not real
occurrence.

The renewed bounded search read 9,002 source-document files already acquired in
the GitHub REST code-search and Sourcegraph public-document pools in this
checkout. 7,400 parsed as OpenAPI 3.x documents. Purpose-written tool examples
are excluded from real witness admission. No new search endpoint was queried.
The six publisher descriptions selected for renewed certification are recorded
with immutable full revisions and source digests below. The public sources were
re-fetched through `scripts/rate_limit_guard.py`; every request reserved the
core bucket at its standing 70% cap. No GraphQL, Postman or SwaggerHub acquisition
was used. Remaining candidates are unverified, so this is a bounded renewal,
not an exhaustive absence claim.

| key | verdict | registered declarations before change | renewed outcome | complete-trigger evidence |
|---|---|---|---|---|
| `client-header-date-format` | `search-incomplete` | 0 (`parameter.schema:promoted-date-header`) | none-registrable | Polygres has a date header, but its schema omits type; the boundary refuses before constructor emission. The typed promoted-date trigger remains uncovered. |
| `global-headers-extension` | `search-incomplete` | 0 (`openapi.x-fern-global-headers`) | none-registrable | No selected publisher description declares the structured global-header extension. |
| `nullable-array-query-explode-false` | `search-incomplete` | 0 (`parameter.schema:nullable-array-explode-false`) | none-registrable | No selected publisher description declares the nullable array, optional form query and explode=false conjunction. |
| `nullable-query-array-items` | `search-incomplete` | 0 (`parameter.schema:nullable-array-items-30`) | none-registrable | CellEngine declares nullable inline scalar query-array items, but certified generation refuses unreferenced path parameters. |
| `parameter-default-extension` | `search-incomplete` | 0 (`parameter.x-fern-default`) | none-registrable | No publisher description in the renewed selection declares a string-valued parameter extension default. |
| `parameter-ignore-extension` | `search-incomplete` | 0 (`parameter.x-fern-ignore`) | none-registrable | No publisher description in the renewed selection declares ignored inline query parameters. |
| `parameter-name-extension` | `search-incomplete` | 0 (`parameter.x-fern-parameter-name`) | none-registrable | No publisher description in the renewed selection declares a query argument rename. |
| `parameter-without-location` | `search-incomplete` | 0 (`parameter.in:absent`) | none-registrable | LXA TAC includes location-less component parameters, but whole SDK parity differs; it supplies no accepted inline-operation proof. |
| `path-parameters-template-order-31` | `search-incomplete` | 0 (`operation.parameters:path-order-31`) | none-registrable | Stilla declares the complete ordering trigger but has request-body/example differences; Stellar Expert is refused by the certified pair. |
| `query-date-union-oneof` | `search-incomplete` | 0 (`parameter.schema:date-union-query-oneof`) | none-registrable | No selected publisher description declares an inline integer/date query oneOf. |
| `required-nullable-query-scalar` | `search-incomplete` | 0 (`parameter.schema:required-nullable-scalar-30`) | none-registrable | Longbridge declares required nullable scalar queries, but no publisher grant was verified at the probed root LICENSE path and certified generation fails ruff. |
| `sdk-variable-parameter-extension` | `search-incomplete` | 0 (`parameter.x-fern-sdk-variable`) | none-registrable | No selected publisher description links a path parameter to a document SDK variable. |
| `sdk-variables-extension` | `search-incomplete` | 0 (`openapi.x-fern-sdk-variables`) | none-registrable | No selected publisher description declares document SDK variables. |
| `base-path-extension` | `search-incomplete` | The earlier [base-path search](witness-search-parameter-lowering/README.md) remains applicable | none-registrable | The renewed selection declares no structured defaulted base path repeated in its URL paths. |

The arm-level searches use the same bounded renewal. Each is distinct from its
broad feature, which real sources already declare.

| key | verdict | arm | renewed outcome |
|---|---|---|---|
| `parameter-in-header` | `search-incomplete` | `src/ir.rs::header_py_type[=^\s*HeaderType::Date]` | none-registrable |
| `parameter-in-header` | `search-incomplete` | `src/ir.rs::global_headers[for header in doc\.global_header_extensions]` | none-registrable |
| `parameter-in-path` | `search-incomplete` | `src/ir.rs::lifted_client_path_parameters[if let Some\(variable\) = parameter\.sdk_variable]` | none-registrable |
| `parameter-in-query` | `search-incomplete` | `src/emit.rs::method_params[if let Some\(default\) = &qp\.default]` | none-registrable |

## Renewed publisher measurements

Every run pins CLI 5.67.1 and `fernapi/fern-python-sdk` 5.20.0, Python enums,
package `fern`, project `default_package_name`, client `FernApi`, extra fields
`allow`, default retries 2, all audiences, packaged preview, and CI/GitHub
metadata. No accepted output was edited. The comparison uses `src/parity.rs`
bidirectionally and only its compiled departure catalog.

| candidate | publisher document | full revision | source SHA-256 | certified outcome |
|---|---|---|---|---|
| stilla-path-order | [aeekayy/stilla](https://raw.githubusercontent.com/aeekayy/stilla/37b99e79c0f20fee6c2b79e7efc0a9859ac5591f/service/pkg/api/api/openapi.yaml) | `37b99e79c0f20fee6c2b79e7efc0a9859ac5591f` | `29e3591a97acc101523193bdbda0e1a1ba3f02f1114544a6e893848734bc4fe5` | accepted; complete parity differs ([exact diff](witness-search-parameters-extension-evidence/stilla-path-order-diff.txt)) |
| cellengine-nullable-items | [cellengine/cellengine-open-api-spec](https://raw.githubusercontent.com/cellengine/cellengine-open-api-spec/a425d8572ff45560b640ed5c046abd2de4fddb68/openapi.json) | `a425d8572ff45560b640ed5c046abd2de4fddb68` | `6910e12959fb37878869906749feff77a9dcdb73e96b36b88fc7eab07ab42363` | refused, exit 1 ([measurement](witness-search-parameters-extension-evidence/cellengine-nullable-items-refusal.txt)) |
| longbridge-nullable-query | [longbridge/developers](https://raw.githubusercontent.com/longbridge/developers/551e371b7fd3e5d593c485ccad15228a2cdc9776/openapi.yaml) | `551e371b7fd3e5d593c485ccad15228a2cdc9776` | `6d911f32e8ea2dde1bc0b4079f008e070b85dc7d144342000338fc989652dd64` | refused, exit 1 ([measurement](witness-search-parameters-extension-evidence/longbridge-nullable-query-refusal.txt)) |
| polygres-date-header | [Evokoa/polygres-sdk](https://raw.githubusercontent.com/Evokoa/polygres-sdk/b4ede83f0dd7176a49b468ac3814ec49106e9291/src/polygres/spec/runtime-v1.openapi.json) | `b4ede83f0dd7176a49b468ac3814ec49106e9291` | `025cd07b615587ca3f86ff573dbe84601fed140331bfeec100f200cd8b7f6c36` | accepted; crozier refuses generator-missing-type ([diagnostic](witness-search-parameters-extension-evidence/polygres-date-header-crozier.txt)) |
| tacd-unlocated-parameter | [linux-automation/tacd](https://raw.githubusercontent.com/linux-automation/tacd/df3958c92643f7e0b06ef1830b9bc2a5e55ab24a/openapi.yaml) | `df3958c92643f7e0b06ef1830b9bc2a5e55ab24a` | `b5dacb83849e3ef5b20249f712ed19ac60838e5052ce0a4de3b6c69aed29bd8c` | accepted; complete parity differs ([exact diff](witness-search-parameters-extension-evidence/tacd-unlocated-parameter-diff.txt)) |
| stellar-path-order | [stellar-expert/stellar-expert-explorer](https://raw.githubusercontent.com/stellar-expert/stellar-expert-explorer/308ef220358192911525272d9ad251225dd1e00b/open-api/openapi.yml) | `308ef220358192911525272d9ad251225dd1e00b` | `5d96955edab4762fc71b8b3f3b1a102873c53b0f3fba4e5998b523eeb87ae96a` | refused, exit 1 ([measurement](witness-search-parameters-extension-evidence/stellar-path-order-refusal.txt)) |

Stilla's five remaining paths are `README.md`, `reference.md`,
`src/fern/audit/client.py`, `src/fern/config/client.py`, and
`src/fern/config/raw_client.py`. Untyped/example-only request fields render
strings in the reference and dictionaries in crozier; documentation additionally
passes requester/config/parents. This is an unresolved request-body/example seam,
not an ordering failure, and is recorded as a separate follow-up.

Polygres is partial: a date-formatted component parameter has no declared type.
LXA TAC has broad model, response and documentation mismatches; its location-less
component declaration does not replace the independently authored inline scalar
operation proof. Neither SDK can be registered as a byte-exact witness. CellEngine
and Stellar Expert fail before producing a complete SDK; Longbridge fails its
registry's grant screen and the certified generation run. The remaining cache
candidates have not completed these admission screens.

## Registered publisher witness

Corpus row 1800, `aws-mobileanalytics`, is the AWS Mobile Analytics description
published by the APIs.guru converter at immutable revision
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`. Its `info.x-origin` identifies the
publisher's service model and its `info.license` grants redistribution under
[the corpus policy](../corpus-licensing.md). The complete unchanged source is
committed with its URL and SHA-256 in `tests/fixtures/corpus-sources.tsv`, and
its attribution is retained in `NOTICE`. It declares a required
`X-Amz-Client-Context` header on its only operation: a complete real witness for
`single-operation-required-header-promoted`. Both certified enum settings have
complete output gates, and the generated public method is driven through a
local HTTP transport to assert the constructor header on the wire and rejection
of an incorrectly supplied method argument.

## Authored proofs and settings

The new handwritten documents recreate only the relevant parameter/header/query
shapes, with unrelated service names, routes and values. Each records its exact
certified tree digest and pin in `evidence.toml`. Their Python-enum output and
[literals measurements](../fern-measurements/parameter-literals/README.md) are
complete tree comparisons. Alias journeys use both spellings and conflicting
values. The separate wire journey verifies values, signatures, defaults and
positional ordering, including failure and recovery cases.

The independently authored `warehouse-header-token` additionally proves that
a structured global-header declaration passes its wire name through unchanged.
It uses the same `global-headers-extension` search above: no selected publisher
description declares that extension, so the invalid-token variation also has
no complete real witness. This is **search-incomplete**, not a claim that no
public description could contain it. The certified accepted outputs and the
direct unknown-alias observation are recorded in
[`header-token-alias`](../fern-measurements/header-token-alias/README.md).

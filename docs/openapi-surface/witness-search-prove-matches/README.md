# Witness search for thirty shapes crozier already matches

Thirty shapes where crozier and Fern (CLI 5.67.1, `fernapi/fern-python-sdk`
5.20.0) generate the same bytes, but no committed artifact proved it. Each needs
a real specification whose complete golden crozier byte-matches, or, failing
one, a hand-written fixture under [`../handwritten/`](../handwritten/AGENTS.md)
whose cover cites the verdict below. Every shape is also measured under Fern's
default `enum_type` (`literals`) in
[`../../fern-measurements/literals-mode/`](../../fern-measurements/literals-mode/README.md).

## The search

Two populations, each read by one detector per shape (below):

- **APIs.guru.** `APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, the revision the corpus's
  `github-raw` APIs.guru rows already pin, fetched once as its archive
  (SHA-256 `816adb9fb4e19dc9ab28d7ad95363de146251fb41164abdb86f953f9f400c644`)
  through `tools/witness-search/rate_limit_guard.py` on 2026-10-09: one `core`
  call for the archive's address and one for its download. Its 1,970
  `openapi.yaml` documents are the OpenAPI 3 ones; 1,969 were read (PyYAML's
  C loader, then a timestamp-free loader for ten its first pass refused).
  `bunq.com/1.0` could not be parsed; its served JSON is registered as the
  corpus's `bunq.com` and is read in the second population.
- **The registered corpus.** All 257 documents under `tests/fixtures/` (each
  corpus source and each vendored fixture `openapi.*`).

[`census.tsv`](census.tsv) lists every document either detector counts for a
key, with its strict and loose site counts. A **strict** site declares the
whole trigger; a **loose** one declares part of it, and is listed so that the
missing portion is on record. GitHub code search, Sourcegraph, the vendor
portals and the registries were not queried for these keys, so no key is
`exhausted`.

### The detectors

| key | strict site | loose site |
|---|---|---|
| `bigint-format-string-typed-str` | object property `type: string, format: bigint` | any property with `format: bigint` |
| `described-ref-oneof-alias-without-docstring` | component with a `description`, no `discriminator`, `properties` or `allOf`, whose `oneOf` lists only `$ref`s to object schemas | a described component `oneOf` of `$ref`s |
| `discriminated-variant-date-value-snippet` | component `oneOf`/`anyOf` with a `discriminator`, used as a JSON request body by `$ref`, whose variants declare both a `format: date` and a `format: date-time` property | a discriminated union whose variants declare either |
| `dotted-mapping-key-variant-class-name` | `oneOf` discriminator whose `mapping` has a key containing `.` | the same under `anyOf` |
| `empty-path-segment-double-slash-kept` | a templated Paths key containing `//` | any Paths key containing `//` |
| `enum-extension-names-dropped-under-literals` | described string enum with a symbol-only value whose `x-fern-enum` gives every value a `name` and a `description` | any string enum with `x-fern-enum` |
| `enum-header-params-stringified` | an operation, beside another, with a required query parameter and both a required and an optional header whose schema `$ref`s a string enum | any header `$ref`ing a string enum |
| `enum-union-body-example-first-member-value` | JSON request body `oneOf`/`anyOf` whose first member is a string enum, with no example | the same with an example |
| `group-path-ending-in-api-nested-package` | `x-fern-sdk-group-name` of two segments, the last `api` | any whose last segment is `api` |
| `literal-enum-description-omitted` | component string enum with a `description` | — |
| `literal-enum-value-quote-escaping` | one string enum carrying a backslash, a double quote, an apostrophe, both quotes in one value and a non-ASCII character | an enum value with a backslash or either quote |
| `literal-prefixed-integer-path-segment` | a path segment of literal text then one `{param}` typed `integer` | the same segment over any type |
| `multipart-inline-object-part-json-encoded` | `multipart/form-data` object with a `format: binary` property beside an inline object property with `properties` | the inline object part alone |
| `multipart-part-encoding-charset-tuple` | `multipart/form-data` `encoding.<part>.contentType` naming a `charset` | any `encoding.<part>.contentType` |
| `multipart-single-value-enum-part-kept-optional` | `multipart/form-data` property, not required, a string enum of one value | the same, required |
| `oneof-duplicate-members-collapsed` | `oneOf` with two JSON-identical inline members | two identical members of any kind |
| `open-object-body-example-extra-keys-dropped` | inline JSON request body with `properties` and `additionalProperties: true` whose example has a key outside `properties` | the same with no such key |
| `patch-inline-nullable-unrequired-props-omit` | PATCH inline JSON body, nothing required, every property nullable | nothing required |
| `query-param-ref-to-enum-or-array-union-converted` | optional query parameter `$ref` to `oneOf [$ref E, array of $ref E]`, E a string enum | the same, required |
| `required-and-nullable-property-defaults-none` | property listed in `required` with `nullable: true` | — |
| `required-param-and-body-defaults-ignored` | an operation with a required integer query parameter carrying `default` and an inline JSON body whose required string property carries `default` | either half |
| `snake-case-component-name-pascal-class` | component schema named in `snake_case` | — |
| `stream-error-status-raises-typed-error` | `200` with `text/event-stream` content beside a `400` with `application/json` content | the `200` alone |
| `string-body-example-backslash-escaped` | JSON request body typed `string` whose example holds a literal `\n` or `\t` | any backslash |
| `undiscriminated-ref-oneof-sibling-properties-dropped` | schema with `properties` beside a two-member `oneOf` of `$ref`s and no `discriminator` | any member count or kind |
| `union-of-enum-ref-const-and-string-members` | `oneOf` of a `$ref` string enum, a `type: string` `const` and a plain `type: string` | an enum `$ref` beside either |
| `union-of-two-enum-refs-alias` | component `oneOf` of exactly two `$ref`s to string enums | two or more, or `anyOf` |
| `variant-nullable-value-optional-default-none` | discriminated `$ref` variant whose non-discriminant property is required and nullable | the same, not required |
| `variant-optional-const-discriminant-merged` | discriminated `$ref` variant declaring the discriminator property as a non-required `const` | the same, required |
| `variant-own-fields-before-allof-parent-fields` | discriminated `$ref` variant with its own `properties` and an `allOf` holding a `$ref` | — |

### How a declarer was screened

A strict APIs.guru declarer is admissible under
[`../../corpus-licensing.md`](../../corpus-licensing.md) through its own
`info.license`, or, declaring none, through the aggregating repository's own
licence, as corpus rows 114 to 121 are. Each admissible one was generated by
the pinned Fern pair with `tools/fern-goldens/generate-fern-fixture.sh` and,
where Fern generated, compared with crozier's output. A registered declarer
already carries a byte-matched golden.

## Verdicts

The hand-written fixture of each key below cites this table. The selector is
the key's census selector in
[`../witness-search-keys.tsv`](../witness-search-keys.tsv); the census
grammar has no predicate for the shapes themselves, so each is the nearest
selector the fixture declares, and the detector above is what the search ran.

| key | outcome | selector | strict declarers |
|---|---|---|---|
| `bigint-format-string-typed-str` | `search-incomplete` | `schema.format=bigint` | 0 |
| `described-ref-oneof-alias-without-docstring` | `search-incomplete` | `schema.description` | 5 APIs.guru, 5 registered |
| `discriminated-variant-date-value-snippet` | `search-incomplete` | `schema.format=date` | 0 |
| `empty-path-segment-double-slash-kept` | `search-incomplete` | `openapi.paths:several-template-expressions` | 2 APIs.guru |
| `enum-union-body-example-first-member-value` | `search-incomplete` | `schema.enum:string-valued` | 0 |
| `group-path-ending-in-api-nested-package` | `search-incomplete` | `operation.x-fern-sdk-group-name` | 0 |
| `literal-enum-value-quote-escaping` | `search-incomplete` | `schema.enum:apostrophe-member` | 0 |
| `literal-prefixed-integer-path-segment` | `search-incomplete` | `openapi.paths:templated-key` | 1 APIs.guru |
| `multipart-inline-object-part-json-encoded` | `search-incomplete` | `schema.format=binary` | 3 APIs.guru, 1 registered |
| `multipart-part-encoding-charset-tuple` | `search-incomplete` | `mediaType.encoding.contentType` | 0 |
| `oneof-duplicate-members-collapsed` | `search-incomplete` | `schema.oneOf` | 0 |
| `patch-inline-nullable-unrequired-props-omit` | `search-incomplete` | `pathItem.patch` | 2 APIs.guru, 1 registered |
| `query-param-ref-to-enum-or-array-union-converted` | `search-incomplete` | `schema.items` | 0 |
| `required-param-and-body-defaults-ignored` | `search-incomplete` | `schema.default` | 0 |
| `stream-error-status-raises-typed-error` | `search-incomplete` | `response.content` | 5 registered |
| `string-body-example-backslash-escaped` | `search-incomplete` | `mediaType.example` | 0 |
| `undiscriminated-ref-oneof-sibling-properties-dropped` | `search-incomplete` | `schema.properties:non-empty` | 1 APIs.guru |
| `union-of-enum-ref-const-and-string-members` | `search-incomplete` | `schema.const:string-valued` | 0 |
| `union-of-two-enum-refs-alias` | `search-incomplete` | `schema.$ref:resolves-to-component` | 0 |
| `variant-nullable-value-optional-default-none` | `search-incomplete` | `schema.nullable` | 3 registered |
| `variant-own-fields-before-allof-parent-fields` | `search-incomplete` | `schema.allOf:sole-member` | 1 APIs.guru |

## Renewed search

What became of every strict declarer of a key above, and why none is a witness.

| key | outcome | why |
|---|---|---|
| `bigint-format-string-typed-str` | `none-registrable` | no document declares it; the corpus's one `bigint`, in `exhaustive`, is `type: integer` |
| `described-ref-oneof-alias-without-docstring` | `none-registrable` | `bkk.hu/1.0.1` (`TransitReferences`) is refused by Fern (26 errors, first a query/header name collision); `whatsapp.local/1.0` (`Audio`, `Document`, `Image`, `Video`) generates, but crozier differs in six files apart from the shape (`reference.md`, `application/client.py`, `media/raw_client.py`, `messages/client.py`, `profile/client.py`, `types/webhook_system_type.py`); `just-eat.co.uk` (5 members), `probely.com` (4) and the registered `tamoss` (5), `hasura-metadata` (3), `mockserver` (3) and `paypal-catalog-products` (7) declare more than two members; `langchain-agent-protocol`'s union is a discriminated one Fern infers; `twitter.com` grants no redistribution (its Developer Agreement) |
| `discriminated-variant-date-value-snippet` | `none-registrable` | no document declares it; four APIs.guru and two registered documents declare only one of the two formats, or not on a request body |
| `empty-path-segment-double-slash-kept` | `none-registrable` | both declarers are refused by Fern: `clever-cloud.com/1.0.0` (40 errors, first a non-object response example) and `tomtom.com/maps/1.0.0` (8, auth required but undefined) |
| `enum-union-body-example-first-member-value` | `none-registrable` | no document declares it |
| `group-path-ending-in-api-nested-package` | `none-registrable` | no document declares it |
| `literal-enum-value-quote-escaping` | `none-registrable` | no document declares it; 27 APIs.guru and 4 registered documents quote or escape some values but carry no value with both quotes, a backslash and a non-ASCII character together |
| `literal-prefixed-integer-path-segment` | `none-registrable` | its one declarer, `mist.com/0.37.7`, is refused by Fern (`CORPUS.md` drops `mist.com` on its duplicate `device_mac` request property); 25 documents type the parameter as a string |
| `multipart-inline-object-part-json-encoded` | `none-registrable` | every declarer is refused by Fern: `box.com` and `mist.com` (each dropped in `CORPUS.md`) and `gerermesaffaires.com/1.0.6` (a `personId` request-property collision) |
| `multipart-part-encoding-charset-tuple` | `none-registrable` | no document declares it; three APIs.guru documents and one registered one name a part content type without a `charset` |
| `oneof-duplicate-members-collapsed` | `none-registrable` | no document declares it; the six that repeat a member repeat a `$ref` |
| `patch-inline-nullable-unrequired-props-omit` | `none-registrable` | `loket.nl/V2` crashes Fern's generator container (its formatter cannot parse the code it wrote) and `vercel.com/0.0.1` is refused by Fern (duplicate request property names); the registered `discord-com` declares every property nullable as an OpenAPI 3.1 `type: [..., "null"]` array, not the `nullable: true` spelling the shape is about |
| `query-param-ref-to-enum-or-array-union-converted` | `none-registrable` | no document declares it |
| `required-param-and-body-defaults-ignored` | `none-registrable` | no document declares both halves; 32 APIs.guru and 6 registered documents declare one |
| `stream-error-status-raises-typed-error` | `none-registrable` | the five registered declarers (`dot-ai`, `standrig`, `truefoundry-trueforge`, `truefoundry-trueforge-5adde28`, `zoonk`) type their `400` body as an object, never the bare `type: string` whose `parse_obj_as(type_=str, …)` is the shape |
| `string-body-example-backslash-escaped` | `none-registrable` | no document declares it |
| `undiscriminated-ref-oneof-sibling-properties-dropped` | `none-registrable` | its one declarer, `rebilly.com/2.1`, is licensed under Rebilly's own API License Agreement, a proprietary grant the corpus cannot redistribute |
| `union-of-enum-ref-const-and-string-members` | `none-registrable` | no document declares it; two registered documents pair an enum `$ref` with one of the other two members only |
| `union-of-two-enum-refs-alias` | `none-registrable` | no document declares it |
| `variant-nullable-value-optional-default-none` | `none-registrable` | the registered `tlon-notes`, `truefoundry-trueforge` and `truefoundry-trueforge-5adde28` spell the nullable value as an OpenAPI 3.1 `type` array, not `nullable: true` |
| `variant-own-fields-before-allof-parent-fields` | `none-registrable` | its one declarer, `apple.com/sirikit-cloud-media/1.0.2`, is refused by Fern (a missing `method` discriminant) |

## The real witnesses

Seven shapes have a real specification declaring the whole trigger, and need
no hand-written fixture.

| key | witness | golden | comparison test |
|---|---|---|---|
| `dotted-mapping-key-variant-class-name` | corpus row 108, `truefoundry-trueforge`: `ActionRequiredEvent`'s mapping keys `mcp.auth_required`, `tool.approval_required` and `tool.response_required` name `ActionRequiredEvent_McpAuthRequired` and its siblings, not the target schemas | `tests/fixtures/truefoundry-trueforge/expected` | `truefoundry_trueforge_matches_fern_output` |
| `literal-enum-description-omitted` | corpus row 150, `groupe-psa`: six described component string enums, among them `ChargingStatusEnum`, a bare `Literal` alias under literals and a documented `enum.StrEnum` under `python_enums` | `tests/fixtures/groupe-psa/expected-literals`, `tests/fixtures/groupe-psa/expected` | `overlay_goldens_match_fern_output`, `groupe_psa_matches_fern_output` |
| `multipart-single-value-enum-part-kept-optional` | corpus row 2400, `mermade-openapi-converter`: `convertUrl`'s optional one-value `validate` part | `tests/fixtures/mermade-openapi-converter/expected` | `mermade_openapi_converter_matches_fern_output` |
| `open-object-body-example-extra-keys-dropped` | corpus row 232, `mockserver`: `mockOidcProvider`'s example passes `subject` and `audience`, which its open body does not declare, and both worked calls leave them out | `tests/fixtures/mockserver/expected` | `mockserver_matches_fern_output` |
| `required-and-nullable-property-defaults-none` | corpus row 10, `apideck.com-crm` (OpenAPI 3.0.3): `Lead.company_name`, required and `nullable: true`, is `typing.Optional[str] = None` | `tests/fixtures/apideck.com-crm/expected` | `apideck_crm_matches_fern_output` |
| `snake-case-component-name-pascal-class` | corpus row 117, `paloalto-remote-networks`: `generic_error` is `class GenericError` in `types/generic_error.py` | `tests/fixtures/paloalto-remote-networks/expected` | `paloalto_remote_networks_matches_fern_output` |
| `variant-optional-const-discriminant-merged` | corpus row 75, `letta`: `SystemMessage` declares `message_type` as an optional `const`, and `LettaStreamingResponse_SystemMessage` carries only the variant's literal, first | `tests/fixtures/letta/expected` | `letta_matches_fern_output` |

`prove_matches_real_witnesses_declare_their_shapes` in
[`../../../crates/crozier-e2e/tests/e2e/real_witnesses.rs`](../../../crates/crozier-e2e/tests/e2e/real_witnesses.rs)
holds each row to its source and golden, so a regenerated golden or a moved
schema that stops declaring the shape fails rather than leaving the claim
standing.

## Literals-mode only

Two shapes are proven under literals alone, the mode Fern was measured in; the
gated hand-written directory compares `python_enums`, where crozier still
differs:

- `enum-header-params-stringified`: under `python_enums` Fern sends an enum
  header as `shift.value` and crozier as `str(shift)`
  (`src/fern/trams/raw_client.py` lines 51-52 and 132-133 of the document in
  [`literals-mode/enum-header-params-stringified`](../../fern-measurements/literals-mode/enum-header-params-stringified/openapi.yml),
  measured with `tools/fern-goldens/generate-fern-fixture.sh` at Fern CLI
  5.67.1 and `fernapi/fern-python-sdk` 5.20.0 and compared with crozier's
  default output). No search above reaches a witness for it.
- `enum-extension-names-dropped-under-literals`: under `python_enums` Fern
  writes each `x-fern-enum` description as a member docstring
  (`src/fern/types/relation.py`, after `BELOW` and `DIFFERS`) and crozier
  writes none, the `enum-value-description-extension-dropped` departure. No
  search above reaches a witness for it.

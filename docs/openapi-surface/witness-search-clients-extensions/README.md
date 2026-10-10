# Client and package construction witness search

The real-specification searches behind the client, package and naming shapes
whose proof is a hand-written fixture. [`keys.tsv`](keys.tsv) is the contract:
one row per searched key and the census selector that decides it.

## The pinned APIs.guru walk

The repository half of APIs.guru, `APIs-guru/openapi-directory` at commit
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, the tree the
[APIs.guru acquisition](../witness-search-apis.guru/README.md) fetched and
listed. Every one of the 4,138 JSON/YAML documents its
[`acquisition-manifest.tsv`](../witness-search-apis.guru/acquisition-manifest.tsv)
names was re-hashed before this walk and matched its recorded SHA-256, so the
walk read exactly those bytes. It ran:

```sh
just witness-search-local-census --contract docs/openapi-surface/witness-search-clients-extensions/keys.tsv \
  --workers 12 --all-documents --documents apis-guru=<extracted tree>
```

[`apis-guru-census.tsv.gz`](apis-guru-census.tsv.gz) keeps one row per document:
its path, SHA-256, OpenAPI version and each key's selector count. 1,970 documents
are OpenAPI 3 and were censused; 2,168 are Swagger 2.0, which crozier does not
read, and carry no count. None failed to parse.

A walk of one source is not an exhausted search: the other declared sources
were not asked, so each key's verdict is `search-incomplete`, and the result
table below records that the walk found nothing registrable.

## Schema named Complex

The shape: a component schema whose class's module stem is `complex`
(`components.schemas:complex-module-name`). Fern reserves the builtin and
writes `types/complex_.py`.

| key | verdict | remaining work |
|---|---|---|
| `schema-name-builtin-complex` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Untagged list or set operation

The shape: an untagged operation whose `operationId` is exactly `list` or `set`
and that names no method by extension
(`operation.operationId:untagged-list-or-set`). Fern leaves both builtins
unsuffixed as method names.

| key | verdict | remaining work |
|---|---|---|
| `operation-id-untagged-list-or-set` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Hyphenated tag method

The shape: a tagged operation whose `operationId` is `<prefix>-<method>`, one hyphen and no `_` or `.`, the prefix spelling its first tag and the method camel-cased (`operation.operationId:hyphenated-tag-method`). Fern lowercases the method segment (`checkstatus`).

| key | verdict | remaining work |
|---|---|---|
| `operation-id-hyphenated-tag-method` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## All-caps tag spelled by a split prefix

The shape: a tagged operation whose all-capitals first tag (`QX`) is spelled letter for letter, but not word for word as Fern splits the tag, by the several `_` segments of its operationId prefix (`q_x_schedule`) (`operation.operationId:all-caps-tag-split-prefix`). Fern names the module from the tag (`qx/`, `QxClient`) and keeps the whole id as the method.

| key | verdict | remaining work |
|---|---|---|
| `operation-id-all-caps-tag-split-prefix` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

The same walk counted the broader form, any tag a prefix spells letter for
letter but not word for word (`operation.operationId:tag-spelled-split-prefix`,
key `operation-id-tag-spelled-split-prefix`). Three documents declare it, and
each is a partial candidate: none has an all-capitals tag, the missing portion
of this trigger.

| partial candidate | sites | example | missing portion |
|---|---:|---|---|
| `APIs/digitalocean.com/2.0/openapi.yaml` | 24 | `sshKeys_list` under `SSH Keys` | an all-capitals tag |
| `APIs/docker.com/hub/beta/openapi.yaml` | 2 | `AuditLogs_GetAuditLogs` under `audit-logs` | an all-capitals tag |
| `APIs/windows.net/graphrbac/1.6/openapi.yaml` | 2 | `DeletedApplications_List` under `deletedApplications` | an all-capitals tag |

## Group name with a leading underscore

The shape: an operation declaring an SDK method name whose SDK group name has a segment starting with `_` (`operation.x-fern-sdk-group-name:leading-underscore`, either spelling). Fern keeps the underscore in the module path and accessor (`_relays/`, `client._audit._trail`).

| key | verdict | remaining work |
|---|---|---|
| `operation-sdk-group-name-leading-underscore` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Group name without a method name

The shape: an operation declaring a non-blank SDK group name and no SDK method name (`operation.x-fern-sdk-group-name:without-method-name`, either spelling). Fern ignores the group and places the operation by its tag and `operationId`.

| key | verdict | remaining work |
|---|---|---|
| `operation-sdk-group-name-without-method-name` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Method name written as a sequence

The shape: an operation whose SDK method name is written as a sequence of strings (`operation.x-fern-sdk-method-name:sequence`, either spelling). Fern generates from it, joining the members with `,` (`[vacancies]` is `vacancies`, `[claim, now]` is `claim_now`).

| key | verdict | remaining work |
|---|---|---|
| `operation-sdk-method-name-sequence` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Header credential extension

The shape: a header `apiKey` scheme whose `x-fern-header` (or `x-crozier-header`) names the credential (`securityScheme.x-fern-header:named`). Fern names the constructor parameter from it and sends the key behind its `prefix` (`meter_token`, `f"Meter {self.meter_token}"`).

| key | verdict | remaining work |
|---|---|---|
| `security-scheme-header-extension-named` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Bearer credential extension

The shape: an http `bearer` scheme whose `x-fern-bearer` (or `x-crozier-bearer`) names the credential (`securityScheme.x-fern-bearer:named`). Fern names the constructor parameter, private field and getter from it (`lift_pass`, `_get_lift_pass`); with an `env` it defaults to that variable and raises `ApiError` when neither is given.

| key | verdict | remaining work |
|---|---|---|
| `security-scheme-bearer-extension-named` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Basic credential extension

The shape: an http `basic` scheme whose `x-fern-basic` (or `x-crozier-basic`) gives its username or password a `name` or `env` (`securityScheme.x-fern-basic:named-or-env`). Fern names each parameter and defaults each to its variable, raising `ApiError` when one is missing.

| key | verdict | remaining work |
|---|---|---|
| `security-scheme-basic-extension-named` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Token variable name extension

The shape: the http `bearer` scheme Fern names the credential from, declaring `x-fern-token-variable-name` (or `x-crozier-token-variable-name`) (`securityScheme.x-fern-token-variable-name:bearer`). Fern names the bearer parameter from it; beside a header key promoted under the same name the two share one parameter.

| key | verdict | remaining work |
|---|---|---|
| `security-scheme-token-variable-name` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Duplicate api-key header schemes

The shape: two header `apiKey` schemes naming one header whose name stems to `api_key`, both offered by the document's `security` (`components.securitySchemes:duplicate-api-key-header`). Fern declares one `api_key` parameter and writes the header twice.

| key | verdict | remaining work |
|---|---|---|
| `security-schemes-duplicate-api-key-header` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

Two walked documents declare two header `apiKey` schemes naming one header, and
each is a partial candidate: `APIs/britbox.co.uk/3.730.300-ref-1-39-0/openapi.yaml`
(`resetPasswordAuth` and `verifyEmailAuth`, both `authorization`; no
`info.license`, so it also fails the licence screen) and
`APIs/kumpeapps.com/5.0.0/openapi.yaml` (`app_key` and `auth_key`, both
`X-Auth`). Neither names a header that stems to `api_key`, and neither offers
both schemes in the document's `security`, the missing portions of this
trigger. The registered `openepcis-dpp-ready` reaches the shared-parameter
emission from another direction, two headers (`X-API-KEY`, `API-KEY`) that stem
to one name; it is no declarer of this key.

## Capitalised http scheme

The shape: an http security scheme whose `scheme` is `bearer` or `basic` spelled with a capital (`securityScheme.scheme:capitalised-http`). HTTP scheme names are case-insensitive, and Fern generates it as the lowercase scheme.

| key | verdict | remaining work |
|---|---|---|
| `security-scheme-capitalised-http` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Server default URL extension

The shape: a document server with a templated `url` declaring `x-fern-default-url` (or `x-crozier-default-url`) (`server.x-fern-default-url:templated`). Fern makes the default URL the environment member's value in place of the expanded template.

| key | verdict | remaining work |
|---|---|---|
| `server-default-url-templated` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Named document servers

The shape: two or more document servers naming themselves by `x-fern-server-name` (or `x-crozier-server-name`) with no `description` (`server.x-fern-server-name:several-undescribed`). Fern makes each an environment member under its name, the first the default.

| key | verdict | remaining work |
|---|---|---|
| `server-name-several` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Idempotent operation

The shape: an operation marked `x-fern-idempotent: true` (or `x-crozier-idempotent`) in a document declaring `x-fern-idempotency-headers` (`operation.x-fern-idempotent:with-root-headers`). Fern gives the method an optional argument per header after its body fields (`X-Dedupe-Token` is `dedupe_token`) and sends it.

| key | verdict | remaining work |
|---|---|---|
| `operation-idempotent-with-root-headers` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Retries disabled

The shape: an operation whose `x-fern-retries` (or `x-crozier-retries`) is a mapping with `disabled: true` (`operation.x-fern-retries:disabled`). Fern sends its request with the caller's options and `max_retries` set to 0.

| key | verdict | remaining work |
|---|---|---|
| `operation-retries-disabled` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Type name on an inline schema

The shape: an inline property schema, not a `components.schemas` entry, declaring `x-fern-type-name` (or `x-crozier-type-name`) (`schema.x-fern-type-name:inline-property`). Fern names the type it hoists by the declaration, as it would a component.

| key | verdict | remaining work |
|---|---|---|
| `schema-type-name-inline-property` | `search-incomplete` | The APIs.guru walk finds 0 declarers among 1,970 OpenAPI 3 documents under the broadened selector (below). The registered corpus declares it in 1 of 244 sources: `webflow-v2` writes it on six inline response-body `payload` objects, each beside an identical `title`. That is a partial witness: a type named by its title gets that same name, so it never shows the extension renaming anything. The missing portion is an inline property whose type name differs from any `title` (`film-shot-planner`'s untitled enum). The other declared sources were not asked. |

The selector first counted only properties nested under a component schema,
which misses this shape's own trigger, an inline response-body property; the
archived [`apis-guru-census.tsv.gz`](apis-guru-census.tsv.gz) holds that
narrower count. It now reads every inline property — a component's, a body's, a
parameter's or a webhook's. The key alone was re-walked with it over the same
tree, every one of the 4,138 documents' SHA-256 first matched against the
acquisition manifest:

```sh
just witness-search-local-census --contract <one-row contract: schema-type-name-inline-property> \
  --workers 12 --all-documents --documents apis-guru=<extracted tree>
```

It found 0 declarers, as before.

## Webhook-marked path operation

The shape: a path operation marked `x-fern-webhook: true` (or `x-crozier-webhook`) (`operation.x-fern-webhook:true`). Fern gives the client no method for it, and the schemas it names stay ordinary types.

| key | verdict | remaining work |
|---|---|---|
| `operation-webhook-extension` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Offset pagination

The shape: an operation whose pagination extension (either spelling) is the offset form, `offset` with no `cursor` (`operation.x-fern-pagination:offset`). Fern returns an offset pager in its packaged tree and, in its flat tree, the page model with the pagination runtime still shipped.

| key | verdict | remaining work |
|---|---|---|
| `operation-pagination-offset` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Boolean pagination over a root contract

The shape: an operation whose pagination extension is `true` in a document whose root declares a pagination contract (`operation.x-fern-pagination:boolean-over-root`). Fern takes the root contract for the operation.

| key | verdict | remaining work |
|---|---|---|
| `operation-pagination-boolean` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Cursor pagination

The shape: an operation whose pagination extension is the cursor form, `cursor`
with `next_cursor` (`operation.x-fern-pagination:cursor`). Registered real
specifications declare it: `truefoundry-trueforge` and
`truefoundry-trueforge-5adde28` (7 sites each), whose packaged goldens
byte-match. The scenario's divergence is Fern's flat tree, where each cursor-
paginated method returns its page model: `truefoundry-trueforge` also carries
that flat golden (`tests/fixtures/truefoundry-trueforge/expected-flat/`, a
[`flat-goldens.txt`](../../../tests/fixtures/flat-goldens.txt) row), which
crozier's `--layout flat` output matches apart from the catalogued
`flat-pagination-pager-docs` departure. The crozier-authored `crane-hire-cursor`
case in
[`../../fern-measurements/clients-extensions/`](../../fern-measurements/clients-extensions/README.md)
pins the same contract on a smaller document, with the next cursor at the top
of the page model.

| key | outcome | registered declarers |
|---|---|---|
| `operation-pagination-cursor` | `golden` | `truefoundry-trueforge`, `truefoundry-trueforge-5adde28` |

## Pagination over a nullable response

The shape: an operation with a pagination contract whose `200` JSON response
references a component declared `nullable: true`
(`operation.x-fern-pagination:nullable-response`). Fern refuses it, and so does
crozier, in both modes: it is the
[`paginated-nullable-response`](../../fern-refusals/paginated-nullable-response/evaluation.md)
refusal class, whose probe and Fern record live in the refusal registry.

| key | outcome |
|---|---|
| `operation-pagination-nullable-response` | `refuse` (no declarer in the walk or the registered corpus) |

## Group with types beside a child group

The shape: an operation declaring an SDK group and method name whose group is a proper prefix of another operation's declared group and whose inline request body has an inline `enum` property (`operation.x-fern-sdk-group-name:types-beside-child-group`). Fern's group package exports its hoisted types and its child group together.

| key | verdict | remaining work |
|---|---|---|
| `operation-group-types-beside-child-group` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Component SDK group

The shape: a component schema declaring an SDK group name (`x-fern-sdk-group-name` or `x-crozier-sdk-group-name`) (`schema.x-fern-sdk-group-name:component`). Fern writes its type into that group's package (`glossary/types/phrase.py`), re-exported from the root through it.

| key | verdict | remaining work |
|---|---|---|
| `schema-sdk-group-name` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Component x-tags

The shape: a component schema declaring a non-empty `x-tags` list (`schema.x-tags:component`). Fern writes its type into its first tag's package (`fermentation/types/batch.py`).

| key | verdict | remaining work |
|---|---|---|
| `schema-x-tags` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Named webhook payload

The shape: a `webhooks` operation whose `application/json` request body is an inline schema and that declares an SDK group or method name (`openapi.webhooks:inline-json-body-named`). With both, Fern names the payload `{Method}{Group}Payload` in the group's package (`parcels/types/delivered_parcels_payload.py`).

| key | verdict | remaining work |
|---|---|---|
| `webhook-inline-json-body-named` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

## Named operation server

The shape: an operation whose `servers` are one URL named by `x-fern-server-name` (either spelling) other than the document's single server's (`operation.servers:named-beside-document-server`). Fern makes the environment an object with a `base` field and one per named operation server, takes it in place of `base_url`, and sends each request to its field's URL.

| key | verdict | remaining work |
|---|---|---|
| `operation-servers-named` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

The registered `webflow-v2` declares operation-level servers too, and its
golden's multi-URL environment (`environment.py`, the root client, the client
wrapper and every raw client reading `get_environment().base`) now
byte-matches. It is a partial witness: each of its operations lists two named
servers, the first the document's own URL, so every request reads `base`; an
operation reaching its own named URL, the missing portion, is the fixture's.

## Empty-string tag

The shape: an operation tagged only with the empty string and no SDK group name (`operation.tags:empty-string`). Fern groups it under an empty namespace it calls `_`, documents `client._.list_lamps()` and links `src/fern/_/client.py`, but writes that package's files over the package root, so the tree cannot be imported; crozier writes the `_` package under `_/` beside a root client exposing it (the `empty-namespace-package` departure).

| key | verdict | remaining work |
|---|---|---|
| `operation-empty-tag` | `search-incomplete` | The APIs.guru walk found 0 declarers among 1,970 OpenAPI 3 documents; the registered corpus declares it in 0 of 243 sources. The other declared sources were not asked. |

The registered `bungie.net` tags four operations with the empty string, but
their `operationId`s begin with `.`, which names the `_` group on its own, so
the selector leaves them out. Its golden shows the same package written over
the root, and the same departure holds it: `bungie_matches_fern_output`
compares every other file byte for byte.

## Results

| key | result | fixture |
|---|---|---|
| `schema-name-builtin-complex` | `none-registrable` | `impedance-complex-reading` |
| `operation-id-untagged-list-or-set` | `none-registrable` | `depot-bin-ledger` |
| `operation-id-hyphenated-tag-method` | `none-registrable` | `ferry-berth-desk` |
| `operation-id-all-caps-tag-split-prefix` | `none-registrable` | `rfid-door-panel` |
| `operation-sdk-group-name-leading-underscore` | `none-registrable` | `signal-box-relays` |
| `operation-sdk-group-name-without-method-name` | `none-registrable` | `cargo-hold-pallets` |
| `operation-sdk-method-name-sequence` | `none-registrable` | `locker-bank-claims` |
| `security-scheme-header-extension-named` | `none-registrable` | `meter-reader-gateway` |
| `security-scheme-bearer-extension-named` | `none-registrable` | `ski-lift-gates` |
| `security-scheme-basic-extension-named` | `none-registrable` | `lock-keeper-vault` |
| `security-scheme-token-variable-name` | `none-registrable` | `grid-valve-console` |
| `security-schemes-duplicate-api-key-header` | `none-registrable` | `twin-key-relay` |
| `security-scheme-capitalised-http` | `none-registrable` | `tide-gauge-sessions` |
| `server-default-url-templated` | `none-registrable` | `harbour-pilot-regions` |
| `server-name-several` | `none-registrable` | `orbit-ground-stations` |
| `operation-idempotent-with-root-headers` | `none-registrable` | `parcel-courier-desk` |
| `operation-retries-disabled` | `none-registrable` | `parcel-courier-desk` |
| `schema-type-name-inline-property` | `none-registrable` | `film-shot-planner` |
| `operation-webhook-extension` | `none-registrable` | `auction-house-bids` |
| `operation-pagination-offset` | `none-registrable` | `ledger-records-offset` |
| `operation-pagination-boolean` | `none-registrable` | `beacon-registry-pages` |
| `operation-group-types-beside-child-group` | `none-registrable` | `dock-yard-bookings` |
| `schema-sdk-group-name` | `none-registrable` | `vineyard-cellar-glossary` |
| `schema-x-tags` | `none-registrable` | `vineyard-cellar-glossary` |
| `webhook-inline-json-body-named` | `none-registrable` | `courier-delivery-hooks` |
| `operation-servers-named` | `none-registrable` | `locker-archive-hosts` |
| `operation-empty-tag` | `none-registrable` | `lamp-room-log` |

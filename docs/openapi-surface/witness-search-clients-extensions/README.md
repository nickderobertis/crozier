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

## Results

| key | result | fixture |
|---|---|---|
| `schema-name-builtin-complex` | `none-registrable` | `impedance-complex-reading` |
| `operation-id-untagged-list-or-set` | `none-registrable` | `depot-bin-ledger` |
| `operation-id-hyphenated-tag-method` | `none-registrable` | `ferry-berth-desk` |
| `operation-id-all-caps-tag-split-prefix` | `none-registrable` | `rfid-door-panel` |
| `operation-sdk-group-name-leading-underscore` | `none-registrable` | `signal-box-relays` |
| `operation-sdk-group-name-without-method-name` | `none-registrable` | `cargo-hold-pallets` |

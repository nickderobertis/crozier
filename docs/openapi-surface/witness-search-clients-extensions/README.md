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

## Results

| key | result | fixture |
|---|---|---|
| `schema-name-builtin-complex` | `none-registrable` | `impedance-complex-reading` |
| `operation-id-untagged-list-or-set` | `none-registrable` | `depot-bin-ledger` |
| `operation-id-hyphenated-tag-method` | `none-registrable` | `ferry-berth-desk` |

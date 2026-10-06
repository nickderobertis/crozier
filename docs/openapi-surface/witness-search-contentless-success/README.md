# Contentless 200 beside a typed 201

## Witness search

The registered-source walk read all 238 golden sources at `29eda6cfc`,
resolving local Response Object references. No operation declares a contentless
200 beside a 201 with content. A bounded extra GitHub code search used
`scripts/witness-search-github.py`'s guarded `Acquirer`: two phrasings in both
serializations, first broad and then restricted to documents smaller than
4,096 bytes. The tool partitioned those searches because each exceeded its
1,000-result window. The bounded pass then used its guarded `github_json`
interface to read page 1 with `per_page=20` for each restricted phrasing.
[`queries.tsv`](queries.tsv) records all six answers; no later page, size
partition, publisher tree or other registry was searched.

The 40 distinct documents returned were fetched at the indexed immutable commit
through `Acquirer.github_document(..., route="raw")`, parsed by the shared
census loader, and walked as operation response maps. Each document's pinned
identity, SHA-256, declaration count and parser or acquisition verdict is in
[`census.tsv`](census.tsv). One document declares the shape: a converter demonstration, excluded because
it is an example rather than an API publisher’s specification. One uninstantiated
Go template cannot be parsed as OpenAPI. [`screens.tsv`](screens.tsv) records
both exclusions; neither proceeds to the licence or Fern-acceptance screen. These are search candidates, never
registered real-specification matches.

| key | verdict | why |
|---|---|---|
| `response-contentless-200-with-created` | `search-incomplete` | the registered corpus and 40 pinned documents were read, but the bounded pages do not exhaust any declared search source |

## Renewed search

| key | outcome | selector | declarations | hand-written fixture |
|---|---|---|---|---|
| `response-contentless-200-with-created` | `none-registrable` | `operation.responses:contentless-two-hundred-with-created` | 0 in 238 registered sources; 1 in 40 additional candidates, excluded on provenance | `contentless-created-success` |

The fixture is weaker evidence than a real specification. Its one operation
has only the requested response combination; it is not a corpus registration.

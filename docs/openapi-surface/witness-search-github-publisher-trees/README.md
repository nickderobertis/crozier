# Relative-file Path Item search: publisher trees

`raybot-tree.json` is the raw GitHub REST git-tree response at commit
`4428dea2f79b833aead4c89df5bd8d9e32b7b0c8`; it reports
`truncated: false`. `pinned-members.tsv` records each OpenAPI member registered
from that tree and from FOLIO's publisher tree, with its path, immutable URL and
SHA-256. The corpus pin lint and fetch path enforce the authoritative manifest;
the offline pin test reconciles this search inventory with it.

`raybot-census.json` measures 23 `pathItem.$ref:relative-file` sites and 69
`schema.$ref:cross-document` sites in Raybot's pinned tree;
`folio-census.json` measures six cross-document schema sites in FOLIO's pinned
tree. `screens.tsv` records each registered candidate's licence, revision and
Fern acceptance. The resulting Fern 5.20.0 goldens are in the corpus itself.

`quota-calls.jsonl` records guarded GitHub REST admissions. `quota-waits.jsonl`
records the one live `core` probe that found insufficient headroom on an
unauthenticated acquisition. That acquisition was interrupted before a call was
admitted and repeated with the authenticated token; there was no completed wait.
The pinned static-file fetches have no GitHub REST bucket. They are spaced and
retry a `429` or `Retry-After` response in the shared pin fetcher.

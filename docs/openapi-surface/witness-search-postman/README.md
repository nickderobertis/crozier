# Postman public-network search (historical, excluded)

**Postman is not a declared witness-search source.** The user excluded it:
reading a body there needs a Postman API key, which this host does not hold and
will not get. See
[the exclusion](../../openapi-surface-coverage.md#the-settlement-rule-as-amended).
Nothing in this directory is counted by any gate, cited as a search of any
key, or listed as outstanding for one. It is kept only as a record of the
requests that were issued before the exclusion.

`queries.jsonl` records the requests issued to the `search-all` proxy over the
`apinetwork.team`, `runtime.collection` and `adp.api` indices. Each record keeps
the request body, response status, response hash, returned `meta.total` and
timestamp. `query-index.tsv` indexes the two query strings per key. The
`apinetwork.team` index and one `runtime.collection` query refused offset 225
with HTTP 400 (`From value: 225 must be non-negative integer and less than
200.`).

The proxy returns team, collection and API **metadata**, never an OpenAPI
body. `api-access.jsonl` is a first keyless request to the Postman API for each
of the 23 API hits, and every one returned HTTP 401.
`scripts/witness-search-postman.py --acquire-hits` then began reading every
hit through its unauthenticated route, recorded in `hit-access.jsonl`:
a collection's JSON link, a team's profile page, or the Postman API for an API.
It was stopped after 562 of 2,285 hits when Postman left the plan. Of those
562, 185 collection links returned a Postman collection body, which the parse
classifies as not an OpenAPI 3 document. 353 answered HTTP 404 `Link does not
exist.`, the 23 APIs answered HTTP 401, and the last request met an HTTP 429.
The run was stopped inside the backoff that 429 opened, so that wait has no
record in `rate-limit-waits.jsonl`. `records.tsv` and `candidates.tsv` carry no
candidate rows.

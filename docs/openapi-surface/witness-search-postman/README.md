# Postman public-network search

`queries.jsonl` records the requests issued to the `search-all` proxy for the
three indices named in the search plan. Each request body, response status,
response hash, returned `meta.total`, and timestamp is retained. The two query
strings per key are indexed in `query-index.tsv`. `records.tsv` has no candidate
rows because no OpenAPI bytes could be acquired from the metadata hits.
The recorded count for an answered query is the sum of `team`, `collection`,
and `api`/`apiDefinition`/`specification` totals from their respective indices.
The `apinetwork.team` index rejected later offsets with HTTP 400;
those queries carry that response and its timestamp instead of an absence claim.

The proxy yielded team, collection, and API **metadata**, rather than an
OpenAPI document body. `api-access.jsonl` names each of the 23 distinct public
API identifiers it returned, its keys, and a guarded request to Postman's
documented API resource. All 23 returned HTTP 401, with their response hashes
and timestamps recorded. An earlier guarded probe of the same resource,
`c776b835-b00d-49e8-ad3e-d8dd10485272`, returned HTTP 401 at
2026-09-24T07:13:37.539+00:00; that call is retained in
`rate-limit-calls.jsonl` alongside the 23 individual attempts. No specification
body was acquired from these metadata hits, so none is classified by a keyword
as a shape declarer. The corresponding keys remain `search-incomplete`.

`rate-limit-waits.jsonl` records Postman's paced spacing waits. The lane uses
no quota figure: `rate-limit-calls.jsonl` records request completion and status,
not a percentage of a purported Postman bucket.

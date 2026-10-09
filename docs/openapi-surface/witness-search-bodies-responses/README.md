# Witness search for request bodies and schemaless responses

The real-specification search behind the repairs to how crozier lowers request
bodies and success or error responses: a single-use `Body_*` model, the JSON
content-type header, a status key spelled with a suffix, the empty-body guard in
OpenAPI 3.0, and schemaless text and download successes. A shape this search
found in a registrable document is registered in
[`../../../tests/fixtures/CORPUS.md`](../../../tests/fixtures/CORPUS.md) (rows
319–328); a shape it did not is carried by a hand-written fixture under
[`../handwritten/`](../handwritten/AGENTS.md), whose cover cites this record.

## Bounded search

Ten selectors of `tools/surface-census/openapi-surface-census.py`, two GitHub code-search
phrasings each, issued between 2026-10-05 and 2026-10-06 through
`tools/witness-search/rate_limit_guard.py` and recorded with their counts in
[`queries.tsv`](queries.tsv). The first page of each phrasing (at most 100
results) was downloaded at its indexed commit from `raw.githubusercontent.com`,
1,469 distinct documents in all. Every one was read by the census, one document
at a time; [`census.tsv`](census.tsv) records each document's count for every
selector, or the parser's reason it could not be read (28). Every declarer was
screened on licence (the repository `LICENSE` at the indexed commit, read through
the guard) and immutable reference, and those passing both on pinned Fern (CLI
5.67.1, `fernapi/fern-python-sdk` 5.20.0) until a registrable witness was found;
each outcome is in [`screens.tsv`](screens.tsv). The search answered GitHub code
search alone, at one page per phrasing, so it is not an exhaustive search.

| key | outcome | declarers | registered witness |
|---|---|---|---|
| `operation.requestBody:body-prefixed-single-use` | `witness-found` | 66 | corpus row 319, `millenium-falcon-challenge` |
| `operation.responses:empty-schema-success-oas-three-zero` | `witness-found` | 172 | corpus row 320, `maximo-wxo-integration` (also row 323) |
| `operation.responses:schemaless-text-success` | `witness-found` | 99 | corpus row 321, `mi-music` (also row 324) |
| `operation.responses:schemaless-download-success` | `witness-found` | 60 | corpus row 321, `mi-music` (`audio/mpeg`, `video/mp4`); row 326, `cphos-ai-question` (`application/pdf`) |
| `operation.requestBody:titled-inline-container-oas-three-zero` | `witness-found` | 11 | corpus rows 322, `g4brym-download-manager`, and 323, `opentosca-license-engine` |
| `operation.responses:suffixed-status-key` | `witness-found` | 3 | corpus row 324, `chat-rest-api` (`404-message`, `404-file`) |
| `operation.responses:schemaless-wav-success` | `witness-found` | 9 | corpus row 325, `esp32-streamline-bridge` |
| `operation.requestBody:schemaless-json` | `witness-found` | 26 | corpus row 327, `flask-example-heroku` |
| `operation.requestBody:blank-description-optional-object` | `witness-found` | 31 | corpus row 328, `oip-web-api` |
| `operation.requestBody:described-inline-scalar` | `none-registrable` | 0 | none: no document read declares it |
| `operation.responses:space-suffixed-status-key` | `none-registrable` | 0 | none: no document read declares it |

Each registered witness failed against crozier at the base commit and byte-matches
its golden after the repairs. Other declarers passed every screen without being
registered, because one witness settles the shape; `screens.tsv` names them.

## Renewed search

The two keys no registrable document declares, each the key of a hand-written
fixture's cover, spelled as the `bodies-media` region file spells them, where
their `search-incomplete` lines are its witness-search record:

| key | outcome | selector | documents declaring it | hand-written fixture |
|---|---|---|---|---|
| `request-body-described-inline-scalar` | `none-registrable` | `operation.requestBody:described-inline-scalar` | 0 of the 235 registered sources, 0 of the 1,469 documents above | `described-scalar-bodies` |
| `response-status-space-suffixed` | `none-registrable` | `operation.responses:space-suffixed-status-key` | 0 of the 235 registered sources, 0 of the 1,469 documents above | `suffixed-status-keys` |

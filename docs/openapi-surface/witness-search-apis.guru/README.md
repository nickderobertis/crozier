# APIs.guru indexed-version redo

`unread-responses.jsonl` is the output of:

```sh
python3 scripts/apis-guru-gap-screen.py \
  --redo-unread docs/openapi-surface/witness-scrape-wide/catalogue-entries.tsv.gz \
  --evidence-dir docs/openapi-surface/witness-search-apis.guru
```

The script fetched the served `list.json`, compared every version identity and
indexed URL with the historical manifest, and wrote its SHA-256 to `index.json`.
The digest equals the prior sweep's catalogue digest, so the 3,894 pinned YAML
associations and their hashes in that manifest remain evidence for those exact
bytes. This run acquired the 98 indexed versions with no YAML alternative at
that pin. All 98 requests returned 200; 95 bodies declared OpenAPI 3. Their
selector counts were calculated by `openapi-surface-census.py` over the parsed
body. The other three were excluded as non-OpenAPI-3, with their response hash
and status retained in the JSONL. A zero selector count means the successfully
parsed document did not declare that selector, not that a request failed.

One of the 95, `webflow.com/2023-03-01T164537Z`, declares
`anyof-array-variant-closed-object-item` and `anyof-array-variant-struct-item`
once each. Its fetched body hash is
`550233e93e78ded22dcce92c91b37be05f459bcea03031efaeaa33b1e861d6aa`.
The [prior candidate screen](../witness-search-redo/candidates.md) records
that this APIs.guru identity is a Lucidtech description mislabelled as Webflow,
with no evidenced publisher grant or immutable publisher provenance. This
round's served URL is mutable (`no-immutable-ref`); it supplies no new
publisher evidence. Its licence screen is blocked, its immutable-ref screen
is blocked, and Fern acceptance was not reached. It is a confirmed declarer,
not a registrable witness. A second fetch at 2026-09-24 05:57 UTC returned
HTTP 403, so this run retains the first response's hash and census result.

The repository half was read separately from the `openapi-directory` archive at
commit `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`. Its archive response and
digest are in `acquisitions.jsonl`; `acquisition-manifest.tsv` names all 4,138
JSON/YAML entries and their individual hashes, and `tree-census.jsonl.gz`
records their parsed selector results. `enumeration.tsv` joins those entries
with the 3,992 served-index versions. The manifest and census both use the
same pinned tree bytes; the served-index half reuses only the historical
3,894 YAML associations whose index digest matched, and measures the other 98
from the responses retained here.

# Vendor portal census

`../witness-search-portal-plan.tsv` identifies the 27 publisher portals and how
this list was derived from the registered corpus, the APIs.guru catalogue, and
the earlier publisher traces. The 25 pinned publisher sources were downloaded
at their exact commit URLs. `acquisitions.jsonl` records each response and
SHA-256. `archive-files.tsv` lists the JSON/YAML paths and byte hashes
from the first 23 archive trees; the two later publisher trees are included in
`acquisition-manifest.tsv`, which along with
`enumeration.tsv` are the corresponding per-document identities and selector
results for the Contract B record. `census.jsonl.gz` contains one parsed
selector result per readable document. The exact source bytes can be recovered
from the pinned archive URLs and checked against those manifests.

The census covers 13,906 JSON/YAML files across the 25 pinned publishers and
the mutable PandaScore response. Twelve OpenAPI 3 YAML files use syntax the
standard-library census reader refuses; their rows name the acquisition-side
`PyYAML 6.0.3 CSafeLoader` fallback, which fed the same selector engine. The 39
remaining parse failures retain their exact reason and byte hash in the census
and enumeration. One is a malformed MongoDB OpenAPI test file with a trailing
comma; the others do not carry an OpenAPI 3 root marker. No parser failure is
counted as a zero selector result.

The `elevenlabs/elevenlabs-docs` commit endpoint returned HTTP 404 at the time
in `acquisitions.jsonl`, so its portal remains a recorded non-answer. The live
PandaScore OpenAPI endpoint answered, but offered neither an immutable revision
nor an evidenced redistribution grant; `pandascore-probes.jsonl` records its
response and selector result. Codat's publisher repository was pinned and
censused, but its root has no licence grant; `publisher-grants.tsv` records that
screen. These are declarers, not replacement witnesses.

The pinned Zulip source declares both annotated-reference keys previously
blocked on PandaScore. Its publisher licence and byte hash are recorded in
`publisher-grants.tsv`, and `zulip-fern.json` records Fern 5.67.1 accepting its
raw document and Python generator 5.20.0 retaining an SDK. Its per-key rows in
`candidates.tsv` are replacement witnesses pending corpus registration.

For `anyof-array-variant-struct-item`, the pinned jentic `cradl.ai` candidate
already passed the licence, publisher revision, and Fern screens in the jentic
candidate ledger. Under the manager's early-witness ruling, the other vendor
declarers for that key are `not-owed` after their selector classification; the
Fern runs completed before the ruling are retained in `fern-screens.jsonl`. If
that witness does not register, the remaining declarers become owed again.
`rate-limit-waits.jsonl` is empty because these acquisitions caused no guard
wait; the guarded REST responses are in `rate-limit-calls.jsonl`.

Cloudflare's pinned JSON and YAML descriptions both declare
`property-sole-anyof-struct-member` and pass the rights and revision screens.
`fern-screens.jsonl` records a 900-second Fern check timeout for each. The
manager-required 60-minute retry of the smaller YAML description returned a
Fern check rejection after 2,130 seconds. The JSON description retains an
inconclusive Fern screen and an `outstanding` disposition. Its key remains
`search-incomplete` for this source; the timeout is neither a refusal nor an
absence claim. A later search should retry that exact pinned JSON document.

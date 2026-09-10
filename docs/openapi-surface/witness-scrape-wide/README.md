# Wide document acquisition and witness search

This run establishes **no new registrable candidate** for the frozen baseline.
The acquired readable corpus is exhausted for registrable baseline witnesses at
these pins. The complete publisher-tree census found no baseline declarations. The
catalogue alternatives declare four baseline keys in ten artifacts, all versions
already named in the preserved search. Eight lack an evidenced publisher
redistribution grant; pinned Fern freshly refuses the other two. Accordingly,
[`ranking.tsv`](ranking.tsv) is empty. Discovery has promoted no golden and has
completed no registration slot. These are finite-corpus findings, not a global
`none-found` outcome; the authoritative search-incomplete rows remain unchanged.

## Refreshed baseline

The source checkout was `e88fcc24dbb8d865dbbdab0c65fd9672679bd8a1`.
The project record used `84b8d3f07674aaefccf1d4d9720b6ed23c8141d1`.
Derivation used `RankedBacklogTests.region_rows` over all six authoritative region
files, selecting only eight-cell **gap** rows whose **own** search outcome is
`search-incomplete`. Selectors were reconciled with the frozen redo contract and
validated by the census instrument. Exact keys were joined to historical artifact
rows and screened through `screened_keys`, including its discarded-key subtraction.

All **26 keys**, their selectors, individual named-artifact counts and usable-screen
states match the project record: **14** keys name artifacts, **12** name none, and
**zero** have an all-screens-passing witness for that key. The changed source commit
is the only baseline discrepancy. The older 30-key universe includes four screened
keys outside this baseline; a candidate's successful disposition does not rescue a
key explicitly discarded at retention.

[`keys.md`](keys.md) is the derived two-column census input.
[`baseline.json`](baseline.json) retains every exact joined artifact identity,
four screen cells, disposition and discarded-key state. Classification authority
and selector semantics remain in the region tables and census instrument.
[`historical-sha256.tsv`](historical-sha256.tsv) fingerprints the untouched redo
records; validation checks those bytes without extending their source obligations.

## Acquisition and inventory

The saved complete `list.json` has SHA-256
`dfac835d2d1f13dfdb82723d72be1acf567df53c1b710bf6d68e28b795696e66`,
exactly the preserved sweep's digest. `apis-guru-gap-screen.py::versions`
enumerated **3,992** version entries: **zero new catalogue entries**. This differs
from the **4,138** documents in the pinned repository tree; those numbers describe
different inventories, not a previously omitted version sweep.

The historical source manifests record pins and URLs, but no reusable local cache
paths; this checkout initially had no `.local` cache. We cloned the complete
specification trees, recorded their commits, and verified pinned file bytes.
GitHub API/search/GraphQL calls and Postman were not used.

Every indexed JSON URL was attempted once and returned **HTTP 403: Forbidden**.
None counts as a zero declaration. The clone provides exact indexed YAML
alternatives for **3,894** entries at the previously fully scanned commit
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`; Git checkout verification and SHA-256
bind that reuse. The other **98** indexed versions have no alternative at that pin.
The **244** tree documents outside the index are separately hashed in
[`unindexed-tree.json.gz`](unindexed-tree.json.gz): unchanged prior-tree bytes,
outside this run's indexed-version census, with no new absence claim.

| acquired document scope | input paths | readable OpenAPI 3 | unreadable | excluded |
|---|---:|---:|---:|---:|
| indexed catalogue YAML alternatives | 3,894 | 1,732 | 0 | 2,162 legacy/non-OpenAPI |
| Adyen publisher specification roots | 258 | 255 | 3 | 0 |
| Twilio publisher specification roots | 120 | 119 | 1 | 0 |
| Kubernetes `api/openapi-spec/v3` | 65 | 65 | 0 | 0 |
| MongoDB publisher specification roots | 63 | 57 | 4 | 2 version inventories |
| GitHub publisher specification roots | 384 | 384 | 0 | 0 |

The five publisher trees contain **890** selected paths, including **885** sibling
paths outside the prior five-path selection. Their **880** readable documents
have **784 distinct hashes**. Two earlier readable paths have identical bytes
(Adyen and GitHub); Kubernetes and MongoDB's prior paths changed. Twilio's changed
prior YAML path remains unreadable. The remaining paths are newly measured in
this selected publisher scope; this is not a claim that their bytes never appeared
in any other historical aggregation. All hashes, old/new refs and prior-path
comparisons are in the manifests. Byte aliases are retained rather than counted
as separate potential registrations.

The eight unreadable publisher files expose explicit YAML mapping-key limitations
of the repository reader. Their exact paths, SHA-256 and diagnostics remain in
acquisition evidence. JSON siblings are independent publisher artifacts, not
conversions of the failed YAML. A MongoDB `.yaml` path contains JSON serialization;
its unchanged bytes were named `.json` in the content-addressed census cache so the
existing JSON loader reads them. No source document was rewritten or converted.
Two interrupted preparation attempts preceded the complete runs; they produced no
negative evidence. An overlapping JSON-only census was also stopped; its partial
run supplies no results. `acquisition: verified-reuse` can mean reuse within this run;
`prior_relation` separately records verified previously scanned bytes, changed
prior bytes, or the absence of such proof.

The following committed evidence is fetchable without downloading bulk corpora
into Git:

- [`catalogue-entries.tsv`](catalogue-entries.tsv): every version, its indexed JSON
  refusal, indexed YAML association, tree hash and alternative outcome.
- [`trees.json.gz`](trees.json.gz): all six repository pins, selected roots,
  excluded tooling/test/metadata paths, previous publisher coordinates and licence
  file coordinates/hashes. The Kubernetes clone selected its complete v3 tree.
- [`inventory.json.gz`](inventory.json.gz): 8,776 attempted artifact identities
  (3,992 JSON URLs, 3,894 YAML alternatives, 890 publisher paths).
- [`acquisition.json.gz`](acquisition.json.gz): one outcome per inventory identity,
  exact hashes where bytes exist, document licences when present, repository
  licence evidence, prior-byte relation and diagnostics. It consolidates the two
  complete census invocations and retains their input-manifest digests.
- [`licences/`](licences/): repository grants read at the same commits. The
  aggregation grant is recorded separately from publisher/document evidence.
- [`measurement.json`](measurement.json): summary and exact census instrument hashes.

Bulk clones, the complete index, content-addressed caches and scratch staging
remain under the dispatch's `ONEPIPELINE_NODE_SCRATCH_DIR`, outside Git. No source
failed because of a missing licence file fetch. A licence is not a substitute for
publisher provenance; screening applies [the repository rule](../../corpus-licensing.md).

## Measurements and candidate decisions

Both recorded `just witness-search-local-census` invocations exited **0**:
[`publisher-census.tsv`](publisher-census.tsv) has no declaration rows;
[`catalogue-census.tsv`](catalogue-census.tsv) has **11** rows across **10** distinct
artifacts and **four** keys. Their diagnostic streams are also preserved. The
acquisition stage excludes unreadable and non-OpenAPI inputs before the census;
a clean census exit does not erase those exclusions or the JSON fetch refusals.

The ten exact YAML artifacts have one row each in [`candidates.md`](candidates.md)
and individual evidence under [`evidence/`](evidence/). All correspond to versions
already named by the historical search. PandaScore and seven Codat versions retain
an explicit missing-publisher-grant blocker. Asana and Box carry document grants
and the preserved publisher/version trace. Their YAML bytes were independently
screened at Fern CLI **5.67.1**, with Route A generation configured for **5.20.0**:

| exact YAML artifact | Fern check | Route A generation | diagnostic |
|---|---|---|---|
| Asana, SHA-256 `4ce2c6ea…` | exit 1 | exit 1 | 3 duplicate request declarations: `AddFollowersRequest`, `ProjectSaveAsTemplateRequest`, `RemoveFollowersRequest` |
| Box, SHA-256 `8fdc22dd…` | exit 1 | exit 1 | 23 example-validation errors; missing event-source properties, unexpected properties, and classification examples that are strings rather than objects |

Full logs, configuration and commands are in their individual evidence records.
These are fresh refusals against the recorded YAML hashes. They are **not** the
historical JSON refusals (17 and 25 diagnostics), which remain unchanged; no
JSON/YAML equivalence is asserted. An initial API-only `fern check` configuration
returned exit 0 without establishing generator acceptance. The final checks above
include Route A's default generator group and enum configuration; the actual Route A
script independently refused both generation attempts. No unfinished run is called
a refusal.

Codat's measured YAML declaration counts are twice the preserved JSON counts.
The compared representations differ, and the JSON refusal prevents attributing
that discrepancy to a particular transformation. This is explicitly not a claim
of normalized equivalence or byte parity. The catalogue also contains excluded
legacy inputs and 98 inaccessible versions, so its smaller declarer inventory
does not revise historical unanswered results or prove absent supply.

**No artifact passed all four screens.** Both Asana and Box lack a generated SDK,
so retention and Crozier comparison cannot be measured. Their comparison evidence
says `not-run` and identifies the actual Fern refusal; the empty differing-file
lists mean no files were compared, not parity. The other eight artifacts were
blocked before Fern. There is no retained candidate to rank, and no candidate is
manufactured to fill registration slots.

Generation used the repository's identical Route A script and configuration in
scratch, with `5.20.0` read from `eos.local` golden provenance. No numbered corpus
row, generated output or Rust source changed. The inaccessible indexed versions
and unreadable publisher files remain explicit blockers outside the exhausted
readable corpus; they do not support a global absence claim.

## Ranking and registration contracts

`candidates.md` uses exactly the existing eight-column candidate schema. Only real
four-screen passes contribute via `screened_keys`; discarded keys do not inherit
an artifact's positive verdict. `--supplement-candidates PATH` is repeatable and
adds only that screened-key union to the existing reconciliation. Without it,
historical behavior is unchanged. The current-run test supplies this report.

`ranking.tsv` is UTF-8 TSV with exactly:
`rank, artifact_sha256, artifact, keys, fern_evidence, comparison_evidence`.
Ranks start at 1; hashes are lowercase SHA-256; keys are JSON arrays of retained
baseline strings; evidence fields are relative report paths. Discovery freezes
order by descending retained-key count, then publisher/licence evidence firmness,
then ascending SHA-256. Firmness is 2 for pinned publisher bytes with both repository
and document grant evidence, 1 with one of those, and 0 for an aggregation-only
trace; byte aliases receive the strongest evidenced grade for those bytes.
Identical bytes receive one rank with provenance aliases retained in acquisition.
Comparison evidence must enumerate differing files and diagnostics, including a
failed comparison. A red Crozier comparison would not disqualify a retained
candidate. This run's empty ranking reflects earlier blockers, not repair cost.

Registration selects the highest frozen rank still relevant to an unproven baseline
key, excluding already registered bytes and prior attempted slot dispositions.
Remaining-key coverage filters eligibility; it never reorders the discovery ranking.
[`slots.md`](slots.md) records exactly
`slot | artifact_sha256 | keys | disposition | evidence`. Registration workers append
one result per dispatch, using `registered`, `blocked` or `exhausted`; an exhausted
slot uses `—` and `[]` and links its explanation. These are slot results, not new
surface outcomes. Discovery's empty slots table does not claim a dispatch ran.

## Reproduction and checks

Re-derive into scratch to compare the current authority with this frozen baseline:

```sh
python3 scripts/witness-scrape-wide.py derive --report "$ONEPIPELINE_NODE_SCRATCH_DIR/refreshed-baseline"
python3 scripts/witness-scrape-wide.py validate --report docs/openapi-surface/witness-scrape-wide --inventory docs/openapi-surface/witness-scrape-wide/inventory.json.gz
```

For a fresh, separately recorded acquisition, the fetchable inventory supplies
expected hashes and immutable artifact coordinates. Cached bytes are reused only
when their digest verifies. Failure outcomes remain in the output:

```sh
python3 scripts/witness-scrape-wide.py acquire --inventory docs/openapi-surface/witness-scrape-wide/inventory.json.gz --cache "$ONEPIPELINE_NODE_SCRATCH_DIR/replay-cache" --contract docs/openapi-surface/witness-scrape-wide/keys.md --output "$ONEPIPELINE_NODE_SCRATCH_DIR/replay.json" --workers 8
```

`index-tree` reproduces the all-version join through `versions()` using the saved
index digest, a verified Git checkout and its recorded ref; `--local-paths` allows
acquisition from that checkout. `--prior-ref` identifies the earlier complete-tree
measurement cited above. JSON remains schema version 1 whether stored directly or
with deterministic gzip compression; absent optional document licences are omitted.

The scoped checks are `just test-witness-search-redo`, `just test-surface-census`,
`just lint-corpus-licensing` and `just lint-llm-diff` against the dispatch base
`e88fcc24dbb8d865dbbdab0c65fd9672679bd8a1`. The witness tests drive real CLI, Git,
filesystem and census boundaries, including corrupt caches, changed digests,
unreachable/malformed inputs, partial inventories, selector/key drift, malformed
ranks, missing evidence, conflicting slot claims and non-ASCII diagnostics.

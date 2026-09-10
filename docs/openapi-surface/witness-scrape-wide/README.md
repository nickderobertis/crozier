# Wide document acquisition and witness search

This run establishes **no new registrable candidate** for the frozen baseline.
The acquired readable corpus is exhausted for registrable baseline witnesses at
these pins. The complete publisher-tree census found no baseline declarations. The
catalogue alternatives declare four baseline keys in ten artifacts, all versions
already named in the preserved search. Eight lack an evidenced publisher
redistribution grant; pinned Fern freshly refuses the other two. Accordingly,
[`ranking.tsv`](ranking.tsv) is empty. Discovery promoted no golden; the subsequent registration dispatch
independently recorded slot 1 as exhausted. These are finite-corpus findings, not a global
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

- [`catalogue-entries.tsv.gz`](catalogue-entries.tsv.gz): every version, its indexed JSON
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
surface outcomes. The appended slot 1 row records the independently completed dispatch.

## Finished-tree reconciliation

Reconciliation starts from the acquisition baseline commit
`e88fcc24dbb8d865dbbdab0c65fd9672679bd8a1` and includes discovery
`b915e322c57f56b521bb244f7e7c803351e388d4` and slot 1
`95ceaa1f` (the reconciliation dispatch comparison base). All committed
registration outcomes are in [slots.md](slots.md): **one exhausted slot, zero
registered slots, zero blocked slots**. There are no additional manager-added
slot rows on this tree. [Slot 1's independent audit](slot-1/README.md) verified
all ten exact hashes and repeated both Fern generation refusals; it produced no
expected tree. The empty slot is explained by eight missing publisher grants
and two Fern refusals, not an omitted registration attempt.

**Actual additions: zero corpus rows, zero committed goldens, zero golden
promotions, zero new retained witnesses.** The additions are acquisition,
census, screening and slot evidence. The 885 additional publisher paths broaden
measured inventory; they do not constitute 885 witnesses. The acquired scope and
its inaccessible, unreadable and excluded inputs are enumerated above. This
reconciliation acquires no further corpus and runs no generation or repair.
No external landing or publication is claimed.

| measure | baseline | finished tree | delta |
|---|---:|---:|---:|
| baseline keys retained | 26 | 26 | 0 |
| baseline keys with historical named artifacts | 14 | 14 | 0 |
| baseline keys with an all-screens-passing witness | 0 | 0 | 0 |
| baseline keys classified `gap` / `FIXTURE`, search-incomplete | 26 | 26 | 0 |
| registered source documents / committed-golden sources | 170 / 153 | 170 / 153 | 0 / 0 |
| schema features / golden / limitations / gap | 222 / 169 / 21 / 32 | 222 / 169 / 21 / 32 | 0 / 0 / 0 / 0 |
| all features / golden / limitations / gap | 511 / 392 / 70 / 49 | 511 / 392 / 70 / 49 | 0 / 0 / 0 / 0 |
| fixture backlog / probe backlog / unreachable gaps | 29 / 0 / 20 | 29 / 0 / 20 | 0 / 0 / 0 |

These totals are derived from the six authoritative region tables and agree with
[the surface index and backlog](../../openapi-surface-coverage.md#ranked-gap-backlog).
The three other fixture-backlog keys already have screened witnesses and are
outside this 26-key acquisition: `oneof-bare-object-example-variant`,
`anyof-array-variant-struct-item`, and `ref-pointer-undeclared-component-head`.
The fourth historically screened key, `anyof-sole-member`, was already golden
before this run. Its PayPal registration is not an acquisition delta.

### Settlement and outstanding sources

Apply the operator's precedence per key: an artifact passing redistribution,
immutable publisher provenance, Fern acceptance and retention establishes
`witness-found` even if a source remains unanswered. With no passing artifact,
`none-found` requires every answerable source to have answered zero; unresolved
answerable sources leave `search-incomplete`. A `golden` classification separately
requires registered byte parity. A declaration, a successful check alone, or an
empty comparison file list establishes none of that parity.

**Postman is excluded from this run and from its future obligations.** Its old
queries and results remain historical evidence, byte-for-byte. This report adds
no query to any source and does not replace an old query's result with the new
acquisition. In particular, completing a finite publisher or catalogue inventory
does not make an incapable search endpoint answer a body query.

The following source codes refer to the unchanged per-key records in the
[catalogue/portal report](../witness-search-redo/catalogue-portals.md) and
[code/platform report](../witness-search-redo/code-platforms.md):

- **V:** historical vendor-portals input remained partially unreadable; the new
  publisher census closes only its 880 readable documents, leaving eight unreadable
  paths explicit and supplying no replacement answer for the old query.
- **S:** Sourcegraph's capped/incomplete funnels or unevaluated bodies prevent a
  zero answer. Positive source answers are omitted from the outstanding column.
- **G:** GitHub code-search windows or unevaluated bodies leave the recorded
  funnel unresolved, including the timed-out CloudGuard pointer-anyOf body.
- **H:** SwaggerHub returned metadata rather than immutable definition-body
  matches. This endpoint cannot answer the selector query; no API retry is a
  prerequisite to closing this run's finite inventory.

Every key below has G outstanding; none therefore becomes global `none-found`
even if H cannot answer. All also inherit this acquisition's 98 indexed versions
without a YAML alternative and eight unreadable publisher files. The 3,992 JSON
403 responses are fetch refusals, not zero declarations; 3,894 verified YAML
alternatives are separate artifact evidence.

### Every baseline key

Each row retains its exact selector in [keys.md](keys.md) and its zero registered
source census in [schemas.md](../schemas.md). **Every final row remains
`search-incomplete`, `gap` / `FIXTURE`, with no registration or byte parity.**
Historical artifact identities and individual screens are in [baseline.json](baseline.json).
Below, B counts `witness-blocked`, R `fern-rejected`, I unfinished
`search-incomplete` screens, and D artifacts explicitly discarding this key at
retention. These are artifact-record counts, not distinct publishers or sites;
a pass for another key cannot override D. An absent historical artifact is
written explicitly. Current sites come only from the two complete acquisition
censuses; publisher sites are zero for every key. Each current blocker links to
the exact [candidate evidence](candidates.md), also independently audited by slot 1.

| baseline key | historical artifact screens | acquired catalogue sites / registration blocker | outstanding sources |
|---|---|---|---|
| `annotated-ref-target-closed-object` | 16 B | 7 / PandaScore publisher grant unproven | V, S, G, H |
| `annotated-ref-target-composed` | 35 B, 8 R, 4 I | 36 / Asana 3 errors; Box 23 errors; no SDK or retention | G, H |
| `annotated-ref-target-oneof` | 21 B, 7 R | 4 / PandaScore publisher grant unproven | S, G, H |
| `annotated-ref-target-string-const` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `anyof-array-variant-anyof-nullable-item` | 5 R | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `anyof-array-variant-closed-object-item` | 26 B, 5 R, 5 D | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `anyof-array-variant-empty-object-item` | 8 B, 2 I | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `anyof-array-variant-oneof-nullable-item` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `array-item-inheritance-union` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `array-item-pointer-walk-anyof` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `array-item-pointer-walk-oneof` | 8 B, 2 I | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `oneof-array-variant-annotated-ref-item` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `oneof-array-variant-anyof-discriminated-union-item` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `oneof-array-variant-anyof-item` | 13 B, 10 R, 2 I | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `oneof-array-variant-anyof-nullable-item` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `oneof-array-variant-closed-object-item` | 15 B | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `oneof-array-variant-composed-item` | 8 B, 2 I | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `oneof-array-variant-empty-object-item` | 3 B, 2 I | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `property-sole-anyof-closed-object-member` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `property-sole-anyof-composed-member` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `property-sole-anyof-empty-object-member` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `property-sole-anyof-struct-member` | 23 B, 1 R, 2 I | 0 / no declarer in acquired readable scope; no candidate to register | S, G, H |
| `property-sole-oneof-closed-object-member` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `property-sole-oneof-composed-member` | 3 B, 2 I | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `property-sole-oneof-empty-object-member` | 0 named artifacts | 0 / no declarer in acquired readable scope; no candidate to register | V, S, G, H |
| `ref-pointer-unnamed-segment` | 55 B, 2 I | 580 / seven Codat versions lack evidenced publisher grants | V, S, G, H |

The I cells preserve unfinished historical screening, including Attentive; a
later acquisition that did not complete that artifact's screen supplies no
refusal for it. B and R cells explain why named historical supply does not yet
prove the key. For the twelve keys with no historical artifacts, the new census
also found no declarer, but unresolved sources still prevent an absence verdict.

### Queue handoff

**Unattempted ranked candidates: none.** The header-only [ranking.tsv](ranking.tsv)
contains zero ranks, so slot 1 exhausts this finite registration queue. There is
no rank to dispatch, no exhaustion claim about inaccessible supply, and no graph
node added by this worker. If a later acquisition supplies a rank, the manager
can use this registration form without changing the frozen ranking:

```text
Assigned slot: <manager-assigned slot>
Candidate: <link to the highest still-relevant unattempted ranking.tsv row>
Prior outcomes: docs/openapi-surface/witness-scrape-wide/slots.md
Deliverable: append the result and specific evidence using that ledger's contract.
```

A present unattempted rank must be reported to the manager using that form;
it is not exhausted. Registration additionally needs the real Route A golden
and Crozier byte comparison before any surface promotion.

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
`just lint-corpus-licensing` and `just lint-llm-diff` against each dispatch comparison base: discovery used
`e88fcc24dbb8d865dbbdab0c65fd9672679bd8a1`; final reconciliation uses
`95ceaa1f` (slot 1’s committed outcome). The witness tests drive real CLI, Git,
filesystem and census boundaries, including corrupt caches, changed digests,
unreachable/malformed inputs, partial inventories, selector/key drift, malformed
ranks, missing evidence, conflicting slot claims and non-ASCII diagnostics.

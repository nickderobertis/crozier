# Renewed witness search for the six `search-incomplete` keys

On 2026-09-30 the six keys whose search record reads `search-incomplete` were
searched again. That record is each key's line under
[`schemas.md`'s Witness search (exhaustive)](../schemas.md#witness-search-exhaustive).
Each key read `search-incomplete` for one reason. GitHub refused 12
`github-code-search` candidates at every route the earlier records show as
tried: the pinned blob, the repository's current head, the history of the path,
Sourcegraph's mirror of the pinned commit, and every namesake repository. The
refusals are the `census` cells of those candidates' rows in
[`../witness-search-github-code-search/records.tsv`](../witness-search-github-code-search/records.tsv).

This search took only routes those records do not show as tried, and only
within Contract B's six declared sources. It kept to routes that plausibly
reach a document. It did not re-run the earlier queries.

**Outcome: all six keys read `none-registrable`.** No route produced a
candidate that passes all three corpus screens. Every candidate the census
confirmed has an outcome on all three screens. Five of the 12 refused rows are
now decided `census 0`. The other seven are still refused by every route, so
the earlier records' `search-incomplete` verdicts stand, and nothing here
reads `exhausted`.

## The routes

Every GitHub request went through
[`scripts/rate_limit_guard.py`](../../../scripts/rate_limit_guard.py): REST
only, no GraphQL, each bucket held at or below 70%. Every Sourcegraph request
went through the guard's paced Sourcegraph lane. No bucket reached the cap and
no wait was made. The guard's per-call record is
[`rate-limit-calls.jsonl`](rate-limit-calls.jsonl). Each request's time, status
and result is [`requests.jsonl`](requests.jsonl).

| route | source | request, per candidate | sent | returned |
|---|---|---|---|---|
| `acquisition-cache` | github-code-search | read the document the source's own acquisition cache holds under the digest another key's row of the same candidate pins (`documents/<sha256>` in the 2026-09-24/25 acquisition caches), kept only where its git blob hash is the blob GitHub's search named | 2026-09-30 | 3 of the 9 refused documents were already cached, each hashing to its named blob: `abylkhaiyrov/Halyk-SafeDeal` (blob `78046bb4`), `prasath-local-host/vibe-platform-architecture-spikes` (`56ecb5c0`) and `vishnu-77/agent-plane` (`90c1f6b8`). Each read `census 0` for every key it was refused for. A git-blob-hash scan of all 73,565 cached documents found none of the other six blobs |
| `repository-by-id` | github-code-search | `GET https://api.github.com/repositories/<id>`, the immutable numeric id the search result's `url` carries, which still resolves a renamed or transferred repository | 2026-09-30T21:09:59Z – 21:10:24Z | HTTP 404 for all six remaining repositories, including `YS-projectcalc/agent-cold-email` and `epifanovmd/rest-api-template-app`, which answered for their head on 2026-09-29 |
| `blob-by-sha` | github-code-search | `GET https://api.github.com/repositories/<id>/git/blobs/<blob>`, the blob object itself rather than a path at a commit | 2026-09-30T21:10:00Z – 21:10:25Z | HTTP 404 for all six |
| `commit-by-sha` | github-code-search | `GET https://api.github.com/repositories/<id>/commits/<pinned commit>` | 2026-09-30T21:10:01Z – 21:10:26Z | HTTP 404 for all six |
| `owner-code-search` | github-code-search | `GET https://api.github.com/users/<owner>`, then `GET https://api.github.com/search/code?q=user:<owner> filename:<basename>&per_page=100`, for the same file under the owner's other repositories | 2026-09-30T21:10:02Z – 21:10:28Z | each owner account answered HTTP 200, and each code search `total_count 0` |
| `sourcegraph-mirror-default-branch` | sourcegraph | `GET https://sourcegraph.com/github.com/<owner>/<repo>/-/raw/<path>`, the mirror's default branch rather than the pinned commit | 2026-09-30T21:10:03Z – 21:10:29Z | HTTP 404 for all six |
| `publisher-revision` | github-publisher-trees | for the two publishers whose documents passed the licence and revision screens and failed only Fern's: `GET https://api.github.com/repos/<repo>`, `GET https://api.github.com/repos/<repo>/commits?path=<path>&per_page=100`, then `GET https://api.github.com/repos/<repo>/contents/<path>?ref=<commit>` and `GET https://api.github.com/repos/<repo>/git/blobs/<blob>` for each revision, kept where the bytes hash to the blob. `APWG/ecx2-openapi-doc` `ecx2-openapi.yaml`, every revision in its history; `OpenRailAssociation/osrd` `editoast/openapi.yaml` at the current head of `dev`, with the root listing at that commit for its licence | 2026-09-30T21:11:21Z – 21:12:42Z, and 21:23:48Z for OSRD's root listing | APWG: 31 commits, 31 revisions read. 9 declare `property-sole-anyof-composed-member`, 17 declare none of the six keys, and the full YAML parser refuses 5, which are JSON pasted into YAML. OSRD: its head `776d7c44` declares `property-sole-oneof-composed-member` once |

Each document was censused with
[`witness-search-recensus.py`](../../../scripts/witness-search-recensus.py)'s
`read_document`, the pinned `ruamel.yaml` 0.19.1 reading, with each key's
selector from [`../witness-search-keys.tsv`](../witness-search-keys.tsv). Each
census-confirmed document was screened by Fern at CLI 5.67.1 and
`fernapi/fern-python-sdk` 5.20.0: `fern check`, then `fern generate --group
python-sdk --local --preview`, in a workspace scaffolded as
[`generate-fern-fixture.sh`](../../../scripts/generate-fern-fixture.sh) scaffolds
one.

## The per-key outcomes

| key | outcome | routes not tried before | candidates, and what decided each | still refused |
|---|---|---|---|---|
| `array-item-inheritance-union` | `none-registrable` | `repository-by-id`, `blob-by-sha`, `commit-by-sha`, `owner-code-search`, `sourcegraph-mirror-default-branch` | none: every route refused `YS-projectcalc/agent-cold-email` `site/openapi.yaml`, and the owner's code search named no file | `YS-projectcalc/agent-cold-email:site/openapi.yaml` |
| `array-item-pointer-walk-oneof` | `none-registrable` | `repository-by-id`, `blob-by-sha`, `commit-by-sha`, `owner-code-search`, `sourcegraph-mirror-default-branch` | none: every route refused both candidates, and neither owner's code search named a file | `YS-projectcalc/agent-cold-email:site/openapi.yaml`, `Gressling/Cheminf-EDU:swagger.yaml` |
| `property-sole-anyof-composed-member` | `none-registrable` | `acquisition-cache`, `repository-by-id`, `blob-by-sha`, `commit-by-sha`, `owner-code-search`, `sourcegraph-mirror-default-branch`, `publisher-revision` | `abylkhaiyrov/Halyk-SafeDeal` `docs/openapi.yaml`: `census 0` from the cache. APWG's eCX description, nine census-confirmed revisions (2 to 6 sites each): each passes the licence screen (GPL-3.0, repository licence and `info.license`) and the revision screen (its commit), and each fails Fern's. Seven fail `fern check` (18 to 24 errors, `Path parameter is unreferenced in endpoint: noteId`, or `Objects can only extend other objects, and root.ActorCategory is not an object`). `4c71b3d3` passes `fern check`, and the generator exits 1 on a `SyntaxError` in the `report_phishing_fields.py` it generated. `9218d45c`, the head, is the revision the earlier record already screened. The other 22 revisions: 17 `census 0`, 5 `census-refused` | `epifanovmd/rest-api-template-app:swagger.json` |
| `property-sole-anyof-empty-object-member` | `none-registrable` | `acquisition-cache`, `repository-by-id`, `blob-by-sha`, `commit-by-sha`, `owner-code-search`, `sourcegraph-mirror-default-branch` | `vishnu-77/agent-plane` `docs/openapi.json`: `census 0` from the cache | `SamakshMathur/LETA-TEC-INFRA:frontend/.orval/openapi.json`, `jdgiles26/madrona-main:docs/openapi.json`, `thecoducer/TravelCopilot:backend/openapi.json` |
| `property-sole-oneof-composed-member` | `none-registrable` | `acquisition-cache`, `publisher-revision` | `abylkhaiyrov/Halyk-SafeDeal` `docs/openapi.yaml` and `prasath-local-host/vibe-platform-architecture-spikes` `openapi.json`: `census 0` from the cache. OSRD `editoast/openapi.yaml` at `776d7c44`: census 1, licence screen passed (LGPL-3.0, `info.license` and the tree's `LICENSES` directory), revision screen passed (its commit). Fern's screen failed: `fern check` exit 0 with 11 warnings, and the generator exits 1 on ruff's `F811 Redefinition of unused EditoastError_EditoastTrainScheduleExceptionNotFound` in the tree it generated, as at `39373752` before | none: both refused rows are decided |
| `property-sole-oneof-empty-object-member` | `none-registrable` | `acquisition-cache` | `prasath-local-host/vibe-platform-architecture-spikes` `openapi.json`: `census 0` from the cache | none: its one refused row is decided |

`none-registrable` means that no route produced a candidate that passes all
three screens, and that every candidate the census confirmed is decided. The
earlier records' own verdicts are unchanged. The four keys with a row that is
still refused stay `search-incomplete` there, since those documents have never
been read. Each key now rests on the hand-written fixture of the same name
under [`../handwritten/`](../handwritten/), whose cover cites both this record
and its `search-incomplete` line.

## The ledgers

One ledger per source this search used. Each has one row per candidate per
route, and the publisher-revision routes' own requests are rows too:
[`github-code-search.tsv`](github-code-search.tsv) (33 rows),
[`sourcegraph.tsv`](sourcegraph.tsv) (7) and
[`github-publisher-trees.tsv`](github-publisher-trees.tsv) (37). apis.guru,
jentic and vendor-portals were not searched again. The earlier records
censused each of their whole collections, and no refused candidate is in any
of them. The columns are:

```
source	key	candidate	revision	digest	route	request	at	status	census	licence_screen	revision_screen	fern_screen	disposition
```

`disposition` is `rejected` for a candidate the census or a screen decided,
`refused` for a candidate that route could not read, and `route` for a
request that lists or describes rather than reads a document.

## What would still move a key

A refused document that GitHub or a mirror serves again. Re-request the seven
with `scripts/witness-search-recensus.py reacquire-head --again` and
`reacquire-namesake --again`. Also, a Fern that generates APWG's eCX
description or OSRD's editoast description.

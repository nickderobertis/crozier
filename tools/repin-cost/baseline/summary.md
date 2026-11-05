# Repin cost — `runs:Close-crozier-s-remaining-Fern-parity-gaps,Close-crozier-s-remaining-Fern-departures-and-unproven-features-and-combinations` until 2026-11-02T12:30:01+00:00

- Changes: 26 (26 with a PR, 20 merged); CI runs 67, failed 28.
- Census-tier CI failures: 15 (0.58 per change, 9 changes hit); runner 3453.6 min, elapsed 1403.4 min, CI retry wait (failed run's end to the branch's next CI run's start) 2595.2 min, 3 with no next CI run by the cutoff (unresolved, not counted) (cycle 3998.6 min, median 230.9 per failure).
- Census-failed journal publications: 6 (the attempt's recorded end to the branch's next attempt's recorded start): 3 observed, 286.7 min (median 80.4); 3 unresolved (no next publication by the cutoff); 9 census failures had no journal publication.
- Publication attempts 47 (census-failed 6); re-dispatches 78 (after a census failure 9, after a derived conflict 8).
- Derived-table conflicts: 9 (6 changes), wait to next attempt 3839.9 min (median 423.8 per conflict), 4 of them also conflicting in code; code-only conflicts 1.

Per kind (a failure naming several kinds counts once under each; its minutes are split evenly between them):

| kind | events | changes | runner min | elapsed min | wait min (CI retry; for a conflict, to the next attempt) | cycle min | publication attempts | publication interval min (observed / unresolved) | re-dispatches |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `derived-conflict` | 9 | 6 | 0.0 | 0.0 | 3839.9 | 3839.9 | 0 | n/a | 8 |
| `measured-count` | 4 | 3 | 776.2 | 294.8 | 322.5 | 617.3 | 2 | 10.3 (1 / 1) | 3 |
| `other-artifact:docs/fern-refusals/classes.tsv` | 1 | 1 | 68.0 | 30.2 | 9.6 | 39.8 | 1 | 9.2 (1 / 0) | 1 |
| `other-artifact:docs/fern-refusals/documents.tsv` | 1 | 1 | 68.0 | 30.2 | 9.6 | 39.8 | 1 | 9.2 (1 / 0) | 1 |
| `other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv` | 4 | 4 | 788.6 | 300.2 | 346.5 | 646.7 | 4 | 344.1 (4 / 0) | 4 |
| `port-digest` | 9 | 6 | 1287.9 | 532.1 | 1134.4 | 1666.5 | 4 | 276.4 (2 / 2) | 7 |
| `site-anchor` | 9 | 6 | 1389.3 | 576.7 | 1138.2 | 1714.9 | 1 | 0.0 (0 / 1) | 4 |

| artifact outside the census | CI failures | conflicts | changes | cycle min | runner min |
| --- | --- | --- | --- | --- | --- |
| `docs/openapi-surface/witness-search-registries/outstanding.tsv` | 4 | 0 | 4 | 646.7 | 788.6 |
| `tests/fixtures/compared-goldens.json` | 0 | 5 | 5 | 127.0 | 0.0 |
| `tests/fixtures/departures-ledger.tsv` | 0 | 5 | 5 | 127.0 | 0.0 |
| `tests/fixtures/CORPUS.md` | 0 | 1 | 1 | 39.9 | 0.0 |
| `tests/fixtures/corpus-sources.tsv` | 0 | 1 | 1 | 39.9 | 0.0 |
| `docs/fern-refusals/classes.tsv` | 1 | 0 | 1 | 39.8 | 68.0 |
| `docs/fern-refusals/documents.tsv` | 1 | 0 | 1 | 39.8 | 68.0 |
| `docs/fern-measurements/cases.tsv` | 0 | 2 | 2 | 35.9 | 0.0 |
| `docs/openapi-surface/scenario-proof-index.tsv` | 0 | 1 | 1 | 35.9 | 0.0 |

Examined and excluded from every total: 1 (1 without a pull request); see excluded.tsv.

GitHub: 0 uncached calls, 173 cache hits.

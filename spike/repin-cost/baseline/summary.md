# Repin cost — `runs:Close-crozier-s-remaining-Fern-parity-gaps,Close-crozier-s-remaining-Fern-departures-and-unproven-features-and-combinations` until 2026-11-02T12:30:01+00:00

- Changes: 27 (26 with a PR, 20 merged); CI runs 68, failed 28.
- Census-tier CI failures: 15 (0.56 per change, 9 changes hit); runner 3453.6 min, elapsed 1403.4 min, wait to next run 2595.2 min (cycle 3998.6 min, median 230.9 per failure).
- Publication attempts 47 (census-failed 6); re-dispatches 82 (after a census failure 9, after a derived conflict 9).
- Derived-table conflicts: 10 (7 changes), wait to next attempt 3839.9 min (median 371.5 per conflict); code-only conflicts 5.

Per kind (a failure naming several kinds counts once under each; its minutes are split evenly between them):

| kind | events | changes | runner min | elapsed min | wait min | cycle min | publication attempts | re-dispatches |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `derived-conflict` | 10 | 7 | 0.0 | 0.0 | 3839.9 | 3839.9 | 0 | 9 |
| `measured-count` | 4 | 3 | 776.2 | 294.8 | 322.5 | 617.3 | 2 | 3 |
| `other-artifact:docs/fern-refusals/classes.tsv` | 1 | 1 | 68.0 | 30.2 | 9.6 | 39.8 | 1 | 1 |
| `other-artifact:docs/fern-refusals/documents.tsv` | 1 | 1 | 68.0 | 30.2 | 9.6 | 39.8 | 1 | 1 |
| `other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv` | 4 | 4 | 788.6 | 300.2 | 346.5 | 646.7 | 4 | 4 |
| `port-digest` | 9 | 6 | 1287.9 | 532.1 | 1134.4 | 1666.5 | 4 | 7 |
| `site-anchor` | 9 | 6 | 1389.3 | 576.7 | 1138.2 | 1714.9 | 1 | 4 |

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

GitHub: 0 uncached calls, 175 cache hits.

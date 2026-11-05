# Repin cost — `base-carries:6302409297c5f81b34b7884207d2029a02dbd508` until 2026-11-02T12:30:01+00:00

- Changes: 3 (3 with a PR, 0 merged); CI runs 14, failed 6.
- Census-tier CI failures: 5 (1.67 per change, 3 changes hit); runner 1158.8 min, elapsed 473.8 min, wait to next run 1062.9 min (cycle 1536.7 min, median 293.4 per failure).
- Publication attempts 3 (census-failed 2); re-dispatches 7 (after a census failure 3, after a derived conflict 0).
- Derived-table conflicts: 1 (1 changes), wait to next attempt 0.0 min (median 0.0 per conflict), 1 of them also conflicting in code; code-only conflicts 0.

Per kind (a failure naming several kinds counts once under each; its minutes are split evenly between them):

| kind | events | changes | runner min | elapsed min | wait min | cycle min | publication attempts | re-dispatches |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `derived-conflict` | 1 | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 0 | 0 |
| `measured-count` | 3 | 2 | 548.8 | 214.3 | 311.8 | 526.1 | 1 | 2 |
| `port-digest` | 3 | 2 | 305.0 | 129.8 | 375.5 | 505.3 | 1 | 2 |
| `site-anchor` | 3 | 2 | 305.0 | 129.8 | 375.5 | 505.3 | 1 | 2 |

| artifact outside the census | CI failures | conflicts | changes | cycle min | runner min |
| --- | --- | --- | --- | --- | --- |
| `docs/fern-measurements/cases.tsv` | 0 | 1 | 1 | 0.0 | 0.0 |
| `tests/fixtures/compared-goldens.json` | 0 | 1 | 1 | 0.0 | 0.0 |
| `tests/fixtures/departures-ledger.tsv` | 0 | 1 | 1 | 0.0 | 0.0 |

Examined and excluded from every total: 209 (107 whose base lacks a required commit; 102 without a pull request); see excluded.tsv.

GitHub: 0 uncached calls, 35 cache hits.

# Repin cost — `base-carries:27ff7dc6455505147f59fd3b0b3aa2d06141091d,8cbca1f51b1a6a5702cb8e9ddc9db06f21d45a73` until 2026-11-06T15:47:39.549000+00:00

- Changes: 5 (5 with a PR, 1 merged); CI runs 7, failed 6.
- Census-tier CI failures: 3 (0.60 per change, 2 changes hit); runner 726.9 min, elapsed 297.8 min, CI retry wait (failed run's end to the branch's next CI run's start) 1717.8 min, 2 with no next CI run by the cutoff (unresolved, not counted) (cycle 2015.6 min, median 108.0 per failure).
- Census-failed journal publications: 1 (the attempt's recorded end to the branch's next attempt's recorded start): 0 observed, 0.0 min (median 0.0); 1 unresolved (no next publication by the cutoff); 2 census failures had no journal publication.
- Publication attempts 3 (census-failed 1); re-dispatches 22 (after a census failure 2, after a derived conflict 3).
- Derived-table conflicts: 3 (2 changes), wait to next attempt 1963.8 min (median 0.0 per conflict), 1 of them also conflicting in code; code-only conflicts 0.

Per kind (a failure naming several kinds counts once under each; its minutes are split evenly between them):

| kind | events | changes | runner min | elapsed min | wait min (CI retry; for a conflict, to the next attempt) | cycle min | publication attempts | publication interval min (observed / unresolved) | re-dispatches |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `census-unattributed` | 2 | 2 | 449.9 | 195.0 | 0.0 | 195.0 | 1 | 0.0 (0 / 1) | 1 |
| `derived-conflict` | 3 | 2 | 0.0 | 0.0 | 1963.8 | 1963.8 | 0 | n/a | 3 |
| `measured-count` | 1 | 1 | 92.3 | 34.3 | 572.6 | 606.9 | 0 | n/a | 1 |
| `other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports` | 1 | 1 | 222.2 | 88.7 | 0.0 | 88.7 | 0 | n/a | 0 |
| `port-digest` | 1 | 1 | 92.3 | 34.3 | 572.6 | 606.9 | 0 | n/a | 1 |
| `site-anchor` | 1 | 1 | 92.3 | 34.3 | 572.6 | 606.9 | 0 | n/a | 1 |

| artifact outside the census | CI failures | conflicts | changes | cycle min | runner min |
| --- | --- | --- | --- | --- | --- |
| `task:fern-goldens-git:test-certified-pair,surface-reach:test-ports` | 1 | 0 | 1 | 88.7 | 222.2 |
| `docs/openapi-surface/golden-reach-witnesses/outstanding.tsv` | 0 | 1 | 1 | 0.0 | 0.0 |

Examined and excluded from every total: 230 (122 whose base lacks a required commit; 108 without a pull request); see excluded.tsv.

GitHub: 19 uncached calls, 9 cache hits.

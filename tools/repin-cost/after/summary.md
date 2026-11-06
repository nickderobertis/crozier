# Repin cost — `base-carries:27ff7dc6455505147f59fd3b0b3aa2d06141091d,8cbca1f51b1a6a5702cb8e9ddc9db06f21d45a73` until 2026-11-06T05:14:09.186000+00:00

- Changes: 2 (2 with a PR, 1 merged); CI runs 3, failed 2.
- Census-tier CI failures: 1 (0.50 per change, 1 changes hit); runner 205.5 min, elapsed 87.0 min, CI retry wait (failed run's end to the branch's next CI run's start) 0.0 min, 1 with no next CI run by the cutoff (unresolved, not counted) (cycle 87.0 min, median 87.0 per failure).
- Census-failed journal publications: 1 (the attempt's recorded end to the branch's next attempt's recorded start): 0 observed, 0.0 min (median 0.0); 1 unresolved (no next publication by the cutoff); 0 census failures had no journal publication.
- Publication attempts 2 (census-failed 1); re-dispatches 4 (after a census failure 1, after a derived conflict 0).
- Derived-table conflicts: 0 (0 changes), wait to next attempt 0.0 min (median 0.0 per conflict), 0 of them also conflicting in code; code-only conflicts 0.

Per kind (a failure naming several kinds counts once under each; its minutes are split evenly between them):

| kind | events | changes | runner min | elapsed min | wait min (CI retry; for a conflict, to the next attempt) | cycle min | publication attempts | publication interval min (observed / unresolved) | re-dispatches |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `census-unattributed` | 1 | 1 | 205.5 | 87.0 | 0.0 | 87.0 | 1 | 0.0 (0 / 1) | 1 |

| artifact outside the census | CI failures | conflicts | changes | cycle min | runner min |
| --- | --- | --- | --- | --- | --- |

Examined and excluded from every total: 230 (123 whose base lacks a required commit; 107 without a pull request); see excluded.tsv.

GitHub: 9 uncached calls, 0 cache hits.

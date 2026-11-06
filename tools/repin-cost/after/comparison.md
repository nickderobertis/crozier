# Repin cost after the incremental census tooling

Measured comparison: 5 after-sample changes; 26 baseline changes.
Cycle intervals include other work and queueing; they do not establish causation.

After-sample PRs: #774, #775, #776, #778, #780.
Landing commits: 27ff7dc6455505147f59fd3b0b3aa2d06141091d, 8cbca1f51b1a6a5702cb8e9ddc9db06f21d45a73.
Cutoff: 2026-11-06T15:47:39.549000+00:00.

```sh
python3 tools/repin-cost/repin_cost.py --window base-carries:27ff7dc6455505147f59fd3b0b3aa2d06141091d,8cbca1f51b1a6a5702cb8e9ddc9db06f21d45a73 --runs-root "$ONEPIPELINE_RUNS_DIR" --until 2026-11-06T15:47:39.549000+00:00 --out tools/repin-cost/after
python3 tools/repin-cost/repin_cost.py compare tools/repin-cost/baseline tools/repin-cost/after
```

Differences are after minus baseline. Per-change denominators are all eligible changes, including those with no repin.
An empty sample has undefined per-change rates (n/a). Unresolved intervals remain excluded from minute sums and medians.
Kind counts overlap when a failure names several kinds; its minutes are split evenly, as in the baseline.
Medians and changes-hit counts are also shown per eligible change for completeness; median totals retain their original meaning.

| figure | baseline total | baseline / change | after total | after / change | difference total | difference / change |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `artifact.docs/fern-measurements/cases.tsv.changes` | 2.00 | 0.08 | 0.00 | 0.00 | -2.00 | -0.08 |
| `artifact.docs/fern-measurements/cases.tsv.ci_failures` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/fern-measurements/cases.tsv.conflicts` | 2.00 | 0.08 | 0.00 | 0.00 | -2.00 | -0.08 |
| `artifact.docs/fern-measurements/cases.tsv.cycle_min` | 35.90 | 1.38 | 0.00 | 0.00 | -35.90 | -1.38 |
| `artifact.docs/fern-measurements/cases.tsv.runner_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/fern-refusals/classes.tsv.changes` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.docs/fern-refusals/classes.tsv.ci_failures` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.docs/fern-refusals/classes.tsv.conflicts` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/fern-refusals/classes.tsv.cycle_min` | 39.80 | 1.53 | 0.00 | 0.00 | -39.80 | -1.53 |
| `artifact.docs/fern-refusals/classes.tsv.runner_min` | 68.00 | 2.62 | 0.00 | 0.00 | -68.00 | -2.62 |
| `artifact.docs/fern-refusals/documents.tsv.changes` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.docs/fern-refusals/documents.tsv.ci_failures` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.docs/fern-refusals/documents.tsv.conflicts` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/fern-refusals/documents.tsv.cycle_min` | 39.80 | 1.53 | 0.00 | 0.00 | -39.80 | -1.53 |
| `artifact.docs/fern-refusals/documents.tsv.runner_min` | 68.00 | 2.62 | 0.00 | 0.00 | -68.00 | -2.62 |
| `artifact.docs/openapi-surface/golden-reach-witnesses/outstanding.tsv.changes` | 0.00 | 0.00 | 1.00 | 0.20 | +1.00 | +0.20 |
| `artifact.docs/openapi-surface/golden-reach-witnesses/outstanding.tsv.ci_failures` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/openapi-surface/golden-reach-witnesses/outstanding.tsv.conflicts` | 0.00 | 0.00 | 1.00 | 0.20 | +1.00 | +0.20 |
| `artifact.docs/openapi-surface/golden-reach-witnesses/outstanding.tsv.cycle_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/openapi-surface/golden-reach-witnesses/outstanding.tsv.runner_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.changes` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.ci_failures` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.conflicts` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.cycle_min` | 35.90 | 1.38 | 0.00 | 0.00 | -35.90 | -1.38 |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.runner_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.changes` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.ci_failures` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.conflicts` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.cycle_min` | 646.70 | 24.87 | 0.00 | 0.00 | -646.70 | -24.87 |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.runner_min` | 788.60 | 30.33 | 0.00 | 0.00 | -788.60 | -30.33 |
| `artifact.task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.changes` | 0.00 | 0.00 | 1.00 | 0.20 | +1.00 | +0.20 |
| `artifact.task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.ci_failures` | 0.00 | 0.00 | 1.00 | 0.20 | +1.00 | +0.20 |
| `artifact.task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.conflicts` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.cycle_min` | 0.00 | 0.00 | 88.70 | 17.74 | +88.70 | +17.74 |
| `artifact.task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.runner_min` | 0.00 | 0.00 | 222.20 | 44.44 | +222.20 | +44.44 |
| `artifact.tests/fixtures/CORPUS.md.changes` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.tests/fixtures/CORPUS.md.ci_failures` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.tests/fixtures/CORPUS.md.conflicts` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.tests/fixtures/CORPUS.md.cycle_min` | 39.90 | 1.53 | 0.00 | 0.00 | -39.90 | -1.53 |
| `artifact.tests/fixtures/CORPUS.md.runner_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.tests/fixtures/compared-goldens.json.changes` | 5.00 | 0.19 | 0.00 | 0.00 | -5.00 | -0.19 |
| `artifact.tests/fixtures/compared-goldens.json.ci_failures` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.tests/fixtures/compared-goldens.json.conflicts` | 5.00 | 0.19 | 0.00 | 0.00 | -5.00 | -0.19 |
| `artifact.tests/fixtures/compared-goldens.json.cycle_min` | 127.00 | 4.88 | 0.00 | 0.00 | -127.00 | -4.88 |
| `artifact.tests/fixtures/compared-goldens.json.runner_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.tests/fixtures/corpus-sources.tsv.changes` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.tests/fixtures/corpus-sources.tsv.ci_failures` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.tests/fixtures/corpus-sources.tsv.conflicts` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `artifact.tests/fixtures/corpus-sources.tsv.cycle_min` | 39.90 | 1.53 | 0.00 | 0.00 | -39.90 | -1.53 |
| `artifact.tests/fixtures/corpus-sources.tsv.runner_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.tests/fixtures/departures-ledger.tsv.changes` | 5.00 | 0.19 | 0.00 | 0.00 | -5.00 | -0.19 |
| `artifact.tests/fixtures/departures-ledger.tsv.ci_failures` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `artifact.tests/fixtures/departures-ledger.tsv.conflicts` | 5.00 | 0.19 | 0.00 | 0.00 | -5.00 | -0.19 |
| `artifact.tests/fixtures/departures-ledger.tsv.cycle_min` | 127.00 | 4.88 | 0.00 | 0.00 | -127.00 | -4.88 |
| `artifact.tests/fixtures/departures-ledger.tsv.runner_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `attempts` | 47.00 | 1.81 | 3.00 | 0.60 | -44.00 | -1.21 |
| `census.attempts` | 6.00 | 0.23 | 1.00 | 0.20 | -5.00 | -0.03 |
| `census.changes_hit` | 9.00 | 0.35 | 2.00 | 0.40 | -7.00 | +0.05 |
| `census.ci_retry_unresolved` | 3.00 | 0.12 | 2.00 | 0.40 | -1.00 | +0.28 |
| `census.cycle_min` | 3998.60 | 153.79 | 2015.60 | 403.12 | -1983.00 | +249.33 |
| `census.elapsed_min` | 1403.40 | 53.98 | 297.80 | 59.56 | -1105.60 | +5.58 |
| `census.failures` | 15.00 | 0.58 | 3.00 | 0.60 | -12.00 | +0.02 |
| `census.median_cycle_min` | 230.90 | 8.88 | 108.00 | 21.60 | -122.90 | +12.72 |
| `census.median_pub_wait_min` | 80.40 | 3.09 | 0.00 | 0.00 | -80.40 | -3.09 |
| `census.pub_observed` | 3.00 | 0.12 | 0.00 | 0.00 | -3.00 | -0.12 |
| `census.pub_unresolved` | 3.00 | 0.12 | 1.00 | 0.20 | -2.00 | +0.08 |
| `census.pub_wait_min` | 286.70 | 11.03 | 0.00 | 0.00 | -286.70 | -11.03 |
| `census.publications` | 6.00 | 0.23 | 1.00 | 0.20 | -5.00 | -0.03 |
| `census.redispatches` | 9.00 | 0.35 | 2.00 | 0.40 | -7.00 | +0.05 |
| `census.runner_min` | 3453.60 | 132.83 | 726.90 | 145.38 | -2726.70 | +12.55 |
| `census.wait_min` | 2595.20 | 99.82 | 1717.80 | 343.56 | -877.40 | +243.74 |
| `census_and_conflict_redispatches` | 17.00 | 0.65 | 5.00 | 1.00 | -12.00 | +0.35 |
| `changes` | 26.00 | 1.00 | 5.00 | 1.00 | -21.00 | +0.00 |
| `changes_with_pr` | 26.00 | 1.00 | 5.00 | 1.00 | -21.00 | +0.00 |
| `ci_failed` | 28.00 | 1.08 | 6.00 | 1.20 | -22.00 | +0.12 |
| `ci_runs` | 67.00 | 2.58 | 7.00 | 1.40 | -60.00 | -1.18 |
| `conflicts.changes_hit` | 6.00 | 0.23 | 2.00 | 0.40 | -4.00 | +0.17 |
| `conflicts.code` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `conflicts.derived` | 9.00 | 0.35 | 3.00 | 0.60 | -6.00 | +0.25 |
| `conflicts.median_wait_min` | 423.80 | 16.30 | 0.00 | 0.00 | -423.80 | -16.30 |
| `conflicts.mixed` | 4.00 | 0.15 | 1.00 | 0.20 | -3.00 | +0.05 |
| `conflicts.redispatches` | 8.00 | 0.31 | 3.00 | 0.60 | -5.00 | +0.29 |
| `conflicts.wait_min` | 3839.90 | 147.69 | 1963.80 | 392.76 | -1876.10 | +245.07 |
| `kind.census-unattributed.attempts` | 0.00 | 0.00 | 1.00 | 0.20 | +1.00 | +0.20 |
| `kind.census-unattributed.changes` | 0.00 | 0.00 | 2.00 | 0.40 | +2.00 | +0.40 |
| `kind.census-unattributed.cycle_min` | 0.00 | 0.00 | 195.00 | 39.00 | +195.00 | +39.00 |
| `kind.census-unattributed.elapsed_min` | 0.00 | 0.00 | 195.00 | 39.00 | +195.00 | +39.00 |
| `kind.census-unattributed.events` | 0.00 | 0.00 | 2.00 | 0.40 | +2.00 | +0.40 |
| `kind.census-unattributed.pub_observed` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.census-unattributed.pub_unresolved` | 0.00 | 0.00 | 1.00 | 0.20 | +1.00 | +0.20 |
| `kind.census-unattributed.pub_wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.census-unattributed.redispatches` | 0.00 | 0.00 | 1.00 | 0.20 | +1.00 | +0.20 |
| `kind.census-unattributed.runner_min` | 0.00 | 0.00 | 449.90 | 89.98 | +449.90 | +89.98 |
| `kind.census-unattributed.wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.attempts` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.changes` | 6.00 | 0.23 | 2.00 | 0.40 | -4.00 | +0.17 |
| `kind.derived-conflict.cycle_min` | 3839.90 | 147.69 | 1963.80 | 392.76 | -1876.10 | +245.07 |
| `kind.derived-conflict.elapsed_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.events` | 9.00 | 0.35 | 3.00 | 0.60 | -6.00 | +0.25 |
| `kind.derived-conflict.pub_observed` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.pub_unresolved` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.pub_wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.redispatches` | 8.00 | 0.31 | 3.00 | 0.60 | -5.00 | +0.29 |
| `kind.derived-conflict.runner_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.wait_min` | 3839.90 | 147.69 | 1963.80 | 392.76 | -1876.10 | +245.07 |
| `kind.measured-count.attempts` | 2.00 | 0.08 | 0.00 | 0.00 | -2.00 | -0.08 |
| `kind.measured-count.changes` | 3.00 | 0.12 | 1.00 | 0.20 | -2.00 | +0.08 |
| `kind.measured-count.cycle_min` | 617.30 | 23.74 | 606.90 | 121.38 | -10.40 | +97.64 |
| `kind.measured-count.elapsed_min` | 294.80 | 11.34 | 34.30 | 6.86 | -260.50 | -4.48 |
| `kind.measured-count.events` | 4.00 | 0.15 | 1.00 | 0.20 | -3.00 | +0.05 |
| `kind.measured-count.pub_observed` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.measured-count.pub_unresolved` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.measured-count.pub_wait_min` | 10.30 | 0.40 | 0.00 | 0.00 | -10.30 | -0.40 |
| `kind.measured-count.redispatches` | 3.00 | 0.12 | 1.00 | 0.20 | -2.00 | +0.08 |
| `kind.measured-count.runner_min` | 776.20 | 29.85 | 92.30 | 18.46 | -683.90 | -11.39 |
| `kind.measured-count.wait_min` | 322.50 | 12.40 | 572.60 | 114.52 | +250.10 | +102.12 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.attempts` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.changes` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.cycle_min` | 39.80 | 1.53 | 0.00 | 0.00 | -39.80 | -1.53 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.elapsed_min` | 30.20 | 1.16 | 0.00 | 0.00 | -30.20 | -1.16 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.events` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.pub_observed` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.pub_unresolved` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.pub_wait_min` | 9.20 | 0.35 | 0.00 | 0.00 | -9.20 | -0.35 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.redispatches` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.runner_min` | 68.00 | 2.62 | 0.00 | 0.00 | -68.00 | -2.62 |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.wait_min` | 9.60 | 0.37 | 0.00 | 0.00 | -9.60 | -0.37 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.attempts` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.changes` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.cycle_min` | 39.80 | 1.53 | 0.00 | 0.00 | -39.80 | -1.53 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.elapsed_min` | 30.20 | 1.16 | 0.00 | 0.00 | -30.20 | -1.16 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.events` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.pub_observed` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.pub_unresolved` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.pub_wait_min` | 9.20 | 0.35 | 0.00 | 0.00 | -9.20 | -0.35 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.redispatches` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.runner_min` | 68.00 | 2.62 | 0.00 | 0.00 | -68.00 | -2.62 |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.wait_min` | 9.60 | 0.37 | 0.00 | 0.00 | -9.60 | -0.37 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.attempts` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.changes` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.cycle_min` | 646.70 | 24.87 | 0.00 | 0.00 | -646.70 | -24.87 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.elapsed_min` | 300.20 | 11.55 | 0.00 | 0.00 | -300.20 | -11.55 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.events` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.pub_observed` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.pub_unresolved` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.pub_wait_min` | 344.10 | 13.23 | 0.00 | 0.00 | -344.10 | -13.23 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.redispatches` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.runner_min` | 788.60 | 30.33 | 0.00 | 0.00 | -788.60 | -30.33 |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.wait_min` | 346.50 | 13.33 | 0.00 | 0.00 | -346.50 | -13.33 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.attempts` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.changes` | 0.00 | 0.00 | 1.00 | 0.20 | +1.00 | +0.20 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.cycle_min` | 0.00 | 0.00 | 88.70 | 17.74 | +88.70 | +17.74 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.elapsed_min` | 0.00 | 0.00 | 88.70 | 17.74 | +88.70 | +17.74 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.events` | 0.00 | 0.00 | 1.00 | 0.20 | +1.00 | +0.20 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.pub_observed` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.pub_unresolved` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.pub_wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.redispatches` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.runner_min` | 0.00 | 0.00 | 222.20 | 44.44 | +222.20 | +44.44 |
| `kind.other-artifact:task:fern-goldens-git:test-certified-pair,surface-reach:test-ports.wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.port-digest.attempts` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `kind.port-digest.changes` | 6.00 | 0.23 | 1.00 | 0.20 | -5.00 | -0.03 |
| `kind.port-digest.cycle_min` | 1666.50 | 64.10 | 606.90 | 121.38 | -1059.60 | +57.28 |
| `kind.port-digest.elapsed_min` | 532.10 | 20.47 | 34.30 | 6.86 | -497.80 | -13.61 |
| `kind.port-digest.events` | 9.00 | 0.35 | 1.00 | 0.20 | -8.00 | -0.15 |
| `kind.port-digest.pub_observed` | 2.00 | 0.08 | 0.00 | 0.00 | -2.00 | -0.08 |
| `kind.port-digest.pub_unresolved` | 2.00 | 0.08 | 0.00 | 0.00 | -2.00 | -0.08 |
| `kind.port-digest.pub_wait_min` | 276.40 | 10.63 | 0.00 | 0.00 | -276.40 | -10.63 |
| `kind.port-digest.redispatches` | 7.00 | 0.27 | 1.00 | 0.20 | -6.00 | -0.07 |
| `kind.port-digest.runner_min` | 1287.90 | 49.53 | 92.30 | 18.46 | -1195.60 | -31.07 |
| `kind.port-digest.wait_min` | 1134.40 | 43.63 | 572.60 | 114.52 | -561.80 | +70.89 |
| `kind.site-anchor.attempts` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.site-anchor.changes` | 6.00 | 0.23 | 1.00 | 0.20 | -5.00 | -0.03 |
| `kind.site-anchor.cycle_min` | 1714.90 | 65.96 | 606.90 | 121.38 | -1108.00 | +55.42 |
| `kind.site-anchor.elapsed_min` | 576.70 | 22.18 | 34.30 | 6.86 | -542.40 | -15.32 |
| `kind.site-anchor.events` | 9.00 | 0.35 | 1.00 | 0.20 | -8.00 | -0.15 |
| `kind.site-anchor.pub_observed` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.site-anchor.pub_unresolved` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.site-anchor.pub_wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.site-anchor.redispatches` | 4.00 | 0.15 | 1.00 | 0.20 | -3.00 | +0.05 |
| `kind.site-anchor.runner_min` | 1389.30 | 53.43 | 92.30 | 18.46 | -1297.00 | -34.97 |
| `kind.site-anchor.wait_min` | 1138.20 | 43.78 | 572.60 | 114.52 | -565.60 | +70.74 |
| `merged` | 20.00 | 0.77 | 1.00 | 0.20 | -19.00 | -0.57 |
| `other_failures` | 13.00 | 0.50 | 3.00 | 0.60 | -10.00 | +0.10 |
| `redispatches` | 78.00 | 3.00 | 22.00 | 4.40 | -56.00 | +1.40 |

| census failures / change reference | reference | after | difference |
| --- | ---: | ---: | ---: |
| pooled baseline | 0.58 | 0.60 | +0.02 |
| live run baseline | 1.86 | 0.60 | -1.26 |

After measurement GitHub quota: 19 uncached core REST calls; 9 cache hits.
The dispatch-wide quota and baseline-cache verification are recorded in the hand-counted evidence below.


## Hand count: census repins by the recipe and by hand

Read from each change's commits and from the worker transcripts of the runs that made them. A repin here is a commit on the change, up to the head the cutoff saw, whose diff rewrites a table the harness's `artifact_kind` calls `site-anchor`, `port-digest` or `measured-count`, or the `golden-reach-witnesses/outstanding.tsv` list `just census-repin` regenerates; a merge counts when its combined diff touches one. "Recipe" means the commit carries the output of `just census-repin` or of `tools/surface-census/census-repin.py`, the script the recipe runs. "Hand" means anything else: a generator run directly, an ad-hoc script, `sed`, a prose edit, or a merge resolved by the worker. Commits that touch only other artifacts, such as `residual-attribution.json`, are outside this count. The attribution is inferred from transcript order: where a session ran several generators, the row names the one before the commit that its diff reflects.

**Totals: 45 repins across the changes, 11 with the recipe and 34 by hand.** Four commits were made on #774's branch and merged into #776's, so they appear under both: 41 distinct commits, 10 with the recipe and 31 by hand. Only 19 of the 45 were made once the branch's base carried both landing commits, from its merge of `main` onward: 8 with the recipe and 11 by hand. #778 made none up to the head the cutoff saw.

| change | repins | recipe | hand | with both commits in the base: recipe / hand |
| --- | ---: | ---: | ---: | ---: |
| #774 | 12 | 4 | 8 | 3 / 3 |
| #775 | 3 | 1 | 2 | 1 / 1 |
| #776 | 17 | 4 | 13 | 2 / 3 |
| #778 | 0 | 0 | 0 | 0 / 0 |
| #780 | 13 | 2 | 11 | 2 / 4 |

| PR | commit | how | base carried both? | evidence |
| --- | --- | --- | --- | --- |
| #774 | 137b06c05 | hand | no | no rewriting recipe run before the commit |
| #774 | 38105d3cb | hand | no | only `census-repin --base-only` before the commit, which rewrites no table |
| #774 | daa26ba30 | hand | no | `golden-reach-search.py outstanding` run directly |
| #774 | 0fc68b7fb | recipe | no | `just census-repin --jobs 1 --verbose`, then committed |
| #774 | ae63accdd | hand | no | merge of `main`; `just golden-reach-report`, `restate-coverage.py --write` and `golden-reach-search.py outstanding` run directly |
| #774 | b4af65f52 | hand | no | merge of `main`; `just golden-reach-report` and `restate-coverage.py --write` run directly |
| #774 | c3a741e46 | hand | yes (this merge) | merge of `main`; a worker's merge, with no recipe run before it |
| #774 | e1e329509 | hand | yes | one proof row in `docs/openapi-surface-coverage.md` edited by an ad-hoc script |
| #774 | aca822f05 | recipe | yes | `just census-repin --verbose`, then `golden-reach.py arms --headline` for the headline the recipe leaves, then committed |
| #774 | edd4b2fdc | recipe | yes | `census-repin.py --verbose`, then committed; the diff is the ledger's header line |
| #774 | 93c9b2e17 | hand | yes | merge of `main`; region tables merged cell by cell with ad-hoc scripts, with the recipe left to run next |
| #774 | 87d6a2ef7 | recipe | yes | `census-repin.py --verbose` with `arms --headline` and `restate-coverage.py --write`; the recipe reported 4 files rewritten |
| #775 | a5eecfc52 | recipe | yes | `census-repin.py --verbose`, then committed; the run reported 3 derived files rewritten |
| #775 | 20e75b613 | hand | yes (this merge) | merge of `main`; conflicts in `docs/openapi-surface-coverage.md` and `document-paths.md` resolved with an ad-hoc script |
| #775 | 0751ef0e4 | hand | no | no recipe run in the session; `golden-reach.py measure`, `restate-coverage.py` and ad-hoc restating scripts |
| #776 | ffcd97399 | recipe | yes | `census-repin.py --confirm-port` for one port |
| #776 | 22a2674d4 | recipe | yes | `just census-repin --jobs 1 --verbose`, then committed |
| #776 | ef2cf0bf1 | hand | yes (this merge) | merge of `main`; region tables merged by an ad-hoc script, with the recipe left to run next |
| #776 | 5911475d2 | hand | yes | headline counts corrected with `sed -i` |
| #776 | 68d15597f | hand | yes | hand edit to `combinations.md` |
| #776 | 0fc68b7fb | recipe | no | `just census-repin --jobs 1 --verbose`, then committed (made on #774's branch, merged into #776's) |
| #776 | c87d03c09 | recipe | no | `just census-repin --jobs 1 --verbose`, then committed; two earlier runs in that session had failed or been stopped |
| #776 | ac37657b6 | hand | no | `golden-reach-search.py outstanding` run directly |
| #776 | daa26ba30 | hand | no | `golden-reach-search.py outstanding` run directly (made on #774's branch) |
| #776 | 137b06c05 | hand | no | no rewriting recipe run before the commit (made on #774's branch) |
| #776 | 38105d3cb | hand | no | only `census-repin --base-only` before the commit, which rewrites no table (made on #774's branch) |
| #776 | 3f35b4e28 | hand | no | `restate-coverage.py` run directly before the commit |
| #776 | 1440957fa | hand | no | one authored fixture's `evidence.toml` staged with the fixture work, while a recipe run was still in progress in that session |
| #776 | 1b5c45105 | hand | no | `restate-coverage.py` run directly before the commit |
| #776 | 26a0eda68 | hand | no | merge of the shared proof runner; its message leaves the reach views to be regenerated afterwards |
| #776 | e5d1b7b58 | hand | no | prose edit to `schemas.md` |
| #776 | b0a0c101f | hand | no | `golden-reach.py arms --headline` and an ad-hoc ranking script; the uncommitted result was preserved by the run's closeout |
| #780 | 5d3555391 | hand | no | `just surface-census --json` and `restate-coverage.py --write` run directly |
| #780 | fbb5ed84e | hand | no | `golden-reach.py measure --golden-only`, `just golden-reach-report` and `restate-coverage.py --write` run directly |
| #780 | 5941e0d5e | hand | no | `golden-reach.py arms --headline`, `restate-coverage.py --write` and ad-hoc scripts |
| #780 | 443c20924 | hand | no | one row of `document-paths.md` edited, with no recipe run before the commit |
| #780 | e1cd561a9 | hand | no | counts in `docs/openapi-surface-coverage.md` edited, with no recipe run before the commit |
| #780 | 08b9ee650 | hand | no | merge of `main`; `just census-repin --jobs 1` exited 1 on the conflicts, which an ad-hoc script then resolved |
| #780 | ad1dd962a | hand | no | merge of `main`; `census-repin` refused the hunks mixing generated counts with authored text, and the worker resolved them |
| #780 | 3b99efebc | hand | yes (this merge) | merge of `main`; an ad-hoc script and `sed -i`, with the recipe left to run next |
| #780 | 16bfb2829 | recipe | yes | `census-repin.py --verbose`, then committed |
| #780 | 4f0eec9d3 | hand | yes | the census script's source counts corrected with `sed -i` |
| #780 | 4b874afb3 | hand | yes | one fixture's `evidence.toml` covers retired by an ad-hoc script, before the recipe ran |
| #780 | 2a18a0d64 | recipe | yes | `census-repin.py --verbose` after re-measuring the residual attribution, then committed |
| #780 | 774c4ccd1 | hand | yes | `golden-reach.py arms --headline`, `restate-coverage.py --write` and `sed -i` |

## What limits this comparison

- **It clears the 5-change line only by counting whole histories.** `compare` labels it measured because 5 changes qualify, but only #778 started on the tooling. #774, #775, #776 and #780 qualified by merging `main` at 8cbca1f51 or later, on 2026-11-06 at about 00:33, 00:33, 00:35 and 04:24 UTC, and most of their commits predate that merge. The harness counts a qualifying change's whole history, as it did for the baseline.
- **#778 is this change.** It qualifies by the window's rule, so it stays in the sample. Its head at the cutoff is bde080c51, and its one CI failure, run 42189641460, came from adding this project: `tools/repin-cost` missing from `test-certified-pair`'s inputs, and a new workspace member moving the residual attribution's fingerprint.
- **0.60 census failures per change is not a reduction on the pooled 0.58.** It is 3 failures on 5 changes: the sample sits 0.02 above the pooled rate and 1.26 below the live run's 1.86. Their composition is what differs. The one failure naming repin kinds, #774's run 41987921718 (`measured-count`, `port-digest`, `site-anchor`), tested b4af65f52, before that branch's base carried both commits. The two that ran with both commits are `census-unattributed` (#774's 42229072863 and #776's 42158486485): on Windows, `surface-census:test-census` fails `test_committed_operation_search_has_rep…`, an assertion over reproducible compressed bytes. So no CI failure naming `site-anchor`, `port-digest`, `measured-count` or `outstanding.tsv` is on a head whose base carried both, in this small sample.
- **Minutes are lower bounds where runs are unresolved.** Two census failures have no next CI run by the cutoff, so their cycle minutes hold elapsed time only, and the one census-failed publication is unresolved.
- **All 3 derived-table conflicts predate qualifying.** They are journal `sync-conflict` records from 2026-11-05 (#774 at 03:39 and 06:55, #780 at 05:06 UTC), before either branch merged 8cbca1f51. The harness counts them under its whole-history rule. The table also undercounts what workers met: workers who merged `main` themselves resolved census conflicts (20e75b613, ef2cf0bf1, 93c9b2e17, 3b99efebc) that the journals do not record as sync conflicts.
- **The method's census tier no longer covers every pin that fails a change.** It is exactly `surface-census:test-census`, `test-reach` and `test-reach-portable`, kept so this sample compares with the baseline. `surface-reach:test-ports`, which 8cbca1f51 created to hold the port-pin tests, is outside it. `reach_document_recipe_test.py` failed in that target on #776, #778 and #780's last runs. On #778 the failure is `stale residual attribution`, a pin that a `pyproject.toml` change moved; the other two logs were not read for their reason. None of the three counts as a census-tier failure here. A later re-take should read that target's failures before relying on the `port-digest` row.
- **The recipe does not finish the repin.** On #774 and #780 workers ran `arms --headline` and `restate-coverage.py` or used `sed` after `just census-repin`, because the recipe leaves the arm headline stale; both filed that as a follow-up. That is why hand repins continue after the base carries both commits.
- **CI answers are frozen at their first read.** #776's and #775's run lists were first read soon after 05:14 UTC and answered from the cache here. A fresh read through the guard at this dispatch showed the same runs, with none newer before the cutoff. Runs after the cutoff are not in this sample.

## Baseline and quota

`baseline/` is the spike's committed measurement, kept as it was. Re-running its window (`runs:Close-crozier-s-remaining-Fern-parity-gaps,Close-crozier-s-remaining-Fern-departures-and-unproven-features-and-combinations`, until 2026-11-02T12:30:01Z) in this dispatch answered from the shared response cache with 0 uncached calls. Its `events.tsv` and `summary.md` came out identical, and every figure `compare` reads matched. Two text columns moved: `nodes`, because node outcomes have changed since and the harness now labels a retired node instead of writing `?`, and `rewrote` on #723, #724, #726 and #727, because that column reads each pull request's head as it is now.

This sample's cutoff is the journal's dispatch time for this node's dispatch, `repin-cost-remeasure-r2`. An earlier dispatch of the node committed a re-take at its own start, 2026-11-06T05:14:09Z, holding #775 and #776 alone; this one replaces it.

GitHub quota this dispatch consumed: 21 `core` REST calls through the rate-limit guard, all answered 200, with no refusal and no wait. 19 are the after-sample pass, whose 9 further answers came from the cache, and 2 are the fresh run-list reads above, sent with a scratch cache so the shared one kept its entries. The `core` bucket stood at 4,475 of 5,000 remaining before the pass and 4,416 after; the other 40 units in that interval were spent by other holders of the shared token. One read went outside the guard: a single `gh pr list` GraphQL query for the five pull requests' states, whose answer no figure here uses. Later log reads were cache hits, and `gh api rate_limit` reads cost nothing.

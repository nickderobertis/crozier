# Repin cost after the incremental census tooling

Provisional comparison: 2 after-sample changes; 26 baseline changes.
Cycle intervals include other work and queueing; they do not establish causation.

After-sample PRs: #775, #776.
Landing commits: 27ff7dc6455505147f59fd3b0b3aa2d06141091d, 8cbca1f51b1a6a5702cb8e9ddc9db06f21d45a73.
Cutoff: 2026-11-06T05:14:09.186000+00:00.

```sh
python3 tools/repin-cost/repin_cost.py --window base-carries:27ff7dc6455505147f59fd3b0b3aa2d06141091d,8cbca1f51b1a6a5702cb8e9ddc9db06f21d45a73 --runs-root "$ONEPIPELINE_RUNS_DIR" --until 2026-11-06T05:14:09.186000+00:00 --out tools/repin-cost/after
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
| `attempts` | 47.00 | 1.81 | 2.00 | 1.00 | -45.00 | -0.81 |
| `census.attempts` | 6.00 | 0.23 | 1.00 | 0.50 | -5.00 | +0.27 |
| `census.changes_hit` | 9.00 | 0.35 | 1.00 | 0.50 | -8.00 | +0.15 |
| `census.ci_retry_unresolved` | 3.00 | 0.12 | 1.00 | 0.50 | -2.00 | +0.38 |
| `census.cycle_min` | 3998.60 | 153.79 | 87.00 | 43.50 | -3911.60 | -110.29 |
| `census.elapsed_min` | 1403.40 | 53.98 | 87.00 | 43.50 | -1316.40 | -10.48 |
| `census.failures` | 15.00 | 0.58 | 1.00 | 0.50 | -14.00 | -0.08 |
| `census.median_cycle_min` | 230.90 | 8.88 | 87.00 | 43.50 | -143.90 | +34.62 |
| `census.median_pub_wait_min` | 80.40 | 3.09 | 0.00 | 0.00 | -80.40 | -3.09 |
| `census.pub_observed` | 3.00 | 0.12 | 0.00 | 0.00 | -3.00 | -0.12 |
| `census.pub_unresolved` | 3.00 | 0.12 | 1.00 | 0.50 | -2.00 | +0.38 |
| `census.pub_wait_min` | 286.70 | 11.03 | 0.00 | 0.00 | -286.70 | -11.03 |
| `census.publications` | 6.00 | 0.23 | 1.00 | 0.50 | -5.00 | +0.27 |
| `census.redispatches` | 9.00 | 0.35 | 1.00 | 0.50 | -8.00 | +0.15 |
| `census.runner_min` | 3453.60 | 132.83 | 205.50 | 102.75 | -3248.10 | -30.08 |
| `census.wait_min` | 2595.20 | 99.82 | 0.00 | 0.00 | -2595.20 | -99.82 |
| `census_and_conflict_redispatches` | 17.00 | 0.65 | 1.00 | 0.50 | -16.00 | -0.15 |
| `changes` | 26.00 | 1.00 | 2.00 | 1.00 | -24.00 | +0.00 |
| `changes_with_pr` | 26.00 | 1.00 | 2.00 | 1.00 | -24.00 | +0.00 |
| `ci_failed` | 28.00 | 1.08 | 2.00 | 1.00 | -26.00 | -0.08 |
| `ci_runs` | 67.00 | 2.58 | 3.00 | 1.50 | -64.00 | -1.08 |
| `conflicts.changes_hit` | 6.00 | 0.23 | 0.00 | 0.00 | -6.00 | -0.23 |
| `conflicts.code` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `conflicts.derived` | 9.00 | 0.35 | 0.00 | 0.00 | -9.00 | -0.35 |
| `conflicts.median_wait_min` | 423.80 | 16.30 | 0.00 | 0.00 | -423.80 | -16.30 |
| `conflicts.mixed` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `conflicts.redispatches` | 8.00 | 0.31 | 0.00 | 0.00 | -8.00 | -0.31 |
| `conflicts.wait_min` | 3839.90 | 147.69 | 0.00 | 0.00 | -3839.90 | -147.69 |
| `kind.census-unattributed.attempts` | 0.00 | 0.00 | 1.00 | 0.50 | +1.00 | +0.50 |
| `kind.census-unattributed.changes` | 0.00 | 0.00 | 1.00 | 0.50 | +1.00 | +0.50 |
| `kind.census-unattributed.cycle_min` | 0.00 | 0.00 | 87.00 | 43.50 | +87.00 | +43.50 |
| `kind.census-unattributed.elapsed_min` | 0.00 | 0.00 | 87.00 | 43.50 | +87.00 | +43.50 |
| `kind.census-unattributed.events` | 0.00 | 0.00 | 1.00 | 0.50 | +1.00 | +0.50 |
| `kind.census-unattributed.pub_observed` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.census-unattributed.pub_unresolved` | 0.00 | 0.00 | 1.00 | 0.50 | +1.00 | +0.50 |
| `kind.census-unattributed.pub_wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.census-unattributed.redispatches` | 0.00 | 0.00 | 1.00 | 0.50 | +1.00 | +0.50 |
| `kind.census-unattributed.runner_min` | 0.00 | 0.00 | 205.50 | 102.75 | +205.50 | +102.75 |
| `kind.census-unattributed.wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.attempts` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.changes` | 6.00 | 0.23 | 0.00 | 0.00 | -6.00 | -0.23 |
| `kind.derived-conflict.cycle_min` | 3839.90 | 147.69 | 0.00 | 0.00 | -3839.90 | -147.69 |
| `kind.derived-conflict.elapsed_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.events` | 9.00 | 0.35 | 0.00 | 0.00 | -9.00 | -0.35 |
| `kind.derived-conflict.pub_observed` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.pub_unresolved` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.pub_wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.redispatches` | 8.00 | 0.31 | 0.00 | 0.00 | -8.00 | -0.31 |
| `kind.derived-conflict.runner_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.derived-conflict.wait_min` | 3839.90 | 147.69 | 0.00 | 0.00 | -3839.90 | -147.69 |
| `kind.measured-count.attempts` | 2.00 | 0.08 | 0.00 | 0.00 | -2.00 | -0.08 |
| `kind.measured-count.changes` | 3.00 | 0.12 | 0.00 | 0.00 | -3.00 | -0.12 |
| `kind.measured-count.cycle_min` | 617.30 | 23.74 | 0.00 | 0.00 | -617.30 | -23.74 |
| `kind.measured-count.elapsed_min` | 294.80 | 11.34 | 0.00 | 0.00 | -294.80 | -11.34 |
| `kind.measured-count.events` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `kind.measured-count.pub_observed` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.measured-count.pub_unresolved` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.measured-count.pub_wait_min` | 10.30 | 0.40 | 0.00 | 0.00 | -10.30 | -0.40 |
| `kind.measured-count.redispatches` | 3.00 | 0.12 | 0.00 | 0.00 | -3.00 | -0.12 |
| `kind.measured-count.runner_min` | 776.20 | 29.85 | 0.00 | 0.00 | -776.20 | -29.85 |
| `kind.measured-count.wait_min` | 322.50 | 12.40 | 0.00 | 0.00 | -322.50 | -12.40 |
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
| `kind.port-digest.attempts` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `kind.port-digest.changes` | 6.00 | 0.23 | 0.00 | 0.00 | -6.00 | -0.23 |
| `kind.port-digest.cycle_min` | 1666.50 | 64.10 | 0.00 | 0.00 | -1666.50 | -64.10 |
| `kind.port-digest.elapsed_min` | 532.10 | 20.47 | 0.00 | 0.00 | -532.10 | -20.47 |
| `kind.port-digest.events` | 9.00 | 0.35 | 0.00 | 0.00 | -9.00 | -0.35 |
| `kind.port-digest.pub_observed` | 2.00 | 0.08 | 0.00 | 0.00 | -2.00 | -0.08 |
| `kind.port-digest.pub_unresolved` | 2.00 | 0.08 | 0.00 | 0.00 | -2.00 | -0.08 |
| `kind.port-digest.pub_wait_min` | 276.40 | 10.63 | 0.00 | 0.00 | -276.40 | -10.63 |
| `kind.port-digest.redispatches` | 7.00 | 0.27 | 0.00 | 0.00 | -7.00 | -0.27 |
| `kind.port-digest.runner_min` | 1287.90 | 49.53 | 0.00 | 0.00 | -1287.90 | -49.53 |
| `kind.port-digest.wait_min` | 1134.40 | 43.63 | 0.00 | 0.00 | -1134.40 | -43.63 |
| `kind.site-anchor.attempts` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.site-anchor.changes` | 6.00 | 0.23 | 0.00 | 0.00 | -6.00 | -0.23 |
| `kind.site-anchor.cycle_min` | 1714.90 | 65.96 | 0.00 | 0.00 | -1714.90 | -65.96 |
| `kind.site-anchor.elapsed_min` | 576.70 | 22.18 | 0.00 | 0.00 | -576.70 | -22.18 |
| `kind.site-anchor.events` | 9.00 | 0.35 | 0.00 | 0.00 | -9.00 | -0.35 |
| `kind.site-anchor.pub_observed` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.site-anchor.pub_unresolved` | 1.00 | 0.04 | 0.00 | 0.00 | -1.00 | -0.04 |
| `kind.site-anchor.pub_wait_min` | 0.00 | 0.00 | 0.00 | 0.00 | +0.00 | +0.00 |
| `kind.site-anchor.redispatches` | 4.00 | 0.15 | 0.00 | 0.00 | -4.00 | -0.15 |
| `kind.site-anchor.runner_min` | 1389.30 | 53.43 | 0.00 | 0.00 | -1389.30 | -53.43 |
| `kind.site-anchor.wait_min` | 1138.20 | 43.78 | 0.00 | 0.00 | -1138.20 | -43.78 |
| `merged` | 20.00 | 0.77 | 1.00 | 0.50 | -19.00 | -0.27 |
| `other_failures` | 13.00 | 0.50 | 1.00 | 0.50 | -12.00 | +0.00 |
| `redispatches` | 78.00 | 3.00 | 4.00 | 2.00 | -74.00 | -1.00 |

| census failures / change reference | reference | after | difference |
| --- | ---: | ---: | ---: |
| pooled baseline | 0.58 | 0.50 | -0.08 |
| live run baseline | 1.86 | 0.50 | -1.36 |

After measurement GitHub quota: 9 uncached core REST calls; 0 cache hits.
The dispatch-wide quota and baseline-cache verification are recorded in the hand-counted evidence below.

## Hand count: census repins by the recipe and by hand

Read from each change's commits and from the worker transcripts of the runs that made them. A repin here is a commit on the change whose diff rewrites a table the harness's `artifact_kind` calls `site-anchor`, `port-digest` or `measured-count`, or the `golden-reach-witnesses/outstanding.tsv` list `just census-repin` regenerates. "Recipe" means the commit carries the output of `just census-repin` or of `tools/surface-census/census-repin.py`, the script the recipe runs. "Hand" means anything else: a generator run directly, an ad-hoc script, `sed`, a prose edit, or a merge resolved by the worker. Commits that touch only other artifacts, such as `residual-attribution.json` (5b6a3d957, fc8f0529c), are outside this count. The attribution is inferred from transcript order: where a session ran several generators, the row names the one before the commit that its diff reflects.

**Totals: 20 repins, 5 with the recipe and 15 by hand.** Only 7 of the 20 were made once the branch's base carried both landing commits, from the merge of `main` onward: 3 with the recipe and 4 by hand.

| PR | commit | how | base carried both? | evidence |
| --- | --- | --- | --- | --- |
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

## What limits this comparison

- **Provisional, on 2 changes.** Neither change started on the tooling. Both branches qualified only by merging `main` at 8cbca1f51 late in their work (2026-11-06, about 00:33 and 00:35 UTC), and most of their commits predate that merge. The harness counts a qualifying change's whole history, as it did for the baseline, so #775's non-census `live-e2e` failure on 0751ef0e4 is in its CI counts.
- **The one census-tier failure is not a stale table.** #776's run 42158486485 fails, on its Windows leg, a census-suite assertion about reproducible compressed bytes. The harness names it `census-unattributed` because its text matches no repin kind and no later head exists to attribute a fix from. The failed run's other legs failed outside the census tier. Neither change failed CI on `site-anchor`, `port-digest`, `measured-count` or `outstanding.tsv`.
- **0.50 census failures per change is not yet a reduction.** It is one failure on 2 changes, against the pooled 0.58 and the live run's 1.86. Its next CI run and next publication are unresolved at the cutoff, so the 87.0 cycle minutes hold elapsed time only.
- **0 derived-table conflicts undercounts what the workers met.** The harness counts the journals' `sync-conflict` records, and neither change has one. Both workers merged `main` themselves and resolved conflicts in census tables (20e75b613, ef2cf0bf1), which the journals do not record as sync conflicts.
- **CI answers are frozen at this dispatch's first read.** #776 was still open at the cutoff, and later runs are not in this sample.

## Baseline and quota

`baseline/` is the spike's committed measurement, kept as it was. Re-running its window (`runs:Close-crozier-s-remaining-Fern-parity-gaps,Close-crozier-s-remaining-Fern-departures-and-unproven-features-and-combinations`, until 2026-11-02T12:30:01Z) in this dispatch answered from the shared response cache with 0 uncached calls and 173 hits. Its `events.tsv` and `summary.md` came out identical, and every figure `compare` reads matched. Two text columns moved: `nodes`, because node outcomes have changed since and the harness now labels a retired node instead of writing `?`, and `rewrote` on #723, #724, #726 and #727, because that column reads each pull request's head as it is now.

GitHub quota this dispatch consumed: 9 `core` REST calls, all answered 200, all from the single after-sample pass through the rate-limit guard, which recorded no refusal and no wait. The baseline re-run and the later reads of the two failed runs' logs were cache hits, and `gh api rate_limit` reads cost nothing. The `core` bucket stood at 4,971 of 5,000 remaining before the pass and 4,843 after; the other 119 units in that interval were spent by other holders of the shared token.

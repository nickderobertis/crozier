# Repin cost after the incremental census tooling

Provisional comparison: 0 after-sample changes; 26 baseline changes.
No reduction can be inferred from an empty sample.

After-sample PRs: none.
Landing commits: 27ff7dc6455505147f59fd3b0b3aa2d06141091d, 8cbca1f51b1a6a5702cb8e9ddc9db06f21d45a73.
Cutoff: 2026-11-05T10:19:09.011000+00:00.

```sh
python3 tools/repin-cost/repin_cost.py --window base-carries:27ff7dc6455505147f59fd3b0b3aa2d06141091d,8cbca1f51b1a6a5702cb8e9ddc9db06f21d45a73 --runs-root "$ONEPIPELINE_RUNS_DIR" --until 2026-11-05T10:19:09.011000+00:00 --out tools/repin-cost/after
python3 tools/repin-cost/repin_cost.py compare tools/repin-cost/baseline tools/repin-cost/after
```

Differences are after minus baseline. Per-change denominators are all eligible changes, including those with no repin.
An empty sample has undefined per-change rates (n/a). Unresolved intervals remain excluded from minute sums and medians.
Kind counts overlap when a failure names several kinds; its minutes are split evenly, as in the baseline.
Medians and changes-hit counts are also shown per eligible change for completeness; median totals retain their original meaning.

| figure | baseline total | baseline / change | after total | after / change | difference total | difference / change |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `artifact.docs/fern-measurements/cases.tsv.changes` | 2.00 | 0.08 | 0.00 | n/a | -2.00 | n/a |
| `artifact.docs/fern-measurements/cases.tsv.ci_failures` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.docs/fern-measurements/cases.tsv.conflicts` | 2.00 | 0.08 | 0.00 | n/a | -2.00 | n/a |
| `artifact.docs/fern-measurements/cases.tsv.cycle_min` | 35.90 | 1.38 | 0.00 | n/a | -35.90 | n/a |
| `artifact.docs/fern-measurements/cases.tsv.runner_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.docs/fern-refusals/classes.tsv.changes` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.docs/fern-refusals/classes.tsv.ci_failures` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.docs/fern-refusals/classes.tsv.conflicts` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.docs/fern-refusals/classes.tsv.cycle_min` | 39.80 | 1.53 | 0.00 | n/a | -39.80 | n/a |
| `artifact.docs/fern-refusals/classes.tsv.runner_min` | 68.00 | 2.62 | 0.00 | n/a | -68.00 | n/a |
| `artifact.docs/fern-refusals/documents.tsv.changes` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.docs/fern-refusals/documents.tsv.ci_failures` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.docs/fern-refusals/documents.tsv.conflicts` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.docs/fern-refusals/documents.tsv.cycle_min` | 39.80 | 1.53 | 0.00 | n/a | -39.80 | n/a |
| `artifact.docs/fern-refusals/documents.tsv.runner_min` | 68.00 | 2.62 | 0.00 | n/a | -68.00 | n/a |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.changes` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.ci_failures` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.conflicts` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.cycle_min` | 35.90 | 1.38 | 0.00 | n/a | -35.90 | n/a |
| `artifact.docs/openapi-surface/scenario-proof-index.tsv.runner_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.changes` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.ci_failures` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.conflicts` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.cycle_min` | 646.70 | 24.87 | 0.00 | n/a | -646.70 | n/a |
| `artifact.docs/openapi-surface/witness-search-registries/outstanding.tsv.runner_min` | 788.60 | 30.33 | 0.00 | n/a | -788.60 | n/a |
| `artifact.tests/fixtures/CORPUS.md.changes` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.tests/fixtures/CORPUS.md.ci_failures` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.tests/fixtures/CORPUS.md.conflicts` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.tests/fixtures/CORPUS.md.cycle_min` | 39.90 | 1.53 | 0.00 | n/a | -39.90 | n/a |
| `artifact.tests/fixtures/CORPUS.md.runner_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.tests/fixtures/compared-goldens.json.changes` | 5.00 | 0.19 | 0.00 | n/a | -5.00 | n/a |
| `artifact.tests/fixtures/compared-goldens.json.ci_failures` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.tests/fixtures/compared-goldens.json.conflicts` | 5.00 | 0.19 | 0.00 | n/a | -5.00 | n/a |
| `artifact.tests/fixtures/compared-goldens.json.cycle_min` | 127.00 | 4.88 | 0.00 | n/a | -127.00 | n/a |
| `artifact.tests/fixtures/compared-goldens.json.runner_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.tests/fixtures/corpus-sources.tsv.changes` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.tests/fixtures/corpus-sources.tsv.ci_failures` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.tests/fixtures/corpus-sources.tsv.conflicts` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `artifact.tests/fixtures/corpus-sources.tsv.cycle_min` | 39.90 | 1.53 | 0.00 | n/a | -39.90 | n/a |
| `artifact.tests/fixtures/corpus-sources.tsv.runner_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.tests/fixtures/departures-ledger.tsv.changes` | 5.00 | 0.19 | 0.00 | n/a | -5.00 | n/a |
| `artifact.tests/fixtures/departures-ledger.tsv.ci_failures` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `artifact.tests/fixtures/departures-ledger.tsv.conflicts` | 5.00 | 0.19 | 0.00 | n/a | -5.00 | n/a |
| `artifact.tests/fixtures/departures-ledger.tsv.cycle_min` | 127.00 | 4.88 | 0.00 | n/a | -127.00 | n/a |
| `artifact.tests/fixtures/departures-ledger.tsv.runner_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `attempts` | 47.00 | 1.81 | 0.00 | n/a | -47.00 | n/a |
| `census.attempts` | 6.00 | 0.23 | 0.00 | n/a | -6.00 | n/a |
| `census.changes_hit` | 9.00 | 0.35 | 0.00 | n/a | -9.00 | n/a |
| `census.ci_retry_unresolved` | 3.00 | 0.12 | 0.00 | n/a | -3.00 | n/a |
| `census.cycle_min` | 3998.60 | 153.79 | 0.00 | n/a | -3998.60 | n/a |
| `census.elapsed_min` | 1403.40 | 53.98 | 0.00 | n/a | -1403.40 | n/a |
| `census.failures` | 15.00 | 0.58 | 0.00 | n/a | -15.00 | n/a |
| `census.median_cycle_min` | 230.90 | 8.88 | 0.00 | n/a | -230.90 | n/a |
| `census.median_pub_wait_min` | 80.40 | 3.09 | 0.00 | n/a | -80.40 | n/a |
| `census.pub_observed` | 3.00 | 0.12 | 0.00 | n/a | -3.00 | n/a |
| `census.pub_unresolved` | 3.00 | 0.12 | 0.00 | n/a | -3.00 | n/a |
| `census.pub_wait_min` | 286.70 | 11.03 | 0.00 | n/a | -286.70 | n/a |
| `census.publications` | 6.00 | 0.23 | 0.00 | n/a | -6.00 | n/a |
| `census.redispatches` | 9.00 | 0.35 | 0.00 | n/a | -9.00 | n/a |
| `census.runner_min` | 3453.60 | 132.83 | 0.00 | n/a | -3453.60 | n/a |
| `census.wait_min` | 2595.20 | 99.82 | 0.00 | n/a | -2595.20 | n/a |
| `census_and_conflict_redispatches` | 17.00 | 0.65 | 0.00 | n/a | -17.00 | n/a |
| `changes` | 26.00 | 1.00 | 0.00 | n/a | -26.00 | n/a |
| `changes_with_pr` | 26.00 | 1.00 | 0.00 | n/a | -26.00 | n/a |
| `ci_failed` | 28.00 | 1.08 | 0.00 | n/a | -28.00 | n/a |
| `ci_runs` | 67.00 | 2.58 | 0.00 | n/a | -67.00 | n/a |
| `conflicts.changes_hit` | 6.00 | 0.23 | 0.00 | n/a | -6.00 | n/a |
| `conflicts.code` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `conflicts.derived` | 9.00 | 0.35 | 0.00 | n/a | -9.00 | n/a |
| `conflicts.median_wait_min` | 423.80 | 16.30 | 0.00 | n/a | -423.80 | n/a |
| `conflicts.mixed` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `conflicts.redispatches` | 8.00 | 0.31 | 0.00 | n/a | -8.00 | n/a |
| `conflicts.wait_min` | 3839.90 | 147.69 | 0.00 | n/a | -3839.90 | n/a |
| `kind.derived-conflict.attempts` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.derived-conflict.changes` | 6.00 | 0.23 | 0.00 | n/a | -6.00 | n/a |
| `kind.derived-conflict.cycle_min` | 3839.90 | 147.69 | 0.00 | n/a | -3839.90 | n/a |
| `kind.derived-conflict.elapsed_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.derived-conflict.events` | 9.00 | 0.35 | 0.00 | n/a | -9.00 | n/a |
| `kind.derived-conflict.pub_observed` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.derived-conflict.pub_unresolved` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.derived-conflict.pub_wait_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.derived-conflict.redispatches` | 8.00 | 0.31 | 0.00 | n/a | -8.00 | n/a |
| `kind.derived-conflict.runner_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.derived-conflict.wait_min` | 3839.90 | 147.69 | 0.00 | n/a | -3839.90 | n/a |
| `kind.measured-count.attempts` | 2.00 | 0.08 | 0.00 | n/a | -2.00 | n/a |
| `kind.measured-count.changes` | 3.00 | 0.12 | 0.00 | n/a | -3.00 | n/a |
| `kind.measured-count.cycle_min` | 617.30 | 23.74 | 0.00 | n/a | -617.30 | n/a |
| `kind.measured-count.elapsed_min` | 294.80 | 11.34 | 0.00 | n/a | -294.80 | n/a |
| `kind.measured-count.events` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `kind.measured-count.pub_observed` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.measured-count.pub_unresolved` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.measured-count.pub_wait_min` | 10.30 | 0.40 | 0.00 | n/a | -10.30 | n/a |
| `kind.measured-count.redispatches` | 3.00 | 0.12 | 0.00 | n/a | -3.00 | n/a |
| `kind.measured-count.runner_min` | 776.20 | 29.85 | 0.00 | n/a | -776.20 | n/a |
| `kind.measured-count.wait_min` | 322.50 | 12.40 | 0.00 | n/a | -322.50 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.attempts` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.changes` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.cycle_min` | 39.80 | 1.53 | 0.00 | n/a | -39.80 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.elapsed_min` | 30.20 | 1.16 | 0.00 | n/a | -30.20 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.events` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.pub_observed` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.pub_unresolved` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.pub_wait_min` | 9.20 | 0.35 | 0.00 | n/a | -9.20 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.redispatches` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.runner_min` | 68.00 | 2.62 | 0.00 | n/a | -68.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/classes.tsv.wait_min` | 9.60 | 0.37 | 0.00 | n/a | -9.60 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.attempts` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.changes` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.cycle_min` | 39.80 | 1.53 | 0.00 | n/a | -39.80 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.elapsed_min` | 30.20 | 1.16 | 0.00 | n/a | -30.20 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.events` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.pub_observed` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.pub_unresolved` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.pub_wait_min` | 9.20 | 0.35 | 0.00 | n/a | -9.20 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.redispatches` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.runner_min` | 68.00 | 2.62 | 0.00 | n/a | -68.00 | n/a |
| `kind.other-artifact:docs/fern-refusals/documents.tsv.wait_min` | 9.60 | 0.37 | 0.00 | n/a | -9.60 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.attempts` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.changes` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.cycle_min` | 646.70 | 24.87 | 0.00 | n/a | -646.70 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.elapsed_min` | 300.20 | 11.55 | 0.00 | n/a | -300.20 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.events` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.pub_observed` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.pub_unresolved` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.pub_wait_min` | 344.10 | 13.23 | 0.00 | n/a | -344.10 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.redispatches` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.runner_min` | 788.60 | 30.33 | 0.00 | n/a | -788.60 | n/a |
| `kind.other-artifact:docs/openapi-surface/witness-search-registries/outstanding.tsv.wait_min` | 346.50 | 13.33 | 0.00 | n/a | -346.50 | n/a |
| `kind.port-digest.attempts` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `kind.port-digest.changes` | 6.00 | 0.23 | 0.00 | n/a | -6.00 | n/a |
| `kind.port-digest.cycle_min` | 1666.50 | 64.10 | 0.00 | n/a | -1666.50 | n/a |
| `kind.port-digest.elapsed_min` | 532.10 | 20.47 | 0.00 | n/a | -532.10 | n/a |
| `kind.port-digest.events` | 9.00 | 0.35 | 0.00 | n/a | -9.00 | n/a |
| `kind.port-digest.pub_observed` | 2.00 | 0.08 | 0.00 | n/a | -2.00 | n/a |
| `kind.port-digest.pub_unresolved` | 2.00 | 0.08 | 0.00 | n/a | -2.00 | n/a |
| `kind.port-digest.pub_wait_min` | 276.40 | 10.63 | 0.00 | n/a | -276.40 | n/a |
| `kind.port-digest.redispatches` | 7.00 | 0.27 | 0.00 | n/a | -7.00 | n/a |
| `kind.port-digest.runner_min` | 1287.90 | 49.53 | 0.00 | n/a | -1287.90 | n/a |
| `kind.port-digest.wait_min` | 1134.40 | 43.63 | 0.00 | n/a | -1134.40 | n/a |
| `kind.site-anchor.attempts` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.site-anchor.changes` | 6.00 | 0.23 | 0.00 | n/a | -6.00 | n/a |
| `kind.site-anchor.cycle_min` | 1714.90 | 65.96 | 0.00 | n/a | -1714.90 | n/a |
| `kind.site-anchor.elapsed_min` | 576.70 | 22.18 | 0.00 | n/a | -576.70 | n/a |
| `kind.site-anchor.events` | 9.00 | 0.35 | 0.00 | n/a | -9.00 | n/a |
| `kind.site-anchor.pub_observed` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.site-anchor.pub_unresolved` | 1.00 | 0.04 | 0.00 | n/a | -1.00 | n/a |
| `kind.site-anchor.pub_wait_min` | 0.00 | 0.00 | 0.00 | n/a | +0.00 | n/a |
| `kind.site-anchor.redispatches` | 4.00 | 0.15 | 0.00 | n/a | -4.00 | n/a |
| `kind.site-anchor.runner_min` | 1389.30 | 53.43 | 0.00 | n/a | -1389.30 | n/a |
| `kind.site-anchor.wait_min` | 1138.20 | 43.78 | 0.00 | n/a | -1138.20 | n/a |
| `merged` | 20.00 | 0.77 | 0.00 | n/a | -20.00 | n/a |
| `other_failures` | 13.00 | 0.50 | 0.00 | n/a | -13.00 | n/a |
| `redispatches` | 78.00 | 3.00 | 0.00 | n/a | -78.00 | n/a |

| census failures / change reference | reference | after | difference |
| --- | ---: | ---: | ---: |
| pooled baseline | 0.58 | n/a | n/a |
| live run baseline | 1.86 | n/a | n/a |

After measurement GitHub quota: 0 uncached core REST calls; 0 cache hits.
The dispatch-wide quota and baseline-cache verification are recorded in the hand-counted evidence below.

## Hand-counted recipe use and evidence

The after sample is empty: **0 repins with `just census-repin`, 0 by hand**.
There is no eligible repin PR or commit to name or transcript to classify. The
implementation PRs #762 (`27ff7dc6455505147f59fd3b0b3aa2d06141091d`) and #767
(`8cbca1f51b1a6a5702cb8e9ddc9db06f21d45a73`) are excluded because their bases do
not carry both landings. Counting their implementation-time repins would change
the window. Both landing SHAs were read from this run's settlements and
`change-merged` journal records after reading `onepipeline results
Stop-crozier-workers-re-pinning-measurement-tables-as-main-moves --json` from the
orchestrator checkout.

The cutoff is the dispatch's `node-dispatched` event,
2026-11-05T10:19:09.011Z, less than three minutes after the second landing.
The harness examined 230 branches: 124 PR changes whose bases lack a required
commit, and 106 branches without a PR. Every one is in `excluded.tsv`; no PR is
in `changes.tsv`. Undefined per-change rates must not be interpreted as zero
cost or an improvement over either 0.58 pooled or 1.86 live-run failures/change.

The baseline's five files were preserved byte for byte from the spike branch.
A replay to dispatch scratch, with a temporary cache-miss barrier preventing
REST access, reproduced 26 changes, 15 census-tier failures and 9 derived-table
conflicts using 173 shared-cache hits and 0 uncached requests. Its census and
conflict totals equal the committed baseline. The committed baseline was not
rewritten. No baseline cache entry needed to be fetched again.

**Dispatch GitHub quota: 0 core REST calls** (after measurement 0; baseline
cache replay 0). The tests used only a loopback server. Git fetches read commit
objects and PR heads, without using the REST quota. No code search, instrumented
measurement or SDK generation was run.

A follow-up re-take is required once at least five changes whose bases carry
both landings exist. Use the measurement command above with the new dispatch's
cutoff, followed by `compare`, against `tools/repin-cost/baseline/`; review each
eligible change's commits and transcript to append recipe-versus-hand counts.

For retired node IDs absent from current `onepipeline results`, 154 excluded
rows explicitly say `unavailable (node retired; not in current results)` rather
than using a placeholder. These outcomes affect none of the window selection,
classification or interval calculations. The final after window was run serially
in this checkout; its exclusion reasons all have known bases where applicable.

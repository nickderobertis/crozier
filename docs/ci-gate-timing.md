# CI gate timing

## After: goal unmet

**Goal unmet.** No ordinary sampled head with accepted required verdicts on the finished four-lane configuration reached required checks in under 3600 seconds: ordinary heads took 8380 s (#794, broad tool selection), 12324 s (#796 first head, macOS queue) and 6551 s (#796 merged-main head, macOS queue). The broad-source head #800 is 11632 s and is **a lower bound with no accepted macOS verdict**: test-macos failed on a test unrelated to timing and was not re-run. Only the release path is inside the line: 860 s for a guard-compliant release candidate (#798), and 425 s for genuine release #777 before the compatibility jobs left. Under-an-hour remains open: the user's decision on runners is pending and their standing default is to accept about two hours; [the manager records it](#goal-status-and-escalation). This section is a measurement record, not a completion claim.

### Reproduce

Exactly the baseline command at an explicit observation cutoff:

```sh
node tools/ci/gate-timing.mjs runs --since 2026-11-08T07:33:26Z --until 2026-11-09T02:15:00Z --limit 200
```

Definitions are the baseline's, unchanged and imported from the same [calculation functions](../tools/ci/gate-timing/core.mjs): gate seconds run from the first workflow created_at at a head (a push proxy seconds after the push) to the last required-context completion across attempts; queue is job created-to-started; needs delay is first workflow creation to job creation. A cancelled or missing required context yields null, and failed heads are never in the passing distribution. The window opens at #791's merge, when the four-lane shape first applied, and contains every completed qualifying run at the cutoff: **64 workflow runs, 266 jobs, complete: true**. Complete output: [after.json.gz](ci-gate-timing/after.json.gz) (schema 1, every head, attempt and job timestamp); per-task lane telemetry: [after-tasks.json.gz](ci-gate-timing/after-tasks.json.gz), parsed from each lane's `gate: task` lines. The `--format markdown` output, verbatim:

Window: 2026-11-08T07:33:26Z — 2026-11-09T02:15:00Z

| Kind | Passing n | Median seconds | p95 | Max | Unsuccessful |
|---|---:|---:|---:|---:|---:|
| pr | 7 | 9247 | 16363 | 16363 | 23 |
| release-pr | 2 | 642.5 | 860 | 860 | 1 |
| main | 0 | unknown | unknown | unknown | 6 |

Required contexts observed at the cutoff from main protection and active rules: **lint, test-linux, test-macos, test-windows**. This matches the human migration's step (`.github/governance.json` required_checks, and the four job ids in ci.yml); no mismatch.

### Configurations measured

Three live-run changes reach the finished shape, in order: [#781](https://github.com/nickderobertis/crozier/pull/781) (repeated suite work removed), [#791](https://github.com/nickderobertis/crozier/pull/791) (four lanes, compatibility jobs still running) and [#794](https://github.com/nickderobertis/crozier/pull/794) (compatibility jobs retired). [#799](https://github.com/nickderobertis/crozier/pull/799) then raised test-windows and test-macos to 150-minute limits; it changes no lane's work, so it is configuration, not a speed change. Heads carry the configuration at which they ran; earlier heads are kept separate below. Main CI is deliberately no longer run: where the baseline's main kind measured a push run (median 8160.5 s, max 9901 s), the push now starts only `main caches`, release-plz, the golden-reach base and gallery jobs, so no main gate span exists to compare. The cost is intentional removal, not an improvement in the same metric.

Corrective configurations during this measurement: none. No limit, shard, job, coverage or protection changed, because no change inside the rules (no larger runners, shards, or moved, dropped or lightened tests) closes a gap of this size.

Demonstration records. Heads were throwaway PRs based on the session branch and closed after capture:

- [#797](https://github.com/nickderobertis/crozier/pull/797) heads `feda075ad`, `459cc01c6`, `eeefbf409`: **discarded, not configuration measurements.** They hand-applied 150-minute limits, and the runs failed the repository's own pins of those limits and a stale residual-attribution digest that any src change must refresh; their test-linux stopped before the live/corpus step, so their spans are lower bounds of a demonstration's own making.
- [#798](https://github.com/nickderobertis/crozier/pull/798) head `74678c4b8`: guard-compliant version/changelog candidate. It carries no limit edit: changing `ci.yml` on a release branch would fail the release guard, and its platform lanes skip anyway, so the instructed 150-minute limit could not apply and has no effect there. #799 changed only skipped lanes for this path.
- [#800](https://github.com/nickderobertis/crozier/pull/800) head `19cda960f`: broad source sample based on main with #799, so it carries the 150-minute limit from main and no hand edit.
- [#801](https://github.com/nickderobertis/crozier/pull/801): a genuine release PR built on top of this dispatch's session commit `09bc6900a` and refused by the release guard. The cause appears to be #798's branch name beginning `release-plz-`. Not a timing sample; it is reported to the manager, recorded as a follow-up, and nothing reached main.

### Finished-configuration heads

Seconds. Needs delay is before job creation, queue is job creation to runner start, execution is runner start to completion. Every workflow's jobs are listed.

#### #794 ordinary, CI configuration change (broad tool selection)

Head `76e15eb439bd3c4560dab0f9cfc4f22ead00b8b3`, run [42489795217](https://github.com/nickderobertis/crozier/actions/runs/42489795217), attempts 1, kind pr, configuration finished: cd5cebc66 tree (lanes 30/150/90/120 min). Gate **8380** s, conclusion **success**, terminal: test-linux.

| Job | Attempt | Conclusion | Needs | Queue | Execution |
|---|---:|---|---:|---:|---:|
| cleanup-preview | 1 | success | 11112 | 1 | 5 |
| lint | 1 | success | 23 | 1 | 803 |
| prune-history | 1 | skipped | 11112 | 0 | 0 |
| test-linux | 1 | success | 23 | 2 | 8355 |
| test-macos | 1 | success | 23 | 135 | 5991 |
| test-windows | 1 | success | 23 | 1 | 4790 |

6 jobs at this head. 
Largest tasks per lane (Nx task seconds, parallel so they exceed job time):

- **lint** (109 tasks, 91 cache-replayed, 26 projects): `github-workflows:lint` 3s, `census-fallback:lint` 0s, `corpus:lint-sources` 0s, `corpus:lint-remote-ref-pins` 0s, `corpus:lint-licence-rescreening` 0s, `corpus:lint-boundaries` 0s
- **test-linux** (69 tasks, 0 cache-replayed, 26 projects): `corpus-match:test-offline` 2394s, `corpus-match:test-match` 2082s, `corpus-match:test-strict` 1952s, `crozier-e2e:test` 1600s, `fern-goldens-weekly:test` 1231s, `corpus-match:test-cold-handoff` 849s
- **test-windows** (68 tasks, 0 cache-replayed, 23 projects): `crozier-e2e:test` 2760s, `surface-census:test-census` 1718s, `ci-journeys:test` 991s, `suite-cases:test` 685s, `surface-reach:test-handwritten-reach` 550s, `witness-search:test-acquisition` 505s
- **test-macos** (58 tasks, 0 cache-replayed, 24 projects): `crozier-e2e:test` 3082s, `fern-goldens-weekly:test` 1777s, `surface-census:test-census` 1045s, `ci-journeys:test` 648s, `witness-search:test-acquisition` 545s, `witness-search:test-github` 518s

#### #796 ordinary, gate-timing tooling, first head

Head `09bc6900a78cd3dd6647a5792af5bf3b30655908`, run [42509048346](https://github.com/nickderobertis/crozier/actions/runs/42509048346), attempts 1, kind pr, configuration finished: cd5cebc66 base. Gate **12324** s, conclusion **success**, terminal: test-macos.

| Job | Attempt | Conclusion | Needs | Queue | Execution |
|---|---:|---|---:|---:|---:|
| lint | 1 | success | 1 | 2 | 818 |
| test-linux | 1 | success | 1 | 2 | 505 |
| test-macos | 1 | success | 1 | 9002 | 3321 |
| test-windows | 1 | success | 1 | 2 | 1159 |

4 jobs at this head. 
Largest tasks per lane (Nx task seconds, parallel so they exceed job time):

- **lint** (16 tasks, 13 cache-replayed, 6 projects): `gate-timing:lint` 2s, `python-workspace:lint` 0s, `fern-goldens-git:lint` 0s, `fern-goldens-git:lint-boundaries` 0s, `fern-goldens-git:lint-ruff` 0s, `python-workspace:lint-boundaries` 0s
- **test-linux** (49 tasks, 33 cache-replayed, 6 projects): `ci-journeys:test` 181s, `suite-cases:test` 122s, `gate-timing:test` 89s, `ci:test` 39s, `fern-goldens-git:test-certified-pair` 18s, `screenshots:test` 9s
- **test-windows** (10 tasks, 0 cache-replayed, 5 projects): `ci-journeys:test` 567s, `suite-cases:test` 380s, `fern-goldens-git:test-certified-pair` 78s, `ci:test` 63s, `fern-goldens-git:test-lifecycle` 5s, `ci:lint-windows` 3s
- **test-macos** (49 tasks, 0 cache-replayed, 6 projects): `fern-goldens-weekly:test` 923s, `surface-census:test-census` 844s, `witness-search:test-acquisition` 542s, `witness-search:test-github` 490s, `ci-journeys:test` 376s, `surface-reach:test-handwritten-reach` 373s

#### #796 ordinary, gate-timing tooling, merged main

Head `f0b5007c194511e8936430485a95b9fafa010538`, run [42532383652](https://github.com/nickderobertis/crozier/actions/runs/42532383652), attempts 1, kind pr, configuration finished: 1a278de16 base (includes #799 limits). Gate **6551** s, conclusion **success**, terminal: test-macos.

| Job | Attempt | Conclusion | Needs | Queue | Execution |
|---|---:|---|---:|---:|---:|
| lint | 1 | success | 1 | 1 | 719 |
| test-linux | 1 | success | 1 | 2 | 2299 |
| test-macos | 1 | success | 1 | 3058 | 3492 |
| test-windows | 1 | success | 1 | 1 | 1125 |

4 jobs at this head. 
Largest tasks per lane (Nx task seconds, parallel so they exceed job time):

- **lint** (16 tasks, 13 cache-replayed, 6 projects): `gate-timing:lint` 2s, `fern-goldens-git:lint` 0s, `python-workspace:lint` 0s, `fern-goldens-git:lint-boundaries` 0s, `fern-goldens-git:lint-ruff` 0s, `python-workspace:lint-boundaries` 0s
- **test-linux** (49 tasks, 0 cache-replayed, 6 projects): `fern-goldens-weekly:test` 571s, `surface-census:test-census` 546s, `witness-search:test-acquisition` 483s, `witness-search:test-github` 378s, `surface-reach:test-handwritten-reach` 344s, `fern-refusals:test` 244s
- **test-windows** (10 tasks, 0 cache-replayed, 5 projects): `ci-journeys:test` 569s, `suite-cases:test` 376s, `fern-goldens-git:test-certified-pair` 77s, `ci:test` 63s, `fern-goldens-git:test-lifecycle` 6s, `ci:lint-windows` 3s
- **test-macos** (49 tasks, 0 cache-replayed, 6 projects): `surface-census:test-census` 1103s, `fern-goldens-weekly:test` 882s, `witness-search:test-github` 556s, `witness-search:test-acquisition` 551s, `surface-reach:test-handwritten-reach` 427s, `fern-refusals:test` 357s

#### #800 broad source (src/lib.rs doc edit + its attribution record), demonstration

Head `19cda960fc654beb513317ea9b53037a091d69ce`, run [42532483422](https://github.com/nickderobertis/crozier/actions/runs/42532483422), attempts 1, kind pr, configuration finished: 1a278de16 base (includes #799 limits). Gate **11632** s, conclusion **failure**, terminal: test-macos.

| Job | Attempt | Conclusion | Needs | Queue | Execution |
|---|---:|---|---:|---:|---:|
| lint | 1 | success | 1 | 2 | 973 |
| test-linux | 1 | success | 1 | 2 | 9190 |
| test-macos | 1 | failure | 1 | 8714 | 2917 |
| test-windows | 1 | success | 1 | 1 | 5070 |

4 jobs at this head. 
Largest tasks per lane (Nx task seconds, parallel so they exceed job time):

- **lint** (107 tasks, 84 cache-replayed, 24 projects): `crozier-e2e:lint` 36s, `crozier-tool-journeys:lint` 33s, `crozier:lint` 26s, `workspace:doc` 10s, `crozier:format` 3s, `nested-discriminator-golden:lint` 2s
- **test-linux** (70 tasks, 0 cache-replayed, 24 projects): `corpus-match:test-offline` 2575s, `corpus-match:test-match` 2447s, `corpus-match:test-strict` 2343s, `live-e2e:test` 1583s, `crozier-e2e:test` 1580s, `fern-goldens-weekly:test` 1112s
- **test-windows** (52 tasks, 0 cache-replayed, 18 projects): `crozier-e2e:test` 2758s, `surface-census:test-census` 1931s, `surface-reach:test-handwritten-reach` 629s, `suite-cases:test` 625s, `witness-search:test-acquisition` 511s, `witness-search:test-github` 484s
- **test-macos** (53 tasks, 0 cache-replayed, 16 projects): `surface-census:test-census` 885s, `fern-goldens-weekly:test` 823s, `witness-search:test-github` 538s, `witness-search:test-acquisition` 536s, `surface-reach:test-handwritten-reach` 388s, `fern-refusals:test` 333s

#### #798 guard-compliant version/changelog release candidate, demonstration

Head `74678c4b8fc280785be7ee25fc102fe50fd73d74`, run [42509110093](https://github.com/nickderobertis/crozier/actions/runs/42509110093), attempts 1, kind release-pr, configuration finished: cd5cebc66 base; lint lane unchanged by #799. Gate **860** s, conclusion **success**, terminal: lint.

| Job | Attempt | Conclusion | Needs | Queue | Execution |
|---|---:|---|---:|---:|---:|
| cleanup-preview | 1 | success | 24650 | 2 | 5 |
| lint | 1 | success | 0 | 2 | 858 |
| prune-history | 1 | skipped | 24650 | 0 | 0 |
| test-linux | 1 | skipped | 1 | 0 | unknown |
| test-macos | 1 | skipped | 1 | 0 | unknown |
| test-windows | 1 | skipped | 1 | 0 | unknown |

6 jobs at this head. 
Largest tasks per lane (Nx task seconds, parallel so they exceed job time):

- **lint** (101 tasks, 0 cache-replayed, 26 projects): `crozier-e2e:lint` 24s, `ci:lint` 21s, `crozier:lint` 18s, `ci-journeys:lint` 6s, `github-action:lint` 3s, `github-workflows:lint` 3s

#### #777 genuine release PR v0.0.160 (compatibility jobs still present)

Head `d9f9f4c157d91fad5b608cddb540c096eb3e3f3a`, run [42459459557](https://github.com/nickderobertis/crozier/actions/runs/42459459557), attempts 1, kind release-pr, configuration pre-#794: #791 four lanes plus compatibility jobs. Gate **425** s, conclusion **success**, terminal: lint.

| Job | Attempt | Conclusion | Needs | Queue | Execution |
|---|---:|---|---:|---:|---:|
| cleanup-preview | 1 | success | 705 | 2 | 6 |
| commitlint | 1 | success | 1 | 2 | 5 |
| gate | 1 | success | 425 | 2 | 31 |
| lint | 1 | success | 1 | 1 | 423 |
| llmlint | 1 | success | 1 | 2 | 330 |
| prune-history | 1 | skipped | 705 | 0 | 0 |
| test-linux | 1 | skipped | 1 | 0 | 0 |
| test-macos | 1 | skipped | 1 | 0 | 0 |
| test-windows | 1 | skipped | 1 | 0 | 0 |

9 jobs at this head. 
### Every observed head at the cutoff

Configuration differs across this table; compatibility jobs appear on heads before #794. Null gates carry a reason in the JSON.

| Run | Kind | PR | Head | Attempts | Outcome | Gate seconds | Jobs |
|---|---|---|---|---:|---|---:|---:|
| [42543621639](https://github.com/nickderobertis/crozier/actions/runs/42543621639) | release-pr | 801 | 733331003bf9 | 1 | failure | 51 | 4 |
| [42509110093](https://github.com/nickderobertis/crozier/actions/runs/42509110093) | release-pr | — | 74678c4b8fc2 | 1 | success | 860 | 6 |
| [42543394021](https://github.com/nickderobertis/crozier/actions/runs/42543394021) | main | — | bad5d6cae406 | 1 | none | unknown | 7 |
| [42530351454](https://github.com/nickderobertis/crozier/actions/runs/42530351454) | pr | — | 210980f53cd7 | 1 | success | 9247 | 4 |
| [42539881675](https://github.com/nickderobertis/crozier/actions/runs/42539881675) | pr | 793 | 66f2db252073 | 1 | none | unknown | 4 |
| [42532483422](https://github.com/nickderobertis/crozier/actions/runs/42532483422) | pr | 800 | 19cda960fc65 | 1 | failure | 11632 | 4 |
| [42524007437](https://github.com/nickderobertis/crozier/actions/runs/42524007437) | pr | — | eeefbf409014 | 1 | failure | 5940 | 6 |
| [42532383652](https://github.com/nickderobertis/crozier/actions/runs/42532383652) | pr | 796 | f0b5007c1945 | 1 | success | 6551 | 4 |
| [42530023747](https://github.com/nickderobertis/crozier/actions/runs/42530023747) | main | — | 1a278de16cf7 | 1 | cancelled | unknown | 7 |
| [42516086127](https://github.com/nickderobertis/crozier/actions/runs/42516086127) | pr | — | 9ffeacc4484e | 1 | success | 6720 | 6 |
| [42525424004](https://github.com/nickderobertis/crozier/actions/runs/42525424004) | pr | 793 | 354b35ab95d0 | 1 | cancelled | unknown | 4 |
| [42519971743](https://github.com/nickderobertis/crozier/actions/runs/42519971743) | pr | 774 | 416a36a38100 | 2 | cancelled | unknown | 8 |
| [42518267781](https://github.com/nickderobertis/crozier/actions/runs/42518267781) | main | — | e7c3a8db4a35 | 1 | none | unknown | 7 |
| [42481455354](https://github.com/nickderobertis/crozier/actions/runs/42481455354) | pr | 790 | 397371d3dca9 | 3 | success | 16363 | 23 |
| [42513978896](https://github.com/nickderobertis/crozier/actions/runs/42513978896) | pr | — | 459cc01c6358 | 1 | failure | 6352 | 4 |
| [42512011009](https://github.com/nickderobertis/crozier/actions/runs/42512011009) | pr | — | d5c91216c06a | 1 | cancelled | unknown | 4 |
| [42509483184](https://github.com/nickderobertis/crozier/actions/runs/42509483184) | pr | — | feda075ada47 | 1 | cancelled | unknown | 4 |
| [42509093015](https://github.com/nickderobertis/crozier/actions/runs/42509093015) | pr | — | c5e71a9be4ac | 1 | cancelled | unknown | 4 |
| [42509048346](https://github.com/nickderobertis/crozier/actions/runs/42509048346) | pr | 796 | 09bc6900a78c | 1 | success | 12324 | 4 |
| [42506906241](https://github.com/nickderobertis/crozier/actions/runs/42506906241) | pr | — | 97054c5e75af | 2 | success | 14850 | 8 |
| [42489795217](https://github.com/nickderobertis/crozier/actions/runs/42489795217) | pr | — | 76e15eb439bd | 1 | success | 8380 | 6 |
| [42505020291](https://github.com/nickderobertis/crozier/actions/runs/42505020291) | main | — | cd5cebc6649f | 1 | cancelled | unknown | 7 |
| [42500282017](https://github.com/nickderobertis/crozier/actions/runs/42500282017) | pr | 774 | 08dc1a569ad6 | 2 | cancelled | unknown | 14 |
| [42499728596](https://github.com/nickderobertis/crozier/actions/runs/42499728596) | pr | 793 | 4763609f00b7 | 2 | cancelled | unknown | 14 |
| [42490892875](https://github.com/nickderobertis/crozier/actions/runs/42490892875) | pr | 793 | bface37c44e5 | 1 | cancelled | unknown | 7 |
| [42490347595](https://github.com/nickderobertis/crozier/actions/runs/42490347595) | pr | 774 | e5c5323f29c0 | 1 | failure | 2744 | 7 |
| [42489423129](https://github.com/nickderobertis/crozier/actions/runs/42489423129) | pr | — | fe54f2a98d74 | 2 | cancelled | unknown | 14 |
| [42487287801](https://github.com/nickderobertis/crozier/actions/runs/42487287801) | pr | — | c68704414e74 | 1 | cancelled | unknown | 4 |
| [42483082162](https://github.com/nickderobertis/crozier/actions/runs/42483082162) | pr | 774 | 297df8111822 | 1 | failure | 5159 | 7 |
| [42483040498](https://github.com/nickderobertis/crozier/actions/runs/42483040498) | pr | — | c3a7f51f0f75 | 1 | cancelled | unknown | 7 |
| [42481508824](https://github.com/nickderobertis/crozier/actions/runs/42481508824) | pr | — | 5100dc422c47 | 1 | cancelled | unknown | 4 |
| [42475322856](https://github.com/nickderobertis/crozier/actions/runs/42475322856) | pr | 793 | ed2c6995beb4 | 1 | cancelled | unknown | 7 |
| [42472362509](https://github.com/nickderobertis/crozier/actions/runs/42472362509) | pr | — | 2e3ee269bec1 | 1 | failure | 5530 | 7 |
| [42462730498](https://github.com/nickderobertis/crozier/actions/runs/42462730498) | pr | — | aaf606c399bd | 1 | failure | 3716 | 7 |
| [42460231103](https://github.com/nickderobertis/crozier/actions/runs/42460231103) | pr | — | 8425594385a5 | 1 | cancelled | unknown | 7 |
| [42459981394](https://github.com/nickderobertis/crozier/actions/runs/42459981394) | main | — | 1834a1896b9f | 1 | none | unknown | 7 |
| [42459459557](https://github.com/nickderobertis/crozier/actions/runs/42459459557) | release-pr | — | d9f9f4c157d9 | 1 | success | 425 | 9 |
| [42459286346](https://github.com/nickderobertis/crozier/actions/runs/42459286346) | pr | — | 99cebe6ac74b | 1 | none | unknown | 2 |
| [42459285764](https://github.com/nickderobertis/crozier/actions/runs/42459285764) | main | — | 94d22c08869c | 1 | cancelled | unknown | 7 |

### Comparison with the baseline, like kinds

Passing heads only; a window spanning configurations, so this is the CLI's raw distribution, and the finished-configuration heads are named above.

| Kind | Baseline median / p95 / max (n) | After median / p95 / max (n passing) |
|---|---|---|
| pr | 9046 / 10069 / 10069 (18) | 9247 / 16363 / 16363 (7) |
| release-pr | 7937 / 9275 / 9275 (5) | 642.5 / 860 / 860 (2) |
| main | 8160.5 / 9901 / 9901 (8) | not comparable: main CI deliberately removed |

The improvements that are real are structural. The release path dropped from about 8000 s to under 900 s because it now runs one guarded lane. Job count per ordinary push fell to 4 from about 20. Ordinary PR gate time did **not** improve: a four-lane broad change is 8380-11632+ s against a baseline median of 9046 s. Execution moved into the lanes rather than vanishing, because test-linux alone holds all Linux-only proof.

**Separating causes.** Queue versus execution, for the finished-configuration heads:

- Execution-dominated: #794 (test-linux 8355 s, queue under 3 s) and #800 test-linux (9190 s).
- Queue-dominated: #796's two heads, a narrow change whose gate is the macOS lane (queue 3058 s, about 51 min, on the second head and 9002 s, about 2.5 h, on the first).
- #800 macOS queued about 2 h 25 min before failing.

Account load: between 5 and 11 other crozier PR heads overlapped each finished-configuration sample (this dispatch's own demonstrations among them, for #796's first head), and the account's macOS capacity is shared with the user's other repositories, whose use is not observable from crozier's records, so a queue cannot be attributed to any single other job. Cache state: `remote-cache` replays appear per lane above. Lint replayed most tasks (91 of 109 on #794). Test lanes replayed almost nothing: 0 on every sampled lane except #796's first head on test-linux (33 of 49), whose result cache came from a run at the same base; after main moved, its later head replayed none. The expensive suites ran cold on every sample.

### Predicted versus observed selection

The baseline predicted a broad source change selects the crozier, crozier-e2e, surface-census (census, reach, portable), SDK, runtime, live-e2e, corpus-match, corpus-match-selection and census-fallback suites (each at 16 or 17 heads of 20, e2e 20/20), with lane costs bounded by planning intervals only.

| Prediction | Observed on #800 (broad source) | Observed on #794 (CI tool change) | Observed on #796 (tooling change) |
|---|---|---|---|
| crozier and crozier-e2e affected | `crozier:test` and `crozier-e2e:test` ran on every test lane; crozier-e2e:test 2758 s on Windows, and macOS failed in it | both tasks ran on every test lane, reached through their task closure | not run |
| surface-census and reach | ran on every test lane | ran on every test lane | `surface-census:test-census` ran on test-linux and test-macos, not test-windows (test-linux result replayed on the first head) |
| corpus-match, live-e2e, census-fallback (Linux only, retained on the PR lane) | ran on test-linux; `corpus-match:test-offline` 2575 s, `test-match` 2447 s, `test-strict` 2343 s | corpus-match ran on test-linux, live-e2e did not | not run |
| SDK env / runtime | ran on test-linux and test-windows | not run | not run |

Broad-source coverage held: full census, reach and the live end-to-end and corpus byte-match suites all ran in the PR lane of #800 on the platforms ci.yml assigns them; none was moved, dropped, lightened or sharded to obtain these numbers.

The baseline's planning intervals (lint [1293,5330]+U; test-linux [386,7260]+U; test-windows [593,6467]+U; test-macos [1446,9297]+U) were explicitly not feasibility claims. Observed lane execution for broad changes: lint 803-973 s; test-linux 8355-9190 s; test-windows 4790-5070 s; test-macos 5991 s on #794 (no complete broad-source figure, because #800 failed at 2917 s). Linux exceeds its interval's upper proxy by 1095-1930 s, and every test lane exceeds the 30-minute inner line.

### Goal status and escalation

The under-hour goal is **unmet at the finished configuration**. The remaining gap for a broad change is execution on test-linux: about 2.3-2.6 times the whole line, before any queue. The gap for narrow changes is account macOS queue. Under the standing rules there is no honest correction within reach: the slowest proof (corpus-match, live-e2e, census) is retained and cannot be moved, shrunk or sharded, and the account has no larger runner. Each result at or above 3600 s was reported to the manager as it occurred (correlations c-15d444f3df4df557c4ab4d4d5584a955, c-9d3a6985de2de8a0161a811fdbf1fbfb, c-479e1b2e6f6819ad7b53aa37a03e35a0); the decision on paid runners or an explicit infeasibility exception is the user's and is still open. Corrective proposals for that decision: reduce test-linux's serial live/corpus/fallback span by honest dependency work (no sharding), or accept the standing two-hour outcome explicitly.

`crozier-pr-gate-minutes` (threshold 3599) is registered and read by this host's delivery hook for each landed head; it is not an on-CI check and reports each landed head's figure, over or within. Its contract proof is `tools/ci-journeys/tests/delivery-budget.test.mjs`, which runs it under real onebudgetspec with recorded answers: for head 76e15eb439 it reports 8380 seconds, verdict over.

## Baseline

**The existing jobs exceed both timing lines. This baseline does not prove that all tests fit four lanes, 30 minutes per job, or an hour outside.** No workflow, suite, platform, corpus case, or enforcement threshold changes here.

Inventory tree: `afe5f8c0bc88aacc4792d8fb301338c946ac6c69` (main at observation). Calculation implementation: `750f1eccc`. Observation began 2026-11-04T01:35:44.674Z. The snapshot was finalized with that commit's exported calculations over the same immutable responses; this measures main CI independently of release-plz/gallery jobs, preserves every required-context attempt, and marks inconsistent job clocks unknown.

Final main refresh: `8f2b78e9344751bab709d7bff6be0c5748d88385` landed during this dispatch. Its changes add generator/parity proof and fixtures; `.github/`, project definitions, `nx.json`, `justfile`, dependency manifests and the toolchain pin are unchanged from the inventory tree. The workflow inventory and graph selection therefore remain applicable, but historical durations do not measure the added test work. Downstream must refresh costs after concurrent proof changes land; no new runtime or feasibility claim follows from this refresh.

### Reproduce and interpret

The maintainer contract is [gate-timing.mjs](../tools/ci/gate-timing.mjs), including `--help`, exported validation/calculation functions, and schema version 1. Reconciliation by the closing node uses this exact window and command, with refreshed run metadata and reused completed attempts:

```sh
node tools/ci/gate-timing.mjs runs --since 2026-10-31T00:00:00Z --until 2026-11-03T20:00:00Z --limit 200
```

The persistent cache is $XDG_CACHE_HOME/crozier/gate-timing, falling back to $HOME/.cache/crozier/gate-timing. The planner's earlier raw records in `scratch/crozier-gate-rev1` supplied recorded test seeds and historical job evidence. Read-only job queries use onevcs host where supported; gh GET supplies listing, protection/rulesets, run metadata, and historical attempts. The scan checks quota before reads, pauses below 40%, and immediately propagates secondary-limit refusals. This observation did not encounter a quota wait; replay tests induce wait/resume without a time threshold.

Committed evidence:

- [baseline.json.gz](ci-gate-timing/baseline.json.gz): schema-1 report, every observed head, job and raw timestamp, summary, sampling completeness and limitations.
- [attempts.json.gz](ci-gate-timing/attempts.json.gz): immutable job answers, run IDs/attempts, observation timestamps and observed context sets. No rerun appears in this capped sample; recorded crozier Visual docs run 41288057298 supplies both real attempt responses outside the capped portion for the CLI replay journey.
- [opportunity.json.gz](ci-gate-timing/opportunity.json.gz): all 20 base/head file lists, old/proposed selections, both full graph snapshots and inputs, broad-change scenarios, pinned Nx version and graph commit. Decompress with `gzip -dc`; these are UTF-8 JSON, compressed to keep the evidence reviewable without thousands of repeated fixture paths.

The window contains **416 workflow runs** at listing. A cap of 200 listing entries yielded **171 completed relevant PR/main workflow runs (138 successful, 21 cancelled, 12 failed), 54 distinct event/head groups and 1100 expanded job records**. Therefore completeness is **partial**, not a census of every run in the three-day window. The 20 ordinary-head study below is wholly inside the selected portion. Cancelled and failed runs remain in the report. A cutoff can omit sibling workflows at the oldest boundary; per-head counts describe observed jobs, not an assertion that GitHub has no additional workflow. Fully represented representative PR 41707011394 has all three PR-triggered workflows and 20 jobs.

Required contexts observed from main protection plus active branch rules: **commitlint, gate, llmlint**. These are current observations, not proof of the contexts required when each historical head ran. The report preserves this historical ambiguity. Gate duration starts at the first workflow creation at the head and ends with the last required-context completion, including earlier failed attempts and waiting. Workflow creation is a proxy seconds after push; commit authored time is never used. Failed gates retain their measurable span but do not enter the passing distribution. Cancelled/missing required contexts yield null plus a reason. Main measures CI workflow completion separately, retaining other workflows only in the job inventory.

Queue is job-created to job-started. Start offset also includes workflow eligibility/needs delay and is **not queue**. A job that never started has a zero start-offset sentinel accompanied by `start_offset_reason`; its raw null timestamp and null queue/run time distinguish it from an instant start. GitHub jobs do not expose the dependency DAG: `critical_path` lists terminal required contexts, not a fabricated ancestry. Platform blocking spans below identify observed costs without pretending to reconstruct reusable-workflow dependencies.

### Head outcomes (seconds)

Passing statistics use nearest-rank p95; median averages the two central samples. Unsuccessful/missing heads are counted separately, never silently treated as passing or zero.

| Kind | Observed heads | Passing n | Unsuccessful/null | Median | p95 | Max |
|---|---|---|---|---|---|---|
| pr | 35 | 18 | 17 | 9046 | 10069 | 10069 |
| release-pr | 7 | 5 | 2 | 7937 | 9275 | 9275 |
| main | 12 | 8 | 4 | 8160.5 | 9901 | 9901 |

All identified groups follow. IDs identify the first workflow at the head; the compressed evidence identifies every sibling run and attempt.

| Run ID | Kind | Head | Outcome | Gate/CI seconds | Observed jobs |
|---|---|---|---|---|---|
| [41707011394](https://github.com/nickderobertis/crozier/actions/runs/41707011394) | pr | 92ba8f4bf1e6 | success | 9950 | 20 |
| [41705104876](https://github.com/nickderobertis/crozier/actions/runs/41705104876) | pr | 788619a61ab4 | success | 9630 | 20 |
| [41705037735](https://github.com/nickderobertis/crozier/actions/runs/41705037735) | pr | 48070335cc99 | failure | 950 | 18 |
| [41688593651](https://github.com/nickderobertis/crozier/actions/runs/41688593651) | release-pr | 751d56be7955 | success | 7594 | 20 |
| [41672240788](https://github.com/nickderobertis/crozier/actions/runs/41672240788) | pr | 259bd2f03ec8 | success | 5741 | 25 |
| [41688206577](https://github.com/nickderobertis/crozier/actions/runs/41688206577) | main | d0a0d6639f51 | success | 4271 | 21 |
| [41679202149](https://github.com/nickderobertis/crozier/actions/runs/41679202149) | release-pr | ae41d4e3721c | failure | 3587 | 18 |
| [41656083162](https://github.com/nickderobertis/crozier/actions/runs/41656083162) | pr | af48c75973a0 | success | 7192 | 25 |
| [41678728430](https://github.com/nickderobertis/crozier/actions/runs/41678728430) | main | b9a51feba099 | cancelled | unknown | 19 |
| [41673733829](https://github.com/nickderobertis/crozier/actions/runs/41673733829) | pr | 67b273481b3c | failure | 6605 | 18 |
| [41631058331](https://github.com/nickderobertis/crozier/actions/runs/41631058331) | release-pr | 35d6cad6df35 | success | 9144 | 25 |
| [41653597938](https://github.com/nickderobertis/crozier/actions/runs/41653597938) | main | 7665d8ae26dd | success | 7517 | 21 |
| [41653569848](https://github.com/nickderobertis/crozier/actions/runs/41653569848) | pr | 6275720cfd2c | failure | 8769 | 20 |
| [41648156354](https://github.com/nickderobertis/crozier/actions/runs/41648156354) | pr | 6fa22ef21534 | failure | 5846 | 18 |
| [41634912765](https://github.com/nickderobertis/crozier/actions/runs/41634912765) | pr | 999c57975b70 | failure | 5645 | 18 |
| [41608351932](https://github.com/nickderobertis/crozier/actions/runs/41608351932) | pr | 612b41a8d978 | success | 9811 | 25 |
| [41630787414](https://github.com/nickderobertis/crozier/actions/runs/41630787414) | main | 92ea90fd998e | cancelled | unknown | 21 |
| [41616839353](https://github.com/nickderobertis/crozier/actions/runs/41616839353) | pr | d506248e0cff | success | 9892 | 20 |
| [41611913481](https://github.com/nickderobertis/crozier/actions/runs/41611913481) | pr | e3fd93e270dc | success | 9836 | 20 |
| [41583499743](https://github.com/nickderobertis/crozier/actions/runs/41583499743) | release-pr | c3152c69dede | success | 9275 | 25 |
| [41599745140](https://github.com/nickderobertis/crozier/actions/runs/41599745140) | main | ab45c3c393d7 | success | 8753 | 21 |
| [41583305128](https://github.com/nickderobertis/crozier/actions/runs/41583305128) | main | caaca4d1a64b | success | 9034 | 21 |
| [41569988917](https://github.com/nickderobertis/crozier/actions/runs/41569988917) | pr | e89ac7e6f3bc | success | 8098 | 25 |
| [41581267167](https://github.com/nickderobertis/crozier/actions/runs/41581267167) | pr | 3b0073af50ca | failure | 8370 | 20 |
| [41573193490](https://github.com/nickderobertis/crozier/actions/runs/41573193490) | pr | c5f89d1193ab | success | 8336 | 20 |
| [41572470837](https://github.com/nickderobertis/crozier/actions/runs/41572470837) | pr | 0445c8f0b2a1 | success | 10069 | 20 |
| [41569374993](https://github.com/nickderobertis/crozier/actions/runs/41569374993) | pr | fc28d57f1b75 | failure | 6685 | 18 |
| [41564205438](https://github.com/nickderobertis/crozier/actions/runs/41564205438) | main | 784580787b14 | success | 9901 | 21 |
| [41548323118](https://github.com/nickderobertis/crozier/actions/runs/41548323118) | pr | 174d25392606 | success | 8298 | 25 |
| [41563149893](https://github.com/nickderobertis/crozier/actions/runs/41563149893) | pr | fe4360751d32 | failure | 5614 | 18 |
| [41542022291](https://github.com/nickderobertis/crozier/actions/runs/41542022291) | pr | 1866b2496924 | failure | 6471 | 18 |
| [41515487826](https://github.com/nickderobertis/crozier/actions/runs/41515487826) | release-pr | 6d3c9761ec1e | success | 7937 | 25 |
| [41535623186](https://github.com/nickderobertis/crozier/actions/runs/41535623186) | main | 3601b87968e3 | success | 8429 | 21 |
| [41531407516](https://github.com/nickderobertis/crozier/actions/runs/41531407516) | pr | 391372aafc2e | success | 9660 | 20 |
| [41523437606](https://github.com/nickderobertis/crozier/actions/runs/41523437606) | pr | f57460f348e9 | failure | 9912 | 20 |
| [41494688538](https://github.com/nickderobertis/crozier/actions/runs/41494688538) | pr | 658ec1b1dc0e | success | 7680 | 25 |
| [41515051767](https://github.com/nickderobertis/crozier/actions/runs/41515051767) | main | 6cbb5146e6d9 | cancelled | unknown | 21 |
| [41504214705](https://github.com/nickderobertis/crozier/actions/runs/41504214705) | pr | 9507e7edc5f3 | failure | 6584 | 18 |
| [41493963863](https://github.com/nickderobertis/crozier/actions/runs/41493963863) | pr | ee229b330ae5 | success | 8299 | 20 |
| [41491171659](https://github.com/nickderobertis/crozier/actions/runs/41491171659) | pr | b130ab4aaa57 | failure | 5715 | 18 |
| [41486697515](https://github.com/nickderobertis/crozier/actions/runs/41486697515) | pr | 712f5da5ebaa | failure | 4543 | 18 |
| [41475751761](https://github.com/nickderobertis/crozier/actions/runs/41475751761) | pr | bb2975523089 | failure | 6495 | 18 |
| [41475668845](https://github.com/nickderobertis/crozier/actions/runs/41475668845) | pr | 395627d34156 | failure | 5845 | 18 |
| [41453228091](https://github.com/nickderobertis/crozier/actions/runs/41453228091) | release-pr | e2102e57d331 | success | 7162 | 25 |
| [41471957599](https://github.com/nickderobertis/crozier/actions/runs/41471957599) | main | a08dc0421817 | success | 7892 | 21 |
| [41466491795](https://github.com/nickderobertis/crozier/actions/runs/41466491795) | pr | fd94cee02b57 | failure | 5008 | 18 |
| [41466472487](https://github.com/nickderobertis/crozier/actions/runs/41466472487) | pr | f644500de9aa | failure | 3625 | 18 |
| [41431621180](https://github.com/nickderobertis/crozier/actions/runs/41431621180) | pr | bcf05aa089b8 | success | 9485 | 25 |
| [41452936325](https://github.com/nickderobertis/crozier/actions/runs/41452936325) | main | 802923daad00 | cancelled | unknown | 21 |
| [41445791807](https://github.com/nickderobertis/crozier/actions/runs/41445791807) | pr | d986e12dccea | success | 7003 | 20 |
| [41441347486](https://github.com/nickderobertis/crozier/actions/runs/41441347486) | pr | e4606778e9bc | success | 9339 | 20 |
| [41436848352](https://github.com/nickderobertis/crozier/actions/runs/41436848352) | pr | b96e3cc89efa | success | 8753 | 20 |
| [41432654427](https://github.com/nickderobertis/crozier/actions/runs/41432654427) | release-pr | a0029bf54e87 | missing or incomplete context | unknown | 5 |
| [41432651954](https://github.com/nickderobertis/crozier/actions/runs/41432651954) | main | 36ad64179693 | success | 7838 | 21 |

### Every observed job (seconds)

These are observed mixed-cache distributions, including unsuccessful executions and skipped jobs with GitHub timestamps. **Cold and warm p50/p95 are unknown for every row**: job success and a restored uv package cache do not establish an Nx task-cache hit or a cold Rust build. Each run/queue cell is n / median / p95 / max; null or inconsistent timestamps are excluded from that cell, not turned into zero. GitHub returned 115 completed-before-started job clock pairs (mostly skipped jobs); those run durations are unknown and their raw timestamps remain in the evidence.

| Expanded job name | Run n/median/p95/max | Queue n/median/p95/max |
|---|---|---|
| check (ubuntu-latest) | 53 / 3890 / 4357 / 4425 | 53 / 2 / 124 / 531 |
| check (windows-latest) | 53 / 5860 / 6468 / 6508 | 53 / 2 / 23 / 227 |
| commitlint | 49 / 5 / 15 / 47 | 53 / 2 / 102 / 798 |
| gate | 53 / 79 / 146 / 292 | 53 / 2 / 12 / 19 |
| guard | 12 / 3 / 4 / 4 | 12 / 2 / 12 / 12 |
| install (${{ matrix.os }}) | 11 / 0 / 0 / 0 | 16 / 0 / 0 / 0 |
| install (ubuntu-latest) | 37 / 277 / 344 / 352 | 37 / 2 / 12 / 568 |
| install (windows-latest) | 37 / 475 / 548 / 575 | 37 / 2 / 13 / 516 |
| live-e2e | 48 / 2542.5 / 3439 / 3544 | 53 / 2 / 12 / 271 |
| llmlint | 47 / 576 / 1155 / 1446 | 53 / 2 / 138 / 790 |
| macOS check, SDK environment and install | 42 / 5516.5 / 7338 / 9610 | 53 / 2 / 304 / 1604 |
| macos-policy | 53 / 40 / 206 / 301 | 53 / 2 / 194 / 840 |
| package | 48 / 313 / 411 / 552 | 53 / 2 / 7 / 579 |
| pool-maintenance | 32 / 0 / 0 / 0 | 53 / 0 / 0 / 0 |
| release-plz | 12 / 127 / 191 / 191 | 12 / 2 / 12 / 12 |
| sdk-env (${{ matrix.os }}) | 11 / 0 / 0 / 0 | 16 / 0 / 0 / 0 |
| sdk-env (ubuntu-latest) | 37 / 283 / 394 / 492 | 37 / 2 / 69 / 477 |
| sdk-env (windows-latest) | 37 / 524 / 741 / 791 | 37 / 2 / 66 / 580 |
| suppressions | 41 / 68 / 221 / 283 | 41 / 2 / 20 / 488 |
| visual-docs / arches | 65 / 71 / 125 / 163 | 65 / 2 / 39 / 493 |
| visual-docs / capture | 17 / 0 / 0 / 0 | 23 / 0 / 0 / 0 |
| visual-docs / capture (x86_64) | 42 / 279 / 315 / 349 | 42 / 2 / 125 / 344 |
| visual-docs / cleanup-preview | 45 / 0 / 8 / 13 | 65 / 0 / 4 / 13 |
| visual-docs / prune-history | 47 / 0 / 1 / 11 | 65 / 0 / 0 / 0 |
| visual-docs / report | 14 / 0 / 0 / 0 | 23 / 0 / 0 / 0 |
| visual-docs / report (x86_64) | 42 / 92.5 / 217 / 238 | 42 / 2 / 33 / 67 |

Names containing `${{ matrix.os }}` are literal GitHub names for unexpanded skipped matrix jobs, not authored placeholder values.

PR-triggered expanded counts, including skipped/cancelled records and additional lifecycle-triggered workflows at the same head, by head kind (not a per-push forecast):

| Kind | Heads | Jobs per head n/median/p95/max |
|---|---|---|
| pr | 35 | 35 / 20 / 25 / 25 |
| release-pr | 7 | 7 / 25 / 25 / 25 |

### Workflow and duplication inventory at the inventory tree

| Workflow / job family | Trigger / platform / tier | Proof and duplication |
|---|---|---|
| ci: macos-policy | PR/main, Linux metadata | Classifies Mac obligation; not an execution substitute. |
| ci: check ×2 | Linux, Windows; ordinary affected, release-PR sweep | Rust coverage, goldens, Python tooling, workflow contracts, tooling supply-chain/doc/lint; both platforms remain. Windows omits the Python coverage aggregate, not the suites. |
| ci: sdk-env ×2 | Linux, Windows; promoted selected inputs | SDK PyPI environments, runtime and nested discriminator runtime. Repeats generator builds in separate jobs today. |
| ci: macOS check, SDK environment and install | Mac policy lane | Same local checks followed serially by SDK environment/runtime and real install/smoke. Source changes do not bypass Mac obligation. |
| ci: live-e2e | Linux; promoted | Real Prism, corpus-match/strict/offline, selection and census-fallback stages; external observations remain uncached where cache would change their proof. |
| ci: package | Linux | Native archive, wheel/sdist and crate packaging/build checks. Another binary build. |
| ci: install ×2 | Linux, Windows | Real installer and generation smoke; distinct artifact proof from source tests. Mac runs its equivalent in the Mac lane. |
| ci: commitlint, llmlint | Linux | PR title and diff-scoped judged/config/plugin-boundary proof. llmlint is an independent required context. |
| ci: gate | Linux, after local/SDK/install/package/live/Mac | Required aggregator, including its checkout/setup and queue; not all contributor waiting is test work. |
| ci: pool-maintenance | Linux, release PR after gate | Real two-build/prune host budget, uncached; ordinary PRs still run its light tests when affected. Not part of gate's needs. |
| notignored: suppressions | PR, Linux | Suppression review; one additional workflow/job outside ci.yml. |
| Visual docs reusable workflow | PR/main, Linux capture/gallery | Five expanded observed jobs, including classify/capture/render/comment/gallery work; binary build and screenshots repeat setup outside ci.yml. Its expanded names and durations are above. |
| release-plz: guard + release-plz | Main push only, Linux | Release bookkeeping, separately inventoried; never substitutes for PR required checks or main CI completion. |
| Fern goldens / release | Schedule/dispatch / published release | Not started by a PR push. No test is moved here by this study. |

The representative ordinary PR observation contains 14 ci job records (pool budget skipped), one suppressions job and five reusable visual-docs records: **20**, not 14. Matrix expansion is counted at job-response level. Repeated builds across check, SDK, package, install and screenshots are real candidates for sharing already-proven artifacts; installed-release, environment and external-contact journeys remain independent proofs.

### Platform blocking example and task evidence

Ordinary PR head `92ba8f4bf1e67aacf1ee5dbcbdf8669092321b86`, CI run [41707011394](https://github.com/nickderobertis/crozier/actions/runs/41707011394), provides these exact job/step timestamps. All are successful. Setup is job start to the first named gate step; checkout/tool provisioning/bootstrap are included. SDK jobs start after check eligibility, so their large workflow offsets are not runner queue.

| Platform/job ID | Actual queue s | Setup s | Serial measured gate phases s |
|---|---:|---:|---|
| Linux check / 126166549882 | 3 | 230 | Check 4037 |
| Windows check / 126166549829 | 2 | 360 | Check 4958 |
| Mac combined / 126167522970 | 3 | 178 | Check 7572 + SDK 1581 = 9153 |
| Linux SDK / 126214119814 | 2 | 298 | SDK/runtime group 191 |
| Windows SDK / 126214119851 | 2 | 441 | SDK/runtime group 289 |
| Linux external / 126214119907 | 2 | 75 | live/corpus/fallback group 2004 |

For this head the Mac serial phases alone take **152.55 minutes**, before setup/install/queue and required-context completion. Linux local plus SDK phases would be **70.47 minutes** serially; Windows **87.45**. These existing combined jobs exceed 30 minutes. Because their Check phases mix lint and tests, they do not alone prove impossibility of the planner's declared separate-lint shape.

For this representative head, ci.yml is byte-identical between the historical head and the inventory tree, so its declared needs edges support the following **observed current-workflow paths**. These explain the baseline; they do not propose routing for the future four lanes.

| Current platform path | Last platform obligation completed | Offset from first workflow creation |
|---|---|---:|
| Linux/Windows Check matrix barrier → Linux live/corpus/fallback → gate | 21:57:11Z | 7601 s |
| Linux/Windows Check matrix barrier → Windows SDK/runtime → gate | 21:34:43Z | 6253 s |
| macos-policy → Mac Check/SDK/install → gate | 22:35:38Z | 9908 s |

The observed overall blocking path is macos-policy → Mac → gate. The first CI jobs were created 187 s after workflow creation; that eligibility/processing interval is not runner queue. Then policy queue 3 s + policy execution 104 s + Mac eligibility 1 s + Mac queue 3 s + Mac execution 9610 s + gate eligibility 1 s + gate queue 2 s + gate execution 39 s totals **9950 s**. Required judged lint completed earlier at 20:06:24Z. Linux SDK cannot start when Linux Check alone finishes: its existing matrix needs barrier also waits for Windows Check, explaining its large start offset despite only 2 s actual queue. Historical reusable-workflow ancestry remains unavailable; the CLI does not infer those edges from timestamps.

Historical successful gate output hides its Nx log. Failed Linux job [126048639037](https://github.com/nickderobertis/crozier/actions/runs/41673733829/job/126048639037) replays it and exposes **0/128 Nx cache hits**, total Nx execution **2294 s** and single-task critical path **1715 s**. Its task bodies report Rust coverage nextest **68.497 s** (plus 53.93 s build), e2e/goldens nextest **627.308 s** (plus 21.58 s build), census pytest **1703.74 s** (failed), reach **54.408 s** and portable reach **51.734 s**. These are individual suite/body costs in one failed Linux observation, **not per-tier cold p95**, and do not establish cache-hit rates for other heads/platforms. The raw logs remain in the shared persistent cache's `job-details/`; job IDs are immutable GitHub provenance.

New gate logs expose the existing Nx profile's per-task seconds and status on both success and failure; no task is repeated. Missing/malformed telemetry is explicitly diagnosed on stderr and retained in the gate log without changing the task's exit status. Real Nx journeys verify exactly-once execution, valid telemetry and damaged-profile recovery.

### Current re-pinning proof

Main at the inventory tree has `tools/surface-census/tests/golden_reach_test.py`: site resolution, report/marker rewriting, unreadable reasons, measurement inputs, arm-search stages and loopback network stages, no-POSIX portability, worker count and recipe contracts. `surface_census_test.py` owns source/census snapshot and shape-proof drift. The three current census/reach/portable targets execute these light tests; full instrumented `golden-reach` remains a separate measurement. The incremental-store/repin commits (including ac9fb6369 and 657062ff0) were **not on fetched main**; they were only on `origin/nick/732/golden-reach-incremental-repin`. The manager was notified of the task's contrary premise. No abandoned multi-edit measurement is run, restored or used as evidence. The optimization node must refresh this inventory after that branch or the other live runs land.

## Revision 2 opportunity study

### Population and real affected replay

The following are **20 distinct ordinary PR heads**, newest first within the same window. Base is the actual git merge-base of the PR's comparison base and historical head; file paths come from `git diff --name-only --no-renames base head`, not title inference. Deleted/renamed paths are therefore retained as changed paths. Complete file lists, comparison bases and selections are in the opportunity artifact.

| PR | Run ID | Base | Head | Changed paths | Current/proposed selected projects |
|---|---|---|---|---|---|
| [#750](https://github.com/nickderobertis/crozier/pull/750) | 41707011874 | d0a0d6639f51 | 92ba8f4bf1e6 | 619 | 26 / 33 |
| [#724](https://github.com/nickderobertis/crozier/pull/724) | 41705104876 | b9a51feba099 | 788619a61ab4 | 859 | 27 / 35 |
| [#750](https://github.com/nickderobertis/crozier/pull/750) | 41705037735 | d0a0d6639f51 | 48070335cc99 | 618 | 26 / 33 |
| [#745](https://github.com/nickderobertis/crozier/pull/745) | 41688209096 | caaca4d1a64b | 259bd2f03ec8 | 21 | 11 / 12 |
| [#723](https://github.com/nickderobertis/crozier/pull/723) | 41678730449 | 92ea90fd998e | af48c75973a0 | 955 | 27 / 35 |
| [#750](https://github.com/nickderobertis/crozier/pull/750) | 41673735832 | 92ea90fd998e | 67b273481b3c | 616 | 26 / 33 |
| [#724](https://github.com/nickderobertis/crozier/pull/724) | 41653570665 | 92ea90fd998e | 6275720cfd2c | 859 | 27 / 35 |
| [#745](https://github.com/nickderobertis/crozier/pull/745) | 41648156354 | caaca4d1a64b | 6fa22ef21534 | 19 | 11 / 12 |
| [#745](https://github.com/nickderobertis/crozier/pull/745) | 41634912765 | caaca4d1a64b | 999c57975b70 | 19 | 11 / 12 |
| [#727](https://github.com/nickderobertis/crozier/pull/727) | 41630789965 | caaca4d1a64b | 612b41a8d978 | 819 | 27 / 35 |
| [#723](https://github.com/nickderobertis/crozier/pull/723) | 41616839353 | caaca4d1a64b | d506248e0cff | 955 | 27 / 35 |
| [#724](https://github.com/nickderobertis/crozier/pull/724) | 41611913481 | caaca4d1a64b | e3fd93e270dc | 858 | 27 / 35 |
| [#725](https://github.com/nickderobertis/crozier/pull/725) | 41583306207 | 3601b87968e3 | e89ac7e6f3bc | 364 | 26 / 33 |
| [#724](https://github.com/nickderobertis/crozier/pull/724) | 41581267167 | 6cbb5146e6d9 | 3b0073af50ca | 858 | 27 / 35 |
| [#727](https://github.com/nickderobertis/crozier/pull/727) | 41573193490 | 6cbb5146e6d9 | c5f89d1193ab | 815 | 27 / 35 |
| [#723](https://github.com/nickderobertis/crozier/pull/723) | 41572470837 | 784580787b14 | 0445c8f0b2a1 | 955 | 27 / 35 |
| [#724](https://github.com/nickderobertis/crozier/pull/724) | 41569374993 | 6cbb5146e6d9 | fc28d57f1b75 | 857 | 27 / 35 |
| [#740](https://github.com/nickderobertis/crozier/pull/740) | 41564207653 | a08dc0421817 | 174d25392606 | 32 | 31 / 37 |
| [#723](https://github.com/nickderobertis/crozier/pull/723) | 41563149893 | 3601b87968e3 | fe4360751d32 | 946 | 27 / 35 |
| [#725](https://github.com/nickderobertis/crozier/pull/725) | 41542022291 | 3601b87968e3 | 1866b2496924 | 363 | 26 / 33 |

Nx **23.1.0**'s actual `filterAffected` selector was replayed over both saved graphs without running generation or targets. Each git path is a WholeFileChange, matching file-list replay; JSON/lockfile edits are conservatively whole-file, not reconstructed semantic diffs. For reproducibility use `nx/dist/src/project-graph/affected/affected-project-graph.js`'s `filterAffected(graph, changes, nxJson, packageJson)`, where each change is `{file, hash:'replay', getChanges:()=>[new WholeFileChange()]}`; the artifact records both complete node/dependency sets, and named inputs are in the inventory tree's nx.json. `NX_FORCE_REUSE_CACHED_GRAPH=true` prevents plugin worker startup. The installed pinned Nx, not a hand-written glob classifier, made these selections.

The study's hypothetical split graph gives each **existing executable test target** a separate project, removes its old execution/aggregate aliases from the parent, preserves its commands and inputs, and expands `default` to the old project's root. New analysis-only roots are `__proposed__/<project>--<target>`. Parent build/lint/format targets and dependency edges remain; no target is run in this experiment. This is a selection prototype, not a runnable CI replacement: downstream implementation must map orchestration/coverage-output dependencies, preserve every original case and prove parity before using it. No corpus or test journey is shrunk, no platform is dropped, and external observations stay inside platform PR lanes when their actual inputs are affected.

### Expensive tiers, input boundaries and proposed splits

Counts below are selected heads / 20. Current project selection runs all its test children; proposed counts select each unchanged child separately. Cache hit/miss **by tier** and cold/warm runtime **by platform** are unknown except the explicitly scoped failed-job observation above. `cache:true` is permission, not evidence of a hit. Corpus/fallback external stages marked uncached remain uncached.

| Tier / current affected | Concrete proposed project(s) / affected | Inputs retained (full paths in graph artifact) |
|---|---|---|
| crozier: 17/20 | crozier--test: 17/20 | src/**/*.rs, templates/**, assets/**, Cargo manifests/lock/toolchain, crate tests and read fixtures |
| crozier-e2e: 20/20 | crozier-e2e--test: 20/20 | crateSource + e2eSource + e2eReads + generator; dependency on crozier build |
| surface-census: 17/20 | surface-census--test-census: 17/20<br>surface-census--test-reach: 17/20<br>surface-census--test-reach-portable: 17/20 | census source/fixtures/docs; reach and portable also crateTests/e2eSource/generator; preserve both portability runs |
| sdk-env: 16/20 | sdk-env--test: 16/20 | SDK harness, generated-source/fixture and Python pins |
| runtime: 17/20 | runtime--test: 16/20 | runtime harness, generated-source/fixture and Python pins |
| nested-discriminator-runtime: 17/20 | nested-discriminator-runtime--test: 16/20 | nested-discriminator source/harness and generated-source pins |
| live-e2e: 17/20 | live-e2e--test: 16/20 | Prism harness + crateSource, SDK fixtures and external inputs |
| corpus-match: 17/20 | corpus-match--test-match: 16/20<br>corpus-match--test-strict: 16/20<br>corpus-match--test-offline: 17/20 | vendored corpus/pins, crateSource, matching/departure and offline harness inputs |
| corpus-match-selection: 17/20 | corpus-match-selection--test: 16/20 | selection harness, generator/corpus source and pins |
| census-fallback: 17/20 | census-fallback--test-samples: 16/20<br>census-fallback--test-parsers: 16/20<br>census-fallback--test-runner: 0/20<br>census-fallback--test-install: 0/20 | parser/sample corpus, census/search scripts and runner/install harness; external parser stages stay uncached |
| pool-maintenance: 1/20 | pool-maintenance--test: 1/20 | own Rust/Bash code, Cargo pins, justfile, prune tool version; real host budget remains uncached |

Runner/install harness-only tests selected 0/20 in this particular proposed population because their own harness files did not change. Their cases remain present with their existing input contracts; this is not permission to remove them. Generic harness tests are distinct from the full source/fixture census proof. Broad generator changes still select Rust coverage/goldens, all three full census/reach/portable targets, generated-SDK/runtime and corpus proof.

### Timing model and fixed lanes

For each tier i and platform p, expected selected execution is **a_i × (1 − h_i,p) × T_i,p**, where a is the measured affected fraction, h the evidenced task-cache hit rate, and T cold p95. For example e2e/goldens is 1.00 × (1 − h) × T; census/reach/portable each 0.85 × (1 − h) × T; proposed SDK/runtime each 0.80 × T (Nx cache disabled by contract); offline corpus is 0.85 × T when uncached. These are expectations, never worst-PR bounds. The artifact supplies every numerator. Most h and T cells lack telemetry, so replacing them with zero hits and a made-up cold p95 would give a false forecast.

The planner's declared shape is exactly **lint (Linux), test-linux, test-windows and test-macos**. Judged lint belongs in the Linux lint lane. External observations, live end-to-end and package proof belong inside the test lanes; they are not a fifth lane or an additional Linux external/package lane. Existing Linux-only external/package observations are included in test-linux's arithmetic below; this does not propose changing their platform coverage. The baseline chooses no strategy or implementation. The split graph above is a measurement hypothesis, not a design recommendation.

Historical Check phases mix lint, typecheck, formatting, builds and tests. Their test-only shares **C_linux ∈ [0,4037], C_windows ∈ [0,4958], C_macos ∈ [0,7572] seconds** are unresolved. Moving lint into the declared lint lane therefore prevents interpreting an entire historical Check phase as a lower bound on a future test lane. In particular, the 152.55-minute combined Mac observation establishes today's cost, not impossibility of the declared four-lane shape.

The following bounded planning model explicitly retains that uncertainty. Let C_i be each phase's test-only share; h_i its unknown task-cache hit rate. The full local selection union is 20/20, SDK group union 16/20, and external/corpus and package unions 17/20. SDK/runtime Nx caching is disabled, so their h is zero by contract. The external phase mixes uncached observations with cacheable corpus work: preserve the uncached observations, and leave the unmeasured child cost unknown. Whole observed phases/jobs supply **conditional proxy caps**, not measured cold p95 or guaranteed future bounds. Do not add a whole phase once for every child: the per-tier formula above applies when child telemetry exists.

Setup and queue remain explicit. The existing Linux check/SDK/external preparation sums to 603 s and their created-to-start queues sum to 7 s; the first check preparation/queue is 233 s. Windows check/SDK preparation plus queue is 805 s, or 362 s for the first check alone. Mac preparation/queue is 181 s. These are observed preparation envelopes, not a claim that a new lane would necessarily reuse all setup.

For the same representative head, commitlint, judged lint and suppressions have full job run-plus-queue spans 8, 767 and 285 s (1060 s total). Package is 552+2=554 s; Linux install 284+2=286 s; Windows install 471+2=473 s. Mac's remaining post-phase job time is 279 s, including install/smoke and cleanup. These complete-job proxies include their own setup, so it must not be added twice.

| Declared lane | Retained work in the conditional proxy model | Partial estimated seconds |
|---|---|---:|
| lint (Linux) | Linux preparation/queue proxy 233 + observed title/judged/suppression job spans 1060 + unresolved Linux lint share [0,4037]; other lint attribution U_lint | [1293,5330] + U_lint |
| test-linux | Preparation/queue [233,610] + 1.00×(1−h_local)×C_linux + 0.80×191 SDK + external/corpus share [0,0.85×2004] + 0.85×(1−h_package)×554 package + install share [0,286]; unresolved screenshot/other proof U_linux | [385.8,7260.1] + U_linux |
| test-windows | Preparation/queue [362,805] + 1.00×(1−h_local)×C_windows + 0.80×289 SDK + install share [0,473]; other proof U_windows | [593.2,6467.2] + U_windows |
| test-macos | Preparation/queue 181 + 1.00×(1−h_local)×C_macos + 0.80×1581 SDK + remaining post-phase share [0,279]; other proof U_macos | [1445.8,9296.8] + U_macos |

Each U is an explicitly **unmeasured nonnegative residual**, not a placeholder or an omitted-test allowance. Every original proof must be assigned within these four declared lanes by the strategy the user selects; none may be removed to set a U to zero. Package and external costs are already inside test-linux above. Judged work is inside lint. The existing pool light tests remain in PR selection and its real host budget keeps its existing release-PR obligation.

The outer model is E[max(lint, test-linux, test-windows, test-macos)] plus any retained aggregation overhead. Max of expected lane times is a lower bound on that expectation, not its value; sum of expected lanes is an upper bound when their values are bounded. Within the stated phase-proxy model the resolved portion spans 1445.8–28354.1 s; the U residuals and aggregation prevent a finite numerical upper bound for the complete wait. These intentionally wide bounds cannot establish either timing line. They account for observed setup, serial work, real queue and unknown attribution without inventing cold/warm/platform p95.

Per-tier cold/warm/cache gaps were sent to the manager before a feasibility claim. No heavy host measurement filled them. The sole observed task-cache sample, 0/128 on one failed Linux job, cannot be generalized. The declared four-lane shape has an **insufficient-evidence** feasibility verdict; the historical combined jobs themselves already violate the requested timing lines.

### Broad changes are separate cases

| Class | Observed heads /20 | Selected expensive proposed projects | Evidence verdict |
|---|---|---|---|
| source | 16/20 | corpus-match--test-match<br>corpus-match--test-offline<br>corpus-match--test-strict<br>corpus-match-selection--test<br>crozier--test<br>crozier-e2e--test<br>live-e2e--test<br>nested-discriminator-runtime--test<br>runtime--test<br>sdk-env--test<br>surface-census--test-census<br>surface-census--test-reach<br>surface-census--test-reach-portable | Selection observed; tier/platform timing unresolved |
| template | 0/20 | corpus-match--test-match<br>corpus-match--test-offline<br>corpus-match--test-strict<br>corpus-match-selection--test<br>crozier--test<br>crozier-e2e--test<br>live-e2e--test<br>nested-discriminator-runtime--test<br>runtime--test<br>sdk-env--test<br>surface-census--test-census<br>surface-census--test-reach<br>surface-census--test-reach-portable | No historical case in population: insufficient timing evidence |
| dependency | 1/20 | corpus-match--test-match<br>corpus-match--test-offline<br>corpus-match--test-strict<br>corpus-match-selection--test<br>crozier--test<br>crozier-e2e--test<br>live-e2e--test<br>nested-discriminator-runtime--test<br>pool-maintenance--test<br>runtime--test<br>sdk-env--test<br>surface-census--test-census<br>surface-census--test-reach<br>surface-census--test-reach-portable | Selection observed; tier/platform timing unresolved |
| toolchain | 0/20 | corpus-match--test-match<br>corpus-match--test-offline<br>corpus-match--test-strict<br>corpus-match-selection--test<br>crozier--test<br>crozier-e2e--test<br>live-e2e--test<br>nested-discriminator-runtime--test<br>pool-maintenance--test<br>runtime--test<br>sdk-env--test<br>surface-census--test-census<br>surface-census--test-reach<br>surface-census--test-reach-portable | No historical case in population: insufficient timing evidence |
| shared_harness | 0/20 | census-fallback--test-parsers<br>census-fallback--test-samples<br>corpus-match--test-match<br>corpus-match--test-offline<br>corpus-match--test-strict<br>corpus-match-selection--test<br>crozier--test<br>crozier-e2e--test<br>runtime--test<br>sdk-env--test<br>surface-census--test-census<br>surface-census--test-reach<br>surface-census--test-reach-portable | No historical case in population: insufficient timing evidence |

Source has 16 observed heads, including the fully timed head above: historical mixed-phase costs are Linux 4228 s, Windows 5247 s, Mac 9153 s, plus Linux external work 2004 s and package work within test-linux in the declared model. Their test-only shares, setup reuse and aggregation remain unresolved. The historical mixed Mac phases exceed an hour by 5553 s and a 30-minute job by 7353 s. Input splitting does not remove the selected work, while separating lint may move some of it to the declared lint lane; its amount is unknown.

Template changes select the same generator/SDK/full-census target sets in the replay, but there is no template-only historical case here: applying those phase numbers is a bounded planning analogy, not an observed template result. Toolchain has no observed case either and keeps the Cargo-dependent pool tests as well. The one dependency head is not an isolated toolchain experiment; dependency and toolchain changes may invalidate every build/cache, so the same platform phase numbers are an incomplete proxy with additional rebuild cost unknown. The shared-harness scenario also has no observed historical case; it selects the full Rust/census/SDK/corpus/fallback proof shown above, with platform runtime unresolved. None of these missing categories inherits feasibility from aggregate frequencies or ordinary-head medians.

**Verdict:** all original tests and platforms can remain represented in the proposed selection graph; the declared lint/test-linux/test-windows/test-macos shape has not been proven feasible. The existing combined jobs exceed 30 minutes and the outer wait exceeds an hour; feasibility after separating lint from tests in the declared shape is **insufficient evidence**, because the historical Check phases do not resolve those shares. This baseline proposes no design; the user selects the strategy from the measurements. The measured gap was sent to the manager before downstream implementation. No compromise may remove tests, reduce corpus cases/platforms, shrink a journey, move tests to a weekly sweep, cache an external observation whose proof changes, or skip SDK/full-census proof on a broad generator change.

### First reduction candidates

1. Keep the per-task profile visibility and collect complete cold/warm samples on all fixed platform lanes before setting a numeric feasibility claim. This resolves the largest uncertainty without repeating tasks merely to time them.
2. Split existing target ownership using the measured boundaries, retaining commands/cases and exact read paths. This saves at most one head of selection for several promoted tiers in this population; census and e2e rates do not improve.
3. Reuse already-built compatible artifacts and tool provisioning across the existing platform proof journeys, while retaining real installed-artifact and environment boundaries. Current separate check/SDK/package/screenshot builds show the concrete duplication; shared work cannot silently replace any artifact proof.
4. Preserve uncached external proofs in affected platform PR lanes. Optimize their honest setup and input edges, then remeasure; the observed 2004-second external phase already exceeds a 30-minute job before setup.

The optimization node must refresh the main-tree inventory after the named live runs land. The closing node's same-CLI/window GitHub reconciliation is a later factual comparison, not a claim made by this baseline.

## Repeated work removed from the slowest suites

**Provenance of every figure below.** *Measured here* means on this shared WSL host for this change, with other work running; such wall times are indicative only. The census runs and the instrumented `cargo llvm-cov` runs held the instrumented-measurement lock. The e2e run, the single-golden timing, the reach suites and the offline suite did not, because each takes that lock itself where it needs it or holds no instrumented build. The work counts come from short profiled runs and are not timing evidence. *Historical* means read from CI logs. Nothing here is a comparison between CI runs: the comparative wall-time result belongs to the later re-measure on real pull requests, which also confirms the collected cases on Windows and macOS. No job, matrix leg, shard or coverage floor changed; the only workflow edit sets `CARGO_HOME` and the handoff switch on the `live-e2e` gate step.

### What each touched suite no longer repeats

| Suite | Repeated work removed | Evidence on the finished tree (measured here) |
|---|---|---|
| `surface-census:test-census` (`FinishedStateGateTests`) | `load_script` executed every tooling script again on each call, which discarded the per-content memo in `golden-reach.py`; `_function_spans` rescanned a whole Rust file for each named site; each case re-parsed the same witness documents. Scripts now run once per content, one scan indexes each file's functions, and a document is parsed once per content. | Over five cases, tooling-script executions fell from 1219 to 26 for about the same number of `load_script` calls. `test_the_committed_ledgers_are_in_their_finished_state` runs 12,571,637 regex matches at base and 265,667 now. |
| `surface-census:test-census` (`RankedBacklogTests`) | One directory walk and one `records.tsv`, `enumeration.tsv` and pin read per key per source (72 keys × 6 sources), and one whole hand-written gate per row. Each is now read once for the test. Every key's own checks still run. | `test_every_linked_arm_search_names_the_six_sources_and_reconciles` took 334.83 s at base and 41.14 s now; `test_every_non_golden_row_carries_a_proof_or_a_searched_gap` took 86.70 s and 0.91 s. Indicative: the base run had no `--cov` and the finished run had it, so these two runs are not like for like. |
| `surface-census:test-census` (`ScenarioProofIndexTests`) | `read_e2e` re-read the e2e sources on every `check`, scanning forward from each function for its closing brace. It now reads each text once and finds each close by index. | Staleness and body-bound cases in `reuse_staleness_test.py`. |
| `surface-census:test-reach`, `test-reach-portable` | The same site scan in `golden-reach.py`. Their test code is unchanged. | 125 tests pass on the finished tree in about the base's time here (398 s against 401 s, indicative): their time is elsewhere, so they stay slow. |
| `surface-reach:test-fixtures-coverage`, `test-handwritten-reach`, `crozier:test` | Separate instrumented compiles of crozier in `target/llvm-cov-gate` and `target/llvm-cov-target`. One compiled tree now backs both, while each directory keeps its own coverage profiles. | Real `cargo llvm-cov`: the reach run after the gate run compiles no `crozier` unit, and the crate report still reads 96.08% lines both before and after the reach run. |
| `crozier-e2e:test`, `sdk-env`, `runtime`, corpus recipes | `-p crozier` and every suite's build resolved `libc` with different features on Unix, so a job compiled crozier's library and binary twice under the dev profile. `crozier` now declares `libc`. | Cargo's JSON messages: `crozier:build` compiles; the e2e build, `--bin crozier`, `cargo test --no-run` and `--workspace` report crozier `fresh`. `cargo tree` feature sets match on Linux, macOS and Windows targets. |
| `corpus-match:test-offline` | Its cold-registry proof compiled crozier a second time, because cargo fingerprints a crate's absolute source path and a different `CARGO_HOME` makes everything dirty. In `live-e2e`, one empty `CARGO_HOME` now covers the whole step. `corpus-match:cold-registry-build` runs first and makes the job's dev build there with the real `cargo test --no-run`, sockets denied. Later steps reuse it, and the proof holds it to the recorded digests. | `tests/corpus_match/cold_handoff_test.py` drives this over crozier's real source: after the cold build, `crozier:build`, the e2e suite's build and `match.sh` compile nothing and the binary's digest is unchanged. `corpus-match:test-offline` run this way, with an empty `CARGO_HOME` and the handoff switched on, reports that the job's build is the one made with sockets denied (1694 s for its two recipe cases at about load 24, indicative). |

The collected-case lists are `tools/ci/suite-cases/pins/`, taken from base `8cbca1f51` and extended by the 73 e2e cases that merging main at `6f4b6138c` brought with no case lost, and `suite-cases:test` (with `corpus-match:test-offline` for its own) compares them with each suite's live collection on Linux: 808 census, 125 reach, 125 portable reach, 26 fixtures-coverage, 10 handwritten-reach, 6 offline, 1254 crate and 1100 e2e cases. The census suite also ran 8273 subtests at base and 8273 on the finished tree (807 passed, 1 skipped; 1383.05 s with `--cov` at a host load near 27, and 883.74 s in a run before the loader repair, both indicative; the base run took 1997.15 s without `--cov`).

Three Nx results this change adds are cached: `suite-cases:test`, `suite-cases:lint` and `surface-census:test-reuse`. Nx hashes files and listed inputs, not the host, so `suite-cases:test` and `surface-census:test-reuse` also hash the output of `tools/ci/suite-cases/cache-key.mjs`. For both it holds the operating system and architecture, the Python interpreter `uv run` runs the suite under (implementation, full version and build, cache tag, ABI flags, platform and machine, by what it is rather than where), the `uv` version and every `PYTHON*` variable and the tier members' manifests. `suite-cases:test` also hashes the Node version, `rustc -vV` (toolchain and host), the `cargo`, `cargo-nextest` and `cargo-llvm-cov` versions, every compiler and profile variable (`RUSTFLAGS`, `CARGO_PROFILE_*` and their family), and the bytes of each cargo config, the user-level one included. `suite-cases:lint` is `node --check` and the boundary check. Its key holds the project's own files, the `boundaries` inputs, `scripts/share-instrumented-build.mjs` (which it syntax-checks from outside the project) and the output of `node --version`; it does not use `cache-key.mjs`. `tools/ci/suite-cases/tests/cache-key.test.mjs` runs a real Nx over that target's real inputs and `node --check` commands, leaving out the boundary command, which needs the real project graph: unchanged inputs replay, a syntax error in the shared-build script reruns and fails, restoring the script replays, and another Node version reruns while the original still replays. Without those two inputs, the edit replayed the cached success and the other Node version replayed too (measured here). A further check fails if lint syntax-checks a file outside the project that its inputs do not name. The same test file runs a real Nx over the other two targets' real inputs: another operating system, another interpreter (a stand-in, and a really installed second one selected with `UV_PYTHON` where the host has one), a `PYTHON*` variable, other flags, another profile or another user-level config reruns the target, and the original host still replays its own result. It also holds the key's interpreter to the one a real `uv run` reports, with and without `UV_PYTHON`. Removing the interpreter from the key fails those cases.

The two targets' file inputs were checked against what they read. An audit hook recorded every repository file opened while `surface-census:test-reuse` ran and while `suite-cases:test`'s Python suites collected (measured here). It found 517 and 12 files outside the declared inputs, among them the committed ledgers `test-reuse`'s gate reads and the census scripts its collection imports. They are declared now, the same trace finds none outside, and the key test changes one such file per kind and sees the target rerun. The trace covers Python reads only: the cargo-driven cases rest on the `cargo`, `crateTests`, `e2eSource` and tool-version inputs.

Both targets run `uv run --locked --all-packages`, and an edit to any workspace member's `pyproject.toml` can make that command reject the lock. The 19 tooling members' manifests are declared inputs of both targets. The 6 tier members' manifests are hashed by content in `cache-key.mjs` instead, because `nx.json`'s boundary rule forbids a `type:tooling` target from naming a `type:tier` project's files; the rule is unchanged. So a tier-manifest edit never replays a cached success, but on its own it does not make these two targets affected; the tier's own `uv run --locked` targets are. The key test changes each of the 24 manifests in turn under a real Nx and sees the target rerun, while unchanged manifests replay. With a real `uv` and lock it also makes one tooling and one tier manifest stale, and the cached success gives way to uv's rejection. Removing the hash or one declared manifest fails these cases, and a member in neither place fails a further check.

No other new cache outlives a process. Cargo's own fingerprints decide build reuse, so the operating system, toolchain, lock, profile, flags and sources are its key. In-process readings are keyed by the bytes they read, and a loaded script runs those same bytes rather than cached bytecode. `tools/ci/suite-cases/tests/build-reuse.test.mjs` runs the real build commands in the real tree, whose builds are the job's own: a later step reports crozier fresh, and removing the `libc` line fails it. It also repeats the changed-source and compiler-flag checks on a small workspace on every platform. `tests/corpus_match/cold_handoff_test.py` makes the real-source proof on Linux: a real change to `src/lib.rs` is rebuilt with sockets denied if it reaches the proof first. If a normal build reaches it first, the proof rejects the handoff and does its own cold build. Each current artifact needs its own provenance: compiled in the denied run, or reused with the record's exact digest. A result mixing a denied rebuild with any unrecorded reused artifact is rejected whole and leaves the record unchanged. The same test holds a mix of a denied rebuild with recorded artifacts as acceptable.

The criterion limits repeat builds of the same inputs. That test's scratch tree is a different build: another path, with sources it edits on purpose to show a changed input rebuilds, so it runs in `live-e2e` as the test's own fixture. The whole test took 201 s here (indicative), for the later re-measure to count. A step that recompiles the unchanged tree would still fail the criterion. `tools/surface-census/tests/reuse_staleness_test.py` warms each reading and then changes the source, script, document or expected table: the moved site resolves anew, a removed one is refused, a same-size, same-timestamp script edit runs the new code, and a stale `handwritten-reach.tsv` is rejected. A site-resolver memo made to ignore content fails five of its cases.

### One compile per profile and flag set

From reading each job's steps and from cargo's JSON messages for the dev builds, on Linux:

| Job | crozier builds |
|---|---|
| `check`, `macos` | One dev (`crozier:build`, then every suite); one instrumented dev (shared tree); `macos` adds one release (`cargo install`) |
| `sdk-env` | One dev |
| `install`, `visual-docs / capture` | One release |
| `live-e2e` | One dev (the cold-registry build, reused by every later step); one release (`tests/live_e2e/run.sh`); plus `corpus-match:test-cold-handoff`'s fixture, a different build (see above) |
| `package` | One release (maturin); one dev (`cargo publish --dry-run`, compiling the packaged tarball) |
| `pool-maintenance` | One dev and one with `overflow-checks` off: two flag sets, the second being what its budget prunes. It runs only on the release pull request |

### What stays slowest

Historical, from CI run [41822525024](https://github.com/nickderobertis/crozier/actions/runs/41822525024) (change request 762), task seconds at base. These do not reflect this change.

| Leg | Slowest tasks (s) |
|---|---|
| Linux check | `surface-census:test-census` 1163, `fern-goldens-weekly:test` 732, `crozier-e2e:test` 714, `witness-search:test-acquisition` 478 |
| Windows check | `surface-census:test-census` 3237, `crozier-e2e:test` 2266, `witness-search:test-acquisition` 506, `witness-search:test-github` 437 |
| macOS | `surface-census:test-census` 3145, `crozier-e2e:test` 1770, `fern-goldens-weekly:test` 1207, `witness-search:test-github` 570 |
| Linux live-e2e | `corpus-match:test-offline` 1774, `test-match` 1396, `test-strict` 1294, `live-e2e:test` 1207 |

Measured here, one `discord_com_matches_fern_output` takes 153.6 s while its `crozier generate` takes 15.2 s in debug and 5.7 s in release: most of a large golden's time is its comparison, compiled at opt-level 0, not repeated work. The corpus-match targets repeat one another's byte comparison by design: the offline proof must really run, since a replay proves nothing about the network.

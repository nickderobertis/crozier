## What

The weekly Fern goldens workflow's `decide` job now finishes on a standard
`ubuntu-latest` runner, and its log says how far it got as it goes.

- `weekly.py decide` writes one line when each comparison starts and one when
  it ends, with its elapsed time and verdict. Each line also gives the free
  disk and available memory. Lines are flushed as they are written, so a runner
  that dies mid-step still leaves them.
- The job runs `weekly.py resources --before <step>` before bootstrap, apply
  and build.
- Per-item comparisons run one per CPU, in planned order. A new one starts
  beside a running one only while 6 GiB is still available (`--reserve-gib`).
  Available memory is read through any cgroup limit around the job, since
  `/proc/meminfo` shows the host inside a container.
- The corpus gate runs summary-only (`CROZIER_DIFF_SUMMARY_ONLY=1`). The
  decision and the pull request say that its reports carry no text diffs, and
  that `just fixtures-diff <corpus>` prints them.
- `apply` runs `just departures-ledger` over the laid-down references. When the
  recipe refuses, main's ledger is kept. A changed ledger row, or a refusal,
  makes the run a diff, never a match. A corpus whose only processing failure
  is ledger drift counts as a difference, reported as "ledger drift: N row(s);
  files not compared", not as a comparison that could not run.
- A reproduced known upstream Fern failure, which has no golden, goes through no
  per-item corpus gate. It is named as "known Fern failure reproduced".
- Splitting the crozier-e2e family report over the 1,080 items is indexed. It
  took 18 minutes before and takes 2.3 seconds now, with the same excerpts.
- The weekly artifacts move to schema 5 (golden `tools/fern-goldens/tests/golden/weekly-v5`).
  The minutes reader (`.github/fern-goldens-budget.mjs`) reads the plan at 5.
- Publication refuses a carried ledger file when a link sits inside the decision
  artifact, and no longer when one sits above it. macOS temporary directories
  are under `/var`, which is a link to `/private/var`.
- The journeys that pin CPU affinity or reserve memory skip on any platform
  other than Linux. Linux is the only platform that reports those, and
  `ubuntu-latest` is where the weekly workflow runs.

## Why

Run 41564405289 died twice in "Decide with crozier's own comparison", 33m07s
and 28m49s into the step, with nothing in its log. The runner itself shut down,
so the upload of the decision never ran either.

### The limits

GitHub's runner reference
(https://docs.github.com/en/actions/reference/runners/github-hosted-runners,
"Standard GitHub-hosted runners for public repositories") gives `ubuntu-latest`
4 CPUs, 16 GB RAM and 14 GB SSD. The runner image's own readme says nothing
about free disk, so the 14 GB is the disk budget used here.

### How it was measured

Every run below is a container held to those limits (`--memory 16g
--memory-swap 16g --cpus 4`, with 4 pinned CPUs). It ran the job's steps from
rustup onward over run 41564405289's `fern-goldens-bundle`. Memory comes from
the cgroup, sampled every 2 s with `memory.peak` and `memory.events` read at the
end. Disk is `du` of HOME plus `/tmp`, sampled about every 4 s (858 samples
over the 58.4-minute run on 7797af82c).

### Findings

- **Baseline, 784580787b, stopped after 143 of 314 corpus comparisons
  (45.9 min).** Peak anon memory was 5.7 GiB (`bunq.com`) and disk was 5.5 GiB.
  Comparisons ran one at a time at about 19 s each, which is about 100 minutes
  for the corpus alone: past what the 120-minute timeout leaves after setup.
  142 of those 143 were "cannot run". At the new Fern pair the regenerated
  references move departure-ledger sites, and the reporter's ledger check
  failed for each.
- **`netbox.dev` alone, over the regenerated tree.** It hit the 16 GiB cap and
  was OOM-killed after 87 s (`oom_kill 1`). With `CROZIER_DIFF_SUMMARY_ONLY=1`
  the cgroup peaked at 375 MiB, and the report ended in the ledger-drift
  processing failure that discards the text diffs anyway. Over main's committed
  tree its largest process reached a 330,524 kB resident set. Its text diffs
  need more memory than the runner has.
- **Which resource the original job ran out of: memory, likely, not
  established.** In the window where GitHub's runner died, the baseline stayed
  far inside both limits. `netbox.dev` is comparison 170 of 314 run one at a
  time, and the evidence can't show the GitHub run had reached it 29–33 minutes
  in, so this stays "likely".

### The finished tree (7797af82c)

The same capped run on 7797af82c completed every step and wrote its decision.

| | measured | limit | 90% bar |
|---|---:|---:|---:|
| wall time, launch to end | 58.4 min | `timeout-minutes` 120 | 108 min |
| peak memory: working set (`memory.current` − `inactive_file`) | 2.98 GiB | 16 GB | 14.4 GB |
| peak memory: cgroup `memory.peak` (includes page cache) | 4.44 GiB | 16 GB | 14.4 GB |
| peak disk use (HOME + `/tmp`) | 5.66 GiB | 14 GB SSD | 12.6 GB |

- No OOM events (`oom 0`, `oom_kill 0`).
- Step times: bootstrap 6.5 min; apply 12.3 min, mostly the ledger recipe,
  which refused; build 0.1 min; decide 39.2 min. GitHub's own checkout and
  setup actions, about 1.5 min in run 41564405289, are outside this count.
- The decision was a **diff**:
  - Corpus: all 314 compared, 0 matched. 313 were ledger-drift-only, with their
    files not compared. 1 differed: `swagger-petstore-distribution`'s flat
    golden, with real regressions. 0 could not run.
  - The family gates rejected 2 and passed 1, with 544 failing items across the
    families. With the 314 corpora, the decision lists 858 differing items in
    all, and none "not checked".
  - One refusal class changed: `heap-exhausted`'s probe now times out rather
    than reproducing the recorded heap exhaustion.
  - `calorieninjas.com` was named as a known Fern failure reproduced.
  - 2 corpora were not regenerated because their upstream specs are
    unfetchable: `viskit-studio` and `subsloth`.
- No other host measurement was running when it launched. My own test runs used
  other host cores during its first ~15 minutes.

## What a failed run's log now shows

```
fern-goldens-weekly: before apply: disk free 435.1 GiB on /home/runner/work/crozier/crozier, memory available 14.9 GiB
fern-goldens-weekly: decide: 317 comparison(s) to run, up to 4 item comparison(s) at once; disk free 433.6 GiB on /home/runner/work/crozier/crozier, memory available 14.2 GiB
fern-goldens-weekly: comparison 170/317 (corpus `netbox.dev`) started: `env CROZIER_DIFF_SUMMARY_ONLY=1 just fixtures-diff {item}`; disk free 430.1 GiB on /home/runner/work/crozier/crozier, memory available 13.5 GiB
fern-goldens-weekly: comparison 170/317 (corpus `netbox.dev`) ended: reject in 113.2s; disk free 430.1 GiB on /home/runner/work/crozier/crozier, memory available 13.6 GiB
```

These lines are copied verbatim from the capped run on 7797af82c. The free disk
there is the measurement host's, and the memory is the container's cgroup limit.
A comparison that started and never ended is the one the runner died in, and
its start line says what was left as it began.

## Follow-ups (drafted)

- Bound `report_fixture_diffs`' text-diff memory (crozier-e2e), so the weekly
  corpus gate can show text diffs again.
- Batch `ruff format` in the reporter, which starts one process per file.

## Not done here

Proof on GitHub's own runner. A later node dispatches the workflow on `main`
after this merges.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

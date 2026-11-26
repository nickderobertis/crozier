# tools/ci-profile (spike harness)

SPIKE ONLY, on the preserved `spike-windows-lane-breakdown` branch: the
measurement harness the plan `crozier-windows-ci-profiling` starts its durable
`test-profiling` and `runtime-profiling` nodes from. Nothing here lands as is.

- `node tools/ci-profile/ci-profile.mjs run <run-id> [--cache-dir DIR] [--out FILE]`
  reads one run of this branch's `ci.yml` (its jobs, each job's log, and the
  `test-timings-<job>` and `spike-profile-<job>` artifacts) into one JSON
  report: per lane its steps, per-Nx-target seconds with start, end and slot,
  per-test-case seconds (nextest `PASS` lines, pytest `--durations`, Node's spec
  reporter), Nx slot utilisation, the aggregated crozier phase profile, the
  spawn micro-benchmark and the one-`ruff`-per-generation experiment. Fetches are
  cached under `${XDG_CACHE_HOME:-~/.cache}/crozier/ci-profile/<run-id>`, read
  before the network, and refused under 40% of the core rate limit.
- `node tools/ci-profile/ci-profile.mjs local <artifact-dir>` reads the same
  from artifacts already downloaded (`gh run download <id> --dir <artifact-dir>`).
- `spike/spawn-bench.mjs` and `spike/ruff-batch-experiment.sh` are the steps the
  workflow runs after the sweep; `spike/schedule.mjs` replays a report's measured
  task durations under other Nx parallelism and task orders.
- crozier's temporary timers write `CROZIER_PROFILE` files (`src/profile.rs`);
  `CROZIER_SPIKE_RUFF_BATCH=1` formats a generation with one `ruff format`, and
  `=verify` formats both ways and fails on any byte of difference.

# SDK Python-environment tier: run evidence

The e2e journeys that build a generated SDK's virtualenv from PyPI and run
`mypy` or `pytest` in it are named `sdk_env_*` and `#[ignore]`d, so the offline
`just test-e2e` / `just check` never runs them; `just test-sdk-env` runs exactly
them, and CI's `sdk-env` job runs that recipe on every OS and `gate` requires
it. `only_the_sdk_env_tier_builds_the_sdk_python_environment` (offline) holds
every test reaching an environment to that prefix and `#[ignore]`.

Both cached environments, the runtime wire suite's venv and the SDK env, are
built under an OS lock with a ready marker, so concurrent journeys share the
first build rather than race it.

Captured on Linux at commit `ef6118978`, the commit that locked the runtime
venv; the evidence commit adds only this directory. `<repo>` stands for the
checkout path, `<tmp>` for a test's temporary directory.

- [`test-e2e.log`](test-e2e.log) — `just test-e2e`, exit 0: 416 passed, 9
  skipped. No `sdk_env_` journey runs; the one line mentioning `sdk_env_` is
  the offline guard above.
- [`ignored.txt`](ignored.txt) — `cargo nextest list -E 'binary(e2e)'
  --run-ignored only`: the 9 skipped, the six `sdk_env_*` journeys and three
  pre-existing manual aids.
- [`test-sdk-env.log`](test-sdk-env.log) — `just test-sdk-env`, exit 0: each of
  the six `sdk_env_*` journeys runs by name and passes.
- [`test-sdk-env-concurrent-a.log`](test-sdk-env-concurrent-a.log) and
  [`test-sdk-env-concurrent-b.log`](test-sdk-env-concurrent-b.log) — two
  `just test-sdk-env` runs started together with one fresh
  `CROZIER_TEST_ENV_ROOT`, so both race the first build of both environments:
  each exits 0 with 6 passed.
- [`unlocked-runtime-venv-race.log`](unlocked-runtime-venv-race.log) —
  `sdk_env_journeys_survive_concurrent_first_use` against the runtime venv
  builder as it was before the lock (reverted after the run): it fails on uv's
  `A virtual environment already exists`, as it did in 3 of 3 runs.
- [`test-sdk-env-induced-failure.log`](test-sdk-env-induced-failure.log) — the
  same recipe with the scratch passing wire test's expected response changed
  from `widget` to `gadget` (reverted after the run): exit 100, naming
  `sdk_env_fern_refusal_gate_runs_each_wire_test`.

# SDK Python-environment tier: run evidence

The e2e journeys that build a generated SDK's virtualenv from PyPI and run
`mypy` or `pytest` in it are named `sdk_env_*` and `#[ignore]`d, so the offline
`just test-e2e` / `just check` never runs them; `just test-sdk-env` runs exactly
them, and CI's `sdk-env` job runs that recipe on every OS and `gate` requires
it. `only_the_sdk_env_tier_builds_the_sdk_python_environment` (offline) holds
every test reaching the environment to that prefix and `#[ignore]`.

Captured on Linux at commit `41b4e74a2`, the commit that made the split; the
evidence commit adds only this directory. `<repo>` stands for the checkout
path.

- [`test-e2e.log`](test-e2e.log) — `just test-e2e`, exit 0: 416 passed, 8
  skipped. No `sdk_env_` journey runs; the one line mentioning `sdk_env_` is
  the offline guard above.
- [`ignored.txt`](ignored.txt) — `cargo nextest list -E 'binary(e2e)'
  --run-ignored only`: the 8 skipped, the five `sdk_env_*` journeys and three
  pre-existing manual aids.
- [`test-sdk-env.log`](test-sdk-env.log) — `just test-sdk-env`, exit 0: each of
  the five `sdk_env_*` journeys runs by name and passes.
- [`test-sdk-env-induced-failure.log`](test-sdk-env-induced-failure.log) — the
  same recipe with the scratch passing wire test's expected response changed
  from `widget` to `gadget` (reverted after the run): exit 100, naming
  `sdk_env_fern_refusal_gate_runs_each_wire_test`.

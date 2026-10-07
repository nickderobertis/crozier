# sdk-env

- The journeys' code lives in `crates/crozier-e2e`; this project only runs the
  `sdk_env_*` ones other than the runtime wire suite (which is `runtime`'s).
- It reaches that crate through its inputs (`crateSource`, `e2eSource`, and the
  files the journeys read), not through an edge onto `crozier-e2e`, whose own
  reads (the Action, release tooling, docs) would otherwise rerun it. A journey
  that starts reading another path adds it to the `test` target's inputs; so
  do `runtime` and `corpus-match`.
- It reaches PyPI, so it is promoted and never cached: PyPI's answer is not an
  input. CI's `sdk-env` job runs it inside the required `gate`.

# sdk-env

- The journeys' code lives in `crates/crozier-e2e`; this project only runs the
  `sdk_env_*` ones other than the runtime wire suite (which is `runtime`'s).
- It reaches PyPI, so it is promoted and never cached: PyPI's answer is not an
  input. CI's `sdk-env` job runs it inside the required `gate`.

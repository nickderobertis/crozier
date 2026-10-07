# sdk-env

The SDK Python-environment tier: crozier-e2e's `sdk_env_*` journeys
(`#[ignore]`d out of crozier-e2e's own run) that build a generated SDK's
virtualenv from PyPI and run mypy or pytest in it — all but the runtime wire
suite, which is the `runtime` project. The journeys' code lives in
`crates/crozier-e2e`; this project only runs them.

- Promoted out of the affected tier (`tier:promoted`) because it reaches PyPI;
  `just check --sweep` and CI's `sdk-env` job run it, and that job stays inside
  the required `gate`. Never cached: PyPI's answer is not an input.
- Tagged `cost:expensive`: nothing outside the expensive suites may depend on it.

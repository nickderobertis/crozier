# ci

The gate's own drivers and the workflow contracts:

- `gate.mjs` is `just check`: the affected tier against `NX_BASE` (a ref name or
  commit SHA, validated) or the merge base with `origin/main`, or `--sweep`.
- `ci-tier.mjs` is `just ci-check`: which tier a GitHub event owes (the
  release-plz pull request sweeps; other pull requests and pushes to main run
  the affected tier against an explicit base).
- `tests/*.rs` (the `crozier-ci` crate) hold the committed workflows to what a
  pull request cannot exercise; `tests/*.test.mjs` drive the two drivers over
  scratch repositories.

The workflows call recipes, never Nx directly. The module-boundary rule itself is
`scripts/check-project-boundaries.mjs`, a shared script every project's `lint`
runs.

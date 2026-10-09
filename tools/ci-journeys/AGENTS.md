# ci-journeys

- The suites that prove the gate and the workflows against real host tools: the
  node journeys drive the real `just`, Nx, `git` and `cargo` over scratch
  repositories (`tests/support.mjs` builds them from the real `justfile` and
  `tools/ci/*.mjs`), and `release_checkout.rs` runs each Windows release job's
  pre-checkout commands before a real `git` sparse checkout of HEAD. They are a
  project of their own so an edit to the offline workflow contracts in `ci`
  never pays for them; a change to a file they exercise reaches them through
  their `{workspaceRoot}` inputs.
- `release_checkout.rs` reads `release.yml` through
  `tools/ci/tests/support/release.rs`, included by path, so the structural test
  and the journey can never disagree on which steps precede a checkout.

# crozier-test-support

- Test code both the crate's integration tests (`tests/generation.rs`) and the
  e2e suite (`crates/crozier-e2e`) include by `#[path]`: the reader of
  `tests/fixtures/departures-ledger.tsv`, and the parameter-lifting controls
  both suites render (`parameter_controls.rs`). It is a project of its own so either
  consumer's edge to it is declared, and the crate never reaches into the e2e
  crate for it.
- It compiles only inside those test binaries, so its format, lint and tests
  are theirs; this project's `lint` holds its graph edges.

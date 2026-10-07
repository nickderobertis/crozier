# crozier (the crate)

- **Why the project lives in `src/`.** The Cargo package is the repository
  root: `src/` is the path thousands of committed reach-ledger and witness rows
  key on, and `cargo install --path .`, maturin's root `pyproject.toml`,
  `action.yml` and the release archives all build the root manifest. A project
  rooted at `.` would own — and be affected by — every file in the repository,
  so it is rooted here and names the rest of the crate (`Cargo.toml`,
  `templates/`, `assets/`, `tests/*.rs`, `tests/support/`) as inputs in `nx.json`.
- `test` writes coverage profiles into `target/llvm-cov-gate` and reports
  nothing; `workspace:coverage` enforces the floor over them, so run the suite as
  `just test`, not a bare `cargo test`, when the number matters.
- A test that starts reading a new repository path adds it to `crateTestReads`
  in `nx.json`, or a change there will not rerun the suite.

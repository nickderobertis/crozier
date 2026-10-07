# crozier (the crate)

The `crozier` package: the binary, the library, and the crate's own tests (unit
tests here, integration tests in `tests/*.rs`, shared test code in
`tests/support/`). Nx project `crozier` (`src/project.json`, tags `type:crate`).

- **Why the project lives in `src/`.** The Cargo package is the repository
  root: `src/` is the path thousands of committed reach-ledger and witness rows
  key on, and `cargo install --path .`, maturin's root `pyproject.toml`,
  `action.yml` and the release archives all build the root manifest. A project
  rooted at `.` would own — and be affected by — every file in the repository,
  so the project is rooted here and names the rest of the crate (`Cargo.toml`,
  `templates/`, `assets/`, `tests/*.rs`, `tests/support/`) as `crateSource` /
  `crateTests` inputs in `nx.json`.
- **It depends on nothing in this repository** (`type:crate` may depend on no
  project). The docs and fixtures its tests read are inputs, not projects.
- `test` writes coverage profiles into `target/llvm-cov-gate` and reports
  nothing; `workspace:coverage` enforces the floor over them. Run the crate's
  suite as `just test` (or `just nx run crozier:test`), not a bare `cargo test`,
  when the number matters.
- A test that starts reading a new repository path must add it to
  `crateTestReads` in `nx.json`, or a change there will not rerun the suite.

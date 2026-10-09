# crozier (the crate)

- **Why the project lives in `src/`.** The Cargo package is the repository
  root: `src/` is the path thousands of committed reach-ledger and witness rows
  key on, and `cargo install --path .`, maturin's root `pyproject.toml`,
  `action.yml` and the release archives all build the root manifest. A project
  rooted at `.` would own — and be affected by — every file in the repository,
  so it is rooted here and names the rest of the crate (`Cargo.toml`,
  `templates/`, `assets/`, `tests/*.rs`, `tests/support/`) as inputs in `nx.json`.

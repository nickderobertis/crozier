# crozier-e2e

- **Run it through its target** (`just test-e2e`). The binary is the one
  `crozier:build` leaves in the profile directory beside this suite's `deps/`
  (Cargo sets `CARGO_BIN_EXE_crozier` only inside the owning package, so
  `crozier_bin()` looks there); a bare `cargo nextest run -p crozier-e2e` drives
  whatever binary was built last.
- **Paths are repository-relative**: read the tree through `repo_root()`;
  `include_str!` paths are relative to this crate (`../../../docs/...`).
- **The harness runs other projects' tooling** — `corpus_sources.py` for every
  golden, the census and hand-written gates, the Action's scripts. Each is an
  input of this project's `test` (`e2eReads` in `nx.json`): a script the suite
  starts running must be added there, or a change to it never reruns the
  suite; one it stops running comes out, or a change to it reruns the suite
  for nothing.
- `#[ignore]` is not a tiering mechanism here; the `sdk_env_*` journeys (PyPI)
  are the one exception, run by the `sdk-env` and `runtime` projects.

# crozier-e2e

- **Run it through its target** (`just test-e2e`). It runs on the `e2e` profile
  (`Cargo.toml`: crozier at opt-level 2, every check on), and the binary is the one
  `crozier-e2e:build-replay` leaves in that profile's directory beside this suite's
  `deps/` (Cargo sets `CARGO_BIN_EXE_crozier` only inside the owning package, so
  `crozier_bin()` looks there). Under nextest the run's first test copies it to
  `crozier-e2e-pinned/<NEXTEST_RUN_ID>/`, and every test of the run drives that copy,
  so a rebuild mid-run cannot reach it. A bare `cargo nextest run -p crozier-e2e`
  (dev profile) drives whatever dev binary was built last. `sdk-env`, `runtime` and
  the corpus recipes use the same profile, so the job compiles the suite once.
- **Paths are repository-relative**: read the tree through `repo_root()`;
  `include_str!` paths are relative to this crate (`../../../docs/...`).
- **The harness runs other projects' tooling** — `corpus_sources.py` for every
  golden, the census and hand-written gates. Each is an
  input of this project's `test` (`e2eReads` in `nx.json`): a script the suite
  starts running must be added there, or a change to it never reruns the
  suite; one it stops running comes out, or a change to it reruns the suite
  for nothing.
- `#[ignore]` is not a tiering mechanism here; the `sdk_env_*` journeys (PyPI)
  are the one exception, run by the `sdk-env` and `runtime` projects.
- Tooling surfaces with no golden behind them belong in `crates/crozier-tool-journeys`, so an
  edit to them does not pay for this suite.

# crozier-e2e

The binary e2e tier: every journey drives the compiled `crozier` as a
subprocess (`assert_cmd`) over real temp dirs, and byte-compares its stripped
output to the committed Fern goldens in `tests/fixtures/`. A `publish = false`
workspace member holding only `tests/`; its own Nx project, so a change the crate
cannot reach never rebuilds or respawns the binary.

- **Run it through its target**: `just test-e2e` (`nx run crozier-e2e:test`).
  The binary is the one `crozier:build` (`cargo build -p crozier`) leaves in the
  profile directory beside this suite's `deps/` — Cargo sets
  `CARGO_BIN_EXE_crozier` only inside the owning package, so `crozier_bin()`
  looks there. A bare `cargo nextest run -p crozier-e2e` drives whatever binary
  was built last; build first, or use the target.
- **Paths are repository-relative.** Read the tree through `repo_root()`;
  `include_str!` paths are relative to this crate (`../../../docs/...`).
- **The harness runs tooling of other projects** — `tools/corpus/corpus_sources.py`
  for every golden, the census and hand-written-fixture gates of
  `tools/surface-census/`, `tools/fern-goldens/fern-overlay-goldens.sh`, and
  the GitHub Action's scripts. Each is a declared input of this project's `test`
  target (`project.json`); a script the suite starts running must be added there,
  or affected detection will not rerun the suite when it changes.
- `#[ignore]` is not a tiering mechanism here. The `sdk_env_*` journeys are
  the one exception (they need PyPI); the `sdk-env` and `runtime` projects run
  them.
- Every corpus's `unmatched` list is empty; a non-empty one is work in flight
  (see `docs/matching.md`).

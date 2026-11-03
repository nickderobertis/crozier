# surface-reach

- The surface-census scripts' suites that drive a real host toolchain: the
  scoped `fixtures-coverage` recipe (real `cargo nextest` selection, real
  instrumented `cargo llvm-cov`), the hand-written reach recipe (an
  instrumented crozier build over temporary fixtures), golden-reach against
  the real `llvm-profdata`, repin composition over a tiny dependency-free Rust
  workspace (real CLIs and instrumentation, without the corpus build), and the
  instrumented-measurement lock across every measuring entry point (real `just`
  recipes, a stand-in `cargo`). They are a project of their own so the offline
  census tests stay cheap; each reads the surface-census scripts it exercises
  through its inputs. A census suite that needs the built crozier or `ruff`
  lands here, never in `surface-census`.
- Its edge onto crozier-e2e (it instruments that suite) is one the
  module-boundary rule admits only under `measures:crozier-e2e`. The two
  instrumented targets run one at a time (`parallelism: false`): they share
  cargo's build directory.

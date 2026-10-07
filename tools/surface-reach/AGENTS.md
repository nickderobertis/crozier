# surface-reach

- The surface-census scripts' suites that drive a real host toolchain: the
  scoped `fixtures-coverage` recipe (real `cargo nextest` selection, real
  instrumented `cargo llvm-cov`), the hand-written reach recipe (an
  instrumented crozier build over temporary fixtures), and golden-reach against
  the real `llvm-profdata`. They are a project of their own so the offline
  census tests stay cheap; each reads the surface-census scripts it exercises
  through its inputs.
- It builds and instruments crozier and crozier-e2e to measure them, hence the
  `measures:crozier-e2e` tag the module-boundary rule allows. The two
  instrumented targets run one at a time (`parallelism: false`): they share
  cargo's build directory.

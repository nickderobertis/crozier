# surface-census

- **Two edges into the Rust suites, both deliberate.** crozier-e2e's harness
  runs the census, golden-reach, the hand-written gate and probe isolation (they
  are inputs of `crozier-e2e:test`); and the census and reach suites read the
  crate's and the e2e suite's sources to measure them — hence the
  `measures:crozier-e2e` tag the module-boundary rule allows.
- The suites that build crozier instrumented or run the coverage toolchain
  (`fixtures-coverage`, `handwritten-reach`, the real `llvm-profdata` case) are
  the `surface-reach` project's, so an edit to an offline census script never
  pays for an instrumented build.
- The census suites run under `scripts/census-python.sh`, never a bare
  `python3`, so a foreign virtualenv cannot answer for this repository.
- The measurement recipes (`just fixtures-coverage`, `golden-reach`,
  `handwritten-reach`, `surface-census`, `apis-guru-gap-screen`) are scripts,
  not gate targets.

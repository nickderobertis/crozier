# surface-census

- **Two edges into the Rust suites, both deliberate.** crozier-e2e's harness
  runs the census, golden-reach, the hand-written gate and probe isolation (they
  are inputs of `crozier-e2e:test`); and this project's reach suites build and
  instrument crozier and crozier-e2e to measure them — hence the
  `measures:crozier-e2e` tag the module-boundary rule allows.
- The census suites run under `scripts/census-python.sh`, never a bare
  `python3`, so a foreign virtualenv cannot answer for this repository.
- The measurement recipes (`just fixtures-coverage`, `golden-reach`,
  `handwritten-reach`, `surface-census`, `apis-guru-gap-screen`) are scripts,
  not gate targets.

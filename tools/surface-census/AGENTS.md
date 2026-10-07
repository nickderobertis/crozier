# surface-census

The OpenAPI surface census (`openapi-surface-census.py`, also the repository's
one document reader) and the measurements built on it: golden reach
(`golden-reach.py`, `golden-reach-search.py`), fixtures coverage
(`fixtures-coverage.sh`, `fixtures-coverage-report.py`), the hand-written
fixture gate (`handwritten-fixtures.py`), the region keys
(`witness-search-region-keys.py`), the APIs.guru gap screen, residual
attribution and probe isolation. Tests and their data are in `tests/`.

- **Two edges into the Rust suites, both deliberate.** crozier-e2e's harness
  runs the census, golden-reach, the hand-written gate and probe isolation (they
  are inputs of `crozier-e2e:test`); and this project's reach suites build and
  instrument crozier and crozier-e2e to measure them — hence the
  `measures:crozier-e2e` tag the module-boundary rule allows.
- `test-reach-portable` reruns `golden_reach_test.py` with
  `tests/without-posix-modules` first on `PYTHONPATH`, as Windows lacks `fcntl`.
- The census tests run under `scripts/census-python.sh` (never a bare
  `python3`), so a foreign virtualenv cannot answer for this repository.
- Measurement recipes (`just fixtures-coverage`, `golden-reach`,
  `handwritten-reach`, `surface-census`, `apis-guru-gap-screen`) are scripts, not
  gate targets.

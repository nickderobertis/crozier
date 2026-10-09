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
- The census suites run under the workspace's locked environment
  (`uv run --locked`) in the gate and the census recipes under
  `scripts/census-python.sh` (which honours that `.venv` first), never a bare
  `python3`, so a foreign virtualenv cannot answer for this repository.
- **`test-reach` and `test-reach-portable` keep their own runner** (a departure
  from `languages/python.md`'s pytest): they run `golden_reach_test.py` as
  `__main__` under `coverage run` rather than through pytest. Its in-process
  calls into `golden-reach-search.py` fan out to a `ProcessPoolExecutor`, whose
  workers (spawn on macOS and Windows, forkserver on Linux from Python 3.14)
  re-import the parent's `__main__`; only this suite run as `__main__` registers
  the hyphen-named script's module for them, and under pytest 20 cases fail with
  `BrokenProcessPool`. Coverage is still measured and combined like every other
  suite's.

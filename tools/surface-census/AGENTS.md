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
- **Name the repin.** A census check that compares a measured table names `just
  census-repin` in its message (`REPIN` in the census suite). The fast offline
  checks only compare, never measure. A scoped run (`--tests`,
  `--fixtures`) leaves the arm sections and the coverage headline alone: a
  subset of the witnesses cannot restate them.
- Every instrumented build or run holds `instrumented-measurement.lock` under
  the host cache, including one started by hand:
  `flock "${XDG_CACHE_HOME:-$HOME/.cache}/crozier/instrumented-measurement.lock" <command>`.
  Never hold it around `crozier-e2e:test`: `growing_reports_keep_peak_memory_bounded`
  takes it itself and would wait forever.
- Readings kept between cases are keyed by the bytes read, and
  `reuse_staleness_test.py` holds them to that. A case that rebinds a script's
  globals takes `fresh_script`, not `load_script`.

- Re-read the named Rust decision against its Python port before
  `just census-repin --confirm-port NAME`, even for a local rename.

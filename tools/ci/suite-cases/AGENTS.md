# suite-cases

- `pins/` holds each sped-up suite's collected cases, taken from the base tree, so
  a speed-up cannot lose a case unnoticed. A deliberate change to a pinned suite's
  cases re-pins it: `node tools/ci/suite-cases/suite-cases.mjs write NAME`. A suite
  whose cases are pinned keeps new reuse tests out of its own target.
- The pins are Linux collections, so the live comparison runs on Linux only.
- `measures:` tags: it reads the pinned suites' sources to collect them and the
  member manifests to compile them, never their results; those suites stay
  unreachable from every other tooling project.
- `tests/build-reuse.test.mjs` compiles a scratch copy of the real manifests, so
  a feature split between `crozier:build` and a suite's build fails it.
- `corpus-match` is a tier this tooling project may not read, so that suite's pin
  (`checkedBy` in `suites.json`) is checked by its own `test-offline`.

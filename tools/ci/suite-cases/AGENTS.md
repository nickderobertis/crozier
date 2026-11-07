# suite-cases

- `pins/` holds each sped-up suite's collected cases, taken from the base tree, so
  a speed-up cannot lose a case unnoticed. A deliberate change to a pinned suite's
  cases re-pins it: `node tools/ci/suite-cases/suite-cases.mjs write NAME`. A suite
  whose cases are pinned keeps new reuse tests out of its own target.
- The pins are Linux collections, so the live comparison runs on Linux only.
- `measures:` tags: it reads the pinned suites' sources to collect them and the
  member manifests to compile them, never their results; those suites stay
  unreachable from every other tooling project.
- `tests/build-reuse.test.mjs` runs the real build commands in the real tree, whose
  builds are the job's own, so a feature split between `crozier:build` and a
  suite's build fails it and it adds no compile of crozier. Changed inputs are
  proved on a scratch workspace with the same package names.
- `corpus-match` is a tier this tooling project may not read, so that suite's pin
  (`checkedBy` in `suites.json`) is checked by its own `test-offline`.
- `cache-key.mjs` is the runtime input of `test` and, with `python`, of
  `surface-census:test-reuse`: Nx does not hash the host, so a tool, variable or
  file that decides what the suites compile, collect or read belongs there.
  `lint` keys only on Node's version and its files; a file it checks from outside
  this project is a declared input, and a test fails until it is.
  `tests/cache-key.test.mjs` proves other hosts, interpreters and flags take no
  cached result. Files a suite reads go in the target's `inputs`, not there, with
  one exception: both targets run `uv run --locked --all-packages`, so every uv
  member's manifest decides their result. The tooling members' are declared inputs.
  The tier members' are hashed in `cache-key.mjs`, because the boundary rule forbids
  a type:tooling target naming them; such an edit misses the cache but does not make
  these targets affected. A new member belongs in one or the other, and a test fails
  until it is.

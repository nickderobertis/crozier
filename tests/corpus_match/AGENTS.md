# corpus-match

- The offline proof runs `just` recipes with sockets denied, so it runs Nx with
  no socket at all: the daemon off (as the gate keeps it) and plugins loaded
  in-process (`NX_ISOLATE_PLUGINS=false`, since an isolated plugin worker talks
  over one), and it skips the Nx cache so a replay cannot pass for an offline
  run. It moves the ignored corpus caches aside while it runs, so its target
  runs alone (`parallelism: false`).
- **Python checks, and a departure from `languages/python.md`:** this tier's Python
  is a uv workspace member (`pyproject.toml` here) with `format` (ruff format),
  `lint` (ruff check) and `typecheck` (ty), which need nothing beyond the
  workspace. Its `test` keeps its own runner and is not a pytest-with-coverage
  target, and its files are outside the combined Python coverage floor: they are
  harnesses for a suite that needs this promoted tier's toolchain, which the
  check legs computing the floor do not carry. See `docs/python-tooling.md`.

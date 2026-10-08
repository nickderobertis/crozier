# census-fallback

- The parser pin is read from each script's own PEP 723 `dependencies` line and
  installed through uv: the tier is promoted and never cached.
- The committed samples it reads belong to the census
  (`tools/surface-census/tests/data/`), so the expensive tier reads the census's
  data rather than the census reading the tier's.
- `test-runner` drives `run.sh` with a stand-in uv and needs no host tool;
  the one journey through the real uv is `test-install`'s.
- **Python checks, and a departure from `languages/python.md`:** this tier's Python
  is a uv workspace member (`pyproject.toml` here) with `format` (ruff format),
  `lint` (ruff check) and `typecheck` (ty), which need nothing beyond the
  workspace. Its `test` keeps its own runner and is not a pytest-with-coverage
  target, and its files are outside the combined Python coverage floor: they are
  harnesses for a suite that needs this promoted tier's toolchain, which the
  check legs computing the floor do not carry. See `docs/python-tooling.md`.

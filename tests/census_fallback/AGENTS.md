# census-fallback

- The parser pin is read from each script's own PEP 723 `dependencies` line and
  installed through uv: the tier is promoted and never cached.
- The committed samples it reads belong to the census
  (`tools/surface-census/tests/data/`), so the expensive tier reads the census's
  data rather than the census reading the tier's.
- `test-runner` drives `run.sh` with a stand-in uv and needs no host tool;
  the one journey through the real uv is `test-install`'s.
- Python: `format`, `lint` and `typecheck` only. `test` keeps its own runner and
  these files stay out of the combined coverage floor, because its suites need
  uv to install the parser pin.

# corpus

The registered corpus's tooling: the source registry and its committed copies
(`corpus_sources.py`), the remote-ref pins (`corpus_remote_ref_pins.py`), the
fetch (`fetch-corpus.sh`, `corpus-lib.sh`), and the two licence gates
(`corpus-licensing-drift.py`, `licence-rescreening-check.py`). Their tests are
in `tests/`. Its `lint` targets are the `lint-corpus-*` / `lint-licence-*`
checks; its `test` targets their boundary suites.

- **The crozier-e2e harness runs `corpus_sources.py` for every golden** (and
  `corpus_remote_ref_pins.py`), so those two files are inputs of
  `crozier-e2e:test`: a change to either reruns the e2e suite and the tiers
  behind it. A change to any other file here reaches no Rust project.
- `corpus_remote_ref_pins.py` reads documents through the census's reader
  (`tools/surface-census/openapi-surface-census.py`), which in turn imports this
  module: the two are one contract across both projects.
- The shell scripts source the shared `scripts/lib.sh` and find the repository
  root two directories up.
- `corpus-sources vendor|audit` and `fetch-corpus.sh` reach the network and are
  never a gate target.

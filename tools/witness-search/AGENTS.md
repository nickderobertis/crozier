# witness-search

The witness acquisition and screening tooling (`witness-*.py`,
`witness_screen.py`) and the GitHub/Postman/Sourcegraph rate-limit guard every
network call goes through (`rate_limit_guard.py`). Tests are in `tests/`; they
run against loopback servers and stub `fern`, offline.

- **Recorded identities stay as recorded.** `witness_screen.py`'s `STAGE` and
  the index's `HISTORICAL_SCREEN` name the stage as the committed screens record
  it (`scripts/witness_screen.py`), and the archived evidence under
  `docs/openapi-surface/witness-search-*` keeps the commands as they were run.
- No Rust suite runs this project's code, so a change here reaches no Rust
  project. It reads the census (surface-census) and the pin reader (corpus).
- `witness-screen`, `witness-search-local-census` and `quota-status` reach third
  parties and are never gate targets.

# witness-search

- **Recorded identities stay as recorded.** `witness_screen.py`'s `STAGE` and
  the index's `HISTORICAL_SCREEN` name the stage as the committed screens record
  it (`scripts/witness_screen.py`), and the archived evidence under
  `docs/openapi-surface/witness-search-*` keeps the commands as they were run.
- No Rust suite may run this project's code, so a witness
  edit never reruns the crate's tiers. A Rust harness that needs one of these
  scripts declares this project as a dependency instead.
- `witness-screen`, `witness-search-local-census` and `quota-status` reach third
  parties and are never gate targets; so do `population_screen.py acquire`,
  `population_screen.py screen --fetch-licence` and `witness-populations-build.py
  search`.
- `population_screen.py` is the only reader of
  `docs/openapi-surface/witness-search-combination-populations/screen.tsv`; read
  it through `read_screen`, never by splitting lines. Regenerate the record's
  README with `witness-populations-record.py` after the table moves.

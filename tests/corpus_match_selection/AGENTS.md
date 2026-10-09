# corpus-match-selection

- Python: `format`, `lint` and `typecheck` only. `test` keeps its own runner and
  this file stays out of the combined coverage floor, because its suite builds
  and drives the real nextest and crozier.

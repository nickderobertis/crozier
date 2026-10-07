# fern-refusals

- Tests here never build or run crozier; the suite that does (`measure` with
  the real binary) is `fern-refusals-strict`'s, which declares the dependency.
- `measure`, `probe`, `finding` and `confirm` need Fern (and `measure` the
  network); never gate targets. Their tests put `FERN_STUB`, a stand-in `fern`,
  first on PATH instead.

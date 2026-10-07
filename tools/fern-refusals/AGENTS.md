# fern-refusals

- Tests here never build or run crozier; the suite that does (`measure` with
  the real binary) is `fern-refusals-strict`'s, which declares the dependency.
- `measure` (`just fern-refusals-measure`) needs Fern and the network; never a
  gate target.

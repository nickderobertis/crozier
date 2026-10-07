# fern-refusals

The Fern refusal registry's population tables (`docs/fern-refusals/`):
`fern-refusals.py` (`select`, `build`, `check`, `measure`) and its test.

- `StrictMeasurement` builds crozier and drives `measure` with that binary, so
  the crate's sources are inputs of `test`: a crozier change reruns it.
- The suite runs `measure` from a scratch copy holding `scripts/`, this project
  and the witness-search, census and pin-reader trees it loads, by path.
- `measure` (`just fern-refusals-measure`) needs Fern and the network; never a
  gate target.

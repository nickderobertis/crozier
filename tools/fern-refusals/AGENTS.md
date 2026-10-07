# fern-refusals

- `StrictMeasurement` builds crozier and drives `measure` with that binary, so
  the crate's sources are inputs of `test`: a crozier change reruns it.
- The suite runs `measure` from a scratch checkout holding exactly the modules it
  loads (`MEASURE_LOADS`); a module `measure` starts loading goes there and into
  `test`'s inputs together.
- `measure` (`just fern-refusals-measure`) needs Fern and the network; never a
  gate target.

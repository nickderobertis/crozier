# fern-goldens

- crozier-e2e's overlay journeys run `fern-overlay-goldens.sh` (with a stub
  generator), so it and what it loads are inputs of `crozier-e2e:test`.
- Generating goldens needs Docker and the Fern CLI: never a gate target. Only
  `test` (`just test-fern-goldens`, offline) is.

# fern-goldens

- crozier-e2e's overlay journeys run `fern-overlay-goldens.sh` (with a stub
  generator), so it and what it loads are inputs of `crozier-e2e:test`.
- Generating goldens needs Docker and the Fern CLI: never a gate target. Only
  `test` is, here and in `fern-goldens-git` (`just test-fern-goldens` runs both;
  neither reaches the network).
- Tests here run the scripts with stand-in tools; a suite that drives the real
  `git` or `just` belongs to `fern-goldens-git`.

# fern-goldens

The Fern golden lifecycle: `fern-goldens` (the workflow's driver),
`generate-fern-fixture.sh` and the corpus/overlay/refresh wrappers around it,
`golden_overlay.py`, and the boundary suite in `tests/`. Maintenance runs
through the manually dispatched Fern goldens workflow; see
`docs/fern-goldens.md`.

- crozier-e2e's overlay journeys run `fern-overlay-goldens.sh` (with a stub
  generator), so it and what it loads are inputs of `crozier-e2e:test`.
- Generating goldens needs Docker and the Fern CLI: never a gate target. Only
  `test` (`just test-fern-goldens`, offline) is.

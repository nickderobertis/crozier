# fern-goldens

- crozier-e2e's overlay journeys run `fern-overlay-goldens.sh` (with a stub
  generator), so it and what it loads are inputs of `crozier-e2e:test`.
- Generating goldens needs Docker and the Fern CLI: never a gate target. Only
  `test` is, here and in `fern-goldens-git` (`just test-fern-goldens` runs both;
  neither reaches the network).
- Tests here run the scripts with stand-in tools; a suite that drives the real
  `git` or `just` belongs to `fern-goldens-git`.
- A suite that drives a publishing generation (`fern-references.py`, the
  witness screen, `generate-fern-fixture.sh` under
  `CROZIER_CERTIFIED_TREE_PUBLISH=1`) with a stand-in `fern` that writes
  `.fern/metadata.json` sets `XDG_CACHE_HOME` to a scratch directory, or its
  stand-in tree lands in the host's certified-tree store.
- Every Fern entry point takes the host's Fern generation lock under
  `XDG_CACHE_HOME`, so any suite reaching a stand-in `fern` through one sets it
  to a scratch directory too, or it waits on a real Fern run on the same host.
  A new entry point joins `fern-goldens-git`'s `fern_generation_lock_test.py`.
- `fern-references.py check` and `generate` share each family's `validate_*`:
  an input a generation starts reading is validated there, and its path joins
  `fern-references-check`'s test inputs (its trace test fails until it does).

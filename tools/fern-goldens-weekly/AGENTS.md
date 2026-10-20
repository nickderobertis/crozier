# fern-goldens-weekly

- The weekly Fern goldens run's journeys: `tools/fern-goldens/weekly.py`'s
  phases, each in a fresh clone of a bare local remote, over a synthetic tree
  with one reference of each family but overlays. Only `fern`, `docker`, `curl`,
  `just` and `gh` are stood in; crozier's engine is the `crozier` binary
  `crozier:build` leaves in `target/debug/`, which `test` depends on.
- A project of its own so only a change to what it runs (its `{workspaceRoot}`
  inputs) reruns these journeys, never the whole-tree certified-pair scan's
  reach.

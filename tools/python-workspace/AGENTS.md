# python-workspace

- Tagged `type:tooling`, not `type:aggregate`: everything it depends on is
  tooling, and `workspace`'s supply-chain inputs glob every `tools/*/` directory,
  which the boundary rule reads as an edge from that aggregate into this one.
- The denominator is `coverage_gate.py`'s, not coverage's: coverage alone counts
  only files a run touched, so a script no test runs (or an extensionless
  `#!…python` one) would go uncounted.
- `coverage_gate.py` never builds a `coverage.Coverage`: one inside a process
  that is itself measured (as the gate is, under its own suite) stops that
  process's data from being saved. It runs the `coverage` CLI in children.

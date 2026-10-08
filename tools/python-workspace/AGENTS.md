# python-workspace

- The Python tooling's one aggregate, tagged `type:tooling` rather than
  `type:aggregate`: everything it depends on is tooling, and `workspace`'s
  supply-chain inputs glob every `tools/*/` directory, which the boundary rule
  reads as an edge from that aggregate into this one. `coverage` combines the data every tooling
  project's `test` targets write under `.coverage-data/<project>/<target>/` and
  holds the union to the floor `AGENTS.md` records (`coverage_gate.py`). It
  depends on every tooling project's `test` through `implicitDependencies`, so
  adding a tooling project means adding it there, to the root `pyproject.toml`'s
  workspace `members` and coverage `source`, and giving it the four uniform
  targets; `tests/workspace_test.py` fails until all three agree.
- The denominator is the gate's, not coverage's: `coverage` alone discovers only
  `*.py`, so an extensionless `#!...python` script no test runs would go
  uncounted. Keep that discovery in `coverage_gate.py`.
- Its own `test` also holds the root manifest to the maturin-built `crozier`
  distribution and the tooling ruff to `.ruff-version`.

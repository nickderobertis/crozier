# Python tooling

crozier is a Rust CLI, but the evidence it rests on — which corpus documents,
licences and witnesses count — is decided by Python under `tools/` and
`screenshots/`. That Python is held to the same strict gate as the crate:
formatted, linted, type-checked and tested with measured coverage, every check
failing on any finding.

## Layout

- **One uv workspace, one lock.** The root `pyproject.toml` declares the
  workspace (`[tool.uv.workspace] members`) and every Python Nx project has its
  own `pyproject.toml` beside its `project.json`, resolved by the single root
  `uv.lock`. `just bootstrap` (via `just sync-python`) installs it into `.venv`
  on Python 3.14; every Python target runs through `uv run --locked`.
- **The root manifest is still the published distribution.** Its
  `[build-system]` (maturin), `[project]` and `[tool.maturin]` are the `crozier`
  wheel's; the uv, ruff, ty, pytest and coverage tables below them are read by
  no build backend. `[tool.uv] package = false` keeps uv from compiling the crate
  into the tooling venv. No member publishes anything (no `[build-system]`,
  `package = false`), so none needs typed packaging.
  `tools/python-workspace/tests/workspace_test.py` holds both.
- **Tooling projects** (`type:tooling`): every `tools/*` project holding Python,
  `screenshots`, and `python-workspace`. Each declares `format` (`ruff format
  --check`), `lint` (its existing lints plus `lint-ruff`: `ruff check`),
  `typecheck` (`ty check`) and `test` (pytest with coverage on).
- **Promoted tiers** (`census-fallback`, `corpus-match`, `live-e2e`, `runtime`)
  are workspace members with `format`, `lint` and `typecheck` only; see the
  departures below.

## Tests and the coverage floor

A tooling project's `test` (or its `test-*` pieces, split by what each reads,
with `test` a no-op over them) runs `pytest --cov --cov-report=` over its suite
with `COVERAGE_FILE=.coverage-data/<project>/<target>/.coverage` — the target's
declared output, so a cache hit restores it. pytest collects the existing
unittest-style suites as they are. Coverage is configured once in the root
`pyproject.toml`: `parallel` and `relative_files`; `patch = ["subprocess"]`,
which measures the scripts the suites drive as subprocesses (how most of them
are driven); `include` patterns rather than `source` directories, because many
suites run a *copy* of a script from a scratch root laid out like the
repository, which `[tool.coverage.paths]` folds back onto the real file; and
`omit` for the test files.

`python-workspace:coverage` depends on every tooling project's `test`, combines
the data, and holds the union to one floor (`coverage_gate.py`, `--fail-under`
in its target). Its denominator is every Python source file under each project
directory the `[tool.coverage.paths]` entries name first, `*.py` and
extensionless `#!…python` scripts alike, whether or not any test runs it; only
the test files under `tests/` are omitted. It runs the `coverage` CLI in child
processes: a second `coverage.Coverage` inside a measured process stops that
process's own data from being saved, which once hid the gate's own runs from its
suite. The floor and the measurement it rests on are recorded in `AGENTS.md`.

## ruff and ty

- **The tooling ruff is the generation ruff.** `uv run` puts `.venv/bin` first on
  PATH, and crozier shells out to the first `ruff` there to format what it emits.
  A tooling ruff of any other version would silently change what a tooling
  suite's `crozier generate` produces, so the dev group pins `ruff==` exactly
  `.ruff-version`, and `python-workspace:test` fails when they differ.
  `.ruff-version` leads: it moves for byte parity with Fern, never for linting.
- **Rules** (root `[tool.ruff.lint]`): pycodestyle, pyflakes, isort, bugbear,
  pyupgrade, simplify, comprehensions, pie, ruff's own, and the injection and
  unsafe-deserialization `S` rules. Line length 120, owned by the formatter.
- **ty** checks at Python 3.11 (see below). `extra-paths` names the directories
  whose modules other projects put on `sys.path` at run time;
  `allowed-unresolved-imports` names the two modules that are deliberately absent
  from the venv (`ruamel.yaml`, the census fallback's PEP 723 pin, whose absence
  a suite asserts; `fern`, the SDK the runtime suite generates). Every
  `ty: ignore` and `cast` carries its reason on the line above.
- **Excluded paths.** Fern's vendored output and probe expectations
  (`tests/fixtures/`, `docs/`), `assets/core`, `assets/scaffolding` and
  `templates/` are excluded from ruff and ty even on a whole-tree run; no Python
  project contains them.

## Measuring

`just test` (or `just nx run python-workspace:coverage`) runs every tooling
suite and the gate. To read the per-project split after it:

    uv run --locked --all-packages python tools/python-workspace/coverage_gate.py --fail-under 88 --by-project

The projects holding only suites (corpus-fetch, fern-goldens-git,
fern-refusals-strict, llmlint-resolution, surface-reach, witness-search-git) count
toward the projects whose scripts they drive. Beyond the two files the floor's
record names, the largest gaps at the recorded measurement were
`golden-reach-search.py` (282 lines missed), `fern-goldens` (124, the Docker/Fern
lifecycle), `golden-reach.py` (94) and `handwritten-fixtures.py` (87).

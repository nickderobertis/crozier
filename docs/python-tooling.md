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
suite. The floor and the measurement it rests on are recorded in [Floor](#floor).

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

## Departures from `languages/python.md`

- **Source valid on 3.11; the venv runs 3.14.** Recipes, the promoted tiers and
  PEP 723 `uv run --script` stages also run these scripts under the host's own
  `python3`, so ruff's `target-version` and ty's `python-version` are 3.11, and
  the members declare `requires-python = ">=3.11"`. The workspace's
  `requires-python` also steers which interpreter `uv venv` picks for the
  generated-SDK environments the e2e suite builds, so it is not raised to 3.14.
- **Stdlib-only scripts: no Pydantic boundary models, no async clients.** The
  census and witness tooling runs under bare `python3` and inside
  `uv run --script` stages with no installs, and its measurements must not
  depend on a third-party parser's version; boundary validation is the scripts'
  explicit checks, each tested.
- **The promoted tiers' harnesses** keep their own runners (`run.sh`, the e2e
  crate's SDK venv) and stay out of the coverage denominator: their suites need
  Prism, PyPI or a release build that the check legs computing the floor do not
  carry. Each tier's `AGENTS.md` records it.
- **`test` is a no-op over `test-*` pieces** where a project's suites read
  different inputs (crozier-nx's split), so a change re-runs only the suite that
  reads it. Each piece is pytest with coverage.

## Floor

**88%**, measured on 2026-10-08 (Linux): **88.60%**, 12408 of 14004 lines across
34 files. It is a floor to ratchet up, not a target; never lower it without a new
measurement recorded here and in `AGENTS.md`.

| project | covered / lines | % |
| --- | --- | --- |
| screenshots | 134 / 138 | 97.10 |
| corpus | 991 / 1063 | 93.23 |
| corpus-licensing | 50 / 50 | 100.00 |
| fern-goldens | 665 / 793 | 83.86 |
| fern-refusals | 746 / 782 | 95.40 |
| llmlint-tooling (`tools/llmlint`) | 245 / 263 | 93.16 |
| python-workspace | 119 / 127 | 93.70 |
| surface-census | 5379 / 6058 | 88.79 |
| witness-search | 4078 / 4730 | 86.22 |

The projects holding only suites (corpus-fetch, fern-goldens-git,
fern-refusals-strict, llmlint-resolution, surface-reach, witness-search-git)
count toward the projects whose scripts they drive.

Two files are 0% in this tier by structure (526 lines):
`tools/witness-search/witness-search-recensus.py`, whose suite needs ruamel.yaml
at the census fallback's pin and runs in the promoted census-fallback tier (the
pin stays out of the workspace venv because the golden-reach suites assert the
refusal when it is absent); and `tools/surface-census/probe-differential-isolation.py`,
which only the Rust e2e harness drives, under a bare `python3`. Without them the
rest measures 92.06%. The largest other gaps: `golden-reach-search.py` (282 lines
missed), `fern-goldens` (124, the Docker/Fern lifecycle), `golden-reach.py` (94),
`handwritten-fixtures.py` (87).

**Platforms.** The floor holds on the Linux and macOS check legs and in the
sweep. The Windows check leg excludes `python-workspace` (ci.yml's Check step),
so every tooling suite still runs there but the aggregate does not: the suites
skip their POSIX-only cases on Windows (stub binaries are shell scripts), so its
number would be lower, and it has not been measured.

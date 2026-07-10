# Matching Fern's output

crozier's contract: **its generated Python, with comments stripped, is
byte-for-byte identical to Fern's**, for the same OpenAPI input and the same
naming. This doc explains how that is verified, what is matched today, and the
known gaps.

## Why the fixtures are what they are

crozier consumes an **OpenAPI document** — nothing else. Fern can be driven from
either its own definition files or an OpenAPI document, and the two produce
*structurally different* SDKs (the definition carries a package/namespace layout
that a plain OpenAPI document does not). So the golden fixtures must be Fern's
output **generated from OpenAPI**, or the target would be unreachable by design.

Two fixture sources, both Fern's real output (Apache-2.0, see `NOTICE`):

- **Offline corpus** — Fern commits Python SDK snapshots for its OpenAPI-sourced
  test APIs (the `*-openapi` seeds). These need no Docker, are reproducible, and
  gate on every run. `query-parameters-openapi` is the first one vendored.
  Refresh with `just fixtures-refresh` (pins a Fern commit; see
  `scripts/fixtures-refresh.sh`).
- **Exhaustive target** — the broad `exhaustive` spec the project aims at. Fern's
  committed `exhaustive` Python output is *definition*-derived, so it is **not** a
  valid OpenAPI target. Producing the true OpenAPI-derived output requires running
  Fern's generator, which only runs under a container runtime. Do that on a
  machine with Docker via `scripts/generate-fern-fixture.sh` (it scaffolds a Fern
  workspace around the vendored `tests/fixtures/exhaustive/openapi.yml`, runs the
  Python generator locally, strips comments, and installs the fixture). Wire the
  resulting files into the manifest below as generation lands.

## How the comparison works

The e2e (`tests/e2e.rs`) runs the compiled binary over a fixture's `openapi.yml`,
strips comments from crozier's output with the **same** stripper that produced
the committed fixtures (`crozier::strip_python_comments`, exposed as
`crozier internal-strip`), and asserts equality against
`tests/fixtures/<api>/expected/**`. Comment stripping is the *only* normalization
— everything else must match exactly.

## The matched manifest (source of truth)

`MATCHED` in `tests/e2e.rs` lists the files byte-matched today. It grows as
generation lands; a file is only added once it matches exactly.

Currently matched for `query-parameters-openapi`:

- `src/seed/version.py`
- `src/seed/py.typed`
- `src/seed/types/user.py`
- `src/seed/types/nested_user.py`

The full expected tree is committed under `expected/` even where not yet matched,
so the finish line is explicit and progress is measurable.

## What generates today

Named `components.schemas` → the Python type layer: pydantic **objects**
(optional/required fields, `= None` vs `pydantic.Field(default=None)` for
described fields, reserved-name aliasing via `typing_extensions.Annotated` +
`FieldMetadata`), string **enums**, and **union/scalar aliases**. Imports are
emitted in Fern's exact two-group order (stdlib `import`s/`from`s, then
everything else). `version.py` and `py.typed` are complete.

## Known gaps (roadmap)

1. **ruff-formatted line wrapping.** Fern runs `ruff format` over its output, so
   long lines (e.g. aliased `Annotated` fields, wide unions) are wrapped. crozier
   emits unwrapped lines that match only when short. Matching the wide cases needs
   a ruff-compatible line-wrapper (in Rust — no runtime Python dependency). This is
   why the exhaustive object files are not yet matched. Until then, keep matched
   files to those with no wrapping.
2. **Inline-schema hoisting.** Fern names and hoists inline request/response
   schemas (e.g. `SearchResponse`, `SearchRequestNeighbor`). crozier only emits
   named component schemas, so `types/__init__.py` and the hoisted types are not
   yet matched.
3. **The client, core, and error layers.** `client.py`/`raw_client.py`, the
   `core/` runtime, and generated errors are not yet emitted. The `core/` files
   are near-static Fern boilerplate and will be reproduced as attributed template
   assets.
4. **Enum member naming / `x-fern-enum`.** The enum template is a first
   approximation and is not in the manifest.

## Coverage note

The gate measures coverage with `cargo llvm-cov --fail-under-lines 95`, which
runs on every CI platform. It cannot run in every sandbox (some restrict the
linker features the LLVM profile runtime needs, and ptrace-based tools need
privileges those sandboxes withhold); when developing in such an environment, run
the rest of the gate and rely on CI for the coverage number.

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

Each `Corpus` in `tests/e2e.rs` carries a `matched` list — the files byte-matched
today for that spec. It grows as generation lands; a file is only added once it
matches exactly.

Currently matched for `query-parameters-openapi`:

- `src/seed/version.py`
- `src/seed/py.typed`
- `src/seed/types/user.py`
- `src/seed/types/nested_user.py`

Matched for `exhaustive` (the OpenAPI-derived fixture from
`scripts/generate-fern-fixture.sh`): `version.py`, `py.typed`, the **entire type
layer** (every `types/*.py` module including the hoisted `typesAnimal` variants,
except `types/__init__.py`), the **entire `core/` runtime** (19 files), each
endpoint client's package marker (`<tag>/__init__.py`), and the per-tag
`raw_client.py` for the **no-request-body tags** (`endpoints_put`,
`endpoints_urls`, `noreqbody`). See the `EXHAUSTIVE` `matched` list in
`tests/e2e.rs` for the exact set.

The full expected tree is committed under `expected/` even where not yet matched,
so the finish line is explicit and progress is measurable.

## What generates today

Named `components.schemas` → the Python type layer:

- **Objects** — pydantic models with Fern's field conventions: required vs
  optional (`nullable` or absent from `required`), `= None` /
  `pydantic.Field(default=None)` / `pydantic.Field()` defaults driven by
  optionality and whether the field is documented, reserved-name aliasing via
  `typing_extensions.Annotated[T, FieldMetadata(alias="wire")]`, and class/field
  docstrings (backslash-escaped, indented).
- **Extensible enums** — an OpenAPI string `enum` becomes
  `typing.Union[typing.Literal[...], typing.Any]`, matching Fern (not an
  `enum.Enum` class).
- **Aliases** — unions (`oneOf`/`anyOf`), maps (`type: object` +
  `additionalProperties`, no properties → `Dict[..]`), nullable scalars
  (`Optional[..]`), and unknown/untyped schemas (`Optional[Any]`).
- **Hoisted inline schemas** — a `oneOf` object variant becomes a named model
  `{Name}{Ordinal}` (`TypesAnimalZero`), an `allOf`'s `$ref` members become its
  base classes, and an inline enum property becomes a named `{Owner}{Prop}` type.

Type mapping follows Fern's OpenAPI importer: `format: uuid`/`byte` → `str`,
`date-time` → `dt.datetime`, `date` → `dt.date`, integer formats → `int`, etc.
Imports are emitted in Fern's exact two-group order (stdlib `import`s/`from`s,
then everything else). `version.py` and `py.typed` are complete.

**Core runtime.** The `core/` SDK runtime (HTTP client, pydantic utilities,
serialization, SSE) is generator boilerplate, not derived from the spec — Fern
ships identical `core/` files into every SDK. crozier vendors them under
`assets/core/` (Apache-2.0; see `NOTICE`) and emits them verbatim, substituting
only the SDK name/version in `client_wrapper.py`.

**Line wrapping.** Fern runs `ruff format` (line length 120) over its output.
crozier reproduces it without a runtime Python dependency: the emitter builds a
[`Doc`](../src/wrap.rs) tree per type expression and `wrap::layout` renders it
with ruff's recursive right-hand-split — keep a statement on one line if it fits,
else explode the outermost bracket, and if the contents still overflow, one
element per line with a trailing comma.

## Known gaps (roadmap)

1. **`types/__init__.py`.** Fern's package `__init__` is a lazy loader
   (`__getattr__` over a `_dynamic_imports` map) re-exporting every type. crozier
   emits the type modules but not yet this aggregator.
2. **Request/response inline-schema hoisting.** Component-schema hoisting is done;
   Fern also hoists inline request/response bodies (e.g. `SearchResponse`,
   `SearchRequestNeighbor`), which arrive with the endpoint layer.
3. **The endpoint layer.** `paths` are now read into an operation IR
   ([`ir::Endpoint`]): module, method name, HTTP method, URL, path params, and
   the success response type. crozier emits each client's package marker
   (`<tag>/__init__.py`) and the per-tag `raw_client.py` for the subset it fully
   supports today — operations with **no request body**, only path parameters,
   and a single JSON 2xx response (a named model or a scalar). A whole module is
   emitted only when every one of its operations is in that subset
   (`Endpoint::emittable`), so output stays honest as coverage widens. Still to
   come, tag by tag: request bodies (`json=request` / inline / the
   `convert_and_respect_annotation_metadata` wrapper and the `content-type`
   header rule), query/header params, error responses (the generated `errors/`),
   the per-tag `client.py` (whose docstrings need a byte-exact example-value
   generator), and the root `client.py`. The two `__init__.py` aggregators'
   import order and gap #2 both depend on the endpoint IR.

## Coverage note

The gate measures coverage with `cargo llvm-cov --fail-under-lines 95`, which
runs on every CI platform. It cannot run in every sandbox (some restrict the
linker features the LLVM profile runtime needs, and ptrace-based tools need
privileges those sandboxes withhold); when developing in such an environment, run
the rest of the gate and rely on CI for the coverage number.

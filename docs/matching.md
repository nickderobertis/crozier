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
except `types/__init__.py`), the **entire `core/` runtime** (19 files), the
**`errors/` package** (a generated exception class per declared error plus its
lazy-loading `__init__.py`), each endpoint client's package marker
(`<tag>/__init__.py`), and the per-tag `raw_client.py` for **every one of the 15
endpoint tags**. That spans the no-request-body tags (`endpoints_put`,
`endpoints_urls`, `noreqbody`), query parameters (`endpoints_pagination`,
incl. array/allow-multiple params in `endpoints_params`), scalar/enum/union `$ref`
bodies via the `convert_and_respect_annotation_metadata` wrapper where needed
(`endpoints_primitive`, `endpoints_enum`, `endpoints_union`), header params
(`reqwithheaders`), inlined object bodies — both `$ref` and inline — hoisted
field-by-field (`endpoints_object`, `endpoints_http_methods`,
`endpoints_content_type`, `inlinedrequests`), container bodies
(`endpoints_container`), unknown (`{}`) and `application/octet-stream` bytes bodies
plus mixed path/query/body operations (`endpoints_params`, `noauth`), and declared
4xx error responses that raise generated exceptions (`noauth`, `inlinedrequests`).
The **high-level per-tag `client.py`** for all 15 tags and the **root `client.py`**
(`FernApi`/`AsyncFernApi`, bearer auth) match too — each wrapper method returns
`_response.data` and carries a worked `Examples` docstring produced by a byte-exact
example-value generator (objects built from their required fields incl. inherited
ones, unions/enums, containers, maps, datetimes, the `long` placeholder; ruff
snippet formatting at line length 88). The project-root **scaffolding**
(`pyproject.toml`, `requirements.txt`, `.fern/metadata.json`) is matched too. See
the `EXHAUSTIVE` `matched` list in `tests/e2e.rs` for the exact set.

Non-Python matched files (the scaffolding) are Fern's verbatim output and compared
without comment stripping; `.py` files are still comment-stripped before the
comparison.

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

1. **The generated docs** (`README.md`, `reference.md`). `README.md` is largely
   static (a usage example plus the exception/advanced sections); `reference.md`
   (~3,800 lines) is a spec-derived per-endpoint reference. Both reuse the
   example-value generator that now backs the per-tag `client.py` docstrings.
   These are the last two of the 104 exhaustive files.
2. **Request/response inline-schema hoisting.** Component-schema hoisting is done;
   Fern also hoists inline request/response bodies (e.g. `SearchResponse`,
   `SearchRequestNeighbor`), which arrive with the endpoint layer.
3. **The endpoint layer.** `paths` are now read into an operation IR
   ([`ir::Endpoint`]): module, method name, HTTP method, URL, path params, and
   the success response type. crozier emits each client's package marker
   (`<tag>/__init__.py`) and the per-tag `raw_client.py` for the subset it fully
   supports today — operations with only path and query parameters, a single JSON
   2xx response (a named model or a scalar), and either no request body or a
   supported one: a `$ref` to a named string enum (`json=request` plus the
   `content-type` header) or a bare scalar (`json=request`, no header; the
   `uuid`/`byte` formats are excluded pending Fern's content-type nuance). Query
   parameters render as keyword-only optional arguments and a `params={...}` entry
   (`endpoints_pagination`); enum bodies as a `request` argument (`endpoints_enum`);
   union bodies through the `convert_and_respect_annotation_metadata` wrapper
   (`endpoints_union`); header params as keyword-only arguments and a `headers={...}`
   entry (`str(x) if x is not None else None`, the `X-` prefix dropped from the
   Python name), which also force the `content-type` header on when they accompany
   a body (`reqwithheaders`). A 2xx response with no content returns `None`. A whole
   module is emitted only when every one of its operations is in that subset
   (`Endpoint::emittable`), so output stays honest as coverage widens. Scalar
   bodies cover every JSON primitive, with `uuid`/`byte` rendered as `str` but
   carrying the content-type header (`endpoints_primitive`). A plain-object `$ref`
   body is *inlined* field-by-field (`endpoints_object`, `endpoints_http_methods`,
   `endpoints_content_type`): every field becomes a keyword-only `= OMIT` argument,
   the call sends `json={...}` mapping wire names to args, request-context
   collections render as `typing.Sequence` (vs `typing.List` in responses),
   reserved names are munged (`long_`, `bool_`, `set_`), object/union-valued fields
   serialize through `convert_and_respect_annotation_metadata`, and a path param
   colliding with a body field is suffixed with `_`. A `$ref` map body passes
   straight through (`json=request`); an inline array of objects goes through the
   convert wrapper with no content-type header. Container bodies (lists/sets/maps
   of primitives or objects) and inline/`$ref`/unknown/`octet-stream` bodies are
   covered, as are declared 4xx responses (each raising a generated `errors/`
   exception) and mixed path/query/body operations. **Every raw client, every
   high-level per-tag `client.py`, and the root `client.py` now match** — the
   per-tag wrappers return `_response.data` and carry a worked `Examples` docstring
   from a byte-exact example-value generator, and the root `FernApi`/`AsyncFernApi`
   aggregates the tag clients under bearer auth. The endpoint layer is complete
   apart from the package `__init__.py` aggregators (gap #1) and the generated docs;
   gap #2 still depends on the endpoint IR.

## Coverage note

The gate measures coverage with `cargo llvm-cov --fail-under-lines 95`, which
runs on every CI platform. It cannot run in every sandbox (some restrict the
linker features the LLVM profile runtime needs, and ptrace-based tools need
privileges those sandboxes withhold); when developing in such an environment, run
the rest of the gate and rely on CI for the coverage number.

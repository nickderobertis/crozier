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
- eight static `core/` runtime assets (`api_error.py`, `file.py`,
  `force_multipart.py`, `query_encoder.py`, `remove_none_from_dict.py`, and the
  three `http_sse/` modules `__init__.py`/`_exceptions.py`/`_models.py`)

This seed pins a **different Fern version** than `exhaustive`, so only the
`core/` assets that are byte-identical between the two Fern versions are matched
here — which is exactly what makes them a useful guard that the vendored
`assets/core/` still tracks upstream.

**`exhaustive` matches all 104 files** — the byte-exact target is reached. This
covers `version.py`, `py.typed`, the **entire type
layer** (every `types/*.py` module including the hoisted `typesAnimal` variants),
the **entire `core/` runtime** (19 files), the
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
snippet formatting at line length 88). The two package `__init__.py` aggregators
(`types/__init__.py`, package-root `__init__.py`), the generated **docs**
(`README.md`, and the per-endpoint `reference.md`), and the project-root
**scaffolding** (`pyproject.toml`, `requirements.txt`, `.fern/metadata.json`) all
match. See the `EXHAUSTIVE` `matched` list in `tests/e2e.rs` for the exact set.

Non-Python matched files (the scaffolding) are Fern's verbatim output and compared
without comment stripping; `.py` files are still comment-stripped before the
comparison.

## Verifying the tool as a user runs it

Byte-matching proves *equality to Fern* for the two corpora. The e2e also covers
the journeys a user actually takes, independent of the golden fixtures:

- **The generated SDK is valid Python.** `assert_valid_python` compiles the whole
  emitted tree with `python -m compileall` — for the `exhaustive` fixture and for
  an **arbitrary spec outside the corpus**. Byte-matching Fern cannot catch a
  generation bug on a spec Fern never saw; compiling can (it first caught an empty
  `from .errors import` emitted when a spec declares no errors). The check skips
  with a message when no Python interpreter is on `PATH` (same posture as the
  coverage tier); GitHub's ubuntu/macos/windows runners all ship one, so the gate
  always runs it.
- **Default naming.** The common bare invocation (no `--package-name` /
  `--project-name`) is exercised: the package directory is `snake_case(title)` and
  `version.py` records the same name.
- **Idempotent regeneration.** Generating twice into the same `--output` prunes a
  module whose schema was dropped from the spec (crozier clears its own
  `src/<package>` tree first) and the result still compiles — no orphaned modules.
- **`--version`.** Asserted against the crate version, the same string the release
  smoke test checks against the published binary.

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

The `exhaustive` corpus is fully matched (all 104 files), and five
feature-coverage targets are **now fully matched too** — `auth-schemes` (42),
`discriminated-unions` (35), `schema-constraints` (33), `integer-enums` (35), and
`form-bodies` (34).
The items below are the remaining generalization gaps — shapes the current specs
do not fully generate — not exhaustive-fixture misses.

The generated **README/reference** now pick the first endpoint with a request body
for the worked example and abbreviate the error-handling/advanced snippets to `...`
(for a fully-required inline body or a container body) or `()` (a body with an
optional field, a union/enum/scalar body, or no body), ruff-wrapped at the 88-col
snippet width. Each gap has a hand-authored **feature-coverage
target** under `tests/fixtures/` (a `FEATURE_TARGETS` corpus in `tests/e2e.rs`),
with the full Fern `expected/` tree committed. Each corpus's `matched` list grows
file-by-file as generation lands; the smoke test also asserts crozier consumes
every spec without panicking regardless of how much is matched. To reproduce the
current output for a target (Fern generated these with the scaffold defaults):

```
cargo build --release
target/release/crozier generate \
  --spec tests/fixtures/<fixture>/openapi.yml \
  --output /tmp/<fixture> --package-name fern --project-name default_package_name
```

1. **Auth models beyond bearer** (`auth-schemes`, partially implemented).
   `components.securitySchemes` plus each operation's `security` now feed an
   [`ir::Auth`] model: the first declared scheme selects the credential, and it is
   *required* when every operation is authenticated (else optional, e.g. exhaustive's
   `noauth`). `client_wrapper.py` is generated from it — api-key (`api_key: str` +
   the scheme's header) and bearer (`token`, required/optional) both match across the
   fixtures, and the bearer-optional form stays byte-identical to Fern's default. The
   auth model is also threaded through the root `client.py` (constructor param, the
   docstring `Parameters` line, and the `Examples` instantiation) and every worked
   `Examples` snippet (per-tag `client.py`, README, reference), so `auth-schemes`
   matches its root + per-tag clients and reference under api-key. Not yet handled:
   basic/OAuth2 primaries (no fixture exercises them; they fall back to the
   optional-bearer wrapper), and cookie-parameters' global-header promotion.
2. **Broader example coverage.** The example-value generator is proven against the
   corpus (objects, unions, enums, containers, maps, datetimes, `long`). Shapes the
   corpus lacks — e.g. a required `date` example, a nameless-slot enum — carry
   plausible-but-unverified placeholders; confirm them as new fixtures land.
   *Integer enums* now generate: a `type: integer` enum becomes a plain `Name = int`
   alias (Fern does not build a `Literal` union for them), and a `$ref` integer-enum
   request body is emittable (`json=request` + content-type header, like a string
   enum) — so `integer-enums` matches its whole `enums` module, root client, and
   reference (only the README example placeholder differs).
3. **Fern's `TYPE_CHECKING` traversal order** in `types/__init__.py` is reproduced
   empirically (the `Types*` types in reverse declaration order, then the rest
   alphabetically). It matches the corpus byte-for-byte; a spec with a different
   type-namespace layout may need the true endpoint-traversal derivation.
4. **Request/response inline-schema hoisting** (`inline-request-response`, partial).
   A component schema used *only* as an inlined (plain-object `$ref`) request body
   is no longer emitted as a standalone type — Fern inlines its fields onto the
   request method and drops the type (verified in `auth-schemes`' `TokenRequest`,
   `schema-constraints`' `CreateAccountRequest`, `servers-webhooks`'
   `CreateSubscriptionRequest`). Still to do: hoisting *inline* (non-`$ref`)
   request/response bodies into new named models (`SearchResponse`,
   `SearchRequestNeighbor`).
5. **Cookie parameters** (`cookie-parameters`). Path, query, and header params are
   emittable; a `cookie` param (`ParameterLocation::Cookie`) puts an operation
   outside today's subset.
6. **Form request bodies (implemented).** `multipart/form-data` splits its fields
   into `data={...}` (non-file) and `files={...}` (`format: binary` → `core.File`)
   with `force_multipart=True`; `application/x-www-form-urlencoded` sends all fields
   via `data={...}` with the form content-type header. `form-bodies` matches in full
   (the reference table reproduces Fern's `core.File` `from __future__` artifact).
7. **Discriminated unions (implemented).** A `oneOf`/`anyOf` with a `discriminator`
   (`propertyName` + `mapping`) becomes Fern's `{Union}_{Variant}` wrapper models —
   each carrying the discriminant as a `typing.Literal[..]` field plus the referenced
   model's other fields — over a `{Union} = typing.Union[..]` alias, and the
   discriminant property is stripped from each member's own model. The type layer
   (`shape.py`, `circle.py`, `square.py`, `types/__init__.py`) matches in
   `discriminated-unions`; the endpoint/docs layer awaits the auth + endpoint work.
   A discriminator without an explicit `mapping` still falls back to a plain union.
8. **Schema annotations and constraints** (`schema-constraints`, mostly matched).
   Fern ignores the validation keywords (`minLength`/`pattern`/`minimum`/`maxItems`/
   …), `default`, and `deprecated` in its generated models, so crozier does too;
   a `readOnly` property is now rendered optional even when `required` (it is
   server-populated), and `additionalProperties: true` maps to
   `Dict[str, Optional[Any]]`. The whole `schema-constraints` type + endpoint layer
   matches (only the README example placeholder differs). Not yet exercised:
   request-vs-response splitting for a `writeOnly` field that is also `required`.
9. **Document-level `servers`/`webhooks`/`callbacks`** (`servers-webhooks`). The
   base URL is hardcoded in the runtime; `servers`, `webhooks`, and `callbacks` are
   absent from the serde model, so multi-server specs and event-driven definitions
   are unsupported.
5. **The endpoint layer (implemented — kept as a reference of the covered
   shapes).** `paths` are read into an operation IR
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
   aggregates the tag clients under bearer auth. The package `__init__.py`
   aggregators and the generated docs (`README.md`, `reference.md`) all match too,
   so the endpoint layer — and the whole `exhaustive` corpus — is complete. Gap #4
   (inline request/response hoisting) is the next generalization step.

## Coverage note

The gate measures coverage with `cargo llvm-cov --fail-under-lines 95`, which
runs on every CI platform. It cannot run in every sandbox (some restrict the
linker features the LLVM profile runtime needs, and ptrace-based tools need
privileges those sandboxes withhold); when developing in such an environment, run
the rest of the gate and rely on CI for the coverage number.

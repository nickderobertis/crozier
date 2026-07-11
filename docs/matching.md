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
matches exactly. After a generator change, `just fixtures-candidates` reports
which committed fixture files crozier now reproduces byte-for-byte but that aren't
yet listed — as ready-to-paste array entries — so growing the manifest is
copy-paste, not a manual tree diff. See [`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md).

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
- **The generated SDK behaves right at runtime.** Compiling proves the source is
  legal Python; it does not prove the *client* issues the right HTTP request or
  parses the response. `generated_sdk_runtime_behavior` generates the `exhaustive`
  SDK and runs the committed driver [`tests/runtime/wire_test.py`](../tests/runtime/wire_test.py)
  against it (in a cached venv holding the SDK's only runtime deps, `httpx` +
  `pydantic`). The generated client accepts an `httpx_client`, so the driver
  injects one whose `httpx.MockTransport` captures the outgoing request and returns
  a scripted response — asserting URL/method construction, bearer-auth and
  `X-Crozier-*` SDK-identity header injection, request-body serialization (wire
  aliasing and `OMIT` filtering), query encoding, typed pydantic deserialization,
  and typed error raising, for the sync **and** async clients. This is the
  in-process analog of Fern's own wire tests — Fern runs a WireMock server in
  Docker and verifies the request via its admin API, but that whole `tests/wire/`
  tree is generated output gated behind an Enterprise `enable_wire_tests` flag that
  none of the corpora set, so crozier does not emit it and reproduces the behavior
  without Docker. Like the validity check it skips when Python/venv/deps are
  unavailable, but is a **hard failure under `CI`** so the gate stays honest.
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
- **String enums** — an OpenAPI string `enum` becomes a real `enum.Enum` class
  (`class Name(str, enum.Enum)`): a `SCREAMING_SNAKE = "value"` member per value and
  a generated `visit(...)` dispatch method. This is Fern's opt-in `enum_type:
  python_enums` shape, which crozier targets and the whole golden corpus is generated
  against (issue #41 gap 2b) — *not* Fern's out-of-the-box open `Literal` union.
  Integer enums stay `Name = int` (`python_enums` does not affect them).
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

**Line wrapping.** Fern runs `ruff format` (line length 120) over its output, so
crozier delegates the wrapping to the same tool. The emitters build each
statement on one line (a small [`Doc`](../src/wrap.rs) expression rendered flat),
and a post-pass ([`pyfmt`](../src/pyfmt.rs)) runs `ruff format` over the generated
`.py` files. `ruff` is therefore a **generation-time dependency**, invoked over
the CLI (not the unstable `ruff_python_formatter` library crates) and pinned in CI
to match Fern's fixtures (the version lives in `.ruff-version`, installed by
`scripts/install-ruff.sh`); its formatter output is byte-identical, on the shapes
crozier emits, across `0.11`–`0.15` (verified by running the e2e under both). The vendored `core/` runtime is left unformatted — it is already
Fern's own `ruff`-formatted source, and reformatting it does not commute with the
comment-strip comparison.

**Aggregator imports.** The lazy-loader `__init__.py` files (`types/`, `errors/`,
the package root) are formatted like any other file, but two artifacts are
normalized on both sides of the e2e comparison (see `normalize_init` in
`tests/e2e.rs`) rather than reproduced: their leading blank lines (a comment-strip
artifact of Fern's multi-line header that a one-line header plus `ruff`, which
caps module-top blanks at two, cannot reproduce), and the order of the
`if typing.TYPE_CHECKING:` import block. That block is never executed, so its
order is meaningless — Fern emits it in traversal order; crozier sorts it
straightforwardly and the e2e canonicalizes both sides with `ruff` isort. The
`_dynamic_imports` map and `__all__` (which *are* executed) stay alphabetical.

**Example snippets.** The worked examples in docstrings/`README`/`reference.md`
are laid out by hand (`Example::render`), *not* through `ruff format`, because
Fern's committed examples are not a `ruff` fixed point: `ruff` reformats a long
`await <call>(...)` by parenthesizing the awaited expression, while Fern leaves
the long `await …(` line and only explodes the call arguments. Reproducing Fern
here means matching Fern, not `ruff`.

## Known gaps (roadmap)

The `exhaustive` corpus is fully matched, and **every** feature-coverage target is
**fully matched too** — `auth-schemes`, `discriminated-unions`,
`schema-constraints`, `integer-enums`, `form-bodies`, `inline-request-response`,
`cookie-parameters`, `servers-webhooks`, the four former gap targets
`basic-auth`, `oauth-client-credentials`, `inline-array-request`, and
`writeonly-fields`, and the two issue-#43 targets `error-responses` and
`sse-streaming`. (The exact matched-file set for each corpus — and the roster of
corpora itself — is the `FEATURE_TARGETS`/`matched` data in `tests/e2e.rs`, the
single source of truth; counts are deliberately not restated here so they cannot
drift.) The items below record how each shape generates; the remaining unproven
paths are called out inline.

### Issue #43: error responses, discriminated-union aliases, and SSE streaming

Three gaps found while checking whether crozier could stand in for a fern-python
SDK. Both real gaps are closed byte-for-byte against a Docker-generated Fern tree;
the third does not reproduce at the corpus's pinned Fern version.

1. **Operations that declared any non-2xx response were silently dropped**
   (`error-responses`, gap #1 — the serious one). crozier emitted the response
   *type* but no client method and wired nothing into the root client, reporting a
   successful generation of an SDK with no way to call the API — every FastAPI-style
   spec (a `422` on every operation) lost every endpoint. The cause was
   [`ir::resolve_errors`] returning "unemittable" whenever an error status was
   unmapped or its body was not an `application/json` `$ref`. Now an error response
   **never** gates method generation: [`ir::error_class_name`] maps every standard
   4xx/5xx status to Fern's typed exception (`404` → `NotFoundError`, `500` →
   `InternalServerError`, …), an unmapped status (a non-standard `460`) is skipped so
   the operation falls through to the generic `ApiError` (exactly as Fern does), and
   the body parses per declared shape — a `$ref` (`Error`), a container
   (`typing.List[str]`), or `typing.Optional[typing.Any]` for a content-less error.
   Still open: an *inline object* error body, which Fern hoists to a root
   `types/{ClassName}Body` model — crozier renders it `typing.Any` today (kept out of
   the corpus, so unmatched rather than wrong).
2. **Discriminated-union alias annotation** (gap #2) is **not a gap at the pinned
   Fern version.** Newer Fern (4.46.x) wraps the alias in
   `typing_extensions.Annotated[Union[...], pydantic.Field(discriminator="…")]`, but
   the corpus pins `fern-python-sdk` 4.34.0, whose OpenAPI importer emits a plain
   `Shape = typing.Union[...]` — which `discriminated-unions` pins and crozier already
   matches. Adopting the annotated form is deferred to a corpus-wide Fern bump (it
   would break the committed 4.34.0 fixture today).
3. **SSE streaming operations were reduced to a `-> None` method** that discarded
   the stream (`sse-streaming`, gap #3). A `text/event-stream` 2xx response now
   ([`ir::is_streaming`]) generates Fern's context-managed streaming shape: the raw
   client is a `@contextlib.(async)contextmanager` over `httpx_client.stream(...)`
   that decodes events through the vendored `core/http_sse` runtime
   (`EventSource.iter_sse`/`aiter_sse`) into
   `typing.(Async)Iterator[typing.Optional[typing.Any]]` chunks, and the high-level
   client yields each chunk with a worked streaming `Examples` block. The chunk stays
   `Optional[Any]`: Fern's OpenAPI importer does not resolve the `x-fern-streaming`
   `chunk-schema-ref` (the same limitation as the OAuth extension), so crozier keys
   off the content type alone and matches Fern's untyped chunk.

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

### Generating a gap target's golden tree

A new gap target ships only `openapi.yml`; its golden `expected/` tree comes from
Fern, whose generator runs only under a container runtime — so the tree is produced
on a Docker host, not in CI. On such a machine:

```
# prerequisites: Docker running, `npm i -g fern-api`, `cargo build --release`
scripts/generate-fern-fixture.sh <fixture>   # writes tests/fixtures/<fixture>/expected/
```

The script scaffolds a Fern workspace around the vendored spec, runs
`fern-python-sdk` (pinned to the same version as the other fixtures — the default
in the script), strips comments with `crozier internal-strip`, and installs the
result as `tests/fixtures/<fixture>/expected/`. Commit that tree, then diff crozier
against it and add each byte-matching file to the fixture's `matched` array in
`tests/e2e.rs` (the e2e starts comparing it immediately). Anything that does not
match is generator work to land next; keep the file out of `matched` until it does.
This is exactly how the four former gap targets (`basic-auth`,
`oauth-client-credentials`, `inline-array-request`, `writeonly-fields`) were closed.

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
   matches its root + per-tag clients and reference under api-key. **HTTP `basic`**
   is now a first-class primary ([`ir::Auth::Basic`]): a required `username`/
   `password` pair (each `str` or callable), the `httpx.BasicAuth(...)._auth_header`
   header wiring, and both credentials threaded through the wrapper, root/per-tag
   clients, and worked examples — `basic-auth` matches in full. **OAuth2** as a
   plain-OpenAPI primary (no `x-fern-*` extensions) produces output identical to the
   optional-bearer fallback, which `oauth-client-credentials` pins in full; a
   token-provider wrapper would need Fern's OAuth extensions, which the OpenAPI
   document does not carry. Still unexercised: an *optional* basic primary (no
   fixture splits basic on `required`).
2. **Broader example coverage.** The example-value generator is proven against the
   corpus (objects, unions, enums, containers, maps, datetimes, a required `date`
   via `writeonly-fields`, `long`) and constructs hoisted tag-scoped element types
   (importing them `from <pkg>.<tag>`, e.g. `inline-array-request`'s
   `ItemsCreateBatchRequestItem`). Shapes the corpus still lacks — e.g. a
   nameless-slot enum — carry plausible-but-unverified placeholders; confirm them as
   new fixtures land.
   *Integer enums* now generate: a `type: integer` enum becomes a plain `Name = int`
   alias (Fern does not build a `Literal` union for them), and a `$ref` integer-enum
   request body is emittable (`json=request` + content-type header, like a string
   enum) — so `integer-enums` matches its whole `enums` module, root client, and
   reference (only the README example placeholder differs).
3. **Fern's `TYPE_CHECKING` traversal order** in `types/__init__.py` is reproduced
   empirically (the `Types*` types in reverse declaration order, then the rest
   alphabetically). It matches the corpus byte-for-byte; a spec with a different
   type-namespace layout may need the true endpoint-traversal derivation.
4. **Request/response inline-schema hoisting (implemented).** A component schema
   used *only* as an inlined (plain-object `$ref`) request body is not emitted as a
   standalone type — Fern inlines its fields onto the request method and drops the
   type (`auth-schemes`' `TokenRequest`, `schema-constraints`' `CreateAccountRequest`,
   `servers-webhooks`' `CreateSubscriptionRequest`). An *inline* (non-`$ref`)
   request/response object body is hoisted into a named model in the **tag's own
   `types/` package** (Fern's `inlined/types/`): a response becomes
   `{Tag}{Method}Response`, a request's nested inline objects
   `{Tag}{Method}Request{Prop}`, and nested inline objects recurse as
   `{Parent}{Prop}` — structural names derived from the operation and property path,
   ignoring any `title`. An [`ir::InlineHoister`] builds these tag-scoped types; a
   location-aware import resolver (`RefLoc`) picks the right relative path from any
   file, and the tag package/`types` package/root `__init__` re-export them.
   `inline-request-response` matches in full. An **inline array body** hoists its
   *element* the same way, as `{Tag}{Method}RequestItem`
   (`inline-array-request`'s `ItemsCreateBatchRequestItem`), so the argument is
   `Sequence[{Ctx}Item]` through the convert wrapper and the worked example
   constructs it, importing it `from <pkg>.<tag>`; the hoisted-type method segment
   preserves the operationId's camelCase ([`ir::endpoint_type_method`]:
   `createBatch` → `CreateBatch`, distinct from the lowercased Python method).
5. **Cookie parameters + global-header promotion (implemented).** A `cookie` param
   (`ParameterLocation::Cookie`) is dropped from the method signature entirely, and
   an **optional** operation header is promoted to a client-wrapper-level "global"
   field (Fern lifts `X-Tenant` → a `tenant` field set once at construction, wired
   through `client_wrapper.py`, the root client, and the worked examples). The
   promotion heuristic is evidence-based: across the corpus the only two operation
   headers split exactly on `required` — `cookie-parameters`' optional `X-Tenant`
   promotes, `exhaustive`'s required `X-TEST-ENDPOINT-HEADER` stays per-method — so
   crozier promotes a header that is optional in every operation it appears in
   ([`ir::global_headers`]). `cookie-parameters` matches in full.
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
   matches (only the README example placeholder differs). When one schema is used as
   *both* request body and response, Fern orders the inlined request signature and
   docstring **required-first** (optional `= OMIT` args last, a stable partition that
   preserves schema order within each group) while the `json={...}` dict keeps pure
   schema order — so a required `readOnly`/`writeOnly` field lands after the plain
   required ones. `writeonly-fields` pins this in full. Not yet exercised: dropping a
   `writeOnly`-only field from the *response* representation (Fern keeps it here).
9. **Document-level `servers` (implemented); `webhooks`/`callbacks` (ignored).**
   When the document declares `servers`, crozier emits `environment.py` (an
   `enum.Enum` of environments) and threads an `environment` / optional-`base_url`
   through the root client, resolving the base URL via a generated `_get_base_url`
   and dropping the hardcoded `base_url` from the worked examples. Fern's OpenAPI
   importer emits a **single** environment member — the first server, named from its
   description (the "2 servers → only `PRODUCTION`" oddity) — which
   [`ir::Environment`] reproduces. `webhooks`/`callbacks` are still absent from the
   serde model (and Fern's OpenAPI SDK does not generate from them), so they are
   ignored; `servers-webhooks` matches in full regardless.
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

## Real-world-spec robustness (issue #40)

The other corpora are hand-authored to have clean, Fern-style `group_method`
operationIds and property names. Real vendor specs are messier, and three shapes
that used to make crozier emit invalid Python or hard-error now generate legal —
and, for the shapes below, byte-matched — output. Each has its own gap-target
corpus (`digit-leading-property`, `operation-id-non-identifier`,
`missing-operation-id`), whose `matched` list is defined in `tests/e2e.rs`.

- **Digit-leading property name** (`2fa_enabled`). [`naming::field_name`] prefixes
  `f_` when the snake-cased name would start with a digit, and the wire name is
  preserved as a `FieldMetadata` alias — byte-for-byte Fern's `f_2fa_enabled`
  (`digit-leading-property/expected/.../types/thing.py`).

- **Non-identifier `operationId`** (`get-all-widgets`, `verify code`).
  [`naming::sanitize_identifier`] coerces any non-`[A-Za-z0-9_]` character in a
  name derived from an operationId to `_`; legal names (every other fixture) pass
  through untouched. The method names snake-case to `get_all_widgets`/`verify_code`
  and the inline response hoists to `VerifyCodeResponse`, matching Fern.

- **Missing `operationId`** (optional in OpenAPI). Instead of hard-erroring,
  [`ir::endpoint_method_name`] synthesizes the method from the route:
  [`ir::synthesized_method_name`] infers a verb from the HTTP method and whether
  the path addresses a collection or an item (`GET /widgets` → `list_widgets`,
  `GET /widgets/{id}` → `get_widget`), matching Fern's route-derived names.

### Tag-based client grouping

Closing the last two required grouping operations by **tag**, as Fern does. Fern's
rule — reproduced in [`ir::endpoint_module`] — is: a `group_method` operationId
names its own client from the prefix (`endpoints_container`, `inlinedrequests`) and
the `tags` are ignored; a groupless operationId (or one with none) is grouped by
its first tag instead (`get-all-widgets`/`verify code`/`GET /widgets` under tag
`widgets` → the `widgets` client). The hoisted-type context comes from the
operationId alone ([`ir::endpoint_pascal_context`]), never the tag, so a tag-grouped
inline response stays `VerifyCodeResponse`, not `WidgetsVerifyCodeResponse`.

### No-auth parity

These specs declare **no security scheme**, so they exercise crozier's
unauthenticated client. [`ir::auth_model`] now returns [`ir::Auth::None`] for such a
document (rather than defaulting to an optional bearer token), and the client
wrapper, root client, and per-tag clients drop every credential parameter and the
`Authorization` header — byte-matching Fern's credential-free clients. The whole
SDK-code layer of all three corpora matches: the types, the tag-grouped raw and
high-level clients, the root client, and the aggregators.

### crozier vs Fern SDK-identity headers

crozier does not impersonate Fern in the generated SDK: it emits `X-Crozier-Language`
/ `X-Crozier-SDK-Name` / `X-Crozier-SDK-Version` where Fern emits `X-Fern-*`. It also
reproduces Fern's *packaged* client wrapper, so it always emits the
`SDK-Name`/`SDK-Version` headers that Fern's publishing metadata supplies — which the
credential-free local golden trees (below) omit. Both are deliberate,
non-behavioral differences in tool branding/packaging, so
`tests/e2e.rs::normalize_sdk_headers` drops the `SDK-Name`/`SDK-Version` lines and
canonicalizes the remaining `X-Crozier-` prefix (the `Language` header) to `X-Fern-`
on both sides before comparison. Every other line of `client_wrapper.py` matches
exactly, so the wrapper is in each corpus's `matched` list.

### What stays unmatched (packaged vs. local Fern output)

The only files the golden trees carry that stay out of the `matched` lists are the
package-root `__init__.py` aggregators (they import `__version__` from a
`version.py` crozier emits but Fern's local output omits). The pure packaging
scaffolding — `pyproject.toml`, `version.py`, `py.typed`, `README.md`,
`reference.md` — is simply absent from the golden trees, so there is nothing to
compare against. This is **not** a crozier defect: crozier reproduces Fern's
*packaged* SDK (a pip package with all of the above), exactly as the auth'd corpora
prove. Fern only writes that packaged form when generating for a registry
(`output.location: pypi`/`github`), which needs publishing credentials; the
credential-free local mode (`local-file-system` → `downloadFiles`) that vendors
these golden trees omits it. (`digit-leading-property` additionally leaves its client
layer unmatched: its `getThing` operation is untagged and groupless, so Fern emits a
root-level method where crozier still nests a single-endpoint client — a separate
root-client gap. Its `f_2fa_enabled` model, the fix under test, matches in full.)

Still open from the issue (tracked, not yet done): hoisting an inline object nested
inside an `array.items` of a *component* schema (dropped to `typing.Any` today —
adjacent to gap #4's request/response hoisting), Swagger 2.0 / fragment-doc
tolerance, and the `address_line_1` → `address_line1` underscore-before-digit
rename.

## Fern-python parity gaps (issue #41)

Issue #41's shape gaps are closed with real Fern golden trees (generated by
`scripts/generate-fern-fixture.sh`, so all are byte-match targets like the rest of the
corpus).

- **Tag-based client grouping** (`tag-based-grouping`). Plain (no `group_method`)
  operationIds `listWidgets`/`createWidget` tagged `widgets` and
  `listGadgets`/`createGadget` tagged `gadgets`. Fern groups by first tag into one
  sub-client per tag (`client.widgets.list_widgets()`), snake-cases the method from
  the operationId, and hoists each inline response to `{Method}Response` in that
  tag's own `types/`. crozier already produced this structure (the #40 grouping
  work); the fixture additionally pinned **sub-client ordering** — Fern lists
  sub-clients in path-**declaration** order (`widgets` before `gadgets`) in the root
  client and `reference.md`, not alphabetically, while the root client's
  `TYPE_CHECKING` imports stay **alphabetical**. crozier now emits both (the earlier
  blanket alphabetical sort was the divergence).
- **Hoisted parameter enums** (`enum-query-param`, issue #41 gap 2a). An inline
  `type: string` enum on a query parameter is hoisted to a named type
  `{Method}Request{Prop}` (`ListWidgetsRequestLevel`) in the tag's `types/` package,
  referenced by name in the client/raw client, rather than inlined at every use site
  ([`ir::InlineHoister::hoist_param_enum`]).
- **Real `enum.Enum` classes (issue #41 gap 2b), the default.** Every string enum —
  a named `components.schemas` enum, a hoisted inline-property enum (`{Owner}{Prop}`),
  or a hoisted parameter enum — renders as `class Name(str, enum.Enum)` with
  `SCREAMING_SNAKE` members and a `visit(...)` dispatch method
  ([`ir::EnumType`]/[`emit::render_enum`]). This is Fern's `enum_type: python_enums`
  mode; the whole golden corpus is regenerated against it
  (`scripts/generate-fern-fixture.sh` passes `pydantic_config.enum_type:
  python_enums`), so exhaustive and every enum-bearing target byte-match the class
  form, and worked examples use member access (`TypesWeatherReport.SUNNY`). The one
  Fern-only artifact this introduces — the `generatorConfig` block Fern writes into
  `.fern/metadata.json` — is normalized out of the comparison
  (`tests/e2e.rs::normalize_metadata`), the same posture as the SDK-identity headers,
  since crozier renders `python_enums` unconditionally and carries no such config.
  (Note this deliberately diverges from Fern's *out-of-the-box* default, which is the
  open `Union[Literal[..], Any]`; per issue #41 real enums are the more useful shape
  and the config unlocks byte-parity with them.)

- **Audience-scoped multi-SDK filtering** (`audience-filter`, issue #41 gap 3).
  `crozier generate --audience <name>` (repeatable) prunes to the operations
  crozier's own `x-crozier-audiences` extension marks for that audience — plus
  operations with *no* audience label, which survive any filter — and emits only the
  **transitive `$ref` closure** of the surviving operations'
  parameter/request/response schemas ([`openapi::filter_by_audience`]). Every other
  `components.schemas` entry, even an unlabelled one no surviving operation reaches,
  is dropped, so each audience SDK is self-contained. crozier brands its own
  extension rather than reading Fern's `x-fern-audiences`, the same way it emits
  `X-Crozier-*` SDK headers where Fern emits `X-Fern-*`; the fixture spec carries
  **both** extensions (identical values) so Fern reads `x-fern-audiences` to produce
  the golden while crozier reads `x-crozier-audiences`. `listWidgets`→`public` and
  `getStats`→`internal`; `--audience public` byte-matches Fern's filtered SDK — the
  `admin` client and the internal-only `Stats` type are gone, `Widget`→`WidgetDetail`
  are kept. The golden tree is regenerated by passing `FERN_AUDIENCES=public` to
  `scripts/generate-fern-fixture.sh` (a group-level `audiences:` filter that acts on
  the spec's `x-fern-audiences`). Property-/schema-level audiences are not yet
  honoured (a follow-up); only operation-level filtering is applied.

All three new fixtures are the *packaged* SDK form (like exhaustive), reproduced with
`fern generate --preview` (see the regeneration note below).

> **Regenerating these golden trees.** `scripts/generate-fern-fixture.sh` pins the
> Fern CLI to the corpus version via `fern.config.json` and installs the *packaged*
> SDK (a pip package: `src/<pkg>/…` + `pyproject.toml` + `README.md`/`reference.md` +
> `.fern/`). It gets the packaged form from `fern generate --preview --output`, which
> — unlike a plain `--local` `local-file-system` run, that emits only the flat module
> tree — writes the full package **and** needs no publishing credentials (a `pypi`/
> `github` output location tries to push and crashes locally). Environment notes:
> (1) `--preview` only emits the package when Fern considers itself authenticated, so
> the script sets a dummy `FERN_TOKEN` (no credential — a non-empty value suffices);
> (2) Fern's generator runs `npm install @fern-api/generator-cli` inside its
> container, so under a TLS-intercepting sandbox the container needs host networking
> and the proxy CA (e.g. a `docker` shim injecting `--network host -v <ca>:/ca.crt -e
> NODE_EXTRA_CA_CERTS=/ca.crt`); (3) on a sandbox whose Docker daemon can't see the
> host `mktemp` dir, point `TMPDIR` at a Docker-visible path.

## Coverage note

The gate measures coverage with `cargo llvm-cov --fail-under-lines 95`, which
runs on every CI platform. It cannot run in every sandbox (some restrict the
linker features the LLVM profile runtime needs, and ptrace-based tools need
privileges those sandboxes withhold); when developing in such an environment, run
the rest of the gate and rely on CI for the coverage number.

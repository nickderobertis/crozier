# Fern 5.20.0 — measured limitations

What `fernapi/fern-python-sdk:5.20.0` **does not do** with an OpenAPI document, as
measured, not as read off a specification. crozier's contract is byte-match with
Fern ([`matching.md`](matching.md)), so a shape Fern discards is a shape no golden
can pin: this file is the record of which shapes those are, so the next person
choosing a fixture does not spend a screen re-deriving it.

The measurements come from four **screens** run on one host on 2026-08-20 — one
each for *serialization*, *auth-and-responses*, *structure-and-media* and
*naming-and-types* — plus the **Round 3** pass that decided what to register from
them. Each screen carried documents from a pinned URL through `fern check` and
then a real local `fern generate`, and cross-checked real documents against
minimal locally authored probes. The screen reports themselves lived in host
scratch outside every repository and are gone; the evidence below is quoted from
them rather than linked, so this file is readable with nothing but this checkout.

**Versions in force for every measurement below:** Fern CLI `5.67.1`
(`fern.config.json`) and generator `fernapi/fern-python-sdk:5.20.0`
(`generators.yml`) — the same pin the corpus goldens record. Runs set
`CI=true`/`GITHUB_ACTIONS=true` to match `scripts/generate-fern-fixture.sh`, which
is why quoted logs carry doubled `::warning::` annotation lines.

## How to read a verdict

Findings are not all the same kind of fact, and the difference decides whether a
future probe is worth running:

| verdict | meaning |
|---|---|
| **implements** | Fern reads the shape and emits output derived from it; registration is warranted only where that behaviour is not already pinned by an existing fixture |
| **discards** | Fern accepts the shape, emits nothing derived from it, and reports nothing |
| **ignores** | Fern emits the node but the modifier under test (a `style`, an `explode`) changes no byte |
| **refuses** | `fern check` exits non-zero on the shape |
| **crashes** | `fern check` passes and `fern generate` fails |
| **coincidence** | Fern's output happens to equal the standard's wire form, produced by an unconditional default rather than by handling the shape |
| **unmeasured** | **an open question**, not a proven absence: no screen probed what Fern emits here, and a probe could still answer it |

A verdict is joined with a qualifier where supply also bore on the outcome:
**supply** (too few verified candidates), **licence** (verified candidates fail the
census licence bar), **pipeline** (crozier's fixture pipeline cannot register the
shape). Those bear on registrability, not on what Fern does.

A **probe** is a minimal, locally authored OpenAPI document isolating one shape.
Probes are evidence about Fern; none is a corpus fixture and none is proposed as
one — the corpus takes real-world specifications only
([`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md)).

## What these measurements do *not* establish

The screens measured **Fern**. None of them built or ran crozier, and none
compared a byte of crozier's output against Fern's. Where this file says what
crozier does beside Fern, it is reading crozier's source and says so — the thing
that settles it is the ordinary end-to-end byte comparison the corpus already
does, not this document.

Two pieces of evidence could not be recovered from the screens and are recorded
as absent rather than reconstructed:

- The serialization screen's probe runner created its Fern workspace with
  `mktemp -d /tmp/fernscreen.XXXXXX` and removed it on exit. For probes whose
  `fern check` failed, the generate stage — the only stage that prints the
  workspace path — never ran, so **the literal inner command path for the
  `header-array` probe is unrecoverable**. Its exit code and full diagnostics were
  captured to files and are quoted below; the path is not invented.
- Every generated SDK tree was deleted at the end of its own run. What survives of
  Fern's output is the extracts quoted here.

## Parameter serialization

The largest finding of the round, and the one that changes what a serialization
fixture is worth.

### Fern branches on the declared `style` in exactly one place

An **array** query parameter declared `style: form` with `explode: false` is
comma-joined. Nothing else in the emitted Python reads `style` at all. Measured on
single-parameter control probes, and reproduced by one operation carrying six
query parameters differing only in style:

| probe | declared | Fern emits |
|---|---|---|
| `form-array-explode-false-CONTROL` | `form`, `explode: false`, array | `"probeParam": ",".join(map(str, probe_param))` |
| `form-array-explode-true-CONTROL` | `form`, `explode: true`, array | `"probeParam": probe_param` (httpx repeated key) |
| `pipeDelimited-array-explode-false` | `pipeDelimited`, `explode: false` | `"probeParam": probe_param` — **not** pipe-joined |
| `pipeDelimited-array-explode-absent` | `pipeDelimited`, explode absent | `"probeParam": probe_param` — **not** pipe-joined |
| `spaceDelimited-array` | `spaceDelimited`, `explode: false` | `"probeParam": probe_param` — **not** space-joined |
| `deepObject-real-object` | `deepObject`, object | `convert_and_respect_annotation_metadata(...)` |
| `pipeDelimited-object` / `spaceDelimited-object` | object-valued | `convert_and_respect_annotation_metadata(...)` — the same call, byte-identical |
| `matrix-array` / `label-array` (path) | `matrix` / `label` | `f"probe/{encode_path_param(probe_param)}"` — no `;` or `.` prefix |
| `matrix-object` / `label-object` (path) | object-valued | `encode_path_param(convert_and_respect_annotation_metadata(...))` |
| `cookie-primitive` / `cookie-array` / `cookie-object` | `in: cookie` | **parameter absent from the generated client** |

Every row above ran `fern check` 0 and `fern generate` 0 unless stated otherwise.

- **`pipeDelimited` and `spaceDelimited` arrays are not joined** — verdict
  *discards*. The declared style leaves no trace in the output.
- **Object-valued query parameters are not style-conditioned at all** — verdict
  *coincidence*. `deepObject`, `form` with `explode` true and false,
  `pipeDelimited` and `spaceDelimited` objects all emit byte-identical code, and
  the runtime `query_encoder.py`'s `traverse_query_dict` then flattens *every*
  dict-valued query parameter to `key[subkey]=value` unconditionally. That wire
  form is what `deepObject` prescribes, so **Fern's `deepObject` output coincides
  with the standard rather than Fern implementing `deepObject` as a style**: it
  produces the same encoding for objects that declare `form`.
- **Path parameters ignore `style` entirely.** `matrix` and `label` emit a plain
  `f"probe/{encode_path_param(probe_param)}"`, `fern check` 0, `fern generate` 0.
  Worse than style-blind: `encode_path_param` is `str(jsonable_encoder(obj))`, so a
  `Sequence[str]` path parameter renders Python's `str(['a','b'])` — a literally
  malformed path segment.

*Beside crozier's source:* crozier's whole style-and-explode rule is the
`comma_separated` predicate in `src/ir.rs` — explode explicitly false, style absent
or `form`, resolved schema an array — which selects the same parameters Fern
comma-joins and falls through where Fern falls through. That reading is inference
from source; only a golden proves it.

### Cookie parameters are dropped from the generated client entirely

Fern emits `Skipping cookie parameter, <name>, in <METHOD> <path>` as a
**warning** — `fern check` still prints `All checks passed` and exits 0 — and the
parameter is then absent from the client. Probe `cookie-primitive`, one operation
with one parameter:

```
$ fern check      → exit 0
[api]: Skipping cookie parameter, probeParam, in GET /probe
All checks passed
$ fern generate --group python-sdk --local --preview --output <tmp> --force   → exit 0
```

Emitted call site: **parameter absent from the generated client.**

Measured **188 times across 32 of the 94 documents** the serialization screen
carried. On `MateEke/picture-frame` the check exits 0 with two such warnings and
the emitted SDK contains zero occurrences of the string `cookie`. A cookie fixture
would pin *"both crozier and Fern emit nothing"*, which is why Round 3 registers
none. crozier drops cookie parameters too (`src/ir.rs`, the
`has_unsupported_params` comment), so the two already agree by construction.

### A `content:`-typed parameter collapses to a bare `str`

Probe `param-content-path` emits `def op(self, probe_param: str, ...)`, losing the
declared JSON object. Verdict *discards*.

### Header parameters: array refuses, object crashes

An **array-typed header parameter fails `fern check`**. Fern synthesizes an
endpoint example for the header using the parameter *name* as a string, then
rejects its own synthesized example against the array schema. Probe `header-array`,
inner `fern check` exit **1** (the wrapper process exits 0 regardless, so the inner
code was captured to a file):

```
[sdk] 1 error
    [error]
        path: probe.yml -> service -> endpoints -> op -> examples[0] -> headers
        issue: Expected example to be a list. Example is: "probeParam"

Found 1 error and 0 warnings in 0.000 seconds.
```

`fern generate` never ran — the runner guards it behind a zero check exit. This is
the same failure [`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md)
records for `jaewook-epcis`, reproduced from first principles on a three-line
specification.

An **object-typed header parameter crashes the generator**. Probe `header-object`:
`fern check` exit **0** (`All checks passed`), `fern generate` exit **1**, tail of
the container traceback:

```
File "/src/fern_python/generators/sdk/declaration_referencers/type_declaration_referencer.py", line 25, in get_filepath
  declaration_fern_filepath = self._types[name.type_id].name.fern_filepath
KeyError: 'type_:ProbeOpRequestProbeParam'
```

### Where the supply ran out, and where it was only test stubs

Six serialization gaps ended **empty**, and the supply is exhausted rather than
unsearched. `matrix-object`, `param-content-path` and `param-content-cookie` each
had one or two candidates carry end to end — short of a primary plus two backups;
`explode-true-simple-header`, `header-array` and `header-object` had none at all.
The screen went past the census's ranked top eight and screened **every remaining
eligible permissively licensed document in the whole 7,137-document census** — six
more, all of which failed `fern check`: `erraggy/oastools` on
`Unsupported OpenAPI version: 3.3.0`, and four `OpenUdon/oas` copies plus
`pb33f/libopenapi` on multipart `is exploded and must be a list` errors.

Four further gaps closed **only on tooling test fixtures** and are therefore not
registrable: `matrix-array`, `label-array-or-object`, `spaceDelimited-object` and
`pipeDelimited-object` each verified, but every candidate is a parser or
code-generator test stub rather than a specification anyone runs an API from — the
"document nobody writes" the real-world constraint exists to exclude — and Fern
discards `matrix` and `label` anyway. The stubs, named so the supply reads as
searched rather than missed:

- `thephpleague/openapi-psr7-validator:tests/stubs/pathParams.yaml`
- `eve0415/oasts:fixtures/{msw-empty-path-3.1,strict-flags-3.1,msw-showcase-3.1}/openapi.yaml`
- `Cornutum/tcases:.../openapi/{styles,normalize-form}.json`
- `micronaut-projects/micronaut-openapi:.../3_0/params-with-style.yml`
- `hey-api/hey-api:specs/3.1.x/rpc-query-styles.yaml`
- `stoicflame/enunciate-openapi:.../arguments/openapi.yml`
- `enorganic/oapi:tests/input-data/parameter-styles.json`

The one non-stub among them,
`on-org/nuxt-openapi-docs-module:playground/docs/openapi/dynamic-query-params.yaml`,
is a real document whose every backup is a stub, so `pipeDelimited-object` cannot
reach a primary plus two backups without them.

## Auth and responses

### The importer drops four security schemes outright

`apiKey` in **query**, `apiKey` in **cookie**, **`mutualTLS`** and HTTP
**`digest`** never reach the generated client. Measured on isolated probes:

| declared security | `fern check` | what Fern generates |
|---|:--:|---|
| `apiKey` in header (control) | 0 | required `api_key: str` → `headers["X-API-Key"]` |
| `apiKey` in **query**, sole scheme, ops secured | **1** | — `Service requires auth, but no auth is defined.` |
| `apiKey` in **cookie**, sole scheme, ops secured | **1** | same refusal |
| `mutualTLS`, sole scheme, ops secured | **1** | same refusal |
| http `digest`, sole scheme, ops secured | **1** | same refusal |
| any of those four declared but **no** operation requires auth | 0 | a **credential-free** client — no `token`, no `api_key`, no `Authorization` |
| unsupported scheme **then** a supported one | 0 | the supported one only; the unsupported scheme leaves no trace |
| `openIdConnect`, sole scheme, all ops secured | 0 | **required** `token: Union[str, Callable[[], str]]` → `Authorization: Bearer` |
| `openIdConnect` with one public operation | 0 | **optional** `token: Optional[...] = None` |
| `oauth2` implicit / password | 0 | `token` → `Authorization: Bearer` (required when every op is secured) |
| operation-level security **alternatives** | 0 | collapses to one credential — the first supported scheme |
| ranged `1XX`/`3XX`/`4XX`/`5XX` response | 0 | **no `errors/` package entry at all**; the operation falls through to `ApiError` |

So for those four schemes **there is no such thing as a specification that
isolates the feature**: declare one alone and Fern refuses the document; declare
one unenforced and Fern emits a credential-free client; pair one with a supported
scheme and Fern generates from the supported one. Every proposed primary in the
screen therefore pairs the unsupported scheme with a supported one.

**`openIdConnect` is the exception in that list** — Fern imports it as a bearer
`token`, required when every operation is secured and optional when one operation
is public. Two independent documents show it:
`gh:questsin/UBC-Rogers-CAMARA-Hackathon:API/sim-swap.yaml` (sole scheme, all ops
secured) and `gh:tractionguest/guest-api:openapi.yml` (MIT, 43 ops, all secured),
both exit 0 at both stages and both emit a **required** token.

*Beside crozier's source:* `auth_model` in `src/ir.rs` selects the first header
`apiKey`, http `bearer`/`basic`, or `oauth2` scheme and falls through to
`_ => Auth::Bearer { required: false }`; it returns `Auth::None` only when the
scheme map is *empty*. Read against the two rows above, an openIdConnect-only fully
secured document and an unenforced-unsupported-scheme document both look like
divergences. Inference from source — no screen ran crozier.

### The four `http-digest` witnesses, and why none can be registered

`http-digest` is the one dropped scheme whose whole verified supply fails the
licence bar rather than failing Fern, so the four documents are named here with
their measurements — the supply is exhausted, and re-searching it would repeat
this. Every one carried from its pinned URL through both stages at exit 0, with
`digest` declared and absent from the client:

| witness | `check` | `generate` | declared | credential Fern emitted | licence bar |
|---|:--:|:--:|---|---|---|
| [`mongodb/openapi:openapi/v2/private/openapi-private-preview-sql-interface.yaml`](https://raw.githubusercontent.com/mongodb/openapi/44ea8293091ddf05272f6ef9bf73637a3833cbbe/openapi/v2/private/openapi-private-preview-sql-interface.yaml) | 0 | 0 | `DigestAuth: http/digest` + `ServiceAccounts: oauth2/clientCredentials` | required `token` → `Authorization` (47 files, 9 types, 7 error classes) | specification declares CC BY-NC-SA 3.0 US |
| [`mongodb/openapi:openapi/v2/openapi-preview.yaml`](https://raw.githubusercontent.com/mongodb/openapi/44ea8293091ddf05272f6ef9bf73637a3833cbbe/openapi/v2/openapi-preview.yaml) | 0 | 0 | same pair | required `token` → `Authorization` (46 files, 9 types, 6 error classes) | specification declares CC BY-NC-SA 3.0 US |
| [`mongodb/openapi:openapi/v2/private/openapi-private-preview-invoicereporting.yaml`](https://raw.githubusercontent.com/mongodb/openapi/44ea8293091ddf05272f6ef9bf73637a3833cbbe/openapi/v2/private/openapi-private-preview-invoicereporting.yaml) | 0 | 0 | same pair | required `token` → `Authorization: f"Bearer {self._get_token()}"` (46 files, 9 types, 6 error classes) | specification declares CC BY-NC-SA 3.0 US |
| [`Valiantsin2021/Cypress-Jenkins:automation-excersize-spec.json`](https://raw.githubusercontent.com/Valiantsin2021/Cypress-Jenkins/7ff789585a1615ee88c4deec07dd0a6d2e427ed2/automation-excersize-spec.json) | 0 | 0 | `basicAuth: http/basic` + `digestAuth: http/digest` | optional `username`/`password` → `Authorization` (28 files, 0 types, 0 error classes) | licence tier Q |

Each is Fern generating from the *other* scheme in the document — the
`clientCredentials` OAuth2 flow in the three MongoDB documents, HTTP basic in the
Cypress one — with the digest scheme leaving no trace. The three MongoDB documents
sit in an Apache-2.0 repository while the specification itself declares CC
BY-NC-SA 3.0 US — the same "the repository's licence does not cover the
specification it holds" problem that tier Q names.

### Ranged responses yield no error class

A `1XX`/`3XX`/`4XX`/`5XX` response key produces **no `errors/` package entry** and
no `raise` branch; the operation falls through to `ApiError`. `fern check` 0,
`fern generate` 0. Verdict *discards*.

### All 21 unpinned status exception names are correct — and 428 is `PreconditionError`

**Read this twice before "fixing" anything.** Issue #148 reasoned from RFC 6585
(which calls 428 *"Precondition Required"*) that crozier's `PreconditionError`
was likely wrong. It is not. Fern 5.20.0 names the 428 exception
**`PreconditionError`**, and names 412 `PreconditionFailedError`, so the two are
distinct classes and nothing collides. Measured three ways: an isolated 428 probe,
a 21-status probe, and two real documents.

Verbatim from the 21-status probe's `raw_client.py`:

```python
            if _response.status_code == 428:
                raise PreconditionError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
```

and from `errors/precondition_error.py`:

```python
class PreconditionError(ApiError):
    def __init__(self, body: Problem, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=428, headers=headers, body=body)
```

A probe declaring all 21 statuses on 21 operations passed `fern check` (exit 0)
and generated (exit 0), emitting exactly 21 error classes. Every class was read
three ways — the `class X(ApiError)` line, the `errors/<module>.py` filename, and
the `super().__init__(status_code=…)` argument — and cross-checked against the
branch the generated `raw_client.py` raises. **Every one of the 21 hand-written
names in crozier's `error_class_name` (`src/ir.rs`) matches, class name,
module filename and status code alike: 0 mismatches out of 21.**

| status | Fern class | `errors/` module | verified real specs emitting it |
|---:|---|---|---:|
| 407 | `ProxyAuthenticationRequiredError` | `proxy_authentication_required_error.py` | 0 (probe only) |
| 408 | `RequestTimeoutError` | `request_timeout_error.py` | 6 |
| 412 | `PreconditionFailedError` | `precondition_failed_error.py` | 5 |
| 414 | `UriTooLongError` | `uri_too_long_error.py` | 1 |
| 417 | `ExpectationFailedError` | `expectation_failed_error.py` | 2 |
| 418 | `ImATeapotError` | `im_a_teapot_error.py` | 4 |
| 421 | `MisdirectedRequestError` | `misdirected_request_error.py` | 0 (probe only) |
| 423 | `LockedError` | `locked_error.py` | 7 |
| 424 | `FailedDependencyError` | `failed_dependency_error.py` | 6 |
| 425 | `TooEarlyError` | `too_early_error.py` | 1 |
| 426 | `UpgradeRequiredError` | `upgrade_required_error.py` | 6 |
| 428 | `PreconditionError` | `precondition_error.py` | 2 |
| 431 | `RequestHeaderFieldsTooLargeError` | `request_header_fields_too_large_error.py` | 1 |
| 451 | `UnavailableForLegalReasonsError` | `unavailable_for_legal_reasons_error.py` | 5 |
| 502 | `BadGatewayError` | `bad_gateway_error.py` | 16 |
| 505 | `HttpVersionNotSupportedError` | `http_version_not_supported_error.py` | 5 |
| 506 | `VariantAlsoNegotiatesError` | `variant_also_negotiates_error.py` | 5 |
| 507 | `InsufficientStorageError` | `insufficient_storage_error.py` | 7 |
| 508 | `LoopDetectedError` | `loop_detected_error.py` | 5 |
| 510 | `NotExtendedError` | `not_extended_error.py` | 6 |
| 511 | `NetworkAuthenticationRequiredError` | `network_authentication_required_error.py` | 5 |

The names being right is not the same as their being *pinned*: eight of the 21
have no registrable witness set, listed under
[What Round 3 did not register](#what-round-3-did-not-register-and-why).

### 407 and 421 — a corpus limit, not a Fern one

**Zero** documents in the eligible pool of 4,864 declare either status anywhere, so
no real specification can pin them. Probed directly, Fern handles both:

| | 407 | 421 |
|---|---|---|
| `fern check` | exit **0**, `All checks passed` | exit **0**, `All checks passed` |
| `fern generate` | exit **0**, packaged SDK | exit **0**, packaged SDK |
| class emitted | `ProxyAuthenticationRequiredError` | `MisdirectedRequestError` |
| module | `errors/proxy_authentication_required_error.py` | `errors/misdirected_request_error.py` |
| `status_code` | 407 | 421 |

The only ways to pin these two are a probe-style specification (which the corpus
rules exclude) or a wider pool.

## Fern exiting zero while doing nothing

Exit codes are the weakest evidence in this whole file. Every failure mode in this
section ends with two zeros.

### `fern check` can exit 0 while the document did not parse

The log carries `Failed to parse openapi document <title>` and a
`CliError: Failed to resolve …`, and then still prints `All checks passed` and
exits 0 — after which Fern generates an empty SDK. Ten of 105 check-passes in the
structure-and-media screen and eight documents in the auth-and-responses screen
are exactly this shape.
[`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md) already records it for
`conjur.local` and `digitalocean.com` (*"Fern falsely returned success"*).

The instructive case is `gh:speakeasy-sdks/moov-go`: 73 operations, 235 KB, both
stages exit 0, and the result is a **26-file skeleton with no client, no types and
no errors**, because `"429": {"$ref": "#/components/schemas/RateLimited"}` points
a response at a *schema* and Fern cannot resolve it.

> **The practical rule for any future fixture work:** exit codes are not enough.
> Grep the check log for `Failed to resolve` and `Failed to parse`, and assert the
> generated tree contains `raw_client.py`.

### Duplicate `operationId` silently collapses operations into one method

`networknt/light-rest-4j`'s `openapi-meta/src/test/resources/config/openapi.yaml`
reuses `operationId: showPetById` across **18 operations** and Fern emits one. On
the sibling `openapi-validator/.../config/openapi.yaml`: **22 operations in, 5
client methods out**. Both exit 0 at both stages, so only reading the output finds
it. Across those three documents only 1 of the 15 operations carrying the shapes
they were ranked for (14 for the third) reaches the generated client — and that
document was the census's **#1-ranked candidate** for `matrix-array`,
`matrix-object`, `label-array-or-object` and `cookie-array`. A byte-match fixture on it would have
proved almost nothing about the shapes it was selected for.

### 28 candidates generated a complete, valid, *empty* SDK

Exit 0, packaged, zero endpoints. Seven had no `paths` at all and could never have
been fixtures. The other **21 declared operations that never arrived**, almost all
behind a Path Item `$ref` (`AppcentMobile/medusa` declares 158,
`trajectoryjp/cudi-oss` 98, `1024XEngineer/XE3-ESL` 85, `stellar/stellar-docs`
46) — and **11 of those printed no failure marker at all**. An empty SDK witnesses
no feature, so a screen reading exit codes alone would have proposed several of
them as primaries.

### `fern check` passing does not mean the generator will

Nine of 115 in the auth-and-responses screen, from two distinct causes:

- **AWS-shaped specifications** die with
  `KeyError: 'type_:<Operation>RequestXAmzTarget'` inside the generator —
  `amazonaws.com:cloudtrail@2013-11-01`, `codedeploy@2014-10-06`,
  `codecommit@2015-04-13`, and non-AWS `gh:kciceblue/sshserver` with
  `KeyError: 'type_:GetHealthRequestJatProtocolVersion'`. Not all AWS
  specifications: `cloudfront@2016-11-25` and `redshift@2012-12-01` generate
  cleanly. The cause was not diagnosed; only that it reproduces.
- **Emitted Python that does not parse.** Five documents fail the generator's own
  `ruff check --fix --no-cache --ignore E741 /fern/output` step. The clearest is
  `gh:koxudaxi/fastapi-code-generator:tests/data/openapi/coverage/python_literal_escaping.yaml`,
  a code-injection test fixture whose path template makes Fern emit
  `"items/'+(__import__("os").system("path") or "")+'/detail"` into
  `raw_client.py` — a `SyntaxError`. It was the census's top 418 candidate.

### A Fern overrides fragment is not a specification

`aabiro/xcelsior:fern/openapi-overrides.yml` was counted by the census at 290
operations and 211 `x-fern-ignore` occurrences. It passes both stages and emits 26
`.py` files with **zero** `types/` modules — the runtime scaffold and nothing else;
a one-operation probe emits 30. An `openapi-overrides.yml` fragment cannot serve as
a fixture.

## Structure and media

### Fern silently discards every Path Item `$ref` that is not a remote URL

A two-path probe with one inline operation and one
`$ref: "#/components/pathItems/ViaRef"`, everything resolvable inside the single
file: `fern check` exit 0 `All checks passed`, `fern generate` exit 0, and the
emitted client has `def get_inline` and **no** `def get_via_ref`. Nothing is
reported. This is worse than the "unresolved reference" failure it looks like: it
also happens when the reference is internal and perfectly resolvable.

Reproduced on every real candidate carrying the shape:

| document | declared | emitted |
|---|---|---|
| `SecondBox` | 48 inline + 5 by internal ref | 48 |
| `0rkx/codex-openai-bridge` | 5 + 10 | 5 |
| `apache/apisix` | 6 + 1 | 6 |
| `Sakayori-Iroha-168/Software_Teamwork` | 2 + 22 | 2 |
| `ga4gh/tool-registry-service-schemas` | 10 + 1 **remote-URL** ref | **11** |

A **remote-URL** Path Item `$ref` is the one form that survives.

### Fern emits no client method for `options` or `trace`

An eight-method probe — one path, all eight OpenAPI methods, each with its own
`operationId` — generates a six-endpoint SDK: `get`, `post`, `put`, `patch`,
`delete`, `head`. `options_thing` and `trace_thing` are absent, `fern check` exits
0 with `All checks passed`, and nothing is reported. A fixture named for either
method would pin *Fern emitting nothing* — still a real regression guard, but the
fixture note would have to say so. No row this round registers carries either
method. crozier's `PathItem` (`src/openapi.rs`) deserializes exactly the six
methods Fern emits, so the two already agree by construction.

### A multi-document specification cannot be registered today

The blocker is the **Fern workspace**, not the fetcher. Three facts about this
repository, unchanged by the screen:

1. `scripts/fern-goldens` validates each `CORPUS.md` URL and refuses a path that
   does not end in `.json`/`.yaml`/`.yml`; its `fetch_spec` then requires exactly
   one spec path pointing at an existing non-empty file.
2. `scripts/corpus-lib.sh` does have a repository-clone shape
   (`corpus_fetch_repo`, a `git clone --filter=blob:none` at the pinned ref), but
   the suffix check in (1) makes it unreachable from the golden path — and every
   numbered `CORPUS.md` row is a direct spec URL anyway.
3. `scripts/generate-fern-fixture.sh` copies the one spec file into the workspace,
   leaving its siblings behind.

Given the tree, **Fern resolves relative-file `$ref`s perfectly well**: the
`Foxcapades/softask-api-doc` entry document emits **0** endpoints when fetched
alone, and **31**, across six sub-clients, with its `v1/` tree present in the
workspace.

Three registration shapes would answer this. Each is a decision for the
maintainer, not a lookup:

- **(a) Register a pre-bundled single document.** Some repositories commit one
  (`trajectoryjp/cudi-oss` has `docs/openapi/cudi/gen/bundled.yaml` beside its
  split source). Needs no crozier change and fits the existing `github-raw` method
  exactly — the bundled document gave byte-for-byte the same `fern check` verdict
  as the tree probe (exit 1, the same single `CreateSaleScoped`/`sales_channel_id`
  error, the same 8 warnings). What it does **not** do is exercise multi-document
  resolution: crozier would be handed a flat document, exactly as Fern is.
- **(b) Register the entry document and accept the loss.** This is what happens
  today if such a URL is registered: Fern generates cleanly and the golden omits
  every operation behind a reference. Legitimate only if the row records that the
  golden pins Fern's silent drop.
- **(c) Teach the workspace about a tree** — a manifest cell naming the spec
  directory plus its entry document, `validate_url` accepting it, and
  `generate-fern-fixture.sh` copying the tree. A small, real crozier change; the
  `softask` probe above establishes it would work.

### A `$ref` key is not always a reference

Three of the census's ranked candidates did not carry the shape they were ranked
for, because the census's feature keys are textual matches on a `$ref` key:

- `factset/enterprise-sdk` — 3 counted relative-file and 9 remote-URL refs are
  SCIM data fields literally named `$ref` **inside request-body examples**;
- `Relequestual/openapi-diff-testing` and `fern-api/swift-sdk-comparison` — the
  single counted relative-file ref is Redoc's
  `x-topics[0].content.$ref -> ./docs/getting-started.md`, a pointer to markdown;
- `gematik/api-erp` — all 17 counted remote-URL refs sit inside a media-type
  `example`.

Screen gap membership from the parsed document, not from a census key.

## Naming and types

### Non-ASCII identifiers split three ways, and the middle case is the dangerous one

Each probe is a minimal OpenAPI 3.0.0 document differing from the others in one
identifier, run `fern check` → `fern generate` → `python3 -m py_compile` over every
emitted module:

| probe | identifier under test | `fern check` | `fern generate` | verdict |
|---|---|:--:|:--:|---|
| `schema-name` | schema `気温` | **1** | 1 | **refuses** — `issue: Type name must begin with a letter` |
| `schema-name-mixed` | schema `気温Data` | **1** | 1 | **refuses** |
| `enum-value` | enum members `暑い`, `寒い` | **1** | 1 | **refuses** |
| `property-name` | property `気温` | 0 | **1** | **emits invalid Python** |
| `property-name-cyrillic` | property `температура` | 0 | **1** | **emits invalid Python** |
| `property-name-greek` | property `θερμοκρασία` | 0 | **1** | **emits invalid Python** |
| `param-name` | query parameter `気温` | 0 | **1** | **emits invalid Python** |
| `operationid` | operationId `天気取得` | 0 | **1** | **emits invalid Python** |
| `schema-name-ascii-lead` | schema `Data気温` | 0 | 0 | normalizes → `class Data` |
| `schema-name-latin1` | schema `Medicação` | 0 | 0 | normalizes → `class Medicacao` |
| `property-name-mixed` | properties `a気温b`, `温度C` | 0 | 0 | normalizes → `a_b`, `c` |
| `property-name-latin1` | property `preço` | 0 | 0 | normalizes → `pre_o` |
| `info-title` | `info.title: 推奨データセット` | 0 | 0 | accepted; never reaches an identifier |
| `path-segment` | path `/天気/current` | 0 | 0 | accepted; emitted verbatim as a URL string |

For the three refusing probes the recorded `fern generate` exit is 1 as well; the
`fern check` refusal is the finding, and the screen's verdict for them is a
rejection.

The middle block is the dangerous one: `fern check` passes and the **generator
fails on its own output**. Every probe that generated also passed
`python3 -m py_compile` on every emitted module (exit 0), so "emits invalid Python"
is Fern failing on what it wrote, not an artefact of how it was checked.

### Float, list and object enum members are accepted and the enum is discarded

| probe | enum declared | `fern check` | `fern generate` | emitted |
|---|---|:--:|:--:|---|
| `enum-member-float` | `[1.5, 2.25]` | 0 | 0 | `Kind = float` — no members |
| `enum-member-list` | `[[a,b],[c,d]]` | 0 | 0 | `Kind = typing.List[str]` |
| `enum-member-object` | `[{a:1},{b:2}]` | 0 | 0 | `Kind = typing.Dict[str, typing.Any]` |

No `Literal`, no members, nothing reported. A golden here pins the *absence* of the
enum.

### Seven naming and type gaps have no complete proposable set

| gap | reason |
|---|---|
| `nonascii-schema-name` | **Fern refuses the shape** — all nine licence-defensible candidates fail `fern check` |
| `nonascii-param-name` | **Fern emits invalid Python** — all three candidates fail |
| `nonascii-path-segment` | **zero documents in the pool carry it**, and Fern handles it anyway: a path segment is emitted verbatim as a URL string |
| `nonascii-operationId` | pool exhausted at 1 eligible (`naming.nonascii.operationId`: 10 documents, A=1 B=4, 5 untiered) |
| `enum-member-float` | pool exhausted at 2 eligible (`types.enum.member.float`: 353 documents, B=2, 351 untiered) |
| `enum-member-object` | pool exhausted at 1 eligible (`types.enum.member.object`: 6 documents, A=1 B=1, 4 untiered) |
| `enum-member-list` | both clean generates are licence **tier Q**, quarantined — a do-not-propose rule, not a gap in verification |

Every tier A/B document in the three exhausted pools was examined. Widening any of
them means extending the census's licence tiering to documents it never tiered,
which is census work rather than screening work — for `types.enum.member.float`
alone that is 351 documents.

## Measurement caveats that outlive this round

### Witness count and witness *independence* are different measures

The screens reported how many documents witnessed a shape; they did not report how
many **independent** documents did, and the two come apart. Round 3 hit it twice:

- Statuses 505, 506, 508 and 511 each have five eligible, licence-clean,
  screen-verified witnesses emitting the same exception class — and those five are
  revisions of just two APIs, `amazonaws.com:cloudfront` (four revisions) and
  `amazonaws.com:redshift`.
- `Ekveer-Sahoo/kepel-xenia` and `jaccen/AIRoute` are forks of one document —
  188,400 against 188,477 bytes — and would otherwise have served as two
  independent backups for status 426.

A count of three witnesses is not a claim that three independent things agree.
Whether that matters depends on **what the fixture pins**. For an exception class
*name*, measured identical across every witness, a fork-family witness pins it just
as correctly as an unrelated one — so the count is the right measure and all four
statuses above were registered. For a fixture pinning a *shape*, it would not be.
Round 3 therefore applied independence one level down: to choosing among equally
eligible backups, where preferring two different documents over two forks costs
nothing — and not to deciding whether a gap is closable at all.

### The four screens applied different licence bars

The most reusable finding of the round, and no screen could see it from inside
itself. Joining the census's own licence pass (`licence-evidence.jsonl`, 1,066
records, 243 of them tier Q) to what each screen proposed shows the four disagreed
about what "verified" meant:

| screen | joined the licence pass? | candidates clean |
|---|---|---|
| naming-and-types | yes, and said so | 46 of 48 |
| serialization | yes — quarantined 11 of its 70 ranked candidates | 51 of 96 |
| structure-and-media | only partly | 31 of 54 |
| auth-and-responses | no | 18 of 39 |

Two exclusion reasons behind those numbers are **not** the same thing, and a reader
comparing screens will otherwise conflate them:

- **Licence tier Q** — the census *verified* that the document describes a
  third-party API whose licence is not the host repository's. This is the same
  distinction [`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md) already
  draws in rejecting `assemblyai-autosdk`.
- **Licence untiered** — the census never measured a licence for the document at
  all. Not a failed check but an absent one; Round 3 treats an unmeasured licence
  as ineligible rather than settling it mid-dispatch.

What the join cost, concretely: an MIT tutorial repository holding AbstractAPI's
specification; a CC0 catalogue holding HERE's under a "HERE Documentation
License"; three `mongodb/openapi` documents whose specification declares **CC
BY-NC-SA 3.0 US**; a permissive repository holding Google's under CC BY 3.0.

Two consequences worth recording so the supply is not re-searched:

- **`http-digest` has no redistribution-compatible witness at all** — a distinct
  empty reason from any the screens recorded, since all four of its verified
  witnesses fail the licence bar rather than failing Fern. They are named with
  their measurements under
  [The four `http-digest` witnesses](#the-four-http-digest-witnesses-and-why-none-can-be-registered):
  three MongoDB documents whose specification declares CC BY-NC-SA 3.0 US, and one
  tier-Q document.
- **`oauth2-implicit` is the near miss beside it**: its one licence-clean
  candidate, `xataio/xata`, declares zero operations, and an empty SDK is not a
  witness.

### Two exclusions a name-based filter does not catch

Both were missed by exclusion-by-repository-name and caught only by reading each
candidate's own `info.title` against the recorded do-not-retry names. The next
screen will need the same second pass.

- `atacan/AssemblyAI` (both `openapi.yaml` and `original_openapi.yaml`) and the
  `gr2m/ai-provider-monitor` cache copy are the **AssemblyAI** specification
  re-hosted in third-party repositories.
  [`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md) records
  `assemblyai-autosdk` as REJECTED because its *source* licence is
  revenue-limited, and a host repository's MIT or ISC licence does not change the
  licence of the specification it re-hosts.
- `open-feature/protocol:service/event-streams.yaml` is the same ref recorded
  DROPPED as `openfeature-protocol`, independently reproduced at `fern check`
  exit 1.

## Round 4 — resolving the eighteen unmeasured rows

Round 3 left eighteen rows reading **unmeasured**: open questions, not proven
absences. Round 4 closes them one family at a time, and each subsection below
records the evidence for its own rows. Every Round 4 measurement was taken on
2026-08-22 under the pins this file already declares — Fern CLI `5.67.1`,
generator `fernapi/fern-python-sdk:5.20.0`, `CI=true`/`GITHUB_ACTIONS=true` —
against a workspace scaffolded exactly as `scripts/generate-fern-fixture.sh`
builds one.

**Fourteen of the eighteen are documented limitations. Two are registrable, and
both were registered.** The remaining two are shapes Fern *does* implement and a
committed, byte-matching golden already pins, so they warrant no new fixture. No
row is left unmeasured, and none of the eighteen resolved as a supply or licence
limit dressed up as a Fern result: every verdict is a measurement of what the
generator emitted. Three rows — `components-links`, `link-requestBody` and
`link-server` — carry a `+ supply` qualifier, but in all three the discard is
established by probe independently of the candidate pool, and the shortfall bears
only on registrability. That is the round's finding, and it lands the same way
round 3's did. Round 3 recorded four gaps of fifty-nine clearing both bars, with
eighteen of the remainder standing as open questions rather than proven absences;
closing all eighteen makes the standing tally **six of fifty-nine**, not four.
The eighteen were not a hidden reservoir of gaps — issue #148 assumed this
surface was full of them, and measured end to end it is mostly shapes Fern
flattens, discards or refuses. But it is not empty either, which is the half of
round 3's result that needed testing rather than repeating: two of the eighteen
were real, and are corpus rows today.

Two evidence routes are in play, and they are not equally cheap. **Route 1**
reads a committed golden: `tests/fixtures/<name>/expected/` is Fern's real
output on a real specification, already byte-matched by the gate, so where a
corpus row's *own source document* declares the shape under test its golden
already shows what Fern did with it. The route is only sound when the shape is
shown **present in the source, quantified**, before its absence from the golden
means anything. **Route 2** is a probe — a minimal locally authored document
isolating one shape, carried through `fern check` and a real `fern generate` —
and is what a row gets when no committed golden's source declares its shape at
all.

### Round 4 — servers and XML

Five rows, all **discards**. Nothing in this family is registrable: Fern emitted
nothing derived from any of the five shapes, so a fixture would pin an
unconditional default and prove nothing.

#### One environment member, always — checked across the whole corpus

Every claim in the two `servers` rows below rests on Fern's environment enum, so
the enum's shape was checked exhaustively first rather than sampled. Of 105
committed `expected/` trees, 71 contain an `environment.py`, and **every one of
them declares exactly one member**:

```console
$ ls -d tests/fixtures/*/expected | wc -l
105
$ ls tests/fixtures/*/expected/src/fern/environment.py | wc -l
71
$ for f in tests/fixtures/*/expected/src/fern/environment.py; do
>   grep -cE '^    [A-Z0-9_]+ = ' "$f"
> done | sort | uniq -c
     71 1
$ grep -hE '^    [A-Z0-9_]+ = ' tests/fixtures/*/expected/src/fern/environment.py \
>   | sed 's/ =.*//' | sort | uniq -c
     66     DEFAULT
      5     PRODUCTION
```

Two member names exist in the entire corpus and no document produces two
members. The 34 trees with no `environment.py` are the ones with nothing to
emit — across all 34 sources exactly one mentions `servers` at all, and it
declares an empty array:

```console
$ for d in tests/fixtures/*/expected; do
>   n=$(basename "$(dirname "$d")")
>   [ -f "$d/src/fern/environment.py" ] || echo "$n"
> done > /tmp/noenv; wc -l < /tmp/noenv
34
$ while read -r n; do
>   f=$(ls tests/fixtures/$n/openapi.* .local/corpus/$n/openapi.* 2>/dev/null | head -1)
>   printf '%s %s %s\n' "$n" "$(grep -cE '^ *"?servers"? *:' "$f")" \
>     "$(grep -hE '^ *"?servers"? *:.*' "$f" | head -1)"
> done < /tmp/noenv | awk '$2!=0'
prometheus-x-edge-computing 1 servers: [ ]
```

#### `server-description-multiword` — discards

**Route 1. `traccar.org`, `CORPUS.md` row 60**
(`https://api.apis.guru/v2/specs/traccar.org/5.6/openapi.json`). Its source
declares **six** root servers, every one of them carrying a **multi-word**
description, and **zero** `servers` blocks below the root:

```console
$ jq -r '[.servers[].description] | length, .[]' .local/corpus/traccar.org/openapi.json
6
Demo Server 1
Demo Server 2
Demo Server 3
Demo Server 4
Subscription Server
Other Server
$ jq '[.paths[] | select(.servers)] | length' .local/corpus/traccar.org/openapi.json
0
$ jq '[.paths[][] | objects | select(.servers)] | length' .local/corpus/traccar.org/openapi.json
0
```

`tests/fixtures/traccar.org/expected/src/fern/environment.py` is, in full (the
corpus is comment-stripped, so its two leading blank lines are where Fern's
`# This file was auto-generated…` banner was):

```python
import enum


class FernApiEnvironment(enum.Enum):
    DEFAULT = "https://demo.traccar.org/api"
```

Six descriptions in, one unconditional `DEFAULT` out. Censused across all 91
fetched sources, the goldens split cleanly on word count — every multi-word
description with a golden to read yields `DEFAULT`, every single-word one
yields `PRODUCTION`, with no exception either way:

```console
$ uv run --no-project --quiet --with pyyaml python3 - <<'PY'
> import glob, os, re, yaml
> tally = {}
> for f in sorted(glob.glob('.local/corpus/*/openapi.*')):
>     n = os.path.basename(os.path.dirname(f))
>     d = (yaml.safe_load(open(f)).get('servers') or [{}])[0].get('description')
>     if not d:
>         continue
>     env = f'tests/fixtures/{n}/expected/src/fern/environment.py'
>     m = re.findall(r'^    ([A-Z0-9_]+) = ', open(env).read(), re.M) \
>         if os.path.exists(env) else []
>     k = ('multi-word' if len(d.split()) > 1 else 'single-word',
>          m[0] if m else 'no-golden')
>     tally[k] = tally.get(k, 0) + 1
> for k in sorted(tally):
>     print(tally[k], *k)
> PY
18 multi-word DEFAULT
4 multi-word no-golden
4 single-word PRODUCTION
```

`yaml.safe_load` rather than `jq` because the 91 sources are not all JSON — a
JSON-only census silently drops six multi-word witnesses:

```console
$ ls .local/corpus/*/openapi.* | sed 's/.*\.//' | sort | uniq -c
     74 json
     15 yaml
      2 yml
```

| first root server description | words | golden's environment member |
|---|---:|---|
| `apideck.com-vault` — `Production server` | 2 | `DEFAULT = "https://unify.apideck.com"` |
| `apideck.com-proxy` — `Production server` | 2 | `DEFAULT = "https://unify.apideck.com"` |
| `apideck.com-crm` — `Production` | 1 | `PRODUCTION = "https://unify.apideck.com"` |
| `apideck.com-lead` — `Production` | 1 | `PRODUCTION = "https://unify.apideck.com"` |

The first two rows are the control the row needed: same publisher, same base
URL, same single root server, and the *only* difference is the word `server`
appended to the description — which costs the name. The four multi-word
documents with no golden to read are counted separately above and excluded
rather than assumed.

`dnd5eapi.co` (row 42) is worth naming separately because it carries both shapes
in one document — `Production` first, `Local Development` second — and its
golden emits `PRODUCTION = "https://www.dnd5eapi.co"` and nothing else. The
multi-word description contributes no member even when a single-word one beside
it does.

The mechanism is narrower still than "multi-word is dropped": the
`servers-three-levels` probe below gives its root server the **single-word**
description `Root` and gets `DEFAULT` back. So Fern does not derive an
environment name from a description in general: `Production` is recognised, and
other descriptions — multi-word ones and the single word `Root` alike — fall
through to `DEFAULT`. What else the recognised set contains was not measured and
is not claimed here; what the row asked, whether a multi-word description
reaches a name, is answered no.

#### `servers-multiple-path-or-operation` — discards

**Route 1. `apideck.com-file-storage`, `CORPUS.md` row 14**
(`https://api.apis.guru/v2/specs/apideck.com/file-storage/9.3.0/openapi.json`).
This is the one committed golden whose source declares servers below the root at
a **different host** from the root's, which is what makes its silence mean
something:

```console
$ jq -c '.servers' .local/corpus/apideck.com-file-storage/openapi.json
[{"url":"https://unify.apideck.com"}]
$ jq -r '[.paths | to_entries[] as $p | $p.value | to_entries[]
>   | select(.value|type=="object") | select(.value.servers)
>   | "\($p.key) \(.key) -> \(.value.servers[].url)"] | length, .[]' \
>   .local/corpus/apideck.com-file-storage/openapi.json
5
/file-storage/files post -> https://upload.apideck.com
/file-storage/upload-sessions post -> https://upload.apideck.com
/file-storage/upload-sessions/{id} get -> https://upload.apideck.com
/file-storage/upload-sessions/{id} put -> https://upload.apideck.com
/file-storage/upload-sessions/{id}/finish post -> https://upload.apideck.com
```

The golden emits `DEFAULT = "https://unify.apideck.com"` — the root — and the
generated call site for the first of those five operations,
`expected/src/fern/upload_sessions/raw_client.py`, carries a bare relative path
and no base URL of its own:

```python
        _response = self._client_wrapper.httpx_client.request(
            "file-storage/upload-sessions",
            method="POST",
            params={
                "raw": raw,
            },
```

`upload.apideck.com` does appear in the golden, and only where it cannot be a
routing decision — three files hold it, and every occurrence is inside docstring
prose copied verbatim from the specification's own `description`:

```console
$ grep -rl 'upload\.apideck\.com' tests/fixtures/apideck.com-file-storage/expected/ | sort
tests/fixtures/apideck.com-file-storage/expected/reference.md
tests/fixtures/apideck.com-file-storage/expected/src/fern/upload_sessions/client.py
tests/fixtures/apideck.com-file-storage/expected/src/fern/upload_sessions/raw_client.py
```

— e.g. *"Note that the base URL is upload.apideck.com instead of
unify.apideck.com."* The SDK documents the override in English and then ignores
it, which is the sharpest possible form of the finding.

No golden anywhere assigns a base URL per operation. Every `base_url=` in every
golden's `src/` is one of four forms:

```console
$ grep -rhoE 'base_url=[A-Za-z_.]+|base_url="[^"]*"' tests/fixtures/*/expected/src/ \
>   | sort | uniq -c | sort -rn
    844 base_url=base_url
    360 base_url="https://yourhost.com/path/to/api"
    210 base_url=self.get_base_url
    140 base_url=_get_base_url
```

`base_url=base_url` and `_get_base_url(...)` thread the constructor argument,
falling back to `environment.value`; `self.get_base_url` reads it back inside
the request layer; the literal is Fern's placeholder in generated docstring
`Examples` blocks. None of the four names a host from a `servers` block below
the root.

`twilio.com-twilio_voice_v1` (row 61) is recorded here as the *weaker* witness
it is. It declares 17 Path Item `servers` blocks — but every one of them repeats
the root URL, so its single `DEFAULT` member cannot distinguish discarding from
honouring:

```console
$ jq -c '.servers' .local/corpus/twilio.com-twilio_voice_v1/openapi.json
[{"url":"https://voice.twilio.com"}]
$ jq '[.paths[] | select(.servers)] | length' .local/corpus/twilio.com-twilio_voice_v1/openapi.json
17
$ jq -r '[.paths[] | select(.servers) | .servers[].url] | unique | .[]' \
>   .local/corpus/twilio.com-twilio_voice_v1/openapi.json
https://voice.twilio.com
```

The verdict rests on `apideck.com-file-storage`, not on this row.

#### `servers-three-levels` — discards

**Route 2 — a probe.** No committed golden's source declares a `servers` block
at all three levels: `apideck.com-file-storage` has root plus Operation,
`twilio.com-twilio_voice_v1` root plus Path Item, and nothing in the corpus has
both below the root. So this row cannot be answered from a golden and was
probed.

The probe declares one server at each level, each on its own host, and one
operation inheriting from each level. In full:

```yaml
openapi: 3.0.3
info:
  title: servers three levels probe
  version: 1.0.0
servers:
  - url: https://root.example.com
    description: Root
paths:
  /root-only:
    get:
      operationId: rootOnly
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Thing"
  /overridden:
    servers:
      - url: https://path-level.example.com
        description: PathLevel
    get:
      operationId: pathOverride
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Thing"
    post:
      operationId: operationOverride
      servers:
        - url: https://operation-level.example.com
          description: OperationLevel
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Thing"
components:
  schemas:
    Thing:
      type: object
      properties:
        id:
          type: string
      required:
        - id
```

`fern check` **exit 0**, `fern generate` **exit 0**; neither reported anything
about the overrides. The generated `src/fern/environment.py` is, in full, as
Fern emitted it (banner included — a probe is not comment-stripped):

```python
# This file was auto-generated by Fern from our API Definition.

import enum


class FernApiEnvironment(enum.Enum):
    DEFAULT = "https://root.example.com"
```

and that line is the **only** occurrence of any of the three hosts anywhere in
the generated tree (run from the probe workspace, not the repository):

```console
$ grep -rn 'root.example.com\|path-level.example.com\|operation-level.example.com' \
>   preview/fern-python-sdk/
preview/fern-python-sdk/src/fern/environment.py:7:    DEFAULT = "https://root.example.com"
```

Both overrides are discarded silently, and `Root` — a *single*-word description
— still yields `DEFAULT`, which is the observation the
`server-description-multiword` row above leans on.

#### `xml-request` and `xml-response` — discards

**`application/xml` is not settled by any committed golden. Decided
explicitly.** The two AWS Query-protocol rows are the corpus's XML documents,
and they declare `text/xml`, never `application/xml`:

```console
$ scripts/fetch-corpus.sh          # all 91 link-ok rows, into .local/corpus/
$ ls -d .local/corpus/*/ | wc -l
91
$ grep -rl 'application/xml' .local/corpus | wc -l
0
$ ls tests/fixtures/*/openapi.* | wc -l
31
$ grep -l 'application/xml' tests/fixtures/*/openapi.* | wc -l
0
$ grep -rhoE '[a-z]+/[a-z0-9.+-]*xml[a-z0-9.+-]*' .local/corpus \
>   | sort | uniq -c | sort -rn
    644 text/xml
     15 image/svg+xml
      7 application/atom+xml
      5 application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
      1 gadgets/activitystream-gadget.xml
      1 application/gpx+xml
```

All 91 `link-ok` sources were fetched from their pinned `CORPUS.md` URLs with
the repository's own `scripts/fetch-corpus.sh` and searched, together with all
31 vendored fixture specs: **zero** declare `application/xml`. The XML-ish media
types that *are* present are `text/xml` (`amazonaws.com-cloudformation`,
`amazonaws.com-cloudfront`), `image/svg+xml` (`atlassian.com-jira`,
`color.pizza`), `application/gpx+xml` and the XLSX type (`traccar.org`), and
`application/atom+xml` (`github.com`, which has no golden — `CORPUS.md` records
it DROPPED at `fern check`). The `gadgets/…` line is the deliberately loose
pattern catching a URL path inside a description, not a media type. So Route 1
cannot finish these two rows and **both rest on a probe**, not on the CloudFront
reading.

**Route 2 — a probe.** One document, three operations against one `Widget`
schema that also carries an OpenAPI `xml` Object (`name`, `wrapped`,
`attribute`, a renamed property): a JSON control, a `POST` with a **required**
`application/xml` request body, and a `GET` with an `application/xml` response.
In full:

```yaml
openapi: 3.0.3
info:
  title: xml media probe
  version: 1.0.0
servers:
  - url: https://api.example.com
paths:
  /json-control:
    post:
      operationId: jsonControl
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Widget"
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Widget"
  /xml-request:
    post:
      operationId: xmlRequest
      requestBody:
        required: true
        content:
          application/xml:
            schema:
              $ref: "#/components/schemas/Widget"
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Widget"
  /xml-response:
    get:
      operationId: xmlResponse
      responses:
        "200":
          description: ok
          content:
            application/xml:
              schema:
                $ref: "#/components/schemas/Widget"
components:
  schemas:
    Widget:
      type: object
      xml:
        name: widget
        wrapped: true
      properties:
        id:
          type: string
          xml:
            attribute: true
        name:
          type: string
          xml:
            name: widgetName
      required:
        - id
```

`fern check` **exit 0**, `fern generate` **exit 0**; neither reported anything
about the media type. The emitted `src/fern/raw_client.py` — control first, so
the difference is legible:

```python
    def json_control(
        self, *, id: str, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Widget]:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Widget]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "json-control",
            method="POST",
            json={
                "id": id,
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
```

```python
    def xml_request(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Widget]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Widget]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "xml-request",
            method="POST",
            request_options=request_options,
        )
```

```python
    def xml_response(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "xml-response",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
```

`xml_request` takes **no body argument at all** and sends no `json=`, `data=` or
`content=`: the required request body is not merely unserialised, it is gone,
and the generated method cannot send one. `xml_response` returns
`HttpResponse[None]` and hands back `data=None` without touching the body; the
declared `Widget` response schema reaches nothing. `reference.md` documents both
as `client.xml_request()` and `client.xml_response()`, no arguments.

The `xml` Object is discarded with the media type. Every occurrence of the
string `xml` in the generated tree is the operationId-derived method name or the
URL path that produced it; `widgetName`, `wrapped` and `attribute` appear
nowhere. `Widget` itself is still emitted — but only because the JSON control
operation references it; the XML operations contribute nothing to it.

This matches, and now explains, what `amazonaws.com-cloudfront` (row 89) shows
for `text/xml` — a source dense with XML, and a golden that reads every response
as JSON and nothing else:

```console
$ grep -o 'text/xml' .local/corpus/amazonaws.com-cloudfront/openapi.json | wc -l
256
$ jq '[.. | objects | select(has("xml"))] | length' \
>   .local/corpus/amazonaws.com-cloudfront/openapi.json
33
$ grep -rhoE '_response\.(json|text|content|iter_[a-z]+)\(\)' \
>   tests/fixtures/amazonaws.com-cloudfront/expected/src/ | sort | uniq -c
    192 _response.json()
```

The CloudFront golden is corroboration for the shape of the behaviour; it is not
the evidence for these rows, because its source declares a different media type.

#### Nothing registrable, and what that means for the rows behind this one

No row in this family is **REGISTRABLE**. In each of the five, what Fern emitted
is an unconditional default or an outright absence, and no byte of the output is
derived from the shape under test — so a fixture would pin the default, not the
feature, which is the `deepObject` failure mode this whole exercise exists to
avoid. No deletion-control generation was run: this records what the measured
output contains, not a byte comparison against a shape-stripped document.

The evidence generalises along one axis, and the axis is narrower than "document
metadata". What was measured is that **Fern's importer keeps one server URL for
the whole client and one wire format for every body**, and that everything the
document says beyond those two facts — a second server, a server below the root,
a description, a non-JSON media type — is dropped without a diagnostic. That is
a statement about the *inputs Fern's IR has a slot for*, not about metadata as a
category.

- **For `m2-links-encoding`:** the same reading predicts null. A Link object
  describes a relationship between two operations and an Encoding object
  describes a per-part wire format; neither has a slot in an IR that keeps one
  base URL and assumes JSON, and the `xml-request` result is the direct
  precedent — Fern discarded a *required* request body rather than represent a
  body it had no wire format for. Descoping `m2` on this basis is defensible. It
  is not proven: no Link or Encoding object was measured here, and the six `m2`
  rows are still `unmeasured` until one is. They were not descoped — every one was
  measured, and the prediction held: see
  [links and encoding](#round-4--links-and-encoding).
- **For `m3-schema-shapes`:** this result predicts nothing. Every discard above
  is a *routing or wire-format* input, and the one place the probe touched the
  type system it behaved correctly — `Widget` was emitted with the right fields
  the moment a JSON operation referenced it. The `m3` rows (`const`, multi-type
  arrays, cycles, nesting depth, normalization collisions) feed the type
  machinery Fern demonstrably does implement, and nothing measured here is
  evidence about them either way. This family is **not** grounds to drop `m3`.

### Round 4 — links and encoding

Six rows. The four link rows are **discards** and behave alike. The two encoding
rows do not, and both carry a split cell: `encoding-object` **implements**
`contentType` and **discards** per-part `headers`, and
`encoding-explode-or-allowReserved` is **refused** at check time in one
configuration and **ignored** at generate time in the other six.

`contentType` is the only thing Round 4 measured Fern to
[**implement**](#how-to-read-a-verdict), and it is the first such result in this
file — Round 3 produced no row that reached one. It still proposes no fixture, and
no `REGISTRABLE` candidate set: `CORPUS.md` rows 73 and 76 already pin that
behaviour, with goldens crozier byte-matches.

#### No corpus document declares these fields — so five of the six rows are probes

Route 1 needs the shape present in a golden's own source, quantified, before its
absence from the golden means anything. Censused across all 91 fetched `link-ok`
sources and all 31 vendored fixture specs, **two** documents declare a Link object
and **two** declare an Encoding object, and between them they declare *none* of the
five fields these six rows are about:

```console
$ scripts/fetch-corpus.sh          # all 91 link-ok rows, into .local/corpus/
$ uv run --no-project --quiet --with pyyaml python3 - <<'PY'
> import glob, os, yaml
> def links(n):
>     "every Link object: response-level, in components.responses, and components.links"
>     out = []
>     def take(m, where):
>         for k, v in (m or {}).items():
>             out.append((where, k, v if isinstance(v, dict) else {}))
>     def walk(x):
>         if isinstance(x, dict):
>             if isinstance(x.get('links'), dict): take(x['links'], 'response')
>             for v in x.values(): walk(v)
>         elif isinstance(x, list):
>             for v in x: walk(v)
>     walk(n.get('paths') or {})
>     walk((n.get('components') or {}).get('responses') or {})
>     take((n.get('components') or {}).get('links'), 'components.links')
>     return out
> tot = {}
> for f in sorted(glob.glob('.local/corpus/*/openapi.*')) + sorted(glob.glob('tests/fixtures/*/openapi.*')):
>     name = os.path.basename(os.path.dirname(f))
>     ls = links(yaml.safe_load(open(f)))
>     if not ls: continue
>     c = {'total': len(ls)}
>     for w, k, v in ls:
>         c[w] = c.get(w, 0) + 1
>         for field in ('description', 'requestBody', 'server', '$ref'):
>             if field in v: c[field] = c.get(field, 0) + 1
>     print(name, c)
>     for k, v in c.items(): tot[k] = tot.get(k, 0) + v
> print('TOTAL', tot)
> PY
apideck.com-crm {'total': 24, 'response': 24}
gambitcomm.local-mimic {'total': 16, 'response': 16}
TOTAL {'total': 40, 'response': 40}
```

Forty Link objects in the whole corpus, all response-level, and the counters for
`description`, `requestBody`, `server` and `$ref` never fire — so no key for them
appears at all. `components.links` is likewise absent from both documents:

```console
$ jq '.components | has("links")' .local/corpus/gambitcomm.local-mimic/openapi.json
false
$ jq '.components | has("links")' .local/corpus/apideck.com-crm/openapi.json
false
```

The Encoding census is the mirror image — the two fields the
`encoding-explode-or-allowReserved` row is about are declared **zero** times, while
`contentType`, `headers` and `style` are dense:

```console
$ uv run --no-project --quiet --with pyyaml python3 - <<'PY'
> import glob, os, yaml
> FIELDS = ('contentType', 'headers', 'style', 'explode', 'allowReserved')
> tot = {}
> for f in sorted(glob.glob('.local/corpus/*/openapi.*')) + sorted(glob.glob('tests/fixtures/*/openapi.*')):
>     name, c = os.path.basename(os.path.dirname(f)), {}
>     def walk(x):
>         if isinstance(x, dict):
>             for k, v in x.items():
>                 if k == 'content' and isinstance(v, dict):
>                     for mto in v.values():
>                         for e in ((mto or {}).get('encoding') or {}).values() if isinstance(mto, dict) else []:
>                             c['encoding'] = c.get('encoding', 0) + 1
>                             for fld in FIELDS:
>                                 if fld in (e or {}): c[fld] = c.get(fld, 0) + 1
>                 walk(v)
>         elif isinstance(x, list):
>             for v in x: walk(v)
>     walk(yaml.safe_load(open(f)))
>     if not c: continue
>     print(name, {k: c.get(k, 0) for k in ('encoding',) + FIELDS})
>     for k, v in c.items(): tot[k] = tot.get(k, 0) + v
> print('TOTAL', {k: tot.get(k, 0) for k in ('encoding',) + FIELDS})
> PY
free5gc-namf-communication {'encoding': 23, 'contentType': 23, 'headers': 14, 'style': 23, 'explode': 0, 'allowReserved': 0}
free5gc-pdu-session {'encoding': 99, 'contentType': 99, 'headers': 58, 'style': 99, 'explode': 0, 'allowReserved': 0}
TOTAL {'encoding': 122, 'contentType': 122, 'headers': 72, 'style': 122, 'explode': 0, 'allowReserved': 0}
```

A raw `grep` for `explode` in `free5gc-pdu-session` **does** hit, 58 times, and every
hit is a trap: it is the `explode` of a *Header* Object nested inside
`encoding.<part>.headers.<name>`, not the Encoding Object's own field. The census
above reads structure rather than text for exactly that reason.

So the route split is: `encoding-object` is Route 1, settled by a committed golden.
The other five are Route 2 — the corpus cannot answer them, and every one of them
was probed.

#### The container result, and what it does *not* finish

Both Link-declaring goldens discard the Link container whole, which is worth
recording because it is what makes the probe's silence unsurprising rather than
suspicious.

**`gambitcomm.local-mimic`, `CORPUS.md` row 47**
(`https://api.apis.guru/v2/specs/gambitcomm.local/mimic/21.00/openapi.json`) declares
16 response-level Link objects, of the `operationRef` + `parameters` form:

```console
$ jq '[.paths[][]? | objects | .responses? // {} | .[]? | objects
>   | select(.links) | .links[]] | length' .local/corpus/gambitcomm.local-mimic/openapi.json
16
$ jq -c '[.paths[][]? | objects | select(.responses) | .responses | to_entries[]
>   | select(.value.links) | {code:.key, links:.value.links}] | .[0]' \
>   .local/corpus/gambitcomm.local-mimic/openapi.json
{"code":"200","links":{"address":{"operationRef":"#/mimic/agent/{agentNum}/get/start","parameters":{"agentNum":"$request.body#/agentNum"}}}}
```

In its committed golden the string `link` occurs five times, in three files, and
every occurrence is the same word inside a docstring copied from the specification:

```console
$ grep -rl 'link' tests/fixtures/gambitcomm.local-mimic/expected/ | sort
tests/fixtures/gambitcomm.local-mimic/expected/reference.md
tests/fixtures/gambitcomm.local-mimic/expected/src/fern/valuespace/client.py
tests/fixtures/gambitcomm.local-mimic/expected/src/fern/valuespace/raw_client.py
$ grep -rho '[A-Za-z]*link[A-Za-z]*' tests/fixtures/gambitcomm.local-mimic/expected/ | sort | uniq -c
      5 linkUp
```

— from *"the commands below will send ifIndex.2 with a value of 5 in the linkUp trap
PDU."* Nothing in the golden derives from any of the 16 Link objects.

**`apideck.com-crm`, `CORPUS.md` row 10**
(`https://api.apis.guru/v2/specs/apideck.com/crm/9.3.0/openapi.json`) is the larger
witness — 24 Link objects, of the `operationId` + `parameters` form, carried on six
`components.responses` entries — and it is also a trap, because its golden emits
`src/fern/types/links.py` and `src/fern/types/social_link.py`. Those two files come
from schemas *named* `Links` and `SocialLink`, not from Link objects:

```console
$ jq -r '.components.schemas | keys[] | select(test("(?i)link"))' .local/corpus/apideck.com-crm/openapi.json
Links
SocialLink
$ jq -r '.components.schemas.Links.description' .local/corpus/apideck.com-crm/openapi.json
Links to navigate to previous or next pages through the API
```

`tests/fixtures/apideck.com-crm/expected/src/fern/types/links.py` opens on that
schema's own description, not on anything a Link object could supply:

```python
class Links(UniversalBaseModel):
    """
    Links to navigate to previous or next pages through the API
    """

    current: typing.Optional[str] = pydantic.Field(default=None)
```

The three link *names* that cannot come from anywhere else in that document settle
it — each is declared exactly once, as a key of a `links` map, and each reaches zero
bytes of the golden:

```console
$ for s in parentById pipelineById primarycontact; do
>   printf '%-16s source=%s golden=%s\n' "$s" \
>     "$(grep -o -F "$s" .local/corpus/apideck.com-crm/openapi.json | wc -l)" \
>     "$(grep -r -o -F "$s" tests/fixtures/apideck.com-crm/expected/ | wc -l)"
> done
parentById       source=1 golden=0
pipelineById     source=1 golden=0
primarycontact   source=1 golden=0
```

**This finishes none of the four link rows.** It establishes that Fern discards the
Link *container*, and a field cannot survive a container that is discarded — but
neither document declares `description`, `requestBody` or `server` on a Link, and
neither declares `components.links` at all, so on its own this reading is silence
about a shape that was never present. All four rows are therefore probed below, and
this container reading is corroboration, not their evidence.

#### `link-description`, `link-requestBody`, `link-server`, `components-links` — discards

**Route 2 — one probe carrying all four shapes.** Two response-level links on a
`201`: one inline, carrying `description`, `requestBody` and a `server` of its own,
and one that is a `$ref` to a `components.links` entry carrying the same three
fields under different, greppable values. In full:

```yaml
openapi: 3.0.3
info:
  title: link fields probe
  version: 1.0.0
servers:
  - url: https://api.example.com
paths:
  /things:
    post:
      operationId: createThing
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Thing"
      responses:
        "201":
          description: created
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Thing"
          links:
            GetThingByIdInline:
              operationId: getThing
              description: Look the created Thing up by its identifier.
              parameters:
                thingId: $response.body#/id
              requestBody: $response.body#/id
              server:
                url: https://inline-link.example.com
                description: InlineLinkServer
            GetThingByIdRef:
              $ref: "#/components/links/GetThingById"
  /things/{thingId}:
    get:
      operationId: getThing
      parameters:
        - name: thingId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Thing"
components:
  links:
    GetThingById:
      operationId: getThing
      description: Component level link description.
      parameters:
        thingId: $response.body#/id
      requestBody: $response.body#/id
      server:
        url: https://component-link.example.com
        description: ComponentLinkServer
  schemas:
    Thing:
      type: object
      properties:
        id:
          type: string
      required:
        - id
```

`fern check` **exit 0**, `fern generate` **exit 0**; neither said anything about a
Link. The generated tree contains no occurrence of the string `link` in any case,
anywhere — not one of the two link names, not either server URL or description, not
either link description:

```console
$ grep -ril 'link' preview/fern-python-sdk/ | wc -l
0
$ for s in inline-link.example.com component-link.example.com InlineLinkServer \
>          ComponentLinkServer GetThingByIdInline GetThingByIdRef GetThingById \
>          'Look the created Thing up' 'Component level link description'; do
>   printf '%-34s %s\n' "$s" "$(grep -r -o -F "$s" preview/fern-python-sdk/ | wc -l)"
> done
inline-link.example.com            0
component-link.example.com         0
InlineLinkServer                   0
ComponentLinkServer                0
GetThingByIdInline                 0
GetThingByIdRef                    0
GetThingById                       0
Look the created Thing up          0
Component level link description   0
```

The emitted `src/fern/raw_client.py` is the two operations the paths declare and
nothing else — `create_thing` returns the `201` body with no trace of either link:

```python
    def create_thing(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Thing]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Thing]
            created
        """
        _response = self._client_wrapper.httpx_client.request(
            "things",
            method="POST",
            json={
                "id": id,
            },
            request_options=request_options,
            omit=OMIT,
        )
```

`environment.py` keeps the root server alone, so neither Link `server` reached the
environment enum either — the same one-member shape the
[servers and XML](#round-4--servers-and-xml) family measured:

```python
class FernApiEnvironment(enum.Enum):
    DEFAULT = "https://api.example.com"
```

and `reference.md` documents exactly `client.create_thing(...)` and
`client.get_thing(...)`, with no follow-up relationship of any kind.

That is one probe settling four rows, and each of the four is settled by its own
marker rather than by the shared silence: `link-description` by
`Look the created Thing up` and `Component level link description`,
`link-requestBody` by both links carrying `requestBody: $response.body#/id` while
the emitted `get_thing` takes only `thing_id`, `link-server` by
`inline-link.example.com` / `component-link.example.com` reaching neither
`environment.py` nor any call site, and `components-links` by the `$ref` form
resolving to a component that emits nothing — `GetThingById` occurs zero times.

`link-server` carries a **+ supply** qualifier and `link-requestBody` and
`components-links` carry one too, and in all three cases the shortfall is about
*candidate documents*, not about Fern: the screens' own counts leave 1 eligible of
3, 2 of 3 and 2 of 4 respectively, each short of the primary-plus-two-backups bar.
The discard is measured; the shortfall is separate and would not save the row even
if it were made up.

#### `encoding-object` — implements `contentType`, discards `headers`

**Route 1. `free5gc-pdu-session`, `CORPUS.md` row 73**
(`https://raw.githubusercontent.com/free5gc/openapi/8d0ee35bc671dd9995240c0ff73d4c75075a204a/Nsmf_PDUSession/api/openapi.yaml`).
Its source declares 99 Encoding objects, 99 of them with a `contentType` and 58 with
per-part `headers` (census above). Five operations carry one on a request body, and
exactly one of the five declares `multipart/related` as its *only* request media
type:

```console
$ uv run --no-project --quiet --with pyyaml python3 - <<'PY'
> import yaml
> d = yaml.safe_load(open('.local/corpus/free5gc-pdu-session/openapi.yaml'))
> for p, item in d['paths'].items():
>     for m, op in item.items():
>         c = ((op or {}).get('requestBody') or {}).get('content') or {}
>         if any(isinstance(v, dict) and v.get('encoding') for v in c.values()):
>             print(f'{op["operationId"]:18} {list(c)}')
> PY
PostSmContexts     ['multipart/related']
UpdateSmContext    ['application/json', 'multipart/related']
ReleaseSmContext   ['application/json', 'multipart/related']
PostPduSessions    ['application/json', 'multipart/related']
UpdatePduSession   ['application/json', 'multipart/related']
```

For the other four Fern picks `application/json` and the multipart branch — encoding
and all — never runs; each of their emitted call sites carries a plain `json={…}`
and no `files=` at all. `PostSmContexts` is the one that exercises the Encoding
objects, and its source block is:

```yaml
          multipart/related:
            encoding:
              jsonData:
                contentType: application/json
                style: form
              binaryDataN1SmMessage:
                contentType: application/vnd.3gpp.5gnas
                headers:
                  Content-Id:
                    explode: false
                    schema:
                      type: string
                    style: simple
                style: form
```

`tests/fixtures/free5gc-pdu-session/expected/src/fern/sm_contexts_collection/raw_client.py`
emits both `contentType` values, verbatim, into the request:

```python
        _response = self._client_wrapper.httpx_client.request(
            "sm-contexts",
            method="POST",
            data={},
            files={
                **(
                    {"jsonData": (None, json.dumps(jsonable_encoder(json_data)), "application/json")}
                    if json_data is not OMIT
                    else {}
                ),
                **(
                    {
                        "binaryDataN1SmMessage": core.with_content_type(
                            file=binary_data_n1sm_message, default_content_type="application/vnd.3gpp.5gnas"
                        )
                    }
                    if binary_data_n1sm_message is not None
                    else {}
                ),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
```

`application/vnd.3gpp.5gnas` is what makes this unambiguous: it is a media type no
default could produce, and in the source it occurs 49 times and *only* under
`encoding.<part>.contentType`:

```console
$ grep -c 'vnd.3gpp.5gnas' .local/corpus/free5gc-pdu-session/openapi.yaml
49
$ grep -B4 'vnd.3gpp.5gnas' .local/corpus/free5gc-pdu-session/openapi.yaml \
>   | grep -c 'contentType: application/vnd.3gpp.5gnas'
49
```

`free5gc-namf-communication` (row 76) is the independent second witness — a
different repository, a different 3GPP service, 23 Encoding objects — and its golden
emits the same construct for all three binary parts of its one multipart-only
operation:

```console
$ grep -rn 'default_content_type=' tests/fixtures/free5gc-namf-communication/expected/src/ \
>   | sed 's/.*default_content_type=//' | sort | uniq -c
      2 "application/vnd.3gpp.5gnas"
      4 "application/vnd.3gpp.ngap"
```

**The `encoding` mentions elsewhere in these two goldens are Fern's static runtime,
not derived output.** Only two files in either tree mention the string, and both are
byte-identical across the entire corpus — including fixtures whose source declares
no Encoding object at all:

```console
$ grep -rl 'encoding' tests/fixtures/free5gc-pdu-session/expected/ | sort
tests/fixtures/free5gc-pdu-session/expected/src/fern/core/force_multipart.py
tests/fixtures/free5gc-pdu-session/expected/src/fern/core/http_client.py
$ md5sum tests/fixtures/*/expected/src/fern/core/force_multipart.py | awk '{print $1}' | sort | uniq -c
    104 b961c5766288e1da18883699e5227918
$ md5sum tests/fixtures/*/expected/src/fern/core/http_client.py | awk '{print $1}' | sort | uniq -c
    104 9f664ce11351b3f5597849f62b929542
$ diff tests/fixtures/free5gc-pdu-session/expected/src/fern/core/force_multipart.py \
>      tests/fixtures/apideck.com-crm/expected/src/fern/core/force_multipart.py && echo identical
identical
$ diff tests/fixtures/free5gc-pdu-session/expected/src/fern/core/http_client.py \
>      tests/fixtures/apideck.com-crm/expected/src/fern/core/http_client.py && echo identical
identical
```

`apideck.com-crm` declares no Encoding object anywhere (it does not appear in the
census above), so those two files carry the string for every golden regardless of
its source. One hash each across 104 trees: they are Fern's runtime, shipped
unconditionally.

**What Fern does *not* take from the Encoding object is `headers`.** The 58
`Content-Id` per-part headers in the source reach nothing:

```console
$ grep -c 'Content-Id' .local/corpus/free5gc-pdu-session/openapi.yaml
58
$ grep -ric 'content-id' tests/fixtures/free5gc-pdu-session/expected/ | awk -F: '{s+=$2} END{print s+0}'
0
```

**A probe confirms `contentType` independently, and on both part shapes.** The
golden alone leaves one ambiguity: `jsonData`'s declared `application/json` is also
what a JSON part would default to, so only the binary part's exotic media type
carries the finding. A probe operation using media types no default could invent
closes it — and reproduces the `headers` discard on a document that declares one
header and nothing else:

```yaml
  /multipart-encoding:
    post:
      operationId: multipartEncoding
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                meta:
                  $ref: "#/components/schemas/Thing"
                attachment:
                  type: string
                  format: binary
              required:
                - attachment
            encoding:
              meta:
                contentType: application/vnd.probe+json
                explode: true
                allowReserved: true
              attachment:
                contentType: application/vnd.probe-binary
                headers:
                  X-Probe-Header:
                    schema:
                      type: string
```

`fern generate` **exit 0**; `fern check` **exit 1**, caused by the `explode: true`
this same part carries — that field is the `encoding-explode-or-allowReserved` row
below and is isolated there, and it changes nothing about what was emitted. Both
declared media types land verbatim, the JSON part's as the third element of the
httpx file tuple and the binary part's as `with_content_type`'s default:

```python
        _response = self._client_wrapper.httpx_client.request(
            "multipart-encoding",
            method="POST",
            data={},
            files={
                **(
                    {"meta": (None, json.dumps(jsonable_encoder(meta)), "application/vnd.probe+json")}
                    if meta is not OMIT
                    else {}
                ),
                "attachment": core.with_content_type(
                    file=attachment, default_content_type="application/vnd.probe-binary"
                ),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
```

```console
$ for s in 'application/vnd.probe+json' 'application/vnd.probe-binary' 'X-Probe-Header'; do
>   printf '%-28s %s\n' "$s" "$(grep -r -o -F "$s" preview/fern-python-sdk/ | wc -l)"
> done
application/vnd.probe+json   2
application/vnd.probe-binary 2
X-Probe-Header               0
```

Two each — the sync and async client — for both `contentType` values, and zero for
the per-part header, on a document where nothing else could have supplied any of the
three.

**No `REGISTRABLE` entry is raised for this row, and the reason is not the semantic
bar — it is that the shape is already registered.** `CORPUS.md` rows 73 and 76 are
exactly this shape (row 73's `shapes` column reads *"multipart `encoding` properties
combining `contentType` and per-part `headers`"*), both are registered in
`tests/e2e.rs`, and both byte-match. A third fixture for a shape two goldens already
pin would add coverage of nothing.

#### `encoding-explode-or-allowReserved` — refuses one configuration, ignores six

**Route 2 — three probes.** Zero documents in the corpus declare either field, so
there is nothing to read; the row is answered by measuring seven configurations of
the two fields against controls that differ only in the field under test.

*Probe 1 — `application/x-www-form-urlencoded`, control vs. modified.* Two
operations over the same referenced schema; the second adds an `encoding` block and
changes nothing else:

```yaml
  /form-control:
    post:
      operationId: formControl
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: "#/components/schemas/FormBody"
      responses:
        "200": { description: ok, content: { application/json: { schema: { $ref: "#/components/schemas/Thing" } } } }
  /form-modified:
    post:
      operationId: formModified
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: "#/components/schemas/FormBody"
            encoding:
              tags:
                style: form
                explode: false
              filter:
                style: deepObject
                explode: true
              redirectUri:
                allowReserved: true
      responses:
        "200": { description: ok, content: { application/json: { schema: { $ref: "#/components/schemas/Thing" } } } }
```

(`FormBody` is `{tags: array<string> (required), filter: map<string,string>,
redirectUri: string}`.) The two emitted methods are byte-identical apart from the
URL path — `form_modified` is:

```python
        _response = self._client_wrapper.httpx_client.request(
            "form-modified",
            method="POST",
            data={
                "tags": tags,
                "filter": filter,
                "redirectUri": redirect_uri,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
```

`explode: false` on `tags` still sends the array under one `data` key; `explode:
true` + `style: deepObject` on `filter` still sends the map under one; and
`allowReserved: true` on `redirectUri` changes nothing. Neither field's name occurs
anywhere in the generated tree. This document also carries the `/multipart-encoding`
operation quoted above, so its `fern check` **exits 1** — on that operation alone,
for its `explode` — and `fern generate` **exits 0**; neither said anything about
`formControl` or `formModified`.

*Probe 2 — `multipart/form-data` on a list part, one control and three variants.*
Four operations over one `MpBody` (`metaList: array<Thing>`, `attachment: binary`
required), differing only in the `encoding.metaList` block: absent, `explode: true`,
`explode: false`, `allowReserved: true`. `fern check` **exit 0**, `fern generate`
**exit 0**, and all four emit the same method body:

```console
$ uv run --no-project --quiet python3 - <<'PY'
> import re
> src = open('preview/fern-python-sdk/src/fern/raw_client.py').read()
> def body(n):
>     m = re.search(r'\n    def %s\(.*?(?=\n    def |\nclass )' % n, src, re.S)
>     return m.group(0).replace(n, 'OP').replace(n.replace('_', '-'), 'OP-PATH').strip('\n')
> base = body('mp_control')
> for n in ('mp_explode_true', 'mp_explode_false', 'mp_allow_reserved'):
>     print(f'{n:20} {"IDENTICAL" if body(n) == base else "DIFFERS"}')
> PY
mp_explode_true      IDENTICAL
mp_explode_false     IDENTICAL
mp_allow_reserved    IDENTICAL
```

```python
        _response = self._client_wrapper.httpx_client.request(
            "mp-control",
            method="POST",
            data={
                "metaList": json.dumps(jsonable_encoder(meta_list)) if meta_list is not OMIT else OMIT,
            },
            files={
                "attachment": attachment,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
```

*Probe 3 — the one place either field changes an outcome.* Two operations over an
`MpBody` whose `meta` part is an **object** rather than a list, differing only in
`encoding.meta.explode: true`. `fern check` **exit 1**:

```console
$ fern check
Warnings for generators.yml:
	Using "api.path" is deprecated. Please use "api.specs[].openapi" or "api.specs[].asyncapi" instead.
[sdk] 1 error
    [error]
        path: __package__.yml -> service -> endpoints -> mpObjectExplode
        issue: meta is exploded and must be a list. Did you mean list<optional<Thing>>?

Found 1 error and 0 warnings in 0.001 seconds.
```

The control operation is not named; the error is caused by that one field. But it
is a validation-only consumption, and it does not stop generation:
`fern generate` prints the same `[error]` and still **exits 0**, and the code it
writes for `mp_object_explode` is byte-identical to `mp_object_control` — `meta` is
still `typing.Optional[Thing]`, not a list, and nothing is repeated:

```python
        _response = self._client_wrapper.httpx_client.request(
            "mp-object-explode",
            method="POST",
            data={
                "meta": json.dumps(jsonable_encoder(meta)) if meta is not OMIT else OMIT,
            },
            files={
                "attachment": attachment,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
```

**The two fields do not behave alike, so the row records both.** `explode: true` on
a non-list *multipart* part is **refused**: `fern check` exits 1 and names that one
operation, and a reader deciding whether a document is usable needs that — Fern
rejects it outright rather than quietly dropping a modifier. The other six
configurations are **ignored** at generate time: `explode` true or false on a list
part, `allowReserved` on either, and — note the asymmetry —
`explode: true` on a form-urlencoded *map* part, which is an object and is *not*
refused. Only the multipart form of the check reaches it.

So `explode` is read far enough to be *validated* and never far enough to be
*emitted*, and `allowReserved` is not even validated. Neither half is worth a
fixture, for different reasons: a document `fern check` rejects cannot become a
corpus row at all, and the ignored six would pin an unconditional default. The exit-1/exit-0 split is
also a fresh instance of the
[`fern check` / `fern generate` disagreement](#fern-check-passing-does-not-mean-the-generator-will),
in the direction the existing note does not cover: check fails, generate succeeds.

#### Nothing registrable, and what that leaves

No row in this family produces a `REGISTRABLE` entry. The four link rows are
discards; `encoding-explode-or-allowReserved` refuses in one configuration and
ignores in six, neither of which a fixture can pin; and the one shape Fern does
implement — `encoding.<part>.contentType` — is already pinned by two committed,
byte-matching goldens, so proposing a third would be work with no coverage behind
it.

The family also narrows the [servers and XML](#round-4--servers-and-xml) reading
rather than merely repeating it. That family concluded Fern's importer *"keeps one
server URL for the whole client and one wire format for every body."* The Encoding
result shows the second half of that is not a blanket rule: Fern does carry a
declared per-part media type into the request when the body is multipart-only. What
it drops is everything that is not a media type or a part's own shape — the Link
graph entirely, the per-part `headers`, and the `explode`/`allowReserved` modifiers,
one of which it rejects at check time rather than dropping quietly. The dividing
line is whether the document is describing *a body Fern will send* or *a
relationship between operations*; only the former has a slot.

### Round 4 — schema shapes

Seven rows, and they do not behave alike. Every verdict below is read off an
artifact Fern actually emitted on this host or off a committed golden; no verdict
rests on a minimal probe alone. **Three are
[implements](#how-to-read-a-verdict)** — Fern reads the shape and emits output
derived from it — which is the first time in this file that more than one row in a
family has reached that verdict. Two of the three are **`REGISTRABLE`** and carry
candidate sets below; the third is already pinned by a committed, byte-matching
golden. Two rows are **discards**, one is **coincidence** in the form the corpus
actually declares, and the seventh discards in a way that takes the whole
enclosing object with it.

Round 3's expectation that this family was the likeliest place for a real gap was
right. The eleven document-metadata rows measured before it produced exactly one
**implements** between them — `encoding.<part>.contentType`, already pinned by two
goldens — while this one family produced three, two of them registrable.

#### Which rows the corpus can answer — censused first

Route 1 needs the shape present in a golden's own source, quantified, before its
absence from the golden means anything. Censused across all 91 fetched `link-ok`
sources and all 31 vendored fixture specs, the corpus declares string `const`s
densely, nullable-via-`type`-array densely, **and neither of the two `const` types
these rows are about, nor a single multi-type array with two non-null members**:

```console
$ scripts/fetch-corpus.sh          # all 91 link-ok rows, into .local/corpus/
$ uv run --no-project --quiet --with pyyaml python3 - <<'PY'
> import glob, os, yaml, collections
> def walk(n):
>     yield n
>     if isinstance(n, dict):
>         for v in n.values(): yield from walk(v)
>     elif isinstance(n, list):
>         for v in n: yield from walk(v)
> tot, docs = collections.Counter(), collections.Counter()
> files = sorted(glob.glob('.local/corpus/*/openapi.*')) + sorted(glob.glob('tests/fixtures/*/openapi.*'))
> for f in files:
>     seen = set()
>     for n in walk(yaml.safe_load(open(f))):
>         if not isinstance(n, dict): continue
>         c = n.get('const')
>         k = ('const-boolean' if isinstance(c, bool) else
>              'const-integer' if isinstance(c, int) else
>              'const-string' if isinstance(c, str) else None)
>         if k: tot[k] += 1; seen.add(k)
>         t = n.get('type')
>         if isinstance(t, list):
>             k = ('type-array-multi-nonnull' if len([x for x in t if x != 'null']) >= 2
>                  else 'type-array-nullable')
>             tot[k] += 1; seen.add(k)
>     for k in seen: docs[k] += 1
> print('documents censused:', len(files))
> for k in ('const-string', 'const-boolean', 'const-integer',
>           'type-array-nullable', 'type-array-multi-nonnull'):
>     print(f'  {k}: {tot[k]} occurrences in {docs[k]} documents')
> PY
documents censused: 122
  const-string: 147 occurrences in 3 documents
  const-boolean: 0 occurrences in 0 documents
  const-integer: 0 occurrences in 0 documents
  type-array-nullable: 498 occurrences in 3 documents
  type-array-multi-nonnull: 0 occurrences in 0 documents
```

That walk visits *every* dict node in the document, including examples and vendor
extensions, so each zero is a strict upper bound rather than a sample. It also
settles the `frankfurter` question directly: `CORPUS.md` row 66 is registered for
"15 nullable-via-`type`-array schemas", and — before this round registered
`openepcis-dpp-ready` as row 93 — every one of the corpus's 498 `type`
arrays had exactly one non-null member.

The same census, run over the four schema-position boolean subschemas JSON Schema
allows, finds only one of them declared anywhere:

```console
$ uv run --no-project --quiet --with pyyaml python3 - <<'PY'
> import glob, os, yaml, collections
> SUB = ('items', 'additionalProperties', 'not', 'contains',
>        'unevaluatedProperties', 'propertyNames', 'if', 'then', 'else')
> LIST = ('allOf', 'anyOf', 'oneOf', 'prefixItems')
> tot, docs = collections.Counter(), collections.Counter()
> def schema(n, seen):
>     if not isinstance(n, dict) or id(n) in seen: return
>     seen.add(id(n))
>     props = n.get('properties')
>     for k, v in (props.items() if isinstance(props, dict) else ()):
>         if v is True: tot['property schema: true'] += 1
>         else: schema(v, seen)
>     for k in SUB:
>         if n.get(k) is True: tot[f'{k}: true'] += 1
>         else: schema(n.get(k), seen)
>     for k in LIST:
>         for v in (n.get(k) or []) if isinstance(n.get(k), list) else (): schema(v, seen)
> def roots(doc):
>     yield from ((doc.get('components') or {}).get('schemas') or {}).values()
>     def rec(x):
>         if isinstance(x, dict):
>             if isinstance(x.get('schema'), dict): yield x['schema']
>             for v in x.values(): yield from rec(v)
>         elif isinstance(x, list):
>             for v in x: yield from rec(v)
>     for k in ('paths', 'webhooks', 'components'): yield from rec(doc.get(k) or {})
> files = sorted(glob.glob('.local/corpus/*/openapi.*')) + sorted(glob.glob('tests/fixtures/*/openapi.*'))
> for f in files:
>     before, seen = dict(tot), set()
>     for r in roots(yaml.safe_load(open(f))): schema(r, seen)
>     for k in tot:
>         if tot[k] != before.get(k, 0): docs[k] += 1
> print('documents censused:', len(files))
> for k in sorted(tot): print(f'  {k}: {tot[k]} occurrences in {docs[k]} documents')
> PY
documents censused: 122
  additionalProperties: true: 217 occurrences in 30 documents
```

That walk follows only schema-valued keywords, which matters: a path-based walk
reports five `property schema: true` hits in `atlassian.com-jira` and `letta`, and
every one is a trap — the `True` sits at `…/properties/<name>/readOnly` or
`…/properties/<name>/nullable`, a *keyword* of a property's schema, not a property
whose schema **is** `true`. `additionalProperties: true` is the only boolean
subschema any of the 122 documents declares.

So the route split for this family is: `boolean-schema-true` (in the one form the
corpus declares), `nesting-depth-ge-15` and `normalization-collision` are Route 1,
settled by committed goldens. `const-boolean`, `const-integer`,
`type-array-multi-nonnull` and `cycle-via-additionalProperties` are Route 2 — but a
probe alone is a hypothesis about a two-property document, so **each of those four
was additionally carried on real candidate specifications**, fetched at a pinned
commit, licence-verified at source and generated on this host, with the verdict read
off the real document's emitted artifact. Where a probe and a real candidate could
disagree, the real candidate is the measurement; none of the four disagreed. `boolean-schema-true` needs both routes: the corpus declares only
`additionalProperties: true`, so `items: true` and the property position were
probed — and the property position was then re-measured on one of the row's own
real-world candidates, because the probe result was large enough to deserve a real
document behind it.

Every probe below was run through the workspace scaffold
`scripts/generate-fern-fixture.sh` builds — Fern CLI `5.67.1`, generator
`fernapi/fern-python-sdk:5.20.0` under `pydantic_config.enum_type: python_enums`,
`CI=true`/`GITHUB_ACTIONS=true`, `fern check` then
`fern generate --group python-sdk --local --preview --output <ws>/preview --force`.
The only diagnostic any of them produced is the scaffold's own doubled
`::warning:: Using "api.path" is deprecated` line, which every corpus generation
also emits; where a probe is described as saying nothing about its shape, that
warning is what it said instead.

#### `const-boolean` and `const-integer` — discards

**The baseline, Route 1. `tamoss`, `CORPUS.md` row 69**
(`https://raw.githubusercontent.com/livewyer-ops/tamoss/ccbef170204082f3ae3842c2ffee476f5008e1fb/src/openapi-contract.yaml`).
Its source declares **eight** `const` schemas and every one of the eight is
string-valued, each on a `type: string` property:

```console
$ grep -c '^ *const:' .local/corpus/tamoss/openapi.yaml
8
$ grep -B1 '^ *const:' .local/corpus/tamoss/openapi.yaml | grep -c 'type: string'
8
$ grep '^ *const:' .local/corpus/tamoss/openapi.yaml
                  const: flows/created
                  const: flows/updated
                  const: flows/deleted
                  const: flows/segments_added
                  const: flows/segments_deleted
                  const: sources/created
                  const: sources/updated
                  const: sources/deleted
```

A string `const` **does** reach Fern's output, as a single-member `StrEnum`.
`tests/fixtures/tamoss/expected/src/fern/types/post_flows_created_payload_event_type.py`
is, in full:

```python
import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostFlowsCreatedPayloadEventType(enum.StrEnum):
    FLOWS_CREATED = "flows/created"

    def visit(self, flows_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostFlowsCreatedPayloadEventType.FLOWS_CREATED:
            return flows_created()
```

That is what makes these two rows sharp rather than routine: a boolean or an
integer cannot be a `StrEnum` member, so Fern has to be doing something else.

**Two probes first, each carrying a string `const` as its own control**, so the
comparison against the `tamoss` baseline is inside one generation rather than across
two. They isolate the shape; the three real specifications below are what the
verdict rests on. The boolean probe, in full:

```yaml
openapi: 3.1.0
info:
  title: Const Boolean Probe
  version: 1.0.0
paths:
  /event:
    get:
      operationId: getEvent
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required: [event_type, is_final]
                properties:
                  event_type:
                    type: string
                    const: flows/created
                  is_final:
                    type: boolean
                    const: true
```

`fern check` **exit 0**, `fern generate` **exit 0**; neither said anything about a
`const`. `preview/fern-python-sdk/src/fern/types/get_event_response.py`:

```python
class GetEventResponse(UniversalBaseModel):
    event_type: GetEventResponseEventType
    is_final: bool
```

and `get_event_response_event_type.py` reproduces the `tamoss` shape exactly:

```python
class GetEventResponseEventType(enum.StrEnum):
    FLOWS_CREATED = "flows/created"

    def visit(self, flows_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventResponseEventType.FLOWS_CREATED:
            return flows_created()
```

The string `const` becomes a type; **`const: true` becomes a plain `bool`** — no
`typing.Literal[True]`, no default, no validator, no separate module. The integer
probe is that document again but for its `info.title`, with `is_final` replaced by
`schema_version: {type: integer, const: 3}`; `fern check` **exit 0**,
`fern generate` **exit 0**, same silence, and the same collapse:

```python
class GetEventResponse(UniversalBaseModel):
    event_type: GetEventResponseEventType
    schema_version: int
```

**The probes are the isolating control, not the finding.** Neither row's verdict is
left resting on a two-property document: three of the round-3 candidate
specifications were fetched at a pinned commit, licence-verified at source, and
carried through the same scaffold on this host. All three pass `fern check` **exit
0** and `fern generate` **exit 0**, and all three emit the bare type.

`omersiar/ript` (MIT,
`https://raw.githubusercontent.com/omersiar/ript/2766ac2460130b3c5cc365254760e807e65bf82a/openapi.yaml`,
8 paths / 8 operations) settles both rows in a single class, and carries its own
control. `ListTopicsUnavailableResponse.allOf[1]` declares five properties — three
integer `const`s, one boolean `const`, and one integer with a *different* constraint:

```json
"count":    {"type": "integer", "const": 0},
"total":    {"type": "integer", "const": 0},
"page":     {"type": "integer", "const": 1},
"limit":    {"type": "integer", "minimum": 1},
"has_more": {"type": "boolean", "const": false}
```

`list_topics_unavailable_response.py` emits all five identically — the three
`const`s, the `minimum`, and the boolean `const` are indistinguishable from a bare
`type`:

```python
class ListTopicsUnavailableResponse(ErrorResponse):
    topics: typing.List[typing.Any]
    count: int
    total: int
    page: int
    limit: int
    has_more: bool
```

`wink-wink-wink555/MarkiNote` (MIT,
`https://raw.githubusercontent.com/wink-wink-wink555/MarkiNote/71c239b7436dd2d071c98eeaada1b0b9b53cabb6/packages/api-client/openapi.json`,
24 paths / 29 operations) declares 13 boolean `const`s and one integer `const`, and
shows the loss is wider than the `const` keyword alone. `CreatedFileResponse.success`
is `{"const": true, "default": true, "type": "boolean"}` — a flag the document says
is always present and always `true`:

```python
class CreatedFileResponse(UniversalBaseModel):
    file_name: str
    path: str
    size: int
    success: typing.Optional[bool] = None
    version: str
```

Both the `const` **and** the `default` beside it reach zero bytes, and the field
comes out `typing.Optional[bool] = None`: the generated client will construct
`CreatedFileResponse(success=False)` without complaint. Its `ApiRootResponse.contract`,
`{"const": 1, "type": "integer"}`, likewise emits `contract: int`.

`tltv-org/protocol` (MIT,
`https://raw.githubusercontent.com/tltv-org/protocol/21fa80202825801b0ce152d367825987f1400f94/schemas/openapi.yaml`,
6 paths / 6 operations) is the third witness: `ChannelMetadata.v`,
`{type: integer, const: 1}`, emits `v: int`.

Both rows are **discards**, and the verdict rests on the three real specifications
rather than on the probes; the probes contribute only the string-`const` control
inside a single generation. Neither row is registrable: a fixture would pin `bool`
and `int`, the same bytes a schema with no `const` at all produces — and, in
`MarkiNote`'s case, it would pin an *optional* field the document declares required
and constant.

#### `type-array-multi-nonnull` — implements

**Route 2.** The census above shows no corpus document declares the shape, and the
`typing.Union[...]` occurrences already in the goldens do not settle it either:
those arise from `oneOf`/`anyOf`, which is a different keyword taking a different
code path. The probe therefore carries an `anyOf` control in the same document, plus
two further type arrays whose members differ, so that "the union is derived from the
declared list" is measured rather than assumed:

```yaml
openapi: 3.1.0
info:
  title: Multi-type Array Probe
  version: 1.0.0
paths:
  /value:
    get:
      operationId: getValue
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required: [multi_type, via_any_of, multi_type_bool_num, multi_type_three]
                properties:
                  multi_type:
                    type: [string, integer]
                  via_any_of:
                    anyOf:
                      - type: string
                      - type: integer
                  multi_type_bool_num:
                    type: [boolean, number]
                  multi_type_three:
                    type: [string, integer, boolean]
```

`fern check` **exit 0**, `fern generate` **exit 0**. Four named modules come out,
one per property, and the three type arrays each produce a union whose members are
exactly their declared non-null types, in the declared order:

```python
# get_value_response_multi_type.py
GetValueResponseMultiType = typing.Union[str, int]

# get_value_response_via_any_of.py          <- the anyOf control
GetValueResponseViaAnyOf = typing.Union[str, int]

# get_value_response_multi_type_bool_num.py
GetValueResponseMultiTypeBoolNum = typing.Union[bool, float]

# get_value_response_multi_type_three.py
GetValueResponseMultiTypeThree = typing.Union[str, int, bool]
```

`[boolean, number]` → `Union[bool, float]` and `[string, integer, boolean]` →
`Union[str, int, bool]` are what rule out a coincidence: no unconditional default
tracks the member list.

**Confirmed on the real candidates, at their use sites.** All three specifications
in the candidate set below were carried through the same scaffold on this host
(`fern check` **exit 0**, `fern generate` **exit 0**), and in each the union is a
*used* type, not an orphan alias. `openepcis/openepcis-dpp-ready` declares
`SingleValuedDataElement.value` as `type: [string, number, boolean]`:

```python
# single_valued_data_element.py
    value: typing.Optional[SingleValuedDataElementValue] = pydantic.Field(default=None)
# single_valued_data_element_value.py
SingleValuedDataElementValue = typing.Union[str, float, bool]
```

`nicholas-ruest/wildfire-robotics` is the sharpest of the three, because its array
has five members including `"null"` — `ReadModel.summary` is a map whose values are
`type: [string, number, integer, boolean, null]` — and every one of the five is
represented, the four non-null ones in the union and `"null"` as the `Optional`
wrapper around it:

```python
# read_model.py
    summary: typing.Dict[str, typing.Optional[ReadModelSummaryValue]]
# read_model_summary_value.py
ReadModelSummaryValue = typing.Union[str, float, int, bool]
```

`agentic-commerce-protocol` is the third: `IntentTrace.metadata`'s
`type: [string, number, boolean]` emits
`IntentTraceMetadataValue = typing.Union[str, float, bool]`.

The row is **implements**, and **`REGISTRABLE`** — see the candidate set below.

#### `cycle-via-additionalProperties` — implements

**Route 2.** No committed golden could answer this one, and the reason is precise:
335 golden files call `update_forward_refs`, so recursion *through `properties` and
`items`* is densely pinned — but **not one golden file in the corpus emitted a
forward-referenced map**, which is the artifact a cycle through
`additionalProperties` produces. Measured on the 105 `expected/` trees that stood
before this round registered one:

```console
$ ls -d tests/fixtures/*/expected | wc -l
105
$ grep -rl 'update_forward_refs' tests/fixtures/*/expected/ | wc -l
335
$ grep -rl 'typing\.Dict\[str, "' tests/fixtures/*/expected/ | wc -l
0
```

That last zero is the gap, and registering `eozilla` is what closed it — re-taken
over the finished tree it now reads **2**, both files under
`tests/fixtures/eozilla/`, and nowhere else
([audit](#round-4--audit-of-the-eighteen)).

The probe is a map of self, the shape a `Field` whose child fields are keyed by
name:

```yaml
openapi: 3.1.0
info:
  title: Map-of-self Cycle Probe
  version: 1.0.0
paths:
  /field:
    get:
      operationId: getField
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Field'
components:
  schemas:
    Field:
      type: object
      required: [name]
      properties:
        name:
          type: string
        fields:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/Field'
```

`fern check` **exit 0**, `fern generate` **exit 0**.
`preview/fern-python-sdk/src/fern/types/field.py` is, in full:

```python
from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Field(UniversalBaseModel):
    name: str
    fields: typing.Optional[typing.Dict[str, "Field"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Field)
```

Three separate bytes derive from the cycle and from nothing else: the
`from __future__ import annotations` header, the quoted `"Field"` inside the map,
and the trailing `update_forward_refs(Field)`.

**Confirmed on the real candidates.** All three specifications in the candidate set
below were carried through the same scaffold on this host (`fern check` **exit 0**,
`fern generate` **exit 0**), and each emits the same three artifacts on its own
cycle. `eo-tools/eozilla`'s `Schema.properties` is a map of `Schema`:

```console
$ grep -n 'from __future__\|properties:\|update_forward_refs' \
>   preview/fern-python-sdk/src/fern/types/schema.py
3:from __future__ import annotations
9:from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
69:    properties: typing.Optional[typing.Dict[str, "Schema"]] = None
112:update_forward_refs(
```

`sam0delkin/intellij-psa` emits
`options: typing.Optional[typing.Dict[str, "PsiElementModelChild"]] = None` for its
two-hop cycle, and `gonecentrix/gcx-access-control-management` emits
`properties: typing.Optional[typing.Dict[str, "Schema"]] = None`.

The row is **implements**, and **`REGISTRABLE`**.

#### `boolean-schema-true` — coincidence, except in the property position

**Route 1 for the one form the corpus declares.** `additionalProperties: true` on a
schema with no `properties` of its own emits a free-form map — and so does a bare
`type: object` that says nothing about additional properties at all. Two committed
goldens make the comparison directly.

`etsi.local-mec010-2_apppkgmgmt`, `CORPUS.md` row 46, declares
`KeyValuePairs` as `{additionalProperties: true, description: …, type: object}`, and
`tests/fixtures/etsi.local-mec010-2_apppkgmgmt/expected/src/fern/types/key_value_pairs.py`
is, in full:

```python
import typing

KeyValuePairs = typing.Dict[str, typing.Any]
"""
'This data type represents a list of key-value pairs. The order of the pairs in the list is not significant. In JSON, a set of key-value pairs is represented as an object. It shall comply with the provisions defined in clause 4 of IETF RFC 8259'
"""
```

`anchore.io`, `CORPUS.md` row 3, declares `Annotations` as
`{description: …, type: object}` — **no `additionalProperties` key at all** — and
`tests/fixtures/anchore.io/expected/src/fern/types/annotations.py` is, in full:

```python
import typing

Annotations = typing.Dict[str, typing.Any]
"""
Simple key/value pairs where the value may be optional
"""
```

Same type, from a source that never declared the keyword. The with-`properties`
form is the same story: `tamoss`'s `ErrorPayload` carries
`additionalProperties: true` beside five properties and emits no map field at all,
only `extra="allow"` — and `tamoss`'s own `HttpRequest`, which declares no
`additionalProperties`, emits the identical `extra="allow"` block, because that is
the generator's `pydantic_config.extra_fields` default and every model in every
golden carries it.

**Route 2 for `items: true`**, which none of the 122 documents declares. One probe
carries it and `additionalProperties: true` each beside a bare-container control:

```yaml
                properties:
                  name:
                    type: string
                  list_of_anything:
                    type: array
                    items: true
                  control_list:
                    type: array
                  free_map:
                    type: object
                    additionalProperties: true
                  control_map:
                    type: object
```

`fern check` **exit 0**, `fern generate` **exit 0**, and the boolean subschema and
its control are indistinguishable in the output:

```python
class GetThingResponse(UniversalBaseModel):
    name: str
    list_of_anything: typing.List[typing.Any]
    control_list: typing.List[typing.Any]
    free_map: typing.Dict[str, typing.Any]
    control_map: typing.Dict[str, typing.Any]
```

That is a [coincidence](#how-to-read-a-verdict) in the exact sense this file
defines: Fern's output equals the standard's meaning, produced by an unconditional
default rather than by reading the keyword. A fixture would pin the default.

**The property position is different, and it is not a coincidence.** The module is
still written, but there is no model inside it: Fern emits the enclosing object as a
bare `typing.Any` alias carrying only its description, and every property it
declared — the boolean-schema one and its ordinary siblings alike — is gone with the
class that would have held them. That was measured on a real specification rather
than inferred from the probe, because this row's own candidates declare the form.

`rocketmq-sre-phase02.openapi.json`
(`https://raw.githubusercontent.com/mxsm/rocketmq-rust/91dceb7e7be6e1321aa954fdf44739143377f297/rocketmq-sre/openapi/rocketmq-sre-phase02.openapi.json`)
was carried through the same scaffold on this host: `fern check` **exit 0**,
`fern generate` **exit 0**, `Found 0 errors and 2 warnings`, both warnings the
`api.path` deprecation. It emits **286** type modules from **253** component
schemas, and exactly **four** of those modules hold a `typing.Any` alias instead of
a class:

```console
$ ls preview/fern-python-sdk/src/fern/types/*.py | wc -l
286
$ grep -h '= typing.Any$' preview/fern-python-sdk/src/fern/types/*.py
ActionItem = typing.Any
PostmortemRevision = typing.Any
IncidentOperationResultTimelineEvent = typing.Any
WhatIfSimulation = typing.Any
```

The correlation is exact, not approximate. Of the 253 component schemas, exactly
**four** declare a property whose schema is literally `true` **directly on the
schema**, five such properties between them — `WhatIfSimulation.input`,
`WhatIfSimulation.projected_utilization`, `PostmortemRevision.timeline`,
`ActionItem.execution_journal` and
`IncidentOperationResult__TimelineEvent.details` — and those four schemas are the
four aliases above, name for name. No other schema in the document collapses, and
none of these four survives.

`WhatIfSimulation` declares sixteen properties, two of them `true`.
`what_if_simulation.py` is, in full:

```python
import typing

WhatIfSimulation = typing.Any
"""
Read-only what-if result. It never carries an executable action.
"""
```

Fourteen ordinary property schemas — `algorithm_version`, `cluster_id`, `status`,
`created_at` and ten more — reach zero bytes because of two siblings, and nothing in
either exit code or in the logs says so. What survives is only what was declared
*elsewhere*: the six `WhatIfSimulation__*` components
(`ClusterId`, `EvidenceId`, `SimulationId`, `SimulationKind`, `SimulationStatus`,
`TenantId`) still emit their own modules, because they are components in their own right, not inline
subschemas of the collapsed object — nothing references them from `WhatIfSimulation`
any more.

The loss reaches the client surface, and the same method shows the contrast. The
request body of `run_what_if_simulation` declares no boolean-schema property and is
emitted as fully typed keyword arguments; its response is the collapsed schema:

```python
# raw_client.py:3136
        current_utilization: typing.Optional[float] = OMIT,
        evidence_ids: typing.Optional[typing.Sequence[WhatIfSimulationRequestEvidenceId]] = OMIT,
        instance_delta: typing.Optional[int] = OMIT,
        queue_delta: typing.Optional[int] = OMIT,
        target_version: typing.Optional[str] = OMIT,
        traffic_increase_percent: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WhatIfSimulation]:
```

`HttpResponse[WhatIfSimulation]` is `HttpResponse[typing.Any]`.

**A probe isolates the rule**, because the real document cannot separate position
from `required`. Two operations, one document:

```yaml
paths:
  /top-optional:
    get:
      operationId: getTopOptional
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required: [name]
                properties:
                  name:
                    type: string
                  anything: true
  /nested-required:
    get:
      operationId: getNestedRequired
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required: [nested]
                properties:
                  nested:
                    type: object
                    required: [inner_name, inner_anything]
                    properties:
                      inner_name:
                        type: string
                      inner_anything: true
```

`fern check` **exit 0**, `fern generate` **exit 0**. The generated tree holds one
type module, not two, and `name` — a sibling that declared nothing unusual — is gone
with the model that would have held it:

```console
$ ls preview/fern-python-sdk/src/fern/types/
__init__.py
get_nested_required_response.py
$ grep -n 'def get' preview/fern-python-sdk/src/fern/raw_client.py
20:    def get_top_optional(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.Any]:
58:    def get_nested_required(
101:    async def get_top_optional(
141:    async def get_nested_required(
```

```python
# get_nested_required_response.py — the only type module emitted
class GetNestedRequiredResponse(UniversalBaseModel):
    nested: typing.Any
```

The rule is position, not `required`: `anything` was **optional** and still took the
whole top-level response model with it, while the nested object — whose boolean
property *was* required — collapsed to `typing.Any` and left its parent standing. An
earlier single-operation probe in which the boolean property sat on the top-level
response schema produced no `types/` package at all and a bare
`HttpResponse[typing.Any]`, which is the same rule with nothing above it to survive.

Probe and real candidate agree here, which is worth stating because they need not
have: the probe's collapse could have been an artefact of a two-property document.
`rocketmq-sre-phase02` is a 253-schema specification and it collapses in exactly the
same way, on schemas of sixteen properties. Where a probe and a real candidate
disagree, the real candidate is the measurement and the probe is the hypothesis.

One position escapes it. `rocketmq-sre-phase02`'s sixth and last declaration sits
in a discriminated `oneOf` branch (`EvidenceSnapshot__EvidenceContent.oneOf[0]
.properties.value`), and there the branch model survives with the property typed
`typing.Any` rather than the model collapsing:

```python
class EvidenceSnapshotEvidenceContent_Inline(UniversalBaseModel):
    value: typing.Any
    storage: typing.Literal["inline"] = "inline"
```

The row's verdict is therefore split, and it is not registrable either way: the
`additionalProperties`/`items` forms would pin an unconditional default, and the
property form makes the golden emit strictly less than the document declares —
`WhatIfSimulation` is what a fixture from this row's own candidate pool would pin.
Its four verified candidates are also **not four independent witnesses**: three are
files from the single repository `mxsm/rocketmq-rust` at one pinned commit
(`91dceb7e7be6e1321aa954fdf44739143377f297`), leaving `secunet-AG/hwaas` as the only
other. Both repositories declare Apache-2.0 at source, which is worth stating because
the round-3 screen rendered `mxsm/rocketmq-rust` as `APACHE-2.0` under one gap and
`None` under another:

```console
$ gh api repos/mxsm/rocketmq-rust --jq '.license.spdx_id'
Apache-2.0
$ gh api repos/secunet-AG/hwaas --jq '.license.spdx_id'
Apache-2.0
```

Across the four candidate files the three forms are declared 44, 32 and 2 times —
and the property form, the destructive one, is the one crozier's whole 122-document
corpus never declares:

```console
$ R=https://raw.githubusercontent.com/mxsm/rocketmq-rust/91dceb7e7be6e1321aa954fdf44739143377f297/rocketmq-sre/openapi
$ for n in 02 03 05; do curl -sSO "$R/rocketmq-sre-phase$n.openapi.json"; done
$ curl -sSo hwaas-contextapi.json \
>   https://raw.githubusercontent.com/secunet-AG/hwaas/dcf11f0ee1836559c511d5e18e8c9b4d6aa38984/expected-oas/contextapi.openapi.json
$ uv run --no-project --quiet python3 - <<'PY'
> import glob, json, collections
> SUB, LIST = ('items', 'additionalProperties'), ('allOf', 'anyOf', 'oneOf')
> for f in sorted(glob.glob('*.json')):
>     tot, seen = collections.Counter(), set()
>     def schema(n):
>         if not isinstance(n, dict) or id(n) in seen: return
>         seen.add(id(n))
>         for v in (n.get('properties') or {}).values():
>             if v is True: tot['property'] += 1
>             else: schema(v)
>         for k in SUB:
>             if n.get(k) is True: tot[k] += 1
>             else: schema(n.get(k))
>         for k in LIST:
>             for v in n.get(k) or []: schema(v)
>     for v in (json.load(open(f)).get('components') or {}).get('schemas', {}).values(): schema(v)
>     print(f, dict(tot))
> PY
hwaas-contextapi.json {'additionalProperties': 31, 'property': 6, 'items': 2}
rocketmq-sre-phase02.openapi.json {'additionalProperties': 3, 'property': 6}
rocketmq-sre-phase03.openapi.json {'additionalProperties': 3, 'property': 10}
rocketmq-sre-phase05.openapi.json {'additionalProperties': 7, 'property': 10}
```

#### `nesting-depth-ge-15` — implements

**Route 1. `openbanking.org.uk-account-info-openapi`, `CORPUS.md` row 58**
(`https://api.apis.guru/v2/specs/openbanking.org.uk/account-info-openapi/3.1.7/openapi.json`),
registered in `tests/e2e.rs` with `unmatched: &[]`. Its source reaches inline depth
**19**, with **91** inline schema nodes at depth ≥ 15:

```console
$ uv run --no-project --quiet --with pyyaml python3 - <<'PY'
> import json
> d = json.load(open('.local/corpus/openbanking.org.uk-account-info-openapi/openapi.json'))
> best, deep = (0, []), 0
> def rec(n, depth, path):
>     global best, deep
>     if depth >= 15: deep += 1
>     if depth > best[0]: best = (depth, path)
>     if not isinstance(n, dict): return
>     for pn, pv in (n.get('properties') or {}).items():
>         if isinstance(pv, dict): rec(pv, depth + 1, path + [f'properties/{pn}'])
>     for k in ('items', 'additionalProperties'):
>         if isinstance(n.get(k), dict): rec(n[k], depth + 1, path + [k])
>     for k in ('allOf', 'anyOf', 'oneOf'):
>         for i, v in enumerate(n.get(k) or []):
>             if isinstance(v, dict): rec(v, depth + 1, path + [f'{k}/{i}'])
> for s, v in d['components']['schemas'].items():
>     if isinstance(v, dict): rec(v, 1, [s])
> print('max inline depth:', best[0])
> print('inline schema nodes at depth >= 15:', deep)
> print(' -> '.join(best[1]))
> PY
max inline depth: 19
inline schema nodes at depth >= 15: 91
OBReadProduct2 -> properties/Data -> properties/Product -> items -> properties/OtherProductType -> properties/Overdraft -> properties/OverdraftTierBandSet -> items -> properties/OverdraftTierBand -> items -> properties/OverdraftFeesCharges -> items -> properties/OverdraftFeeChargeDetail -> items -> properties/OverdraftFeeChargeCap -> items -> properties/OtherFeeType -> items -> properties/Code
```

Fern names the deepest of them by concatenating every segment of that chain. The
golden's longest module is 230 characters of filename, and it is a fully populated
model, not a fallback:

```console
$ ls tests/fixtures/openbanking.org.uk-account-info-openapi/expected/src/fern/types \
>   | awk '{print length($0), $0}' | sort -rn | head -1
230 ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item.py
```

```python
class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem(
    UniversalBaseModel
):
    """
    Other fee type code which is not available in the standard code set
    """

    code: typing_extensions.Annotated[
        typing.Optional[ObCodeMnemonic], FieldMetadata(alias="Code"), pydantic.Field(alias="Code")
    ] = None
    description: typing_extensions.Annotated[
        Description3, FieldMetadata(alias="Description"), pydantic.Field(alias="Description")
    ]
    name: typing_extensions.Annotated[Name4, FieldMetadata(alias="Name"), pydantic.Field(alias="Name")]
```

No truncation, no `typing.Any`, no depth limit: the row is **implements**. It
proposes no fixture and no `REGISTRABLE` entry, because the behaviour is already
pinned — `CORPUS.md` row 58 is registered and byte-matching, and crozier reproduces
that 230-character module name byte-for-byte today.

#### `normalization-collision` — discards

**Route 1, same document.** `openbanking.org.uk-account-info-openapi` declares two
pairs of component schemas whose names differ only in an underscore, and each pair
normalizes to one Python name. The two members of a pair are not the same type:

```console
$ jq -r '.components.schemas | to_entries[]
>   | select(.key|test("^OB_?Rate1_[01]$"))
>   | "\(.key)\t\(.value.type)\t\(.value.description)"' \
>   .local/corpus/openbanking.org.uk-account-info-openapi/openapi.json
OBRate1_0	number	Rate charged for Statement Fee (where it is charged in terms of a rate rather than an amount)
OBRate1_1	number	field representing a percentage (e.g. 0.05 represents 5% and 0.9525 represents 95.25%). Note the number of decimal places may vary.
OB_Rate1_0	string	Rate charged for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
OB_Rate1_1	string	Rate charged for Fee/Charge (where it is charged in terms of a rate rather than an amount)
```

Four schemas in; **two** modules out, and the survivor of each pair is the `string`
one:

```console
$ ls tests/fixtures/openbanking.org.uk-account-info-openapi/expected/src/fern/types \
>   | grep -i 'rate1'
ob_rate10.py
ob_rate11.py
```

```python
# ob_rate10.py, in full
ObRate10 = str
"""
Rate charged for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
"""
```

The loss is not confined to the discarded declaration. `OBStatement2` `$ref`s
`OBRate1_0`, the `number`, at `properties/StatementFee/items/properties/Rate` — and
the golden types that field with the `str` that replaced it:

```python
# ob_statement2statement_fee_item.py
    rate: typing_extensions.Annotated[
        typing.Optional[ObRate10], FieldMetadata(alias="Rate"), pydantic.Field(alias="Rate")
    ] = None
```

A second, independent witness shows the collapse is not specific to that document.
`amazonaws.com-cloudformation`, `CORPUS.md` row 51, also registered with
`unmatched: &[]`, declares `RoleArn` and `RoleARN` — different constraints, both
referenced, one of them eleven times:

```console
$ jq -r '.components.schemas | to_entries[]
>   | select(.key|test("^RoleAr?n$";"i"))
>   | "\(.key)\ttype=\(.value.type)\tminLength=\(.value.minLength)"' \
>   .local/corpus/amazonaws.com-cloudformation/openapi.json
RoleArn	type=string	minLength=1
RoleARN	type=string	minLength=20
$ ls tests/fixtures/amazonaws.com-cloudformation/expected/src/fern/types | grep '^role'
role_arn.py
```

```python
# role_arn.py, in full
RoleArn = str
```

`fern check` and `fern generate` both pass on these documents — the corpus goldens
exist — and neither says anything about a collision. Fern accepts the second
declaration, emits nothing derived from it, and silently retypes every reference to
it: **discards**. It is not registrable for the ordinary reason plus a sharper one —
a fixture would pin the *loss*, and both documents that exhibit it are already
registered and byte-matching, so crozier already reproduces the loss exactly.

#### `REGISTRABLE` — two candidate sets

Neither is registered here; `justfile`, `tests/e2e.rs` and `tests/fixtures/CORPUS.md`
belong to the registering node. Every candidate below was carried end to end on this
host under the pins above: `fern check` **exit 0**, `fern generate` **exit 0**, and
the shape's artifact present in the generated tree. That is a stronger bar than the
round-3 screens applied, and it is the bar that matters, because
[`tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md) records that Fern's own
gate is what kills most raw public specs.

Licences were re-verified at each source repository rather than copied from the
round-3 candidate lists:

```console
$ for r in eo-tools/eozilla sam0delkin/intellij-psa \
>          gonecentrix/gcx-access-control-management \
>          openepcis/openepcis-dpp-ready nicholas-ruest/wildfire-robotics \
>          agentic-commerce-protocol/agentic-commerce-protocol; do
>   printf '%-45s %s\n' "$r" "$(gh api repos/$r --jq '.license.spdx_id')"
> done
eo-tools/eozilla                              Apache-2.0
sam0delkin/intellij-psa                       MIT
gonecentrix/gcx-access-control-management     MIT
openepcis/openepcis-dpp-ready                 Apache-2.0
nicholas-ruest/wildfire-robotics              MIT
agentic-commerce-protocol/agentic-commerce-protocol Apache-2.0
```

**`cycle-via-additionalProperties`** — Fern emits `from __future__ import
annotations`, a forward-referenced `typing.Dict[str, "<Schema>"]`, and a trailing
`update_forward_refs(...)`. Three witnesses, three different projects:

| role | pinned URL | licence | cyclic `additionalProperties` edges | emitted |
|---|---|---|---:|---|
| primary | `https://raw.githubusercontent.com/eo-tools/eozilla/70187a1bba9fe5a77001a623322f23bb30ea49c7/tools/openapi.yaml` | Apache-2.0 | 3 | `properties: typing.Optional[typing.Dict[str, "Schema"]] = None` |
| backup | `https://raw.githubusercontent.com/sam0delkin/intellij-psa/079c0377d4e33dab1b18a97a539c30580595f4b7/doc/schema.yaml` | MIT | 1 | `options: typing.Optional[typing.Dict[str, "PsiElementModelChild"]] = None` |
| backup | `https://raw.githubusercontent.com/gonecentrix/gcx-access-control-management/e472a0819f1423fae10f9ac8ee0c01139c79f0ea/admin-interface/src/main/resources/openapi/openapi.json` | MIT | 3 | `properties: typing.Optional[typing.Dict[str, "Schema"]] = None` |

`eo-tools/eozilla` is the primary rather than round 3's `sam0delkin/intellij-psa`
because its three cycles are *direct* — `Schema.properties.<k> → Schema` — where the
`intellij-psa` cycle is two hops
(`PsiElementModel -[additionalProperties]→ PsiElementModelChild → PsiElementModel`),
and because it carries nine operations to `intellij-psa`'s six. `intellij-psa` is a
sound backup, but the round-3 lead's shape claim needed the indirect edge to hold at
all, which a direct self-reference check does not find.

**`type-array-multi-nonnull`** — Fern emits a `typing.Union[...]` whose members are
the declared non-null types. Three witnesses:

| role | pinned URL | licence | multi-non-null `type` arrays | emitted |
|---|---|---|---:|---|
| primary | `https://raw.githubusercontent.com/openepcis/openepcis-dpp-ready/5c1f308d350cfcc9abb80aa6c70262c87141f201/extensions/common/interop/api/en18222-dpp-api.openapi.yaml` | Apache-2.0 | 2 | `SingleValuedDataElementValue = typing.Union[str, float, bool]` |
| backup | `https://raw.githubusercontent.com/nicholas-ruest/wildfire-robotics/29077c9f6536fb649673b93a185ea1cbc5c35a01/contracts/openapi/wildfire-api-v1.yaml` | MIT | 1 | `ReadModelSummaryValue = typing.Union[str, float, int, bool]` |
| backup | `https://raw.githubusercontent.com/agentic-commerce-protocol/agentic-commerce-protocol/32b1cad685b566fdab43e0c73f2773fd578c8478/spec/2025-12-12/openapi/openapi.agentic_checkout.yaml` | Apache-2.0 | 1 | `IntentTraceMetadataValue = typing.Union[str, float, bool]` |

Two of round 3's leads for this gap are disqualified, and neither is a licence
problem — both are schema libraries with no `paths`, so Fern generates a complete,
valid, **empty** SDK from them and they can never be fixtures:

```console
$ uv run --no-project --quiet --with pyyaml python3 -c '
> import sys, yaml
> for f in sys.argv[1:]:
>     d = yaml.safe_load(open(f))
>     print(f, "paths=", len(d.get("paths") or {}),
>              "schemas=", len((d.get("components") or {}).get("schemas") or {}))' \
>   allez/condarc_openapi.json opensearch/security._common.yaml
allez/condarc_openapi.json paths= 0 schemas= 23
opensearch/security._common.yaml paths= 0 schemas= 52
```

`nteract/allez` was round 3's **primary** for this gap on a count of 14 occurrences;
the occurrences are real and the BSD-3-Clause licence checks out, but a zero-path
document is the failure mode this file already records under
[28 candidates generated a complete, valid, *empty* SDK](#28-candidates-generated-a-complete-valid-empty-sdk).
The `agentic-commerce-protocol` entry is likewise **one** witness and not four: the
repository holds six dated copies of the same specification
(`spec/2025-09-29`, `2025-12-12`, `2026-01-16`, `2026-01-30`, `2026-04-17`,
`unreleased`), and the round-3 list named four of them separately.

#### What this family changes about the round's headline

Round 3's result was that four gaps of fifty-nine cleared the registration bar, and
Round 4's first eleven rows added one already-pinned `implements` to that: server
metadata, XML bodies and Link objects are shapes Fern's importer flattens, and the
one Encoding field it reads is registered twice over already. This family is the
counterweight. Fern's **type system** is real — multi-type arrays become unions,
map-of-self becomes a forward-referenced map, and eighteen levels of inline nesting
become eighteen named models with no fallback anywhere in the chain. What it drops
is the *annotation beside* the type: a `const` next to a `type`, a boolean subschema
in place of one, the second of two names that normalize alike. The dividing line in
[servers and XML](#round-4--servers-and-xml) was whether a document is describing a
body Fern will send; here it is whether the document is describing a **shape** or a
**constraint on** a shape. Shapes survive. Constraints beside them do not.

### Round 4 — what the round registered

The measurement phase reported exactly two rows as **`REGISTRABLE`**:
`cycle-via-additionalProperties` and `type-array-multi-nonnull`. Both are now
corpus fixtures, and no other row is — the remaining sixteen are discards,
coincidences, refusals, or `implements` already pinned by a registered golden.
Round 4 therefore registers **two** rows where round 3 registered four, and where
[servers and XML](#round-4--servers-and-xml) and
[links and encoding](#round-4--links-and-encoding) between them registered none.

`cycle-via-additionalProperties` is `CORPUS.md` row 92, `eozilla`
(`eo-tools/eozilla@70187a1b`, `tools/openapi.yaml`);
`type-array-multi-nonnull` is row 93, `openepcis-dpp-ready`
(`openepcis/openepcis-dpp-ready@5c1f308d`,
`extensions/common/interop/api/en18222-dpp-api.openapi.yaml`). Each candidate
set's primary carried, so no backup was needed. Both licences were re-verified at
the source repository at the pinned ref rather than inherited from the round-3
screens: each repository's `LICENSE` opens `Apache License / Version 2.0, January
2004`, and `eozilla`'s document repeats it in `info.license` as
`Apache 2.0 license`. Both raw documents pass `fern check` at exit 0 with none of
the three documented killers present — zero inline (non-`$ref`) request bodies,
zero `format: date` fields whose example carries a time, zero unnamed integer
enums — and both generated at `fernapi/fern-python-sdk:5.20.0` at exit 0.

Both goldens carry the artifact their row predicted.
`eozilla`'s `types/schema.py` emits
`properties: typing.Optional[typing.Dict[str, "Schema"]] = None` under
`from __future__ import annotations` with a trailing `update_forward_refs(`;
`openepcis-dpp-ready` emits
`SingleValuedDataElementValue = typing.Union[str, float, bool]` in a module of its
own. Both rows are registered with `unmatched: &[]` — no exclusion — and their
byte-match is proven by `just test-corpus-match`, whose
`eozilla_matches_fern_output` and `openepcis_dpp_ready_matches_fern_output` lines
pass over all 105 and 90 expected files respectively.

Reproducing them cost eleven generator repairs and no golden edit. Two of the
eleven are worth recording here because they are Fern *behaviours* this file had
not measured, and both were probed directly rather than inferred: a union member
declared `format: binary` renders as the `string` it is declared as
(`oneOf: [{type: string, format: binary}, {type: integer}]` generates
`typing.Union[str, int]`, not `bytes`), and equal union members fold together
where the **last** of them stood (`oneOf: [string, integer, string/uri]` generates
`typing.Union[int, str]`). The third probe measured a member declaring nothing but
`nullable: true` as `typing.Optional[typing.Any]`.

### Round 4 — audit of the eighteen

A fifth pass, reading the four measurement subsections above as a whole rather
than row by row on their own branches. It changed no `expected/` tree, deleted no
`.crozier-fern-golden.json` marker, and touched neither `justfile`, `tests/e2e.rs`
nor `tests/fixtures/CORPUS.md`. Every figure below was re-measured in this
checkout on 2026-08-22, against fetched specifications and committed goldens
rather than against the prose.

**All eighteen clear the three mechanical bars.** None still reads `unmeasured`;
every verdict is drawn from the vocabulary
[`How to read a verdict`](#how-to-read-a-verdict) defines (`implements`,
`discards`, `ignores`, `refuses`, `coincidence`, joined where relevant with
`+ supply`); and each row's table cell links to the `## Round 4` subsection that
carries its evidence.

| row | verdict | route | evidence re-taken here |
|---|---|---|---|
| `boolean-schema-true` | coincidence / discards | 1 + 2 | `etsi…apppkgmgmt` (row 46) declares `additionalProperties: true`, `anchore.io` (row 3) declares no such key, and both goldens emit `typing.Dict[str, typing.Any]`. `rocketmq-sre-phase02` **re-generated**: 253 schemas, 286 modules, exactly 4 `typing.Any` aliases |
| `components-links` | discards + supply | 2 | link probe **re-run**: `GetThingById` emits 0 bytes |
| `const-boolean` | discards | 2 | census re-run: 0 boolean `const`s in 124 documents |
| `const-integer` | discards | 2 | census re-run: 0 integer `const`s in 124 documents |
| `cycle-via-additionalProperties` | implements | 2 | registered row 92; `eozilla_matches_fern_output` passes |
| `encoding-explode-or-allowReserved` | refuses / ignores | 2 | probe 3 **re-run**: `fern check` exit 1, `fern generate` exit 0, error text verbatim |
| `encoding-object` | implements / discards | 1 | `free5gc-pdu-session` (row 73) declares 99 `contentType`, 58 `headers`; golden emits the first, none of the second |
| `link-description` | discards | 2 | link probe **re-run**: both descriptions emit 0 bytes |
| `link-requestBody` | discards + supply | 2 | link probe **re-run**: `get_thing` takes only `thing_id` |
| `link-server` | discards + supply | 2 | link probe **re-run**: neither host reaches `environment.py` |
| `nesting-depth-ge-15` | implements | 1 | `openbanking…account-info` (row 58) reaches depth 19, 91 nodes ≥ 15; the 230-character module is present |
| `normalization-collision` | discards | 1 | row 58 declares 4 `OB_?Rate1_[01]` schemas, golden emits 2; row 51 collapses `RoleArn`/`RoleARN` |
| `server-description-multiword` | discards | 1 | `traccar.org` (row 60) declares 6 multi-word descriptions, 0 below root; golden emits one `DEFAULT` |
| `servers-multiple-path-or-operation` | discards | 1 | `apideck.com-file-storage` (row 14) declares 5 operation servers on `upload.apideck.com`; golden routes all through the root |
| `servers-three-levels` | discards | 2 | probe quoted in full, both exits 0, sole host occurrence quoted |
| `type-array-multi-nonnull` | implements | 2 | registered row 93; `openepcis_dpp_ready_matches_fern_output` passes |
| `xml-request` | discards | 2 | probe quoted in full, both exits 0; corpus declares `application/xml` 0 times |
| `xml-response` | discards | 2 | as `xml-request`; golden corroboration is `text/xml`, and is named as corroboration |

**Every golden-derived verdict rests on a specification that does declare the
shape, and every declared count re-measures.** This was the failure mode most
worth hunting — a `discards` read off a golden whose own source never declared the
shape under test, which would make Fern's silence meaningless. It does not occur.
Each of the three measurement families ran a structural census *first* and moved
to a probe wherever the corpus was silent, which is the guard that prevents it:
the link census finds 40 Link objects declaring none of the four fields under
test, the encoding census finds `explode`/`allowReserved` declared zero times, and
the schema census finds no boolean or integer `const` and no multi-non-null `type`
array. All three censuses re-run **byte-identically** here at 124 documents. The
one row that could have gone wrong the cheap way — `xml-request`/`xml-response`,
where `amazonaws.com-cloudfront` is dense with XML — explicitly declines to use it,
records that its 256 hits are `text/xml` and not `application/xml`, and rests on a
probe instead.

**Every probe-derived verdict names its probe, both exit codes, and an emitted
call site or a recorded absence.** Three were re-run end to end on this host,
against the same pins (`fern check` then `fern generate --group python-sdk --local
--preview`, CLI `5.67.1`, generator `fernapi/fern-python-sdk:5.20.0`,
`CI=true`/`GITHUB_ACTIONS=true`):

- **The link-fields probe**, chosen because four of the eighteen rest on it alone
  and an all-zeros absence table is exactly what an unrun measurement would look
  like. `fern check` **exit 0**, `fern generate` **exit 0**. All nine markers
  return 0, `grep -ril link` over the generated tree returns 0, and
  `environment.py` and `create_thing` come back byte-identical to the blocks
  quoted above. The four rows stand.
- **The multipart-object `explode` probe**, chosen because it carries the only
  `refuses` verdict in the eighteen. `fern check` **exit 1** and `fern generate`
  **exit 0**, and the diagnostic reproduces verbatim — `meta is exploded and must
  be a list. Did you mean list<optional<Thing>>?` at `__package__.yml -> service ->
  endpoints -> mpObjectExplode` — with `mp_object_explode`'s emitted body identical
  to its control.
- **`rocketmq-sre-phase02`**, the real candidate behind `boolean-schema-true`,
  chosen because this row's draft once claimed models were missing that its own run
  showed present. The corrected row is right in every particular: `fern check` exit
  0 (`Found 0 errors and 2 warnings`), `fern generate` exit 0, 253 component
  schemas, 286 emitted modules, and exactly four `typing.Any` aliases —
  `ActionItem`, `PostmortemRevision`, `IncidentOperationResultTimelineEvent`,
  `WhatIfSimulation` — matching name for name the four schemas that declare a
  property whose schema is literally `true`. `WhatIfSimulation` declares 16
  properties and emits none of them; its six `WhatIfSimulation__*` components
  survive; and the `oneOf`-branch exception reproduces exactly, `value: typing.Any`
  beside `storage: typing.Literal["inline"]`.

**Both registrations hold.** `tests/e2e.rs` declares 108 corpora and 108
`unmatched: &[]`, with no non-empty exclusion list anywhere in the file, and
`just test-corpus-match`'s `eozilla_matches_fern_output` and
`openepcis_dpp_ready_matches_fern_output` lines both pass. That recipe sets
`CROZIER_REQUIRE_CORPUS`, so an unfetched spec would have failed the run rather
than skipping it quietly. The two `expected/` trees hold 106 and 91 files, which
is the 105 and 90 compared plus the `.crozier-fern-golden.json` the comparison
walk skips.

**Three corrections, all of them staleness this round created in its own record.**
Each was a present-tense claim that was true when measured and is false in the
finished tree, because a later node in the same round registered the fixture that
falsified it:

- `cycle-via-additionalProperties` read *"not one golden file in the corpus emits a
  forward-referenced map"* over a 105-tree checkout. Re-taken over the 107 trees
  that stand now, `grep -rl 'typing\.Dict\[str, "' tests/fixtures/*/expected/`
  returns **2**, both under `tests/fixtures/eozilla/`. Scoped to the checkout it
  described, and the closure recorded.
- The `type-array-multi-nonnull` table cell read *"of the corpus's 498 `type`
  arrays every one has a single non-null member."* Re-running that census at 124
  documents returns **2 occurrences in 1 document**, `openepcis-dpp-ready` — which
  is the row's own registered primary, and matches the 2 its candidate table
  declares. Scoped, and the registration named. (`tests/e2e.rs` already worded this
  correctly as *"before this row"*.)
- The servers-and-XML family's forward-looking note said the six links-and-encoding
  rows *"are still `unmeasured` until one is."* They were measured, in this same
  round; a pointer now says so.

Counts that moved without changing a finding are left as the transcripts they are:
the environment census (71 of 105 → **73 of 107**, still exactly one member each,
still only `DEFAULT` and `PRODUCTION`), the `base_url` tally (four forms, none
naming a sub-root host, counts risen), the `force_multipart.py`/`http_client.py`
hashes (104 → **106** trees, still one hash each), the description word-count split
(18/4 → **20/4**, still no exception either way), and `additionalProperties: true`
(217/30 → **219/32**, still the only boolean subschema any document declares).
Every one of these strengthens the claim it supports rather than weakening it.

## What Round 3 did not register, and why

The round's main result. Round 3 registers a fixture only where **both** bars are
met:

1. **Semantic** — a screen must have measured Fern *implementing* the shape and
   emitting something that reflects it, and all three candidates must witness that
   same behaviour. A successful, non-empty generation is not that: it says the
   document generates, not that the feature reaches the output.
2. **Eligibility** — a verified primary and at least two verified backups, each
   with a pinned credential-free URL and a licence tier the census measured.

Four gaps clear both bars. **Fifty-five do not** — the fifty-five rows tabulated
below, of which round 4 later measured two into **`REGISTRABLE`** and registered
both, for a standing tally of six of fifty-nine. That ratio is the finding, and
it is the opposite of what issue #148 assumed: for most of this surface Fern either
discards the shape, ignores it, refuses it, or produces output that matches only by
coincidence with an unconditional default — and where it does none of those, no
screen measured what it emits.

`eligible` and `verified` below are the screens' own counts: how many candidates
the screen carried end to end (`verified`), and how many of those also clear the
census licence bar (`eligible`). A row whose verdict is **unmeasured** is an **open
question a future probe could answer**, not a proven absence.

| gap | eligible | verified | verdict | why no fixture was proposed |
|---|---:|---:|---|---|
| `apiKey-cookie` | 4 | 6 | discards | the importer drops the scheme outright; the client is generated from whatever other scheme the document declares |
| `apiKey-query` | 2 | 6 | discards + supply | as `apiKey-cookie`; and only 2 eligible of 6 verified — 4× licence tier Q — short of a primary plus two backups |
| `boolean-schema-true` | 4 | 4 | coincidence (`additionalProperties`, `items`) / discards (property position) | the corpus declares one form of it, 217 times across 30 documents, and Fern's output for that form is the no-keyword default: `additionalProperties: true` emits the `typing.Dict[str, typing.Any]` a bare `type: object` emits, and `items: true` emits the `typing.List[typing.Any]` a bare `type: array` emits. A property whose schema is literally `true` is different — the module is still written but holds no model, and every property of the enclosing object goes with the class. Measured on this row's own candidate `rocketmq-sre-phase02`: of 253 component schemas exactly four declare the form directly, and exactly those four emit `X = typing.Any`, `WhatIfSimulation` shedding all sixteen of its properties and degrading `run_what_if_simulation` to `HttpResponse[typing.Any]`, at exit 0 with no diagnostic. Its four verified candidates are three files from the single repository `mxsm/rocketmq-rust` plus `secunet-AG/hwaas`, so the pool holds two independent witnesses, not four. Measured in [Round 4](#round-4--schema-shapes) |
| `components-links` | 2 | 4 | discards + supply | probed directly: a response Link that is a `$ref` to a `components.links` entry emits nothing — the component's name, description, `requestBody` and `server` all reach zero bytes, and no corpus document declares `components.links` at all. 2 eligible of 4 verified, short of a primary plus two backups. Measured in [Round 4](#round-4--links-and-encoding) |
| `components-pathItems` | 6 | 7 | discards | `components.pathItems` reaches the SDK only through a Path Item `$ref`, which Fern discards; the one candidate that loses nothing witnesses the *declaration* alone |
| `const-boolean` | 13 | 13 | discards | measured on two of its own candidate specifications, both generating at exit 0: `omersiar/ript` emits `has_more: bool` for `{type: boolean, const: false}`, and `MarkiNote` emits `success: typing.Optional[bool] = None` for `{const: true, default: true, type: boolean}` — the `default` is dropped with the `const`, so the client can construct the flag `False`. A probe supplies the control: a `type: string` `const` in the same document becomes the single-member `StrEnum` `tamoss` (row 69) pins, while the boolean one becomes a bare `bool`. No corpus document declares a boolean `const` at all. Measured in [Round 4](#round-4--schema-shapes) |
| `const-integer` | 7 | 8 | discards | as `const-boolean`, on three candidate specifications that all generate at exit 0: `omersiar/ript` emits `count: int`, `total: int` and `page: int` for `const` 0, 0 and 1 — indistinguishable from the `limit: int` beside them, which declares `minimum: 1` instead — and `MarkiNote` and `tltv-org/protocol` each emit a bare `int` for their own integer `const`. No corpus document declares an integer `const` at all. Measured in [Round 4](#round-4--schema-shapes) |
| `cookie-array` | 0 | 3 | discards + supply | cookie parameters are dropped from the client entirely; and 0 eligible of 3 verified — 3× licence untiered |
| `cookie-object` | 1 | 6 | discards + supply | as `cookie-array`; 1 eligible of 6 verified — 5× licence untiered |
| `cookie-parameter` | 7 | 7 | discards | cookie parameters are dropped from the client entirely; the warning does not fail `fern check` |
| `cycle-via-additionalProperties` | 3 | 3 | implements | probed directly: a map of self emits `from __future__ import annotations`, `typing.Optional[typing.Dict[str, "Field"]]` and a trailing `update_forward_refs(Field)` — three bytes that derive from the cycle and nothing else. Confirmed on all three candidate specifications, which generate at exit 0 and each emit the same three artifacts on their own cycle. Recursion through `properties`/`items` is densely pinned already (335 golden files call `update_forward_refs`), but no golden emits a forward-referenced *map*, so this is not registered anywhere. **REGISTRABLE** — candidate set in [Round 4](#round-4--schema-shapes) |
| `deepObject-real-object` | 5 | 5 | **coincidence** | `query_encoder.py` flattens *every* dict-valued query parameter to `key[subkey]=value` unconditionally, and `form`, `pipeDelimited` and `deepObject` objects emit byte-identical code. A golden would pin the default, not style handling |
| `encoding-explode-or-allowReserved` | 3 | 3 | refuses (multipart object `explode`) / ignores (list `explode`, `allowReserved`) | probed directly, and the two fields do not behave alike. `explode: true` on a **non-list multipart part** is refused at check time: `fern check` **exit 1**, `meta is exploded and must be a list`. In the other six configurations — `explode` true and false on a list part, `allowReserved` on either, and `explode: true` on a form-urlencoded map part — the emitted method is byte-identical to a no-encoding control. `fern generate` **exits 0** even on the refused document, emitting that same identical code. Measured in [Round 4](#round-4--links-and-encoding) |
| `encoding-object` | 4 | 6 | implements (`contentType`) / discards (`headers`) | the object's two fields differ. `free5gc-pdu-session` (row 73) declares 99 Encoding objects; its golden emits `default_content_type="application/vnd.3gpp.5gnas"` from one of them — the only shape Round 4 found Fern handles — while the 58 per-part `Content-Id` headers reach zero bytes. No fixture is proposed because the shape is already registered, at `CORPUS.md` rows 73 and 76, both byte-matching. Measured in [Round 4](#round-4--links-and-encoding) |
| `enum-member-float` | 2 | 2 | discards + supply | Fern accepts the schema and silently strips the enum, emitting `Kind = float` with no members; and only 2 eligible, pool exhausted |
| `enum-member-object` | 1 | 1 | discards + supply | as above, emitting `Kind = typing.Dict[str, typing.Any]`; only 1 eligible, pool exhausted |
| `explode-true-simple-header` | 0 | 0 | refuses | `fern check` refuses the header parameter that carries it, exit 1; no candidate carried end to end at all |
| `explode-true-simple-path` | 4 | 4 | ignores | the parameter is emitted but `explode` is ignored entirely on a simple-style path parameter |
| `header-array` | 0 | 0 | refuses | `fern check` refuses an array-typed header parameter, exit 1; no candidate carried end to end at all |
| `header-object` | 0 | 0 | crashes | `fern generate` crashes on an object-typed header parameter with an internal `KeyError`; no candidate carried end to end at all |
| `http-digest` | 0 | 4 | discards + licence | the importer drops the scheme outright; and 0 eligible of 4 verified — 3× the specification declares CC BY-NC-SA 3.0 US, 1× licence tier Q |
| `label-array-or-object` | 0 | 3 | discards + licence | Fern discards the `label` style and renders `str(list)` into the path segment; 0 eligible of 3 verified — 3× licence untiered |
| `link-description` | 5 | 9 | discards | probed directly: a Link `description` reaches no docstring, no `reference.md` entry and no byte of the SDK; the generated tree holds no occurrence of `link` in any case at all. No corpus document declares the field, so this rests on the probe. Measured in [Round 4](#round-4--links-and-encoding) |
| `link-requestBody` | 2 | 3 | discards + supply | probed directly: a Link `requestBody` expression emits nothing — the target operation's generated method takes only its path parameter. No corpus document declares the field. 2 eligible of 3 verified, short of a primary plus two backups. Measured in [Round 4](#round-4--links-and-encoding) |
| `link-server` | 1 | 3 | discards + supply | probed directly: a Link `server` reaches neither the environment enum — which keeps the root URL alone — nor any call site. No corpus document declares the field. 1 eligible of 3 verified, so the pool holds one real-world witness where three are needed. Measured in [Round 4](#round-4--links-and-encoding) |
| `matrix-array` | 0 | 4 | discards + licence | Fern discards the `matrix` style and renders `str(list)` into the path segment; 0 eligible of 4 verified — 4× licence untiered |
| `matrix-object` | 0 | 0 | discards | Fern discards the `matrix` style; no candidate carried end to end at all |
| `mutualTLS` | 2 | 6 | discards + supply | the importer drops the scheme outright; 2 eligible of 6 verified — 2× tier Q, 2× untiered |
| `nesting-depth-ge-15` | 6 | 6 | implements | `openbanking.org.uk-account-info-openapi` (row 58) reaches inline depth 19 with 91 schema nodes at depth ≥ 15, and its golden emits a fully populated model for the deepest of them, named by concatenating all eighteen path segments — no truncation, no `typing.Any`, no depth limit. No fixture is proposed because the shape is already registered, at `CORPUS.md` row 58, byte-matching. Measured in [Round 4](#round-4--schema-shapes) |
| `nonascii-info-title` | 5 | 5 | ignores | probed directly: `info.title: 推奨データセット` is accepted and never reaches an identifier, so nothing emitted derives from it |
| `nonascii-operationId` | 1 | 1 | crashes + supply | the generator emits invalid Python for a genuinely non-ASCII operationId; the one surviving candidate carries a Latin-1 accented one that folds, so it does not carry the shape |
| `normalization-collision` | 4 | 5 | discards | Fern does not resolve the collision, it loses one side of it. `openbanking.org.uk-account-info-openapi` (row 58) declares `OBRate1_0` (`type: number`) and `OB_Rate1_0` (`type: string`); the golden emits one module, `ObRate10 = str`, and silently retypes every reference to the `number` schema. `amazonaws.com-cloudformation` (row 51) is a second witness, collapsing `RoleArn` and `RoleARN` into one `role_arn.py`. Both documents are registered and byte-matching, so crozier already reproduces the loss. Measured in [Round 4](#round-4--schema-shapes) |
| `oauth2-implicit` | 0 | 7 | supply | no eligible candidate carries the screen's verdict that Fern selected the flow; 0 eligible of 7 verified — 4× untiered, 3× tier Q |
| `oauth2-password` | 5 | 6 | supply | only two eligible candidates carry the screen's verdict that Fern *selected* the password flow; the others show Fern selecting a different scheme from the same document |
| `operation-security-alternatives` | 2 | 5 | ignores + supply | Fern collapses declared alternatives to a single credential — the first supported scheme — so the alternatives are not represented; 2 eligible of 5 verified — 2× tier Q, 1× OGC license |
| `options-operation` | 3 | 6 | discards | Fern emits no client method for `options` |
| `param-content-cookie` | 0 | 0 | discards | cookie parameters are dropped from the client entirely; no candidate carried end to end at all |
| `param-content-path` | 0 | 0 | discards | Fern collapses a `content:`-typed parameter to a bare `str`, losing the declared object; no candidate carried end to end at all |
| `pathitem-ref` | 7 | 7 | discards | only the **remote-URL** form resolves; every other form is silently discarded. Exactly one eligible candidate witnesses the resolving behaviour, and the available backups witness the opposite one |
| `pipeDelimited-array` | 7 | 7 | discards | Fern discards the declared style: the array emits as an httpx repeated key, `"probeParam": probe_param`, not pipe-joined |
| `pipeDelimited-object` | 1 | 7 | discards + supply | Fern discards the declared style; object query parameters are flattened regardless of it; 1 eligible of 7 verified — 6× licence untiered |
| `range-1XX` | 1 | 6 | discards + supply | a ranged response yields no error class at all; the operation falls through to `ApiError`; 1 eligible of 6 verified — 5× licence untiered |
| `range-3XX` | 3 | 5 | discards | a ranged response yields no error class at all |
| `range-4XX` | 5 | 6 | discards | a ranged response yields no error class at all |
| `range-5XX` | 4 | 4 | discards | a ranged response yields no error class at all |
| `relative-file-ref` | 2 | 2 | discards + pipeline | Fern discards a relative-file Path Item `$ref` when the document is fetched alone, and crozier's fixture pipeline cannot register the tree that would make it resolve; only 2 eligible |
| `server-description-multiword` | 15 | 16 | discards | a multi-word server description reaches no identifier: all 18 goldens whose first root server carries one emit `DEFAULT`, while the four whose description is the single word `Production` emit `PRODUCTION`. Measured in [Round 4](#round-4--servers-and-xml) |
| `servers-multiple-path-or-operation` | 2 | 5 | discards | a Path Item or Operation `servers` block emits nothing: `apideck.com-file-storage` declares five operation-level servers on a *different* host and its golden routes every one through the single root base URL. Measured in [Round 4](#round-4--servers-and-xml) |
| `servers-three-levels` | 1 | 5 | discards | probed directly: with a root, a Path Item and an Operation server in one document, `fern check` and `fern generate` both exit 0 and only the root URL is emitted. Measured in [Round 4](#round-4--servers-and-xml) |
| `spaceDelimited-object` | 0 | 6 | discards + licence | Fern discards the declared style; object query parameters are flattened regardless of it; 0 eligible of 6 verified — 6× licence untiered |
| `trace-operation` | 2 | 5 | discards + supply | Fern emits no client method for `trace`; 2 eligible of 5 verified — 3× licence tier Q |
| `type-array-multi-nonnull` | 8 | 8 | implements | probed directly: `type: [string, integer]` emits `typing.Union[str, int]`, and the members track the declared list — `[boolean, number]` gives `typing.Union[bool, float]`, `[string, integer, boolean]` gives `typing.Union[str, int, bool]`, so no unconditional default can account for it. Confirmed at the use sites of all three candidate specifications, which generate at exit 0 — `wildfire-robotics`'s five-member `[string, number, integer, boolean, null]` emits `typing.Dict[str, typing.Optional[ReadModelSummaryValue]]` with `ReadModelSummaryValue = typing.Union[str, float, int, bool]`, representing every declared member. Before this round registered one, the `typing.Union[...]` occurrences in the goldens all arose from `oneOf`/`anyOf`, and every one of the corpus's 498 `type` arrays had a single non-null member. **REGISTRABLE** — candidate set in [Round 4](#round-4--schema-shapes); registered as `CORPUS.md` row 93 |
| `x-fern-or-crozier-ignore` | 2 | 4 | supply | two of its four verified candidates are the AssemblyAI specification `CORPUS.md` records REJECTED, leaving two eligible |
| `xml-request` | 18 | 20 | discards | probed directly: a **required** `application/xml` request body is dropped whole — the method takes no body argument and the call site sends none. No committed golden declares `application/xml`, so this rests on the probe. Measured in [Round 4](#round-4--servers-and-xml) |
| `xml-response` | 20 | 24 | discards | probed directly: an `application/xml` response schema is dropped whole — the method returns `HttpResponse[None]` and never parses the body. No committed golden declares `application/xml`, so this rests on the probe. Measured in [Round 4](#round-4--servers-and-xml) |

### The eight HTTP statuses left unpinned

The rule is applied **per status rather than per document**: a status is pinned
only when three eligible witnesses each emit that same exception name for it, so a
row claiming several statuses has to be backed for every one of them separately.
Two rows this round registers name their backups per status, because no single
document witnesses both statuses they claim.

**428 is the one to read twice.** Issue #148 reasoned from RFC 6585 that
`PreconditionError` was likely wrong; the screens measured that it is exactly what
Fern emits; and it still cannot be pinned, because only two eligible witnesses
exist in the whole pool. Both halves are true — the name is correct, and no fixture
holds it.

| status | eligible | verified | class Fern emits | why no fixture was proposed |
|---|---:|---:|---|---|
| 407 | 0 | 0 | `ProxyAuthenticationRequiredError` (probe) | **zero pool documents declare it anywhere** in the eligible pool of 4,864. Probed directly, Fern generates it correctly — a corpus supply limit, not a Fern one |
| 414 | 0 | 1 | `UriTooLongError` | 0 eligible witnesses of 1 verified — short of a primary plus two backups |
| 417 | 2 | 2 | `ExpectationFailedError` | 2 eligible witnesses of 2 verified — short of a primary plus two backups |
| 418 | 1 | 4 | `ImATeapotError` | 1 eligible witness of 4 verified — short of a primary plus two backups |
| 421 | 0 | 0 | `MisdirectedRequestError` (probe) | **zero pool documents declare it anywhere** in the eligible pool of 4,864. Probed directly, Fern generates it correctly — a corpus supply limit, not a Fern one |
| 425 | 1 | 1 | `TooEarlyError` | 1 eligible witness of 1 verified — short of a primary plus two backups |
| 428 | 2 | 2 | `PreconditionError` | 2 eligible witnesses of 2 verified — short of a primary plus two backups |
| 431 | 1 | 1 | `RequestHeaderFieldsTooLargeError` | 1 eligible witness of 1 verified — short of a primary plus two backups |

In every row above the class name itself is **not** in doubt — it was measured
against Fern's output and matches crozier's table. What is missing is a
redistributable witness set to pin it.


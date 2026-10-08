# Vendored assets

## `core/` — Fern's SDK runtime (Apache-2.0)

`core/` is [Fern](https://github.com/fern-api/fern)'s Python SDK **runtime
support library** (HTTP client, pydantic utilities, serialization, SSE, request
options), vendored here and emitted verbatim into every SDK crozier generates —
exactly as Fern ships it into its own output. It is **generator boilerplate, not
derived from any OpenAPI document**: none of these files reference a generated
type; they are identical across every SDK Fern produces from a given generator
version.

- **License / attribution:** Apache-2.0. See [`../NOTICE`](../NOTICE) and
  [`../licenses/fern-APACHE-2.0.txt`](../licenses/fern-APACHE-2.0.txt); both must
  be retained, and they cover this vendored runtime as redistributed product
  (not only the test fixtures).
- **Source:** produced by `fernapi/fern-python-sdk:5.20.0` over the managed Corpus
  fixtures via `tools/fern-goldens/generate-fern-fixture.sh`.
- **Change made (Apache-2.0 §4(c)):** Python comments are stripped with the same
  string-safe normalizer used for fixtures, except Fern's `# type: ignore`
  pragmas, which stay at the lines Fern's own output carries them so a generated
  SDK type-checks clean under its pinned `mypy`. The auth-shaped
  `client_wrapper.py` is assembled by Crozier and is not one of the verbatim
  runtime assets.
- **Judged lint:** the verbatim runtime files here, and the three Python
  scaffolding copies below, are excluded from `llmlint` in `llmlint.yml` as
  vendored Fern output, as `tests/fixtures/**` is; the byte-match and the
  generated-SDK `mypy` test gate them instead.

## `scaffolding/` — Fern's project-root files (Apache-2.0)

`scaffolding/` is the project output Fern writes alongside the SDK: packaging and
metadata, README/contribution guidance, the default async-client helper, and its
generated tests. Like `core/`, these are emitted into every generated SDK.

- **License / attribution:** Apache-2.0; the same `../NOTICE` and
  `../licenses/fern-APACHE-2.0.txt` cover them.
- **Source:** Fern's Python generator over the same managed Corpus fixture and
  version as `core/`.
- **Change made (Apache-2.0 §4(c)):** in `pyproject.toml`, the project name,
  package name, and version are replaced with the `@@CROZIER_SDK_NAME@@`,
  `@@CROZIER_PACKAGE@@`, and `@@CROZIER_SDK_VERSION@@` placeholders. The default
  client and generated test templates use the name placeholders for valid custom
  package imports; `conftest.py`, `default_clients.py.tmpl` and
  `test_aiohttp_autodetect.py.tmpl` are otherwise Fern's verbatim, `# type:
  ignore` pragmas included. Non-Python files are not comment-stripped.

### `scaffolding/README.md.tmpl` — Fern's generated README (Apache-2.0)

`README.md.tmpl` is the `README.md` Fern writes into a generated SDK: static
prose (installation, usage, exception handling, the advanced/retries/timeouts
sections, contributing), identical across SDKs apart from the substituted names,
the worked examples, and the two conditional sections below.

- **License / attribution:** Apache-2.0; the same `../NOTICE` and
  `../licenses/fern-APACHE-2.0.txt` cover it.
- **Source:** Fern's Python generator, at the same version as `core/`. Its per-SDK
  text is parameterized as described below.
- **Change made (Apache-2.0 §4(c)):** `@@...@@` placeholders replace the per-SDK
  text, which the emitter fills in: the organization, package, and client
  names (`@@ORG@@`, `@@PKG@@`, `@@CLIENT@@`); the worked sync and async usage
  examples (`@@USAGE@@`, `@@ASYNC_EXAMPLE@@`, synthesized by crozier's own
  example-value generator); the call lines inside the exception-handling,
  raw-response, and retry/timeout examples (`@@ERR_CALL@@`, `@@RAW_CALL@@`,
  `@@RETRY_CALL@@`); and the Environments and Streaming sections with their
  table-of-contents entries (`@@ENVIRONMENTS@@`, `@@ENVIRONMENTS_TOC@@`,
  `@@STREAMING@@`, `@@STREAMING_TOC@@`), which the emitter drops entirely for an
  SDK with no environment or no streaming endpoint. The prose is otherwise
  Fern's output verbatim. `reference.md` is not vendored — it is spec-derived and
  assembled entirely by the emitter.

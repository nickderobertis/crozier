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
- **Source:** produced by Fern's published Python generator over the exhaustive
  OpenAPI document (see `scripts/generate-fern-fixture.sh`), matching the version
  recorded in `NOTICE`.
- **Change made (Apache-2.0 §4(c)):** in `client_wrapper.py`, the two SDK-header
  values are replaced with the placeholders `@@CROZIER_SDK_NAME@@` and
  `@@CROZIER_SDK_VERSION@@`, which the emitter substitutes per SDK. The files are
  otherwise Fern's output verbatim (comment-stripped, as with all fixtures).

## `scaffolding/` — Fern's project-root files (Apache-2.0)

`scaffolding/` is the project-root output Fern writes alongside the SDK:
`pyproject.toml`, `requirements.txt`, and the `.fern/metadata.json` marker
(renamed `metadata.json` here, emitted to `.fern/metadata.json`). Like `core/`,
these are emitted into every generated SDK.

- **License / attribution:** Apache-2.0; the same `../NOTICE` and
  `../licenses/fern-APACHE-2.0.txt` cover them.
- **Source:** Fern's Python generator over the exhaustive OpenAPI document, same
  version as `core/`.
- **Change made (Apache-2.0 §4(c)):** in `pyproject.toml`, the project name,
  package name, and version are replaced with the `@@CROZIER_SDK_NAME@@`,
  `@@CROZIER_PACKAGE@@`, and `@@CROZIER_SDK_VERSION@@` placeholders. These files
  are **not** comment-stripped (they are not Python), so they carry Fern's inline
  TOML comments verbatim.

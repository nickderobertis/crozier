# missing-info-object: refuse

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, in both modes. A document whose `info` is absent or
written as null is not valid OpenAPI (the Info Object is required), and the
certified pair does not generate from it: it reads `info.version` before
anything else, logs `Failed to parse openapi document` with
`TypeError: Cannot read properties of null (reading 'version')` (`undefined`
where `info` is absent), and exits 0 over the 35-file empty scaffold — a false
success, so a refusal under the refusal rule ([probe record](fern-refusal.txt);
logs under
[`../../openapi-surface/fern-refusals/probe-logs/`](../../openapi-surface/fern-refusals/probe-logs/)).
The empty scaffold is a client exposing no operations and no model types, so
design-review ruling `empty-sdk-refused` keeps crozier refusing it too, rather
than writing the SDK crozier used to write from the document's components.

crozier refuses at the document boundary, before any other check, with
`missing-info-object: info` in default mode and `missing-info-object: info
(fern-strict refusal)` under `--fern-strict`, writing nothing. An `info`
object, however sparse (`info: {}`), is no refusal.

The class was measured from scratch for the document-acceptance handed-off
area:
[`null-info-paths-components`](../../fern-measurements/handed-off/document-acceptance/null-info-paths-components/README.md)
(`info:` written empty beside `paths:` and `components.schemas`) and
[`crozier-refuses-unreferenced-path-parameter`](../../fern-measurements/handed-off/document-acceptance/crozier-refuses-unreferenced-path-parameter/README.md),
whose real document (swagger-core's ticket-3303 petstore) omits `info` and is
refused by the certified pair for that reason before its unreferenced path
parameter is read. No document of the registry's population carries the
class, so `documents` and `population_strict` are `0` and `0/0`.

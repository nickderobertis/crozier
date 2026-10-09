# Workspace pre-steps, measured

Measured on 2026-10-07 with Fern CLI **5.67.1** and
**fernapi/fern-python-sdk 5.20.0**, using the freshly authored documents beside
this note. These are workspace measurements, not corpus sources or coverage
fixtures. No Fern output was edited.

Each run used organization `fern`, `pydantic_config.enum_type: python_enums`,
`CI=true`, `GITHUB_ACTIONS=true` and the preview-only dummy token used by
`tools/fern-goldens/generate-fern-fixture.sh`. `GIT_CEILING_DIRECTORIES` was set to the
measurement directory so Git discovery stopped there; the generated metadata
contains no source revision.
The command was:

```sh
fern generate --group python-sdk --local --preview --output ../preview --force
```

Its `fern.config.json` was:

```json
{"organization":"fern","version":"5.67.1"}
```

Its `generators.yml` was:

```yaml
api:
  specs:
    - openapi: ../../swagger.json
groups:
  python-sdk:
    generators:
      - name: fernapi/fern-python-sdk
        version: 5.20.0
        config:
          pydantic_config:
            enum_type: python_enums
        output:
          location: local-file-system
          path: ../generated/python
```

The relative path assumes the workspace is `<measurement>/case/fern/` and
these documents are in `<measurement>/`. Copy the documents to a fresh
directory before running. Each generation exited zero. The cases below state
the changes to this configuration and the output observed.

## Swagger

[`swagger.json`](swagger.json) has `host: conversion.example.com`,
`basePath: /v2` and no `schemes`. Fern generated this line in
`src/fern/environment.py`:

```python
    DEFAULT = "https://conversion.example.com/v2"
```

Running `swagger2openapi` 7.0.8 with default options on that input instead
produced `servers: [{"url":"//conversion.example.com/v2"}]`. The guide now
adds `schemes: ["https"]` only when the field is absent, before conversion.
Its output is [`swagger-corrected.json`](swagger-corrected.json), with
`servers: [{"url":"https://conversion.example.com/v2"}]`.

A second Fern run, with `openapi: ../../swagger-corrected.json`, generated the
same environment line. Every file in its complete preview tree was byte-equal
to the original Swagger run's corresponding file, without normalization.

## Overlays

[`overlay-input.json`](overlay-input.json) declares a required JSON body with
`type: object`, `additionalProperties: false`, `properties: {}` and a media
`example: {}`. [`overlay.json`](overlay.json) adds the operation's summary.
The Fern workspace used:

```yaml
api:
  specs:
    - openapi: ../../overlay-input.json
      overlays: ../../overlay.json
```

Fern's `src/fern/client.py` and `src/fern/raw_client.py` respectively contain:

```python
    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
```

```python
    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
```

The raw method sends `json={}`. Both async methods have the same zero-field
argument list.

The old `openapi-format` 1.33.5 CLI recipe, even with `--no-sort`, removes both
empty fields. Calling that release's `openapiOverlay` API and then `writeFile`
preserves them: [`overlay-corrected.json`](overlay-corrected.json) is the
corrected recipe's output. A second Fern run read that document with no
workspace overlay. Its complete preview tree was byte-equal to the original
overlay run's tree, without normalization.

## Pruning

[`pruning.json`](pruning.json) has three component schemas: `Reply`, reached
from `200`; `RangeProblem`, reached only from `4XX`; and `Unused`, reached
nowhere. The Fern workspace used:

```yaml
api:
  specs:
    - openapi: ../../pruning.json
      settings:
        only-include-referenced-schemas: true
```

Fern's generated `src/fern/types/` contains exactly `__init__.py` and
`reply.py`. The method returns `Reply`; neither `RangeProblem` nor `Unused`
is generated. Thus range-status responses do not keep schemas alive in this
workspace setting.

For comparison, the following invocation of `openapi-format` 1.33.5 keeps
`Reply` **and** `RangeProblem` and removes only `Unused`. Its output is
[`pruning-openapi-format.json`](pruning-openapi-format.json).

```js
const format = require("openapi-format");
const input = await format.parseFile("pruning.json");
if (input instanceof Error) throw input;
const result = await format.openapiFilter(input, {
  filterSet: { unusedComponents: ["schemas"] }
});
await format.writeFile("pruning-openapi-format.json", result.data);
```

The migration guide therefore records this difference and supplies no pruning
recipe. It does not recommend the above filter as an equivalent to Fern.

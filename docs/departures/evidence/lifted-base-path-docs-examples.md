# `lifted-base-path-docs-examples`

**Kind:** `fern-defect`. Fern's `README.md` and `reference.md` treat a base-path
parameter it lifted to the client as a method argument: each method snippet
passes it, `reference.md` documents it under each method, and the constructor
snippets leave it out.

## The input

Three crozier-authored documents, each with one tag's `POST /{edition}/layers`
(a JSON `$ref` body) and `GET /{edition}/layers/{layer_id}`, under a
document-level `x-fern-base-path` object whose `path` is `/{edition}`:

- [`base-path-lifted-default/openapi.yml`](../../fern-measurements/parameter-lowering/base-path-lifted-default/openapi.yml)
  sets `paths-include-base-path: true` and gives `edition` a `default: v2`
  under the extension's `parameters`;
- [`base-path-lifted-required/openapi.yml`](../../fern-measurements/parameter-lowering/base-path-lifted-required/openapi.yml)
  gives it none;
- [`base-path-lifted-unincluded/openapi.yml`](../../fern-measurements/parameter-lowering/base-path-lifted-unincluded/openapi.yml)
  keeps the default but leaves `paths-include-base-path` out, its routes not
  repeating the prefix.

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0 (the certified pair), in
the workspace `scripts/generate-fern-fixture.sh` scaffolds (`organization:
fern`, `pydantic_config.enum_type: python_enums`, `fern generate --group
python-sdk --local --preview`), exits 0 on each. The trees, comment-stripped,
are committed as each document's `fern-expected/`.

Its client lifts `edition` out of both methods into a keyword-only constructor
argument the routes read from the client wrapper
(`encode_path_param(self._client_wrapper._edition)`): `edition:
typing.Optional[str] = "v2"` with the default, `edition: str` without. Yet:

| file | lines | what Fern writes |
|---|---|---|
| `README.md` | 43, 75 | `client.layers.create_layer(edition="v2", …)` (`edition="edition"` without the default) |
| `reference.md` | 24, 91 | the same in each method's usage snippet |
| `reference.md` | 39–46, 106–113 | an `**edition:** \`str\`` parameter block under each method |
| `README.md` | 40, 64 | `client = FernApi()` / `AsyncFernApi()`, with the argument left out even where it is required |
| `reference.md` | 19–21, 86–88 | `client = FernApi(environment=…)`, likewise |

## Why it is a defect

With each tree's `src/` on `PYTHONPATH` beside `httpx` and `pydantic` (a copy,
so no bytecode is written into the committed tree):

```text
$ python -c 'from fern import FernApi; FernApi(edition="v2").layers.create_layer(edition="v2", title="title")'
TypeError: LayersClient.create_layer() got an unexpected keyword argument 'edition'
$ python -c 'import inspect; from fern import FernApi; print(list(inspect.signature(FernApi(edition="v2").layers.get_layer).parameters))'
['layer_id', 'request_options']
$ python -c 'from fern import FernApi; FernApi()'          # base-path-lifted-required
TypeError: FernApi.__init__() missing 1 required keyword-only argument: 'edition'
```

Every method snippet calls a method with an argument it does not take,
`reference.md` documents that argument under methods that do not have it, and
without a default the constructor snippet misses a required argument. Docs and
examples that contradict the generated code are a defect under the defect rule.

## crozier's output

`crozier generate` over the same documents writes the same trees but for those
lines: its method snippets and parameter lists leave `edition` out, and every
`README.md` and `reference.md` constructor snippet passes it first, by keyword —
`edition="v2"` with the default, `edition="YOUR_EDITION"` (the placeholder
Fern's own docstrings use) without — ahead of the environment. `crozier compare`
over each pair matches and reports this departure once per file, at the first
line of the differing window: `README.md:40` and `reference.md:20` in each. Those are
the trees' `lifted-base-path-docs-examples` rows in
`tests/fixtures/departures-ledger.tsv`, and
`compare_reports_the_lifted_base_path_departures_and_fails_on_any_other_difference`
in `crates/crozier-e2e/tests/e2e/compare.rs` drives exactly that, and shows the comparison failing
when one more line of either file differs.

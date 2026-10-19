# Examples and docs shapes, measured outside the hand-written fixtures

Each directory here is a complete tree Fern generated at Fern CLI 5.67.1 with
`fernapi/fern-python-sdk` 5.20.0, comment-stripped by `crozier internal-strip`
and never edited. The workspace is the one
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds (packaged preview
layout, organization and package `fern`, project `default_package_name`),
built outside any checkout. `examples_docs_measurements_match_fern` in
[`crates/crozier-e2e/tests/e2e/examples_docs.rs`](../../../crates/crozier-e2e/tests/e2e/examples_docs.rs)
generates each case's document with crozier under the same setting and holds
the whole tree to `fern-expected/` under the corpus gate's normalization,
every departure held to [the ledger](../../../tests/fixtures/departures-ledger.tsv).

This is no corpus fixture and no coverage probe: it is never a `CORPUS.md` row
and settles no coverage row. Each shape these cases measure has a registered
real witness; the document here isolates the shape, or reaches the kinds of it
that witness does not. `examples_docs_cases_fail_on_an_adjacent_unexplained_byte`
plants one byte beside what each `marina-*` case pins and holds that the
comparison then fails.

## The cases

| case | document | setting | what it pins |
|---|---|---|---|
| `archive-glob-rules` | [`archive-glob-rules`](archive-glob-rules/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | every `*/` in an operation, operation and path-level parameter, component parameter, response, component response, schema, property and enum description written `* /` in the docstrings, raw clients, models and `reference.md`, and the inline (`journal/*/segment`) and component (`restore/*/staging`) binary request body descriptions so written in `reference.md`, while the `logs/*/old` operation summary, the `hosts/*/volumes` document description and the `spool/*/queue` component request body description reach no output |
| `archive-glob-rules-literals` | [`archive-glob-rules`](archive-glob-rules/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the same splits with the `Cadence` enum an open `Literal` alias, whose description Fern drops |
| `marina-component-examples` | [`marina-component-examples`](marina-component-examples/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | a request-body component's own `example` as the worked example: an object body whose `oneOf` property is discriminated by single-value `material` enums (`HullRequestHull_Steel(length_m=24, beam_m=6, draft_cm=180)`), top-level array bodies of objects and of strings, and a urlencoded form body with an enum value, its enum imported |
| `marina-component-examples-literals` | [`marina-component-examples`](marina-component-examples/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the same examples with the form's enum value its plain string |
| `marina-crew-roles` | [`marina-crew-roles`](marina-crew-roles/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | a component example whose map (`additionalProperties`) of objects constructs each value: the docstring ends every entry with a comma, the Markdown writers all but the last |
| `marina-dock-log` | [`marina-dock-log`](marina-dock-log/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | the `text-response-optional-query-examples` departure: a `text/plain`-only operation whose optional query parameters declare examples |
| `marina-dock-refs` | [`marina-dock-refs`](marina-dock-refs/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | the `anyof-path-param-schema-example` departure: a path parameter whose inline `anyOf` declares a schema-level example |
| `marina-emoji-tag` | [`marina-emoji-tag`](marina-emoji-tag/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | the `emoji-tag-reference-identifiers` departure: a declared tag `🚧 Legacy endpoints` whose module is `legacy_endpoints` |
| `marina-empty-list-example` | [`marina-empty-list-example`](marina-empty-list-example/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | a first named request example whose array properties are empty: one filled from the property's schema example, one synthesized from its name |
| `marina-firmware-upload` | [`marina-firmware-upload`](marina-firmware-upload/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | a JSON `$ref` body offered beside a binary media type: `reference.md` documents the flattened body arguments, renamed where a query parameter shares a name, in signature order |
| `marina-nullable-note` | [`marina-nullable-note`](marina-nullable-note/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | an inline body property that is a nullable `anyOf` whose string member carries the description, documented in both docstrings and `reference.md` |
| `marina-radio-parts` | [`marina-radio-parts`](marina-radio-parts/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | example items of an inline `oneOf` of titled objects with single-value `kind` enums constructed as the union's variants, imported in the docstring's sorted order and the Markdown writers' example order |
| `marina-skipper-refs` | [`marina-skipper-refs`](marina-skipper-refs/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | the `collapsed-anyof-property-description` departure: a required property that is an `anyOf` of two strings, described on the property, on a flattened body and on a model |
| `marina-tide-channels` | [`marina-tide-channels`](marina-tide-channels/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | a required query array left out of the worked call beside a required parameter exampled as the unknown placeholder, and, where it declares an array example, the `optional-lowered-required-query-array-example` departure |

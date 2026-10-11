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
and settles no coverage row. The shape these cases measure has a registered
real witness; the document here reaches the description kinds that witness
does not.

## The cases

| case | document | setting | what it pins |
|---|---|---|---|
| `archive-glob-rules` | [`archive-glob-rules`](archive-glob-rules/openapi.yml) | the defaults (`pydantic_config.enum_type: python_enums`; crozier's `python-enums`) | every `*/` in an operation, operation and path-level parameter, component parameter, response, component response, schema, property and enum description written `* /` in the docstrings, raw clients, models and `reference.md`, and the inline (`journal/*/segment`) and component (`restore/*/staging`) binary request body descriptions so written in `reference.md`, while the `logs/*/old` operation summary, the `hosts/*/volumes` document description and the `spool/*/queue` component request body description reach no output |
| `archive-glob-rules-literals` | [`archive-glob-rules`](archive-glob-rules/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the same splits with the `Cadence` enum an open `Literal` alias, whose description Fern drops |

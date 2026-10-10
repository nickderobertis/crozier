# `union-value-wrapper-docs-example`

**Kind:** `fern-defect`. Fern's Markdown usage examples call a
discriminated-union wrapper that holds its payload whole with an empty keyword
argument, which Python cannot compile.

## The input

The hand-written fixture
[`kitchen-nested-mapping-target`](../../openapi-surface/handwritten/kitchen-nested-mapping-target/openapi.yml),
a crozier-authored document whose `fireTicket` body is the component `Course`:
a `oneOf` with `discriminator.mapping` `grill → GrillCourse`, `pastry →
PastryCourse`, where `GrillCourse` is itself a `oneOf` of the `$ref`s
`SteakOrder` and `SkewerOrder`, both tagging `station: grill`.

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0 (the certified pair)
generates the fixture's committed
[`fern-expected/`](../../openapi-surface/handwritten/kitchen-nested-mapping-target/fern-expected/).
Its `Course_Grill` wrapper is `value: GrillCourse` beside
`station: typing.Literal["grill"]`, and the method docstrings in
`src/fern/client.py` call it `Course_Grill(value=SteakOrder(...))`. The
Markdown writers instead write:

- `README.md` line 37 `from fern import FernApi, Course_Grill`, and lines 45
  and 67 (the sync and async snippets) `grill=,` as the wrapper's only
  argument;
- `reference.md` line 15 the same import line and line 23 `grill=,`.

## Why it is a defect

The snippets do not compile.
[`union-value-wrapper-docs-example.py`](union-value-wrapper-docs-example.py),
which `just test-sdk-env` runs over the committed Fern tree and crozier's tree
for the same document (the journey named at the end of this note), prints:

```text
fern README.md block 1: SyntaxError: expected argument value expression (line 9: 'grill=,')
fern README.md block 2: SyntaxError: expected argument value expression (line 13: 'grill=,')
fern reference.md block 1: SyntaxError: expected argument value expression (line 9: 'grill=,')
crozier README.md block 1: compiles; request=Course_Grill(value=SteakOrder(station=<SteakOrderStation.GRILL: 'grill'>, doneness='doneness'), station='grill') binds fire_ticket
crozier README.md block 2: compiles; request=Course_Grill(value=SteakOrder(station=<SteakOrderStation.GRILL: 'grill'>, doneness='doneness'), station='grill') binds fire_ticket
crozier reference.md block 1: compiles; request=Course_Grill(value=SteakOrder(station=<SteakOrderStation.GRILL: 'grill'>, doneness='doneness'), station='grill') binds fire_ticket
```

An example call with an empty argument value is a defect under the defect rule.

## crozier's output

`crozier generate python --spec openapi.yml --package-name fern --project-name
default_package_name` writes the same tree but for those lines: each Markdown
snippet passes the payload the docstrings pass, `value=SteakOrder(` …`)`, and
its import line also names `SteakOrder` and `SteakOrderStation` (only
`SteakOrder` under `enum-type: literals`). The rule rewrites crozier's
`value=` block back to `<discriminant value>=,` and drops the names only the
payload used from the import line; the result must equal Fern's file exactly.
Each file's departure is one window, from its import line to its last
wrapper call, so the fixture's `union-value-wrapper-docs-example` rows in
`tests/fixtures/departures-ledger.tsv` are `README.md` line 37 and
`reference.md` line 15, where those windows open. The
`compare_reports_the_union_value_wrapper_departure_and_rejects_an_adjacent_line`
journey in `crates/crozier-e2e/tests/e2e/compare.rs` drives `crozier compare`
over the fixture and shows an adjacent unexplained mismatch in the same snippet
still failing; `sdk_env_union_value_wrapper_docs_examples_compile_only_in_crozier`
in `crates/crozier-e2e/tests/e2e.rs` runs the script above in the SDK tier.

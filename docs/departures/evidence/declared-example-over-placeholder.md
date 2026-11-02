# `declared-example-over-placeholder`

**Kind:** `usefulness`, granted by design-review ruling 2
(`falsy-property-example`, decided 2026-11-01): crozier keeps the example the
API's author declared where the certified pair discards it for a placeholder of
its own. This node applies the same ruling's principle to two further handed-off
causes, `example-enum-member` and the kept sub-rules of `example-value-source`
(`ruling-applied:falsy-property-example` in
[`example-values.tsv`](../../fern-measurements/handed-off/example-values.tsv)).

## The input

Three crozier-authored documents, each with the certified pair's fresh tree
(Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, generated through
`tools/fern-goldens/fern-references.py generate measurements`) beside it:

- [`falsy-property-example/openapi.yml`](../../fern-measurements/handed-off/example-values/falsy-property-example/openapi.yml):
  `POST /buoys` takes a required header `X-Survey-Ref` declaring `example: ""`
  and a multipart body whose parts declare `label: ""`, `depth_metres: 0` and
  `harbour: north-basin`.
- [`example-enum-member/openapi.yml`](../../fern-measurements/handed-off/example-values/example-enum-member/openapi.yml):
  the body's `kinds` array names `AlertKind`, an enum of `*`, `beacon_lit`,
  `beacon_out` declaring `example: beacon_lit`.
- [`example-value-source/openapi.yml`](../../fern-measurements/handed-off/example-values/example-value-source/openapi.yml):
  a multipart part `title` (`example: Lizard Point`), a query parameter
  `scale` (`example: "1:25000"`) on an operation answering `application/pdf`,
  and a path parameter `harbourSlug` (`example: cornwall/porthleven`) beside
  `berthRef`, whose schema is `{}`.

## Both outputs and the declared value

`reference.md`, the certified pair's line first and crozier's second (the same
pairs appear in `README.md` and both docstrings of each method):

```text
falsy-property-example   survey_ref="X-Survey-Ref",   survey_ref="",            declared ""
                         label="label",               label="",                 declared ""
                         depth_metres=1,              depth_metres=0,           declared 0
                         harbour="harbour",           harbour="north-basin",    declared north-basin
example-enum-member      AlertKind.ALL                AlertKind.BEACON_LIT      declared beacon_lit
                         "*"   (literals)             "beacon_lit"   (literals)
example-value-source     title="title",               title="Lizard Point",     declared Lizard Point
                         scale="scale",               scale="1:25000",          declared 1:25000
                         harbour_slug="harbourSlug",  harbour_slug="cornwall/porthleven"
```

On both sides each value has the argument's annotated type (a `str`, an `int`
or a member of the argument's enum, read off the generated signatures; no call
was executed): no binding defect is claimed either way. The certified pair's values are synthesized from
the argument's name (or its enum's first member); crozier's are the values the
document declares, which the ruling keeps. Synthesized placeholders never count
as more useful.

## The rule

`declared_values::declared_example_over_placeholder` admits a worked-example
argument line only where Fern writes the argument's wire name, `1`,
`1000000`, `1.1` or `True`, and crozier writes exactly the literal the source
document declares for that argument in one of the shapes above; or an enum list
item where Fern names the enum's first member and crozier the member its schema
declares as its example. The `multipart-object-required-file-example` region
tolerates exactly these lines beside the file it corrects. The crozier-e2e test
`handed_off_example_values::declared_value_departures_hold_only_their_lines`
shows an adjacent unexplained change still fails.

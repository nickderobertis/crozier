# `colliding-component-own-class`

**Kind:** `fern-defect`. Issue
[#944](https://github.com/nickderobertis/crozier/issues/944); manager rulings
`a1` and `a3`.

## The document

[`docs/fern-measurements/naming-acceptance/normalized-component-identity/openapi.yml`](../../fern-measurements/naming-acceptance/normalized-component-identity/openapi.yml)
declares two components whose names spell one class, `kiln/glaze-coat`
(`left: string`, required) and `kiln-glaze/coat` (`right: integer`, required),
and one inline request body naming both: `left: $ref kiln/glaze-coat`,
`right: $ref kiln-glaze/coat`.

## What the certified pair writes

`fern-expected/` beside that document is Fern CLI 5.216.0 with
`fernapi/fern-python-sdk` 5.42.0 (`just fern-references measurements
naming-acceptance/normalized-component-identity`; `fern check` and
`fern generate` both exit 0). It holds one class for both components, the last
declaration's:

```text
$ grep -h '^class\|^    [a-z]*:' src/fern/types/kiln_glaze_coat.py
class KilnGlazeCoat(UniversalBaseModel):
    right: int
$ grep -n 'left' src/fern/client.py | head -1
112:        left: typing.Optional[KilnGlazeCoat] = OMIT,
```

So `create_records(left=...)` takes the `right`-holding model: a caller cannot
build the `left` object the document declares, and a server answering with
`{"left": "matte"}` where `kiln/glaze-coat` is the declared response fails
`KilnGlazeCoat`'s validation (its required `right` is missing). That is a
runtime failure under the defect rule.

## What crozier writes

```text
$ crozier generate --spec docs/fern-measurements/naming-acceptance/normalized-component-identity/openapi.yml \
    --output /tmp/n944 --package-name fern --project-name default_package_name
$ diff fern-expected/src/fern/client.py /tmp/n944/src/fern/client.py | grep '^[<>]'
> from .types.kiln_glaze_coat2 import KilnGlazeCoat2
<         left: typing.Optional[KilnGlazeCoat] = OMIT,
>         left: typing.Optional[KilnGlazeCoat2] = OMIT,
<         left : typing.Optional[KilnGlazeCoat]
>         left : typing.Optional[KilnGlazeCoat2]
$ grep -h '^class\|^    [a-z]*:' /tmp/n944/src/fern/types/kiln_glaze_coat.py /tmp/n944/src/fern/types/kiln_glaze_coat2.py
class KilnGlazeCoat(UniversalBaseModel):
    right: int
class KilnGlazeCoat2(UniversalBaseModel):
    left: str
```

`kiln-glaze/coat`, the last declaration, keeps Fern's `KilnGlazeCoat` and its
module byte for byte; `kiln/glaze-coat` is `KilnGlazeCoat2`, the shared class
followed by the first ordinal from 2 no other component's class spells, which
depends only on the document. The rule (`src/departures.rs`,
`colliding_component_own_class`) reads the renamed classes from the source
document's load (`src/openapi.rs::normalize_colliding_component_classes`
records each one's shared class) and accepts exactly: a line that is Fern's
once each renamed class is read as the class Fern merged it into (an import
list repeating the name keeps it once), a line only crozier writes naming a
renamed class or its module, and the renamed class's own module under
`types/`. Every other difference in those files remains a difference.

`crates/crozier-e2e/tests/e2e/naming_acceptance.rs` holds the tree whole in
both enum modes with the departure applied, generates the two sibling
measurements (both colliding components as responses, and the one-component
control), and its SDK-environment journey sends each request and parses each
response through the generated client.

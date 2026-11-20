# #828's trigger: a list item whose member requires a null-bearing nested union

Issue [#828](https://github.com/nickderobertis/crozier/issues/828), the
`union-body-item-example` residual of Vercel (`65e9c34e`, rows 43–44 of
[`../../residuals.tsv`](../../residuals.tsv)). Both documents here were authored
from scratch with the shape of Vercel's `PATCH /v1/edge-config/{edgeConfigId}/items`
body: `entries` is an array of `oneOf` items, whose first member requires
`label`, `operation` and a `payload` that is a `oneOf` of a `oneOf` of scalar
and object members and an array of the same. `patchShelfTags` (a single-level
`payload` union) and `patchShelfNotes` (a plain object item with the nested
`payload`) are controls beside it.

| Document | SHA-256 | `payload`'s members |
| --- | --- | --- |
| [`with-null.openapi.yml`](with-null.openapi.yml) | `7abfb12020bd76ca5e53b86930e636eeca82d4af645ec7bb918b91e05efd2606` | string, number, boolean, **null**, object |
| [`without-null.openapi.yml`](without-null.openapi.yml) | `7ce6a79cde19eaabb3903e6761f06ed523660e318b01d5f57a4e47e543b904e4` | string, number, boolean, object |

Fern CLI 5.200.0 with `fernapi/fern-python-sdk` 5.41.25 generated each through
`fern-references.py generate measurements` under the shared generation lock
(packaged preview layout, organization/package `fern`,
`pydantic_config.enum_type: python_enums`) on 2026-11-17. The trees are kept in
this host's certified-tree store under those digests, not committed: neither is
a gate input (below).

## What the certified pair writes

**With the `null` members**, the certified `reference.md` (line 24) and README
write the union-item list empty, `entries=[],`. The docstring example of
`patch_shelf_entries` (sync and async) constructs the item without its
required field:

```python
            entries=[
                PatchShelfEntriesRequestEntriesItemPayload(
                    label="label",
                    operation=PatchShelfEntriesRequestEntriesItemPayloadOperation.CREATE,
                )
            ],
```

while `PatchShelfEntriesRequestEntriesItemPayload` declares
`payload: PatchShelfEntriesRequestEntriesItemPayloadPayload` with no default, so
that construction is the invalid example the issue names. The controls behave
the same way about `null` in `reference.md`: the plain-object `notes` item is
written without `payload`, and the single-level `tags` union writes
`payload=None`.

**Without the `null` members**, the same three lists are populated in Markdown
and docstrings alike, each item with `payload="payload"`, and crozier already
writes exactly that.

## Repaired

The `union-member-nullability-and-object-models` repair landed first, so the
payload types match the certified pair, and the follow-on
`union-member-nullability-2` then repaired #828 against
[`union-inheritance/list-item-nested-union`](../../../union-inheritance/list-item-nested-union/openapi.yml),
a copy of `with-null.openapi.yml` whose certified trees in both enum modes are
committed there. The README's and `reference.md`'s `entries=[],` now match. So
does `reference.md`'s `tags` item. The two omissions of a required field, in the
docstrings and in `reference.md`'s `notes` item, are the `fern-defect` departure
`required-null-union-field-example`. Its
[evidence](../../../../departures/evidence/required-null-union-field-example.md)
executes each certified construction and shows it raising pydantic's
`ValidationError` for the missing `payload`. The departure entry covers any
worked example, in a docstring or in Markdown, that omits a required field
whose union opens with an optional member. Its rule admits only the one keyword
line inside a constructor whose class requires that field in Fern's own tree.

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

## Why this is not repaired here

The trigger is the `null` member itself, and a `null` member inside a union is
the shape of the separate residual `union-member-nullability-and-object-models`
(Vercel rows 45–57): the certified pair types those members
`typing.Optional[…]` and drops the `null` alternative, where crozier keeps it as
`typing.Any`. Every document exhibiting #828 therefore also differs on that
residual (the with-null comparison differs on all six `payload` type modules),
so no reduction for #828 alone can byte-match whole, and a Markdown selection
rule written against crozier's current union IR would have to be rewritten once
that IR changes. By the manager's rulings `a5` and `a6`, the member-nullability
repair belongs to the `combinations-schemas-2` node, and #828's emit rule (the
empty Markdown list) and its `fern-defect` departure (the docstring's omitted
required field) belong to a follow-on node that runs after it lands; these two
documents are its measured trigger.

## Scope of the departure the follow-on writes

By the manager's ruling `c24.1`, `combinations-schemas` will cite this
departure where Fern's union usage example omits a required field (its ticket
#825: a union whose first alternative becomes `Optional`). The behaviour
measured here is of that general kind: in every omission above, the field left
out is required and typed by a union carrying a `null` member, whether the
model holding it is a union item (`entries`) or a plain list item (`notes`, in
`reference.md`). So the follow-on's `fern-defect` entry should be worded for a
worked example, in a docstring or in Markdown, that omits a required field whose
union type Fern makes `Optional`, not only for a list of union items. Its rule
should then admit only the shapes it can hold to a certified tree. These two
reductions measure the list-item and plain-item cases; #825's own measurement
is that node's evidence.

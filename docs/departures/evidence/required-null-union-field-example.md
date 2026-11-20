# Worked examples omit a required field typed by a null-bearing union

The certified pair (Fern CLI 5.200.0, `fernapi/fern-python-sdk` 5.41.25,
packaged preview layout, organization/package `fern`, project
`default_package_name`, no audience filter) types a union whose first member is
itself a union carrying a `null` member with that alternative made optional,
`Union[Optional[…Zero], List[Optional[…OneItem]]]`. A model's required property
of that type is declared with no default, yet Fern's example writer samples it
as null and leaves it out of the constructor. Issue
[#828](https://github.com/nickderobertis/crozier/issues/828) first found this.

The from-scratch measurement
[`union-inheritance/list-item-nested-union`](../../fern-measurements/union-inheritance/list-item-nested-union/openapi.yml)
(the reduction first certified in
[`828-list-item-nested-union/`](../../fern-measurements/handed-off/remeasure/828-list-item-nested-union/README.md))
holds its unedited certified tree in `fern-expected/` (`python_enums`) and its
literals overlay in `expected-literals/fern-expected/` (`enum_type` unset). Its
`PatchShelfEntriesRequestEntriesItemPayload` declares
`payload: PatchShelfEntriesRequestEntriesItemPayloadPayload` and
`PatchShelfNotesRequestNotesItem` declares
`payload: PatchShelfNotesRequestNotesItemPayload`, both with no default. Both
client docstrings (`src/fern/client.py` lines 144, 226, 382 and 482) construct
those models without `payload`, and so does `reference.md` (line 165) for
the plain `notes` item. The certified Markdown writes the list of union items
`entries=[]`, which is valid and which crozier matches. The single-level control
`tags` (whose union holds the `null` directly, so its field is
`Optional[…] = None`) is valid in both trees.

The registered Vercel document (`65e9c34e…`, the certified store's tree for it at
this pair) shows the same shape at `PatchtEdgeConfigItemsRequestItemsItemValue`,
whose `value` the `patcht_edge_config_items` docstrings
(`src/fern/edge_config/client.py`) leave out.

## Executed construction

The committed [proof script](required-null-union-field-example.py) finds every
model of an SDK that has such a field, and evaluates every constructor of one in
a client docstring or `reference.md` against the generated package. Run on
2026-11-21 with Python 3.14, Pydantic 2.14.4 and HTTPX:

```sh
python docs/departures/evidence/required-null-union-field-example.py \
  docs/fern-measurements/union-inheritance/list-item-nested-union/fern-expected invalid
```

```text
src/fern/client.py:144: ValidationError: missing payload
src/fern/client.py:226: ValidationError: missing payload
src/fern/client.py:382: ValidationError: missing payload
src/fern/client.py:482: ValidationError: missing payload
reference.md:165: ValidationError: missing payload
```

It exited 0. Over the certified Vercel trees it printed
`src/fern/edge_config/client.py:366: ValidationError: missing value` and `:960`
(`python_enums`), and `:363` and `:954` (literals). The same script with `valid`
over crozier's SDKs for both documents prints `constructs` for each, in both
enum modes. `sdk_env_required_null_union_field_examples_construct_where_fern_s_fail`
in `crates/crozier-e2e/tests/e2e/union_inheritance.rs` runs both directions on
every `just test-sdk-env`.

## What crozier writes

crozier writes the same constructor with the field's synthesized example, a
one-line value its union admits (`payload="payload",` / `value="value",`). Every
other argument, the imports and the method signature are unchanged. The rule
admits only that one keyword line inside a constructor whose class, in Fern's
own tree, requires the field with a union alias opening `typing.Optional[`. Any
other added argument, or such a field in a model Fern gives a default, is still
a difference. The line ledger is recorded from `src/parity.rs`, never hand-edited.

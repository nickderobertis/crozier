# A docstring constructs a model without its required union field

Vercel's `patchtEdgeConfigItems` (`APIs-guru/openapi-directory`, `APIs/vercel.com/0.0.1/openapi.yaml`, revision `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, SHA-256 `65e9c34eefc5925ec44f6a375912deabcd7354f9e15d1af94533cf98b7bb2b48`) takes a list of a `oneOf` whose first object requires `value`, a `oneOf` led by a `oneOf` with a `null` member.

Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3 declares the required field in `src/fern/edge_config/types/patcht_edge_config_items_request_items_item_value.py`:

```python
value: PatchtEdgeConfigItemsRequestItemsItemValueValue
```

Its sync and async docstrings in `src/fern/edge_config/client.py` construct the model without it:

```python
PatchtEdgeConfigItemsRequestItemsItemValue(
    key="key",
    operation=PatchtEdgeConfigItemsRequestItemsItemValueOperation.CREATE,
)
```

Importing the certified package and running that constructor fails:

```text
ValidationError ['1 validation error for PatchtEdgeConfigItemsRequestItemsItemValue', 'value', "  Field required [type=missing, ...]"]
```

The same call with crozier's added `value="value",` line constructs the model; the field's union admits a string. This is the standing defect kind of an example that does not match the signature. No method or model was mocked: the run used the certified tree on `PYTHONPATH` with pydantic 2 and httpx installed.

The rule accepts only a `<field>="<field>",` line in a `client.py` docstring constructor, for a `(class, field)` crozier's own models type this way. Any other value, field or model stays a mismatch, as `a_required_null_union_field_line_is_excused_only_on_its_own_model` shows. Vercel is not a registered corpus row, because it still differs on `union-member-nullability-and-object-models`, so this departure has no ledger lines yet.

# A list example written with Fern's fixed number of items

Fern's worked example writes a list with one item (two where its fallback
example writer builds the operation's example), whatever the schema's
`minItems` or `maxItems` say. discord's `bulk_delete_messages` posts
`messages: {type: array, items: {$ref: SnowflakeType}, minItems: 2,
maxItems: 100, uniqueItems: true}`, and its committed golden (Fern CLI 5.163.1
with `fernapi/fern-python-sdk` 5.41.3, corpus row `discord-com`) passes
`messages=["messages"]`: one item, which `minItems` rejects, and an item
`SnowflakeType`'s pattern rejects too. The API refuses that call, so the
example is invalid for its own schema: a defect under the defect rule. The same
construction writes one `GraphNode` beneath `minItems: 5` in
`ecommerce-ai-skills-runtime` and one item beneath `maxItems: 0` there.

crozier writes the schema's own declared example, else its `default`, each only
when the schema accepts it, else Fern's items cut to `maxItems` or padded to
`minItems`. A list declaring `uniqueItems: true` is padded only with items that
are pairwise distinct and each accepted by the item schema — the next strings
its `pattern` matches, its `enum`'s members, numbered variants of a plain
string, or numbers stepped within its bounds — and any other list with copies
of its first item. Where Fern writes the list empty — a tuple's
`prefixItems` it has no item for, a nullable item an executable docstring
leaves out, a recursive item it stops at — crozier writes the items the
schema's own shape builds (`seed_of` in `src/example_values.rs`): each
`prefixItems` member's value, or `minItems` copies of its items' value, where
a nullable item is `None`, a free-form one Fern's `{"key": "value"}`, and an
object its required properties', a union's inline member before a reference.
marimo's `x_bounds`, `{type: array, prefixItems: [{type: number}, {type:
number}], minItems: 2, maxItems: 2}`, which Fern writes `x_bounds=[]`, is
`x_bounds=[1.1, 1.1]`; RS-Server's `interval=[[]]` is `[[None, None]]`; and
sim-tables' `all_=[]`, whose items are a recursive predicate or a condition,
is one `TablePredicateAllAllItemField(field="string", op=…EQ)`, which the
example's import then names. Where no distinct items can be built, Fern's
value stays and the inventory records a `residual-unconstructible` row. The items' own repairs are those of
the other `schema-rejected-*` departures. Every list this departure repairs is
a `schema-rejected-array-length-example` row of
[the inventory](invalid-example-values/inventory.tsv).

## Executed evidence

Generated and validated on 2026-10-25 with crozier at this change, Python
3.14.7 and jsonschema 4.26.0, which reads the whole property schema,
`uniqueItems` included:

```sh
crozier generate python --spec tests/fixtures/corpus-sources/discord-com/openapi.json \
  --output /tmp/discord --package-name fern --project-name default_package_name --no-config
python3 docs/departures/evidence/invalid-example-values/validate.py \
  tests/fixtures/corpus-sources/discord-com/openapi.json \
  '/paths/~1channels~1{channel_id}~1messages~1bulk-delete/post/requestBody/content/application~1json/schema/properties/messages' \
  tests/fixtures/discord-com/expected/src/fern/client.py:2154 \
  /tmp/discord/src/fern/client.py:2154 messages
```

It exited 0 and reported:

```text
fern messages=['messages']: rejected: ['messages'] is too short
crozier messages=['0', '1']: accepted
```

An empty list, generated and validated on 2026-11-21 the same way against the
golden regenerated at Fern CLI 5.216.0 with `fernapi/fern-python-sdk` 5.42.0:

```sh
crozier generate python --spec tests/fixtures/corpus-sources/marimo-plugins/openapi.yaml \
  --output /tmp/marimo-plugins --package-name fern --project-name default_package_name --no-config
python3 docs/departures/evidence/invalid-example-values/validate.py \
  tests/fixtures/corpus-sources/marimo-plugins/openapi.yaml \
  /components/schemas/marimo-matplotlib.data/properties/xBounds \
  tests/fixtures/marimo-plugins/expected/src/fern/plugin_data/client.py:1965 \
  /tmp/marimo-plugins/src/fern/plugin_data/client.py:1965 x_bounds
```

It exited 0 and reported:

```text
fern x_bounds=[]: rejected: [] is too short
crozier x_bounds=[1.1, 1.1]: accepted
```

## The rule

The comparison's region rule reads the parsed source document. It reads one
list argument of an example on both sides, item by item across lines, and
accepts it only where the count changed, a list schema the document declares
for that argument rejects Fern's count and chooses crozier's, the items Fern
wrote are kept (equal, or differing only in literals another
`schema-rejected-*` departure repairs), and every added item is a copy of the
first or, under `uniqueItems`, exactly the distinct items the item schema's
repair builds. Where the list spans lines the region is only its added items,
so the first item's own repairs keep their own lines. A list Fern writes
empty is accepted only where crozier's items are exactly those the schema's
shape builds, and a same-count list (`windows=[[]]`) only where a list nested
in it is such a list. The example's `from … import` line is accepted beside
it only where crozier's keeps every name Fern's imports and each name it adds
is constructed in such a list (`a_seeded_list_s_model_import_is_the_array_departure_s_and_nothing_else`).
`each_rejected_example_rule_accounts_for_its_repair_and_nothing_else` in
`src/departures.rs` holds the negative cases.

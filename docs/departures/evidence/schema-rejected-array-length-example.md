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
of its first item. Where no distinct items can be built, or Fern wrote the
list empty and there is no item to copy, Fern's value stays and the inventory
records a `residual-unconstructible` row. The items' own repairs are those of
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

## The rule

The comparison's region rule reads the parsed source document. It reads one
list argument of an example on both sides, item by item across lines, and
accepts it only where the count changed, a list schema the document declares
for that argument rejects Fern's count and chooses crozier's, the items Fern
wrote are kept (equal, or differing only in literals another
`schema-rejected-*` departure repairs), and every added item is a copy of the
first or, under `uniqueItems`, exactly the distinct items the item schema's
repair builds. Where the list spans lines the region is only its added items,
so the first item's own repairs keep their own lines.
`each_rejected_example_rule_accounts_for_its_repair_and_nothing_else` in
`src/departures.rs` holds the negative cases.

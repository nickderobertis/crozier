# A number example written as Fern's fixed placeholder

Where a number declares no example Fern uses, Fern's worked example passes a
fixed placeholder — `1` for an integer, `1000000` for an `int64`, `1.1` for a
float — whatever the schema's bounds, `enum`, `const` or `multipleOf` say.
discord's `DefaultKeywordListUpsertRequest.trigger_type` is
`{type: integer, enum: [4], allOf: [$ref AutomodTriggerType], format: int32}`,
and its committed golden (Fern CLI 5.163.1 with `fernapi/fern-python-sdk`
5.41.3, corpus row `discord-com`) passes `trigger_type=1`. The `enum` rejects
it, so the example is invalid for its own schema: a defect under the defect
rule. The same construction writes `interval_minutes=1` beneath `minimum: 60`
in `ecommerce-ai-skills-runtime`, `chain_id=1` beneath `const: 4663` in
`fletch-mcp`, and `due_days=1.1` beneath `minimum: 7` in `fergus`.

crozier writes the schema's own declared example, else its `default`, each only
when the schema accepts it, else a value constructed to satisfy every in-scope
keyword: a declared `const` or `enum` member first, else Fern's placeholder
moved inside the bounds and onto the `multipleOf` grid. Every value this
departure repairs is a `schema-rejected-number-example` row of
[the inventory](invalid-example-values/inventory.tsv).

## Executed evidence

Generated and validated on 2026-10-25 with crozier at this change, Python
3.14.7 and jsonschema 4.26.0:

```sh
crozier generate python --spec tests/fixtures/corpus-sources/discord-com/openapi.json \
  --output /tmp/discord --package-name fern --project-name default_package_name --no-config
python3 docs/departures/evidence/invalid-example-values/validate.py \
  tests/fixtures/corpus-sources/discord-com/openapi.json \
  /components/schemas/DefaultKeywordListUpsertRequest/properties/trigger_type \
  tests/fixtures/discord-com/expected/src/fern/client.py:3025 \
  /tmp/discord/src/fern/client.py:3025 trigger_type
```

It exited 0 and reported:

```text
fern trigger_type=1: rejected: 1 is not one of [4]
crozier trigger_type=4: accepted
```

## The rule

The comparison's rule reads the parsed source document. It accepts an example
line only where the two lines differ in literals alone, Fern's literal is one
of the fixed placeholders, a number schema the document declares rejects it,
and crozier's is the value the repair chooses for that schema. Its negative
regressions are those of `each_rejected_example_rule_accounts_for_its_repair_and_nothing_else`.

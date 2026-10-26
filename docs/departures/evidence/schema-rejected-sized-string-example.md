# A string example sized by its lengths alone

Where Fern's importer builds no example for an operation, its fallback example
writer samples a string one `minLength` long (or one `maxLength` long, under
ten), from a fixed list of words — `"apricot"` for seven, `"strawberry"` for
ten — and reads no other keyword. amazonaws.com-cloudformation's `TypeName` is
`{type: string, pattern: "[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}", minLength: 10, maxLength: 204}`,
and its committed golden (Fern CLI 5.163.1 with `fernapi/fern-python-sdk`
5.41.3, corpus row `amazonaws.com-cloudformation`) passes
`type_name="strawberry"` to `get_register_type`. The pattern requires `::`
separators, so the example is invalid for its own schema: a defect under the
defect rule. A sample the schema accepts is Fern's value and stays: nexmo's
`to="apricot"` satisfies `ToNumber`'s `minLength: 7` and `maxLength: 15`, the
only keywords it declares.

crozier writes the schema's own declared example, else its `default`, each only
when the schema accepts it, else a value constructed to satisfy every in-scope
keyword: `"aa::aa::aa"` here. Every value this departure repairs is a
`schema-rejected-sized-string-example` row of
[the inventory](invalid-example-values/inventory.tsv).

## Executed evidence

Generated and validated on 2026-10-25 with crozier at this change, Python
3.14.7 and jsonschema 4.26.0:

```sh
crozier generate python --spec tests/fixtures/corpus-sources/amazonaws.com-cloudformation/openapi.json \
  --output /tmp/cloudformation --package-name fern --project-name default_package_name --no-config
python3 docs/departures/evidence/invalid-example-values/validate.py \
  tests/fixtures/corpus-sources/amazonaws.com-cloudformation/openapi.json /components/schemas/TypeName \
  tests/fixtures/amazonaws.com-cloudformation/expected/src/fern/client.py:7497 \
  /tmp/cloudformation/src/fern/client.py:7497 type_name
```

It exited 0 and reported:

```text
fern type_name='strawberry': rejected: 'strawberry' does not match '[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}'
crozier type_name='aa::aa::aa': accepted
```

## The rule

The comparison's rule reads the parsed source document. It accepts an example
line only where the two lines differ in literals alone, Fern's literal is the
sample a string schema's declared lengths give, that schema rejects it, and
crozier's is the value the repair chooses for it. Its negative regressions are
those of `each_rejected_example_rule_accounts_for_its_repair_and_nothing_else`.

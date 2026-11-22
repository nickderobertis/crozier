# A declared example its own schema rejects

Where the specification declares an example — a schema's `example`,
`examples` or `default`, or an enclosing request body's or parameter's example
— Fern's worked example passes it as written, whether or not the schema it
documents accepts it. dot-ai's `operateRequest.executeChoice` is
`{type: number, minimum: 1, maximum: 1}`, its `POST /api/v1/tools/operate`
body example declares `executeChoice: 42`, and its committed golden (corpus
row `dot-ai`, regenerated at Fern CLI 5.216.0 with `fernapi/fern-python-sdk`
5.42.0) passes `execute_choice=42.0`. The `maximum` rejects it, so the example
is invalid for its own schema: a defect under the defect rule, whoever chose
the value. The same holds for RayBot's `ip="192.168.1.100/24"` beneath
`format: ipv4`, ADME Seismic's `checksum="checksum-value"` beneath
`pattern: ^[0-9a-fA-F]{32}`, dcp-ai's `session_nonce="a1b2c3..."` beneath
`pattern: ^[0-9a-f]{64}$`, milvus' `offset=0` beneath `exclusiveMinimum: 0`,
and the empty strings Supabase and the apifox lab declare beneath a
`minLength`.

crozier writes Fern's own construction for the slot where the schema accepts
it (dot-ai's `remediateRequest.executeChoice`, beneath `maximum: 2`, is Fern's
float `1.1`), else another declared example the schema accepts, else its
`default` when the schema accepts it, else a value constructed to satisfy
every in-scope keyword (`execute_choice=1.0`). Where no such value exists or
crozier cannot decide validity, Fern's value stays. Every value this departure
repairs is a `schema-rejected-declared-example` row of
[the inventory](invalid-example-values/inventory.tsv).

A declared value crozier itself keeps where Fern writes its placeholder
([`declared-example-over-placeholder`](declared-example-over-placeholder.md))
is held to the same bar: where its schema rejects it, crozier writes Fern's
placeholder when the schema accepts that, matching Fern, and otherwise the
placeholder's own repair.

## Executed evidence

Generated and validated on 2026-11-21 with crozier at this change, Python
3.14.7 and jsonschema 4.26.0:

```sh
crozier generate python --spec tests/fixtures/corpus-sources/dot-ai/openapi.json \
  --output /tmp/dot-ai --package-name fern --project-name default_package_name --no-config
python3 docs/departures/evidence/invalid-example-values/validate.py \
  tests/fixtures/corpus-sources/dot-ai/openapi.json \
  /components/schemas/operateRequest/properties/executeChoice \
  tests/fixtures/dot-ai/expected/src/fern/operations/client.py:80 \
  /tmp/dot-ai/src/fern/operations/client.py:80 execute_choice
```

It exited 0 and reported:

```text
fern execute_choice=42.0: rejected: 42.0 is greater than the maximum of 1
crozier execute_choice=1.0: accepted
```

## The rule

The comparison's rule reads the parsed source document. It accepts an example
line only where the two lines differ in literals alone, Fern's literal is a
scalar the document declares somewhere (a leaf of any `example`, `examples` or
`default`, a media type's or parameter's included) and no construction of
Fern's for the argument's schema, a schema the document declares for that
argument rejects it, and crozier's is the value the repair chooses for that
schema or Fern's own construction for it where the schema accepts that. Its
negative regressions are those of
`each_rejected_example_rule_accounts_for_its_repair_and_nothing_else`: a
replacement the schema rejects, an accepted value the repair does not choose,
a rejected value the document never declares, a value the schema accepts, a
runtime line, and a comparison without the source document are each refused.

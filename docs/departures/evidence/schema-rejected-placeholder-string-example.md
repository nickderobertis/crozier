# A string example written as Fern's fixed placeholder

Where a string has no name to stand for it — a bare string request body, a
map's value — Fern's worked example passes the fixed placeholder `"string"`
or `"value"`, whatever the schema says. audiobookshelf's
`addAuthorImageById` posts `#/components/schemas/imageUrl`, a string with
`format: uri`, and its committed golden (Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3, corpus row `audiobookshelf`) passes
`request="string"` in its README, `reference.md` and both client docstrings. A
URI has a scheme; `string` has none, so the example is invalid for its own
schema: a defect under the defect rule.

crozier writes the schema's own declared example, else its `default`, each only
when the schema accepts it, else a value constructed to satisfy every in-scope
keyword. `imageUrl` declares an example the schema accepts, so crozier passes
it. Every value this departure repairs is a
`schema-rejected-placeholder-string-example` row of
[the inventory](invalid-example-values/inventory.tsv).

## Executed evidence

Generated and validated on 2026-10-25 with crozier at this change, Python
3.14.7 and jsonschema 4.26.0. jsonschema asserts `uri` only with the optional
`rfc3987` package installed; the [validator](invalid-example-values/validate.py)
asserts it with the standard library otherwise, by RFC 3986's `URI` rule:

```sh
crozier generate python --spec tests/fixtures/corpus-sources/audiobookshelf/openapi.json \
  --output /tmp/audiobookshelf --package-name fern --project-name default_package_name --no-config
python3 docs/departures/evidence/invalid-example-values/validate.py \
  tests/fixtures/corpus-sources/audiobookshelf/openapi.json /components/schemas/imageUrl \
  tests/fixtures/audiobookshelf/expected/README.md:46 \
  /tmp/audiobookshelf/README.md:46 request
```

It exited 0 and reported:

```text
fern request='string': rejected: 'string' is not a 'uri'
crozier request='https://images-na.ssl-images-amazon.com/images/I/51NoQTm33OL.__01_SX120_CR0,0,120,120__.jpg': accepted
```

## The rule

The comparison's rule reads the parsed source document. It accepts an example
line only where the two lines differ in literals alone, Fern's literal is the
placeholder, a string schema the document declares rejects it, and crozier's
is the value the repair chooses for that schema. Its negative regressions are
those of `each_rejected_example_rule_accounts_for_its_repair_and_nothing_else`.

# A string example written as its own name

Where a string parameter or property declares no example Fern uses, Fern's
worked example passes the parameter's or property's own name as its value,
whatever the schema says. discord's `SnowflakeType` is
`{type: string, pattern: "^(0|[1-9][0-9]*)$", format: snowflake}`, and its
committed golden (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3,
corpus row `discord-com`) passes `guild_id="guild_id"` 186 times in
`src/fern/client.py` and 93 times in `reference.md`; the pattern rejects every
one. The API answers a call shaped like the example with a 4xx, so the example
is invalid for its own schema: a defect under the defect rule.

crozier writes, in this order, the schema's own declared example, its declared
`default`, each only when the schema accepts it, or a value constructed to
satisfy every in-scope keyword: `"0"` here, the shortest string the pattern
matches. The argument, its place and every other line are Fern's. Every value
this departure repairs is a `schema-rejected-name-example` row of
[the inventory](invalid-example-values/inventory.tsv).

## Executed evidence

Generated and validated on 2026-10-25 with crozier at this change, Python
3.14.7 and jsonschema 4.26.0, whose format assertions the
[validator](invalid-example-values/validate.py) completes with the standard
library where jsonschema needs an optional package:

```sh
crozier generate python --spec tests/fixtures/corpus-sources/discord-com/openapi.json \
  --output /tmp/discord --package-name fern --project-name default_package_name --no-config
python3 docs/departures/evidence/invalid-example-values/validate.py \
  tests/fixtures/corpus-sources/discord-com/openapi.json /components/schemas/SnowflakeType \
  tests/fixtures/discord-com/expected/src/fern/client.py:9367 \
  /tmp/discord/src/fern/client.py:9367 guild_id
```

It exited 0 and reported:

```text
fern guild_id='guild_id': rejected: 'guild_id' does not match '^(0|[1-9][0-9]*)$'
crozier guild_id='0': accepted
```

The same holds for a `format` the name does not satisfy: discord's
`sender.html_url` (`format: uri`) is `"html_url"` in Fern's examples and
`"https://example.com"` in crozier's.

## The rule

The comparison's rule reads the parsed source document. It accepts an example
line of `README.md`, `reference.md` or a client module's docstring only where
the two lines differ in literals alone, Fern's literal is the name of a
parameter or property the document declares, that node's schema rejects it,
and crozier's is the value the repair chooses for that schema.
`each_rejected_example_rule_accounts_for_its_repair_and_nothing_else` in
`src/departures.rs` holds that a replacement the schema rejects, a change to a
value the schema accepts, the same change outside a documented example, and a
comparison without the source document all still fail.

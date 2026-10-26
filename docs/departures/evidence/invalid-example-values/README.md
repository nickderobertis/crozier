# Worked-example values their own schema rejects

[`inventory.tsv`](inventory.tsv) lists every worked-example value Fern writes,
in the `README.md`, `reference.md` and client docstrings of every Fern tree a
golden comparison reads, that an in-scope keyword or format of the schema it
documents rejects — and what crozier writes there instead. The trees are the
population [`tests/fixtures/departures-ledger.tsv`](../../../../tests/fixtures/departures-ledger.tsv)
keys on: corpus goldens and their overlays, flat goldens, hand-written
fixtures, and the measurement and probe trees.

## How the values are found

Nothing here matches names or text. crozier's example writer knows the schema
behind every value it writes: each parameter, body field, model field and
alias carries the in-scope keywords of its source schema
([`src/example_values.rs`](../../../../src/example_values.rs)), read through
`$ref`s and `allOf` members, a discarded `allOf` included. After an example is
built, [`src/emit/example_repair.rs`](../../../../src/emit/example_repair.rs)
validates each scalar value, each list's length and items, each map's values and
each model constructor's fields against those keywords, and records every value
they reject with the line it lands on. crozier byte-matches Fern on every tree
before the repair, so the value the writer built is Fern's value; the golden
comparison checks that Fern's own line holds it.

A value is rejected when it fails one of these:

- a string's `pattern`, `minLength`, `maxLength`, `enum` or `const`;
- a number's `minimum`, `maximum`, `exclusiveMinimum` (3.1's number or 3.0's
  `true`), `exclusiveMaximum` or `multipleOf`;
- an array's `minItems` or `maxItems`;
- `format` `date`, `date-time`, `time`, `uuid`, `email`, `uri`, `ipv4`, `ipv6`
  or `hostname`, and the `int32` and `int64` ranges.

Any other keyword or format neither rejects a value nor blocks a repair.
`oneOf`, `anyOf` and `not` are among them. A `date` or `date-time` property
crozier types as `datetime.date` or `datetime.datetime` is a constructed
object, not a string, and is not read.

## Columns

The first line is the header. Each row has eight tab-separated fields, and rows
sort by `golden`, `file`, `line` and `argument`:

| Column | Holds |
| --- | --- |
| `golden` | the Fern tree's path, spelled as the departure ledger spells it |
| `file` | the path inside that tree |
| `line` | Fern's 1-based line |
| `argument` | the keyword argument; inside a body, the dotted path to the value (`request.sender.html_url`), a list item as `[index]` |
| `fern_value` | the value as Fern writes it |
| `constraint` | the first rejecting keyword and its declared value, such as `pattern=^(0|[1-9][0-9]*)$` |
| `mechanism` | the id of the departure covering the row's mechanism, or `-` where none applies |
| `disposition` | one of the five below |

## Dispositions

- `repaired`: crozier writes a value the schema accepts instead: the
  specification's own declared example for that schema, else its `default`,
  each only when the schema accepts it, else a value constructed
  deterministically to satisfy every keyword above.
- `declared-in-spec`: the value is the specification's own declared example,
  which stays.
- `out-of-scope-keyword`: only a keyword or format outside the set above
  rejects the value.
- `residual-undecidable`: crozier cannot decide validity: a pattern it cannot
  compile, a `$ref` that does not resolve, or an enum member the enum's own
  example selection (`pattern-narrowed-enum-example`) cannot decide although
  another member is valid.
- `residual-unconstructible`: no value satisfies every keyword (no enum member
  does), or crozier cannot build one: a pattern holding a lookaround or
  backreference, a list Fern writes empty with no item to copy, or a
  `uniqueItems` list whose padding would need distinct items crozier cannot
  build.

Every row that is not `repaired` keeps Fern's bytes.

## Mechanisms

Fern's constructions are a string's own name, its fixed `"string"` and
`"value"` placeholders, a string its fallback writer sizes by the declared
lengths, the fixed numbers `1`, `1000000` and `1.1`, a list's fixed item count,
and an enum's first member. Each but the last is one `schema-rejected-*`
`fern-defect` entry of
[`assets/departures.yml`](../../../../assets/departures.yml), whose rule in
[`src/departures/rejected_examples.rs`](../../../../src/departures/rejected_examples.rs)
reads the parsed source document. It accounts for a line only where Fern's
value is that construction's, a source schema rejects it, and crozier's is the
value that schema's repair chooses. An enum's first member is corrected, where
it can be, by the earlier `pattern-narrowed-enum-example` entry, which its rows
name. A value Fern did not construct — the specification's own example — names
no mechanism.

## Regenerating it

```sh
just departures-ledger
```

The recipe ([`crates/crozier-e2e/departures-ledger.sh`](../../../../crates/crozier-e2e/departures-ledger.sh))
regenerates the inventory in the same pass as the departure ledger: every golden
comparison runs with `CROZIER_RECORD_EXAMPLE_INVENTORY` set and records its
golden's rows instead of checking them, and `write_example_values_inventory`
merges them. Review the diff before committing it; never edit a row by hand.

Outside that recipe every golden comparison holds its golden's rows to what it
finds, as it holds the ledger's, so a stale or missing row fails the comparison
that reads the golden
([`crates/crozier-e2e/tests/e2e/example_values_inventory.rs`](../../../../crates/crozier-e2e/tests/e2e/example_values_inventory.rs)).
A repaired row also fails it unless its mechanism's departure was applied at
that line, which validates crozier's generated value against the source
document.
`the_inventory_holds_to_its_format_and_names_only_compared_goldens` holds the
file to this format.

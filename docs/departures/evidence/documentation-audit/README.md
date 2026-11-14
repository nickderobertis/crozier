# Documentation examples against the generated code

[`documentation-audit.py`](documentation-audit.py) checks every Python example a
generated SDK documents against that SDK's own code. It checks every fenced
`python` block of `README.md` and `reference.md`, and every numpydoc `Examples`
section of a `client.py` docstring. Byte parity cannot show that an example
binds; this audit does. It measures:

| Check | Fails when |
| --- | --- |
| `syntax` | the block does not compile; a repeated keyword is a `SyntaxError` |
| `import` | `from M import N` names a module, or a name, the tree does not define |
| `call` | a call on `client.…`, or a client constructor, passes a keyword the generated method does not take, passes too many positional arguments, or omits a required argument |
| `placeholder` | a `"YOUR_*"` string is passed where the generated annotation admits no `str` |

Whether a value satisfies its declared type and constraints is a separate
check, and it is not this one. That is
[`invalid-example-values/inventory.tsv`](../invalid-example-values/README.md),
which every golden comparison holds. The new pair left it unchanged: it has
9424 rows. Of those, 9235 are repaired. The other 189 keep Fern's bytes:

- 95 are `declared-in-spec`, the document's own example;
- 94 are `residual-unconstructible`.

The `list-path-parameter-example` evidence adds one case that inventory does not
read: a list path parameter documented with a string, which
`pydantic.TypeAdapter` rejects.

## Population

`documentation-audit.py fern` audits every tree that
[`tests/fixtures/compared-goldens.json`](../../../../tests/fixtures/compared-goldens.json)
names. That is 1308 trees, the comparisons the new pair regenerated, with each
overlay rebuilt over its base as the gate rebuilds it. Together they hold 87,701
example blocks. [`fern-findings.tsv`](fern-findings.tsv) lists what it finds in
Fern's output:

| Check | Fern findings | of which in a partial tree |
| --- | ---: | ---: |
| `call` | 805 | 81 |
| `import` | 552 | 107 |
| `placeholder` | 1032 | 0 |
| `syntax` | 158 | 0 |

These findings fall in 351 trees. Nine of those trees are partial snapshots.
They are measurement trees under `docs/fern-measurements/` that keep
`src/fern/` without its `__init__.py`. In them, every import of `fern` and every
client-module lookup fails no matter what the example says. Those 188 rows
measure the snapshot, not Fern. The other 2359 rows are Fern defects, and they
fall in 342 trees.

`documentation-audit.py crozier TREE...` generates crozier's tree for each
named golden, with the settings its comparison uses, and audits it the same
way. It was run over 507 trees: the 351 trees with a Fern finding, joined with
every tree where the departure ledger has crozier write a documentation line
that Fern does not. [`crozier-results.tsv`](crozier-results.tsv) records one
`generated` row per tree, with its block count. A finding would add its own row.
There are none. The pass audited 62,954 blocks.

## What closed the gap

Each Fern defect class the audit found is a `fern-defect` entry of
[`assets/departures.yml`](../../../../assets/departures.yml). Each entry's
evidence note shows Fern's example failing when run against Fern's own code,
and each rule in [`src/departures.rs`](../../../../src/departures.rs) has a unit
test that rejects an unrelated mutation of the same line. These entries were
added or extended for the new pair:

- `readme-environment-constructor-arguments`
- `readme-escaped-method-call`
- `readme-abbreviated-call-arguments`
- `list-path-parameter-example`
- `digit-leading-property-example-keyword`
- `readme-constructor-required-header`
- `non-string-client-header-example`, extended to cover literal and array
  headers

A body property that collides with a query parameter is the repeated-keyword
`syntax` finding. `repeated-query-body-example-keyword` and
`repeated-credential-example-keyword` already cover it.

Fern's 445 undefined imports in full trees are covered by entries that predate
the new pair:

- `empty-namespace-package` covers 414. These are `from fern import FernApi`
  where Fern's package exports nothing.
- `readme-client-class-casing` covers 31. These are a client class name that
  Fern's flat layout does not define.

Every Fern finding in a full tree sits on a line that crozier writes
differently. crozier matches Fern byte for byte everywhere else, so a finding
crozier does not reproduce must sit on one of those departed lines. The crozier
pass shows that what crozier writes there binds.

## Rerunning it

From the repository root, after `cargo build -p crozier --bin crozier`:

```sh
python3 docs/departures/evidence/documentation-audit/documentation-audit.py fern > fern.tsv
python3 docs/departures/evidence/documentation-audit/documentation-audit.py crozier TREE... > crozier.tsv
```

`TREE...` is the tree column of `fern.tsv`, joined with every golden of
`tests/fixtures/departures-ledger.tsv` whose departure writes a documentation
line.

Neither mode gates anything. The script reports findings and changes nothing.
A tree it cannot generate is reported as `unverified`, with the reason.

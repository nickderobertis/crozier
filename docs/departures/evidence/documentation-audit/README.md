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

## The gate

Every whole-tree golden comparison runs the audit over the tree crozier
generated, beside the example-values inventory
([`crates/crozier-e2e/tests/e2e/documentation_audit.rs`](../../../../crates/crozier-e2e/tests/e2e/documentation_audit.rs)).
A finding fails the comparison that reads that golden. Those comparisons are
the goldens [`tests/fixtures/compared-goldens.json`](../../../../tests/fixtures/compared-goldens.json)
names, 1308 trees, so crozier's documentation for each of them binds to the
code beside it. The same file drives each check, and the refusal of a path that is not a
directory.

## Fern's findings

**Historical.** This section and [`fern-findings.tsv`](fern-findings.tsv) were
measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25; "the new pair" in this
note means that one. At the current certified pair, Fern CLI 5.216.0 /
fern-python-sdk 5.42.0, the audit was re-run once over Fern's side of every
golden `compared-goldens.json` names, each overlay rebuilt over the base its
`cases.tsv` row or sibling tree gives. Of this record's rows, 2,335 recur
unchanged and 24 recur ten lines earlier (README rows after the Retries
section, which 5.42.0 states in ten fewer lines); the other 188 are the nine
partial snapshots' rows described below, which a tree rebuilt over its base
does not have. No other finding appeared in those trees. Six trees registered
since carry 13 more, all `call`. The file was not rewritten, so its rows and
line numbers are 5.41.25's. The gate above, over crozier's own output for
every compared golden, is what holds the current trees.

[`fern-findings.tsv`](fern-findings.tsv) is the audit of Fern's side of the
same 1308 trees, each overlay rebuilt over its base as the comparison rebuilds
it. Together they hold 87,701 example blocks.

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

crozier departs from Fern on every one of those lines; the gate shows that what
it writes there binds.

## Rerunning it

```sh
python3 docs/departures/evidence/documentation-audit/documentation-audit.py TREE...
```

It prints one row per finding: tree, file, line, check, detail. A summary of
trees, blocks and findings goes to stderr. It exits 0 when there is no finding,
1 when there are findings, and 2 when a TREE is not a directory. For a complete
tree of `compared-goldens.json`, it reproduces that tree's rows of
`fern-findings.tsv`. An overlay is audited once it has been rebuilt: copy its
base, delete what its `.crozier-overlay.json` removes, then lay the overlay's
files over the copy.

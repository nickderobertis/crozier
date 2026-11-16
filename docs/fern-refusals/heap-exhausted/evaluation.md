# heap-exhausted: refuse

## At Fern CLI 5.200.0 / fern-python-sdk 5.41.25: not compared

**Not compared at the certified pair; no refusal is certified here.** The class
does not count toward the certified pair, and everything under the 5.163.1
heading below is history at that pair.

- **Probe: unsettled.** The Fern goldens run 43423270787 and one serial bounded
  rerun (`fern-refusals.py probe heap-exhausted --jobs 1 --timeout 900`, with
  `NODE_OPTIONS=--max-old-space-size=16384`, node v26.8.2, a 94 GiB host with no
  cgroup memory limit, load average about 63 on 20 CPUs) each ran `fern check`
  to its 900-second bound (897.7 s) and `fern generate` to its bound (898.8 s),
  printing nothing. A run cut short says nothing about whether Fern refuses
  given more time or memory, so [`fern-refusal.txt`](fern-refusal.txt) stays
  the 5.163.1 / 5.41.3 record. [`unsettled.txt`](unsettled.txt) records the
  timings and the reason, and the registry's checks
  (`fern-refusals.py check`, `crozier-e2e::fern_refusal_classes_hold`) accept
  the older record only beside it.
- **Shapes: not retaken.** The 2 probe and 5 control shapes keep their 5.163.1
  logs.
- **Real documents: corroboration only.** `confirm` retook both
  [`confirmations.tsv`](../../openapi-surface/fern-refusals/confirmations.tsv)
  rows at this pair (jakemannix `0117d8bf…` and Wiremock `94e583d7…`): each
  generation exits 1 with `FATAL ERROR: Ineffective mark-compacts near heap limit
  … JavaScript heap out of memory`. That is two real documents, not the probe,
  and does not settle the class.
- **crozier's behaviour is unchanged**: it refuses the probe in both modes, as
  the e2e gate still checks.
- **Follow-up:** *Settle crozier's heap-exhausted refusal class at Fern CLI
  5.200.0 / fern-python-sdk 5.41.25* (drafted by the `upstream-evidence` node;
  whether to spend the long one-at-a-time re-measure is an open question).

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. Its 2 probe and 5 control shapes are measured at this pair too ([`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv)): a `-probe` is a shape Fern refuses, a `-control` one it generates from, and each `evaluation-logs/fern-<shape>.log` holds that measurement. The population carries the class on 2 documents at this pair, as at Fern CLI 5.67.1. crozier's release build refuses both under `--fern-strict` ([`documents.tsv`](../documents.tsv)).

What moved: A union recursing through a component's `$defs` is followed as a schema of its own and generates (`defs-json-value` control; AgenticDriver's `$defs/__schema0`), and crozier no longer refuses it. `single-child` and `recursive-union-allof` are probes: Fern refuses them, through `generated-file-name-too-long`, as this evaluation records. A cycle that grows by one reference a turn is refused by Fern through `generated-file-name-too-long` (the `single-child` and `recursive-union-allof` probes; Kibana's zod schema reduced to itself), and crozier now names that class for it; two or more growing references stay `heap-exhausted`. A single referenced `allOf` member with no fields of its own is an alias, not an extension, so it grows nothing (`nullable-union-alias` control; Helicone's nullable `CustomerSource`). The check is decided once per document over the reference graph's strongly connected components.

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's.

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair.
Measurements use CPython 3.12.3, mypy 1.13.0 and each generated
`pyproject.toml` with its declared dependencies.

The [probe package and client import](evaluation-logs/probe.log), and mypy
reports zero errors. Its [public client journey](evaluation-logs/probe.wire.log)
sends the declared bodyless `GET /tools` and parses nested `composition`,
`child0` and `child1` response fields without renaming or losing any field.
The partial Schema Object reference returns to the containing inline union.

Both retrievable population documents have been evaluated, from different publishers:

- [jakemannix's virtual-tools document, `0117d8bf597b8d795a9db545faded552db868006d48f398a12f07563506a3693`](evaluation-logs/virtual-tools.log)
  imports its package and client but reports **40 mypy errors**. Its recursive
  `ToolDefinition.implementation` contains inline composition unions whose
  pipeline operations and scatter/gather targets return by partial references.
  The [public client journey](evaluation-logs/virtual-tools.wire.log) sends the
  declared bodyless `GET /tools/nested` and parses a recursive nested pipeline
  with its original `steps`, `operation`, `composition` and `tool` fields.
- [Wiremock's admin document, `94e583d7f5868949fe8bfd835e902928733f9d05fc5983c7fcf86298c93ee1ee`](evaluation-logs/wiremock.log)
  imports its package and client but reports **26 mypy errors in five files**.
  Its `content-pattern` union returns through `matches-json-path-pattern` and
  `matches-xpath-pattern` inline object branches that extend that same union.
  The [public client journey](evaluation-logs/wiremock.wire.log) sends
  `POST /__admin/mappings` with `bodyPatterns`, `matchesJsonPath`, `expression`,
  `and`, `equalTo` and `contains` preserved, then parses the declared response
  and reserializes the same fields exactly.

Correct measured wire does not rescue packages that fail their own type checks.
The population failures make the class **refuse** in both modes.

Pinned measurements preserve [ordinary named object recursion](evaluation-logs/fern-named-object-recursion.log),
[named binary recursion](evaluation-logs/fern-named-binary-recursion.log), and
[a nonrecursive inline union](evaluation-logs/fern-nonrecursive-union.log).
They distinguish recursion that expands an inline declaration: with
[one partial-reference child](evaluation-logs/fern-single-child.log), or with
[recursive inline union inheritance](evaluation-logs/fern-recursive-union-allof.log),
check passes but generation fails with an unbounded filename. The population
checks exhaust the heap; these reduced examples expose the same unbounded
inline expansion with a different resource failure. The detector follows
schema edges and refuses a union cycle containing a partial Schema Object
reference or inheritance from a union. Ordinary named recursion remains allowed.
The CLI journey preserves accepted output bytes between modes and exercises
both ignore-extension spellings at the recursive union.

The [population refusal log](evaluation-logs/population-refusals.jsonl) covers
both retrievable documents in both modes: exit 1, no files, one line naming
`heap-exhausted` and the offending schema, with `fern-strict` as the strict cause.

The [CLI refusal assertion fails with only this predicate disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 44 files from the probe instead of refusing. This log records an induced
earlier state; the finished detector restores the predicate.

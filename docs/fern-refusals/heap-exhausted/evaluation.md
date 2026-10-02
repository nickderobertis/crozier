# heap-exhausted: refuse

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

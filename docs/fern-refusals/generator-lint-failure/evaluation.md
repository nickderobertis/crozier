# generator-lint-failure: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was made
to qualify this class. Checks use CPython 3.12.3, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe output](evaluation-logs/probe.log) imports its package and client
but reports **3 mypy errors in 2 files**: `Event_UserAccountDeleted` is defined
twice (`no-redef`), because the discriminant values `user:account_deleted` and
`user_account:deleted` both name that wrapper class. The [public client
journey](evaluation-logs/probe.wire.log) sends the declared bodyless
`GET /events` both times. It parses `user_account:deleted`, but the declared
`user:account_deleted` variant has no surviving class: its response fails with
`ParsingError`. Losing a declared variant disqualifies the class.

Three population representatives, from different publishers:

- [codesearch.debian.net (APIs.guru), `266d68e1…`](evaluation-logs/population-266d68e1.log)
  imports but reports **6 mypy errors in 3 files**, among them the root
  client's `search` method redefined by the `search` sub-client property.
- [queryhat's super-hat, `56435877…`](evaluation-logs/population-56435877.log)
  imports but reports **122 mypy errors in 9 files**, among them `chat` defined
  twice on the root client the same way.
- [Helicone's AI gateway, `921a3ac6…`](evaluation-logs/population-921a3ac6.log)
  imports and reports **zero mypy errors**. Its null-only enum branches are
  rendered as plain optional strings, so this document generates where Fern's
  enum class cannot parse. That does not rescue the probe's lost variant under
  the class-wide conjunction rule.

The class is `refuse` in both modes. Fern's own `ruff check` over its output
fails for several distinct shapes. The detector refuses each shape that a
pinned Fern generate failure backs, and it reads that shape from crozier's
IR, which names those elements as Fern does:

| Shape | Fern's ruff failure | Probe | Accepted near-miss |
|---|---|---|---|
| two discriminant values naming one union wrapper class | [F811](evaluation-logs/fern-discriminant-collision.log) | [probe](probe.yml) | [distinct names](distinct-discriminants-control.yml) ([log](evaluation-logs/fern-distinct-discriminants.log)) |
| a root-client method and a sub-client of one name | [F811](evaluation-logs/fern-root-collision.log) | [probe](root-collision-probe.yml) | [one tagged operation](single-root-method-control.yml) ([log](evaluation-logs/fern-single-root-method.log)) |
| an operationId repeating its tag, beside another operation of that tag | [F811](evaluation-logs/fern-tag-suffix-collision.log) | [probe](tag-suffix-collision-probe.yml) | — (see below) |
| a method named from a summary with no ASCII word | [syntax error](evaluation-logs/fern-untitled-summary.log) | [probe](untitled-summary-probe.yml) | [ASCII summary](ascii-summary-control.yml) ([log](evaluation-logs/fern-ascii-summary.log)) |
| a default-server variable that is no Python keyword argument | [hyphen](evaluation-logs/fern-server-hyphen.log), [dot](evaluation-logs/fern-server-dot.log), [keyword](evaluation-logs/fern-server-keyword.log) | [hyphen](server-hyphen-probe.yml), [dot](server-dot-probe.yml), [keyword](server-keyword-probe.yml) | [identifier](server-identifier-control.yml) ([log](evaluation-logs/fern-server-identifier.log)); [hyphen on a non-default server](server-secondary-hyphen-control.yml) ([log](evaluation-logs/fern-server-secondary-hyphen.log)) |
| a default-server placeholder with no declared variable, beside one that has a variable | [F524](evaluation-logs/fern-server-unbound-placeholder.log) | [probe](server-unbound-placeholder-probe.yml) | [placeholder with no variables at all](server-placeholder-without-variables-control.yml) ([log](evaluation-logs/fern-server-placeholder-without-variables.log)) |
| a model property whose Python name is empty (`/`) | [syntax error](evaluation-logs/fern-slash-property.log) | [probe](slash-property-probe.yml) | [`/data`](slash-prefixed-property-control.yml) ([log](evaluation-logs/fern-slash-prefixed-property.log)) |
| a `type: string` enum with no non-null value | [empty](evaluation-logs/fern-empty-enum.log), [nullable null](evaluation-logs/fern-null-only-enum.log), [null](evaluation-logs/fern-null-enum-not-nullable.log), [inline union branch](evaluation-logs/fern-inline-null-only-enum.log) | [empty](empty-enum-probe.yml), [nullable](null-only-enum-probe.yml), [null](null-enum-not-nullable-probe.yml), [inline](inline-null-only-enum-probe.yml) | [null beside a value](null-and-value-enum-control.yml) ([log](evaluation-logs/fern-null-and-value-enum.log)) |

When the operationId only repeats its tag (`Search_` under `Search`), Fern
hoists the method to the root. That collides only when the tag keeps another
operation. Alone, as in [this document](evaluation-logs/tag-suffix-single.yml), Fern
[generates](evaluation-logs/fern-tag-suffix-single.log). crozier named that
method empty and failed its own `ruff format` there from the baseline until the
authored probe `376-357-tag-only-operation-id` committed Fern's tree for it. It now
writes the root `search` method and byte-matches that tree in both modes. The
detector does not refuse that single-operation shape. Beside another operation
of the tag, the [probe](tag-suffix-collision-probe.yml) and BBC (`eeab4173…`)
are still refused in both modes, now as `GET /search root method and sub-client
search`: the collision Fern's F811 on `search` names in
[the probe's log](evaluation-logs/fern-tag-suffix-collision.log) and BBC's. The
population log below predates that and records `method name is empty` for BBC.

Per the planner's ruling, operation naming is read as pinned Fern reads it:
`x-crozier-sdk-group-name` and `x-crozier-sdk-method-name` are set aside while
the detector's IR is built, then restored before emission. A
[canonical group override](canonical-group-name-control.yml) puts an operation
in a `search` sub-client beside a root `search` method. Fern
[generates from it](evaluation-logs/fern-canonical-group-name.log), so crozier does
too. Every accepted control generates identical bytes in both crozier modes.

The [CLI assertion failed with only the union predicate
disabled](evaluation-logs/refusal-e2e-induced-red.log), writing 40 files; the
predicate was then restored. [All eleven population
documents](evaluation-logs/population-refusals.jsonl), measured with the
finished detector, are refused in both modes: exit 1, no files, and one stderr
line with the strict cause when it applies. Ten are refused by this class,
covering every measured shape but the union collision. `875e6bce…` (OSRD) is
refused first by `object-extends-non-object`; its own failure is the union F811.

## Global-header constructor-name cases

Fresh independently authored [punctuation-only](global-header-punctuation-name-probe.yml)
and [empty](global-header-empty-name-probe.yml) names were measured with CLI
5.67.1 and Python SDK 5.20.0, packaged preview, package `fern`, client `FernApi`,
Python enums, extra fields `allow`, retries 2, and no audience filtering. Both
`fern check` runs exit 0; both generation runs exit 1 with no SDK tree because
`ruff check` rejects an empty constructor argument identifier. The certified
[punctuation check](evaluation-logs/global-header-punctuation-name.check.log),
[punctuation generation](evaluation-logs/global-header-punctuation-name.generate.log),
[empty check](evaluation-logs/global-header-empty-name.check.log), and
[empty generation](evaluation-logs/global-header-empty-name.generate.log) record
the failures. This extends the existing `generator-lint-failure` mechanism; its
status and historical evaluation remain unchanged. These name-only faults
refuse in both modes, naming the declared header and constructor name. They
are never generated under repaired names. The independently authored Warehouse
Ledger complete golden remains the adjacent valid constructor-name control,
including the canonical alias and conflicting values.

## Idempotency-argument cases

Fresh independently authored probes give an idempotent operation an
idempotency header whose argument the method cannot take: an
[empty name](idempotency-header-empty-name-probe.yml) (header `-`), a name
[repeating a query parameter](idempotency-header-parameter-collision-probe.yml),
and [two headers](idempotency-header-shared-name-probe.yml) stemming to one
name once `X-` is stripped. Each was measured with CLI 5.67.1 and Python SDK
5.20.0 through `tools/fern-goldens/generate-fern-fixture.sh` with its default
settings (packaged preview, package `fern`, client `FernApi`, Python enums).
Fern's own checks pass; each generation exits 1 with no SDK tree because
`ruff check` rejects the signature: a missing argument name for the
[empty name](evaluation-logs/idempotency-header-empty-name.generate.log), and
`Duplicate keyword argument "firing_token"` for the
[query collision](evaluation-logs/idempotency-header-parameter-collision.generate.log)
and the [shared name](evaluation-logs/idempotency-header-shared-name.generate.log).
These are name-only faults: crozier refuses all three in both modes, naming
the operation, the header and the argument, and never renames one. The
`x-crozier-idempotency-headers` spelling refuses the same way and wins over a
conflicting `x-fern-*` list. The independently authored Parcel Courier Desk
complete golden remains the adjacent valid idempotency control.

# Quoted scalar continued at its key's column

**Verdict: `parity-gap-repaired`.** The certified pair (Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3) generates from a document whose multi-line
quoted scalar continues at its key's own column, or shallower. YAML reserves
that column for the next key. crozier's parser (serde-saphyr over
granit-parser) refused the document with `invalid indentation in multiline
quoted scalar`. crozier now reads it as Fern's reader does, and its SDK for
this document byte-matches `fern-expected/`.

## Root cause and repair

Fern's YAML reader puts no indentation floor on a quoted scalar's
continuation lines. It folds a line at the key's column exactly as it folds a
deeper one, and a continuation line's leading white space is never part of the
value. granit-parser applies YAML's floor: a continuation must sit deeper than
the block collection that holds the scalar.

The repair lives in crozier's loading code, `src/yaml.rs`, and the third-party
parser is unchanged. `from_str` parses strictly first. Only when that parse
fails does `reindented` run. It asks the parser for its first
`invalid indentation in multiline quoted scalar` refusal, finds that scalar's
opening quote (`underindented_scalar`, `opening_quote`), and indents each of
the scalar's shallower continuation lines to the quote's column
(`pad_continuations`). It repeats this until no such refusal is left, then
parses the repaired text.

- **Valid documents are unaffected.** A document that already parses never
  reaches the repair.
- **Only leading white space is added.** The padding adds white space only at
  the start of a continuation line, which no reader includes in the value, so
  the repaired text reads the values Fern reads.
- **Some lines are left alone.** These are a line opening with a document
  marker (`---` or `...`) at column 0, a blank line, and a line that is only
  the closing quote. Every other refusal is also left for the parser to report.

`src/document_refusals/examples.rs`'s `plain_timestamps` reads the parser's
events over the repaired text when the original stops at an error. Without
that, it would lose every plain timestamp after the first repaired scalar.

## This measurement

`openapi.yml` was written from scratch for this measurement. It holds:

- a summary and a schema description continued at the key's column;
- a description continued shallower than its key;
- an escaped line break and a blank line inside a double-quoted scalar;
- a single-quoted parameter description with an `''` escape and a `#`;
- a block-sequence enum whose values continue at the dash's column.

`fern-expected/` is the complete, comment-stripped tree the certified pair
generated from it under `python_enums`, produced by
`just fern-references measurements refusal-parity/quoted-continuation-at-key-column`
(the `cases.tsv` row). It has 41 files, and its Contract A tree digest is
`0e5d606748e9573310ce24622e2a98efa90a143a1956a8c07537d9995b82f3d9`.

Each `*.openapi.yml` beside it is malformed in a way Fern's reader refuses too.
Its `*.fern.log` holds the certified pair's refusal, `check exit: 1` and
`generate exit: 1`:

| Document | Fern's reader | crozier |
|---|---|---|
| `unclosed-quote` | `unexpected end of the stream within a double quoted scalar` | refused at the parser |
| `document-marker` | `unexpected end of the document within a double quoted scalar` | refused at the parser |
| `trailing-content` | `a multiline key may not be an implicit key` | refused at the parser |

`crates/crozier-e2e/tests/e2e/refusal_parity.rs` drives all of this through the
binary:

- the SDK byte-matches the tree, apart from the five `sdk-identity-header-prefix`
  lines the departures ledger records;
- each malformed neighbour is refused and writes nothing;
- valid multi-line scalars read as they always have.

Every Fern run was serial and held
`${XDG_CACHE_HOME:-$HOME/.cache}/crozier/fern-generation.lock` for its whole
duration.

## The documents

### ingef/conquery `openapi.yaml`

- **Source:** `0379408a4b681575daf311d37bd12ff08ccc409d`, sha256
  `c3a52b3c5453c003a563a9b39784dfcd9f89f69e0ae1848dbec2881a24b9ec21`, from
  `https://raw.githubusercontent.com/ingef/conquery/0379408a4b681575daf311d37bd12ff08ccc409d/openapi.yaml`.
- **Licence:** MIT, from the repository's LICENSE. The document's own
  `info.license` is a `TODO` placeholder.
- **Outcome:** not excepted, repaired, and still not byte-matching.

Two crozier refusals stood between this document and an SDK.

1. **This node's YAML cause.** Its descriptions continue at their key's column
   (line 172 first), and the repair above reads them.
2. **A null-only discriminant.** `NullOutput.operation` is `type: string,
   enum: [ NULL ]`, and YAML's `NULL` is null. It is the `operation`
   discriminant of the `OutputDescription` union. `generator-lint-failure`
   refused it as an enum with no non-null value. The certified pair drops a
   variant's discriminant property, so it writes no such enum class. The rule
   in `src/document_refusals.rs` now skips the inline property nodes crozier's
   model strips as a variant's discriminant (`variant_discriminants`, reading
   `ir::document_discriminant_strips`). The same enum *beside* the
   discriminant stays refused. Both shapes are registry shapes measured at the
   pair:
   - `docs/fern-refusals/generator-lint-failure/null-only-discriminant-control.yml`
     (the tag in an inline `allOf` member) generates;
   - `null-only-direct-discriminant-control.yml` (the tag in the variant's own
     `properties`) generates;
   - `null-only-beside-discriminant-probe.yml` is refused.

With both repaired, crozier generates 238 files. The certified pair wrote 239
from the same bytes, measured here under the lock.

`crozier compare` checked that output against the pair's comment-stripped
tree:

- 239 files compared;
- 229 match, apart from five `sdk-identity-header-prefix` lines
  (`src/fern/core/client_wrapper.py` lines 38–42);
- 9 differ;
- 1 is only in Fern's tree.

This was re-measured on the finished tree (`bbf7a405b`). The pair's tree came
from `tools/fern-goldens/generate-fern-fixture.sh` (packaged, `python_enums`),
which ran from 2026-10-27T09:49:28Z to 09:50:07Z holding
`${XDG_CACHE_HOME:-$HOME/.cache}/crozier/fern-generation.lock`. It wrote 239
files, identical to the first measurement's. `crozier compare` ran with
`package-name: fern` and `project-name: default_package_name`, the names the
pair's preview uses, and gave the same counts and files listed above.

Each of those ten files is accounted for by one of two generator causes this
node does not own.

**Cause A: a discriminator mapping target naming no schema.** `Query` maps
`SECONDARY_ID_QUERY` to `#/components/schemas/secondary-Id-query`, but the
component is `SecondaryIdQuery`. Fern still writes a discriminated union of
`Query_*` wrappers. It keeps `SecondaryIdQuery.type` and hoists
`SecondaryIdQueryType`. crozier writes an undiscriminated `typing.Union`.
Correcting only that target in a copy makes crozier write the `Query_*`
wrappers. The files:

- `reference.md`
- `src/fern/__init__.py`
- `src/fern/types/__init__.py`
- `src/fern/query/client.py`
- `src/fern/types/query.py`
- `src/fern/types/secondary_id_query.py`
- `src/fern/types/secondary_id_query_type.py` (only in Fern's tree)

The two `__init__.py` files also split a union's alias from its wrappers'
import. Sorted with ruff's isort, the `TYPE_CHECKING` blocks differ by cause
A's lines alone, which is `init-type-checking-import-order`'s ordering.

**Cause B: fields inherited through an `allOf`-only base.** Each `Filter`,
`Select` and `UniversalSelect` variant is `allOf: [$ref FilterBase, {…}]`.
`FilterBase` is itself `allOf: [$ref Labeled, {properties}]`. Fern's
`Filter_*` wrappers carry the variant's fields, `FilterBase`'s and
`Labeled`'s. crozier's carry only the variant's own. A from-scratch,
crozier-only reduction shows it: one variant level over a base that is itself
an `allOf` drops every inherited field, while a base with direct `properties`
keeps them. The files:

- `src/fern/types/filter.py`
- `src/fern/types/select.py`
- `src/fern/types/universal_select.py`

The document is not registered as a corpus golden. Its licence admits it, but
it does not byte-match until causes A and B are repaired. Both are drafted as
follow-ups.

## Scope ruling

The manager of this run ruled on the node's scope twice, over the planner
channel, each reply amending the node's acceptance criteria. An amendment
clause takes precedence over any criterion it contradicts.

**Reply 35** (correlation `c-d065d7b4f1a27d3fc79e84fbd8f2ce39`) brought the
null-only-discriminant refusal into scope. It said:

> Then take conquery as far as it goes: register it as a golden if it
> byte-matches and its licence allows, otherwise record its measured residual
> by cause.

**Reply 36** (correlation `c-775c7fadb2321550a66bdbf172a0b87b`) answered how
to prove the lexical YAML shape, given that the hand-written fixture gate
requires a census-region cover no lexical shape has. It said:

> Option (c) […]: prove the YAML shape with a from-scratch document and its
> certified-pair tree, byte-compared by a dedicated e2e test in
> crates/crozier-e2e through the parity engine, plus the probe/control pair
> for the discriminant narrowing. Do not commit a fixture under
> docs/openapi-surface/handwritten/ with a cover that misstates coverage, and
> do not change the fixture contract or gate in this node. Do not register
> conquery. Record its two remaining causes […] as measured residuals in your
> report, and draft each as a follow-up with ORCHESTRATOR_FOLLOW_UP_DRAFT.

Its amendment added these clauses to the node's criteria:

> - For the lexical YAML shape this node repairs, the hand-written fixture
>   criterion is met by a from-scratch document of the triggering shape whose
>   crozier output is byte-compared with its certified-pair tree by an e2e
>   test in crates/crozier-e2e, apart from lines the departures ledger records
>   under an authorized departure. No handwritten_fixtures_match_fern_goldens
>   cover is required for that shape.
> - Where ingef/conquery still differs from the certified pair after this
>   node's repairs, the report records each remaining difference by cause with
>   its measured evidence, and each cause is drafted as a follow-up.

So causes A and B are recorded and drafted here, not repaired, and conquery
is not registered.

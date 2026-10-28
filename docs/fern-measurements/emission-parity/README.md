# Emission parity: ingef/conquery's two union causes

crozier generated from ingef/conquery's `openapi.yaml` once its YAML and
null-only-discriminant refusals were repaired
([`quoted-continuation-at-key-column`](../refusal-parity/quoted-continuation-at-key-column/README.md)).
Its SDK still differed from the certified pair's (Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3) in ten files, through two causes. This
record names each cause, the crozier code each repair changed, and conquery's
outcome. Each cause also has a from-scratch document in this directory, with
its certified-pair tree in both enum modes.

## A: a discriminator mapping target that names no schema

conquery's `Query` is a `oneOf` of seven `$ref`s discriminated by `type`. Its
mapping sends `SECONDARY_ID_QUERY` to `#/components/schemas/secondary-Id-query`,
but the component is `SecondaryIdQuery`. The mapping's other six targets name
their components.

**What Fern writes.** The certified pair writes the discriminated union of
`Query_*` wrappers, one per mapping value. It keeps `SecondaryIdQuery`'s own
`type` property and hoists its enum, `SecondaryIdQueryType`. Its
`Query_SecondaryIdQuery` holds `value: typing.Any` beside the tag, not the
member's fields. Fern warns at generation that the member "will be omitted from
the generated union, so payloads using it will fail to serialize or
deserialize".

**What crozier wrote.** crozier read the dangling target as no union at all and
wrote `Query = typing.Union[ConceptQuery, …]`. It stripped `SecondaryIdQuery.type`,
and its examples constructed `ConceptQuery()`.

**The ruling.** Fern's `value: typing.Any` wrapper was shown failing through
the real client, against a local HTTP server. `get_query_status` answered with a
`SECONDARY_ID_QUERY` query raised `ParsingError` (`query.SECONDARY_ID_QUERY.value
Field required`). The only `Query_SecondaryIdQuery` Fern's types can build sends
`{"type": "SECONDARY_ID_QUERY", "value": {…}}`. The manager ruled (reply 40,
correlation `c-51e67196fe481507738163e14e450baa`), superseding the earlier ruling
to copy the certified pair. crozier writes Fern's union, and every line of the
affected files is Fern's, except `Query_SecondaryIdQuery`. That wrapper carries
`SecondaryIdQuery`'s fields, and its lines, with the imports and the
`update_forward_refs` call they need, are the catalogued departure
[`dangling-mapping-variant-fields`](../../departures/evidence/dangling-mapping-variant-fields.md).

**The repair.**

- `src/ir.rs`, `Builder::discriminated_union`: a mapping target naming no
  component no longer ends the union. Its wrapper carries the fields of the
  `oneOf` member that no mapping target names and that tags itself with the
  value (`dangling_target_member`). Where no member does, it holds Fern's
  `value: typing.Any`.
- `reads_dangling_targets` limits this to the measured shape: every member
  resolves, and some target names a component. A mapping whose targets all
  dangle keeps the `value` wrappers it already had. A single dangling target
  with no resolving one, or a member that is itself a `$ref` to nothing, keeps
  crozier's undiscriminated union, as before.
- `collect_discriminant_strips` strips nothing for a target naming no
  component in that same shape, so the member keeps its tag, as Fern's does.
  Outside it, the strip reads the target as it always did.
- `UnionMember::declared_discriminant` (`DeclaredDiscriminant`,
  `member_declared_discriminant`) records whether the variant requires its own
  tag. With the union discriminated, conquery's examples construct
  `Query_ConceptQuery`, and `ConceptQuery` declares an optional `type`. Fern's
  client docstring passes it, and its `reference.md` leaves it out. `src/emit.rs`
  now has the Markdown writers pass a variant's own tag only where it is
  required. The observatory measurement shows the same split independently.
- `src/departures.rs`, `dangling_mapping_variant_fields` (with
  `any_valued_wrapper` and `drop_unused_imports`), is the departure's rule. It
  reads the wrappers off the source document (`ir::dangling_mapping_wrappers`)
  and accounts for a module only when rewriting them Fern's way yields Fern's
  file exactly. The entry is in `assets/departures.yml`.

## B: fields inherited through an `allOf`-only base

Each `Filter`, `Select` and `UniversalSelect` variant is `allOf: [$ref
FilterBase | SelectBase | SelectFilterBase, {…}]`. `FilterBase` is itself
`allOf: [$ref Labeled, {unit, tooltip, …}]`, and `SelectFilterBase` composes
`FilterBase`, `Searchable`, its own `column` and an inline `oneOf` of `labels`
and `template`. Fern's wrappers carry the variant's own fields, then the
base's inline members' fields, then the base's own bases' fields. crozier
walked only a base's direct `properties`, so `Filter_DateDistance` lacked
`unit` … `default_value`, `name` and `label`. This is a crozier defect the
certified pair does not share.

The same three files showed a second gap: an inline `allOf` member that is an
undiscriminated `oneOf` lends its branches' properties, optional, to the
wrapper. `CountFilter` composes `oneOf: [{column}, {distinctByColumn}]`, and
Fern's `Filter_Count` carries both after `distinct`. crozier's standalone model
already did this, and its wrapper did not.

**The repair.** In `src/ir.rs`:

- `member_fields` hands a variant's `$ref` bases to `append_base_fields`. That
  function walks each base in `member_fields`' own order, recursing into the
  base's own bases, with a path guard against a chain that reaches back.
- `append_inline_member_fields` reads an inline member through
  `branch_union_properties`, which `Builder::add_object` now shares.
- `member_discriminant_index` scans the same order through nested bases.

A variant over a base with direct `properties` gets exactly the fields it did
before.

## The from-scratch documents

Both documents were written for this record. Their trees were generated by
`just fern-references measurements emission-parity/<case>` (rows in
[`../cases.tsv`](../cases.tsv)), under
`${XDG_CACHE_HOME:-$HOME/.cache}/crozier/fern-generation.lock`, from
2026-10-27T20:57:02Z to 20:58:35Z.

| case | shape beside its control | mode | files | crozier |
|---|---|---|---|---|
| [`allof-only-base`](allof-only-base/evidence.md) | B; `Humidity` over a plain base | python-enums | 47 | byte-matches, apart from `sdk-identity-header-prefix` |
| [`allof-only-base-literals`](allof-only-base-literals/evidence.md) | the same | literals | 46 | byte-matches, apart from `sdk-identity-header-prefix` and `fern-metadata-generator-config` |
| [`dangling-mapping-target`](dangling-mapping-target/evidence.md) | A; `Instrument`, every target resolving | python-enums | 48 | byte-matches, apart from `sdk-identity-header-prefix` and `dangling-mapping-variant-fields` in `types/reading.py` |
| [`dangling-mapping-target-literals`](dangling-mapping-target-literals/evidence.md) | the same | literals | 47 | byte-matches, apart from those and `fern-metadata-generator-config` |

`crates/crozier-e2e/tests/e2e/emission_parity.rs` holds each tree whole
through the parity engine and the departures ledger. Each test then induces a
change the comparison must refuse. Its `sdk_env_*` journey runs
[`dangling_mapping_wire.py`](../../../crates/crozier-e2e/tests/e2e/dangling_mapping_wire.py)
over crozier's SDK in both modes, and over the certified tree, which fails at
the `METEOR` read. The unit tests beside each repair are in `src/ir.rs`
(`variant_wrappers_inherit_fields_through_an_all_of_only_base`,
`branch_union_properties_lends_only_an_undiscriminated_members_branches`,
`a_mapping_target_naming_no_schema_carries_its_tagged_members_fields`,
`a_dangling_mapping_reads_as_before_unless_its_members_resolve_beside_a_named_target`,
`dangling_mapping_wrappers_names_only_wrappers_a_member_fills`), `src/emit.rs`
(`markdown_examples_pass_a_variants_own_tag_only_where_it_is_required`) and
`src/departures.rs`
(`dangling_mapping_variant_fields_holds_on_the_wrapper_and_nowhere_else`).

## conquery's outcome

conquery is registered as corpus row 3477, `ingef-conquery`
([`CORPUS.md`](../../../tests/fixtures/CORPUS.md)). Its row records:

- the source bytes, vendored at sha256
  `c3a52b3c5453c003a563a9b39784dfcd9f89f69e0ae1848dbec2881a24b9ec21`, from
  revision `0379408a4b681575daf311d37bd12ff08ccc409d`;
- the MIT grant of the repository's LICENSE at that revision (the document's
  own `info.license` is a placeholder);
- its `NOTICE` entry.

Its golden was generated by Route A, `just fern-goldens-generate --version
5.41.3 --fixture ingef-conquery` at CLI 5.163.1, and then its literals overlay,
which `just fern-references overlays ingef-conquery/expected-literals`
regenerates. Both ran in one hold of the lock, from 2026-10-27T21:23:58Z to
21:24:45Z. The 239-file tree is
byte-identical to the one the earlier node measured.

**The comparison.** crozier generated from the exact document on the finished
tree and was compared through `crozier compare` with the committed golden
(python-enums) and the certified pair's complete literals tree, measured with
the same bytes and pair:

| mode | files compared | differing | departures applied |
|---|---|---|---|
| python-enums | 239 | 0 | five `sdk-identity-header-prefix` lines; `init-type-checking-import-order` at `types/__init__.py:73`; `dangling-mapping-variant-fields` at `types/query.py:1` |
| literals | 238 | 0 | the same, and `fern-metadata-generator-config` at `.fern/metadata.json:5` |

Both report `matched`. The corpus gate holds the same result:
`ingef_conquery_matches_fern_output` compares the golden, and
`overlay_goldens_match_fern_output` compares its `expected-literals` overlay.
Both hold every departure to its row in
[`departures-ledger.tsv`](../../../tests/fixtures/departures-ledger.tsv).
That ledger is regenerated by `just departures-ledger` over every golden
comparison (see the derived records below). It added rows only for the new goldens, so no other
golden's output moved.

**At runtime.** `sdk_env_conquery_secondary_id_query_round_trips_through_the_client`
drives the client crozier generates from the registered document against a
local HTTP server, through
[`conquery_secondary_id_wire.py`](../../../crates/crozier-e2e/tests/e2e/conquery_secondary_id_wire.py).
In both enum modes, a `SECONDARY_ID_QUERY` status parses into
`Query_SecondaryIdQuery` with `SecondaryIdQuery`'s `secondary_id` and
`date_aggregation_mode`. Posting it back sends the server exactly the payload it
answered. The certified golden's client raises `ParsingError` on the same
response, at `query.SECONDARY_ID_QUERY.value`. The departure's
[evidence note](../../departures/evidence/dangling-mapping-variant-fields.md#the-same-failure-on-conquerys-registered-document)
records each run's output.

## Derived records

The branch's final `src/` is that of `3e92ba290`. It is unchanged through the
merge of main at `275e9d3da` (`cc2dd11da`) and every later commit. Each derived
record was generated from that source:

| record | generated by | at |
|---|---|---|
| [`departures-ledger.tsv`](../../../tests/fixtures/departures-ledger.tsv) and the invalid-example inventory | `just departures-ledger`, every golden comparison passing | `cc2dd11da`; the committed rows were already current |
| [`golden-reach.tsv`](../../openapi-surface/golden-reach.tsv) and the region files' reach cells | `just golden-reach`'s steps: the source check, the measurement over 275 golden tests, the census and the report | `cc2dd11da`, which the ledger's header names |
| the census JSON (`.local/golden-reach/census.json`, not committed) and the [`document-paths`](../../openapi-surface/document-paths.md) snapshot, its digest and stated counts | `just surface-census --json`, then `restate-coverage.py --snapshot-json` | `cc2dd11da`; the check passes at `c309d2ebe` |
| the coverage restatements in [`openapi-surface-coverage.md`](../../openapi-surface-coverage.md) | `restate-coverage.py --write`; the reach ranking's counts restated from the `cc2dd11da` reach ledger | the check passes at `c309d2ebe` |
| [`handwritten-reach.tsv`](../../openapi-surface/handwritten-reach.tsv) | `just handwritten-reach` | `c309d2ebe`; the committed file was already current |

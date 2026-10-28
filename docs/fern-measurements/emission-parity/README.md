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
  `member_declared_discriminant`) records whether the Markdown writers pass the
  variant's own tag back. With the union discriminated, conquery's examples
  construct `Query_ConceptQuery`, and `ConceptQuery` declares an optional
  `type`. Fern's client docstring passes it, and its `reference.md` leaves it
  out. The observatory measurement shows the same split. `src/emit.rs` has the
  Markdown writers leave an optional tag out only for a member of a union in
  this measured shape. Every other union's examples pass the tag back, as they
  did before: no certified tree shows Fern leaving it out beside a mapping
  whose targets all resolve, and the corpus offers none either way (every
  registered document generated the same Markdown before and after the change,
  conquery aside).
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

A third document, [`unaffected-control`](unaffected-control/openapi.yml), has
neither shape. Every mapping target resolves, each `allOf` variant's base is a
plain object, and `Letter`'s own tag is optional. It is held to the tree
crozier wrote before either repair, not to Fern's: its `base-tree.<mode>.sha256`
files are `sha256sum` over the output of this branch's base, `275e9d3da`, in
each enum mode (45 and 44 files). The control's whole generated tree, README.md
and reference.md included, matches them byte for byte. After main was merged
at `cea260ad4`, `sha256sum -c` over a binary built at `cea260ad4` itself, and
over one built from the merged tree, passed for every file in both modes. The
digests therefore hold for the new base too.

`crates/crozier-e2e/tests/e2e/emission_parity.rs` holds each tree whole
through the parity engine and the departures ledger. Each test then induces a
change the comparison must refuse.
`a_document_neither_cause_touches_generates_the_base_tree_byte_for_byte`
compares the control's every file with the base's digests. Its `sdk_env_*` journey runs
[`dangling_mapping_wire.py`](../../../crates/crozier-e2e/tests/e2e/dangling_mapping_wire.py)
over crozier's SDK in both modes, and over the certified tree, which fails at
the `METEOR` read. The unit tests beside each repair are in `src/ir.rs`
(`variant_wrappers_inherit_fields_through_an_all_of_only_base`,
`branch_union_properties_lends_only_an_undiscriminated_members_branches`,
`a_mapping_target_naming_no_schema_carries_its_tagged_members_fields`,
`a_dangling_mapping_reads_as_before_unless_its_members_resolve_beside_a_named_target`,
`dangling_mapping_wrappers_names_only_wrappers_a_member_fills`), `src/emit.rs`
(`markdown_examples_leave_an_optional_tag_out_only_beside_a_dangling_mapping_target`) and
`src/departures.rs`
(`dangling_mapping_variant_fields_holds_on_the_wrapper_and_nowhere_else`).

## conquery's outcome

conquery is registered as corpus row 3478, `ingef-conquery`
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

**The comparison.** At `491ba4aba`, an earlier source than the final one,
crozier generated from the exact document and was compared through `crozier
compare` with the committed golden
(python-enums) and the certified pair's complete literals tree, measured with
the same bytes and pair:

| mode | files compared | differing | departures applied |
|---|---|---|---|
| python-enums | 239 | 0 | five `sdk-identity-header-prefix` lines; `init-type-checking-import-order` at `types/__init__.py:73`; `dangling-mapping-variant-fields` at `types/query.py:1` |
| literals | 238 | 0 | the same, and `fern-metadata-generator-config` at `.fern/metadata.json:5` |

Both report `matched`. The corpus gate holds the same result, and on the
merged source it is the comparison of record (see "Verification on the merged
source" below):
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

## Merging main at `cea260ad4`

The merge of main at `cea260ad4` (`5cba42910`) brought RS-Server, which keeps
corpus row 3477, so conquery is row 3478. Both rows had raised the
registered-source count from 274 to 275, and the two identical edits merged as
one; `49c42b1a1` counts both (276 sources, 245 under `corpus-sources/`).

Main registered RS-Server without re-measuring golden reach, so re-measuring
here moved two census facts. Both are RS-Server's consequences, not conquery's.
RS-Server's golden executes `nested_array_element`'s `items.one_of` arm in 21 of
its 21 regions. That supersedes `nested-array-elements`' arm-level
`items-oneof-element` cover, which `03333dd02` retires under the manager's
ruling. RS-Server also declares two null examples, so the ledger lists it beside
`webflow-v2` for `schema-example-null`. Removing them moves no generated file,
so it is no witness of that row. The row's residual-only `harbor-signal-null`
proof therefore stays, as the manager's later ruling holds. `03333dd02` had
retired it too, and the revert after it restores the base's content. The census
gate change that stops such a declarer superseding the proof comes from
main.

## Earlier derived records

The measurements below used merge commit `5cba42910`'s `src/`. The post-merge
records below supersede them. Each earlier derived record was regenerated from that source:

| record | generated by | at |
|---|---|---|
| [`departures-ledger.tsv`](../../../tests/fixtures/departures-ledger.tsv) and the invalid-example inventory | `crates/crozier-e2e/departures-ledger.sh` (the script behind `just departures-ledger`), every golden comparison passing | `34b82e4f2`; rerun after `harbor-signal-null` moved, and its rows follow the move in `03333dd02`. Against main the ledger adds the 32 rows of this branch's goldens and moves `harbor-signal-null`'s five, and the inventory is unchanged |
| [`golden-reach.tsv`](../../openapi-surface/golden-reach.tsv) and the region files' reach cells | `just golden-reach`: the source check, the measurement over 276 golden tests, the census and the report | measured at `34b82e4f2`, which the ledger's header names; committed in `a745a6ab5` |
| the census JSON (`.local/golden-reach/census.json`, not committed) and the [`document-paths`](../../openapi-surface/document-paths.md) snapshot, its digest and stated counts | `just golden-reach`'s census step, then `restate-coverage.py --snapshot-json` | `a745a6ab5` |
| the coverage restatements in [`openapi-surface-coverage.md`](../../openapi-surface-coverage.md) | `restate-coverage.py --write`, `golden-reach.py arms --headline`, and the reach ranking's and blind-spot rows' cells restated from the reach ledger | `a745a6ab5` |
| [`handwritten-reach.tsv`](../../openapi-surface/handwritten-reach.tsv) and [`witness-search-keys.tsv`](../../openapi-surface/witness-search-keys.tsv) | `just handwritten-reach`; `witness-search-region-keys.py` | `a745a6ab5` and `03333dd02`, after the retirements |

## Earlier verification

Every result below is from an earlier state: the final `src/`, `5cba42910`'s,
with both retirements of `03333dd02` in the tree, before the revert. The
post-merge results are recorded separately below. Temporary files went under a TMPDIR
outside the worktree, and PATH held only absolute entries.

| check | result |
|---|---|
| the library's unit tests | 743 passed |
| every crozier-e2e comparison, run by `departures-ledger.sh` (among them `ingef_conquery_matches_fern_output`, `overlay_goldens_match_fern_output` with conquery's `expected-literals`, `rs_server_matches_fern_output`, `every_registered_corpus_is_wired_into_the_gate`, the `emission_parity` journeys including the unaffected control's whole-tree comparison, and `residual_null_example_is_absent_from_matching_request_snippets` over the moved tree) | all pass |
| `sdk_env_conquery_secondary_id_query_round_trips_through_the_client`, `sdk_env_a_dangling_mapping_variant_round_trips_through_the_client`, `sdk_env_empty_root_security_client_calls_unsecured_operations_without_a_key` | 3 passed |
| the unaffected control against binaries built at `cea260ad4` and from the merged tree, `sha256sum -c` over its digests | every file matches, in both modes |
| the `surface-census` project's `test-census` suite, complete | 615 passed, 1 skipped |
| `corpus_sources.py check`, `corpus-licensing-drift.py`, `licence-rescreening-check.py` | pass |
| `test-corpus-offline`: `corpus_offline_test`, `corpus_offline_recovery_test`, `match_usage_test` | all pass (2, 1 and 3 tests) |
| clippy with `-D warnings` over `crozier` and `crozier-e2e`, rustfmt's check, ty over `tools/surface-census` | clean |

Two of these first failed because of where temporary files went, not because
of the code. With TMPDIR inside the worktree, nine `compare` discovery unit
tests found the repository's own git top level, and nx's socket path for the
ledger run exceeded the socket-length limit. `corpus_offline_test` failed on the
doubled source count until `49c42b1a1`, and the census suite on the superseded
proofs until `03333dd02`.

## Post-merge source and derived records

Merge `6235dc9b6` concludes the merge of `bc66bfb08` into this branch; its
parents are `02f81c49c` and `bc66bfb08`. No merge state, unmerged path or conflict
marker remains in the eight resolved files. The source commit for every record
below is `4e009625a`: it follows that merge, and its `src/` is byte-identical to
`5cba42910`'s. No subsequent change modifies `src/`.

| record | generation from source `4e009625a` |
|---|---|
| departures ledger and invalid-example inventory | `just departures-ledger`; 811 e2e checks passed, and both generated files were unchanged |
| golden-reach ledger and region reach cells | `just golden-reach` measured all 276 golden tests; `just golden-reach-report` rejoined them after the interaction-site migration; the ledger header names `4e009625a` |
| census JSON, document-path snapshot and extension counts | the census step of `just golden-reach`, then `restate-coverage.py --snapshot-json .local/golden-reach/census.json --write`; 903 selectors, 1,328,715 declaration sites, 276 sources; the JSON is an uncommitted measurement artifact |
| coverage index restatements | `restate-coverage.py --write` and `golden-reach.py arms --headline`; the source count is 276. The ranking's 83 rows were generated from the ledger by `restate-reach-ranking.py` in the dispatch scratch directory, preserving boundary text by key and rejecting a changed key population; the existing restater does not write that table |
| hand-written reach and configuration-gate ledgers | `just handwritten-reach`; 117 arm covers, 10 combination interaction sites and no configuration gates; both generated files were unchanged |
| outstanding arm-search list | `golden-reach-search.py outstanding`; 171 items across six searches |

Main's new `combo-allof-oneof-member` site named the arm this repair moved out
of `Builder::add_object`. Its replacement is that method's
`Some(BranchUnion::Tagged) => continue` arm inside the `allOf`-member loop,
following the manager's requirement that both features meet within one function.
It has its own counter region, `[13289, 50, 13289, 58]` in `src/ir.rs` at
`4e009625a`; Zoonk's scoped measurement reaches that region. Thus the row still
measures an interaction, and no production code or gate rule changed to create
a measurement site. The first census run exposed the stale site and the source
count of 275; it was interrupted after 325 passing tests and one skip to read
those failures. It reported no failure concerning `schema-example-null`.

## Verification on the merged source

The following completed checks exercise `4e009625a`'s source:

| check | result |
|---|---|
| `crozier:test`, including every touched module's unit tests | 1,096 passed |
| focused `crozier-e2e:test` with normal ledger enforcement: `emission_parity`, conquery's golden, overlays and gate wiring | 12 passed; both enum modes and the unaffected control's full tree pass |
| `just test-sdk-env` | 38 SDK-environment journeys passed, including both conquery and from-scratch dangling-target HTTP journeys; the runtime comparison and nested-discriminator runtime project also passed |
| corpus source and licence lint targets | passed |
| `just test-corpus-offline` | 2 offline tests, 1 recovery test and 3 command-usage tests passed |
| clippy, rustfmt checks and project boundaries for both Rust projects | passed |

The source document still has SHA-256
`c3a52b3c5453c003a563a9b39784dfcd9f89f69e0ae1848dbec2881a24b9ec21`.

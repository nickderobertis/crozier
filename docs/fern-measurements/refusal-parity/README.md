# Refusal parity: discriminants Fern never reads

crozier refused three real documents with `discriminant-value-unsuitable`, but
the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3)
generates from all three. This record names the root cause, the code that
changed, and each document's outcome.

`quoted-continuation-at-key-column/` is another case in this directory, with
its own record in its `README.md`.

## Root cause

Each document's discriminator names a mapping target by **bare schema name**,
not by reference (`c: Child`, `'#microsoft.graph.aadUserConversationMember':
AadUserConversationMember`). Fern cannot resolve that target. It writes the
union as `typing.Any` and never checks the discriminant's name, so `$_type` and
`@odata.type` pass. crozier already lowered a bare-name `oneOf` to `typing.Any`
(Hasura's `FunctionReturnType`). It still refused the name first, and it lowered
the inheritance spelling, a base object whose mapping names the subtypes that
`allOf` it, to a discriminated union.

A mapping of references only is still refused by the certified pair, in both
spellings and for every name tried. The class keeps those refusals. The class's
probes and controls in
[`../../fern-refusals/discriminant-value-unsuitable/`](../../fern-refusals/discriminant-value-unsuitable/)
are measured into
[`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv):

| shape | discriminant | mapping | Fern |
|---|---|---|---|
| `probe.yml` | `_t`, `oneOf` | references | refused |
| `dollar-oneof-probe.yml` | `$_type`, `oneOf` | references | refused |
| `odata-oneof-probe.yml` | `@odata.type`, `oneOf` | references | refused |
| `underscore-inheritance-probe.yml` | `_t`, inheritance base | references | refused |
| `odata-inheritance-probe.yml` | `@odata.type`, inheritance base | references | refused |
| `mapping-only-probe.yml` | `_t`, mapping and no `oneOf` or subtypes | references | refused |
| `inferred-probe.yml` | `_t`, inferred from one-value enums | none | refused |
| `bare-name-oneof-control.yml` | `$_type`, `oneOf` | one bare name | generates |
| `bare-name-inheritance-control.yml` | `_t`, inheritance base | one bare name | generates |

Under a bare-name mapping, the AllOf document generates byte-identical trees
with its `$_type` renamed to `kind`, `_t` or `kind-name`.

Teams needed one more rule. Its `addMultipleTeamMembers` answers a typed `200`
beside a bodyless `207`, and Fern types the method by the `200`. A
from-scratch probe measured `203`, `205`, `206`, `207`, `208`, `226` and `299`
beside a typed `200`: every one is non-optional, and only a `204` makes the
method optional.

## The repair

- `src/name_refusals.rs` `check_schema_names` skips the discriminant-name check
  for a union that `bare_name_mapped_union` matches. It still checks that
  union's properties and members.
- `src/ir.rs`:
  - `bare_name_mapped_union` (new) is the shared predicate: a `oneOf` or an
    inheritance base whose mapping names a target with no `/`.
  - `add_named_shape` lowers both spellings to `typing.Any`.
  - `collect_discriminant_strips` strips a `oneOf` member's tag only where the
    mapping names that member by reference. The bare-named member keeps its
    tag, as Fern's does.
  - `build_endpoint` guards the empty body of a response naming such a union.
  - `resolve_request_body` sends such a union body as `json=request`, without
    the annotation converter, with the content-type header.
  - `has_bodyless_success` treats only a bodyless `204` beside a typed success
    as the empty-body case.

## Each document

None is excepted. Each one now generates, and the three are registered as
corpus goldens (rows 3473 to 3475 of
[`tests/fixtures/CORPUS.md`](../../../tests/fixtures/CORPUS.md)), with the
source bytes vendored at the digest the finding recorded.

| document | sha256 | golden row | python-enums | literals |
|---|---|---|---|---|
| `OpenAPITools/openapi-generator:samples/client/petstore/csharp/generichost/net10/AllOf/api/openapi.yaml@10e6c21c97abb098cc67f14dfdd02171ce56b115` | `cc2fa0a1aab917a00f77fa60624b7b20a62d6efd1290f7d5aff7407e0ce5e153` | `openapitools-csharp-allof` | 41 of 41 files match | 40 of 40 files match |
| `Carapacik/swagger_parser:swagger_parser/test/schemas/null-types-with-type-array.yaml@1fec2df2fd073ff5bb93a703b856cdfad25b129c` | `55071fd9a9c9cd7c1beec58a95f789269dc37a14d130f5d5998a72133145d378` | `swagger-parser-null-types` | 42 of 42 files match | 41 of 41 files match |
| `ToolJet/ToolJet:marketplace/plugins/microsoft_graph/openapi-specs/teams.yaml@63c2b08614b78f8f289fb6127a32f10ed5987362` | `09ac0c7b1b7a47717896622ec4fdf2b752575aabd215659f3fb1438e83de1d87` | `tooljet-microsoft-teams` | 188 of 188 files match | 187 of 187 files match |

"Match" means the parity engine found no unexplained difference.
`sdk-identity-header-prefix` explains lines in every tree, and
`fern-metadata-generator-config` in the literals trees. In teams,
`init-type-checking-import-order`, `schema-rejected-name-example` and
`schema-rejected-array-length-example` explain lines too. The departures
ledger pins each such line.

Each document's grant, as read from its repository's `LICENSE` at the pinned
revision and its own `info.license`, is in its `CORPUS.md` row and `NOTICE`
entry. All three are admissible under
[`docs/corpus-licensing.md`](../../corpus-licensing.md).

The null-types document's first refusal was this class. With it repaired,
nothing else refuses or diverges.

## The refused population is unchanged

crozier ran over the class's 13 refused documents, recorded in
[`../../fern-refusals/discriminant-value-unsuitable/evidence/population-strict.log`](../../fern-refusals/discriminant-value-unsuitable/evidence/population-strict.log),
on the repaired tree in both modes. Each document's bytes were checked against
its digest first. All 13 still exit 1 in both modes.

- Eleven are refused by this class at the element the log names. Their mappings
  name references only.
- Two Helicone documents (`9fa0f757…`, `ccf555cd…`) are refused first by
  `example-type-mismatch`. Their `DataEntry` is an `anyOf` with no
  `discriminator`, which the repair cannot reach.

## The from-scratch case

[`discriminant-names-orchard/`](discriminant-names-orchard/evidence.md) is a
document written for this measurement. It puts both spellings under unusable
discriminants (`@kind`, `$label`), sends and answers each, and declares a
bodyless `206` beside a typed `200`. Its python-enums tree and its
[literals tree](discriminant-names-orchard-literals/evidence.md) are compared
whole by
`refusal_parity::bare_name_mapped_discriminants_match_fern_in_both_enum_modes`
in `crates/crozier-e2e/tests/e2e/refusal_parity.rs`. The same file's
`pointer_mapped_discriminant_refusals_hold_beside_the_bare_name_controls`
drives every refused shape above, and both controls, through the CLI in both
modes.

Every arm the repair touches is reached by the three registered real goldens.
So, by the manager's ruling, the case is a byte-gated e2e measurement rather
than a `docs/openapi-surface/handwritten/` fixture. No census key was added to
give it a cover.

The ruling was delivered over the run's planner channel (correlation
`c-f7ed5ca398118fe8d4cad89fa01725f1`, reply 34). It answered the question of
how a hand-written fixture could carry a cover once real witnesses reach every
arm. It amended this node's acceptance criteria with this text, quoted
verbatim:

> Where every arm the repair touches is reached by a registered real golden
> witness, the hand-written fixture criterion is met by a from-scratch document
> of the triggering shape whose crozier output is byte-compared with its
> certified-pair tree by an e2e test in crates/crozier-e2e, apart from lines the
> departures ledger records under an authorized departure. No
> `handwritten_fixtures_match_fern_goldens` cover is required for that shape.

## Red and green

The new real-CLI acceptance tests were run twice, both times through
`cargo nextest run -p crozier-e2e` against the debug binary each tree builds:

- **Red:** in an isolated worktree at commit `a9a1d4cef`, with only
  `src/ir.rs` and `src/name_refusals.rs` restored to the base `0f348a953`.
  This reverts the production fix and keeps every new test, fixture, golden and
  ledger row.
- **Green:** the finished tree at the same commit.

| test | red | green |
|---|---|---|
| `refusal_parity::bare_name_mapped_discriminants_match_fern_in_both_enum_modes` | FAIL: the orchard document is refused, `#/components/schemas/Crate discriminant "@kind"` | PASS |
| `refusal_parity::pointer_mapped_discriminant_refusals_hold_beside_the_bare_name_controls` | FAIL: every refused probe is refused, then `bare-name-oneof-control.yml` is refused, `#/components/schemas/Asset discriminant "$_type"` | PASS |
| `openapitools_csharp_allof_matches_fern_output` | FAIL: refused, `#/components/schemas/Person discriminant "$_type"` | PASS |
| `swagger_parser_null_types_matches_fern_output` | FAIL: refused, `#/components/schemas/Person discriminant "$_type"` | PASS |
| `tooljet_microsoft_teams_matches_fern_output` | FAIL: refused, `#/components/schemas/ConversationMember discriminant "@odata.type"` | PASS |
| `overlay_goldens::overlay_goldens_match_fern_output` | FAIL: only the three new literals overlays, each refused as above | PASS |
| `discriminant_refusals_recover_with_a_valid_document_name` (existing guard) | PASS | PASS |

Every red failure is the triggering refusal of a bare-name-mapped document, and
no other fixture failed. The pre-existing guard passes in both runs, because the
shapes it refuses are refused before and after the repair. The excerpts are
[`evidence/red.log`](evidence/red.log) and
[`evidence/green.log`](evidence/green.log). The `src/` unit tests were shown
failing the same way earlier, against the four reverted hunks.

## Measurement provenance

Every Fern run this record rests on held the shared generation lock
`${XDG_CACHE_HOME:-$HOME/.cache}/crozier/fern-generation.lock`:

- the goldens and literals overlays;
- the `shapes` measurements;
- the from-scratch trees;
- the re-measurement of every probe and document.

An earlier pass held a different lock file, so it was not serialised against
other workers. It was re-run under the shared lock, and every tree and exit
code came out identical.

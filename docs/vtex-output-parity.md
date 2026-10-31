# VTEX Marketplace Protocol: emission parity and registration

`APIs-guru/openapi-directory`
`APIs/vtex.local/Marketplace-Protocol/1.0/openapi.yaml` at
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` (sha256
`748ff9ba7fba914537047a5198e24da9d32e64608cede2a67f9561cd53cee743`) generates
under the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk`
5.41.3) and under crozier. Before this change, crozier's output differed from
the certified pair's in 12 files, through three causes. This record gives each
cause, the crozier code its repair changed, and its outcome. It also registers
the document as corpus row 3479. No cause is excepted: on each shape crozier now
writes what the certified pair writes.

## 1. Worked-example parameter order

`POST /{accountName}.vtexcommercestable.com.br/api/order-integration/orders`
declares the optional query `an` before the required query `affiliateId`.
`place_fulfillment_order` and its `/fulfill` sibling declare the optional `sc`
first in the same way. The certified pair's worked call keeps declaration order
(`an="apiexamples", affiliate_id="MKP"`) in `reference.md` and in both client
docstrings. crozier grouped required query parameters before optional ones.
Signatures already matched.

**Measured.** [`query-declaration-order`](fern-measurements/emission-parity/query-declaration-order/evidence.md)
interleaves optional and required query parameters, and optional and required
header parameters, beside a JSON body, a `multipart/form-data` body and an
operation whose required query comes first. The certified pair walks each kind
in declaration order. It shows a required parameter, unless one of the
omissions crozier already models applies, and an optional one only by its
declared example. `reference.md` and the README put queries before
headers, and the docstrings put headers before queries. The headers follow the
same rule as the queries: `write_logbook`'s optional `X-Watch-Note`, declared
first, comes before the required `X-Keeper-Id` everywhere.

**Repair.** `src/emit.rs`, `build_example_inner`: the query and header
parameters are each collected in one declaration-order pass, with each
parameter's value computed as before. The group order and the docstrings'
headers-first partition are unchanged. Unit test:
`emit::tests::worked_examples_keep_each_parameter_kind_in_declaration_order`.

## 2. Framing and forwarding header parameters

`POST /{fulfillmentEndpoint}/pvt/orders` declares required header parameters
`content-length` and `x-forwarded-for` beside `x-forwarded-proto` and nine
others. The certified pair's `order_placement` takes neither of the first two.
It keeps `forwarded_proto`. crozier exposed `content_length: str` and
`forwarded_for: str`, documented them, sent them, and wrote them into the worked
call.

**Measured: the rule.** [`framing-headers`](fern-measurements/emission-parity/framing-headers/evidence.md)
declares 48 header names on one operation in lower case and on another in
canonical case, all required, and five of them optional on a third. The names
are the standard request, framing, forwarding, caching, conditional and
credential headers plus common `X-` extensions. The certified pair drops exactly
seven, in both spellings and whether required or optional:

`Content-Length`, `X-Forwarded-For`, `Content-Disposition`, `Content-Type`,
`User-Agent`, `Origin`, `Cookie`.

Every other name stays an ordinary argument. That includes `X-Forwarded-Proto`,
`X-Forwarded-Host`, `X-Forwarded-Port`, `X-Forwarded-Server`, `Forwarded`,
`X-Real-IP`, `X-Original-Forwarded-For`, `Host`, `Transfer-Encoding`,
`Content-Encoding`, `Content-Range`, `Content-MD5`, `Set-Cookie` and
`Authorization` (the probe declares no security scheme). So the rule is a fixed
set of names, compared without regard to letter case. It is not a category such
as hop-by-hop or forwarding headers.
[`promoted-framing-headers`](fern-measurements/emission-parity/promoted-framing-headers/evidence.md)
puts `Content-Length`, `X-Forwarded-For`, `X-Forwarded-Proto` and `X-Tower` on
every operation. Only `forwarded_proto` and `tower` become client constructor
fields. The same set is kept off the client wrapper too.

crozier already dropped four of the seven (`Content-Type`, `User-Agent`,
`Origin`, `Cookie`). The probe confirms those four at the certified pair, and
adds `Content-Length`, `X-Forwarded-For` and `Content-Disposition`.

**Repair.** `src/ir.rs`, `is_transport_managed_parameter`: the three names join
the set. That function already gates both a method's header parameters
(`build_endpoint`) and client-wrapper promotion (`global_headers`). Unit test:
`ir::tests::framing_and_forwarding_headers_leave_the_method_and_the_wrapper_and_their_neighbours_stay`.
It fails against the previous set. The census's port of the same rule,
`UNPROMOTED_HEADERS` in `tools/surface-census/openapi-surface-census.py`,
takes the three names too, under the function's new pinned digest. Its
subset-header test gains a decoy for each, and fails without the port change.
The port moves no census count.

## 3. A declared array that also lists properties

The finding said the simulation response's `assemblyOptions`,
`installmentOptions` and `installmentOptions.installments` declare no `type`.
They do declare one: each is `type: array` with `items: {}` and a `properties`
map. The certified pair types each field `typing.Optional[typing.List[typing.Any]]`.
crozier hoisted three object models for them.

**Measured.** [`array-with-properties`](fern-measurements/emission-parity/array-with-properties/evidence.md)
covers four cases:

- `type: array` with `properties` beside empty items, nested two deep: the pair
  writes `List[Any]`.
- With string items: `List[str]`.
- With no `items`: `List[Any]`.
- As a component: `Bundle = typing.List[typing.Any]`.

In every case the declared type decides, and the `properties` map is never read.
A schema carrying `items: {}` and `properties` with *no* declared type (`weather`)
is still an object model. crozier already wrote it that way.

**Usefulness.** The question was whether an object reading would be more useful
here. It would not. The document declares the fields arrays, and its own
simulation response example sends `installmentOptions` as a JSON array of
objects. A model typed as an object cannot hold that array, so crozier's reading
contradicted both the declaration and the example. `List[Any]` accepts what the
API returns. Matching the certified pair copies no defect.

**Repair.** `src/openapi.rs`, the new `normalize_array_properties` pass in
`load`: a schema whose declared type is `array` loses its `properties` map
before anything reads it. Its `items` are kept. Unit test:
`openapi::tests::a_declared_array_drops_the_properties_beside_its_items_and_an_untyped_one_keeps_them`.

## The from-scratch documents

All four documents were written for this record. Their trees were generated by
`just fern-references measurements emission-parity/<case>` (rows in
[`fern-measurements/cases.tsv`](fern-measurements/cases.tsv)), under the shared
lock `${XDG_CACHE_HOME:-$HOME/.cache}/crozier/fern-generation.lock`, one Fern
run at a time.

| case | proves | crozier against both trees |
|---|---|---|
| `query-declaration-order` (+ `-literals`) | cause 1 | matches, apart from `sdk-identity-header-prefix`, `multipart-object-required-file-example` on `upload_photo`'s docstring, and, in literals, `fern-metadata-generator-config` |
| `framing-headers` (+ `-literals`) | cause 2, method signatures | matches, apart from `sdk-identity-header-prefix` and, in literals, `fern-metadata-generator-config` |
| `promoted-framing-headers` (+ `-literals`) | cause 2, client wrapper | the same |
| `array-with-properties` (+ `-literals`) | cause 3 | the same |

The `multipart-object-required-file-example` lines are an existing catalogued
departure. They are the required file placeholder crozier adds to the docstring
example Fern leaves unbindable. They have nothing to do with ordering.

`crates/crozier-e2e/tests/e2e/emission_parity.rs` holds each tree whole through
the parity engine and the departures ledger in both enum modes. Then each test
restores crozier's previous output in one file and asserts the comparison names
that file:

- `worked_examples_keep_parameter_declaration_order`
- `framing_headers_leave_the_method`
- `framing_headers_on_every_operation_stay_off_the_client`
- `an_array_declaring_properties_is_a_list_of_its_items`

## Registration

VTEX's document is corpus row 3479, `vtex-marketplace-protocol`
([`CORPUS.md`](../tests/fixtures/CORPUS.md)). The corpus rules admit it on the
same terms as row 121, `vtex-pricing`, from the same aggregation revision:

- **Grant:** CC0-1.0. This is the aggregating repository's own `LICENSE`, and
  the document declares no `info.license`.
- **Revision:** the immutable commit `f04b8d0b…`.
- **Source bytes:** vendored under
  `tests/fixtures/corpus-sources/vtex-marketplace-protocol/` and recorded in
  `corpus-sources.tsv` at the sha256 above.
- **`NOTICE`:** the entry for the specification and its golden.
- **Gate wiring:** the `CORPORA` list and `vtex_marketplace_protocol_matches_fern_output`,
  `tests/corpus_match/match.sh`, the literals overlay in `overlay_goldens.rs`,
  `compared-goldens.json`, and the registered-source count in
  `corpus_surface_census_test.py`.

The golden was generated by Route A, `just fern-goldens-generate --version
5.41.3 --fixture vtex-marketplace-protocol` at CLI 5.163.1. The literals
overlay came from `fern-overlay-goldens.sh --enum-type literals`. Each ran
under the shared lock.

## VTEX's outcome

On the finished tree, crozier's SDK for the exact document byte-matches the
certified pair's in both enum modes. `vtex_marketplace_protocol_matches_fern_output`
compares all 142 files of the python-enums golden.
`overlay_goldens_match_fern_output` compares the 141-file literals tree. The
only departure lines the ledger records for it are these:

- the five `sdk-identity-header-prefix` lines in `core/client_wrapper.py`
- `fern-metadata-generator-config` at `.fern/metadata.json:5` (literals only)

No line is attributed to an excepted cause, because none is excepted.

## Goldens the repair moves

A base binary built at `1748b7946`, this branch's base, and one built from the
repaired source at `27ef9c038` each generated every registered source in both
enum modes, with the same flags. That covers the 263 documents of
`corpus-sources.tsv` and the 31 vendored `tests/fixtures/*/openapi.yml`. The
two trees differed for one document only: VTEX's own, in both modes. 18
documents are refused identically by both binaries, the refusal-parity rows,
and every other document generated byte-identical trees. So the targeted golden
tests for the moved output are VTEX's two:
`vtex_marketplace_protocol_matches_fern_output` (python-enums) and
`overlay_goldens_match_fern_output` (its `expected-literals`). Separately, the
complete crozier-e2e suite passed on the repaired source, every corpus golden
among it. It ran first on its own, then again under `just departures-ledger`,
which records every comparison's departures. The regenerated ledger adds rows
only for VTEX's goldens and the four new measurement trees. It drops only the
five rows of the hand-written fixture retired below.

## Hand-written evidence the registration supersedes

A real specification registered later supersedes a hand-written proof of the
same thing ([the hand-written contract](openapi-surface/handwritten/AGENTS.md)).
Once VTEX's golden was measured, `handwritten_fixtures_match_fern_goldens`
named two arm-level covers whose arms VTEX now reaches. VTEX is also the first
registered golden source declaring `header-subset-string-default`: the census
counts 7 sites of `parameter.schema:subset-header-string-default` in it. The
manager approved the following (reply 123, correlation
`c-d80f4a590dff01d75c81e1223c90f356`):

- **`blank-reading-description` loses its `description` arm cover**
  (`InlineHoister::hoist_object`'s empty-description arm). The fixture keeps its
  feature-level cover, `empty-description-inline-response-docstring`.
- **`header-subset-string-default` reads `golden`** in
  [`parameters.md`](openapi-surface/parameters.md), witnessed by
  `vtex-marketplace-protocol`, under the category precedence in
  [`openapi-surface-coverage.md`](openapi-surface-coverage.md#the-category-rules).
  Its handling site is `global_headers`' subset-string-default arm, now listed
  in [`golden-reach-sites.tsv`](openapi-surface/golden-reach-sites.tsv). VTEX
  reaches it.
- **The `header-subset-string-default` hand-written fixture is retired.** Its
  feature cover needs a `handwritten` row, and its `parameter-in-header` arm
  cover is superseded the same way, so it has no valid cover left. Its key
  leaves [`witness-search-keys.tsv`](openapi-surface/witness-search-keys.tsv),
  as `witness-search-region-keys.py` derives it. The parameter-lowering search
  record names VTEX as the declarer that became the witness.

The reach ledger moves for VTEX in two more places:
`parameter-in-header` goes from 3 unreached sites to 2, and `description` from 1
to 0.

## Derived records

Main was merged again at `8c0170eb7` (merge `caa31dac1`), which registered
corpus rows 4200 to 4212 beside VTEX's row 3479. The merge brought main's
changes to three `src/` files, and the repair's own `src/` changes are
`27ef9c038`'s. Each record below was regenerated with its own tool on
`9a9c7621f`, the tree after the merge, and committed in `8584228f0`.

| record | generated by |
|---|---|
| [`golden-reach.tsv`](openapi-surface/golden-reach.tsv) and the region files' reach cells | `just golden-reach` over 290 golden tests: 353 reach cells, and the census over 916 selectors, 1,357,551 declaration sites and 290 sources |
| the document-path snapshot and the coverage restatements | `restate-coverage.py --snapshot-json .local/golden-reach/census.json --write`, `restate-coverage.py --write`, and the arm restatement of `just golden-reach-arms` with its `--headline` flag |
| the reach ranking, the blind-spot rows' unreached-arm counts, the hand-written totals and the hand-written verdict split in the coverage index | restated from the ledger, since no restater writes them: 79 ranked rows, 107 unreached arms, 141 features and 102 arms on hand-written fixtures, and 10 `exhausted` against 130 `search-incomplete`. `RankedBacklogTests` checks each one against the ledger |
| [`handwritten-reach.tsv`](openapi-surface/handwritten-reach.tsv) | `just handwritten-reach`: 107 arm covers, 20 combination interaction sites, no configuration gates; the merged file was already exact |
| [`witness-search-keys.tsv`](openapi-surface/witness-search-keys.tsv) | `witness-search-region-keys.py`; the merged file was already exact |
| [`witness-search-registries/outstanding.tsv`](openapi-surface/witness-search-registries/outstanding.tsv) | `witness-search-registries-index.py`, which drops `header-subset-string-default`'s two rows |
| [`golden-reach-witnesses/outstanding.tsv`](openapi-surface/golden-reach-witnesses/outstanding.tsv) | `golden-reach-search.py outstanding`: 171 items across six searches, unchanged apart from its commit column |

The departures ledger and `compared-goldens.json` merged without conflict, and
their gates (`departures_ledger_gate`, `compared_goldens_inventory_is_current`)
pass on the merged tree.

### The failed publication

The first publication's `gate` check failed on every leg (Linux, macOS,
Windows) in two witness-search tests. When `header-subset-string-default`
became a `golden` row, two things were left stale: the registries'
outstanding inventory still listed the key, and the single-feature key count
was not lowered. `9a9c7621f` regenerates the inventory and states the count,
now 141 after main's merge.

## Verification

Every check below ran on `8584228f0`, apart from the census suite and the
judged lint, which ran on `564e46794`, the commit adding this table. Commits
after `8584228f0` change only this record.

| check | result |
|---|---|
| `just nx run-many --targets=test,lint,format --projects=crozier` (unit tests, clippy, rustfmt) | passed; 1,105 tests |
| `just nx run crozier-e2e:test`, the complete suite: `vtex_marketplace_protocol_matches_fern_output`, `overlay_goldens_match_fern_output`, all 290 `*_matches_fern_output` corpus goldens (main's rows 4200 to 4212 among them), `handwritten_fixtures_match_fern_goldens`, `every_registered_corpus_is_wired_into_the_gate`, the `emission_parity` tests and the departures-ledger gates | 845 passed, 45 skipped (the ignored tiers) |
| VTEX's golden test and the overlay test, with sockets denied by `corpus_offline_test.py --deny-network` and `.local/corpus` and `.local/census-fallback-sample` absent | 2 passed |
| `just lint-corpus-sources`, `just lint-corpus-licensing`, `just lint-licence-rescreening` | passed |
| `restate-coverage.py` drift check | no drift |
| `witness_search_acquisition_test.py`, the file holding the two tests that failed the publication | 33 passed |
| the `surface-census` project's `test-census` suite, complete | 639 passed, 1 skipped |
| judged lint over the diff against `8c0170eb7`, `origin/main` as merged (`just lint-llm-diff 8c0170eb7`) | all 5 batches passed, 0 rules failed |

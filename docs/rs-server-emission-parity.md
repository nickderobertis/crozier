# RS-Server: emission parity and registration

`RS-PYTHON/rs-server` `services/frontend/resources/openapi.json` at
`83ebcafb173c53443d92c54aeeba4f221e36f9c2` (sha256
`a87710725b8bdea9cdeab44b61390b10718280a88432f6a4896c757c8704d27a`) generates
under both the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk`
5.41.3) and crozier. The refusal was repaired first
([`rs-server-collision-parity.md`](fern-refusals/example-type-mismatch/rs-server-collision-parity.md)).
That record measured six causes behind crozier's differing output. This record
gives each cause's outcome and registers the document as corpus row 3477.

## The six causes

| # | cause | crozier code changed | outcome |
|---|---|---|---|
| 1 | Discriminated-union variants inlined from components typed `bbox` as an undeclared `PointBbox`-style name, and their nested `coordinates` as an inline `Union`. `MultiPolygon.coordinates`, three arrays deep, got no `…ItemItemItem` alias | `src/ir.rs`: new `align_flattened_member_types`, called from `build`, types every field a wrapper flattens from a component as the component's model types it. `Builder::field_type_ref` names a union leaf three arrays deep through `nested_array_element`. The unit test `an_annotated_lone_all_of_ref_property_is_its_component_everywhere` had pinned another dangling name, `WeftTrigger`, which nothing declares. It now expects the model's `Trigger` | repaired |
| 2 | The standalone geometry models lost their `type: {const}` tag and its single-value enum (`PointType` …), and the PATCH body's `…PatchRequestBodyType` was missing | `src/ir.rs`: `collect_standalone_references` (with the new `strips_members`) now counts a member of a union that nothing discriminates as a standalone use, outside `text/event-stream` media. `SearchPostRequest.intersects` is such a union, so the tags stay. `resolve_request_body` declares the string `const`/`enum` named by a property written beside an inline union body's alternatives | repaired |
| 3 | `TimeInterval.interval`, arrays of arrays of `anyOf [date-time, null]`, became a named `TimeIntervalIntervalItemItem` | `src/ir.rs`: `Builder::field_type_ref` makes a one-alternative-beside-`null` leaf two arrays deep an optional element. The examples then follow: `[[]]` in docstrings, as Fern writes it, a residual the inventory records. In `reference.md`, crozier pads Fern's `[None]` to the `minItems: 2` that `[None, None]` satisfies, under `schema-rejected-array-length-example`. For that, `src/emit/example_repair.rs` records a nested list that opens on a bare `[`, and `src/departures/rejected_examples.rs` (`list_argument`, new `enclosing_list`) reads one | repaired |
| 4 | The root client's `api_key` is `Optional[str] = None` in crozier and required in the pair | none to the output. `src/ir.rs`: new `empty_root_security_credentials`. `src/departures.rs`: a new `usefulness` kind and the `empty-root-security-optional-credential` rule. `assets/departures.yml` entry and [evidence](departures/evidence/empty-root-security-optional-credential.md) | **excepted**, by the planner's ruling: a catalogued usefulness departure. An empty root `security` list means what an absent one does, and for an absent one the pair already makes the credential optional |
| 5 | `catalog_transaction_extension/types/__init__.py` imported a module's three names in three statements | `src/emit.rs`: `tag_types_init_file` groups consecutive names from one module into one statement, as `types_init_file` does | repaired |
| 6 | The root `__init__.py` places `from .client import …` before the tag subpackages | none | **excepted**: the existing `init-type-checking-import-order` departure (kind `ordering`) covers it. The comparison failed only while other lines of that file differed. With causes 1 to 3 and 5 repaired, the departure applies as it does on every other golden, and crozier's output for the shape is unchanged from this node's base |

Cause 5 also moves other goldens. Wherever a tag's `types/__init__.py`
re-exports a discriminated union, crozier now writes Fern's single import
statement, and the `init-type-checking-import-order` ledger rows that excused
the split statements are gone. The goldens are `deepsearch-ds-v2`,
`get-a-room`, `langchain-agent-server`, `letta`, `osparc-simcore-webserver`,
`paloalto-cspm-alerts`, `panoptes` and `qontract-api`, the hand-written
`glaze-ledger-coats`, and the `output-defects/617-annotated-inherited-union`
measurement. In `sim-tables` the one row moves to the window that still
differs. The regenerated ledger shows exactly those rows moving. Every such
golden still byte-matches in each enum mode it is registered in: `just
departures-ledger` re-ran every golden comparison and every one passed.

## Hand-written measurements

Each repaired cause and the departure have a document written for this record,
with the tree the certified pair generated from it through the shared Fern
generation lock. Each is registered in both enum modes in
[`fern-measurements/cases.tsv`](fern-measurements/cases.tsv), and
`crates/crozier-e2e/tests/e2e/emission_parity.rs` holds crozier to each tree,
then induces an unexplained difference to show the comparison still fails:

| case | proves |
|---|---|
| [`emission-parity/survey-shapes`](fern-measurements/emission-parity/survey-shapes/evidence.md) (+ `-literals`) | causes 1, 2 and 5 |
| [`emission-parity/tide-windows`](fern-measurements/emission-parity/tide-windows/evidence.md) (+ `-literals`) | cause 3 |
| [`emission-parity/lantern-open-ping`](fern-measurements/emission-parity/lantern-open-ping/evidence.md) (+ `-literals`) | cause 4's departure, and nothing else |

Unit tests drive each touched function on these documents:
`ir::emission_parity_tests`, `emit::emission_parity_tests`, and
`departures::tests::an_empty_root_security_list_excuses_only_its_optional_credential`.
The last also shows that an adjacent credential mismatch the departure does not
describe still fails. Cause 4's behaviour is driven end to end by
`sdk_env_empty_root_security_client_calls_unsecured_operations_without_a_key`.
Run against a local HTTP server, a keyless client calls the unsecured ping with
no key header, and a keyed client sends its key on a secured operation. The
same script fails on the pair's tree, which cannot build the keyless client.

## The comparison and the registration

On the finished tree, `rs_server_matches_fern_output` byte-matches all 231
files of the certified pair's golden. That golden is the one the collision
node generated, its `.fern/metadata.json` records CLI 5.163.1 and SDK 5.41.3,
and its literals overlay is registered too (`overlay_goldens.rs`). The only
departure lines in `tests/fixtures/departures-ledger.tsv` are these:

- the `sdk-identity-header-prefix` lines in `core/client_wrapper.py`
- `empty-root-security-optional-credential` on `client.py`'s and
  `client_wrapper.py`'s credential lines (cause 4)
- `init-type-checking-import-order` on the root `__init__.py` (cause 6)
- `schema-rejected-array-length-example` on `reference.md`'s two `interval`
  examples (cause 3)

The registration has these parts:

- the source bytes, under `tests/fixtures/corpus-sources/rs-server/`, recorded in
  `corpus-sources.tsv` at their sha256
- the immutable revision `83ebcafb…`
- the `NOTICE` entry
- the grant: the repository's own `LICENSE` at that commit is Apache-2.0 (blob
  `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`), and the document declares no
  `info.license`
- the gate wiring in `CORPUS.md` (row 3477), the `CORPORA` list,
  `tests/corpus_match/match.sh` and `compared-goldens.json`

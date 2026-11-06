# Bounded continuation of the parameter, security and extension witness search

Base: `92be4edfa6378d3e509c775f8f9796de40cb9b54`. [`targets.tsv`](targets.tsv) freezes every fixture-only
feature, combination and remaining authored arm cover in `parameters`,
`security` and `oas31-extensions`: 39 feature/combination targets and 12 arm
targets. No generator behavior changes. Corpus rows 5370 and 5371 register
HappyHamster and Seldon's wrapper; rows 5372–5399 remain unused.
The 51 targets finish as two real-witness proofs, 47 exhausted searches within
the assigned populations, and two incomplete searches with outstanding candidates.

## Populations screened

1. Exactly the outstanding candidates in the [previous record](../witness-search-fixture-only-operations-extensions/README.md):
   212 target/candidate pairs, 205 distinct document identities. Each identity,
   immutable revision, recovered or newly established SHA-256, byte size,
   preliminary decision and generation selection is in [`candidates.tsv`](candidates.tsv).
   Source-hash-only identities without a recoverable locator remain explicitly
   incomplete; there is no acquisition to rediscover them. Only handed-off decisions are reused. Other historical refusals are not
   current-pair decisions; their outstanding candidates remain unscreened.
2. Exactly the seven [newly admitted documents](../../fern-measurements/handed-off/README.md#newly-admitted-documents).
   [`newly-admitted.tsv`](newly-admitted.tsv) lists their committed paths, byte
   sizes and verified digests, smallest first. All seven digests equal the
   handed-off pins; no fetch is needed for them.

The native census's necessary-condition counts, including zeroes, are in
[`selector-prefilters.tsv`](selector-prefilters.tsv). The exact detectors are
those in the previous record. The nonzero broad hits are `schema.items`,
`schema.default` and `parameter.schema`; none establishes a target alone.
The newly admitted query parameters are plain scalars or arrays of strings:
Grafikart's optional folder strings, Clencyc's required story strings, Arawa's
optional nullable scalars and required string arrays, and VTEX's plain scalar
query arguments. None is a required integer query with a default, a referenced
query enum-or-array union, a required query object with an array member, a
const-member query union, or a nullable union item array. Nixtla and the two
publisher tooling resources have no query parameters of these shapes. The
tracked extension/security predicates and the example-beside-ref conjunction
are zero. The base's complete golden measurement executes none of the 12
remaining target arms, so these seven supply no new arm witness.

Already-screened handed-off documents stay outside this continuation, under
the manager's scope ruling. [`known-declarers.tsv`](known-declarers.tsv) joins
them to the base's handed-off document and residual tables, grouped by cause.
Their statuses are explicitly **base-state measurements**, not comparisons
rerun here. Missing literals overlays are registration work, not a claim that
an existing overlay differs.

## Screening and bounds

Cheap provenance, reference and licence decisions precede generation. Within
each target, its admissible candidates are sorted by exact byte size, then
immutable locator. [`generation-order.tsv`](generation-order.tsv) records the
round-robin selections: at most three distinct certified-pair documents per
target. A shared document is generated once and reused; under the manager's
budget ruling it counts against another target only if it is also among that
target's own three selected candidates. Documents left beyond that bound are
named individually in `candidates.tsv`, even where a registered witness has
already settled their target.

No live licence-file fetch is made. The manager authorized the existing
`witness_screen.licence_screen` and `fern_screen_document` APIs instead of
`just witness-screen`, whose wrapper would fetch files outside the assigned
candidate population. Licence files are read only through existing guarded
response-cache entries. A missing cached grant leaves the candidate incomplete;
it is never turned into a no-grant finding. A full revision without an earlier
digest is fetched through the guard and pinned from that revision, under the
manager's explicit pin-establishment ruling. Every existing digest is checked
before use. Persona's relative reference trees remain unacquired: its eight
named versions are incomplete, not refused by the generator.

Every Fern command runs serially under the shared Fern lock at CLI 5.163.1 /
Python SDK 5.41.3. The first scratch workspaces inherited enclosing Git
provenance. Five successful trees from that preliminary run were removed only
from entries this dispatch itself created and regenerated cleanly with
`GIT_CEILING_DIRECTORIES`; no other dispatch's entry was changed. The five
source hashes are `d3aacb203499646e297b5bfe04d62342d76435ef086fd51d435c9a77fa08c91c`, `5126e1a45f30a9451dcc92a4451a01df8e2cac89d0775ec1d8592fac1459c866`, `fa08d30f1984e480be0b413de20bfc6e0c96b90f109067b45d58013ace144c3c`, `3a8dc3a8efd746de64254da9e8ef7b775f53e59ab6995f056499b42fba580b02`, `481043a3e30df4344d266e5aaba520da1f509e011a1329a415bcb4f9619132ed`.
The initial comparisons also used the wrong distribution name; final comparisons
use package `fern`, distribution `default_package_name`. Those preliminary
results are superseded and are not handoffs. Final cache trees have no enclosing
Git metadata and are untouched complete generated output. Their digest and
successful exit status are checked before reuse. The final current-pair screening results are recorded document by document
in `generation-order.tsv`; older refusal measurements do not decide them. The two registered witnesses also have certified literals
trees, generated through the existing `fern-references.run_fern` API under the
same lock and reduced with `golden_overlay.reduce` after the normal Python
comment stripping. The manager approved this path to avoid a release build
solely for the script's stripper.

## GitHub requests

No GitHub code search was made. No GitHub request was made outside the guard.
Every live request is the exact-commit fetch of a candidate the earlier record
names; no license file, tree, code-search, GraphQL, Sourcegraph, Postman or
SwaggerHub request was made. The guard's own call, wait and cache-hit logs are
committed under [`guard`](guard/). The 92 raw-lane waits are pacing,
not primary-quota waits. The response cache supplied 223 answers,
including cached licence reads; these spend no live request.

| bucket | live requests |
|---|---:|
| code_search | 0 |
| core | 0 |
| raw candidate fetch | 95 |

## Verdicts

`exhausted` decides only the two assigned populations. It does not claim a
new unbounded public search or erase a known handed-off residual. A registered
witness settles its target even where other individually listed candidates
remain unscreened. Persona's eight versions remain outstanding for the header-extension feature;
five recovered nullable-array candidates remain at the screening bound. Each
identity and reason is recorded in `candidates.tsv` and below.

| key | verdict | cover at base |
|---|---|---|
| `client-header-date-format` | `exhausted` | `observatory-client-date` |
| `nullable-array-query-explode-false` | `exhausted` | `observatory-nullable-query` |
| `nullable-query-array-items` | `search-incomplete` | `observatory-nullable-query` |
| `parameter-default-extension` | `exhausted` | `observatory-query-extensions` |
| `parameter-ignore-extension` | `exhausted` | `observatory-query-extensions` |
| `parameter-name-extension` | `exhausted` | `declared-rename-control;observatory-query-extensions` |
| `parameter-without-location` | `exhausted` | `observatory-unlocated-parameter` |
| `query-date-union-oneof` | `exhausted` | `observatory-nullable-query` |
| `required-nullable-query-scalar` | `exhausted` | `observatory-nullable-query` |
| `sdk-variable-parameter-extension` | `exhausted` | `observatory-client-variable` |
| `sdk-variables-extension` | `exhausted` | `observatory-client-variable` |
| `query-array-items-union` | `exhausted` | `query-array-items-union` |
| `query-param-ref-to-enum-or-array-union-converted` | `exhausted` | `query-param-ref-to-enum-or-array-union-converted` |
| `required-param-and-body-defaults-ignored` | `exhausted` | `kiln-firing-curves;required-param-and-body-defaults-ignored` |
| `example-nested-array-two-items` | `exhausted` | `tram-route-query` |
| `query-anyof-const-member-example-as-enum-member` | `exhausted` | `ferry-slot-query` |
| `required-query-array-nullable-union-items` | `exhausted` | `sensor-batch-query` |
| `combo-param-example-beside-ref-schema` | `corpus row 5371` | `harbor-parcel-requests` |
| `security-scheme-header-extension-named` | `search-incomplete` | `meter-reader-gateway` |
| `security-scheme-token-variable-name` | `exhausted` | `grid-valve-console` |
| `security-schemes-duplicate-api-key-header` | `exhausted` | `twin-key-relay` |
| `operation-sdk-group-name-leading-underscore` | `exhausted` | `signal-box-relays` |
| `operation-sdk-group-name-without-method-name` | `exhausted` | `cargo-hold-pallets` |
| `operation-sdk-method-name-sequence` | `exhausted` | `locker-bank-claims` |
| `operation-idempotent-with-root-headers` | `exhausted` | `parcel-courier-desk` |
| `operation-webhook-extension` | `exhausted` | `auction-house-bids` |
| `operation-pagination-offset` | `exhausted` | `ledger-records-offset` |
| `operation-pagination-boolean` | `exhausted` | `beacon-registry-pages` |
| `operation-group-types-beside-child-group` | `exhausted` | `dock-yard-bookings` |
| `webhook-inline-json-body-named` | `exhausted` | `courier-delivery-hooks` |
| `fern-streaming-boolean` | `exhausted` | `streaming-extension-boolean` |
| `fern-streaming-condition-ref-body-header` | `exhausted` | `stream-condition-ref-body-header` |
| `fern-streaming-condition-shared-body` | `exhausted` | `stream-condition-shared-body` |
| `fern-streaming-condition-union-body` | `exhausted` | `stream-condition-union-body` |
| `fern-streaming-format-over-json` | `exhausted` | `streaming-extension-sse-format` |
| `fern-streaming-terminator` | `exhausted` | `streaming-extension-terminator` |
| `base-path-extension` | `exhausted` | `base-path-client-argument;observatory-base-path` |
| `discriminated-extension` | `exhausted` | `greenhouse-undiscriminated-unions` |
| `discriminator-property-name-extension` | `exhausted` | `telescope-renamed-discriminant` |

## Arm verdicts

| key | verdict | arm | cover at base |
|---|---|---|---|
| `parameter-in-path` | `exhausted` | `src/ir.rs::lifted_client_path_parameters[\.map\(\x7cparameter\x7c ClientPathParameter \{]` | `base-path-client-argument` |
| `http-dpop` | `exhausted` | `src/ir.rs::auth_model[=_ => Auth::None,]` | `http-dpop-unrequired` |
| `http-mutual` | `exhausted` | `src/ir.rs::auth_model[=_ => Auth::None,]` | `http-mutual-unrequired` |
| `http-negotiate` | `exhausted` | `src/ir.rs::auth_model[=_ => Auth::None,]` | `http-negotiate-unrequired` |
| `parameter-schema` | `exhausted` | `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*TypeRef::Optional\(element\) => \*element,]` | `nullable-query-union-items` |
| `parameter-in-header` | `exhausted` | `src/ir.rs::header_py_type[=^\s*HeaderType::Date]` | `observatory-client-date` |
| `parameter-in-path` | `exhausted` | `src/ir.rs::lifted_client_path_parameters[if let Some\(variable\) = parameter\.sdk_variable]` | `observatory-client-variable` |
| `parameter-in-query` | `exhausted` | `src/emit.rs::method_params[if let Some\(default\) = &qp\.default]` | `observatory-query-extensions` |
| `parameter-style-form-query-object` | `corpus rows 5370 and 5371` | `src/emit.rs::append_request_call_args[\} else if qp\.convert \{]` | `ore-bin-screen` |
| `parameter-schema` | `exhausted` | `src/ir.rs::InlineHoister::hoist_param_enum[if composition_admits_null\(item, members\) \{]` | `sensor-batch-query` |
| `fern-streaming-extension` | `exhausted` | `src/ir.rs::declare_split_union_body[=tag_types\.push\(TagTypeDecl \{]` | `stream-condition-union-body` |
| `fern-streaming-extension` | `exhausted` | `src/emit.rs::sse_end[=\x7cend\x7c format!]` | `streaming-extension-terminator` |

## Registered witnesses

Row 5370, `happy-hamster`, is the publisher's own description at its full
revision, redistributed under its declared grant. Row 5371, `seldon-wrapper`,
is the pinned archive's Seldon Core wrapper description; its publisher and
origin are declared in the source, and the archive grant is retained. Both
have committed unmodified sources, NOTICE attribution, complete certified
python-enums trees, literals overlays and real compiled-binary golden tests.
Each clean whole-tree comparison is in `comparisons/<source hash>/compare.json`.
The corresponding generation logs are beside it. The historical byte-matching
Automata candidate is the same published API already represented by corpus
row 34; it is not registered twice.

The Seldon `/predict` query declares an example beside a referenced schema.
Its combination proof is co-occurrence, following the existing declaration in
`combination-cooccurrence.tsv`; no new interaction branch is claimed.

Both new golden runs execute 26 of 30 measured regions in the required-query
object conversion arm; [arm-execution.tsv](arm-execution.tsv) records the exact
site. Their implicit default-form objects need named-fixture selector overrides
in the existing reach declaration. The sole authored cover for this arm is
retired in full; the authored example-beside-ref combination cover is removed
while its fixture's other cover remains.

The joined reach store contains 321 real tests (two newly measured and 319
carried) and 53 retained authored fixtures. The manager approved the carry after
the [input audit](carry-input-audit.txt): carried source bytes, golden trees and
generation inputs are unchanged, except the release-only package-version bump.
Each carried entry retains its original measured commit; this is not a claim
that those 319 tests were instrumented again here.

## Handed-off differences

Crozier output is unchanged for every declarer here. New clean comparisons
are grouped below; their complete normalized diffs are committed alongside the
comparison reports. No `default-matched` or `ruling-applied` output decision is
made in this search-only stream.

| root cause | document | files and observed difference |
|---|---|---|
| `declared-body-example-and-numeric-value` | Cloudfoundry custom metrics, `3a8dc3a8efd746de64254da9e8ef7b775f53e59ab6995f056499b42fba580b02` | README, reference and custom-metrics client: the certified pair synthesizes two metric members and `instance_index=1000000`; crozier works the declared metric and `instance_index=0`. |
| `query-worked-value-selection` | Mbus, `d3aacb203499646e297b5bfe04d62342d76435ef086fd51d435c9a77fa08c91c` | README, reference and root client: the certified pair works `address="48"`, crozier `address="x"`; `maxframes` also differs. |
| `query-union-member-nullability` | Cortexware agent-trace, `fa08d30f1984e480be0b413de20bfc6e0c96b90f109067b45d58013ace144c3c` | reference.md: nullable members remain optional inside the certified pair's scalar-or-array union; crozier removes the nested optional types. |
| `inherited-example-field-order` | Cortexware agent-trace, same hash | reference.md: worked ingestion-event fields `id` and `timestamp` precede `body` in crozier and follow it in the certified pair. |
| `empty-object-example-omitted` | Cortexware agent-trace, same hash | reference.md and OpenTelemetry client: crozier omits the certified pair's worked `status={}` member. |

Cloudfoundry also names an unacquired relative `shared_definitions.yaml`; its comparison is over the assigned root bytes, with both generators treating that unresolved schema as unknown. It is not a registration candidate without that reference closure, and no extra file is fetched here.

Previously known declarers and remaining root causes are listed separately in
[`known-declarers.tsv`](known-declarers.tsv). Refusal and registration statuses
are preserved as base evidence; none is relabelled as a new byte difference.
The new production differences have a nonblocking follow-up draft; repairing
them is outside this search.

## Verification

Final commands, results, derived-file reproduction and suppression accounting
are recorded in [`verification.txt`](verification.txt).

## Renewed incomplete search

| key | outcome | outstanding candidates |
|---|---|---|
| `security-scheme-header-extension-named` | `none-registrable` | Eight pinned Persona versions in candidates.tsv need their unacquired relative-reference trees; the authorized population contains only the named root documents. |

## Late recovery of nullable-array candidates

An intermediate `exhausted` verdict for `nullable-query-array-items` incorrectly
rested on historical refusals outside the handed-off set. That verdict is
withdrawn. Thirty source-hash-only rows had been misclassified as decided. Those
historical decisions are withdrawn: one receives the current-pair screen below,
and the other 29 remain unscreened. Nothing more is screened for their already
witnessed targets. Six
nullable-array candidates have immutable locators in earlier committed refusal
records. Those locators were recovered late; all six sources were fetched
through the guard and their exact recorded SHA-256 digests verified. They are
larger than Cellengine and Cortexware, the target's first two current-pair
selections. Under the manager's corrective ruling, the smallest admissible
recovered document takes the target's third and last slot. The remaining five
are individually named in candidates.tsv as incomplete at the bound; an older
refusal is not substituted for a new certified-pair screen.

| key | outcome | outstanding candidates |
|---|---|---|
| `nullable-query-array-items` | `none-registrable` | The recovered candidate table below names the selected document and each remaining document beyond the three-document bound; the handed-off Unicourt residual stays outside this search. |

| source SHA-256 | bytes | immutable locator | current-pair decision |
|---|---:|---|---|
| `5ce68565710ca03a17792aaccccb4949d135632e69898d665aa349dbf710385a` | 1882714 | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/probely.com/main/1.2.0/meta/import/input-bundled.json | selected in the third slot; certified CLI refuses it (two enum-name errors) |
| `6bcb5d3a66421190f4cb701cd5ddd04eaff6426e5a1c0cd2794ec8724ea34ed4` | 1883132 | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/probely.com/main/1.2.0/meta/import/input-entry.json | search-incomplete: beyond the three-document target bound |
| `e9e3e8c2e24db88e950ae00c1faf5cb82e43bd7853ac70d16757ac91dfd7bf45` | 5647749 | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/gcore.com/main/1.0.0/meta/import/input-bundle.json | search-incomplete: beyond the three-document target bound |
| `b8a3425257222511aa6b955b982cf481dad1b77f03614ea3b768b6aa2a770b31` | 18238873 | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/cloudflare.com/main/4.0.0/meta/import/input-entry.json | search-incomplete: beyond the three-document target bound |
| `007fc39ac57873d75305243cee61e5d358c12b975bfbbee6ba0894126e820b0e` | 18238942 | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/cloudflare.com/main/4.0.0/openapi.json | search-incomplete: beyond the three-document target bound |
| `38b1209900e52de20213b0f486937f022f51b9ed814ae19bbdf661e89454a1b7` | 18238953 | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/cloudflare.com/main/4.0.0/meta/import/input-bundle.json | search-incomplete: beyond the three-document target bound |

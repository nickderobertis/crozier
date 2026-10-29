# Interaction search for operation combinations

This bounded search reopens the five operation-owned combinations named on
base `bc66bfb087fbd34abfe89f1075912b103e848896`: one in `parameters`, four in `bodies-responses`, and none
in `naming-clients`. A census declaration alone is not proof. The detector for
each key is its conjunction below **and an instrumented crozier run executing
every declared interaction site**. The authored `beacon-signal-results` fixture now proves the path/body-name
branch and both nullable-response branches. The authored `harbor-relay-registration` fixture carries the inline-body fallback. Registered `steaminputdb` proves the corrected referenced-body branch, as recorded below.

## Populations read

The enumeration and hash audit were taken in preceding dispatch `2858861-4`
on 2026-10-28, starting with the registered corpus. This retry reuses that
recorded population and finishes its screening, rather than repeating acquisition:

| population | files read | OpenAPI 3 | other version or no root OpenAPI marker | unreadable |
|---|---:|---:|---:|---:|
| registered | 977 | 293 | 684 | 0 |
| APIs.guru | 4138 | 1970 | 2168 | 0 |
| GitHub code search acquisitions | 5125 | 4787 | 285 | 53 |
| Sourcegraph acquisitions | 4078 | 2852 | 1209 | 17 |

The registered population is every JSON/YAML file under `tests/fixtures/` at
base `bc66bfb087fbd34abfe89f1075912b103e848896`, including each registered source; generated metadata is
classified separately rather than counted as a specification. No source bytes
changed in this dispatch.

APIs.guru is the complete `APIs-guru/openapi-directory` archive at
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, SHA-256
`816adb9fb4e19dc9ab28d7ad95363de146251fb41164abdb86f953f9f400c644`.
The archive was recovered from the shared HTTP response cache and its digest
verified before extraction. An initial 19-document extraction was superseded
by this complete enumeration; none of the counts above comes from that subset.

Earlier acquisitions are the retained `candidate-documents.json` manifests and
`documents/` trees from the earlier searches. The two retained copies were
compared: after the index's repository exclusions, the second contributes no
additional file. Their 5,657 and 5,210 manifest identities resolve to the 5,125
and 4,078 distinct files above. Every one of those 9,203 files was hashed and
matched its recorded SHA-256 filename; there were no mismatches. Each positive
row in [census.tsv](census.tsv) names its publisher, path and full immutable
revision, retaining aliases that name identical bytes. The preceding searches'
committed acquisition ledgers retain those same identities and hashes.

The retained identity-map snapshot `2858861-4/acquired-identities.json` pins
both acquisition populations: SHA-256
`ecdfa0355116f4c28e5b0768997eedb070d2453aef9668fb77a56ad1817165b5`.
Its two maps contain 5,125 and 4,078 document hashes respectively, each mapping
to the publisher/path/full-revision identities read. This digest is the
population revision; its members are immutable document revisions, not a live
search result set.

No live specification, GitHub, portal or registry request was made for this
search. YAML was first read with PyYAML 6.0.3's C safe loader and JSON with the
stdlib reader. Every unreadable result was retried with the census's own reader
and its normal fallback. [unreadable.tsv](unreadable.tsv) retains the remaining
70 diagnostics; none is counted as a zero declaration. Every parsed document
was evaluated by the repository census's unchanged conjunction evaluator.

## Detectors

The selectors are unchanged from the base. The two read-only interaction
declarations follow the manager-approved corrections recorded below.
Each detector requires both its selector's positive count and execution of its
interaction site in `golden-reach-sites.tsv`.

| key | conjunction | interaction |
|---|---|---|
| `combo-body-property-named-as-path-param` | `operation.requestBody&operation.requestBody:property-named-as-path-parameter` | `rename_claimed_path_params`: the `!overridden && spread.contains(&param.wire_name)` branch |
| `combo-ref-body-read-only-property` | `requestBody.content>mediaType.schema>schema.$ref~>schema.properties>schema.readOnly` | `build`: a dropped body resolves `body_schema.reference`, then `fields.retain` tests `schema_property_is_read_only` |
| `combo-inline-body-read-only-property` | `requestBody.content>mediaType.schema>schema.properties>schema.readOnly` | the declared inline request body's read-only handling site |
| `combo-success-oneof-nullable` | `operation.context:success-nullable&operation.context:success-oneof` | `build_endpoint`: `Some(if dropped_null {` |
| `combo-success-anyof-nullable` | `operation.context:success-anyof&operation.context:success-nullable` | `build_endpoint`: `Some(if dropped_null {` |

## Verdicts

The bounded search uses `search-incomplete` where no registrable reaching witness was found in these populations, and `witness-blocked` for the expressly permitted inline-body fallback. A historical output-sensitive witness is not promoted to interaction proof. `census.tsv` records each declarer and its screening outcome.

| key | verdict | declarers | outstanding evidence |
|---|---|---:|---|
| `combo-body-property-named-as-path-param` | `search-incomplete` | 1256 | none-registrable; authored `beacon-signal-results` reaches all three interaction regions |
| `combo-ref-body-read-only-property` | `search-incomplete` | 731 | proven: registered `steaminputdb` byte-matches and reaches the corrected field-retention interaction |
| `combo-inline-body-read-only-property` | `witness-blocked` | 20 | authored `harbor-relay-registration`, under the manager-approved fallback; [remaining residuals](../witness-search-operation-combinations-bodies-responses/README.md#blocked-witnesses) |
| `combo-success-oneof-nullable` | `search-incomplete` | 24 | none-registrable; authored `beacon-signal-results` reaches both interaction regions |
| `combo-success-anyof-nullable` | `search-incomplete` | 69 | none-registrable; authored `beacon-signal-results` reaches both interaction regions |

### Nullable responses

Scoped golden-only runs over `ebusd`, `deepsearch-ds-v2` and `letta` reproduced
the base's missing interaction reach. A structural screen of all nullable
declarers found no inline union with an explicit null alternative beside at
least two non-null alternatives. The one declaring document the C loader could
not parse was also screened through the census reader: its `/api/auth/me`
response is `anyOf: [$ref UserProfile, null]`, a simple nullable reference.

Three tooling documents instead declare outer `nullable: true` on multi-member
unions: `Rcmade/hono-docs`' example at
`38a1bc9b0f595b9cc0111db34095a820969aeb94`, and two
`OpenAPITools/openapi-generator` resources at
`f81c416b76bcf9baabfb0361a7e94eb3881a2ca4`.
The manager's 2026-10-28 screening ruling classifies each as a tooling example
or converter test resource, not a real-world specification. Each is recorded
with that reason in `census.tsv`; none is a registrable real witness.

| key | verdict | renewed search result | disposition |
|---|---|---|---|
| `combo-success-oneof-nullable` | `search-incomplete` | none-registrable | authored `beacon-signal-results`, both interaction regions reached |
| `combo-success-anyof-nullable` | `search-incomplete` | none-registrable | authored `beacon-signal-results`, both interaction regions reached |

### Path and body name

Every declarer was screened for a selected URL-encoded body naming a component
whose properties include a path parameter's wire name, with that component
also referenced outside this request. The latter includes references from
component schemas, responses, and reuse by another request, exactly as
`non_request_referenced_schemas` records. No document selects that spreading
branch. Documents whose YAML needed the census reader's recovery were screened
separately with that reader; none adds a candidate.

| key | verdict | renewed search result | disposition |
|---|---|---|---|
| `combo-body-property-named-as-path-param` | `search-incomplete` | none-registrable | authored `beacon-signal-results`, all three interaction regions reached |

The fixture was authored from scratch and freshly generated at the certified
pair. Its conjunction counts are one for each covered key. The instrumented
hand-written reach measurement records 3/3 regions for the path/body-name site
and 2/2 for each nullable-response site. The complete generated tree is checked
by `handwritten_fixtures_match_fern_goldens`. It is hand-written evidence, not a
real-specification match.

## Webflow parity

The real Webflow interface was generated before and after the parameter-map
repair and compared through `just fixtures-diff webflow-v2`, using the parity
engine's normalizations. Its measured residual shrank from **83 to 69 files**,
with **14 closed files and no new mismatches**. Only those fourteen paths were
removed from `WEBFLOW_V2.unmatched`; no allowance was added or widened.

`InlineHoister::hoist_parameter_type` now declares structured map values under
`{Request}{Parameter}Value`, including the filter object's nested union types
and the sort-direction enum. The triggering object-map assertion failed with `Dict[str, Any]` on the base
implementation, then passed after the repair; the same regression now drives
the parameter-type wrapper. Its
primitive-map case ensures scalar values still retain their original type.
The IR-module filter passed 209 tests. A structural scan of all 293 registered
OpenAPI documents identified Webflow as the only registered document with a
parameter shape this repair changes.

A second repair gives each endpoint package's own inline declarations
precedence when a type name occurs in several packages. Both annotation imports
and worked-example constructors use that local declaration, retaining the
canonical owner of types declared elsewhere. Its generator regression first
failed because the teams client imported the projects package's declaration;
it then passed, including the check that a root `Counter` type still imports
from the root. The IR and emitter filters passed 334 tests.

Compared with the fresh certified SDK, this closes another **16 files** and
moves the residual from **69 to 53**, with no new mismatches. The scripts clients
and raw client now byte-match. Of the eleven files moved by removing the inline
bodies' `readOnly` flags, only `reference.md` still mismatches: collection-field
union selection, worked examples and a query enum rendered as `Any` remain.
These are parity gaps, not departures. The
[blocked-witness record](../witness-search-operation-combinations-bodies-responses/README.md#blocked-witnesses)
continues to name Webflow and `osf.io`; no allowance was widened.

Fresh generation at Fern CLI 5.163.1 and python-sdk 5.41.3 reproduced all
1,501 committed SDK files byte for byte. The direct generation script leaves
its cache marker out; that marker was restated with the repository's
`expected_state` helper and verified identical to its prior bytes. No SDK
expectation was edited. The preceding reproduction is evidence from dispatch `2858861-4`, before the final two repairs below.

## Referenced read-only body

The structural screen of all 731 declarers selected fourteen candidate documents.
Instrumented runs taken on the preceding dispatch's tree (scratch
`2858861-4/ref-candidate-reach.jsonl`) found five generating documents with
0/1 regions reached: netboxdemo.com/2.8, cadenya, Confluent BYOK, Gobii, and
Google policysimulator. Visma/1.0 reached 1/1, but its document and publisher
record supplied no redistribution grant, so it cannot be registered. Eight
other candidates were refused by crozier; these are **crozier refusals**, not
measurements of certified-pair non-generation. The individual errors and
identities are preserved in `census.tsv`. They do not create a Fern refusal
class. The manager approved the authored-fixture route on 2026-10-28.

| key | verdict | renewed search result | disposition |
|---|---|---|---|
| old content-type-site search | historical `search-incomplete` | none-registrable | superseded by the corrected interaction below |

The fixture is authored from scratch: a relay registration whose input names
one writable field and three server-populated fields. Its referenced body is
used only for that request, so its response-heavy spread reaches the declared
`ep.body_schema_is_open` operand.

### Final Webflow repairs and fallback

The incomplete step's read-only request-example repair is retained: lowering
records `Field.read_only`, and request-example projection omits those fields
while the generated models retain them. Its regression failed before the repair
in the preceding dispatch (`2858861-4/readonly-example-red.log`) and passes
on this tree for both inline and referenced property spellings, preserving a
normal optional field as well as the required field. The unfinished package
scope test now checks the README's actually selected projects endpoint against
its own project field; each endpoint client still checks its own fields and the
absence of the other package's fields.

`InlineHoister::hoist_parameter_type` also retains a single inline `allOf`
string enum as a named query type. The new regression first failed with
`typing.Optional[typing.Any]` (`enum-red.log` in this dispatch's scratch), then
passed for the generated client and reference annotation. A structural screen
of all 293 registered OpenAPI documents found this shape only in Webflow.
The IR filter passed 209 tests. The final emitter filter passed 136 tests,
including the added hoisted-object and discriminated-union read-only cases.
Temporarily removing only the union filter made the latter fail on the emitted
`server_id="server-7"` argument; restoring it made the whole emitter filter green.
That induced-state failure is recorded in `union-red.log`, not claimed as a
result of the finished source.

The normalized Webflow report now has **47 differing files**, down from 53,
with six closed files and no new mismatches. Its `unmatched` list loses exactly
those six paths. One of the eleven inline-readOnly-sensitive files still differs:
`reference.md`. The remaining classes are collection-field union selection,
nested schema versus media example precedence, query example precedence,
optional request-body omission, and string-list samples. Each is named in the
blocked-witnesses section. These independent example heuristics remain outside
the completed repairs, so this dispatch cannot claim a real-specification proof.
On 2026-10-29 UTC the manager directed stopping Webflow repairs at 47 residuals
and taking the task's authorized `witness-blocked` fallback. A follow-up draft
records those five classes. The authored fixture is lower evidence, never a
real-specification match.

The manager also approved declaring the inline interaction site by contract
(a)'s condition chain: `resolve_request_body` first enters
`if !schema.properties.is_empty()`, hoists those fields, and passes them through
`fields.retain` to `.is_none_or(|property| property.read_only != Some(true))`.
That predicate is the newly declared site; the selected combination rows and
all other interaction declarations are unchanged.

The preceding retry (`2858861-7`) freshly regenerated Webflow through the pinned
generation script into a disposable staging tree: all **1,501** SDK files
reproduced the committed golden byte for byte (`fresh-fern.log` in that retry’s
scratch).
The staging tree and temporary screening fixture are removed after generation.

## Intermediate authored measurements

Before the header repair, `harbor-relay-registration` reached **3/3** regions of
the inline retain predicate and **1/1** of the old referenced-body operand.
The latter measurement is historical: the certified byte gate exposed the
incorrect content-type omission it exercised, so it was never an admitted proof. The full
`just handwritten-reach` run first regenerated 117 arm covers and 14
combination sites, including the referenced-body cover. The inline cover was
added afterward. Under the manager's scoped-update ruling, the existing CLI
measured this fixture alone:

```sh
just handwritten-reach --handwritten-dir "$ONEPIPELINE_NODE_SCRATCH_DIR/handwritten-only" \
  --ledger "$ONEPIPELINE_NODE_SCRATCH_DIR/harbor-reach.tsv" \
  --gates "$ONEPIPELINE_NODE_SCRATCH_DIR/harbor-gates.tsv"
```

The input directory contains only a symlink to the committed fixture. This
script then replaced only its rows in the full run's saved ledger. Its
assertions passed: **130 other rows remained byte-identical**, including their
order and line endings. No shared measurement tool or format changed; the
missing scoped-merge option has a follow-up draft.

```python
import sys
from pathlib import Path

baseline, scoped, destination = map(Path, sys.argv[1:])
original = baseline.read_text().splitlines(keepends=True)
measured = scoped.read_text().splitlines(keepends=True)
fixture = "harbor-relay-registration\t"
assert original[0] == measured[0]
assert len(measured[1:]) == 2
assert all(row.startswith(fixture) for row in measured[1:])
other_rows = [row for row in original[1:] if not row.startswith(fixture)]
result = [original[0], *sorted(other_rows + measured[1:])]
assert [row for row in result[1:] if not row.startswith(fixture)] == other_rows
assert len(result) == len(other_rows) + 3
destination.write_text("".join(result))
print(f"Preserved {len(other_rows)} other rows byte for byte; wrote two scoped interaction rows")
```

The script was called with `handwritten-full.tsv`, `harbor-reach.tsv`, and
`docs/openapi-surface/handwritten-reach.tsv`, in that order. Both scratch TSVs
are outputs of the commands above, not edited measurements.

The fresh OSF comparison records **69 common differing files, 425 missing
expected modules, and 26 extra crozier modules** against 583 certified files.
Thus 494 expected files do not byte-match. The old 69 figure omitted missing
paths; it was not evidence of a nearly matching tree. The blocked-witnesses
section now states the full finished-source counts.

The scoped ledger replacement call was:

```sh
python3 "$ONEPIPELINE_NODE_SCRATCH_DIR/merge-scoped.py" \
  "$ONEPIPELINE_NODE_SCRATCH_DIR/handwritten-full.tsv" \
  "$ONEPIPELINE_NODE_SCRATCH_DIR/harbor-reach.tsv" \
  docs/openapi-surface/handwritten-reach.tsv
```

## Output-impact screen

A conservative scan parsed all 293 registered OpenAPI documents. It selected
58 sources: any document with `readOnly: true`, any non-local `$ref` (so a
referenced document cannot hide the flag), or a single-member `allOf` whose
member declares `enum`, `const`, `oneOf` or `anyOf`. An unreadable document
would be included, never treated as negative. Thus the filter can over-include
body schemas and other parameter kinds; it cannot exclude a schema the two
repairs read.

Before/after generation hashes over those candidates changed only Webflow.
Two baseline rendering failures, Atlassian Jira and GitHub, have no certified
golden and supplied no byte-match proof. The offline diagnostic refused remote
loads for Helios and MockServer; their real golden tests are checked
conservatively as well. No source bytes changed and no allowance was widened.
The first broader diagnostic was stopped only after the manager approved its
recorded process tree; no other process was signalled.

## Corrected referenced-body interaction

The authored input was kept unchanged when its complete SDK comparison found
one mismatch: crozier omitted the JSON content-type header for registration,
while the certified pair kept it. A fresh control deleting only the writable
property's description also keeps the header. The new unit regression drives
both shapes and first failed with zero header entries instead of the expected
two (sync and async); removing the incorrect response-heavy omission clause
makes it pass. The complete emitter filter then passed 136 tests.

The conservative clause screen began with every registered source selected by
the output-impact filter and every hand-written fixture. Its necessary IR
conditions are the original clause's guards: response-heavy body, no query or
stream condition, inline lowered request, referenced source, and a false left
operand of the clause's `or`. Earlier header guards are deliberately ignored,
so the screen can only over-include. All broader positive registered corpora
have empty audience lists and default extra-field settings, avoiding a
configuration-dependent body-lowering omission from that screen.

Seven complete registered goldens survive that screen: `apache.org`,
`apache.org-airflow`, `apideck.com-vault`, `bunq.com`, `netbox.dev`,
`paloalto-cspm-reports` and `paloalto-cspm-search-manager`. Each has an empty
`unmatched` list. The new authored fixture is its only hand-written positive.
The two unresolved remote-reference corpora are included conservatively.
Atlassian Jira has no certified golden and remains a non-witness.

All seven registered golden tests passed both before and after the removal,
as did Helios, MockServer and SteamInputDB (ten exact tests in each run).
Thus no registered SDK regressed. The only hand-written change is toward its
certified JSON header; the fixture and its Fern tree were not changed to conceal
the mismatch. The manager approved removing the clause and replacing this
key's site, Selected `why`, and declaration comment.

The genuine interaction is the condition chain in `src/ir.rs::build`:
`if endpoint.body_schema_dropped` selects the lowered body,
`body_schema.reference` resolves its source, and
`fields.retain` calls `schema_property_is_read_only` on each source property.
The new line-only site is that retain predicate. The existing single-feature
read-only evidence already identifies SteamInputDB's omitted `$schema`
arguments. Its complete golden byte-matches. This retry’s scoped instrumented
golden run at commit `ba0dbb016f84` measures the corrected interaction:
SteamInputDB executes every counter region
on the declared retain-predicate line. The scoped report records **6/6**
regions reached. The same preceding retry freshly reproduced all 133
SteamInputDB golden files and generated its literals overlay
(`2858861-7/fresh-steaminput.log`); the source and golden bytes are unchanged
in this retry. This real witness takes precedence over an authored referenced-body
proof; no referenced-body cover remains in the authored fixture.

### CLI build boundary

The first post-removal e2e attempts used a stale `target/debug/crozier`:
`cargo test -p crozier-e2e` rebuilt its library dependency and test harness,
but not that CLI executable. Those post-removal results (`header-repaired-goldens.log`
and the first two recording rounds) are **void as finished-source evidence**.
The unit-test failures and passes used newly compiled library code.

After the repeated finding was surfaced, the manager directed an explicit
`just nx run crozier:build`. The rebuilt executable's timestamp is
2026-10-28 20:57:14 -0600, later than the header source change at 20:26:28.
Fresh comparisons use that executable and separate recording directories;
no result from the stale executable is carried forward as verification.

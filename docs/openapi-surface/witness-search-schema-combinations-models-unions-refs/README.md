# Witness search for schema combinations in models, unions and references

This bounded search covers the twenty-four `models-unions-refs` rows owned by
`prove-schema-combinations` in [combinations.md](../combinations.md). The
certified pair is Fern CLI 5.163.1 and `fernapi/fern-python-sdk` 5.41.3.
Each key is settled one of two ways:

- **Proven:** one admissible registered declarer, whose complete certified-pair
  golden crozier byte-matches, is output-sensitive. Removing the combination's
  feature from it moves the same generated files in both generators.
- **Decided output-insensitive:** the feature moves neither generator's output
  on any document tried, a from-scratch one included. Such a key is decided, not
  proven.

Eighteen keys are proven and six are decided output-insensitive. No owned key
is left unproven.

## The search

Measured on 2026-10-24, without a new specification fetch:

- **APIs.guru:** `APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, read from the shared GitHub
  response cache (archive SHA-256
  `816adb9fb4e19dc9ab28d7ad95363de146251fb41164abdb86f953f9f400c644`, no call made).
- **Registered:** every JSON/YAML document below `tests/fixtures/` at the tree
  this record is committed with. That includes every registered corpus source
  and corpus row 3300, which this search registers.
- **Earlier acquisitions:** the GitHub code-search and Sourcegraph documents
  that the earlier searches' `candidate-documents.json` manifests retain. Each
  is named in `census.tsv` by repository, path and full revision.

Generator-vendor and excluded repositories are dropped before counting, under
the `excluded_repository` / `normalize_repo` contract in
`tools/witness-search/witness-search-github-index.py`. No code search, portal or
registry was queried. Two GitHub requests were made, both through
`tools/witness-search/rate_limit_guard.py` and the shared cache:

- the repository-licence reads in [licences/lookup.json](licences/lookup.json);
- one raw read of row 3300's pinned document, whose bytes equal the acquired
  copy (`168b8aaa…80d7`).

| population | JSON/YAML files read | OpenAPI 3 | other version or no root OpenAPI 3 marker | unreadable |
|---|---:|---:|---:|---:|
| `apis.guru` | 4138 | 1970 | 2168 | 0 |
| `github-code-search` | 5125 | 4787 | 285 | 53 |
| `registered` | 932 | 284 | 648 | 0 |
| `sourcegraph` | 4078 | 2852 | 1209 | 17 |

[unreadable.tsv](unreadable.tsv) keeps every unreadable input with its
diagnostic; none is counted as a zero.

### The detectors

Each detector is exactly its census conjunction (`&` same anchor, `>` object
edge, `~>` local reference), as declared in
`tools/surface-census/openapi-surface-census.py`.

| key | detector |
|---|---|
| `combo-allof-deprecated` | `schema.allOf&schema.deprecated` |
| `combo-allof-nullable` | `schema.allOf&schema.nullable` |
| `combo-allof-nullable-member` | `schema.allOf>schema.nullable` |
| `combo-allof-oneof-member` | `schema.allOf>schema.oneOf` |
| `combo-allof-ref-scalar-default` | `schema.default&schema.allOf>schema.$ref~>schema.type:primary-scalar` |
| `combo-allof-with-required` | `schema.allOf&schema.required` |
| `combo-annotated-ref-to-nullable-target` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.nullable` |
| `combo-anyof-beside-discriminator` | `schema.anyOf&schema.discriminator` |
| `combo-anyof-beside-properties` | `schema.anyOf&schema.properties:non-empty` |
| `combo-array-item-anyof-titled-member` | `schema.items>schema.anyOf>schema.title` |
| `combo-array-item-oneof-titled-member` | `schema.items>schema.oneOf>schema.title` |
| `combo-array-of-nullable-unknown-item` | `schema.items>!schema.type&schema.nullable` |
| `combo-discriminated-inline-members` | `schema.discriminator&schema.oneOf>!schema.$ref` |
| `combo-map-beside-anyof` | `schema.additionalProperties&schema.anyOf` |
| `combo-map-beside-oneof` | `schema.additionalProperties&schema.oneOf` |
| `combo-map-of-anyof` | `schema.additionalProperties>schema.anyOf` |
| `combo-map-of-discriminated-union` | `schema.additionalProperties>schema.oneOf:discriminated-union` |
| `combo-map-of-nullable-values` | `schema.additionalProperties>schema.nullable` |
| `combo-map-of-oneof` | `schema.additionalProperties>schema.oneOf` |
| `combo-nullable-map` | `schema.additionalProperties&schema.nullable` |
| `combo-oneof-beside-properties` | `schema.oneOf&schema.properties:non-empty` |
| `combo-properties-beside-additional-properties` | `schema.additionalProperties&schema.properties:non-empty` |
| `combo-property-ref-to-nullable-target` | `schema.properties>schema.$ref~>schema.nullable` |
| `combo-property-ref-to-read-only-target` | `schema.properties>schema.$ref~>schema.readOnly` |

### Reproducing the enumeration

Select the twenty-four rows above from `witness-search-keys.tsv` into a contract
with its header. Then run `just witness-search-local-census --contract CONTRACT
--all-documents-jsonl --documents SOURCE=DIR` for each population. Join each
positive count to the manifest identities, minus excluded repositories, as
[census.tsv](census.tsv) does. Each `census.tsv` row is one `(source, document)`
declarer with its site count, SHA-256 and screening outcome.

## Verdicts

Every key is `search-incomplete`: these bounded cached populations cannot
exhaust the public population. The declarer count is the key's number of
`census.tsv` rows. Once a key had one admitted, output-sensitive, generating
witness, further declarers keep their recorded screening state.

| key | outcome | declarers | disposition |
|---|---|---:|---|
| `combo-allof-deprecated` | `search-incomplete` | 53 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-allof-nullable` | `search-incomplete` | 376 | proven: registered `onevoice`; the paired removal moves the same files in both generators |
| `combo-allof-nullable-member` | `search-incomplete` | 73 | proven: registered `rapidata-identity`; the paired removal moves the same files in both generators |
| `combo-allof-oneof-member` | `search-incomplete` | 186 | proven: registered `oal-example`; the paired removal moves the same files in both generators |
| `combo-allof-ref-scalar-default` | `search-incomplete` | 142 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-allof-with-required` | `search-incomplete` | 459 | proven: registered `auto-agent-protocol`; the paired removal moves the same files in both generators |
| `combo-annotated-ref-to-nullable-target` | `search-incomplete` | 16 | proven: registered `braintrust-dev`; the paired removal moves the same files in both generators |
| `combo-anyof-beside-discriminator` | `search-incomplete` | 94 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-anyof-beside-properties` | `search-incomplete` | 334 | proven: registered `auto-agent-protocol`; the paired removal moves the same files in both generators |
| `combo-array-item-anyof-titled-member` | `search-incomplete` | 44 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-array-item-oneof-titled-member` | `search-incomplete` | 73 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-array-of-nullable-unknown-item` | `search-incomplete` | 36 | proven: registered `braintrust-dev`; the paired removal moves the same files in both generators |
| `combo-discriminated-inline-members` | `search-incomplete` | 108 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-map-beside-anyof` | `search-incomplete` | 172 | proven: registered `auto-agent-protocol`; the paired removal moves the same files in both generators |
| `combo-map-beside-oneof` | `search-incomplete` | 147 | proven: registered `qredence-fleet-rlm`; the paired removal moves the same files in both generators |
| `combo-map-of-anyof` | `search-incomplete` | 302 | proven: registered `tamoss`; the paired removal moves the same files in both generators |
| `combo-map-of-discriminated-union` | `search-incomplete` | 18 | proven: registered `zoonk`; the paired removal moves the same files in both generators |
| `combo-map-of-nullable-values` | `search-incomplete` | 185 | proven: registered `svix-webhooks`; the paired removal moves the same files in both generators |
| `combo-map-of-oneof` | `search-incomplete` | 228 | proven: registered `subsloth`; the paired removal moves the same files in both generators |
| `combo-nullable-map` | `search-incomplete` | 543 | proven: registered `svix-webhooks`; the paired removal moves the same files in both generators |
| `combo-oneof-beside-properties` | `search-incomplete` | 390 | proven: registered `qredence-fleet-rlm`; the paired removal moves the same files in both generators |
| `combo-properties-beside-additional-properties` | `search-incomplete` | 2673 | proven: registered `eozilla`; the paired removal moves the same files in both generators |
| `combo-property-ref-to-nullable-target` | `search-incomplete` | 588 | proven: registered `openfigi.com`; the paired removal moves the same files in both generators |
| `combo-property-ref-to-read-only-target` | `search-incomplete` | 183 | proven: registered `apideck.com-webhook`; the paired removal moves the same files in both generators |

## How a removal control is taken

Each control deletes one member of the key's conjunction at every matching
anchor, leaving the rest of the document unchanged. Afterwards the census counts
the key at zero in the ablated document. Where both members can be deleted, the
control removes the one whose handling the combination's branch decides: the
union beside a map, the `nullable` on a composition, the `required` beside an
`allOf`. Each control's edited pointers are listed with it.

**Before.** For a registered witness, the committed source and its complete
certified-pair golden. For a from-scratch document, a fresh certified-pair
generation of it.

**After.** One fresh serial certified-pair generation of the ablated document,
under `flock ~/.cache/crozier-run-generation.lock`.

Crozier generates both states. `crozier compare` then holds crozier's ablated
output against the certified ablated tree. The records keep each changed file's
before/after SHA-256 in both engines, the corpus marker excluded.

**Formatting condition.** Every comparison in this record ran under one neutral
condition:

- crozier generated from a fresh temporary working directory, outside crozier's
  repository, so no repository ruff configuration applied;
- the certified pair generated in its own temporary Fern workspace;
- `crozier compare` ran from a temporary directory.

Controls first taken from the repository root were all re-run under this
condition, and the earlier verdicts are not used. Run from inside the repository,
crozier's `ruff format --stdin-filename` call inherits the repository's
`force-exclude` list (`templates`, `docs`) and leaves those packages unformatted.
That is a separate defect, drafted as a follow-up; this node does not change it.

## Proven keys

[paired-removal-comparisons.json](paired-removal-comparisons.json) holds the
eighteen proving controls. In each, crozier's and the certified pair's changed
file sets are equal, and the ablated tree compares with exit 0. Each witness's
corpus golden test passes with `unmatched: &[]`. So the files the combination
writes byte-match in the witness's own golden.

| key | witness | removed | files that move in both generators |
|---|---|---|---|
| `combo-allof-nullable` | `onevoice` | removing the composition's own `nullable` | 1 file: `types/presence_health_response.py` |
| `combo-allof-nullable-member` | `rapidata-identity` | removing `nullable` from the `allOf` members writing it | 1 file: `types/client.py` |
| `combo-allof-oneof-member` | `oal-example` | removing the `allOf` member that writes `oneOf` | 5 files: `types/obj3.py`, `types/obj3stuff.py`, `types/obj3stuff_zero.py` and both `__init__.py` |
| `combo-allof-with-required` | `auto-agent-protocol` | removing `required` beside the `allOf` | 2 files: `types/event.py`, `types/lead_submit_request.py` |
| `combo-annotated-ref-to-nullable-target` | `braintrust-dev` | removing the annotated reference target's `nullable` | 3 files: the evals, experiments and projects raw clients |
| `combo-anyof-beside-properties` | `auto-agent-protocol` | removing the `anyOf` beside non-empty `properties` | 2 files: `types/customer.py`, `types/vehicle_detail_request.py` |
| `combo-array-of-nullable-unknown-item` | `braintrust-dev` | removing `nullable` from the untyped items | 8 files, among them `types/dataset_event.py` and `types/experiment_event.py` |
| `combo-map-beside-anyof` | `auto-agent-protocol` | removing the `anyOf` beside `additionalProperties` | 2 files: `types/customer.py`, `types/vehicle_detail_request.py` |
| `combo-map-beside-oneof` | `qredence-fleet-rlm` | removing the `oneOf` beside `additionalProperties` | 13 files: the settings clients, `reference.md` and the policy types |
| `combo-map-of-anyof` | `tamoss` | removing the map value's `anyOf` | 5 files: `types/tags.py`, `types/tags_value.py`, `webhooks/raw_client.py` and both `__init__.py` |
| `combo-map-of-discriminated-union` | `zoonk` | removing the map value union's member tags | 21 files: the progress clients and their answer types |
| `combo-map-of-nullable-values` | `svix-webhooks` | removing the map value's `nullable` | 3 files: the endpoint clients and `reference.md` |
| `combo-map-of-oneof` | `subsloth` | removing the map value's `oneOf` | 4 files: `types/subtitles_value.py`, `types/subtitles_value_one_value.py` and both `__init__.py` |
| `combo-nullable-map` | `svix-webhooks` | removing the map's own `nullable` | 4 files: the event-type clients, `reference.md` and `types/event_type_out.py` |
| `combo-oneof-beside-properties` | `qredence-fleet-rlm` | removing the `oneOf` beside non-empty `properties` | 13 files (the ablated document is byte-identical to `combo-map-beside-oneof`'s) |
| `combo-properties-beside-additional-properties` | `eozilla` | removing `additionalProperties` beside non-empty `properties` | 7 files, among them `types/input_description.py` and `types/output_description.py` |
| `combo-property-ref-to-nullable-target` | `openfigi.com` | removing the referenced target's `nullable` | 2 files: `types/nullable_date_interval.py`, `types/nullable_number_interval.py` |
| `combo-property-ref-to-read-only-target` | `apideck.com-webhook` | removing the referenced target's `readOnly` | 1 file: `types/webhook.py` |

`combo-allof-nullable-member`'s registered declarers are `hse` and the
Fern-refused `asana.com` and `box.com`. Every `hse` member writing `nullable`
writes `false` beside properties, so removing the field moves neither generator:
it reaches the branch but does not prove it.

The acquired candidates were screened instead (see `census.tsv`), and one
qualifies. RapidataAI's own SDK repository carries an Apache-2.0 `LICENSE` and
publishes `identity.openapi.json`, whose `contacts` property is an `allOf` around
one nullable array. Its candidacy:

- **The certified pair generates it** (complete golden committed).
- **It is output-sensitive.** Removing the member's `nullable` makes the
  `Client.contacts` field required in both generators.
- **It is now registered** as corpus row 3300, `rapidata-identity`, with its
  source bytes, licence (`licenses/rapidata-python-sdk-Apache-2.0.txt`), NOTICE
  entry, golden, literals overlay and e2e gate wiring.

Its two sites are single-member compositions whose member writes `nullable:
true` beside its array shape. They are not bare nullability-only members.

Other acquired candidates were screened out:

| candidate | reason screened out |
|---|---|
| `inconceivablelabs/fabric-api` (MIT) | the certified pair refuses it: `fern generate` exits 1 with nine `Unexpected property` errors in the `listResourceRoots` example |
| two candidates | the repository licence endpoint answers 404 |
| two candidates | a third party's copy of another publisher's specification |
| a further copy of Rapidata's specification | a third party's copy; the publisher's own copy is the one registered |

### How the files were attributed

These proofs are attributed by the paired removal itself, not by a new
golden-reach measurement. The changed files are exactly the ones the feature
writes, the witness's complete golden byte-matches them, and the certified
ablated tree byte-matches crozier's ablated output.

The proven rows' reach cells still read `pending measurement`. They enter
[the reach ledger](../golden-reach.tsv) at the next full `just golden-reach`, a
restatement this node leaves to `reconcile-coverage`.

## Output-insensitive keys

Each key below moves neither generator on every document tried. A from-scratch
document is among them for every key, and crozier matches the certified tree in
both states of each control. Each is a row of
[the shared table](../output-insensitive.tsv) at context `-`, whose complete
before/after maps are the `*-fern.json` and `*-crozier.json` records here. Their
region rows read `gap`: decided, neither proven nor unproven.

| key | documents tried, none moving either generator |
|---|---|
| `combo-allof-deprecated` | groupe-psa and the kiln document |
| `combo-allof-ref-scalar-default` | openfoodfacts-taxonomy-editor (property sites) and the kiln document (a component and a property site) |
| `combo-anyof-beside-discriminator` | marimo (untyped tags) and the kiln document (typed tags) |
| `combo-array-item-anyof-titled-member` | langchain-agent-protocol and the kiln document |
| `combo-array-item-oneof-titled-member` | langchain-agent-server and the kiln document |
| `combo-discriminated-inline-members` | letta, tlon-notes and the glaze-batch document (a lone tagged member and a two-member union) |

[screening-removal-comparisons.json](screening-removal-comparisons.json) records
these real and from-scratch controls with the other screening controls. The
from-scratch documents and their ablations are in
[removal-controls/](removal-controls/):

- `kiln-firing-schedule.yml` holds one site for each of five keys;
- `glaze-batch-tracker.yml` holds a lone tagged `oneOf` member and a two-member
  union, both under written discriminators.

Both are written for this search and are not hand-written fixtures. Each records
a decision, not a proof.

## Repairs

The controls exposed crozier departing from the certified pair; each was fixed
in `src/ir.rs` with unit tests driving the touched function. No golden or Fern
tree was edited and no departure was catalogued.

1. **Untyped tags under a discriminator-less union.** A one-member `enum` tag
   without `type: string` no longer strips the member models' field when a union
   of `$ref`s writes no discriminator (`inferred_strip_discriminant_property`).
   Marimo with its discriminators removed now keeps `ActiveLineNotificationOp`
   and the rest, as Fern does.
2. **A discriminator beside `anyOf`.** A discriminator beside an `anyOf` with no
   `oneOf` strips as though unwritten (`collect_discriminant_strips`). The kiln
   document's typed `result` tags are dropped from its member models in both
   states.
3. **One container inside `allOf`.** A property `allOf` around one inline array,
   map or scalar is that member (`Builder::field_type_ref`). A required field
   loses the description beside it (`annotation_lost_description`); Rapidata's
   `contacts`, `fields` and `capabilities` follow this.
4. **A scalar alias over a lone reference.** A lone scalar `$ref` in a
   component's `allOf`, annotated only beside it, aliases the referenced
   component (`Builder::annotated_scalar_all_of`). The kiln document's
   `TargetCone = ConeNumber` follows this.
5. **Multi-line descriptions.** A description of several lines keeps its opening
   indentation (`clean_doc`, `operation_doc`), as Rapidata's `ExternalAppId`
   enum docstring shows.
6. **The request header of a self-tagged union body.** An inline request-body
   union whose members tag themselves keeps the JSON content-type header without
   a written discriminator (`BodySchemaShape::of`). This is letta's template
   body with its discriminator removed.
7. **A lone tagged member.** A lone tagged inline member is a plain model with or
   without a written discriminator (`Builder::discriminated_union`,
   `Builder::field_type_ref`), and the description beside the one-member union
   is lost. The glaze-batch document shows this.

These ablations exposed three further differences, recorded as drafted
follow-ups because no proof here rests on them:

- an empty `{}` `allOf` member, which Fern ignores;
- a repeated union member after two `allOf` members collapse to one shape;
- variant wrappers lost on annotated copies of an inheritance-spelled union.

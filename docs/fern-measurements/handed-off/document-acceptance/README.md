# Handed-off area: document acceptance

The root causes the three fixture-only witness searches handed off where
crozier refuses or fails to read a document the certified pair (Fern CLI
5.163.1, `fernapi/fern-python-sdk` 5.41.3) generates from, settled at this
node's base `6b4509ab9` and repaired here. Each cause is one row of
[`../document-acceptance.tsv`](../document-acceptance.tsv) and one directory
beside this file, holding its from-scratch `openapi.yml`, the certified pair's
fresh output for it, a `README.md` stating the comparison and the verdict, and
a `runtime.txt` where the verdict rests on a run. The trees are held by
`crates/crozier-e2e/tests/e2e/document_acceptance.rs`.

| root cause | source record | verdict |
|---|---|---|
| [`bare-string-parameter-example`](bare-string-parameter-example/README.md) | bodies and paths | parity-gap-repaired |
| [`R14`](R14/README.md) | operations and extensions | parity-gap-repaired |
| [`crozier-refuses-component-link-ref`](crozier-refuses-component-link-ref/README.md) | schemas | parity-gap-repaired (R14's rule) |
| [`crozier-invalid-duplicate-parameter`](crozier-invalid-duplicate-parameter/README.md) | schemas | parity-gap-repaired |
| [`crozier-refuses-boolean-schema`](crozier-refuses-boolean-schema/README.md) | schemas | parity-gap-repaired |
| [`crozier-refuses-dangling-component-ref`](crozier-refuses-dangling-component-ref/README.md) | schemas | refusal-kept |
| [`crozier-refuses-nullable-error-extension`](crozier-refuses-nullable-error-extension/README.md) | schemas | parity-gap-repaired |
| [`crozier-refuses-path-without-slash`](crozier-refuses-path-without-slash/README.md) | schemas | parity-gap-repaired |
| [`crozier-refuses-type-name-collision`](crozier-refuses-type-name-collision/README.md) | schemas | parity-gap-repaired |
| [`crozier-refuses-unknown-type-value`](crozier-refuses-unknown-type-value/README.md) | schemas | parity-gap-repaired |
| [`crozier-refuses-unreferenced-path-parameter`](crozier-refuses-unreferenced-path-parameter/README.md) | schemas | refusal-kept |
| [`null-info-paths-components`](null-info-paths-components/README.md) | schemas | refusal-kept (also ruling `empty-sdk-refused`) |
| [`never-compared-request-property-name-collision`](never-compared-request-property-name-collision/README.md) | bodies and paths, never compared | parity-gap-repaired |
| [`never-compared-type-name-collision`](never-compared-type-name-collision/README.md) | bodies and paths, never compared | parity-gap-repaired |
| [`never-compared-request-property-camelcase-collision`](never-compared-request-property-camelcase-collision/README.md) | bodies and paths, never compared | refusal-kept |

No row is `default-matched` or `ruling-applied`, and no departure is added or
changed. Every registered corpus golden and every committed hand-written,
probe and measurement document generates byte for byte what it generated at the
base, in both enum modes (crozier at the base and on this branch, run over each
one). No document of the refusal registry's population changes its
`--fern-strict` verdict or class.

## The handed-off documents on the finished tree

Each document below is the one its record names, with that record's revision
and SHA-256 (each re-verified on the bytes compared). Each was compared on the
finished tree with `crozier compare`, every catalogued departure applied,
against the certified pair's tree for those exact bytes from the shared
certified-tree cache (generated there for this node where it was missing).
"Both refuse" means the certified pair's own run exits non-zero, or exits 0
logging `Failed to parse openapi document` over the empty scaffold, and crozier
refuses in default and `--fern-strict` modes.

### Documents whose every listed cause is this area's

| document | revision | SHA-256 | cause | on the finished tree |
|---|---|---|---|---|
| `JHUAPL-DTNMA/dtnma-tools:src/refdm/openapi.json` | `598da6c6793998ea1d845ec32f1e4107c0c4930a` | `de4dc81fea0801628868bb1cb1576f546e8498404f8ad4b94fd65b2bd0d3bef3` | `bare-string-parameter-example` | **byte-matches** |
| `datamodel-code-generator/datamodel-code-generator:tests/data/openapi/multiple_required_any_of.yaml` | `34f144ff3569ef7525c1718a5d818841ed2cc43a` | `37841dac8c168d33cf0951517a242a43f74783a005bba83a76f84b8e5f18cb4e` | `null-info-paths-components` | both refuse (`missing-info-object`, row `refusal-kept`) |
| `swagger-api/swagger-core:modules/swagger-core/src/test/resources/specFiles/petstore-3.0-v2-ticket-3303.json` | `04558121268f1228d88c83291723cee416a990e4` | `f0f99a8ab816418ba331db4071ad5dc64e3397d860864f4e12ad2798e26150e3` | `crozier-refuses-unreferenced-path-parameter` | both refuse (the document has no `info`: `missing-info-object`, row `refusal-kept`) |
| `speakeasy-sdks/bolt-embedded-go:openapi.yaml` | `61fde63b20a4638aed45d9cef13bb702c8d48dd0` | `ddae331c90d254f9fca6e516417ace183f9ee131bf88869098451ea02182d861` | `crozier-refuses-dangling-component-ref` | both refuse (`unresolved-reference`, row `refusal-kept`) |
| `OLeier/IBLeier.VictronEnergy:Monitor/OpenAPIs/VrmApi/VrmApi_BundledReferences.yaml` | `774baffe059489634f310640d004a42a5e28f8fe` | `21f398c40ee6b173dd661fe1435fc565f1f2af277d2098fad3ece22cf2bce77c` | `crozier-refuses-unknown-type-value` | both refuse: the certified pair fails to parse its `#/paths/~1users~1me/get/parameters/0` reference (exit 0 over the empty scaffold) and crozier refuses it as `unresolved-reference` — the schemas record's `crozier-refuses-path-pointer-ref` shape, another area's; the `type` value no longer stops crozier |
| `jentic/jentic-public-apis:apis/openapi/assemblyai.com/main/1.3.4/meta/import/input-bundle.json` | `c72e13e0f80e71997209aba985eff6ef34869cd7` | `2011299d2095426af64fdf2209daa58c58152a09d34980717a048cf406b67a87` | `R14` | generates; 63 files differ, attributed [below](#assemblyai) |
| `atacan/AssemblyAI:openapi.yaml` | `ed31d2fbb08b69633e7d1bcc31bc4cf8eacc8718` | `b306bf4455446eb3bc38f0e687888206b017b5e89c6047a5592e2fbdd88160b7` | `crozier-refuses-component-link-ref` | generates; 53 files differ, [below](#assemblyai) |
| `atacan/AssemblyAI:original_openapi.yaml` | `ed31d2fbb08b69633e7d1bcc31bc4cf8eacc8718` | `10ca68affcc55d46649da53ca342ee804c56af96b0a963d584562c8b21e20824` | `crozier-refuses-component-link-ref` | generates; 53 files differ, [below](#assemblyai) |
| `tryAGI/AssemblyAI:src/libs/AssemblyAI/openapi.yaml` | `1028f8b61cda3f1dc8777d732093fd3e4558d9c9` | `215ec23ddd849ffd78349383788255dfeb417532c81f6dc5c2cdd6b5c577ab02` | `crozier-refuses-component-link-ref` | generates; 58 files differ, [below](#assemblyai) |
| `plaid.com/2020-09-14_1.345.1` (APIs.guru) | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `79291d99cc1de9909805841b30b2795b8c9327563d76b94d37a2df3733176bda` | `crozier-refuses-nullable-error-extension` | generates; 9 files differ |
| `Azure-Samples/digitization-of-piping-and-instrument-diagrams:docs/webapi-swagger.yaml` | `c51302e3ec34147c676ef6eedbdd7551ea908b05` | `4f917fb1f4dd02c8b787af9d37e859c543b51a05ad56136af0eef59543dcf165` | `crozier-refuses-path-without-slash` | generates; 2 files differ |
| `mithileshchellappan/pushboy:docs/openapi.yaml` | `688123d556fe2895a1578a233f993158317c40b0` | `4ff659431c74aa0959d933e61be266448bcfb6367fad745fd94b4313041ebcec` | `crozier-invalid-duplicate-parameter` | generates; 3 files differ |
| `pAI-OS/paios:apis/openai/openapi.yaml` | `b65d858f12c1da472176829af4b533a9e7c246e2` | `413656b4a262ac7a49ea37f30ef4d8e1a1f3785fb6d85a7aaca4c054e9299fb8` | `crozier-refuses-type-name-collision` | generates; 14 files differ |
| `membrane/api-gateway:core/src/test/resources/openapi/specs/oas31/boolean-schemas.yaml` | `c24a0204aaa9d07ee5237c44e43e8e9ef4129f2c` | `8340f5da585023194c7154cb6e72a111e5643bb9cd3364cb75e0eacb0b1fcb89` | `crozier-refuses-boolean-schema` | generates; 3 files differ |

`jentic/jentic-public-apis:apis/openapi/assemblyai.com/main/1.3.4/meta/source/source.dat`
at the same revision is the AssemblyAI bundle's raw source, not a document as
is (the operations-and-extensions record says so); it was not compared.

### Documents never compared with the certified pair

The eleven documents the bodies-and-paths record lists under *crozier failures
never compared with the certified pair*, now each generated by the certified
pair. Where the certified pair refuses too, the refusal is shared and is no
root cause; the three it does not share are this area's `never-compared-*`
rows.

| document | revision | SHA-256 | the certified pair | crozier on the finished tree |
|---|---|---|---|---|
| `fossology/FOSSology.REST.dotnet:openapi/FOSSology REST API 1.6.2.yaml` | `b362ec94ddf8ab6da0f8606183dfc2bc79b157b9` | `7da1db69e60df38ffa4ae477eee68eab2e29932dad65de682d4d22bac71b9872` | generates | generates (`never-compared-request-property-name-collision`); 10 files differ |
| `jentic/jentic-public-apis:apis/openapi/cloudbeds.com/main/v1.3/openapi.json` | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `8724cc349f5f6c3835b0c45e8b17b15807ac17fed862354b479c584d08cb319c` | refuses (exit 1, `enum-name-unsuitable`: `Сunion`) | refuses (`type-name-collision`) — shared refusal under another class |
| `konfig-dev/konfig:sdks/db/intermediate-fixed-specs/peach-payments/openapi.yaml` | `bec3d36b9a341f30707a4ab3d9de6c4154809ada` | `adc6eff9c74263a89fe32f9ed7fcffac14d86055a602d7cb9494934b4524f67c` | refuses (exit 1, `PaymentResponse is already declared`) | refuses (`type-name-collision`: `PaymentResponse`) |
| `konfig-sdks/openapi-examples:peach-payments/openapi.yaml` | `161ab49c45e45825ca3832945c59a3ba904321ba` | `d7497fa8a725dfea1f77f5c50653f3ee1d9d866e27b1592b6f6c7911ea77f972` | generates | generates (`never-compared-type-name-collision`); 12 files differ |
| `prometheus/prometheus:web/api/v1/testdata/openapi_3.1_golden.yaml` | `ea954809ceafceb53ecfa295ab0947753929de9e` | `76fb085db4bfd0d30515cd7a45d345997bf9dfb1d3e6a51aa74c852574ccd437` | refuses (exit 1, `ruff check` fails) | refuses (`generator-lint-failure`) |
| (bytes only, no recorded provenance) | — | `072f630295a0a00fdf0b613dd33a7297686c489e247ceec447ad18d0e387eaab` | refuses (exit 1, `enum-name-unsuitable`) | refuses (`enum-value-unnameable`) |
| (bytes only, no recorded provenance) | — | `60784093c680e6a4364097d78a1b8406b09a9c1656fbfe16c8491d75eb5a1fd6` | refuses (exit 1, `enum-name-unsuitable`) | refuses (`enum-value-unnameable`) |
| `shikorism/tissue:openapi.yaml` | `34abc826977006d68ee8da515b40a57935fd8fcb` | `ba4127ea2b1b0d50a0f501286dbffa0e5c4297a7ea806a1f133169b962dab8e0` | refuses (exit 1, `ruff check` fails on an empty method name) | refuses (`generator-lint-failure`) |
| `OWASP/crAPI:services/chatbot/src/resources/crapi-openapi-spec.json` | `b5fc307f3e5f875809b095b771108ef342a33724` | `8d16b09f329e7372db703dc8a95d7ef2f7e53deb3ff19a75e604ec6d3b84e09b` | refuses (exit 1, `ApplyCouponRequest is already declared`) | refuses (`type-name-collision`) |
| `lightning-rod-labs/lightningrod-python-sdk:openapi/openapi-docs.json` | `7e6a5d0f91ee29842f8f32c2ffea49ec397f1656` | `7d19c17a5221a635e78463a780a822f2593d6f126226c29255158ccce88e567c` | refuses (exit 1, `MppTopupRequest is already declared`) | refuses (`type-name-collision`) |
| `api-platform/schema-generator:tests/e2e/openapi.yml` | `22635fbacac8011c73cdbbb5c20507c77c02d89d` | `978fbacd3483f78d34c90ff71bdc8429223ef8409e531b4960cb0c78dec31206` | refuses (exit 1, `request-property-camelcase-collision`: `book`, `book[]`) | refuses (`request-property-camelcase-collision`, row `never-compared-request-property-camelcase-collision`), where it wrote a call passing `book` twice |

## What still differs, and why

Every document above that generates got past this area's cause and now meets
others the records never measured on it, because crozier refused or failed to
read it first. [`residuals.tsv`](residuals.tsv) attributes **every** remaining
differing file of those eleven documents (280 files: 124 differ, 78 only the
certified pair writes, 78 only crozier writes) to one or more named root
causes, by document SHA-256 and path; each attribution was checked against that
file's own diff lines. None is a cause of this area.

### Causes another area's record names

| cause (record) | what it explains here |
|---|---|
| `example-value-source` (bodies and paths) | worked-example values in plaid, paios and peach-payments snippets |
| `example-optional-members` (bodies and paths; ruling `minimal-worked-call`) | the AssemblyAI READMEs, `reference.md` and `transcripts/client.py` working optional parameters into the call |
| `example-presence` (bodies and paths) | paios' bare `create_image_variation(...)` and image call, AssemblyAI's `files.upload` example, FOSSology's file-upload example in `reference.md` |
| `allof-description-wrapper` (bodies and paths) | plaid's `recurring_transfer_nullable.py`, `simulated_transfer_sweep.py` (an `allOf` of a `$ref` and a nullable-only member) |
| `readme-endpoint-choice` (bodies and paths) | the Azure README's demonstrated call |
| `union-modelling` (bodies and paths) | paios' fine-tuning integration union files |
| `parameter-type-resolution` (bodies and paths, its `items: false` arm) | membrane's `reference.md`, `client.py`, `raw_client.py` |
| `request-content-type-header` (bodies and paths) | the AssemblyAI `transcripts/raw_client.py` explicit header |
| `multipart-scalar-union-part-encoding` (schemas) | paios' `audio/raw_client.py`, `images/raw_client.py` |
| `mistyped-scalar-example` (schemas) | peach-payments' `amount` example |

### Causes newly named here: unrepaired, measured residuals

No source record names these eleven; each is **an unrepaired, measured
residual**, named here under the planner's ruling, with the follow-up draft
*Settle the causes the document-acceptance repairs surfaced on newly generated
real documents* naming every one. Only `allof-required-parent-field` lies in code this node
changes, and it is not small (below); the rest are output-parity repairs in
code this node does not touch.

- **`group-placed-nested-type-placement`** — a component its
  `x-fern-sdk-group-name` places in a group's package keeps its nested inline
  types in that package in the certified pair and at the root in crozier.
  Explains 198 files of the four AssemblyAI documents (every
  `lemur/types/*`/`transcripts/types/*` model and `__init__.py` it touches, the
  type files only one side writes, the clients' imports).
- **`enum-member-digit-separator`** — an enum value whose digits are separated
  by `-` (`claude-3-5-sonnet`) is `ANTHROPIC_CLAUDE3_5_SONNET` in the certified
  pair and `ANTHROPIC_CLAUDE35SONNET` in crozier. Explains
  `lemur/types/lemur_model.py` in three AssemblyAI documents.
- **`typed-single-ref-allof-alias`** — a `type: object` schema whose only other
  content is `allOf: [$ref …]` is an alias in the certified pair and a subclass
  in crozier. Explains 13 files of the four AssemblyAI documents
  (`lemur_action_items_response.py`, `lemur_summary_response.py`,
  `lemur_task_response.py`, `redacted_audio_notification.py`).
- **`x-fern-type-extension`** — `type: string` with a `pattern` and
  `x-fern-type: datetime` is `dt.datetime` in the certified pair, which reads
  the extension, and `str` in crozier. Explains `transcript_list_item.py` in
  the four AssemblyAI documents.
- **`description-trailing-whitespace`** — the certified pair keeps a
  description's trailing space in a docstring; crozier trims it. Explains
  plaid's five `*_account_subtypes.py`.
- **`multipart-json-string-part-encoding`** — a multipart part
  `type: string, format: json-string` is JSON-encoded by the certified pair and
  sent as is by crozier. Explains the Azure `pid_digitization/raw_client.py`.
- **`allof-oneof-ref-variant-field-order`** — an `allOf` of a `$ref` target, an
  inline object and a `oneOf` of `$ref` scopes orders its fields differently
  (the certified pair puts the scope's after the target's). Explains pushboy's
  `types/live_activity_end_job_request.py`,
  `types/live_activity_update_job_request.py`, `live_activity/client.py`.
- **`urlencoded-allof-body-fields`** — a form-urlencoded body that is an
  `allOf` of a `$ref` and an inline object: crozier drops its fields (as at the
  base), the certified pair spreads them. Explains FOSSology's
  `auth/client.py`, `auth/raw_client.py`, `README.md`, and part of
  `reference.md`.
- **`allof-required-parent-field`** — a `required` list of an `allOf` body (the
  outer schema's or an inline member's) naming a parent's property makes it
  required in the certified pair, which also lists it first in `reference.md`
  and works it into the call; crozier keeps it optional. Explains FOSSology's
  `license/client.py`, `license/raw_client.py`, `user/client.py`,
  `user/raw_client.py` and part of `reference.md`. It sits in the `allOf` body
  lowering this node added; a first repair making the field required was
  measured (a `required: [name]` variant of
  `never-compared-request-property-name-collision`) and reverted because the
  ordering and worked call still differed.
- **`body-properties-beside-oneof`** — a multipart file property declared beside
  a `oneOf` of `$ref`s is left out by the certified pair and taken by crozier.
  Explains FOSSology's `report/client.py`, `report/raw_client.py`.
- **`inherited-inline-enum-naming`** — an inline enum a subtype inherits is
  named after the declaring base by the certified pair and after the subtype by
  crozier, and a redeclared `status: {type: string, default: …}` is the base's
  enum in the certified pair and `str` in crozier. Explains peach-payments'
  webhook models, their enum files and the two `__init__.py` (9 files).

## Reproducing

The certified-pair trees of the real documents are in the shared cache under
`${XDG_CACHE_HOME:-$HOME/.cache}/crozier/certified-trees/fern-5.163.1_python-5.41.3/<sha256>/python_enums/`.
Each comparison is `crozier compare` over a config whose `reference.command`
copies that entry's `tree/`, with `package-name: fern` and `project-name:
default_package_name`, as the certified pair names them.

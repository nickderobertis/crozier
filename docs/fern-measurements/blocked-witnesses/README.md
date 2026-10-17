# Handed-off witness comparisons on the finished tree

These are public publisher specifications that earlier fixes screened but could
not register while other shapes differed. [`witnesses.tsv`](witnesses.tsv) lists
every one, with its immutable revision and source SHA-256. Each was fetched at
that revision, and its bytes were checked against the recorded digest. Fern CLI
**5.67.1** with `fernapi/fern-python-sdk` **5.20.0** then generated it afresh,
and crozier compared its output from the finished generator, through the shared
departure engine. Fern generated every one. The table retains only witnesses whose fresh
comparison exits **3**. Vocode now compares with exit **0**, so its closed row
and empty diff are retired; its exact source provenance is retained below.
None enters an `unmatched` allowance.

Each `<witness>.diff` is that witness's complete normalized comparison: `-` for
Fern, `+` for crozier, with every remaining file and changed line.
[`residuals.tsv`](residuals.tsv) attributes **every hunk** of every diff exactly
once. It names the file, the hunk (`-start,count +start,count` on the Fern and
crozier files, or a one-sided file), the owning scenario shape of the
[scenario proof index](../../openapi-surface/scenario-proof-index.tsv) or
`unowned`, and the OpenAPI construct with what each side writes.
`tools/surface-census/scenario-proof-index.py check` reads the hunks from the
diffs themselves. It fails when a hunk is unattributed, attributed twice, or
attributed to a shape the index does not hold, so a re-measured diff cannot
leave this table behind. `scenario-proof-index.py hunks <diff>` prints a diff's
hunks in the table's spelling.

An `unowned` hunk is a generator residual that no scenario of the plan covers. A
hunk that names a scenario comes from that scenario's own trigger: the committed
proof matches its fixture, but this real document still differs. That scenario
counts as closed on its fixture only, with this residual open in the index's
`open` cell. Neither kind counts as matched.

## Reproduction

Use the workspace scaffold of `tools/fern-goldens/generate-fern-fixture.sh`
(Route A): organization `fern`, package `fern`, project `default_package_name`,
and generator setting `pydantic_config.enum_type: python_enums`. Place the
workspace outside a Git checkout, or set `GIT_CEILING_DIRECTORIES` to its
parent, so that Fern records no origin commit. Then run:

```sh
fern generate --group python-sdk --local --preview --output ../preview --force
crozier compare crozier.yml --json report.json --diff-dir diff
```

`crozier.yml` names the workspace document as `spec`, the names above, and the
reference command `cp -R preview/fern-python-sdk/. "$CROZIER_REFERENCE_OUTPUT"`.

## dystore

One cause. The tag `⚠️ Not supported yet` is spelled with its raw emoji in
Fern's `reference.md` calls, links and imports, although Fern's own Python uses
the identifier-safe `not_supported_yet`. crozier writes the identifier-safe
spelling everywhere. This is a candidate Fern defect, but no departure entry
claims it, so it remains `unowned`.

## kompaz

Two residual causes remain: `OrganizationLogo` tag/prefix folding and the
multipart example hunks that cause prevents the existing departure from
admitting. The three problem+json error-body models and their exports now match.
The root import-order row also closes: with identical imported name sets, the
existing `init-type-checking-import-order` rule admits it.

## langchain

The `stream_mode` array-item enum modules, aliases and exports now match.
The remaining causes are the collapsed `assistant_id` description, variant
constructors in the `post_a2a` example, the `runs/batch` content-type header and
the `kwargs_` enum visitor callback. The root import-order row also closes under
`init-type-checking-import-order` once the imported name sets agree.

## rice-shower

The nested const-only `stopReason` aliases, enum modules and exports now match.
The `channels` query-array examples and `createSystem` nullable `location`
description remain residuals.

## speech-ai

Every certified public client method is exposed (112 sync/async methods and
resource accessors), including the SSML, OpenAI speech and transcription
operations. The one-member allOf bodies now match. Only the STT multipart
`format` field serialization remains, owned by parity-naming-wire's
`multipart-optional-enum-part-plain-field` difference.

## supabase

The nullable `JsonValue_Output` union member now keeps its `Optional`, and the
urlencoded `grant_type` parameter reuses `OAuthTokenBodyGrantType`; the extra
operation enum, its module and its exports are gone. The root import-order row
also closes under `init-type-checking-import-order` once the imported name sets
agree. The remaining example and naming differences retain their individual
attributions in `residuals.tsv`.

## Import boundary

The six generated SDKs were installed as real packages under Python 3.14.7 and
Pydantic 2.14.0. Every relative import resolves to a module the package contains.
Vocode, speech-ai, langchain, kompaz and rice-shower import every module cleanly.

Supabase's root package and standalone `JsonValueOutput` alias import cleanly,
but eleven modules constructing models over the implicit recursive JSON alias
graph raise `RecursionError`. The same eleven imports fail in the SDK generated
from merge base `19c121ed7` and in freshly generated certified output. This is a
preexisting runtime incompatibility, not a departure used to admit the owned
nullable union-member difference. All other Supabase module imports pass.

The eleven are `fern.billing.client`, `fern.billing.raw_client`,
`fern.domains.client`, `fern.domains.raw_client`, and the seven
`fern.types.list_project_addons_response_output*` and
`fern.types.update_custom_hostname_response_output*` models. They fail the same
way under Pydantic 2.9, 2.10 and 2.11 on Python 3.12, and with the alias's
member written without `Optional`. Supabase's import boundary is therefore its
root package, every module outside the `JsonValueOutput` alias graph, and the
static resolution of its relative imports. Making the alias importable is a
catalogued recursive-alias departure across every golden with such an alias,
which keeps the declared Python 3.8+ support; it is follow-up work, not this
comparison's.

## twitter

One cause, `unowned`. The first named media example of `statuses/update` is an
empty `media_ids` array. Fern treats it as absent and uses the schema example,
while crozier writes `[]`.

## vocode

The complete fresh comparison matches: **exit 0**, 354 files compared. All
128 certified public client methods and resource accessors are exposed,
including `buy_number`. Its flattened request types and exports, and the
flattened variants' `action_trigger` references, match without an allowance.

Source: `vocodedev/vocode-core:docs/openapi.json` at revision `e054c33a72787b6a4920f91eb8598ad0bafb4240`.
Source SHA-256: `ffca17c004e206072f4b71307c83bdcf9fe3f8ba3cf56f16825136ccbaf801f6`.
Fern CLI 5.67.1 with fernapi/fern-python-sdk 5.20.0 generated the reference;
the packaged scaffold in the reproduction section above applies unchanged.
This source is a registration candidate, not a registered corpus golden. Its row is retired
from the blocked set rather than given a false `differs` status or a new table
status. Corpus admission can proceed separately.

# Handed-off witness comparisons on the finished tree

These are public publisher specifications that earlier fixes screened but could
not register while other shapes differed. [`witnesses.tsv`](witnesses.tsv) lists
every one, with its immutable revision and source SHA-256. Each was fetched at
that revision, and its bytes were checked against the recorded digest. Fern CLI
**5.67.1** with `fernapi/fern-python-sdk` **5.20.0** then generated it afresh,
and crozier compared its output from the finished generator, through the shared
departure engine. Fern generated every one. Every comparison still exits **3**,
so each witness is blocked, not a corpus match. None is registered, and none
enters an `unmatched` allowance.

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

One cause, `unowned`: three `application/problem+json` component responses.
Fern hoists them as unused `*ErrorBody` models, and crozier emits none of them.

The `OrganizationLogo` tag's `organizationLogo.*` operations now match: the
`organizationlogo` group, its `Organizationlogo` heading and the
`show`/`update`/`destroy` methods. With that file otherwise equal to Fern's, the
catalogued `multipart-object-required-file-example` correction applies to the
`PUT /organizations/{organization}/logo` docstring examples. The root
`__init__.py`'s reordered `.auth`, `.client` and `.environment` imports are
taken by the catalogued `init-type-checking-import-order` departure; the
`*ErrorBody` names beside them stay that cause's.

## langchain

Three causes, all `unowned`:

- the inline `stream_mode` item enum, which Fern hoists as `*StreamModeZeroItem`;
- the description of `assistant_id`, a collapsed two-string `anyOf`, which Fern
  omits;
- the variant constructors in the `post_a2a` example's union items.

The `content-type` header on the titled array body of `runs/batch` and the
`kwargs_` enum visitor callback now match. The root `__init__.py`'s reordered
`.client` import is taken by the catalogued `init-type-checking-import-order`
departure; the `*StreamModeZeroItem` names beside it stay that cause's.

## rice-shower

Three causes, all `unowned`:

- The const-only `stopReason` `anyOf` nested in a nullable `anyOf`. Fern hoists
  it to a union alias over four one-value enums, written as 30 Fern-only
  modules; crozier inlines it.
- The `channels` query array examples.
- The request-field description of `createSystem`'s nullable `location`.

## speech-ai

One cause, `unowned`: one-member `allOf` request bodies on `POST /v1/ssml`
and `POST /v1/audio/speech`. Fern keeps both operations and flattens the
referenced object. crozier drops them, together with the `open_ai_api` and
`ssml` clients, and writes the components as standalone types.

The nullable enum-`$ref` multipart part `format` now matches, sent as a plain
form field.

## supabase

Seven causes are `unowned`:

- the example of the `branch_id_or_ref` `anyOf` path parameter;
- component `example`s on array, object and form request bodies;
- `OAuthTokenBody`'s operation-level enum hoisting;
- `reference.md`'s parameter list for JSON-beside-binary function bodies;
- missing commas in a map-of-objects example.

The root `__init__.py`'s reordered `.client` and `.environment` imports are
taken by the catalogued `init-type-checking-import-order` departure; the
operation-scoped `V1ExchangeOauthTokenRequestGrantType` re-export beside them
stays the `OAuthTokenBody` cause's.

The `file=["example_file"]` docstring lines in `edge_functions/client.py` are
the catalogued multipart file-example correction. The engine cannot apply it
while the `BulkUpdateFunctionBody` component-example difference sits in the same
file, so they belong to that cause.

Two causes fall on scenarios' own triggers. Their proofs match their fixtures,
and each is open in the index:

- `text-response-drops-request-example`: optional query examples on a
  text-only response.
- `union-member-nullability-dropped`: a nested hoisted nullable member that loses
  `Optional`.

## twitter

One cause, `unowned`. The first named media example of `statuses/update` is an
empty `media_ids` array. Fern treats it as absent and uses the schema example,
while crozier writes `[]`.

## vocode

Two causes, both `unowned`:

- The one-member `allOf` request body of `POST /v1/numbers/buy`. Fern keeps the
  operation and flattens the component. crozier drops it, together with the
  numbers client, and relocates the body's types.
- The one-member `allOf` property `action_trigger` inside flattened
  discriminated-union variants. Fern types it as the referenced component;
  crozier names variant-specific types that it never writes.

The environment difference that `server-name-extension-ignored` owned no longer
reproduces.

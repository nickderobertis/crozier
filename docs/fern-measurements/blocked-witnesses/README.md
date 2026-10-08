# Handed-off witness comparisons on the reconciled generator

These are public publisher specifications that earlier fixes screened but could
not register while other shapes differed. They were generated afresh with
Fern CLI **5.67.1** and `fernapi/fern-python-sdk` **5.20.0**, then compared with
crozier **0.0.106** using the shared departure engine. No generator source has
changed during reconciliation. All eight comparisons exit **3**; they are
blocked witnesses, not corpus matches. The attached normalized diffs enumerate
every remaining file and changed line, with `-` for Fern and `+` for crozier.

The owners below are shapes in the separate follow-on scenario plan. They are
not additional rows or proof claims in the repair index. A shape with a scenario
id is named by that id; an additional combination is described directly.

## Reproduction

Fetch each immutable publisher document below, then use the workspace scaffold
of `tools/fern-goldens/generate-fern-fixture.sh` (Route A): organization `fern`, package
`fern`, project `default_package_name`, generator setting
`pydantic_config.enum_type: python_enums`. Run:

```sh
fern generate --group python-sdk --local --preview --output ../preview --force
crozier compare crozier.yml --json report.json --diff-dir diff
```

`crozier.yml` supplies the authored workspace document as `spec`, the names
above, and reference command `cp -R preview/fern-python-sdk/. "$CROZIER_REFERENCE_OUTPUT"`.
The workspace is outside a Git checkout (or its parent is
`GIT_CEILING_DIRECTORIES`), so local Git metadata cannot create a spurious
comparison difference. These runs generated successfully before comparison.
NetGSM generated and compared with exit 0 and is now corpus row 332; Waylay
already has row 329 and its catalogued body/query correction.

## kompaz

Publisher revision: `Stichting-KOMPAZ-1/KOMPAZ-web-frontend:openapi.json@a847053e46b98324c57183af2b2c09abe01f8ecf`. Source SHA-256: `0437ad48ef2e96fae47e804e86333cbf76ad6a280918373a9f479f9646240511`.

Remaining differences: Operation-name tag-prefix normalization; mixed-case group headings; range-status-only error model retention.

Owner: Follow-on scenario plan: tag-prefix normalization, mixed-case group heading, range-status error components.

Exact comparison: [kompaz.diff](kompaz.diff), **74** files compared, **5** differing, **3** Fern-only, **0** crozier-only.

## langchain

Publisher revision: `langchain-ai/docs:src/langsmith/agent-server-openapi.json@264fdf88d3fc53d5d2397fadf3b6dba36b95dd0e`. Source SHA-256: `25903f3bc462fdf43558e46ba3c72118aaff32cc30a2730336e53382bf43667e`.

Remaining differences: Nested array-item union aliases and model exports; raw versus tagged-model example values; nullable member descriptions; streaming request content-type; root import ordering; callable-field kwargs spelling; stream example parentheses.

Owner: Follow-on scenario plan: nested array-item union hoisting, nullable-anyof-member-description-dropped, stream-condition-ref-body-json-header-dropped, example-imports-case-insensitive-order, callable-field naming and stream snippet layout.

Exact comparison: [langchain.diff](langchain.diff), **241** files compared, **20** differing, **5** Fern-only, **0** crozier-only.

## speech-ai

Publisher revision: `lenML/Speech-AI-Forge:docs/openapi.json@a41b70abba866ecded6e1e90beea6cc68e3fd0ae`. Source SHA-256: `1ae1ec5faa3031d10996730f4dfda9726b828ef3a9bd8554d77adcd4ba1b32f6`.

Remaining differences: One-member composed JSON bodies lose whole groups; optional binary multipart values are sent as form data rather than files; JSON multipart parts lack annotation conversion.

Owner: Follow-on scenario plan: request-body-ref-to-alias-component-drops-operation, multipart-nullable-binary-anyof-not-a-file, multipart-inline-object-part-json-encoded.

Exact comparison: [speech-ai.diff](speech-ai.diff), **110** files compared, **7** differing, **4** Fern-only, **2** crozier-only.

## rice-shower

Publisher revision: `Q2TM/low-temperature-control:apps/rice-shower/docs/openapi.yaml@b100b3633a68a41ba63181379455e98b4814da19`. Source SHA-256: `0a43b3181f2fd75a20a15bae6169a1c09f495916fdc697cd4584198cb0355741`.

Remaining differences: Nested untagged object union aliases/models are absent (six stop-reason families); optional query arrays appear in examples; nullable property descriptions differ; systems request-field descriptions differ.

Owner: Follow-on scenario plan: nested untagged object-union hoisting, optional query-array examples, nullable-anyof-member-description-dropped, nullable request-field descriptions.

Exact comparison: [rice-shower.diff](rice-shower.diff), **157** files compared, **13** differing, **30** Fern-only, **0** crozier-only.

## vocode

Publisher revision: `vocodedev/vocode-core:docs/openapi.json@e054c33a72787b6a4920f91eb8598ad0bafb4240`. Source SHA-256: `ffca17c004e206072f4b71307c83bdcf9fe3f8ba3cf56f16825136ccbaf801f6`.

Remaining differences: One-member composed request body drops numbers operations and relocates body types; environment ignores the server-name extension; inherited action-trigger properties reuse one component type in Fern but use variant-specific types in crozier.

Owner: Follow-on scenario plan: `server-name-extension-ignored` owns the environment difference; the allOf-wrapped request-body operation omission and inherited property type reuse are separate shapes owned by that plan, without confirmed scenario ids.

Exact comparison: [vocode.diff](vocode.diff), **358** files compared, **14** differing, **5** Fern-only, **4** crozier-only.

## supabase

Publisher revision: `supabase/supabase:apps/docs/spec/api_v1_openapi.json@36371de15127206280d2d40786e8578dfe1b681a`. Source SHA-256: `0a1a19774d3749e84d2e2c2896006c58e4b67779d8cc2806f3135488fc7fb1dc`.

Remaining differences: Example selection differs for path parameters, optional queries, media-level body examples, arrays and nested objects (including trailing comma layout); OAuth body enum is hoisted under the operation instead of retaining the component enum; a nullable recursive union loses Optional; root import placement differs.

Owner: Follow-on scenario plan: media-level example retention, example-nested-array-two-items, parameter example selection, request-type placement, union-member-nullability-dropped, example-imports-case-insensitive-order.

Exact comparison: [supabase.diff](supabase.diff), **613** files compared, **13** differing, **0** Fern-only, **1** crozier-only.

## dystore

Publisher revision: `dystcz/dystore-api:openapi.yaml@ffd4d907e6909b0e2b137a490765e144e8d537e7`. Source SHA-256: `11f419fb0094197b3262ffe844583bb561b34b32bb51aad4a5b8c61dda691c23`.

Remaining differences: reference.md uses an emoji-bearing tag spelling in Python expressions and links although emitted Python uses the identifier-safe spelling.

Owner: Follow-on scenario plan: non-identifier tag documentation (candidate Fern defect; no departure entry claims it yet).

Exact comparison: [dystore.diff](dystore.diff), **144** files compared, **1** differing, **0** Fern-only, **0** crozier-only.

## twitter

Publisher revision: `RTAinJapan/rta-in-japan-twitter-api-docs:openapi.yaml@b5b30318e41647d44795f85dbfc428da8e93739a`. Source SHA-256: `e8b4ac8ed7b18fe20157faaf19144df91b39621fafdbaa44e34b94790f7c5607`.

Remaining differences: An empty first named media example wins in crozier; Fern selects the later nonempty media_ids example in README.md, reference.md and statuses/client.py.

Owner: Follow-on scenario plan: empty named media-example selection.

Exact comparison: [twitter.diff](twitter.diff), **58** files compared, **3** differing, **0** Fern-only, **0** crozier-only.

The diffs include secondary import/export and documentation changes caused by
the listed shapes; none is normalized away. Registration stays blocked until
the complete comparison is equal, with any intended defect correction first
certified through the public departure catalog.

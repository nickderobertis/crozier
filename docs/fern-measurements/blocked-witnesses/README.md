# Handed-off witness comparisons on the finished tree

These are public publisher specifications that earlier fixes screened but could
not register while other shapes differed. [`witnesses.tsv`](witnesses.tsv) lists
every one, with its immutable revision and source SHA-256. Each was fetched at
that revision, and its bytes were checked against the recorded digest. Fern CLI
**5.67.1** with `fernapi/fern-python-sdk` **5.20.0** then generated it afresh,
and crozier compared its output from the finished generator, through the shared
departure engine. Fern generated every one.

Every fresh comparison now exits **0**: each witness's only differences are
catalogued departures. Each is registered as a real corpus witness, with its
committed source bytes, its publisher's redistribution grant recorded in
[`CORPUS.md`](../../../tests/fixtures/CORPUS.md) and `NOTICE`, and a
certified-pair golden in both enum modes gated by the corpus byte-match. No
witness keeps a comparison diff, so [`residuals.tsv`](residuals.tsv) holds its
header alone. None enters an `unmatched` allowance.

[`residuals.tsv`](residuals.tsv) attributes **every hunk** of every committed
diff exactly once, to the owning scenario shape of the
[scenario proof index](../../openapi-surface/scenario-proof-index.tsv) or to
`unowned`. `tools/surface-census/scenario-proof-index.py check` reads the hunks
from the diffs themselves and fails when a hunk is unattributed, attributed
twice, or attributed to a shape the index does not hold, and when a registered
witness keeps a diff or a residual. `scenario-proof-index.py hunks <diff>`
prints a diff's hunks in the table's spelling.

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

Registered as corpus row 2801, `dystore-api`. The comparison exits **0** over
144 files. The tag `⚠️ Not supported yet` is spelled with its raw emoji in
Fern's `reference.md` calls, links and imports, although Fern's own Python names
the module `not_supported_yet`; its 31 lines are the
`emoji-tag-reference-identifiers` correction, a `fern-defect` (Fern's documented
call is a `SyntaxError`). The root `__init__.py`'s reordered imports are taken by
`init-type-checking-import-order`.

## kompaz

The complete fresh comparison matched: **exit 0**, 74 files compared. Its row
and diff were retired by an earlier fix; it is not registered here, and its
exact source provenance is retained below.

Source: `Stichting-KOMPAZ-1/KOMPAZ-web-frontend:openapi.json` at revision `a847053e46b98324c57183af2b2c09abe01f8ecf`.
Source SHA-256: `0437ad48ef2e96fae47e804e86333cbf76ad6a280918373a9f479f9646240511`.

## langchain

Registered as corpus row 2802, `langchain-agent-server`. The comparison exits
**0** over 241 files. The `post_a2a` example's union items are now
constructed as `PostA2ARequestParamsMessageMessagePartsItem_Text`/`_Data`
variants, as Fern writes them. The description of `assistant_id`, a collapsed
two-string `anyOf` described on the property, which Fern omits and crozier
writes, is the `collapsed-anyof-property-description` departure (44 lines over
models, docstrings and `reference.md`).

## rice-shower

Registered as corpus row 2803, `rice-shower`. The comparison exits **0** over
157 files with only the SDK identity headers departing. The `createSystem`
body's nullable `location` documents its member's description, and the
required `channels` query array, which declares no example, is left out of the
`getThermoMetrics`/`getHeaterMetrics` examples beside the unknown-object
`time_start`, as Fern leaves it.

## speech-ai

The complete fresh comparison matched: **exit 0**, 108 files compared. Its row
and diff were retired by an earlier fix; it is not registered here, and its
exact source provenance is retained below.

Source: `lenML/Speech-AI-Forge:docs/openapi.json` at revision `a41b70abba866ecded6e1e90beea6cc68e3fd0ae`.
Source SHA-256: `1ae1ec5faa3031d10996730f4dfda9726b828ef3a9bd8554d77adcd4ba1b32f6`.

## supabase

Registered as corpus row 2804, `supabase-api-v1`. The comparison exits **0**
over 612 files. Component-level request-body examples, the JSON-beside-binary
function bodies' `reference.md` parameters and the map-of-objects commas now
match. What departs is catalogued: `branch_id_or_ref`'s declared example
(`anyof-path-param-schema-example`, 23 lines), the text-only
`v1-diff-a-branch`'s optional query examples
(`text-response-optional-query-examples`, 6 lines), the required deploy file
(`multipart-object-required-file-example`) and the root import order.

## Import boundary

The generated SDKs were installed as real packages under Python 3.14.7 and
Pydantic 2.14.1 by the earlier fix. Supabase's root package and standalone
`JsonValueOutput` alias import cleanly, but eleven modules constructing models
over the implicit recursive JSON alias graph raise `RecursionError`, in
crozier's output and in certified Fern output alike: `fern.billing.client`,
`fern.billing.raw_client`, `fern.domains.client`, `fern.domains.raw_client`,
and the seven `fern.types.list_project_addons_response_output*` and
`fern.types.update_custom_hostname_response_output*` models. Making the alias
importable is follow-up work, not this comparison's.

## twitter

Registered as corpus row 2805, `rta-in-japan-twitter`. The comparison exits
**0** over 58 files with only the SDK identity headers departing. The first
named media example of `statuses/update` is an empty `media_ids` array; crozier
now treats it as absent and passes the schema example, as Fern does.

## vocode

Registered as corpus row 2800, `vocode-core`. The comparison exits **0** over
354 files, with only the SDK identity headers and the root import order
departing. All 128 certified public client methods and resource accessors are
exposed, including `buy_number`.

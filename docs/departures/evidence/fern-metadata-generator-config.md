# `fern-metadata-generator-config`

**Kind:** `provenance`. crozier writes one fixed `.fern/metadata.json`.

## The command and its result

crozier writes the same metadata record whatever it is configured with
(`assets/scaffolding/metadata.json`, emitted verbatim by `src/emit.rs`). Fern
records the configuration its generator ran with. Corpus row 57, the published
OpenFIGI API, has a literals golden whose Fern metadata leaves
`pydantic_config.enum_type` unset. Generating that same SDK with crozier shows:

```text
$ crozier generate python --spec tests/fixtures/corpus-sources/openfigi.com/openapi.json --output "$SDK_OUT" --package-name fern --project-name default_package_name --enum-type literals
$ diff tests/fixtures/openfigi.com/expected-literals/.fern/metadata.json "$SDK_OUT/.fern/metadata.json"
4a5,9
>   "generatorConfig": {
>     "pydantic_config": {
>       "enum_type": "python_enums"
>     }
>   },
```

`SDK_OUT` names a writable scratch directory. That block is this departure. The goldens generated with `client_class_name`,
`extra_fields` or `default_max_retries` record a different `generatorConfig`
object instead, and each is this departure on its first differing line; their rows are in
`tests/fixtures/departures-ledger.tsv`. The rule applies to the SDK root's
`.fern/metadata.json` alone: any other file whose name ends in `metadata.json`
is SDK content and is compared as written. It takes crozier's side only when it
is that fixed record byte for byte, reads both sides as JSON so only the
`generatorConfig` member may differ, and locates the member string-aware, so a
brace inside a string can neither hide another difference nor stretch it.

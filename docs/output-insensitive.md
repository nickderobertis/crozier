# Output-insensitive contexts

[The shared table](openapi-surface/output-insensitive.tsv) records a decision,
not a proof: deleting the feature changes neither generator's complete output.
The certified Fern pair comes from `assets/scaffolding/metadata.json`.

Each TSV row has `key`, `context`, `search_record`, `fern_comparison`, and
`crozier_comparison`. Paths are relative to the repository. The citing search
record names the key and describes the exact document and control. Use `-` for
a whole feature or combination; use the canonical handling-site spelling for
an arm, or describe the narrower document context. A narrow context settles
only that context.

Each comparison is JSON with exactly these fields:

```json
{
  "schema_version": 1,
  "generator": "fern",
  "fern_cli_version": "5.163.1",
  "fern_python_sdk_version": "5.41.3",
  "before": {"relative/generated/file.py": "<SHA-256>"},
  "after": {"relative/generated/file.py": "<SHA-256>"}
}
```

`generator` is `fern` or `crozier`. Both maps contain every generated file,
including scaffolding. Hash each generator's own bytes independently; compare
before with after, not Fern with crozier. The corpus and differential gates
separately establish parity between generators. A changed, added, or removed
file makes this disposition invalid.

The finished-state gate and arm headline read the same validated table. Missing
records, invalid pins, changed output, duplicate key/context pairs, and a proof
claim for the same key/context fail. Region categories, the census, and the reach
ledger retain their existing formats. An output-insensitive decision never
increases the count of proven features or arms.

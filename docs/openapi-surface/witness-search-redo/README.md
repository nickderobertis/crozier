# Reproducing the local witness search

The TSVs and `catalogue-portals.md` are preserved search evidence. Their recorded
commands describe the original run and remain unchanged for provenance. For a
new run over those same pinned inputs, use the repository command surface:

```sh
just witness-search-local-census --contract docs/openapi-surface/witness-search-redo/contract.md --workers 8 --documents jentic=/path/to/pinned/tree
```

Pass the source labels and pinned directories recorded in the shard with repeated
`--documents SOURCE=DIR` arguments. The recipe selects Python through
`scripts/census-python.sh`, avoiding an unrelated virtual environment. It prints
TSV to stdout; do not overwrite preserved evidence as part of validation.

`just test-witness-search-redo` checks the ledger and drives the CLI on temporary
JSON and YAML documents, including malformed inputs. It is a dependency of
`just check`, so CI checks report/declarer drift without fetching or rerunning the
source census.

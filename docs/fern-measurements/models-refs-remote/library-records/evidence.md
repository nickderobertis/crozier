# Library Records remote components

Independently authored inputs:
`tests/e2e/fixtures/models-refs-remote/library-records/openapi.yml` and
`models.yml`. `@REMOTE_URL@` is replaced with the ephemeral real loopback HTTP
server URL, both for certification and the real-binary proof. The source is
handwritten, not a publisher witness. The bounded failed and renewed search is
[recorded separately](../../../openapi-surface/witness-search-models-refs/README.md#remote-component-identities).

Fern CLI 5.67.1 and `fernapi/fern-python-sdk` 5.20.0 generated the complete
packages without edits other than the repository's string-safe comment stripper.
Default tree settings: `pydantic_config.enum_type: python_enums`. Literals tree:
no generator configuration, under
`docs/fern-measurements/models-refs-literals/library-records/fern-expected`.

Tree SHA-256, using the gate's sorted relative-path/length/bytes framing:

- Python enums: `6f81dfab32b3eb9117dde2defc473c16461ccbad59606d3a2e917419af5c0163`.
- Literals: `e4b929eb0fc0f5706aa394934e525105cd719a54d18dbaff38b9e3741151ad14`.

`remote_model_components_match_the_certified_fern_tree` drives the compiled
crozier binary through failed HTTP acquisition and successful recovery, then
compares every file in both directions through `src/parity.rs` in both enum
modes. Catalogue's Curator pointer resolves in its defining document, and the
direct response retains Curator's named component identity.
`remote_model_controls_reject_an_unexplained_dependency_mismatch` verifies that
changing the resolved dependency annotation to Any still fails comparison.
The ledger admits only existing identity and metadata departures.

## Multi-file cover contract

`scripts/handwritten-fixtures.py gate` admits these two rows through the distinct
`handwritten-e2e` cover kind in `docs/openapi-surface/handwritten-e2e.toml`.
This registry's version is 1. Each cover has exactly `kind`, `key`, `fixture`,
`test`, `evidence`, `golden`, `search`, `verdict` and `renewed`, all nonempty
strings. The kind is `handwritten-e2e`; keys are unique. Paths remain inside
the repository. The fixture is a committed directory holding multiple YAML
documents. The named gated Rust test serves that fixture with
`LocalDocumentServer`, drives `probe_command`, and asserts a complete
`golden_tree_failures` comparison. The evidence and certified metadata exist;
the search declares its verdict and renewed none-registrable result. The region
row names exactly those inputs. The existing three-entry directory contract,
ordinary covers and category vocabulary are unchanged. This representation
adds two handwritten proofs and no real witnesses.

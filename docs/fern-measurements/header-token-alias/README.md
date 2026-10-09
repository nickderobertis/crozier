# Header-token pass-through measurement

The independently authored Warehouse Ledger input declares `X Ledger` as a
client-wide header. CLI 5.67.1 with Python SDK 5.20.0 accepts it and emits the
required `ledger: str` constructor argument and the exact `X Ledger` wire key.
The complete, unedited output (Python comments stripped) is committed at
`docs/openapi-surface/handwritten/warehouse-header-token/fern-expected`.

Settings: packaged layout, package `fern`, project `default_package_name`,
client `FernApi`, `python_enums`, extra fields `allow`, default retries 2,
no audience filtering. `fern-pinned.log` records the generation.

The direct `x-crozier-global-headers` run also succeeds, but Fern ignores that
unknown spelling: its constructor has no `ledger` argument and its wrapper has
no `X Ledger` wire key. `ignored-alias-input.json`, `crozier-pinned.log` and
`ignored-alias-metadata.json` record that observation and pin. Crozier's alias
comparison uses the supported Fern spelling's certified golden, following the
standing dual-header policy, including conflicting values on the same node.

A wire-header token check would refuse an input the certified pair accepts.
The declared name therefore passes through unchanged. This is matched generator
behavior, not an exception to parity or a new refusal-registry class. The
bounded real-source search remains incomplete; its record is linked from the
fixture evidence. No real witness is claimed for this independently authored
input.

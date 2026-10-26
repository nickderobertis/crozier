# Empty composition member beside a reference

**Verdict: `parity-gap-repaired`.** Compared against the certified pair, Fern
types an `allOf` of `$ref Kiln` and an empty `{}` member as `Kiln` itself, where
crozier copied the target into a new model (`LoadKiln`). crozier now drops a
bare `{}` `allOf` member before any reference reader runs, and its SDK for this
document byte-matches `fern-expected/`.

Proposal: [#615](https://github.com/nickderobertis/crozier/issues/615).

`openapi.yml` was written from scratch for this measurement. `fern-expected/` is
the complete, comment-stripped output that Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3 generated from it under `python_enums`. It was
produced by `just fern-references measurements
output-defects/615-empty-composition-member-reference`, the case `cases.tsv`
registers. Its tree digest (Contract A) is
`6200d8c9a762d556aaf0d777911f366f1f60885a4d53976ff0f0b0f4bfa45057`.

## The comparison

`Load` holds the defect and its removal controls side by side, and the inline
`transferLoad` body repeats the defect where operation bodies are lowered:

| Site | Composition | Fern | crozier at `80331e4bb` |
|---|---|---|---|
| `Load.kiln` | `[$ref Kiln, {}]` | `Kiln` | `LoadKiln` (copy) |
| `Load.overflowKiln` | `[{}, $ref Kiln]` | `Optional[Kiln]` | `Optional[LoadOverflowKiln]` (copy) |
| `transferLoad` `destination` | `[$ref Kiln, {}]` | `Kiln` | `TransferLoadRequestDestination` (copy) |
| `Load.usualKiln` | plain `$ref Kiln` | `Optional[Kiln]` | same |
| `Load.soloKiln` | `[$ref Kiln]` | `Optional[Kiln]` | same |
| `Load.notedKiln` | `[$ref Kiln, {description}]` | `LoadNotedKiln` (copy) | same |
| `Load.reservedKiln` | `[$ref Kiln, {required, properties}]` | `LoadReservedKiln(Kiln)` | same |
| `transferLoad` `fallback` | `[$ref Kiln, {description}]` | `TransferLoadRequestFallback`, argument documented | copy, argument undocumented |

The empty member is the whole difference. With it removed (`soloKiln`), both
generators already named `Kiln`. With a member that says something (a
description, or a constraint), both still declare a class of their own.

## The outcome

- `src/openapi.rs`: `normalize_empty_compositions` drops each bare `{}` `allOf`
  member, so every single-reference reader in `src/ir.rs` sees the one `$ref`
  left. A `{}` alternative of a `oneOf`/`anyOf` admits anything, so it is kept.
- `src/ir.rs`: an inline body argument whose description sits in its `allOf`
  member is documented by it (`hoist_inline_object`), as a model field already
  was. This is the `fallback` row, which this document also exposed.

`crates/crozier-e2e/tests/e2e/output_defects.rs` holds crozier's whole SDK to
`fern-expected/`. It also shows that crozier's former `kiln: LoadKiln` and
`destination: TransferLoadRequestDestination` fail the comparison. Its
`sdk_env_*` journey runs the SDK as `runtime.txt` records.

## Runtime

`runtime.txt` records an actual run of the certified SDK with Pydantic 2.14.1,
and the same run over crozier's pre-repair SDK as a control. The journey
(`crates/crozier-e2e/tests/e2e/output_defects_runtime.py 615`) drives the
generated client over an `httpx.MockTransport`:

- `schedule_load(kiln=Kiln(...))` sends a body that `Load` validates;
- the returned `Load.kiln` and `Load.overflow_kiln` are instances of the `Kiln`
  the package exports;
- the controls parse as `LoadNotedKiln` and `LoadReservedKiln`;
- `transfer_load` takes `destination` as `Kiln`.

To reproduce, install `httpx` and `pydantic` in a disposable environment, convert
`openapi.yml` to `openapi.json` (any YAML loader), and run:

```sh
python crates/crozier-e2e/tests/e2e/output_defects_runtime.py 615 \
  docs/fern-measurements/output-defects/615-empty-composition-member-reference/fern-expected/src \
  openapi.json
```

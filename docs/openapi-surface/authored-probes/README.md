# Authored-probe measurements

Documents written to isolate one shape, each with what pinned Fern (CLI 5.67.1,
`fernapi/fern-python-sdk` 5.20.0) generated from it, that crozier is byte-gated
against. A case is **neither** a [hand-written fixture](../handwritten/AGENTS.md)
nor real-specification evidence: no real-specification search was run for its
shape, so its evidence tier is undecided. It names no region row, census
selector, golden-reach site or search record, and no count treats it as a match.
What it proves is narrower: on this document, crozier emits what Fern emits.

## Layout

One directory per case, `<ticket>-<shape>/`, holding:

- `openapi.yml`: the authored document.
- `fern.log`: Fern's measurement, opening `Fern CLI 5.67.1, python-sdk 5.20.0`
  and recording `check exit:` and `generate exit:` with each command's output.
- `fern-expected/`: the complete comment-stripped tree Fern generated, in the
  workspace [`../probes/AGENTS.md`](../probes/AGENTS.md#re-running-one)
  prescribes. A document Fern refuses is no case here: it belongs to the
  [refusal registry](../../fern-refusals/README.md).

Nothing in a case is edited after the measurement. A divergence is repaired in
`src/`.

## The gate

`authored_probe_measurements_match_fern` in
[`../../../crates/crozier-e2e/tests/e2e.rs`](../../../crates/crozier-e2e/tests/e2e.rs) lists this directory, holds
each case to the layout above, and byte-compares crozier's output over its
`openapi.yml` (`--package-name fern`) against `fern-expected/` under the
corpus gate's normalization.

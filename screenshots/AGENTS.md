# Terminal screenshots (`screenshots/`)

The README's "See it in action" images are **real captures of the `crozier`
CLI**, gated by [screencomp](https://github.com/nickderobertis/screencomp) so a
change to what a command prints can't land without the committed image changing
with it. This folder holds the inputs; the mechanics live in
[`scripts/screenshots.sh`](../scripts/screenshots.sh) (static SVGs) and
[`scripts/demo-gif.py`](../scripts/demo-gif.py) (the animated hero).

## What's here

- `petstore.yml` — the demo OpenAPI document every scene generates from. Kept
  small and self-contained so the captures stay stable and decoupled from the
  `tests/fixtures/` corpus. Changing it re-renders the `generate`, `model`, and
  GIF scenes (the file count in the summary, the tree, and the shown model), so
  re-bless the baseline when you do.
- `broken.yml` — a paths fragment with no `openapi` field, so the `error` scene
  captures crozier's real boundary-validation message.
- `fonts/JetBrainsMono-Regular.ttf` — the pinned font `freeze` embeds into every
  SVG (base64) and Pillow draws the GIF with. Vendoring it is what makes the SVG
  bytes identical on every machine and CI runner. Licensed under the SIL Open
  Font License 1.1 (`fonts/OFL.txt`).

## The contract

`scripts/screenshots.sh` drives the **real release binary** — the two `--help`
screens, a real `generate` run, a `cat` of a generated file, and the real error —
and renders each scene to a deterministic SVG. Only the `$ …` prompt lines are
synthetic framing; everything below each one is the binary's own output. Because
the font is embedded and the few per-machine values (temp paths) are kept out of
frame, the SVG bytes — and therefore screencomp's digests — are reproducible. The
gate is: identical output ⇒ identical bytes ⇒ identical hash.

Scenes → cards (see `screencomp.toml`): `help` (a `command` toggle flips between
`main` and `generate`), `generate`, `model`, `error`. The GIF is informational
and **not** hash-gated (a GIF isn't byte-reproducible across Pillow versions).

## Workflow

```sh
just screenshots-tools    # install the pinned `freeze` (needs Go); once
just screenshots          # re-capture the SVGs into shots/current + docs/screenshots
just screenshots-gif      # re-render docs/screenshots/demo.gif (needs Python + Pillow)
just screenshots-bless    # re-capture AND refresh shots/baseline/<arch>.json
```

`ruff` must be on PATH — crozier defers Python wrapping to it, so `generate`
(and thus the `generate`/`model`/GIF scenes) needs it. `just bootstrap` installs
the pinned one.

After an **intended** output change: `just screenshots-bless`, then commit
`shots/baseline/` and `docs/screenshots/` together. The `.githooks/pre-push`
guard (enabled by `just bootstrap`) re-captures automatically when a
`[guard].paths` file changed and stops the push on un-blessed drift; CI's
`.github/workflows/visual-docs.yml` is the authoritative gate and also posts a
before/after gallery comment on the PR.

# generated-file-name-too-long

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe exits 1 after writing a partial SDK because the emitted filename exceeds the filesystem limit. No usable package, import, mypy configuration or send/parse journey exists. Refusal must happen before any output is written.
[generate](evidence/generated-file-name-too-long.generate.log)

Retrievable population representative `905d87c6b9f10eecc25fabcbd3dae791b0c8e717ff3ed75f5fa3ef4cdc8b81e4` (source locator in generation log):
The Presentation Exchange representative generates, but fails import with an undefined FilterV2Base; mypy reports zero errors under its own generated pyproject configuration. Import failure makes a send/parse journey unavailable and fails the required bar.
[generate](evidence/905d87c6b9f10eecc25fabcbd3dae791b0c8e717ff3ed75f5fa3ef4cdc8b81e4.generate.log), [import](evidence/905d87c6b9f10eecc25fabcbd3dae791b0c8e717ff3ed75f5fa3ef4cdc8b81e4.import.log), [mypy](evidence/905d87c6b9f10eecc25fabcbd3dae791b0c8e717ff3ed75f5fa3ef4cdc8b81e4.mypy.log)

All 1 retrievable population documents refuse with exit 1 and no output under strict mode: [measurements](evidence/population-strict.log).

Pinned Fern controls: .

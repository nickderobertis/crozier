# sdk-method-collision

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. The population carries the class on 2 documents at this pair, as at Fern CLI 5.67.1. crozier's release build refuses both under `--fern-strict` ([`documents.tsv`](../documents.tsv)).

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's. The Fern logs listed under *Dated history* were taken at 5.67.1 and are kept as that record; no claim about 5.163.1 rests on them.

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe imports and reports zero mypy errors under its generated pyproject configuration, but analytics.create sends POST /reports only. The POST /queries endpoint is silently dropped, so the package is not fully useful.
[generate](evidence/sdk-method-collision.generate.log), [import](evidence/sdk-method-collision.import.log), [mypy](evidence/sdk-method-collision.mypy.log), [wire](evidence/sdk-method-collision.wire.log)

Retrievable population representative `d0208b3d35ab47ace5d0b7ea458abc826154adf640a9be9934991f1ec7932f27` (source locator in generation log):
The Cloudflare representative fails import and reports 4,065 mypy errors. Its generated package cannot run a send/parse journey; this independently fails the required bar.
[generate](evidence/d0208b3d35ab47ace5d0b7ea458abc826154adf640a9be9934991f1ec7932f27.generate.log), [import](evidence/d0208b3d35ab47ace5d0b7ea458abc826154adf640a9be9934991f1ec7932f27.import.log), [mypy](evidence/d0208b3d35ab47ace5d0b7ea458abc826154adf640a9be9934991f1ec7932f27.mypy.log)

Pinned Fern accepts inferred method names and differently spelled explicit names or groups; the detector compares only exact explicit group and method names. Controls: [sdk-method-different-group.pinned-fern](evidence/sdk-method-different-group.pinned-fern.log), [sdk-method-inferred.pinned-fern](evidence/sdk-method-inferred.pinned-fern.log), [sdk-method-normalized-group.pinned-fern](evidence/sdk-method-normalized-group.pinned-fern.log), [sdk-method-normalized-method.pinned-fern](evidence/sdk-method-normalized-method.pinned-fern.log).

Both retrievable population documents refuse with exit 1 and no output under strict mode: [measurements](evidence/population-strict.log).

## Dated history

Taken at Fern CLI 5.67.1 / fern-python-sdk 5.20.0, over a document never committed or one since re-measured in `shapes.tsv`:

- [`evidence/sdk-method-different-group.pinned-fern.log`](evidence/sdk-method-different-group.pinned-fern.log)
- [`evidence/sdk-method-inferred.pinned-fern.log`](evidence/sdk-method-inferred.pinned-fern.log)
- [`evidence/sdk-method-normalized-group.pinned-fern.log`](evidence/sdk-method-normalized-group.pinned-fern.log)
- [`evidence/sdk-method-normalized-method.pinned-fern.log`](evidence/sdk-method-normalized-method.pinned-fern.log)

# sdk-method-collision

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe imports and reports zero mypy errors under its generated pyproject configuration, but analytics.create sends POST /reports only. The POST /queries endpoint is silently dropped, so the package is not fully useful.
[generate](evidence/sdk-method-collision.generate.log), [import](evidence/sdk-method-collision.import.log), [mypy](evidence/sdk-method-collision.mypy.log), [wire](evidence/sdk-method-collision.wire.log)

Retrievable population representative `d0208b3d35ab47ace5d0b7ea458abc826154adf640a9be9934991f1ec7932f27` (source locator in generation log):
The Cloudflare representative fails import and reports 4,065 mypy errors. Its generated package cannot run a send/parse journey; this independently fails the required bar.
[generate](evidence/d0208b3d35ab47ace5d0b7ea458abc826154adf640a9be9934991f1ec7932f27.generate.log), [import](evidence/d0208b3d35ab47ace5d0b7ea458abc826154adf640a9be9934991f1ec7932f27.import.log), [mypy](evidence/d0208b3d35ab47ace5d0b7ea458abc826154adf640a9be9934991f1ec7932f27.mypy.log)

Pinned Fern accepts inferred method names and differently spelled explicit names or groups; the detector compares only exact explicit group and method names. Controls: [sdk-method-different-group.pinned-fern](evidence/sdk-method-different-group.pinned-fern.log), [sdk-method-inferred.pinned-fern](evidence/sdk-method-inferred.pinned-fern.log), [sdk-method-normalized-group.pinned-fern](evidence/sdk-method-normalized-group.pinned-fern.log), [sdk-method-normalized-method.pinned-fern](evidence/sdk-method-normalized-method.pinned-fern.log).

Both retrievable population documents refuse with exit 1 and no output under strict mode: [measurements](evidence/population-strict.log).

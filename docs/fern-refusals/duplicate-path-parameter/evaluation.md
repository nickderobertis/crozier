# Repeated path parameter names

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe generates, imports, and reports zero mypy errors under its own
pyproject configuration. Its single `account_id` argument fills both declared
path positions, and its 204 response parses as `None`.
[generation](evidence/duplicate-path-parameter.generate.log), [import](evidence/duplicate-path-parameter.import.log),
[mypy](evidence/duplicate-path-parameter.mypy.log), [wire](evidence/duplicate-path-parameter.wire.log).

The retrievable Hugging Face representative `6b26beb70fb91ee1fd2e7ae1fb99b8b7b974be9a39d832e678e8da60a5f65123` generates but fails to
import all package modules and reports 156 mypy errors under its own generated
configuration. No send/parse claim can be established through that broken SDK.
Its source locator is committed in the generation log:
[generation](evidence/6b26beb70fb91ee1fd2e7ae1fb99b8b7b974be9a39d832e678e8da60a5f65123.generate.log), [import](evidence/6b26beb70fb91ee1fd2e7ae1fb99b8b7b974be9a39d832e678e8da60a5f65123.import.log),
[mypy](evidence/6b26beb70fb91ee1fd2e7ae1fb99b8b7b974be9a39d832e678e8da60a5f65123.mypy.log). The class therefore fails the required bar.

Pinned Fern refuses [repeated route placeholders](evidence/path-repeated.pinned-fern.log)
but accepts [repeated declarations for one placeholder](evidence/path-declarations.pinned-fern.log)
and [distinct placeholders](evidence/path-valid.pinned-fern.log).
The detector counts placeholders in the document's route, rather than declarations.

All six retrievable population documents refuse under strict mode with no output: [run](evidence/population-strict.log).

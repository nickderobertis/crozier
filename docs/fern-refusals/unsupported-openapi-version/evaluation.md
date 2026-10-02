# unsupported-openapi-version: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No emitted SDK was
repaired to change the result of this evaluation.

The [3.2.0 probe](evaluation-logs/unsupported-openapi-version.log) imports and
reports **zero mypy errors** under its own `pyproject.toml` configuration, with
its declared mypy 1.13.0 and dependencies installed under CPython 3.12.3. Its
[wire journey](evaluation-logs/probe.wire.log) sends `GET /probe` and parses the
declared bodyless 204 as `None`. The probe alone would qualify for generation.

The population prevents choosing `generate` for the whole class:

| Publisher and digest | Import | mypy errors | Default wire behavior |
| --- | --- | --- | --- |
| [LangWatch, `05274561b1…`](evaluation-logs/unsupported-openapi-version-05274561b18c20b41f3d9acb0c611fdadafc28aa62aa695ce506c030cf7dd391.log) | succeeds | 0 | GET /api/dataset; page and limit remain query parameters |
| [ContextualWisdomLab/Orgmetra, `09c1e43486…`](evaluation-logs/unsupported-openapi-version-09c1e43486779198574fe31b8bcabbd1c1f74beec7bf86245ae578061619838f.log) | succeeds | 0 | POST /person-records; display_name and effective_from remain their declared wire names |
| [Scalar, `0b1bdec6ee…`](evaluation-logs/unsupported-openapi-version-0b1bdec6eedd86d139977fff23b88f87ad366f004c116567760ffdec4e1211c9.log) | succeeds | 8 | POST /stripe preserves the request object and parses the declared null response |

All three logs record immutable source URLs, document digests, generation,
imports and complete mypy reports under the generated SDK's own configuration.
The wire traces exercise one endpoint of each document, rather than claiming
coverage of every OpenAPI 3.2 feature. The Scalar SDK's eight mypy errors mean
this class does not satisfy the required import/type-check/wire conjunction,
even though its selected wire journey and the probe work. The decision is
therefore `refuse`, applying in both modes, without repairing that SDK.

The detector retains OpenAPI 3.0 and 3.1 support and rejects the newer minor
versions Fern refuses. Version checking precedes normalization, so an unknown
3.2 construct cannot mask the class with an unrelated loader error. An ordinary
read or parse failure retains the existing loader diagnostic.

The real binary recovery journey refuses the 3.2.0 probe in both modes, writes
nothing and prints one line naming its version; replacing the version with
3.1.0 restores byte-identical generation in both modes. Both the
[unit test](evaluation-logs/version-unit-red.log) and the
[real binary journey](evaluation-logs/version-e2e-red.log) were observed failing
before this behavior existed.

[All 20 population documents](evaluation-logs/population-refusals.jsonl) were
retrieved at their recorded digests and refused in both modes with this class:
exit 1, no output, one stderr line, and a `fern-strict` cause in strict mode.
The table records `20/20` and all 20 strict exits.

[LangWatch wire trace](evaluation-logs/05274561b18c20b41f3d9acb0c611fdadafc28aa62aa695ce506c030cf7dd391.wire.log).

[Orgmetra wire trace](evaluation-logs/09c1e43486779198574fe31b8bcabbd1c1f74beec7bf86245ae578061619838f.wire.log).

[Scalar wire trace](evaluation-logs/0b1bdec6eedd86d139977fff23b88f87ad366f004c116567760ffdec4e1211c9.wire.log).

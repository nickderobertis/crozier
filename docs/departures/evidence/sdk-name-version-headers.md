# `sdk-name-version-headers`

**Kind:** `packaging`. crozier writes the packaged wrapper's SDK name and version
from its own settings.

## The command and its result

crozier's packaged client wrapper always sends `X-Crozier-SDK-Name` (its project
name) and `X-Crozier-SDK-Version`, the fixed packaged version `0.0.0`
(`DEFAULT_SDK_VERSION` in `src/emit.rs`). Fern's value is the version the SDK is
released under. At the certified pair, Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3, every packaged golden is generated without
`--version` and its wrapper sends the pair with `0.0.0`
(`tests/fixtures/alma-france/expected/src/fern/core/client_wrapper.py` lines
39–40); the golden's `.fern/metadata.json` records `"cliVersion": "5.163.1"` and
`"generatorVersion": "5.41.3"`. crozier, over the document of
[`readme-client-class-casing.md`](readme-client-class-casing.md):

```text
$ crozier generate python --spec docs/departures/evidence/readme-client-class-casing/openapi.yml --output cz --package-name fern --project-name default_package_name
$ grep -n SDK- cz/src/fern/core/client_wrapper.py
37:            "X-Crozier-SDK-Name": "default_package_name",
38:            "X-Crozier-SDK-Version": "0.0.0",
```

A reference released under another version carries it in that header: run
with `--version 2.3.1` (`FERN_TOKEN=preview-only-no-publish fern generate
--group python-sdk --local --preview --output preview --force --version
2.3.1`, organization `fern`), Fern's wrapper reads `"X-Fern-SDK-Version":
"2.3.1"` beside `"X-Fern-SDK-Name": "default_package_name"`. That run was
measured at the previous certified pair (Fern CLI 5.67.1 with
`fernapi/fern-python-sdk` 5.20.0) and has not been repeated at the new one,
since no committed golden is released under a version; the comparison is held
on the new pair's packaged golden by
`compare_applies_the_packaging_and_metadata_departures_exactly` in
`crates/crozier-e2e/tests/e2e/compare.rs`, which edits that golden's header to
`2.3.1` (and drops the pair altogether) and checks the comparison reports this
departure.

The version line is this departure; the name line, with equal values, is
`sdk-identity-header-prefix`. A reference whose wrapper sends no such pair (one
generated without publishing metadata) makes both of crozier's lines this
departure.

## Where it applies

No committed golden: every packaged golden is generated without `--version`, so
Fern writes `0.0.0` and crozier's lines differ from it only in the prefix. The
release version reaches other files too — the same run writes `version =
"2.3.1"` in `pyproject.toml` and `"requestedVersion": "2.3.1"` in
`.fern/metadata.json`, which no catalog entry accounts for — so a reference
released under another version still fails `crozier compare` on those files.
This entry carries forward the header half of what the comparison tolerated
before the catalog existed; its rule recognises only these two header lines.

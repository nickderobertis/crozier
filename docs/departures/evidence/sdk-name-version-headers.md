# `sdk-name-version-headers`

**Kind:** `packaging`. crozier writes the packaged wrapper's SDK name and version
from its own settings.

## The command and its result

crozier's packaged client wrapper always sends `X-Crozier-SDK-Name` (its project
name) and `X-Crozier-SDK-Version`, the fixed packaged version `0.0.0`
(`DEFAULT_SDK_VERSION` in `src/emit.rs`). Fern's value is the version the SDK is
released under. Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, the
organization `fern` and the generators file of
[`readme-client-class-casing.md`](readme-client-class-casing.md), run as
`FERN_TOKEN=preview-only-no-publish fern generate --group python-sdk --local
--preview --output preview --force --version 2.3.1`:

```text
$ grep -n SDK- preview/fern-python-sdk/src/fern/core/client_wrapper.py
37:            "X-Fern-SDK-Name": "default_package_name",
38:            "X-Fern-SDK-Version": "2.3.1",
$ crozier generate python --spec openapi.yml --output cz --package-name fern --project-name default_package_name
$ grep -n SDK- cz/src/fern/core/client_wrapper.py
37:            "X-Crozier-SDK-Name": "default_package_name",
38:            "X-Crozier-SDK-Version": "0.0.0",
```

Line 38 is this departure; line 37, with equal values, is
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

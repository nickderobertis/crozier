# Shared collections export verification

Source: [#694](https://github.com/nickderobertis/crozier/issues/694).
Local verdict: `already-matching`; the base already contains that ticket's
repair. [The document record](../README.md) gives the immutable source and
fresh certified generation. `comparison.json` is the normalized report data
from the real `crozier compare`; `comparison.diff` is its unchanged output.
The target initializer byte-matches. Other measured files remain open under
[their named causes](../remaining.tsv).

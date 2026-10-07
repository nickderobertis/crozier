# census-fallback

The arm search's YAML fallback held to the census's stdlib loader under the
pinned ruamel.yaml (`run.sh samples`, `run.sh parsers`). The parser pin is read
from each script's own PEP 723 `dependencies` line and installed through uv, so
the tier is promoted (`tier:promoted`) and never cached; CI's live-e2e leg runs
it. The committed samples it reads belong to the census
(`tools/surface-census/tests/data/`).

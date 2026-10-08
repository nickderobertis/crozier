#!/usr/bin/env bash
# A reference tool refusing the document: no reference to compare.
set -euo pipefail
echo "reference tool: this document is not supported — point the generator at a" \
     "document the reference tool accepts, or remove its reference from crozier.yml" >&2
exit 7

"""Bind the advertised whole request against the actual generated signatures."""

from __future__ import annotations

import argparse
import importlib
import inspect
import json
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("sdk", type=Path)
args = parser.parse_args()
sys.path.insert(0, str(args.sdk.resolve()))
sdk = importlib.import_module("fern")
results = {}
for name in ("FernApi", "AsyncFernApi"):
    signature = inspect.signature(getattr(sdk, name).register_label)
    signature.bind(None, label="orchard")
    try:
        signature.bind_partial(None, request=sdk.LabelRegistration(label="orchard"))
    except TypeError as error:
        assert "unexpected keyword argument 'request'" in str(error), str(error)
        results[name] = str(error)
    else:
        raise AssertionError(f"{name}: advertised request unexpectedly binds")
print(json.dumps(results, sort_keys=True))

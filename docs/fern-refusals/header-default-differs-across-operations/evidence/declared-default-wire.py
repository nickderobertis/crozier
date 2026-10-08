# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo CLI driven by just, with no Nx workspace; this documentary evidence script belongs to the linked departure or refusal evaluation and is run explicitly against the committed certified output or an identified generated SDK.
"""Assert both declared defaults using a generated SDK's public methods."""
import os
import sys
from pathlib import Path

import httpx

location = os.environ.get("SDK_EVALUATION_DIR")
if not location:
    raise SystemExit("set SDK_EVALUATION_DIR to the generated Calibration Atlas SDK")
sdk = Path(location).resolve()
package = sdk / "src" / "fern"
if not all((package / name).is_file() for name in ("__init__.py", "client.py")):
    raise SystemExit(f"{sdk}: expected a generated SDK with src/fern/client.py and __init__.py")
sys.path.insert(0, str(sdk / "src"))
import fern
if Path(fern.__file__).resolve() != (package / "__init__.py").resolve():
    raise SystemExit(f"imported {fern.__file__}, expected the SDK at {package}")
from fern import FernApi

sent = []
def answer(request):
    sent.append((request.method, request.headers["X-Projection"]))
    return httpx.Response(200, json=["measurement"])

client = FernApi(base_url="https://atlas.example.net", httpx_client=httpx.Client(transport=httpx.MockTransport(answer)))
assert client.list_measurements() == ["measurement"]
assert client.replace_measurements() == ["measurement"]
print(f"sent: {sent}", flush=True)
assert sent == [("GET", "radial"), ("PUT", "linear")], f"operation defaults lost: {sent}"

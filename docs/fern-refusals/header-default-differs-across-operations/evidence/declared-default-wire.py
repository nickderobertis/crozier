"""Assert both declared defaults using a generated SDK's public methods."""
import os
import sys
from pathlib import Path

import httpx

sdk = Path(os.environ["SDK_EVALUATION_DIR"])
sys.path.insert(0, str(sdk / "src"))
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

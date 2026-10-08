"""Exercise generated nullable file methods against the local HTTP transport."""

import asyncio
from email import policy
from email.parser import BytesParser
import importlib
from pathlib import Path
import sys

import httpx

sys.path.insert(0, str(Path(sys.argv[1]).resolve()))
sdk = importlib.import_module("fern")
requests: list[httpx.Request] = []
payload = b"archived page\x00\xff"


def handle(request: httpx.Request) -> httpx.Response:
    content_type = request.headers["content-type"]
    assert content_type.startswith("multipart/form-data; boundary=")
    message = BytesParser(policy=policy.default).parsebytes(
        f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode()
        + request.read()
    )
    parts = {part.get_param("name", header="content-disposition"): part
             for part in message.iter_parts()}
    assert set(parts) == {"page"}
    assert parts["page"].get_filename() == "page.bin"
    assert parts["page"].get_payload(decode=True) == payload
    requests.append(request)
    return httpx.Response(204)


with httpx.Client(transport=httpx.MockTransport(handle)) as transport:
    client = sdk.FernApi(base_url="https://archive.example.test", httpx_client=transport)
    try:
        client.preserve_reel(page={"invalid": "file"})
    except AttributeError as error:
        assert "read" in str(error)
    else:
        raise AssertionError("an invalid file value reached the transport")
    assert not requests
    assert client.preserve_reel(page=("page.bin", payload, "application/octet-stream")) is None


async def async_wire() -> None:
    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as transport:
        client = sdk.AsyncFernApi(base_url="https://archive.example.test", httpx_client=transport)
        assert await client.preserve_reel(page=("page.bin", payload, "application/octet-stream")) is None


asyncio.run(async_wire())
assert len(requests) == 2
print("nullable files encode in sync and async methods; invalid file recovers")

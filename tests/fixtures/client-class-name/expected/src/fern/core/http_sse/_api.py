

import re
from contextlib import asynccontextmanager, contextmanager
from typing import Any, AsyncGenerator, AsyncIterator, Iterator, cast

import httpx
from ._decoders import SSEDecoder
from ._exceptions import SSEError
from ._models import ServerSentEvent


class EventSource:
    def __init__(self, response: httpx.Response) -> None:
        self._response = response

    def _check_content_type(self) -> None:
        content_type = self._response.headers.get("content-type", "").partition(";")[0]
        if "text/event-stream" not in content_type:
            raise SSEError(
                f"Expected response header Content-Type to contain 'text/event-stream', got {content_type!r}"
            )

    def _get_charset(self) -> str:
        """Extract charset from Content-Type header, fallback to UTF-8."""
        content_type = self._response.headers.get("content-type", "")


        charset_match = re.search(r"charset=([^;\s]+)", content_type, re.IGNORECASE)
        if charset_match:
            charset = charset_match.group(1).strip("\"'")

            try:

                "test".encode(charset).decode(charset)
                return charset
            except (LookupError, UnicodeError):

                pass


        return "utf-8"

    @property
    def response(self) -> httpx.Response:
        return self._response

    def iter_sse(self) -> Iterator[ServerSentEvent]:
        self._check_content_type()
        decoder = SSEDecoder()
        charset = self._get_charset()

        buffer = ""
        for chunk in self._response.iter_bytes():

            text_chunk = chunk.decode(charset, errors="replace")
            buffer += text_chunk


            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.rstrip("\r")
                sse = decoder.decode(line)


                if sse is not None:
                    yield sse


        if buffer.strip():
            line = buffer.rstrip("\r")
            sse = decoder.decode(line)
            if sse is not None:
                yield sse

    async def aiter_sse(self) -> AsyncGenerator[ServerSentEvent, None]:
        self._check_content_type()
        decoder = SSEDecoder()
        lines = cast(AsyncGenerator[str, None], self._response.aiter_lines())
        try:
            async for line in lines:
                line = line.rstrip("\n")
                sse = decoder.decode(line)
                if sse is not None:
                    yield sse
        finally:
            await lines.aclose()


@contextmanager
def connect_sse(client: httpx.Client, method: str, url: str, **kwargs: Any) -> Iterator[EventSource]:
    headers = kwargs.pop("headers", {})
    headers["Accept"] = "text/event-stream"
    headers["Cache-Control"] = "no-store"

    with client.stream(method, url, headers=headers, **kwargs) as response:
        yield EventSource(response)


@asynccontextmanager
async def aconnect_sse(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    **kwargs: Any,
) -> AsyncIterator[EventSource]:
    headers = kwargs.pop("headers", {})
    headers["Accept"] = "text/event-stream"
    headers["Cache-Control"] = "no-store"

    async with client.stream(method, url, headers=headers, **kwargs) as response:
        yield EventSource(response)

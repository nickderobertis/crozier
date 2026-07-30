

import codecs
import re
import time
from contextlib import asynccontextmanager, contextmanager
from typing import (
    Any,
    AsyncContextManager,
    AsyncGenerator,
    AsyncIterator,
    Callable,
    ContextManager,
    Iterator,
    Optional,
)

import anyio
import httpx
from ._decoders import SSEDecoder
from ._exceptions import SSEError
from ._models import ServerSentEvent

MAX_LINE_SIZE: int = 1_048_576


DEFAULT_MAX_RECONNECTION_ATTEMPTS: int = 5
DEFAULT_RECONNECT_DELAY_MS: int = 1_000
MAX_RECONNECT_DELAY_MS: int = 30_000






class EventSource:
    def __init__(
        self,
        response: httpx.Response,
        *,
        resumable: bool = False,
        stream_reconnection_enabled: bool = True,
        max_stream_reconnection_attempts: Optional[int] = None,
        stream_terminator: Optional[str] = None,
        reconnect: Optional[Callable[[str], Any]] = None,
    ) -> None:
        self._response = response
        self._resumable = resumable
        self._stream_reconnection_enabled = stream_reconnection_enabled
        self._max_stream_reconnection_attempts = max_stream_reconnection_attempts
        self._stream_terminator = stream_terminator
        self._reconnect = reconnect

    @staticmethod
    def _is_event_stream(response: httpx.Response) -> bool:
        content_type = response.headers.get("content-type", "").partition(";")[0]
        return "text/event-stream" in content_type

    def _check_content_type(self) -> None:
        if not self._is_event_stream(self._response):
            content_type = self._response.headers.get("content-type", "").partition(";")[0]
            raise SSEError(
                f"Expected response header Content-Type to contain 'text/event-stream', got {content_type!r}"
            )

    def _is_reconnect_response_usable(self, response: httpx.Response) -> bool:
        """Whether a reconnected response can be resumed as an SSE stream.

        ``httpx.stream`` does not raise on non-success status, so a resume that
        returns an error page (e.g. ``200 text/html`` or a ``500`` body) would
        otherwise be parsed as SSE and yield garbage/zero events. Such a
        response is treated as a failed attempt (back off and retry) instead.
        """
        return response.status_code < 400 and self._is_event_stream(response)

    def _get_charset(self, response: Optional[httpx.Response] = None) -> str:
        """Extract charset from Content-Type header, fallback to UTF-8."""
        resolved = response if response is not None else self._response
        content_type = resolved.headers.get("content-type", "")


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

    @staticmethod
    def _normalize_sse_line_endings(buf: str) -> str:
        """Normalize line endings per the SSE spec (\\r\\n → \\n, bare \\r → \\n).

        A trailing \\r is preserved because it may pair with a leading \\n in
        the next chunk to form a single \\r\\n terminator.
        """
        buf = buf.replace("\r\n", "\n")
        if buf.endswith("\r"):
            return buf[:-1].replace("\r", "\n") + "\r"
        return buf.replace("\r", "\n")

    def _new_text_decoder(self, response: Optional[httpx.Response] = None) -> "codecs.IncrementalDecoder":
        return codecs.getincrementaldecoder(self._get_charset(response))(errors="replace")

    def _reconnect_applicable(self) -> bool:
        """Whether reconnection is configured for this stream at all.

        This is the terminator-gating half of the reconnect decision, kept
        separate from :meth:`_should_reconnect` (which additionally requires a
        last *dispatched* id and an unexhausted attempt budget). The split lets
        a mid-stream transport error terminate consistently:
        - a stream that can never reconnect (non-resumable, no terminator,
          disabled, or no callback) must re-raise the error to the caller, so a
          truncated stream is not mistaken for a clean completion;
        - a resumable stream that has merely run out of attempts (or has no id
          to resume from) ends cleanly — the same way an exhausted empty/error
          -body resume already does, matching the TypeScript ``return``.
        """
        return (
            self._resumable
            and self._stream_terminator is not None
            and self._stream_reconnection_enabled
            and self._reconnect is not None
        )

    def _should_reconnect(self, last_dispatched_id: Optional[str], reconnect_attempts: int) -> bool:
        """Decide whether a prematurely-ended stream should be reconnected.

        Mirrors the TypeScript ``shouldReconnect`` gating:
        - only resumable SSE endpoints with a configured terminator, reconnect
          enabled, and a reconnect callback are eligible (see
          :meth:`_reconnect_applicable`);
        - a last *dispatched* event id must exist to resume from;
        - the consecutive-failed-attempt cap must not be exceeded.
        """
        if not self._reconnect_applicable():
            return False
        if not last_dispatched_id:
            return False
        max_attempts = (
            self._max_stream_reconnection_attempts
            if self._max_stream_reconnection_attempts is not None
            else DEFAULT_MAX_RECONNECTION_ATTEMPTS
        )
        if reconnect_attempts >= max_attempts:
            return False
        return True

    def _reconnect_delay_seconds(self, last_retry: Optional[int]) -> float:
        """Backoff before a reconnect.

        Uses the server's most recent ``retry:`` directive (milliseconds) when
        present, otherwise a default of ``DEFAULT_RECONNECT_DELAY_MS``, clamped
        to ``MAX_RECONNECT_DELAY_MS``.
        """
        base_ms = last_retry if (last_retry is not None and last_retry > 0) else DEFAULT_RECONNECT_DELAY_MS
        return min(base_ms, MAX_RECONNECT_DELAY_MS) / 1000.0

    def _sleep_before_reconnect(self, last_retry: Optional[int]) -> None:



        time.sleep(self._reconnect_delay_seconds(last_retry))

    async def _asleep_before_reconnect(self, last_retry: Optional[int]) -> None:



        await anyio.sleep(self._reconnect_delay_seconds(last_retry))

    def _decode_response(
        self,
        response: httpx.Response,
        decoder: SSEDecoder,
        text_decoder: "codecs.IncrementalDecoder",
    ) -> Iterator[ServerSentEvent]:
        buf = ""
        for chunk in response.iter_bytes():
            buf += text_decoder.decode(chunk)
            buf = self._normalize_sse_line_endings(buf)

            while "\n" in buf:
                line, buf = buf.split("\n", 1)
                sse = decoder.decode(line)
                if sse is not None:
                    yield sse

            if len(buf) > MAX_LINE_SIZE:
                raise SSEError(
                    f"SSE line exceeded maximum size of {MAX_LINE_SIZE} characters without encountering a newline"
                )

        yield from self._flush_decoder(buf, decoder, text_decoder)

    async def _adecode_response(
        self,
        response: httpx.Response,
        decoder: SSEDecoder,
        text_decoder: "codecs.IncrementalDecoder",
    ) -> AsyncGenerator[ServerSentEvent, None]:
        buf = ""
        async for chunk in response.aiter_bytes():
            buf += text_decoder.decode(chunk)
            buf = self._normalize_sse_line_endings(buf)

            while "\n" in buf:
                line, buf = buf.split("\n", 1)
                sse = decoder.decode(line)
                if sse is not None:
                    yield sse

            if len(buf) > MAX_LINE_SIZE:
                raise SSEError(
                    f"SSE line exceeded maximum size of {MAX_LINE_SIZE} characters without encountering a newline"
                )

        for sse in self._flush_decoder(buf, decoder, text_decoder):
            yield sse

    def _flush_decoder(
        self,
        buf: str,
        decoder: SSEDecoder,
        text_decoder: "codecs.IncrementalDecoder",
    ) -> Iterator[ServerSentEvent]:

        buf += text_decoder.decode(b"", final=True)
        buf = buf.replace("\r\n", "\n").replace("\r", "\n")

        if len(buf) > MAX_LINE_SIZE:
            raise SSEError(
                f"SSE line exceeded maximum size of {MAX_LINE_SIZE} characters without encountering a newline"
            )

        while "\n" in buf:
            line, buf = buf.split("\n", 1)
            sse = decoder.decode(line)
            if sse is not None:
                yield sse

        if buf.strip():
            sse = decoder.decode(buf)
            if sse is not None:
                yield sse

    def iter_sse(self) -> Iterator[ServerSentEvent]:
        self._check_content_type()
        decoder = SSEDecoder()
        text_decoder = self._new_text_decoder()

        last_dispatched_id: Optional[str] = None
        last_retry: Optional[int] = None




        reconnect_attempts = 0




        response: Optional[httpx.Response] = self._response


        owned_cm: Optional[ContextManager[httpx.Response]] = None
        try:
            while True:
                if response is not None:
                    events = self._decode_response(response, decoder, text_decoder)
                    while True:
                        try:
                            sse = next(events)
                        except StopIteration:
                            break
                        except SSEError:




                            raise
                        except httpx.TransportError:












                            if not self._reconnect_applicable():
                                raise
                            break
                        yield sse
                        if sse.id:
                            last_dispatched_id = sse.id
                        if sse.retry is not None:
                            last_retry = sse.retry
                        reconnect_attempts = 0

                if not self._should_reconnect(last_dispatched_id, reconnect_attempts):
                    return
                reconnect_attempts += 1

                self._sleep_before_reconnect(last_retry)



                if owned_cm is not None:
                    owned_cm.__exit__(None, None, None)
                    owned_cm = None

                assert self._reconnect is not None
                try:
                    cm: ContextManager[httpx.Response] = self._reconnect(last_dispatched_id or "")
                    new_response = cm.__enter__()
                except Exception:

                    response = None
                    continue
                owned_cm = cm
                if new_response is None or not self._is_reconnect_response_usable(new_response):


                    response = None
                    continue

                response = new_response



                decoder.reset_in_progress_event()
                text_decoder = self._new_text_decoder(new_response)
        finally:
            if owned_cm is not None:
                owned_cm.__exit__(None, None, None)

    async def aiter_sse(self) -> AsyncGenerator[ServerSentEvent, None]:
        self._check_content_type()
        decoder = SSEDecoder()
        text_decoder = self._new_text_decoder()

        last_dispatched_id: Optional[str] = None
        last_retry: Optional[int] = None
        reconnect_attempts = 0

        response: Optional[httpx.Response] = self._response
        owned_cm: Optional[AsyncContextManager[httpx.Response]] = None
        try:
            while True:
                if response is not None:
                    events = self._adecode_response(response, decoder, text_decoder)
                    while True:
                        try:
                            sse = await events.__anext__()
                        except StopAsyncIteration:
                            break
                        except SSEError:




                            raise
                        except httpx.TransportError:










                            if not self._reconnect_applicable():
                                raise
                            break
                        yield sse
                        if sse.id:
                            last_dispatched_id = sse.id
                        if sse.retry is not None:
                            last_retry = sse.retry
                        reconnect_attempts = 0

                if not self._should_reconnect(last_dispatched_id, reconnect_attempts):
                    return
                reconnect_attempts += 1

                await self._asleep_before_reconnect(last_retry)

                if owned_cm is not None:
                    await owned_cm.__aexit__(None, None, None)
                    owned_cm = None

                assert self._reconnect is not None
                try:
                    cm: AsyncContextManager[httpx.Response] = self._reconnect(last_dispatched_id or "")
                    new_response = await cm.__aenter__()
                except Exception:
                    response = None
                    continue
                owned_cm = cm
                if new_response is None or not self._is_reconnect_response_usable(new_response):
                    response = None
                    continue

                response = new_response
                decoder.reset_in_progress_event()
                text_decoder = self._new_text_decoder(new_response)
        finally:
            if owned_cm is not None:



                with anyio.CancelScope(shield=True):
                    await owned_cm.__aexit__(None, None, None)


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

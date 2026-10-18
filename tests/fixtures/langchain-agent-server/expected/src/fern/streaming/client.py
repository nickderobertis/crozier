

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.protocol_channel import ProtocolChannel
from ..types.protocol_namespace import ProtocolNamespace
from .raw_client import AsyncRawStreamingClient, RawStreamingClient
from .types.protocol_thread_command_post_response import ProtocolThreadCommandPostResponse


OMIT = typing.cast(typing.Any, ...)


class StreamingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStreamingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStreamingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStreamingClient
        """
        return self._raw_client

    def protocol_thread_events_post(
        self,
        thread_id: str,
        *,
        channels: typing.Sequence[ProtocolChannel],
        namespaces: typing.Optional[typing.Sequence[ProtocolNamespace]] = OMIT,
        depth: typing.Optional[int] = OMIT,
        since: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Open a connection-scoped SSE event stream for a thread. The request body is a `ProtocolEventStreamRequest` carrying channel and namespace filters; the server replies with `Content-Type: text/event-stream` and pushes matching `ProtocolEvent` frames for the lifetime of the connection. Closing the connection unsubscribes — no state is persisted server-side.

        Reconnect: clients pass the last `seq` they received as `since` in the body. Buffered events with `seq > since` are replayed before the stream goes live. The endpoint is POST-only, so browser-native `EventSource` auto-resume (`Last-Event-ID`) does not apply — clients drive resume explicitly via the body.

        Parameters
        ----------
        thread_id : str
            The ID of the thread to observe.

        channels : typing.Sequence[ProtocolChannel]
            Channels to subscribe to for the lifetime of this connection.

        namespaces : typing.Optional[typing.Sequence[ProtocolNamespace]]
            Prefix-match filter. An event matches if its namespace starts with any of these prefixes. Omit for all namespaces.

        depth : typing.Optional[int]
            Max depth below the namespace prefix. Omit for unbounded depth.

        since : typing.Optional[int]
            Replay events with `seq` greater than this value before streaming live events.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            SSE event stream

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.streaming.protocol_thread_events_post(
            thread_id="thread_id",
            channels=["channels"],
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.protocol_thread_events_post(
            thread_id,
            channels=channels,
            namespaces=namespaces,
            depth=depth,
            since=since,
            request_options=request_options,
        ) as r:
            yield from r.data

    def protocol_thread_command_post(
        self,
        thread_id: str,
        *,
        id: int,
        method: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProtocolThreadCommandPostResponse:
        """
        Send a single protocol command scoped to a thread. The request body is a `ProtocolCommand` envelope with a `method` (e.g. `run.start`, `input.respond`, `agent.getTree`) and method-specific `params`. The response is either a `ProtocolSuccess` (with method-specific `result`) or a `ProtocolError`.

        Commands that create runs (`run.start`, `input.respond`) leave the run executing in the background on the worker queue. Event streaming for that run is observed via a concurrent `POST /threads/{thread_id}/stream/events` connection.

        WebSocket clients use the same command envelope in-band on `/threads/{thread_id}/stream/events` and additionally have access to `subscription.subscribe` / `subscription.unsubscribe` over the same connection.

        Parameters
        ----------
        thread_id : str
            The ID of the thread the command applies to.

        id : int
            Client-assigned command id; echoed in the response.

        method : str
            Command method name (e.g. `run.start`).

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Method-specific parameters. See the CDDL spec for per-method shapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtocolThreadCommandPostResponse
            Protocol response — either `ProtocolSuccess` or `ProtocolError`.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.streaming.protocol_thread_command_post(
            thread_id="thread_id",
            id=1,
            method="method",
        )
        """
        _response = self._raw_client.protocol_thread_command_post(
            thread_id, id=id, method=method, params=params, request_options=request_options
        )
        return _response.data


class AsyncStreamingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStreamingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStreamingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStreamingClient
        """
        return self._raw_client

    async def protocol_thread_events_post(
        self,
        thread_id: str,
        *,
        channels: typing.Sequence[ProtocolChannel],
        namespaces: typing.Optional[typing.Sequence[ProtocolNamespace]] = OMIT,
        depth: typing.Optional[int] = OMIT,
        since: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Open a connection-scoped SSE event stream for a thread. The request body is a `ProtocolEventStreamRequest` carrying channel and namespace filters; the server replies with `Content-Type: text/event-stream` and pushes matching `ProtocolEvent` frames for the lifetime of the connection. Closing the connection unsubscribes — no state is persisted server-side.

        Reconnect: clients pass the last `seq` they received as `since` in the body. Buffered events with `seq > since` are replayed before the stream goes live. The endpoint is POST-only, so browser-native `EventSource` auto-resume (`Last-Event-ID`) does not apply — clients drive resume explicitly via the body.

        Parameters
        ----------
        thread_id : str
            The ID of the thread to observe.

        channels : typing.Sequence[ProtocolChannel]
            Channels to subscribe to for the lifetime of this connection.

        namespaces : typing.Optional[typing.Sequence[ProtocolNamespace]]
            Prefix-match filter. An event matches if its namespace starts with any of these prefixes. Omit for all namespaces.

        depth : typing.Optional[int]
            Max depth below the namespace prefix. Omit for unbounded depth.

        since : typing.Optional[int]
            Replay events with `seq` greater than this value before streaming live events.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            SSE event stream

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = client.streaming.protocol_thread_events_post(
                thread_id="thread_id",
                channels=["channels"],
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.protocol_thread_events_post(
            thread_id,
            channels=channels,
            namespaces=namespaces,
            depth=depth,
            since=since,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def protocol_thread_command_post(
        self,
        thread_id: str,
        *,
        id: int,
        method: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProtocolThreadCommandPostResponse:
        """
        Send a single protocol command scoped to a thread. The request body is a `ProtocolCommand` envelope with a `method` (e.g. `run.start`, `input.respond`, `agent.getTree`) and method-specific `params`. The response is either a `ProtocolSuccess` (with method-specific `result`) or a `ProtocolError`.

        Commands that create runs (`run.start`, `input.respond`) leave the run executing in the background on the worker queue. Event streaming for that run is observed via a concurrent `POST /threads/{thread_id}/stream/events` connection.

        WebSocket clients use the same command envelope in-band on `/threads/{thread_id}/stream/events` and additionally have access to `subscription.subscribe` / `subscription.unsubscribe` over the same connection.

        Parameters
        ----------
        thread_id : str
            The ID of the thread the command applies to.

        id : int
            Client-assigned command id; echoed in the response.

        method : str
            Command method name (e.g. `run.start`).

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Method-specific parameters. See the CDDL spec for per-method shapes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProtocolThreadCommandPostResponse
            Protocol response — either `ProtocolSuccess` or `ProtocolError`.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.streaming.protocol_thread_command_post(
                thread_id="thread_id",
                id=1,
                method="method",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_thread_command_post(
            thread_id, id=id, method=method, params=params, request_options=request_options
        )
        return _response.data

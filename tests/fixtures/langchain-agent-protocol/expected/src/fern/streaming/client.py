

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.streaming_channel import StreamingChannel
from ..types.streaming_command_response import StreamingCommandResponse
from ..types.streaming_namespace import StreamingNamespace
from .raw_client import AsyncRawStreamingClient, RawStreamingClient


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

    def open_thread_websocket_stream(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Upgrade to a WebSocket connection for a thread. After the connection is upgraded, clients send streaming protocol commands in-band and receive command responses plus unsolicited events on the same connection. Use `subscription.subscribe`, `subscription.unsubscribe`, and `subscription.reconnect` to manage event filters on the WebSocket.

        Parameters
        ----------
        thread_id : str
            The ID of the thread to open over WebSocket.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.streaming.open_thread_websocket_stream(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.open_thread_websocket_stream(thread_id, request_options=request_options)
        return _response.data

    def open_thread_sse_stream(
        self,
        thread_id: str,
        *,
        channels: typing.Sequence[StreamingChannel],
        namespaces: typing.Optional[typing.Sequence[StreamingNamespace]] = OMIT,
        depth: typing.Optional[int] = OMIT,
        since: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Open a connection-scoped Server-Sent Events stream for a thread. The request body selects channels, namespace prefixes, optional namespace depth, and an optional sequence number to replay buffered events after. Closing the HTTP connection unsubscribes from this stream.

        Parameters
        ----------
        thread_id : str
            The ID of the thread whose events should be streamed.

        channels : typing.Sequence[StreamingChannel]
            Channels to include in this event stream.

        namespaces : typing.Optional[typing.Sequence[StreamingNamespace]]
            Namespace prefixes to include. Omit to receive matching events from all namespaces.

        depth : typing.Optional[int]
            Maximum depth below each namespace prefix.

        since : typing.Optional[int]
            Replay buffered matching events after this monotonic sequence number, then switch to live delivery.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            A filtered stream of protocol events in SSE format.

        Examples
        --------
        from fern import FernApi, StreamingChannelZero

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.streaming.open_thread_sse_stream(
            thread_id="thread_id",
            channels=[StreamingChannelZero.VALUES],
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.open_thread_sse_stream(
            thread_id,
            channels=channels,
            namespaces=namespaces,
            depth=depth,
            since=since,
            request_options=request_options,
        ) as r:
            yield from r.data

    def send_thread_streaming_command(
        self,
        thread_id: str,
        *,
        id: int,
        method: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreamingCommandResponse:
        """
        Send a streaming protocol command to a thread over HTTP. This endpoint is the request/response companion to the SSE event stream and supports commands such as `run.start`, `input.respond`, `input.inject`, `state.get`, `state.listCheckpoints`, and `state.fork`.

        Parameters
        ----------
        thread_id : str
            The ID of the thread that should receive the command.

        id : int
            Client-assigned command ID used to correlate the command response.

        method : str
            Streaming protocol command method, such as `run.start`, `subscription.subscribe`, `input.respond`, or `state.get`.

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Command parameters. Shape depends on the command method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamingCommandResponse
            Command response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.streaming.send_thread_streaming_command(
            thread_id="thread_id",
            id=1,
            method="method",
        )
        """
        _response = self._raw_client.send_thread_streaming_command(
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

    async def open_thread_websocket_stream(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Upgrade to a WebSocket connection for a thread. After the connection is upgraded, clients send streaming protocol commands in-band and receive command responses plus unsolicited events on the same connection. Use `subscription.subscribe`, `subscription.unsubscribe`, and `subscription.reconnect` to manage event filters on the WebSocket.

        Parameters
        ----------
        thread_id : str
            The ID of the thread to open over WebSocket.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.streaming.open_thread_websocket_stream(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.open_thread_websocket_stream(thread_id, request_options=request_options)
        return _response.data

    async def open_thread_sse_stream(
        self,
        thread_id: str,
        *,
        channels: typing.Sequence[StreamingChannel],
        namespaces: typing.Optional[typing.Sequence[StreamingNamespace]] = OMIT,
        depth: typing.Optional[int] = OMIT,
        since: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Open a connection-scoped Server-Sent Events stream for a thread. The request body selects channels, namespace prefixes, optional namespace depth, and an optional sequence number to replay buffered events after. Closing the HTTP connection unsubscribes from this stream.

        Parameters
        ----------
        thread_id : str
            The ID of the thread whose events should be streamed.

        channels : typing.Sequence[StreamingChannel]
            Channels to include in this event stream.

        namespaces : typing.Optional[typing.Sequence[StreamingNamespace]]
            Namespace prefixes to include. Omit to receive matching events from all namespaces.

        depth : typing.Optional[int]
            Maximum depth below each namespace prefix.

        since : typing.Optional[int]
            Replay buffered matching events after this monotonic sequence number, then switch to live delivery.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            A filtered stream of protocol events in SSE format.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, StreamingChannelZero

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.streaming.open_thread_sse_stream(
                thread_id="thread_id",
                channels=[StreamingChannelZero.VALUES],
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.open_thread_sse_stream(
            thread_id,
            channels=channels,
            namespaces=namespaces,
            depth=depth,
            since=since,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def send_thread_streaming_command(
        self,
        thread_id: str,
        *,
        id: int,
        method: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreamingCommandResponse:
        """
        Send a streaming protocol command to a thread over HTTP. This endpoint is the request/response companion to the SSE event stream and supports commands such as `run.start`, `input.respond`, `input.inject`, `state.get`, `state.listCheckpoints`, and `state.fork`.

        Parameters
        ----------
        thread_id : str
            The ID of the thread that should receive the command.

        id : int
            Client-assigned command ID used to correlate the command response.

        method : str
            Streaming protocol command method, such as `run.start`, `subscription.subscribe`, `input.respond`, or `state.get`.

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Command parameters. Shape depends on the command method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamingCommandResponse
            Command response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.streaming.send_thread_streaming_command(
                thread_id="thread_id",
                id=1,
                method="method",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_thread_streaming_command(
            thread_id, id=id, method=method, params=params, request_options=request_options
        )
        return _response.data

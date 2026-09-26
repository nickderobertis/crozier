

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.mcp_json_rpc_response import McpJsonRpcResponse
from .raw_client import AsyncRawMcpProtocolClient, RawMcpProtocolClient
from .types.mcp_json_rpc_request_id import McpJsonRpcRequestId
from .types.mcp_json_rpc_request_jsonrpc import McpJsonRpcRequestJsonrpc


OMIT = typing.cast(typing.Any, ...)


class McpProtocolClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMcpProtocolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMcpProtocolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMcpProtocolClient
        """
        return self._raw_client

    def open_mcp_sse_stream(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[str]:
        """
        Opens a Server-Sent Events (SSE) stream for Model Context Protocol communication. This endpoint allows the server to push messages to the client without the client first sending data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            SSE stream opened successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        response = client.mcp_protocol.open_mcp_sse_stream()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.open_mcp_sse_stream(request_options=request_options) as r:
            yield from r.data

    def send_mcp_json_rpc_message(
        self,
        *,
        jsonrpc: McpJsonRpcRequestJsonrpc,
        method: str,
        id: typing.Optional[McpJsonRpcRequestId] = OMIT,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpJsonRpcResponse:
        """
        Send a JSON-RPC message using Model Context Protocol. Used for tool calls, initialization, and other MCP operations. The server may respond with either a JSON object or open an SSE stream.

        Parameters
        ----------
        jsonrpc : McpJsonRpcRequestJsonrpc
            JSON-RPC version

        method : str
            Method name (e.g., initialize, tools/call, tools/list)

        id : typing.Optional[McpJsonRpcRequestId]
            Request identifier

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Method parameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpJsonRpcResponse
            JSON-RPC response or SSE stream

        Examples
        --------
        from fern.mcp_protocol import McpJsonRpcRequestJsonrpc

        from fern import FernApi

        client = FernApi()
        client.mcp_protocol.send_mcp_json_rpc_message(
            jsonrpc=McpJsonRpcRequestJsonrpc.TWO0,
            id=1.0,
            method="initialize",
            params={
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "example-client", "version": "1.0.0"},
            },
        )
        """
        _response = self._raw_client.send_mcp_json_rpc_message(
            jsonrpc=jsonrpc, method=method, id=id, params=params, request_options=request_options
        )
        return _response.data


class AsyncMcpProtocolClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMcpProtocolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMcpProtocolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMcpProtocolClient
        """
        return self._raw_client

    async def open_mcp_sse_stream(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[str]:
        """
        Opens a Server-Sent Events (SSE) stream for Model Context Protocol communication. This endpoint allows the server to push messages to the client without the client first sending data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            SSE stream opened successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            response = await client.mcp_protocol.open_mcp_sse_stream()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.open_mcp_sse_stream(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def send_mcp_json_rpc_message(
        self,
        *,
        jsonrpc: McpJsonRpcRequestJsonrpc,
        method: str,
        id: typing.Optional[McpJsonRpcRequestId] = OMIT,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpJsonRpcResponse:
        """
        Send a JSON-RPC message using Model Context Protocol. Used for tool calls, initialization, and other MCP operations. The server may respond with either a JSON object or open an SSE stream.

        Parameters
        ----------
        jsonrpc : McpJsonRpcRequestJsonrpc
            JSON-RPC version

        method : str
            Method name (e.g., initialize, tools/call, tools/list)

        id : typing.Optional[McpJsonRpcRequestId]
            Request identifier

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Method parameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpJsonRpcResponse
            JSON-RPC response or SSE stream

        Examples
        --------
        import asyncio

        from fern.mcp_protocol import McpJsonRpcRequestJsonrpc

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.mcp_protocol.send_mcp_json_rpc_message(
                jsonrpc=McpJsonRpcRequestJsonrpc.TWO0,
                id=1.0,
                method="initialize",
                params={
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {"name": "example-client", "version": "1.0.0"},
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_mcp_json_rpc_message(
            jsonrpc=jsonrpc, method=method, id=id, params=params, request_options=request_options
        )
        return _response.data

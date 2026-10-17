

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMcpClient, RawMcpClient
from .types.post_mcp_request_accept import PostMcpRequestAccept


OMIT = typing.cast(typing.Any, ...)


class McpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMcpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMcpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMcpClient
        """
        return self._raw_client

    def get_mcp(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Implemented according to the Streamable HTTP Transport specification.

        Parameters
        ----------
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
        client.mcp.get_mcp()
        """
        _response = self._raw_client.get_mcp(request_options=request_options)
        return _response.data

    def post_mcp(
        self,
        *,
        accept: PostMcpRequestAccept,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Implemented according to the Streamable HTTP Transport specification.
        Sends a JSON-RPC 2.0 message to the server.

        - **Request**: Provide an object with `jsonrpc`, `id`, `method`, and optional `params`.
        - **Response**: Returns a JSON-RPC response or acknowledgment.

        **Notes:**
        - Stateless: Sessions are not persisted across requests.

        Parameters
        ----------
        accept : PostMcpRequestAccept
            Accept header must include both 'application/json' and 'text/event-stream' media types.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful JSON-RPC response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp.post_mcp(
            accept="application/json, text/event-stream",
            request={
                "jsonrpc": "2.0",
                "id": "1",
                "method": "initialize",
                "params": {
                    "clientInfo": {"name": "test_client", "version": "1.0.0"},
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                },
            },
        )
        """
        _response = self._raw_client.post_mcp(accept=accept, request=request, request_options=request_options)
        return _response.data

    def delete_mcp(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Implemented according to the Streamable HTTP Transport specification.
        Terminate an MCP session. The server implementation is stateless, so this is a no-op.

        Parameters
        ----------
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
        client.mcp.delete_mcp()
        """
        _response = self._raw_client.delete_mcp(request_options=request_options)
        return _response.data


class AsyncMcpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMcpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMcpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMcpClient
        """
        return self._raw_client

    async def get_mcp(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Implemented according to the Streamable HTTP Transport specification.

        Parameters
        ----------
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
            await client.mcp.get_mcp()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mcp(request_options=request_options)
        return _response.data

    async def post_mcp(
        self,
        *,
        accept: PostMcpRequestAccept,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Implemented according to the Streamable HTTP Transport specification.
        Sends a JSON-RPC 2.0 message to the server.

        - **Request**: Provide an object with `jsonrpc`, `id`, `method`, and optional `params`.
        - **Response**: Returns a JSON-RPC response or acknowledgment.

        **Notes:**
        - Stateless: Sessions are not persisted across requests.

        Parameters
        ----------
        accept : PostMcpRequestAccept
            Accept header must include both 'application/json' and 'text/event-stream' media types.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful JSON-RPC response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp.post_mcp(
                accept="application/json, text/event-stream",
                request={
                    "jsonrpc": "2.0",
                    "id": "1",
                    "method": "initialize",
                    "params": {
                        "clientInfo": {"name": "test_client", "version": "1.0.0"},
                        "protocolVersion": "2024-11-05",
                        "capabilities": {},
                    },
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_mcp(accept=accept, request=request, request_options=request_options)
        return _response.data

    async def delete_mcp(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Implemented according to the Streamable HTTP Transport specification.
        Terminate an MCP session. The server implementation is stateless, so this is a no-op.

        Parameters
        ----------
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
            await client.mcp.delete_mcp()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_mcp(request_options=request_options)
        return _response.data

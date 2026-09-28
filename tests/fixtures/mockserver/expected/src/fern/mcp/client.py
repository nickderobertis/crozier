

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMcpClient, RawMcpClient


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

    def not_supported(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Documented so the behaviour is not mistaken for SSE support: MockServer's MCP endpoint does not implement the server-initiated SSE stream, and a GET is always refused.

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

        client = FernApi()
        client.mcp.not_supported()
        """
        _response = self._raw_client.not_supported(request_options=request_options)
        return _response.data

    def mcp_model_context_protocol_json_rpc_endpoint(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        mcp_session_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Streamable-HTTP MCP endpoint, letting AI agents and LLM tooling drive MockServer as an MCP server. The body is a JSON-RPC 2.0 request object or a batch array. Call `initialize` first; the response carries a new session id in the `Mcp-Session-Id` response header, which subsequent calls must send back in the `Mcp-Session-Id` request header. Protocol versions 2025-06-18 (default), 2025-03-26 and 2024-11-05 are negotiated. Note that a missing or invalid session is reported as a JSON-RPC error inside a 200 response, not as a 4xx. Unlike its sibling endpoints this path has no bare `/mcp` alias, and sub-paths under `/mockserver/mcp/` also route here.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        mcp_session_id : typing.Optional[str]
            session id returned by a previous `initialize` call; omit on `initialize` itself

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON-RPC response. Also used for JSON-RPC-level errors such as an missing or invalid session. On `initialize` the response carries the new session id in the Mcp-Session-Id header.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.mcp.mcp_model_context_protocol_json_rpc_endpoint(
            request={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2025-06-18",
                    "capabilities": {},
                    "clientInfo": {"name": "example-client", "version": "1.0.0"},
                },
            },
        )
        """
        _response = self._raw_client.mcp_model_context_protocol_json_rpc_endpoint(
            request=request, mcp_session_id=mcp_session_id, request_options=request_options
        )
        return _response.data

    def end_an_mcp_session(
        self, *, mcp_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes the MCP session identified by the `Mcp-Session-Id` request header.

        Parameters
        ----------
        mcp_session_id : str
            the session to end

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.mcp.end_an_mcp_session(
            mcp_session_id="Mcp-Session-Id",
        )
        """
        _response = self._raw_client.end_an_mcp_session(mcp_session_id=mcp_session_id, request_options=request_options)
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

    async def not_supported(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Documented so the behaviour is not mistaken for SSE support: MockServer's MCP endpoint does not implement the server-initiated SSE stream, and a GET is always refused.

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

        client = AsyncFernApi()


        async def main() -> None:
            await client.mcp.not_supported()


        asyncio.run(main())
        """
        _response = await self._raw_client.not_supported(request_options=request_options)
        return _response.data

    async def mcp_model_context_protocol_json_rpc_endpoint(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        mcp_session_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Streamable-HTTP MCP endpoint, letting AI agents and LLM tooling drive MockServer as an MCP server. The body is a JSON-RPC 2.0 request object or a batch array. Call `initialize` first; the response carries a new session id in the `Mcp-Session-Id` response header, which subsequent calls must send back in the `Mcp-Session-Id` request header. Protocol versions 2025-06-18 (default), 2025-03-26 and 2024-11-05 are negotiated. Note that a missing or invalid session is reported as a JSON-RPC error inside a 200 response, not as a 4xx. Unlike its sibling endpoints this path has no bare `/mcp` alias, and sub-paths under `/mockserver/mcp/` also route here.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        mcp_session_id : typing.Optional[str]
            session id returned by a previous `initialize` call; omit on `initialize` itself

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON-RPC response. Also used for JSON-RPC-level errors such as an missing or invalid session. On `initialize` the response carries the new session id in the Mcp-Session-Id header.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.mcp.mcp_model_context_protocol_json_rpc_endpoint(
                request={
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "initialize",
                    "params": {
                        "protocolVersion": "2025-06-18",
                        "capabilities": {},
                        "clientInfo": {"name": "example-client", "version": "1.0.0"},
                    },
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_model_context_protocol_json_rpc_endpoint(
            request=request, mcp_session_id=mcp_session_id, request_options=request_options
        )
        return _response.data

    async def end_an_mcp_session(
        self, *, mcp_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes the MCP session identified by the `Mcp-Session-Id` request header.

        Parameters
        ----------
        mcp_session_id : str
            the session to end

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.mcp.end_an_mcp_session(
                mcp_session_id="Mcp-Session-Id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.end_an_mcp_session(
            mcp_session_id=mcp_session_id, request_options=request_options
        )
        return _response.data

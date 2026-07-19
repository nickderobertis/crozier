

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tool import Tool
from ..types.tool_execution_result import ToolExecutionResult
from .raw_client import AsyncRawMcpServersClient, RawMcpServersClient
from .types.create_mcp_server_request_config import CreateMcpServerRequestConfig
from .types.mcp_create_mcp_server_response import McpCreateMcpServerResponse
from .types.mcp_list_mcp_servers_response_item import McpListMcpServersResponseItem
from .types.mcp_retrieve_mcp_server_response import McpRetrieveMcpServerResponse
from .types.mcp_update_mcp_server_response import McpUpdateMcpServerResponse
from .types.update_mcp_server_request_config import UpdateMcpServerRequestConfig


OMIT = typing.cast(typing.Any, ...)


class McpServersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMcpServersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMcpServersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMcpServersClient
        """
        return self._raw_client

    def mcp_list_mcp_servers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[McpListMcpServersResponseItem]:
        """
        Get a list of all configured MCP servers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[McpListMcpServersResponseItem]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_list_mcp_servers()
        """
        _response = self._raw_client.mcp_list_mcp_servers(request_options=request_options)
        return _response.data

    def mcp_create_mcp_server(
        self,
        *,
        server_name: str,
        config: CreateMcpServerRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpCreateMcpServerResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Parameters
        ----------
        server_name : str
            The name of the MCP server

        config : CreateMcpServerRequestConfig
            The MCP server configuration (Stdio, SSE, or Streamable HTTP)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpCreateMcpServerResponse
            Successful Response

        Examples
        --------
        from fern.mcp_servers import CreateMcpServerRequestConfig_Sse

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_create_mcp_server(
            server_name="server_name",
            config=CreateMcpServerRequestConfig_Sse(
                server_url="server_url",
            ),
        )
        """
        _response = self._raw_client.mcp_create_mcp_server(
            server_name=server_name, config=config, request_options=request_options
        )
        return _response.data

    def mcp_retrieve_mcp_server(
        self, mcp_server_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> McpRetrieveMcpServerResponse:
        """
        Get a specific MCP server

        Parameters
        ----------
        mcp_server_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpRetrieveMcpServerResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_retrieve_mcp_server(
            mcp_server_id="mcp_server_id",
        )
        """
        _response = self._raw_client.mcp_retrieve_mcp_server(mcp_server_id, request_options=request_options)
        return _response.data

    def mcp_delete_mcp_server(
        self, mcp_server_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an MCP server by its ID

        Parameters
        ----------
        mcp_server_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_delete_mcp_server(
            mcp_server_id="mcp_server_id",
        )
        """
        _response = self._raw_client.mcp_delete_mcp_server(mcp_server_id, request_options=request_options)
        return _response.data

    def mcp_update_mcp_server(
        self,
        mcp_server_id: str,
        *,
        config: UpdateMcpServerRequestConfig,
        server_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpUpdateMcpServerResponse:
        """
        Update an existing MCP server configuration

        Parameters
        ----------
        mcp_server_id : str

        config : UpdateMcpServerRequestConfig
            The MCP server configuration updates (Stdio, SSE, or Streamable HTTP)

        server_name : typing.Optional[str]
            The name of the MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpUpdateMcpServerResponse
            Successful Response

        Examples
        --------
        from fern.mcp_servers import UpdateMcpServerRequestConfig_Sse

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_update_mcp_server(
            mcp_server_id="mcp_server_id",
            config=UpdateMcpServerRequestConfig_Sse(),
        )
        """
        _response = self._raw_client.mcp_update_mcp_server(
            mcp_server_id, config=config, server_name=server_name, request_options=request_options
        )
        return _response.data

    def mcp_list_tools_for_mcp_server(
        self, mcp_server_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Tool]:
        """
        Get a list of all tools for a specific MCP server

        Parameters
        ----------
        mcp_server_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tool]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_list_tools_for_mcp_server(
            mcp_server_id="mcp_server_id",
        )
        """
        _response = self._raw_client.mcp_list_tools_for_mcp_server(mcp_server_id, request_options=request_options)
        return _response.data

    def mcp_retrieve_mcp_tool(
        self, mcp_server_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tool:
        """
        Get a specific MCP tool by its ID

        Parameters
        ----------
        mcp_server_id : str

        tool_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tool
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_retrieve_mcp_tool(
            mcp_server_id="mcp_server_id",
            tool_id="tool_id",
        )
        """
        _response = self._raw_client.mcp_retrieve_mcp_tool(mcp_server_id, tool_id, request_options=request_options)
        return _response.data

    def mcp_run_tool(
        self,
        mcp_server_id: str,
        tool_id: str,
        *,
        args: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResult:
        """
        Execute a specific MCP tool

        The request body should contain the tool arguments in the ToolExecuteRequest format.

        Parameters
        ----------
        mcp_server_id : str

        tool_id : str

        args : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the tool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_run_tool(
            mcp_server_id="mcp_server_id",
            tool_id="tool_id",
        )
        """
        _response = self._raw_client.mcp_run_tool(mcp_server_id, tool_id, args=args, request_options=request_options)
        return _response.data

    def mcp_refresh_mcp_server_tools(
        self,
        mcp_server_id: str,
        *,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Refresh tools for an MCP server by:
        1. Fetching current tools from the MCP server
        2. Deleting tools that no longer exist on the server
        3. Updating schemas for existing tools
        4. Adding new tools from the server

        Returns a summary of changes made.

        Parameters
        ----------
        mcp_server_id : str

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_refresh_mcp_server_tools(
            mcp_server_id="mcp_server_id",
        )
        """
        _response = self._raw_client.mcp_refresh_mcp_server_tools(
            mcp_server_id, agent_id=agent_id, request_options=request_options
        )
        return _response.data

    def mcp_connect_mcp_server(
        self, mcp_server_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Connect to an MCP server with support for OAuth via SSE.
        Returns a stream of events handling authorization state and exchange if OAuth is required.

        Parameters
        ----------
        mcp_server_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.mcp_connect_mcp_server(
            mcp_server_id="mcp_server_id",
        )
        """
        _response = self._raw_client.mcp_connect_mcp_server(mcp_server_id, request_options=request_options)
        return _response.data


class AsyncMcpServersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMcpServersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMcpServersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMcpServersClient
        """
        return self._raw_client

    async def mcp_list_mcp_servers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[McpListMcpServersResponseItem]:
        """
        Get a list of all configured MCP servers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[McpListMcpServersResponseItem]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_list_mcp_servers()


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_list_mcp_servers(request_options=request_options)
        return _response.data

    async def mcp_create_mcp_server(
        self,
        *,
        server_name: str,
        config: CreateMcpServerRequestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpCreateMcpServerResponse:
        """
        Add a new MCP server to the Letta MCP server config

        Parameters
        ----------
        server_name : str
            The name of the MCP server

        config : CreateMcpServerRequestConfig
            The MCP server configuration (Stdio, SSE, or Streamable HTTP)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpCreateMcpServerResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.mcp_servers import CreateMcpServerRequestConfig_Sse

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_create_mcp_server(
                server_name="server_name",
                config=CreateMcpServerRequestConfig_Sse(
                    server_url="server_url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_create_mcp_server(
            server_name=server_name, config=config, request_options=request_options
        )
        return _response.data

    async def mcp_retrieve_mcp_server(
        self, mcp_server_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> McpRetrieveMcpServerResponse:
        """
        Get a specific MCP server

        Parameters
        ----------
        mcp_server_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpRetrieveMcpServerResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_retrieve_mcp_server(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_retrieve_mcp_server(mcp_server_id, request_options=request_options)
        return _response.data

    async def mcp_delete_mcp_server(
        self, mcp_server_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an MCP server by its ID

        Parameters
        ----------
        mcp_server_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_delete_mcp_server(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_delete_mcp_server(mcp_server_id, request_options=request_options)
        return _response.data

    async def mcp_update_mcp_server(
        self,
        mcp_server_id: str,
        *,
        config: UpdateMcpServerRequestConfig,
        server_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpUpdateMcpServerResponse:
        """
        Update an existing MCP server configuration

        Parameters
        ----------
        mcp_server_id : str

        config : UpdateMcpServerRequestConfig
            The MCP server configuration updates (Stdio, SSE, or Streamable HTTP)

        server_name : typing.Optional[str]
            The name of the MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpUpdateMcpServerResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.mcp_servers import UpdateMcpServerRequestConfig_Sse

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_update_mcp_server(
                mcp_server_id="mcp_server_id",
                config=UpdateMcpServerRequestConfig_Sse(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_update_mcp_server(
            mcp_server_id, config=config, server_name=server_name, request_options=request_options
        )
        return _response.data

    async def mcp_list_tools_for_mcp_server(
        self, mcp_server_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Tool]:
        """
        Get a list of all tools for a specific MCP server

        Parameters
        ----------
        mcp_server_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tool]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_list_tools_for_mcp_server(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_list_tools_for_mcp_server(mcp_server_id, request_options=request_options)
        return _response.data

    async def mcp_retrieve_mcp_tool(
        self, mcp_server_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tool:
        """
        Get a specific MCP tool by its ID

        Parameters
        ----------
        mcp_server_id : str

        tool_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tool
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_retrieve_mcp_tool(
                mcp_server_id="mcp_server_id",
                tool_id="tool_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_retrieve_mcp_tool(
            mcp_server_id, tool_id, request_options=request_options
        )
        return _response.data

    async def mcp_run_tool(
        self,
        mcp_server_id: str,
        tool_id: str,
        *,
        args: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResult:
        """
        Execute a specific MCP tool

        The request body should contain the tool arguments in the ToolExecuteRequest format.

        Parameters
        ----------
        mcp_server_id : str

        tool_id : str

        args : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the tool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_run_tool(
                mcp_server_id="mcp_server_id",
                tool_id="tool_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_run_tool(
            mcp_server_id, tool_id, args=args, request_options=request_options
        )
        return _response.data

    async def mcp_refresh_mcp_server_tools(
        self,
        mcp_server_id: str,
        *,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Refresh tools for an MCP server by:
        1. Fetching current tools from the MCP server
        2. Deleting tools that no longer exist on the server
        3. Updating schemas for existing tools
        4. Adding new tools from the server

        Returns a summary of changes made.

        Parameters
        ----------
        mcp_server_id : str

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_refresh_mcp_server_tools(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_refresh_mcp_server_tools(
            mcp_server_id, agent_id=agent_id, request_options=request_options
        )
        return _response.data

    async def mcp_connect_mcp_server(
        self, mcp_server_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Connect to an MCP server with support for OAuth via SSE.
        Returns a stream of events handling authorization state and exchange if OAuth is required.

        Parameters
        ----------
        mcp_server_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.mcp_connect_mcp_server(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_connect_mcp_server(mcp_server_id, request_options=request_options)
        return _response.data

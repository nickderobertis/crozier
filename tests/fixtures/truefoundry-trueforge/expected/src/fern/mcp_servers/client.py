

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.available_mcp_server import AvailableMcpServer
from ..types.get_mcp_server_response import GetMcpServerResponse
from ..types.list_available_mcp_servers_response import ListAvailableMcpServersResponse
from ..types.list_mcp_server_tools_response import ListMcpServerToolsResponse
from ..types.mcp_auth_status import McpAuthStatus
from .raw_client import AsyncRawMcpServersClient, RawMcpServersClient


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

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[AvailableMcpServer, ListAvailableMcpServersResponse]:
        """
        Paginated MCP servers as a slim name/url list for the composer.

        Parameters
        ----------
        limit : typing.Optional[int]
            Page size. Defaults to 100, max 200.

        page_token : typing.Optional[str]
            Opaque token from a previous response `next_page_token`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[AvailableMcpServer, ListAvailableMcpServersResponse]
            Paginated MCP servers (chat projection).

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.mcp_servers.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(limit=limit, page_token=page_token, request_options=request_options)

    def authorize(
        self,
        name: str,
        *,
        return_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpAuthStatus:
        """
        Returns current auth status. When OAuth is required, includes an authorization URL. Optional return_to is the post-consent landing path.

        Parameters
        ----------
        name : str
            MCP server name.

        return_to : typing.Optional[str]
            Same-origin path to land in the browser after consent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpAuthStatus
            Either already authenticated, or an authorization URL to redirect to.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_servers.authorize(
            name="name",
        )
        """
        _response = self._raw_client.authorize(name, return_to=return_to, request_options=request_options)
        return _response.data

    def delete_authorization(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMcpServerResponse:
        """
        Disconnects OAuth for the MCP server when applicable and returns the updated server with auth_status. No-op when the server does not use stored OAuth tokens.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            The MCP server after disconnect.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_servers.delete_authorization(
            name="name",
        )
        """
        _response = self._raw_client.delete_authorization(name, request_options=request_options)
        return _response.data

    def list_tools(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListMcpServerToolsResponse:
        """
        All tools exposed by the given MCP server (non-paginated), as returned by the MCP `tools/list` call.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMcpServerToolsResponse
            All tools of the MCP server.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.mcp_servers.list_tools(
            name="name",
        )
        """
        _response = self._raw_client.list_tools(name, request_options=request_options)
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

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[AvailableMcpServer, ListAvailableMcpServersResponse]:
        """
        Paginated MCP servers as a slim name/url list for the composer.

        Parameters
        ----------
        limit : typing.Optional[int]
            Page size. Defaults to 100, max 200.

        page_token : typing.Optional[str]
            Opaque token from a previous response `next_page_token`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[AvailableMcpServer, ListAvailableMcpServersResponse]
            Paginated MCP servers (chat projection).

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.mcp_servers.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(limit=limit, page_token=page_token, request_options=request_options)

    async def authorize(
        self,
        name: str,
        *,
        return_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpAuthStatus:
        """
        Returns current auth status. When OAuth is required, includes an authorization URL. Optional return_to is the post-consent landing path.

        Parameters
        ----------
        name : str
            MCP server name.

        return_to : typing.Optional[str]
            Same-origin path to land in the browser after consent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpAuthStatus
            Either already authenticated, or an authorization URL to redirect to.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_servers.authorize(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authorize(name, return_to=return_to, request_options=request_options)
        return _response.data

    async def delete_authorization(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMcpServerResponse:
        """
        Disconnects OAuth for the MCP server when applicable and returns the updated server with auth_status. No-op when the server does not use stored OAuth tokens.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            The MCP server after disconnect.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_servers.delete_authorization(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_authorization(name, request_options=request_options)
        return _response.data

    async def list_tools(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListMcpServerToolsResponse:
        """
        All tools exposed by the given MCP server (non-paginated), as returned by the MCP `tools/list` call.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMcpServerToolsResponse
            All tools of the MCP server.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.mcp_servers.list_tools(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tools(name, request_options=request_options)
        return _response.data

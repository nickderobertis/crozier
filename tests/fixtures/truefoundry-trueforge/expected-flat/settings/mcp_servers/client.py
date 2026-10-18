

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.pagination import AsyncPager, SyncPager
from ...core.request_options import RequestOptions
from ...types.configured_mcp_server import ConfiguredMcpServer
from ...types.get_mcp_server_response import GetMcpServerResponse
from ...types.list_mcp_servers_response import ListMcpServersResponse
from ...types.mcp_server_manifest import McpServerManifest
from .raw_client import AsyncRawMcpServersClient, RawMcpServersClient


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

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ConfiguredMcpServer, ListMcpServersResponse]:
        """
        Paginated MCP servers with auth_status. Header secrets are redacted.

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
        SyncPager[ConfiguredMcpServer, ListMcpServersResponse]
            Paginated MCP servers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.settings.mcp_servers.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(limit=limit, page_token=page_token, request_options=request_options)

    def create(
        self, *, manifest: McpServerManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMcpServerResponse:
        """
        Creates an MCP server by `name`. Fails if `name` is already taken. Runs DCR registration when `auth.type` is `dcr`. Header secrets: real value required; redacted with no stored value returns 400.

        Parameters
        ----------
        manifest : McpServerManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            The created MCP server with auth_status

        Examples
        --------
        from fern import FernApi, McpServerManifest, McpServerType

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.settings.mcp_servers.create(
            manifest=McpServerManifest(
                description="description",
                name="name",
                type=McpServerType.REMOTE,
                url="url",
            ),
        )
        """
        _response = self._raw_client.create(manifest=manifest, request_options=request_options)
        return _response.data

    def create_or_update(
        self, *, manifest: McpServerManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMcpServerResponse:
        """
        Create or replace by `name`. Header secrets: real value sets/rotates; redacted keeps existing (400 if none).

        Parameters
        ----------
        manifest : McpServerManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            The saved MCP server with auth_status

        Examples
        --------
        from fern import FernApi, McpServerManifest, McpServerType

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.settings.mcp_servers.create_or_update(
            manifest=McpServerManifest(
                description="description",
                name="name",
                type=McpServerType.REMOTE,
                url="url",
            ),
        )
        """
        _response = self._raw_client.create_or_update(manifest=manifest, request_options=request_options)
        return _response.data

    def get(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetMcpServerResponse:
        """
        A single MCP server by name, with nested live auth_status (settings / admin projection). Header auth values are redacted.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            The MCP server

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.settings.mcp_servers.get(
            name="name",
        )
        """
        _response = self._raw_client.get(name, request_options=request_options)
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
    ) -> AsyncPager[ConfiguredMcpServer, ListMcpServersResponse]:
        """
        Paginated MCP servers with auth_status. Header secrets are redacted.

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
        AsyncPager[ConfiguredMcpServer, ListMcpServersResponse]
            Paginated MCP servers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.settings.mcp_servers.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(limit=limit, page_token=page_token, request_options=request_options)

    async def create(
        self, *, manifest: McpServerManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMcpServerResponse:
        """
        Creates an MCP server by `name`. Fails if `name` is already taken. Runs DCR registration when `auth.type` is `dcr`. Header secrets: real value required; redacted with no stored value returns 400.

        Parameters
        ----------
        manifest : McpServerManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            The created MCP server with auth_status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, McpServerManifest, McpServerType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.settings.mcp_servers.create(
                manifest=McpServerManifest(
                    description="description",
                    name="name",
                    type=McpServerType.REMOTE,
                    url="url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(manifest=manifest, request_options=request_options)
        return _response.data

    async def create_or_update(
        self, *, manifest: McpServerManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMcpServerResponse:
        """
        Create or replace by `name`. Header secrets: real value sets/rotates; redacted keeps existing (400 if none).

        Parameters
        ----------
        manifest : McpServerManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            The saved MCP server with auth_status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, McpServerManifest, McpServerType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.settings.mcp_servers.create_or_update(
                manifest=McpServerManifest(
                    description="description",
                    name="name",
                    type=McpServerType.REMOTE,
                    url="url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update(manifest=manifest, request_options=request_options)
        return _response.data

    async def get(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetMcpServerResponse:
        """
        A single MCP server by name, with nested live auth_status (settings / admin projection). Header auth values are redacted.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            The MCP server

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.settings.mcp_servers.get(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(name, request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.mcp_server import McpServer
from ..types.mcp_server_id_param import McpServerIdParam
from ..types.mcp_server_name import McpServerName
from ..types.org_name import OrgName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawMcpServersClient, RawMcpServersClient
from .types.get_mcp_server_response import GetMcpServerResponse


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

    def get_mcp_server(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        mcp_server_name: typing.Optional[McpServerName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMcpServerResponse:
        """
        List out all mcp_servers. The mcp_servers are sorted by creation date, with the most recently-created mcp_servers coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        mcp_server_name : typing.Optional[McpServerName]
            Name of the mcp_server to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            Returns a list of mcp_server objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.get_mcp_server()
        """
        _response = self._raw_client.get_mcp_server(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            mcp_server_name=mcp_server_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_mcp_server(
        self,
        *,
        project_id: str,
        name: str,
        url: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpServer:
        """
        Create a new mcp_server. If there is an existing mcp_server with the same name as the one specified in the request, will return the existing mcp_server unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the MCP server belongs under

        name : str
            Name of the MCP server. Within a project, MCP server names are unique

        url : str
            URL of the MCP server endpoint

        description : typing.Optional[str]
            Textual description of the MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the new mcp_server object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.post_mcp_server(
            project_id="project_id",
            name="name",
            url="url",
        )
        """
        _response = self._raw_client.post_mcp_server(
            project_id=project_id, name=name, url=url, description=description, request_options=request_options
        )
        return _response.data

    def put_mcp_server(
        self,
        *,
        project_id: str,
        name: str,
        url: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpServer:
        """
        Create or replace mcp_server. If there is an existing mcp_server with the same name as the one specified in the request, will replace the existing mcp_server with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the MCP server belongs under

        name : str
            Name of the MCP server. Within a project, MCP server names are unique

        url : str
            URL of the MCP server endpoint

        description : typing.Optional[str]
            Textual description of the MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the new mcp_server object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.put_mcp_server(
            project_id="project_id",
            name="name",
            url="url",
        )
        """
        _response = self._raw_client.put_mcp_server(
            project_id=project_id, name=name, url=url, description=description, request_options=request_options
        )
        return _response.data

    def get_mcp_server_id(
        self, mcp_server_id: McpServerIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> McpServer:
        """
        Get a mcp_server object by its id

        Parameters
        ----------
        mcp_server_id : McpServerIdParam
            McpServer id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the mcp_server object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.get_mcp_server_id(
            mcp_server_id="mcp_server_id",
        )
        """
        _response = self._raw_client.get_mcp_server_id(mcp_server_id, request_options=request_options)
        return _response.data

    def delete_mcp_server_id(
        self, mcp_server_id: McpServerIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> McpServer:
        """
        Delete a mcp_server object by its id

        Parameters
        ----------
        mcp_server_id : McpServerIdParam
            McpServer id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the deleted mcp_server object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.delete_mcp_server_id(
            mcp_server_id="mcp_server_id",
        )
        """
        _response = self._raw_client.delete_mcp_server_id(mcp_server_id, request_options=request_options)
        return _response.data

    def patch_mcp_server_id(
        self,
        mcp_server_id: McpServerIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpServer:
        """
        Partially update a mcp_server object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        mcp_server_id : McpServerIdParam
            McpServer id

        name : typing.Optional[str]
            Name of the MCP server. Within a project, MCP server names are unique

        url : typing.Optional[str]
            URL of the MCP server endpoint

        description : typing.Optional[str]
            Textual description of the MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the mcp_server object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mcp_servers.patch_mcp_server_id(
            mcp_server_id="mcp_server_id",
        )
        """
        _response = self._raw_client.patch_mcp_server_id(
            mcp_server_id, name=name, url=url, description=description, request_options=request_options
        )
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

    async def get_mcp_server(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        mcp_server_name: typing.Optional[McpServerName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMcpServerResponse:
        """
        List out all mcp_servers. The mcp_servers are sorted by creation date, with the most recently-created mcp_servers coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        mcp_server_name : typing.Optional[McpServerName]
            Name of the mcp_server to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMcpServerResponse
            Returns a list of mcp_server objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.get_mcp_server()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mcp_server(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            mcp_server_name=mcp_server_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_mcp_server(
        self,
        *,
        project_id: str,
        name: str,
        url: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpServer:
        """
        Create a new mcp_server. If there is an existing mcp_server with the same name as the one specified in the request, will return the existing mcp_server unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the MCP server belongs under

        name : str
            Name of the MCP server. Within a project, MCP server names are unique

        url : str
            URL of the MCP server endpoint

        description : typing.Optional[str]
            Textual description of the MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the new mcp_server object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.post_mcp_server(
                project_id="project_id",
                name="name",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_mcp_server(
            project_id=project_id, name=name, url=url, description=description, request_options=request_options
        )
        return _response.data

    async def put_mcp_server(
        self,
        *,
        project_id: str,
        name: str,
        url: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpServer:
        """
        Create or replace mcp_server. If there is an existing mcp_server with the same name as the one specified in the request, will replace the existing mcp_server with the provided fields

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the MCP server belongs under

        name : str
            Name of the MCP server. Within a project, MCP server names are unique

        url : str
            URL of the MCP server endpoint

        description : typing.Optional[str]
            Textual description of the MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the new mcp_server object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.put_mcp_server(
                project_id="project_id",
                name="name",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_mcp_server(
            project_id=project_id, name=name, url=url, description=description, request_options=request_options
        )
        return _response.data

    async def get_mcp_server_id(
        self, mcp_server_id: McpServerIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> McpServer:
        """
        Get a mcp_server object by its id

        Parameters
        ----------
        mcp_server_id : McpServerIdParam
            McpServer id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the mcp_server object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.get_mcp_server_id(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mcp_server_id(mcp_server_id, request_options=request_options)
        return _response.data

    async def delete_mcp_server_id(
        self, mcp_server_id: McpServerIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> McpServer:
        """
        Delete a mcp_server object by its id

        Parameters
        ----------
        mcp_server_id : McpServerIdParam
            McpServer id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the deleted mcp_server object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.delete_mcp_server_id(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_mcp_server_id(mcp_server_id, request_options=request_options)
        return _response.data

    async def patch_mcp_server_id(
        self,
        mcp_server_id: McpServerIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> McpServer:
        """
        Partially update a mcp_server object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        mcp_server_id : McpServerIdParam
            McpServer id

        name : typing.Optional[str]
            Name of the MCP server. Within a project, MCP server names are unique

        url : typing.Optional[str]
            URL of the MCP server endpoint

        description : typing.Optional[str]
            Textual description of the MCP server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        McpServer
            Returns the mcp_server object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mcp_servers.patch_mcp_server_id(
                mcp_server_id="mcp_server_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_mcp_server_id(
            mcp_server_id, name=name, url=url, description=description, request_options=request_options
        )
        return _response.data

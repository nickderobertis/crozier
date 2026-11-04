

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWorkspaceClient, RawWorkspaceClient
from .types.workspace_api_ocs_create_response import WorkspaceApiOcsCreateResponse
from .types.workspace_api_ocs_edit_response import WorkspaceApiOcsEditResponse
from .types.workspace_api_ocs_find_all_response import WorkspaceApiOcsFindAllResponse
from .types.workspace_api_ocs_find_response import WorkspaceApiOcsFindResponse


OMIT = typing.cast(typing.Any, ...)


class WorkspaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkspaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkspaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkspaceClient
        """
        return self._raw_client

    def api_ocs_find_all(
        self,
        *,
        name: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceApiOcsFindAllResponse:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            Optional filter to return workspaces by name

        offset : typing.Optional[int]
            Optional page number for pagination

        limit : typing.Optional[int]
            Optional limit of workspaces per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsFindAllResponse
            Successfully retrieved workspaces

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace.api_ocs_find_all()
        """
        _response = self._raw_client.api_ocs_find_all(
            name=name, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def api_ocs_create(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsCreateResponse:
        """
        Parameters
        ----------
        name : str
            Workspace name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsCreateResponse
            Workspace created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace.api_ocs_create(
            name="name",
        )
        """
        _response = self._raw_client.api_ocs_create(name=name, request_options=request_options)
        return _response.data

    def api_ocs_find(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsFindResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of a workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsFindResponse
            Workspace returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace.api_ocs_find(
            id=1000000,
        )
        """
        _response = self._raw_client.api_ocs_find(id, request_options=request_options)
        return _response.data

    def api_ocs_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            of a workspace to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace.api_ocs_delete(
            id=1000000,
        )
        """
        _response = self._raw_client.api_ocs_delete(id, request_options=request_options)
        return _response.data

    def api_ocs_edit(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceApiOcsEditResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of a workspace

        name : typing.Optional[str]
            Optional - Workspace name.

        color : typing.Optional[str]
            Optional - Workspace color in hexadecimal format (example: #f91616).

        quota : typing.Optional[int]
            Optional - Workspace quota in bytes; e.g., 5368709120 for 5GB, or -3 for unlimited.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsEditResponse
            Workspace returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace.api_ocs_edit(
            id=1000000,
        )
        """
        _response = self._raw_client.api_ocs_edit(
            id, name=name, color=color, quota=quota, request_options=request_options
        )
        return _response.data


class AsyncWorkspaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkspaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkspaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkspaceClient
        """
        return self._raw_client

    async def api_ocs_find_all(
        self,
        *,
        name: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceApiOcsFindAllResponse:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            Optional filter to return workspaces by name

        offset : typing.Optional[int]
            Optional page number for pagination

        limit : typing.Optional[int]
            Optional limit of workspaces per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsFindAllResponse
            Successfully retrieved workspaces

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace.api_ocs_find_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.api_ocs_find_all(
            name=name, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def api_ocs_create(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsCreateResponse:
        """
        Parameters
        ----------
        name : str
            Workspace name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsCreateResponse
            Workspace created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace.api_ocs_create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_ocs_create(name=name, request_options=request_options)
        return _response.data

    async def api_ocs_find(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsFindResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of a workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsFindResponse
            Workspace returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace.api_ocs_find(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_ocs_find(id, request_options=request_options)
        return _response.data

    async def api_ocs_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            of a workspace to delete

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
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace.api_ocs_delete(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_ocs_delete(id, request_options=request_options)
        return _response.data

    async def api_ocs_edit(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkspaceApiOcsEditResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of a workspace

        name : typing.Optional[str]
            Optional - Workspace name.

        color : typing.Optional[str]
            Optional - Workspace color in hexadecimal format (example: #f91616).

        quota : typing.Optional[int]
            Optional - Workspace quota in bytes; e.g., 5368709120 for 5GB, or -3 for unlimited.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsEditResponse
            Workspace returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workspace.api_ocs_edit(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_ocs_edit(
            id, name=name, color=color, quota=quota, request_options=request_options
        )
        return _response.data

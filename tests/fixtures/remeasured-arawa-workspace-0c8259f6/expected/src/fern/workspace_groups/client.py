

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWorkspaceGroupsClient, RawWorkspaceGroupsClient
from .types.workspace_api_ocs_create_sub_group_response import WorkspaceApiOcsCreateSubGroupResponse
from .types.workspace_api_ocs_find_groups_by_space_id_response import WorkspaceApiOcsFindGroupsBySpaceIdResponse


OMIT = typing.cast(typing.Any, ...)


class WorkspaceGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkspaceGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkspaceGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkspaceGroupsClient
        """
        return self._raw_client

    def workspace_api_ocs_find_groups_by_space_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsFindGroupsBySpaceIdResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsFindGroupsBySpaceIdResponse
            Groups of the specified workspace returned successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_groups.workspace_api_ocs_find_groups_by_space_id(
            id=1000000,
        )
        """
        _response = self._raw_client.workspace_api_ocs_find_groups_by_space_id(id, request_options=request_options)
        return _response.data

    def workspace_api_ocs_create_sub_group(
        self, id: int, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsCreateSubGroupResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        name : str
            The subgroup name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsCreateSubGroupResponse
            Subgroup created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_groups.workspace_api_ocs_create_sub_group(
            id=1000000,
            name="name",
        )
        """
        _response = self._raw_client.workspace_api_ocs_create_sub_group(id, name=name, request_options=request_options)
        return _response.data

    def workspace_api_ocs_remove_group(
        self, id: int, gid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Id of the workspace

        gid : str
            id of the subgroup to delete

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
        client.workspace_groups.workspace_api_ocs_remove_group(
            id=1000000,
            gid="gid",
        )
        """
        _response = self._raw_client.workspace_api_ocs_remove_group(id, gid, request_options=request_options)
        return _response.data


class AsyncWorkspaceGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkspaceGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkspaceGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkspaceGroupsClient
        """
        return self._raw_client

    async def workspace_api_ocs_find_groups_by_space_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsFindGroupsBySpaceIdResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsFindGroupsBySpaceIdResponse
            Groups of the specified workspace returned successfully.

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
            await client.workspace_groups.workspace_api_ocs_find_groups_by_space_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_find_groups_by_space_id(
            id, request_options=request_options
        )
        return _response.data

    async def workspace_api_ocs_create_sub_group(
        self, id: int, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsCreateSubGroupResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        name : str
            The subgroup name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsCreateSubGroupResponse
            Subgroup created successfully

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
            await client.workspace_groups.workspace_api_ocs_create_sub_group(
                id=1000000,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_create_sub_group(
            id, name=name, request_options=request_options
        )
        return _response.data

    async def workspace_api_ocs_remove_group(
        self, id: int, gid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Id of the workspace

        gid : str
            id of the subgroup to delete

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
            await client.workspace_groups.workspace_api_ocs_remove_group(
                id=1000000,
                gid="gid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_remove_group(id, gid, request_options=request_options)
        return _response.data

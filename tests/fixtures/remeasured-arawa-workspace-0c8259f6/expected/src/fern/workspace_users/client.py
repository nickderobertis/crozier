

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWorkspaceUsersClient, RawWorkspaceUsersClient
from .types.workspace_api_ocs_add_user_as_workspace_manager_response import (
    WorkspaceApiOcsAddUserAsWorkspaceManagerResponse,
)
from .types.workspace_api_ocs_add_users_in_workspace_response import WorkspaceApiOcsAddUsersInWorkspaceResponse
from .types.workspace_api_ocs_add_users_to_group_response import WorkspaceApiOcsAddUsersToGroupResponse
from .types.workspace_api_ocs_find_users_by_id_response import WorkspaceApiOcsFindUsersByIdResponse


OMIT = typing.cast(typing.Any, ...)


class WorkspaceUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkspaceUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkspaceUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkspaceUsersClient
        """
        return self._raw_client

    def workspace_api_ocs_find_users_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsFindUsersByIdResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsFindUsersByIdResponse
            Users of the specified workspace returned successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_users.workspace_api_ocs_find_users_by_id(
            id=1000000,
        )
        """
        _response = self._raw_client.workspace_api_ocs_find_users_by_id(id, request_options=request_options)
        return _response.data

    def workspace_api_ocs_add_users_in_workspace(
        self, id: int, *, uids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsAddUsersInWorkspaceResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uids : typing.Sequence[str]
            Represents the user uids to add to the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsAddUsersInWorkspaceResponse
            Confirmation message indicating that users have been added successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_users.workspace_api_ocs_add_users_in_workspace(
            id=1000000,
            uids=["uids"],
        )
        """
        _response = self._raw_client.workspace_api_ocs_add_users_in_workspace(
            id, uids=uids, request_options=request_options
        )
        return _response.data

    def workspace_api_ocs_remove_users_in_workspace(
        self,
        id: int,
        *,
        uids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Represents the user uids to remove to the workspace

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
        client.workspace_users.workspace_api_ocs_remove_users_in_workspace(
            id=1000000,
            uids=["uids[]"],
        )
        """
        _response = self._raw_client.workspace_api_ocs_remove_users_in_workspace(
            id, uids=uids, request_options=request_options
        )
        return _response.data

    def workspace_api_ocs_add_user_as_workspace_manager(
        self, id: int, *, uid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsAddUserAsWorkspaceManagerResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uid : str
            Represents the user uid to add as a workspace manager

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsAddUserAsWorkspaceManagerResponse
            Confirmation for users added to the workspace.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_users.workspace_api_ocs_add_user_as_workspace_manager(
            id=1000000,
            uid="uid",
        )
        """
        _response = self._raw_client.workspace_api_ocs_add_user_as_workspace_manager(
            id, uid=uid, request_options=request_options
        )
        return _response.data

    def workspace_api_ocs_remove_user_as_workspace_manager(
        self, id: int, *, uid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uid : str
            Represents the user uid to remove as a workspace manager

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
        client.workspace_users.workspace_api_ocs_remove_user_as_workspace_manager(
            id=1000000,
            uid="uid",
        )
        """
        _response = self._raw_client.workspace_api_ocs_remove_user_as_workspace_manager(
            id, uid=uid, request_options=request_options
        )
        return _response.data

    def workspace_api_ocs_add_users_to_group(
        self, id: int, gid: str, *, uids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsAddUsersToGroupResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        gid : str
            The subgroup id

        uids : typing.Sequence[str]
            Represents the user uids to add to the subgroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsAddUsersToGroupResponse
            Users added in subgroup successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspace_users.workspace_api_ocs_add_users_to_group(
            id=1000000,
            gid="gid",
            uids=["uids"],
        )
        """
        _response = self._raw_client.workspace_api_ocs_add_users_to_group(
            id, gid, uids=uids, request_options=request_options
        )
        return _response.data

    def workspace_api_ocs_remove_users_from_group(
        self,
        id: int,
        gid: str,
        *,
        uids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        gid : str
            The subgroup id

        uids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Represents the user uids to remove from the subgroup

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
        client.workspace_users.workspace_api_ocs_remove_users_from_group(
            id=1000000,
            gid="gid",
            uids=["uids[]"],
        )
        """
        _response = self._raw_client.workspace_api_ocs_remove_users_from_group(
            id, gid, uids=uids, request_options=request_options
        )
        return _response.data


class AsyncWorkspaceUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkspaceUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkspaceUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkspaceUsersClient
        """
        return self._raw_client

    async def workspace_api_ocs_find_users_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsFindUsersByIdResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsFindUsersByIdResponse
            Users of the specified workspace returned successfully.

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
            await client.workspace_users.workspace_api_ocs_find_users_by_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_find_users_by_id(id, request_options=request_options)
        return _response.data

    async def workspace_api_ocs_add_users_in_workspace(
        self, id: int, *, uids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsAddUsersInWorkspaceResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uids : typing.Sequence[str]
            Represents the user uids to add to the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsAddUsersInWorkspaceResponse
            Confirmation message indicating that users have been added successfully.

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
            await client.workspace_users.workspace_api_ocs_add_users_in_workspace(
                id=1000000,
                uids=["uids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_add_users_in_workspace(
            id, uids=uids, request_options=request_options
        )
        return _response.data

    async def workspace_api_ocs_remove_users_in_workspace(
        self,
        id: int,
        *,
        uids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Represents the user uids to remove to the workspace

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
            await client.workspace_users.workspace_api_ocs_remove_users_in_workspace(
                id=1000000,
                uids=["uids[]"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_remove_users_in_workspace(
            id, uids=uids, request_options=request_options
        )
        return _response.data

    async def workspace_api_ocs_add_user_as_workspace_manager(
        self, id: int, *, uid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsAddUserAsWorkspaceManagerResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uid : str
            Represents the user uid to add as a workspace manager

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsAddUserAsWorkspaceManagerResponse
            Confirmation for users added to the workspace.

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
            await client.workspace_users.workspace_api_ocs_add_user_as_workspace_manager(
                id=1000000,
                uid="uid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_add_user_as_workspace_manager(
            id, uid=uid, request_options=request_options
        )
        return _response.data

    async def workspace_api_ocs_remove_user_as_workspace_manager(
        self, id: int, *, uid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uid : str
            Represents the user uid to remove as a workspace manager

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
            await client.workspace_users.workspace_api_ocs_remove_user_as_workspace_manager(
                id=1000000,
                uid="uid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_remove_user_as_workspace_manager(
            id, uid=uid, request_options=request_options
        )
        return _response.data

    async def workspace_api_ocs_add_users_to_group(
        self, id: int, gid: str, *, uids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceApiOcsAddUsersToGroupResponse:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        gid : str
            The subgroup id

        uids : typing.Sequence[str]
            Represents the user uids to add to the subgroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiOcsAddUsersToGroupResponse
            Users added in subgroup successfully

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
            await client.workspace_users.workspace_api_ocs_add_users_to_group(
                id=1000000,
                gid="gid",
                uids=["uids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_add_users_to_group(
            id, gid, uids=uids, request_options=request_options
        )
        return _response.data

    async def workspace_api_ocs_remove_users_from_group(
        self,
        id: int,
        gid: str,
        *,
        uids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        gid : str
            The subgroup id

        uids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Represents the user uids to remove from the subgroup

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
            await client.workspace_users.workspace_api_ocs_remove_users_from_group(
                id=1000000,
                gid="gid",
                uids=["uids[]"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workspace_api_ocs_remove_users_from_group(
            id, gid, uids=uids, request_options=request_options
        )
        return _response.data

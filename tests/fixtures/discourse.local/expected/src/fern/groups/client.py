

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGroupsClient, RawGroupsClient
from .types.add_group_members_response import AddGroupMembersResponse
from .types.create_group_request_group import CreateGroupRequestGroup
from .types.create_group_response import CreateGroupResponse
from .types.delete_group_response import DeleteGroupResponse
from .types.get_group_response import GetGroupResponse
from .types.list_group_members_response import ListGroupMembersResponse
from .types.list_groups_response import ListGroupsResponse
from .types.remove_group_members_response import RemoveGroupMembersResponse
from .types.update_group_request_group import UpdateGroupRequestGroup
from .types.update_group_response import UpdateGroupResponse


OMIT = typing.cast(typing.Any, ...)


class GroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGroupsClient
        """
        return self._raw_client

    def create_group(
        self, *, group: CreateGroupRequestGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateGroupResponse:
        """
        Parameters
        ----------
        group : CreateGroupRequestGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGroupResponse
            group created

        Examples
        --------
        from fern.groups import CreateGroupRequestGroup

        from fern import FernApi

        client = FernApi()
        client.groups.create_group(
            group=CreateGroupRequestGroup(
                name="name",
            ),
        )
        """
        _response = self._raw_client.create_group(group=group, request_options=request_options)
        return _response.data

    def delete_group(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteGroupResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteGroupResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.delete_group(
            id=1,
        )
        """
        _response = self._raw_client.delete_group(id, request_options=request_options)
        return _response.data

    def list_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListGroupsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGroupsResponse
            response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.list_groups()
        """
        _response = self._raw_client.list_groups(request_options=request_options)
        return _response.data

    def get_group(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetGroupResponse:
        """
        Parameters
        ----------
        id : str
            Use group name instead of id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGroupResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.get_group(
            id="name",
        )
        """
        _response = self._raw_client.get_group(id, request_options=request_options)
        return _response.data

    def update_group(
        self, id: int, *, group: UpdateGroupRequestGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateGroupResponse:
        """
        Parameters
        ----------
        id : int

        group : UpdateGroupRequestGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateGroupResponse
            success response

        Examples
        --------
        from fern.groups import UpdateGroupRequestGroup

        from fern import FernApi

        client = FernApi()
        client.groups.update_group(
            id=1,
            group=UpdateGroupRequestGroup(
                name="name",
            ),
        )
        """
        _response = self._raw_client.update_group(id, group=group, request_options=request_options)
        return _response.data

    def list_group_members(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListGroupMembersResponse:
        """
        Parameters
        ----------
        id : str
            Use group name instead of id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGroupMembersResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.list_group_members(
            id="name",
        )
        """
        _response = self._raw_client.list_group_members(id, request_options=request_options)
        return _response.data

    def add_group_members(
        self,
        id: int,
        *,
        usernames: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddGroupMembersResponse:
        """
        Parameters
        ----------
        id : int

        usernames : typing.Optional[str]
            comma separated list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddGroupMembersResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.add_group_members(
            id=1,
        )
        """
        _response = self._raw_client.add_group_members(id, usernames=usernames, request_options=request_options)
        return _response.data

    def remove_group_members(
        self,
        id: int,
        *,
        usernames: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemoveGroupMembersResponse:
        """
        Parameters
        ----------
        id : int

        usernames : typing.Optional[str]
            comma separated list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveGroupMembersResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.remove_group_members(
            id=1,
        )
        """
        _response = self._raw_client.remove_group_members(id, usernames=usernames, request_options=request_options)
        return _response.data


class AsyncGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGroupsClient
        """
        return self._raw_client

    async def create_group(
        self, *, group: CreateGroupRequestGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateGroupResponse:
        """
        Parameters
        ----------
        group : CreateGroupRequestGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGroupResponse
            group created

        Examples
        --------
        import asyncio

        from fern.groups import CreateGroupRequestGroup

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.create_group(
                group=CreateGroupRequestGroup(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_group(group=group, request_options=request_options)
        return _response.data

    async def delete_group(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteGroupResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteGroupResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.delete_group(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group(id, request_options=request_options)
        return _response.data

    async def list_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListGroupsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGroupsResponse
            response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.list_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_groups(request_options=request_options)
        return _response.data

    async def get_group(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetGroupResponse:
        """
        Parameters
        ----------
        id : str
            Use group name instead of id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGroupResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.get_group(
                id="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group(id, request_options=request_options)
        return _response.data

    async def update_group(
        self, id: int, *, group: UpdateGroupRequestGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateGroupResponse:
        """
        Parameters
        ----------
        id : int

        group : UpdateGroupRequestGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateGroupResponse
            success response

        Examples
        --------
        import asyncio

        from fern.groups import UpdateGroupRequestGroup

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.update_group(
                id=1,
                group=UpdateGroupRequestGroup(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_group(id, group=group, request_options=request_options)
        return _response.data

    async def list_group_members(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListGroupMembersResponse:
        """
        Parameters
        ----------
        id : str
            Use group name instead of id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGroupMembersResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.list_group_members(
                id="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_group_members(id, request_options=request_options)
        return _response.data

    async def add_group_members(
        self,
        id: int,
        *,
        usernames: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddGroupMembersResponse:
        """
        Parameters
        ----------
        id : int

        usernames : typing.Optional[str]
            comma separated list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddGroupMembersResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.add_group_members(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_group_members(id, usernames=usernames, request_options=request_options)
        return _response.data

    async def remove_group_members(
        self,
        id: int,
        *,
        usernames: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemoveGroupMembersResponse:
        """
        Parameters
        ----------
        id : int

        usernames : typing.Optional[str]
            comma separated list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveGroupMembersResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.remove_group_members(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_group_members(
            id, usernames=usernames, request_options=request_options
        )
        return _response.data

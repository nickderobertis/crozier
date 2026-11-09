

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.group import Group
from ..types.info import Info
from ..types.user_group_member import UserGroupMember
from .raw_client import AsyncRawGroupsClient, RawGroupsClient


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

    def get_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Group]:
        """
        Returns accessible groups for a user, all groups for an admin

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            List of groups

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.get_groups()
        """
        _response = self._raw_client.get_groups(request_options=request_options)
        return _response.data

    def delete_group_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Deletes a single group by id.

        Parameters
        ----------
        id : int
            Id of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User group will be deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.delete_group_by_id(
            id=1,
        )
        """
        _response = self._raw_client.delete_group_by_id(id, request_options=request_options)
        return _response.data

    def add_member(
        self,
        id: int,
        user_id: int,
        *,
        perm: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        add a new user to group

        Parameters
        ----------
        id : int
            Id of the group

        user_id : int
            user id of the member

        perm : typing.Optional[int]
            Default permission of the new member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User has been added to group

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.add_member(
            id=1,
            user_id=1,
        )
        """
        _response = self._raw_client.add_member(id, user_id, perm=perm, request_options=request_options)
        return _response.data

    def delete_group_member_by_group_id_and_user_id(
        self, id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Deletes a single group member by groupId and userId

        Parameters
        ----------
        id : int
            Id of the group

        user_id : int
            user id of the member

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User will be removed from group.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.delete_group_member_by_group_id_and_user_id(
            id=1,
            user_id=1,
        )
        """
        _response = self._raw_client.delete_group_member_by_group_id_and_user_id(
            id, user_id, request_options=request_options
        )
        return _response.data

    def deletable_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Group]:
        """
        Return a list of the groups which it is possible to delete.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            List of groups

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.deletable_groups()
        """
        _response = self._raw_client.deletable_groups(request_options=request_options)
        return _response.data

    def get_group_users_with_roles(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserGroupMember]:
        """
        Returns accessible objects of users with roles from the group

        Parameters
        ----------
        id : int
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserGroupMember]
            List of group-user-member

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.get_group_users_with_roles(
            id=1,
        )
        """
        _response = self._raw_client.get_group_users_with_roles(id, request_options=request_options)
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

    async def get_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Group]:
        """
        Returns accessible groups for a user, all groups for an admin

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            List of groups

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.get_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_groups(request_options=request_options)
        return _response.data

    async def delete_group_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Deletes a single group by id.

        Parameters
        ----------
        id : int
            Id of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User group will be deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.delete_group_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group_by_id(id, request_options=request_options)
        return _response.data

    async def add_member(
        self,
        id: int,
        user_id: int,
        *,
        perm: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        add a new user to group

        Parameters
        ----------
        id : int
            Id of the group

        user_id : int
            user id of the member

        perm : typing.Optional[int]
            Default permission of the new member.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User has been added to group

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.add_member(
                id=1,
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_member(id, user_id, perm=perm, request_options=request_options)
        return _response.data

    async def delete_group_member_by_group_id_and_user_id(
        self, id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Deletes a single group member by groupId and userId

        Parameters
        ----------
        id : int
            Id of the group

        user_id : int
            user id of the member

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            User will be removed from group.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.delete_group_member_by_group_id_and_user_id(
                id=1,
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group_member_by_group_id_and_user_id(
            id, user_id, request_options=request_options
        )
        return _response.data

    async def deletable_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Group]:
        """
        Return a list of the groups which it is possible to delete.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            List of groups

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.deletable_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.deletable_groups(request_options=request_options)
        return _response.data

    async def get_group_users_with_roles(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserGroupMember]:
        """
        Returns accessible objects of users with roles from the group

        Parameters
        ----------
        id : int
            ID of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserGroupMember]
            List of group-user-member

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.get_group_users_with_roles(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group_users_with_roles(id, request_options=request_options)
        return _response.data

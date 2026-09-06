

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.ending_before import EndingBefore
from ..types.group import Group
from ..types.group_id_param import GroupIdParam
from ..types.group_name import GroupName
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawGroupsClient, RawGroupsClient
from .types.get_group_response import GetGroupResponse


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

    def get_group(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        group_name: typing.Optional[GroupName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetGroupResponse:
        """
        List out all groups. The groups are sorted by creation date, with the most recently-created groups coming first

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

        group_name : typing.Optional[GroupName]
            Name of the group to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGroupResponse
            Returns a list of group objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.get_group()
        """
        _response = self._raw_client.get_group(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            group_name=group_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_group(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        member_users: typing.Optional[typing.Sequence[str]] = OMIT,
        member_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Create a new group. If there is an existing group with the same name as the one specified in the request, will return the existing group unmodified

        Parameters
        ----------
        name : str
            Name of the group

        description : typing.Optional[str]
            Textual description of the group

        member_users : typing.Optional[typing.Sequence[str]]
            Ids of users which belong to this group

        member_groups : typing.Optional[typing.Sequence[str]]
            Ids of the groups this group inherits from

            An inheriting group has all the users contained in its member groups, as well as all of their inherited users

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the group belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the new group object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.post_group(
            name="name",
        )
        """
        _response = self._raw_client.post_group(
            name=name,
            description=description,
            member_users=member_users,
            member_groups=member_groups,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def put_group(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        member_users: typing.Optional[typing.Sequence[str]] = OMIT,
        member_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Create or replace group. If there is an existing group with the same name as the one specified in the request, will replace the existing group with the provided fields

        Parameters
        ----------
        name : str
            Name of the group

        description : typing.Optional[str]
            Textual description of the group

        member_users : typing.Optional[typing.Sequence[str]]
            Ids of users which belong to this group

        member_groups : typing.Optional[typing.Sequence[str]]
            Ids of the groups this group inherits from

            An inheriting group has all the users contained in its member groups, as well as all of their inherited users

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the group belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the new group object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.put_group(
            name="name",
        )
        """
        _response = self._raw_client.put_group(
            name=name,
            description=description,
            member_users=member_users,
            member_groups=member_groups,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def get_group_id(self, group_id: GroupIdParam, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
        """
        Get a group object by its id

        Parameters
        ----------
        group_id : GroupIdParam
            Group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the group object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.get_group_id(
            group_id="group_id",
        )
        """
        _response = self._raw_client.get_group_id(group_id, request_options=request_options)
        return _response.data

    def delete_group_id(
        self, group_id: GroupIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Delete a group object by its id

        Parameters
        ----------
        group_id : GroupIdParam
            Group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the deleted group object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.delete_group_id(
            group_id="group_id",
        )
        """
        _response = self._raw_client.delete_group_id(group_id, request_options=request_options)
        return _response.data

    def patch_group_id(
        self,
        group_id: GroupIdParam,
        *,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        add_member_users: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_member_users: typing.Optional[typing.Sequence[str]] = OMIT,
        add_member_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_member_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Partially update a group object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        group_id : GroupIdParam
            Group id

        description : typing.Optional[str]
            Textual description of the group

        name : typing.Optional[str]
            Name of the group

        add_member_users : typing.Optional[typing.Sequence[str]]
            A list of user IDs to add to the group

        remove_member_users : typing.Optional[typing.Sequence[str]]
            A list of user IDs to remove from the group

        add_member_groups : typing.Optional[typing.Sequence[str]]
            A list of group IDs to add to the group's inheriting-from set

        remove_member_groups : typing.Optional[typing.Sequence[str]]
            A list of group IDs to remove from the group's inheriting-from set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the group object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.patch_group_id(
            group_id="group_id",
        )
        """
        _response = self._raw_client.patch_group_id(
            group_id,
            description=description,
            name=name,
            add_member_users=add_member_users,
            remove_member_users=remove_member_users,
            add_member_groups=add_member_groups,
            remove_member_groups=remove_member_groups,
            request_options=request_options,
        )
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

    async def get_group(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        group_name: typing.Optional[GroupName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetGroupResponse:
        """
        List out all groups. The groups are sorted by creation date, with the most recently-created groups coming first

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

        group_name : typing.Optional[GroupName]
            Name of the group to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGroupResponse
            Returns a list of group objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.get_group()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            group_name=group_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_group(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        member_users: typing.Optional[typing.Sequence[str]] = OMIT,
        member_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Create a new group. If there is an existing group with the same name as the one specified in the request, will return the existing group unmodified

        Parameters
        ----------
        name : str
            Name of the group

        description : typing.Optional[str]
            Textual description of the group

        member_users : typing.Optional[typing.Sequence[str]]
            Ids of users which belong to this group

        member_groups : typing.Optional[typing.Sequence[str]]
            Ids of the groups this group inherits from

            An inheriting group has all the users contained in its member groups, as well as all of their inherited users

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the group belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the new group object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.post_group(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_group(
            name=name,
            description=description,
            member_users=member_users,
            member_groups=member_groups,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def put_group(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        member_users: typing.Optional[typing.Sequence[str]] = OMIT,
        member_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        org_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Create or replace group. If there is an existing group with the same name as the one specified in the request, will replace the existing group with the provided fields

        Parameters
        ----------
        name : str
            Name of the group

        description : typing.Optional[str]
            Textual description of the group

        member_users : typing.Optional[typing.Sequence[str]]
            Ids of users which belong to this group

        member_groups : typing.Optional[typing.Sequence[str]]
            Ids of the groups this group inherits from

            An inheriting group has all the users contained in its member groups, as well as all of their inherited users

        org_name : typing.Optional[str]
            For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the group belongs in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the new group object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.put_group(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_group(
            name=name,
            description=description,
            member_users=member_users,
            member_groups=member_groups,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def get_group_id(
        self, group_id: GroupIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Get a group object by its id

        Parameters
        ----------
        group_id : GroupIdParam
            Group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the group object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.get_group_id(
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group_id(group_id, request_options=request_options)
        return _response.data

    async def delete_group_id(
        self, group_id: GroupIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Delete a group object by its id

        Parameters
        ----------
        group_id : GroupIdParam
            Group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the deleted group object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.delete_group_id(
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group_id(group_id, request_options=request_options)
        return _response.data

    async def patch_group_id(
        self,
        group_id: GroupIdParam,
        *,
        description: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        add_member_users: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_member_users: typing.Optional[typing.Sequence[str]] = OMIT,
        add_member_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_member_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Partially update a group object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        group_id : GroupIdParam
            Group id

        description : typing.Optional[str]
            Textual description of the group

        name : typing.Optional[str]
            Name of the group

        add_member_users : typing.Optional[typing.Sequence[str]]
            A list of user IDs to add to the group

        remove_member_users : typing.Optional[typing.Sequence[str]]
            A list of user IDs to remove from the group

        add_member_groups : typing.Optional[typing.Sequence[str]]
            A list of group IDs to add to the group's inheriting-from set

        remove_member_groups : typing.Optional[typing.Sequence[str]]
            A list of group IDs to remove from the group's inheriting-from set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Returns the group object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.patch_group_id(
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_group_id(
            group_id,
            description=description,
            name=name,
            add_member_users=add_member_users,
            remove_member_users=remove_member_users,
            add_member_groups=add_member_groups,
            remove_member_groups=remove_member_groups,
            request_options=request_options,
        )
        return _response.data

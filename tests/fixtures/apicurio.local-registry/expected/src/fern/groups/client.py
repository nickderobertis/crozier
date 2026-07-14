

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.group_id import GroupId
from ..types.group_meta_data import GroupMetaData
from ..types.group_search_results import GroupSearchResults
from ..types.properties import Properties
from ..types.sort_by import SortBy
from ..types.sort_order import SortOrder
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

    def list_groups(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupSearchResults:
        """
        Returns a list of all groups.  This list is paged.

        Parameters
        ----------
        limit : typing.Optional[int]
            The number of groups to return.  Defaults to 20.

        offset : typing.Optional[int]
            The number of groups to skip before starting the result set.  Defaults to 0.

        order : typing.Optional[SortOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SortBy]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupSearchResults
            On a successful response, returns a bounded set of groups.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.list_groups()
        """
        _response = self._raw_client.list_groups(
            limit=limit, offset=offset, order=order, orderby=orderby, request_options=request_options
        )
        return _response.data

    def create_group(
        self,
        *,
        id: str,
        description: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupMetaData:
        """
        Creates a new group.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)
        * The group already exist (HTTP error `409`)

        Parameters
        ----------
        id : str


        description : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupMetaData
            The group has been successfully created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.create_group(
            description="The description of the artifact.",
            id="group-identifier",
            properties={"custom-1": "foo", "custom-2": "bar"},
        )
        """
        _response = self._raw_client.create_group(
            id=id, description=description, properties=properties, request_options=request_options
        )
        return _response.data

    def get_group_by_id(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupMetaData:
        """
        Returns a group using the specified id.

        This operation can fail for the following reasons:

        * No group exists with the specified ID (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupMetaData
            The group's metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.get_group_by_id(
            group_id='"my-group"',
        )
        """
        _response = self._raw_client.get_group_by_id(group_id, request_options=request_options)
        return _response.data

    def delete_group_by_id(self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a group by identifier.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)
        * The group does not exist (HTTP error `404`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.groups.delete_group_by_id(
            group_id='"my-group"',
        )
        """
        _response = self._raw_client.delete_group_by_id(group_id, request_options=request_options)
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

    async def list_groups(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupSearchResults:
        """
        Returns a list of all groups.  This list is paged.

        Parameters
        ----------
        limit : typing.Optional[int]
            The number of groups to return.  Defaults to 20.

        offset : typing.Optional[int]
            The number of groups to skip before starting the result set.  Defaults to 0.

        order : typing.Optional[SortOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SortBy]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupSearchResults
            On a successful response, returns a bounded set of groups.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.list_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_groups(
            limit=limit, offset=offset, order=order, orderby=orderby, request_options=request_options
        )
        return _response.data

    async def create_group(
        self,
        *,
        id: str,
        description: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupMetaData:
        """
        Creates a new group.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)
        * The group already exist (HTTP error `409`)

        Parameters
        ----------
        id : str


        description : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupMetaData
            The group has been successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.create_group(
                description="The description of the artifact.",
                id="group-identifier",
                properties={"custom-1": "foo", "custom-2": "bar"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_group(
            id=id, description=description, properties=properties, request_options=request_options
        )
        return _response.data

    async def get_group_by_id(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GroupMetaData:
        """
        Returns a group using the specified id.

        This operation can fail for the following reasons:

        * No group exists with the specified ID (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupMetaData
            The group's metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.get_group_by_id(
                group_id='"my-group"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group_by_id(group_id, request_options=request_options)
        return _response.data

    async def delete_group_by_id(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a group by identifier.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)
        * The group does not exist (HTTP error `404`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.groups.delete_group_by_id(
                group_id='"my-group"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group_by_id(group_id, request_options=request_options)
        return _response.data

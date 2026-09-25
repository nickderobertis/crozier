

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1label import V1Label
from .raw_client import AsyncRawTagsClient, RawTagsClient
from .types.list_tags_request_filter import ListTagsRequestFilter
from .types.v1labels_create_label import V1LabelsCreateLabel
from .types.v1labels_update_label import V1LabelsUpdateLabel


OMIT = typing.cast(typing.Any, ...)


class TagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTagsClient
        """
        return self._raw_client

    def list_tags(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[ListTagsRequestFilter] = None,
        parent_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Label:
        """
        Retrieve all labels (tags) for the specified account. Labels help classify work, group related tasks, and require certain information for events. Supports filtering by status and pagination.

        Parameters
        ----------
        account_id : int
            Account ID

        limit : typing.Optional[int]
            Maximum number of labels to return (default: 10000)

        offset : typing.Optional[int]
            Number of labels to skip (default: 0)

        filter : typing.Optional[ListTagsRequestFilter]
            Filter labels by status: all (default), active, or archived

        parent_id : typing.Optional[int]
            Filter by parent label ID to get child labels only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Label
            Child labels retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.list_tags(
            account_id=1,
        )
        """
        _response = self._raw_client.list_tags(
            account_id, limit=limit, offset=offset, filter=filter, parent_id=parent_id, request_options=request_options
        )
        return _response.data

    def create_tag(
        self, account_id: int, *, label: V1LabelsCreateLabel, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Label:
        """
        Create a new label (tag) for the account. Labels can be hierarchical by specifying a parent_id.

        Parameters
        ----------
        account_id : int
            Account ID

        label : V1LabelsCreateLabel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Label
            Label with external_id created successfully

        Examples
        --------
        from fern.tags import V1LabelsCreateLabel

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.create_tag(
            account_id=1,
            label=V1LabelsCreateLabel(
                name="Project Management",
                emoji="https://emoji.memorycdn.com/tw64/1f4cb.png",
                active=True,
            ),
        )
        """
        _response = self._raw_client.create_tag(account_id, label=label, request_options=request_options)
        return _response.data

    def get_tag(self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> V1Label:
        """
        Retrieve a specific label by ID. The response includes child labels if any exist.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Label ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Label
            Label retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.get_tag(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.get_tag(account_id, id, request_options=request_options)
        return _response.data

    def update_tag(
        self,
        account_id: int,
        id: int,
        *,
        label: V1LabelsUpdateLabel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Label:
        """
        Update an existing label. All fields are optional for partial updates. Set active to false to archive a label.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Label ID

        label : V1LabelsUpdateLabel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Label
            Label updated successfully

        Examples
        --------
        from fern.tags import V1LabelsUpdateLabel

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.update_tag(
            account_id=1,
            id=1,
            label=V1LabelsUpdateLabel(
                name="Updated Name",
                emoji="https://emoji.memorycdn.com/tw64/1f504.png",
            ),
        )
        """
        _response = self._raw_client.update_tag(account_id, id, label=label, request_options=request_options)
        return _response.data

    def delete_tag(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a label from the account. This will permanently remove the label.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Label ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Label deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.delete_tag(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.delete_tag(account_id, id, request_options=request_options)
        return _response.data


class AsyncTagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTagsClient
        """
        return self._raw_client

    async def list_tags(
        self,
        account_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[ListTagsRequestFilter] = None,
        parent_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Label:
        """
        Retrieve all labels (tags) for the specified account. Labels help classify work, group related tasks, and require certain information for events. Supports filtering by status and pagination.

        Parameters
        ----------
        account_id : int
            Account ID

        limit : typing.Optional[int]
            Maximum number of labels to return (default: 10000)

        offset : typing.Optional[int]
            Number of labels to skip (default: 0)

        filter : typing.Optional[ListTagsRequestFilter]
            Filter labels by status: all (default), active, or archived

        parent_id : typing.Optional[int]
            Filter by parent label ID to get child labels only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Label
            Child labels retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.list_tags(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tags(
            account_id, limit=limit, offset=offset, filter=filter, parent_id=parent_id, request_options=request_options
        )
        return _response.data

    async def create_tag(
        self, account_id: int, *, label: V1LabelsCreateLabel, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Label:
        """
        Create a new label (tag) for the account. Labels can be hierarchical by specifying a parent_id.

        Parameters
        ----------
        account_id : int
            Account ID

        label : V1LabelsCreateLabel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Label
            Label with external_id created successfully

        Examples
        --------
        import asyncio

        from fern.tags import V1LabelsCreateLabel

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.create_tag(
                account_id=1,
                label=V1LabelsCreateLabel(
                    name="Project Management",
                    emoji="https://emoji.memorycdn.com/tw64/1f4cb.png",
                    active=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tag(account_id, label=label, request_options=request_options)
        return _response.data

    async def get_tag(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Label:
        """
        Retrieve a specific label by ID. The response includes child labels if any exist.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Label ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Label
            Label retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.get_tag(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tag(account_id, id, request_options=request_options)
        return _response.data

    async def update_tag(
        self,
        account_id: int,
        id: int,
        *,
        label: V1LabelsUpdateLabel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Label:
        """
        Update an existing label. All fields are optional for partial updates. Set active to false to archive a label.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Label ID

        label : V1LabelsUpdateLabel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Label
            Label updated successfully

        Examples
        --------
        import asyncio

        from fern.tags import V1LabelsUpdateLabel

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.update_tag(
                account_id=1,
                id=1,
                label=V1LabelsUpdateLabel(
                    name="Updated Name",
                    emoji="https://emoji.memorycdn.com/tw64/1f504.png",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tag(account_id, id, label=label, request_options=request_options)
        return _response.data

    async def delete_tag(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a label from the account. This will permanently remove the label.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Label ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Label deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.delete_tag(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tag(account_id, id, request_options=request_options)
        return _response.data

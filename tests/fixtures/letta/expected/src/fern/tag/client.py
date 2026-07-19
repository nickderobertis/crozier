

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTagClient, RawTagClient
from .types.list_tags_request_order import ListTagsRequestOrder
from .types.list_tags_request_order_by import ListTagsRequestOrderBy


class TagClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTagClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTagClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTagClient
        """
        return self._raw_client

    def list_tags(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListTagsRequestOrder] = None,
        order_by: typing.Optional[ListTagsRequestOrderBy] = None,
        query_text: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Get the list of all tags (from agents and blocks) that have been created.

        Parameters
        ----------
        before : typing.Optional[str]
            Tag cursor for pagination. Returns tags that come before this tag in the specified sort order

        after : typing.Optional[str]
            Tag cursor for pagination. Returns tags that come after this tag in the specified sort order

        limit : typing.Optional[int]
            Maximum number of tags to return

        order : typing.Optional[ListTagsRequestOrder]
            Sort order for tags. 'asc' for alphabetical order, 'desc' for reverse alphabetical order

        order_by : typing.Optional[ListTagsRequestOrderBy]
            Field to sort by

        query_text : typing.Optional[str]
            Filter tags by text search. Deprecated, please use name field instead

        name : typing.Optional[str]
            Filter tags by name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tag.list_tags()
        """
        _response = self._raw_client.list_tags(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            query_text=query_text,
            name=name,
            request_options=request_options,
        )
        return _response.data


class AsyncTagClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTagClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTagClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTagClient
        """
        return self._raw_client

    async def list_tags(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListTagsRequestOrder] = None,
        order_by: typing.Optional[ListTagsRequestOrderBy] = None,
        query_text: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Get the list of all tags (from agents and blocks) that have been created.

        Parameters
        ----------
        before : typing.Optional[str]
            Tag cursor for pagination. Returns tags that come before this tag in the specified sort order

        after : typing.Optional[str]
            Tag cursor for pagination. Returns tags that come after this tag in the specified sort order

        limit : typing.Optional[int]
            Maximum number of tags to return

        order : typing.Optional[ListTagsRequestOrder]
            Sort order for tags. 'asc' for alphabetical order, 'desc' for reverse alphabetical order

        order_by : typing.Optional[ListTagsRequestOrderBy]
            Field to sort by

        query_text : typing.Optional[str]
            Filter tags by text search. Deprecated, please use name field instead

        name : typing.Optional[str]
            Filter tags by name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tag.list_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tags(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            query_text=query_text,
            name=name,
            request_options=request_options,
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tags_collection import TagsCollection
from .raw_client import AsyncRawTagsClient, RawTagsClient


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
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TagsCollection:
        """
        Returns an array of Tag objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagsCollection
            Tags collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tags.list_tags()
        """
        _response = self._raw_client.list_tags(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
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
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TagsCollection:
        """
        Returns an array of Tag objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagsCollection
            Tags collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.tags.list_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tags(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

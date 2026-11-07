

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ticket_get_collections_response import TicketGetCollectionsResponse
from .raw_client import AsyncRawTicketCollectionClient, RawTicketCollectionClient


class TicketCollectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTicketCollectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTicketCollectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTicketCollectionClient
        """
        return self._raw_client

    def ticket_collection_get_collections(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketGetCollectionsResponse:
        """
        Get all the collections

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetCollectionsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_collection.ticket_collection_get_collections()
        """
        _response = self._raw_client.ticket_collection_get_collections(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data


class AsyncTicketCollectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTicketCollectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTicketCollectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTicketCollectionClient
        """
        return self._raw_client

    async def ticket_collection_get_collections(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketGetCollectionsResponse:
        """
        Get all the collections

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetCollectionsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_collection.ticket_collection_get_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_collection_get_collections(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

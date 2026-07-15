

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_listing_response import GetListingResponse
from ..types.get_listings_response import GetListingsResponse
from .raw_client import AsyncRawListingClient, RawListingClient


class ListingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawListingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawListingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawListingClient
        """
        return self._raw_client

    def listings_all(
        self,
        ecosystem_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        external_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetListingsResponse:
        """
        List listings

        Parameters
        ----------
        ecosystem_id : str

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        external_id : typing.Optional[str]
            Filter on external_id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetListingsResponse
            Listings

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.listing.listings_all(
            ecosystem_id="ecosystem_id",
        )
        """
        _response = self._raw_client.listings_all(
            ecosystem_id, cursor=cursor, limit=limit, external_id=external_id, request_options=request_options
        )
        return _response.data

    def listings_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetListingResponse:
        """
        Get listing

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetListingResponse
            Listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.listing.listings_one(
            ecosystem_id="ecosystem_id",
            id="id",
        )
        """
        _response = self._raw_client.listings_one(ecosystem_id, id, request_options=request_options)
        return _response.data


class AsyncListingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawListingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawListingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawListingClient
        """
        return self._raw_client

    async def listings_all(
        self,
        ecosystem_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        external_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetListingsResponse:
        """
        List listings

        Parameters
        ----------
        ecosystem_id : str

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        external_id : typing.Optional[str]
            Filter on external_id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetListingsResponse
            Listings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.listing.listings_all(
                ecosystem_id="ecosystem_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listings_all(
            ecosystem_id, cursor=cursor, limit=limit, external_id=external_id, request_options=request_options
        )
        return _response.data

    async def listings_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetListingResponse:
        """
        Get listing

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetListingResponse
            Listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.listing.listings_one(
                ecosystem_id="ecosystem_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listings_one(ecosystem_id, id, request_options=request_options)
        return _response.data

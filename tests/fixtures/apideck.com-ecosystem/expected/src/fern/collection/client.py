

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_collection_response import GetCollectionResponse
from ..types.get_collections_response import GetCollectionsResponse
from ..types.get_listings_response import GetListingsResponse
from .raw_client import AsyncRawCollectionClient, RawCollectionClient


class CollectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionClient
        """
        return self._raw_client

    def collections_all(
        self,
        ecosystem_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionsResponse:
        """
        List collections

        Parameters
        ----------
        ecosystem_id : str

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionsResponse
            Collections

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collection.collections_all(
            ecosystem_id="ecosystem_id",
        )
        """
        _response = self._raw_client.collections_all(
            ecosystem_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def collections_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCollectionResponse:
        """
        Get collection

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionResponse
            Collection

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collection.collections_one(
            ecosystem_id="ecosystem_id",
            id="id",
        )
        """
        _response = self._raw_client.collections_one(ecosystem_id, id, request_options=request_options)
        return _response.data

    def listings_all(
        self,
        ecosystem_id: str,
        id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetListingsResponse:
        """
        List collection listings

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

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
        client.collection.listings_all(
            ecosystem_id="ecosystem_id",
            id="id",
        )
        """
        _response = self._raw_client.listings_all(
            ecosystem_id, id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data


class AsyncCollectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionClient
        """
        return self._raw_client

    async def collections_all(
        self,
        ecosystem_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCollectionsResponse:
        """
        List collections

        Parameters
        ----------
        ecosystem_id : str

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionsResponse
            Collections

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collection.collections_all(
                ecosystem_id="ecosystem_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collections_all(
            ecosystem_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def collections_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCollectionResponse:
        """
        Get collection

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCollectionResponse
            Collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collection.collections_one(
                ecosystem_id="ecosystem_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collections_one(ecosystem_id, id, request_options=request_options)
        return _response.data

    async def listings_all(
        self,
        ecosystem_id: str,
        id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetListingsResponse:
        """
        List collection listings

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

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
            await client.collection.listings_all(
                ecosystem_id="ecosystem_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listings_all(
            ecosystem_id, id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

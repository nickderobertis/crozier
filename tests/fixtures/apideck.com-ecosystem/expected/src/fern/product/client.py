

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_listings_response import GetListingsResponse
from ..types.get_product_response import GetProductResponse
from ..types.get_products_response import GetProductsResponse
from .raw_client import AsyncRawProductClient, RawProductClient


class ProductClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProductClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProductClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProductClient
        """
        return self._raw_client

    def products_all(
        self, ecosystem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductsResponse:
        """
        List products

        Parameters
        ----------
        ecosystem_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductsResponse
            Products

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.product.products_all(
            ecosystem_id="ecosystem_id",
        )
        """
        _response = self._raw_client.products_all(ecosystem_id, request_options=request_options)
        return _response.data

    def products_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductResponse:
        """
        Get product

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductResponse
            Product

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.product.products_one(
            ecosystem_id="ecosystem_id",
            id="id",
        )
        """
        _response = self._raw_client.products_one(ecosystem_id, id, request_options=request_options)
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
        List product listings

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
        client.product.listings_all(
            ecosystem_id="ecosystem_id",
            id="id",
        )
        """
        _response = self._raw_client.listings_all(
            ecosystem_id, id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data


class AsyncProductClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProductClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProductClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProductClient
        """
        return self._raw_client

    async def products_all(
        self, ecosystem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductsResponse:
        """
        List products

        Parameters
        ----------
        ecosystem_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductsResponse
            Products

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.product.products_all(
                ecosystem_id="ecosystem_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.products_all(ecosystem_id, request_options=request_options)
        return _response.data

    async def products_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductResponse:
        """
        Get product

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductResponse
            Product

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.product.products_one(
                ecosystem_id="ecosystem_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.products_one(ecosystem_id, id, request_options=request_options)
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
        List product listings

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
            await client.product.listings_all(
                ecosystem_id="ecosystem_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listings_all(
            ecosystem_id, id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

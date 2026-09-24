

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProductsClient, RawProductsClient
from .types.get_product_response import GetProductResponse
from .types.list_products_request_status import ListProductsRequestStatus
from .types.list_products_response import ListProductsResponse


OMIT = typing.cast(typing.Any, ...)


class ProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProductsClient
        """
        return self._raw_client

    def list_products(
        self,
        *,
        status: typing.Optional[ListProductsRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListProductsResponse:
        """
        Get a list of all products in the account. Optionally filter by status (live or test).

        Parameters
        ----------
        status : typing.Optional[ListProductsRequestStatus]
            Filter by product status. Omit for all products.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProductsResponse
            List of products

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_products()
        """
        _response = self._raw_client.list_products(status=status, request_options=request_options)
        return _response.data

    def get_product(
        self, product_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductResponse:
        """
        Retrieve a single product by its ID.

        Parameters
        ----------
        product_id : int
            The product ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductResponse
            Product details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product(
            product_id=1,
        )
        """
        _response = self._raw_client.get_product(product_id, request_options=request_options)
        return _response.data


class AsyncProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProductsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProductsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProductsClient
        """
        return self._raw_client

    async def list_products(
        self,
        *,
        status: typing.Optional[ListProductsRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListProductsResponse:
        """
        Get a list of all products in the account. Optionally filter by status (live or test).

        Parameters
        ----------
        status : typing.Optional[ListProductsRequestStatus]
            Filter by product status. Omit for all products.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProductsResponse
            List of products

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_products()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_products(status=status, request_options=request_options)
        return _response.data

    async def get_product(
        self, product_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductResponse:
        """
        Retrieve a single product by its ID.

        Parameters
        ----------
        product_id : int
            The product ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductResponse
            Product details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product(
                product_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product(product_id, request_options=request_options)
        return _response.data

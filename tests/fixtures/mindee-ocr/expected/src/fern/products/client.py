

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProductsClient, RawProductsClient


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

    def list_customer_products(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieve products available to the authenticated customer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            List of products.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_customer_products()
        """
        _response = self._raw_client.list_customer_products(request_options=request_options)
        return _response.data

    def get_product_open_api(
        self, account: str, product: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get product OpenAPI spec

        Parameters
        ----------
        account : str

        product : str

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OpenAPI spec.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_open_api(
            account="account",
            product="product",
            version="version",
        )
        """
        _response = self._raw_client.get_product_open_api(account, product, version, request_options=request_options)
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

    async def list_customer_products(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieve products available to the authenticated customer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            List of products.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_customer_products()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_customer_products(request_options=request_options)
        return _response.data

    async def get_product_open_api(
        self, account: str, product: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get product OpenAPI spec

        Parameters
        ----------
        account : str

        product : str

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OpenAPI spec.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_open_api(
                account="account",
                product="product",
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_open_api(
            account, product, version, request_options=request_options
        )
        return _response.data

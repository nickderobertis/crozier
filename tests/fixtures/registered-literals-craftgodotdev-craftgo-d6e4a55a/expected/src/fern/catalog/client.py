

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cents import Cents
from ..types.create_product_resp_body import CreateProductRespBody
from ..types.currency_code import CurrencyCode
from ..types.delete_product_resp_body import DeleteProductRespBody
from ..types.get_product_resp_body import GetProductRespBody
from ..types.list_categories_resp_body import ListCategoriesRespBody
from ..types.list_products_resp_body import ListProductsRespBody
from ..types.non_empty_id import NonEmptyId
from ..types.sku import Sku
from .raw_client import AsyncRawCatalogClient, RawCatalogClient


OMIT = typing.cast(typing.Any, ...)


class CatalogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogClient
        """
        return self._raw_client

    def list_categories(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCategoriesRespBody:
        """
        List categories.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCategoriesRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.catalog.list_categories(
            limit=1,
        )
        """
        _response = self._raw_client.list_categories(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    def list_products(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListProductsRespBody:
        """
        List products with cursor pagination.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        category : typing.Optional[str]

        tag : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProductsRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.catalog.list_products(
            limit=1,
        )
        """
        _response = self._raw_client.list_products(
            limit=limit, cursor=cursor, category=category, tag=tag, request_options=request_options
        )
        return _response.data

    def create_product(
        self,
        *,
        category_id: NonEmptyId,
        name: str,
        price_cents: Cents,
        sku: Sku,
        currency: typing.Optional[CurrencyCode] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProductRespBody:
        """
        Create a product (admin only).

        Parameters
        ----------
        category_id : NonEmptyId

        name : str

        price_cents : Cents

        sku : Sku

        currency : typing.Optional[CurrencyCode]

        description : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProductRespBody
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.catalog.create_product(
            category_id="categoryId",
            name="name",
            price_cents=1,
            sku="sku",
        )
        """
        _response = self._raw_client.create_product(
            category_id=category_id,
            name=name,
            price_cents=price_cents,
            sku=sku,
            currency=currency,
            description=description,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def get_product(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetProductRespBody:
        """
        Fetch one product by id.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.catalog.get_product(
            id="id",
        )
        """
        _response = self._raw_client.get_product(id, request_options=request_options)
        return _response.data

    def delete_product(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteProductRespBody:
        """
        Delete a product (admin only).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteProductRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.catalog.delete_product(
            id="id",
        )
        """
        _response = self._raw_client.delete_product(id, request_options=request_options)
        return _response.data


class AsyncCatalogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogClient
        """
        return self._raw_client

    async def list_categories(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCategoriesRespBody:
        """
        List categories.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCategoriesRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.list_categories(
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_categories(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    async def list_products(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListProductsRespBody:
        """
        List products with cursor pagination.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        category : typing.Optional[str]

        tag : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProductsRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.list_products(
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_products(
            limit=limit, cursor=cursor, category=category, tag=tag, request_options=request_options
        )
        return _response.data

    async def create_product(
        self,
        *,
        category_id: NonEmptyId,
        name: str,
        price_cents: Cents,
        sku: Sku,
        currency: typing.Optional[CurrencyCode] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProductRespBody:
        """
        Create a product (admin only).

        Parameters
        ----------
        category_id : NonEmptyId

        name : str

        price_cents : Cents

        sku : Sku

        currency : typing.Optional[CurrencyCode]

        description : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProductRespBody
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.create_product(
                category_id="categoryId",
                name="name",
                price_cents=1,
                sku="sku",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_product(
            category_id=category_id,
            name=name,
            price_cents=price_cents,
            sku=sku,
            currency=currency,
            description=description,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def get_product(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductRespBody:
        """
        Fetch one product by id.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.get_product(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product(id, request_options=request_options)
        return _response.data

    async def delete_product(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteProductRespBody:
        """
        Delete a product (admin only).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteProductRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog.delete_product(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_product(id, request_options=request_options)
        return _response.data

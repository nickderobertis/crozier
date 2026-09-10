

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.patch_request import PatchRequest
from ..types.product import Product
from ..types.product_category import ProductCategory
from ..types.product_collection import ProductCollection
from .raw_client import AsyncRawProductsClient, RawProductsClient
from .types.product_request_post_type import ProductRequestPostType


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

    def list(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        total_required: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProductCollection:
        """
        Lists products.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The number of items to return in the response.

        page : typing.Optional[int]
            A non-zero integer which is the start index of the entire list of items that are returned in the response. So, the combination of `page=1` and `page_size=20` returns the first 20 items. The combination of `page=2` and `page_size=20` returns the next 20 items.

        total_required : typing.Optional[bool]
            Indicates whether to show the total items and total pages in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProductCollection
            A successful request returns the HTTP `200 OK` status code and a JSON response body that lists products with details.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list()
        """
        _response = self._raw_client.list(
            page_size=page_size, page=page, total_required=total_required, request_options=request_options
        )
        return _response.data

    def create(
        self,
        *,
        name: str,
        type: ProductRequestPostType,
        pay_pal_request_id: typing.Optional[str] = None,
        id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        category: typing.Optional[ProductCategory] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        home_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Product:
        """
        Creates a product.

        Parameters
        ----------
        name : str
            The product name.

        type : ProductRequestPostType
            The product type. Indicates whether the product is physical or digital goods, or a service.

        pay_pal_request_id : typing.Optional[str]
            The server stores keys for 72 hours.

        id : typing.Optional[str]
            The ID of the product. You can specify the SKU for the product. If you omit the ID, the system generates it. System-generated IDs have the `PROD-` prefix.

        description : typing.Optional[str]
            The product description.

        category : typing.Optional[ProductCategory]

        image_url : typing.Optional[str]
            The image URL for the product.

        home_url : typing.Optional[str]
            The home page URL for the product.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Product
            A successful request returns the HTTP `200 OK` status code and a JSON response body that shows product details.

        Examples
        --------
        from fern.products import ProductRequestPostType

        from fern import FernApi, ProductCategory

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.create(
            name="Video Streaming Service",
            description="Video streaming service",
            type=ProductRequestPostType.SERVICE,
            category=ProductCategory.SOFTWARE,
            image_url="https://example.com/streaming.jpg",
            home_url="https://example.com/home",
        )
        """
        _response = self._raw_client.create(
            name=name,
            type=type,
            pay_pal_request_id=pay_pal_request_id,
            id=id,
            description=description,
            category=category,
            image_url=image_url,
            home_url=home_url,
            request_options=request_options,
        )
        return _response.data

    def get(self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Product:
        """
        Shows details for a product, by ID.

        Parameters
        ----------
        product_id : str
            The product ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Product
            A successful request returns the HTTP `200 OK` status code and a JSON response body that shows product details.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get(
            product_id="product_id",
        )
        """
        _response = self._raw_client.get(product_id, request_options=request_options)
        return _response.data

    def patch(
        self, product_id: str, *, request: PatchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates a product, by ID. You can patch these attributes and objects:<table><thead><tr><th>Attribute or object</th><th>Operations</th></tr></thead><tbody><tr><td><code>description</code></td><td>add, replace, remove</td></tr><tr><td><code>category</code></td><td>add, replace, remove</td></tr><tr><td><code>image_url</code></td><td>add, replace, remove</td></tr><tr><td><code>home_url</code></td><td>add, replace, remove</td></tr></tbody></table>

        Parameters
        ----------
        product_id : str
            The product ID.

        request : PatchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, Patch, PatchOp

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.patch(
            product_id="product_id",
            request=[
                Patch(
                    op=PatchOp.REPLACE,
                    path="/description",
                    value="Premium video streaming service",
                )
            ],
        )
        """
        _response = self._raw_client.patch(product_id, request=request, request_options=request_options)
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

    async def list(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        total_required: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProductCollection:
        """
        Lists products.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The number of items to return in the response.

        page : typing.Optional[int]
            A non-zero integer which is the start index of the entire list of items that are returned in the response. So, the combination of `page=1` and `page_size=20` returns the first 20 items. The combination of `page=2` and `page_size=20` returns the next 20 items.

        total_required : typing.Optional[bool]
            Indicates whether to show the total items and total pages in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProductCollection
            A successful request returns the HTTP `200 OK` status code and a JSON response body that lists products with details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            page_size=page_size, page=page, total_required=total_required, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        *,
        name: str,
        type: ProductRequestPostType,
        pay_pal_request_id: typing.Optional[str] = None,
        id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        category: typing.Optional[ProductCategory] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        home_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Product:
        """
        Creates a product.

        Parameters
        ----------
        name : str
            The product name.

        type : ProductRequestPostType
            The product type. Indicates whether the product is physical or digital goods, or a service.

        pay_pal_request_id : typing.Optional[str]
            The server stores keys for 72 hours.

        id : typing.Optional[str]
            The ID of the product. You can specify the SKU for the product. If you omit the ID, the system generates it. System-generated IDs have the `PROD-` prefix.

        description : typing.Optional[str]
            The product description.

        category : typing.Optional[ProductCategory]

        image_url : typing.Optional[str]
            The image URL for the product.

        home_url : typing.Optional[str]
            The home page URL for the product.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Product
            A successful request returns the HTTP `200 OK` status code and a JSON response body that shows product details.

        Examples
        --------
        import asyncio

        from fern.products import ProductRequestPostType

        from fern import AsyncFernApi, ProductCategory

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.create(
                name="Video Streaming Service",
                description="Video streaming service",
                type=ProductRequestPostType.SERVICE,
                category=ProductCategory.SOFTWARE,
                image_url="https://example.com/streaming.jpg",
                home_url="https://example.com/home",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            name=name,
            type=type,
            pay_pal_request_id=pay_pal_request_id,
            id=id,
            description=description,
            category=category,
            image_url=image_url,
            home_url=home_url,
            request_options=request_options,
        )
        return _response.data

    async def get(self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Product:
        """
        Shows details for a product, by ID.

        Parameters
        ----------
        product_id : str
            The product ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Product
            A successful request returns the HTTP `200 OK` status code and a JSON response body that shows product details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get(
                product_id="product_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(product_id, request_options=request_options)
        return _response.data

    async def patch(
        self, product_id: str, *, request: PatchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates a product, by ID. You can patch these attributes and objects:<table><thead><tr><th>Attribute or object</th><th>Operations</th></tr></thead><tbody><tr><td><code>description</code></td><td>add, replace, remove</td></tr><tr><td><code>category</code></td><td>add, replace, remove</td></tr><tr><td><code>image_url</code></td><td>add, replace, remove</td></tr><tr><td><code>home_url</code></td><td>add, replace, remove</td></tr></tbody></table>

        Parameters
        ----------
        product_id : str
            The product ID.

        request : PatchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Patch, PatchOp

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.patch(
                product_id="product_id",
                request=[
                    Patch(
                        op=PatchOp.REPLACE,
                        path="/description",
                        value="Premium video streaming service",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch(product_id, request=request, request_options=request_options)
        return _response.data

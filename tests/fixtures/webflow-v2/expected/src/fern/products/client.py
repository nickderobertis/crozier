

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProductsClient, RawProductsClient
from .types.create_products_request_product import CreateProductsRequestProduct
from .types.create_products_request_publish_status import CreateProductsRequestPublishStatus
from .types.create_products_request_sku import CreateProductsRequestSku
from .types.create_products_response import CreateProductsResponse
from .types.create_sku_products_request_publish_status import CreateSkuProductsRequestPublishStatus
from .types.create_sku_products_request_skus_item import CreateSkuProductsRequestSkusItem
from .types.create_sku_products_response import CreateSkuProductsResponse
from .types.get_products_response import GetProductsResponse
from .types.list_products_response import ListProductsResponse
from .types.update_products_request_product import UpdateProductsRequestProduct
from .types.update_products_request_publish_status import UpdateProductsRequestPublishStatus
from .types.update_products_request_sku import UpdateProductsRequestSku
from .types.update_products_response import UpdateProductsResponse
from .types.update_sku_products_request_publish_status import UpdateSkuProductsRequestPublishStatus
from .types.update_sku_products_request_sku import UpdateSkuProductsRequestSku
from .types.update_sku_products_response import UpdateSkuProductsResponse


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
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListProductsResponse:
        """
        Retrieve all products for a site.

        Use `limit` and `offset` to page through all products with subsequent requests. All SKUs for each product
        will also be fetched and returned. The `limit`, `offset` and `total` values represent Products only and do not include any SKUs.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProductsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list(site_id, offset=offset, limit=limit, request_options=request_options)
        return _response.data

    def create(
        self,
        site_id: str,
        *,
        product: CreateProductsRequestProduct,
        sku: CreateProductsRequestSku,
        publish_status: typing.Optional[CreateProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProductsResponse:
        """
        Create a new ecommerce product and defaultSKU. A product, at minimum, must have a single SKU.

        To create a product with multiple SKUs:
          - First, create a list of `sku-properties`, also known as [product options](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants). For example, a T-shirt product may have a "color" `sku-property`, with a list of enum values: red, yellow, and blue, another `sku-property` may be "size", with a list of enum values: small, medium, and large.
          - Once, a product is created with a list of `sku-properties`, Webflow will create a **default SKU**, which is always a combination of the first `enum` values of each `sku-property`. (e.g. Small - Red - T-Shirt)
          - After creation, you can create additional SKUs for the product, using the [Create SKUs endpoint.](/data/reference/ecommerce/products/create-sku)

        Upon creation, the default product type will be `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product : CreateProductsRequestProduct

        sku : CreateProductsRequestSku

        publish_status : typing.Optional[CreateProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProductsResponse
            Request was successful

        Examples
        --------
        from fern.products import (
            CreateProductsRequestProduct,
            CreateProductsRequestProductFieldData,
            CreateProductsRequestProductFieldDataSkuPropertiesItem,
            CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem,
            CreateProductsRequestPublishStatus,
            CreateProductsRequestSku,
            CreateProductsRequestSkuFieldData,
            CreateProductsRequestSkuFieldDataPrice,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.create(
            site_id="580e63e98c9a982ac9b8b741",
            publish_status=CreateProductsRequestPublishStatus.STAGING,
            product=CreateProductsRequestProduct(
                field_data=CreateProductsRequestProductFieldData(
                    name="Colorful T-shirt",
                    slug="colorful-t-shirt",
                    description="Our best-selling t-shirt available in multiple colors and sizes",
                    sku_properties=[
                        CreateProductsRequestProductFieldDataSkuPropertiesItem(
                            id="color",
                            name="Color",
                            enum=[
                                CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                    id="red",
                                    name="Red",
                                    slug="red",
                                ),
                                CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                    id="yellow",
                                    name="Yellow",
                                    slug="yellow",
                                ),
                                CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                    id="blue",
                                    name="Blue",
                                    slug="blue",
                                ),
                            ],
                        ),
                        CreateProductsRequestProductFieldDataSkuPropertiesItem(
                            id="size",
                            name="Size",
                            enum=[
                                CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                    id="small",
                                    name="Small",
                                    slug="small",
                                ),
                                CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                    id="medium",
                                    name="Medium",
                                    slug="medium",
                                ),
                                CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                    id="large",
                                    name="Large",
                                    slug="large",
                                ),
                            ],
                        ),
                    ],
                ),
            ),
            sku=CreateProductsRequestSku(
                field_data=CreateProductsRequestSkuFieldData(
                    name="Colorful T-shirt - Red Small",
                    slug="colorful-t-shirt-red-small",
                    price=CreateProductsRequestSkuFieldDataPrice(
                        value=2499.0,
                        unit="USD",
                        currency="USD",
                    ),
                    main_image="https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987",
                ),
            ),
        )
        """
        _response = self._raw_client.create(
            site_id, product=product, sku=sku, publish_status=publish_status, request_options=request_options
        )
        return _response.data

    def get(
        self, site_id: str, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductsResponse:
        """
        Retrieve a single product by its ID. All of its SKUs will also be
        retrieved.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get(
            site_id="580e63e98c9a982ac9b8b741",
            product_id="580e63fc8c9a982ac9b8b745",
        )
        """
        _response = self._raw_client.get(site_id, product_id, request_options=request_options)
        return _response.data

    def update(
        self,
        site_id: str,
        product_id: str,
        *,
        publish_status: typing.Optional[UpdateProductsRequestPublishStatus] = OMIT,
        product: typing.Optional[UpdateProductsRequestProduct] = OMIT,
        sku: typing.Optional[UpdateProductsRequestSku] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateProductsResponse:
        """
        Update an existing Product.

        Updating an existing Product will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        publish_status : typing.Optional[UpdateProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        product : typing.Optional[UpdateProductsRequestProduct]
            The Product object

        sku : typing.Optional[UpdateProductsRequestSku]
            The SKU object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateProductsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.update(
            site_id="580e63e98c9a982ac9b8b741",
            product_id="580e63fc8c9a982ac9b8b745",
        )
        """
        _response = self._raw_client.update(
            site_id,
            product_id,
            publish_status=publish_status,
            product=product,
            sku=sku,
            request_options=request_options,
        )
        return _response.data

    def create_sku(
        self,
        site_id: str,
        product_id: str,
        *,
        skus: typing.Sequence[CreateSkuProductsRequestSkusItem],
        publish_status: typing.Optional[CreateSkuProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSkuProductsResponse:
        """
        Create additional SKUs to manage every [option and variant of your Product.](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants)

        Creating SKUs through the API will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        skus : typing.Sequence[CreateSkuProductsRequestSkusItem]
            An array of the SKU data your are adding

        publish_status : typing.Optional[CreateSkuProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSkuProductsResponse
            Request was successful

        Examples
        --------
        from fern.products import (
            CreateSkuProductsRequestSkusItem,
            CreateSkuProductsRequestSkusItemFieldData,
            CreateSkuProductsRequestSkusItemFieldDataPrice,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.create_sku(
            site_id="580e63e98c9a982ac9b8b741",
            product_id="580e63fc8c9a982ac9b8b745",
            skus=[
                CreateSkuProductsRequestSkusItem(
                    field_data=CreateSkuProductsRequestSkusItemFieldData(
                        name="Colorful T-shirt - Default",
                        slug="colorful-t-shirt-default",
                        price=CreateSkuProductsRequestSkusItemFieldDataPrice(
                            value=2499.0,
                            unit="USD",
                            currency="USD",
                        ),
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.create_sku(
            site_id, product_id, skus=skus, publish_status=publish_status, request_options=request_options
        )
        return _response.data

    def update_sku(
        self,
        site_id: str,
        product_id: str,
        sku_id: str,
        *,
        sku: UpdateSkuProductsRequestSku,
        publish_status: typing.Optional[UpdateSkuProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSkuProductsResponse:
        """
        Update a specified SKU.

        Updating an existing SKU will set the Product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        sku_id : str
            Unique identifier for a SKU

        sku : UpdateSkuProductsRequestSku
            The SKU object

        publish_status : typing.Optional[UpdateSkuProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSkuProductsResponse
            Request was successful

        Examples
        --------
        from fern.products import (
            UpdateSkuProductsRequestSku,
            UpdateSkuProductsRequestSkuFieldData,
            UpdateSkuProductsRequestSkuFieldDataPrice,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.update_sku(
            site_id="580e63e98c9a982ac9b8b741",
            product_id="580e63fc8c9a982ac9b8b745",
            sku_id="5e8518516e147040726cc415",
            sku=UpdateSkuProductsRequestSku(
                field_data=UpdateSkuProductsRequestSkuFieldData(
                    name="Colorful T-shirt - Default",
                    slug="colorful-t-shirt-default",
                    price=UpdateSkuProductsRequestSkuFieldDataPrice(
                        value=2499.0,
                        unit="USD",
                        currency="USD",
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.update_sku(
            site_id, product_id, sku_id, sku=sku, publish_status=publish_status, request_options=request_options
        )
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
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListProductsResponse:
        """
        Retrieve all products for a site.

        Use `limit` and `offset` to page through all products with subsequent requests. All SKUs for each product
        will also be fetched and returned. The `limit`, `offset` and `total` values represent Products only and do not include any SKUs.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProductsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(site_id, offset=offset, limit=limit, request_options=request_options)
        return _response.data

    async def create(
        self,
        site_id: str,
        *,
        product: CreateProductsRequestProduct,
        sku: CreateProductsRequestSku,
        publish_status: typing.Optional[CreateProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProductsResponse:
        """
        Create a new ecommerce product and defaultSKU. A product, at minimum, must have a single SKU.

        To create a product with multiple SKUs:
          - First, create a list of `sku-properties`, also known as [product options](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants). For example, a T-shirt product may have a "color" `sku-property`, with a list of enum values: red, yellow, and blue, another `sku-property` may be "size", with a list of enum values: small, medium, and large.
          - Once, a product is created with a list of `sku-properties`, Webflow will create a **default SKU**, which is always a combination of the first `enum` values of each `sku-property`. (e.g. Small - Red - T-Shirt)
          - After creation, you can create additional SKUs for the product, using the [Create SKUs endpoint.](/data/reference/ecommerce/products/create-sku)

        Upon creation, the default product type will be `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product : CreateProductsRequestProduct

        sku : CreateProductsRequestSku

        publish_status : typing.Optional[CreateProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProductsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.products import (
            CreateProductsRequestProduct,
            CreateProductsRequestProductFieldData,
            CreateProductsRequestProductFieldDataSkuPropertiesItem,
            CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem,
            CreateProductsRequestPublishStatus,
            CreateProductsRequestSku,
            CreateProductsRequestSkuFieldData,
            CreateProductsRequestSkuFieldDataPrice,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.create(
                site_id="580e63e98c9a982ac9b8b741",
                publish_status=CreateProductsRequestPublishStatus.STAGING,
                product=CreateProductsRequestProduct(
                    field_data=CreateProductsRequestProductFieldData(
                        name="Colorful T-shirt",
                        slug="colorful-t-shirt",
                        description="Our best-selling t-shirt available in multiple colors and sizes",
                        sku_properties=[
                            CreateProductsRequestProductFieldDataSkuPropertiesItem(
                                id="color",
                                name="Color",
                                enum=[
                                    CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                        id="red",
                                        name="Red",
                                        slug="red",
                                    ),
                                    CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                        id="yellow",
                                        name="Yellow",
                                        slug="yellow",
                                    ),
                                    CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                        id="blue",
                                        name="Blue",
                                        slug="blue",
                                    ),
                                ],
                            ),
                            CreateProductsRequestProductFieldDataSkuPropertiesItem(
                                id="size",
                                name="Size",
                                enum=[
                                    CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                        id="small",
                                        name="Small",
                                        slug="small",
                                    ),
                                    CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                        id="medium",
                                        name="Medium",
                                        slug="medium",
                                    ),
                                    CreateProductsRequestProductFieldDataSkuPropertiesItemEnumItem(
                                        id="large",
                                        name="Large",
                                        slug="large",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
                sku=CreateProductsRequestSku(
                    field_data=CreateProductsRequestSkuFieldData(
                        name="Colorful T-shirt - Red Small",
                        slug="colorful-t-shirt-red-small",
                        price=CreateProductsRequestSkuFieldDataPrice(
                            value=2499.0,
                            unit="USD",
                            currency="USD",
                        ),
                        main_image="https://rocketamp-sample-store.myshopify.com/cdn/shop/products/Gildan_2000_Antique_Cherry_Red_Front_1024x1024.jpg?v=1527232987",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            site_id, product=product, sku=sku, publish_status=publish_status, request_options=request_options
        )
        return _response.data

    async def get(
        self, site_id: str, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProductsResponse:
        """
        Retrieve a single product by its ID. All of its SKUs will also be
        retrieved.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProductsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get(
                site_id="580e63e98c9a982ac9b8b741",
                product_id="580e63fc8c9a982ac9b8b745",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(site_id, product_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        site_id: str,
        product_id: str,
        *,
        publish_status: typing.Optional[UpdateProductsRequestPublishStatus] = OMIT,
        product: typing.Optional[UpdateProductsRequestProduct] = OMIT,
        sku: typing.Optional[UpdateProductsRequestSku] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateProductsResponse:
        """
        Update an existing Product.

        Updating an existing Product will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        publish_status : typing.Optional[UpdateProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        product : typing.Optional[UpdateProductsRequestProduct]
            The Product object

        sku : typing.Optional[UpdateProductsRequestSku]
            The SKU object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateProductsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.update(
                site_id="580e63e98c9a982ac9b8b741",
                product_id="580e63fc8c9a982ac9b8b745",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            site_id,
            product_id,
            publish_status=publish_status,
            product=product,
            sku=sku,
            request_options=request_options,
        )
        return _response.data

    async def create_sku(
        self,
        site_id: str,
        product_id: str,
        *,
        skus: typing.Sequence[CreateSkuProductsRequestSkusItem],
        publish_status: typing.Optional[CreateSkuProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSkuProductsResponse:
        """
        Create additional SKUs to manage every [option and variant of your Product.](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants)

        Creating SKUs through the API will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        skus : typing.Sequence[CreateSkuProductsRequestSkusItem]
            An array of the SKU data your are adding

        publish_status : typing.Optional[CreateSkuProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSkuProductsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.products import (
            CreateSkuProductsRequestSkusItem,
            CreateSkuProductsRequestSkusItemFieldData,
            CreateSkuProductsRequestSkusItemFieldDataPrice,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.create_sku(
                site_id="580e63e98c9a982ac9b8b741",
                product_id="580e63fc8c9a982ac9b8b745",
                skus=[
                    CreateSkuProductsRequestSkusItem(
                        field_data=CreateSkuProductsRequestSkusItemFieldData(
                            name="Colorful T-shirt - Default",
                            slug="colorful-t-shirt-default",
                            price=CreateSkuProductsRequestSkusItemFieldDataPrice(
                                value=2499.0,
                                unit="USD",
                                currency="USD",
                            ),
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sku(
            site_id, product_id, skus=skus, publish_status=publish_status, request_options=request_options
        )
        return _response.data

    async def update_sku(
        self,
        site_id: str,
        product_id: str,
        sku_id: str,
        *,
        sku: UpdateSkuProductsRequestSku,
        publish_status: typing.Optional[UpdateSkuProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSkuProductsResponse:
        """
        Update a specified SKU.

        Updating an existing SKU will set the Product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        sku_id : str
            Unique identifier for a SKU

        sku : UpdateSkuProductsRequestSku
            The SKU object

        publish_status : typing.Optional[UpdateSkuProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSkuProductsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.products import (
            UpdateSkuProductsRequestSku,
            UpdateSkuProductsRequestSkuFieldData,
            UpdateSkuProductsRequestSkuFieldDataPrice,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.update_sku(
                site_id="580e63e98c9a982ac9b8b741",
                product_id="580e63fc8c9a982ac9b8b745",
                sku_id="5e8518516e147040726cc415",
                sku=UpdateSkuProductsRequestSku(
                    field_data=UpdateSkuProductsRequestSkuFieldData(
                        name="Colorful T-shirt - Default",
                        slug="colorful-t-shirt-default",
                        price=UpdateSkuProductsRequestSkuFieldDataPrice(
                            value=2499.0,
                            unit="USD",
                            currency="USD",
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_sku(
            site_id, product_id, sku_id, sku=sku, publish_status=publish_status, request_options=request_options
        )
        return _response.data

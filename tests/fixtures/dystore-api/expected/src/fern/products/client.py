

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

    def get_product(
        self,
        *,
        include: typing.Optional[str] = None,
        filter_url_slug: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get product

        Parameters
        ----------
        include : typing.Optional[str]
            Include product relations

        filter_url_slug : typing.Optional[str]
            Get sigle product by its slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product(
            include="variants.prices,cheapest_variant.prices",
            filter_url_slug="slug",
        )
        """
        _response = self._raw_client.get_product(
            include=include, filter_url_slug=filter_url_slug, request_options=request_options
        )
        return _response.data

    def list_products(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List products

        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_products(
            include="variants.prices,cheapest_variant.prices",
        )
        """
        _response = self._raw_client.list_products(include=include, request_options=request_options)
        return _response.data

    def list_product_associations(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product associations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_associations()
        """
        _response = self._raw_client.list_product_associations(request_options=request_options)
        return _response.data

    def list_product_associations_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List product associations relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_associations_relationships()
        """
        _response = self._raw_client.list_product_associations_relationships(request_options=request_options)
        return _response.data

    def list_product_inverse_associations(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product inverse associations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_inverse_associations()
        """
        _response = self._raw_client.list_product_inverse_associations(request_options=request_options)
        return _response.data

    def list_product_inverse_associations_index_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List product inverse associations index relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_inverse_associations_index_relationships()
        """
        _response = self._raw_client.list_product_inverse_associations_index_relationships(
            request_options=request_options
        )
        return _response.data

    def get_product_brand(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product brand

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_brand()
        """
        _response = self._raw_client.get_product_brand(request_options=request_options)
        return _response.data

    def get_product_brand_relationship(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product brand relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_brand_relationship()
        """
        _response = self._raw_client.get_product_brand_relationship(request_options=request_options)
        return _response.data

    def list_product_collection(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product collection

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_collection()
        """
        _response = self._raw_client.list_product_collection(request_options=request_options)
        return _response.data

    def list_product_collection_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product collection relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_collection_relationships()
        """
        _response = self._raw_client.list_product_collection_relationships(request_options=request_options)
        return _response.data

    def list_product_images(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product images

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_images()
        """
        _response = self._raw_client.list_product_images(request_options=request_options)
        return _response.data

    def list_product_images_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product images relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_images_relationships()
        """
        _response = self._raw_client.list_product_images_relationships(request_options=request_options)
        return _response.data

    def get_product_thumbnail(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product thumbnail

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_thumbnail()
        """
        _response = self._raw_client.get_product_thumbnail(request_options=request_options)
        return _response.data

    def get_product_thumbnail_relationship(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product thumbnail relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_thumbnail_relationship()
        """
        _response = self._raw_client.get_product_thumbnail_relationship(request_options=request_options)
        return _response.data

    def get_product_lowest_price(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product lowest price

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_lowest_price()
        """
        _response = self._raw_client.get_product_lowest_price(request_options=request_options)
        return _response.data

    def get_product_lowest_price_relationship(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product lowest price relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_lowest_price_relationship()
        """
        _response = self._raw_client.get_product_lowest_price_relationship(request_options=request_options)
        return _response.data

    def list_product_prices(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product prices

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_prices()
        """
        _response = self._raw_client.list_product_prices(request_options=request_options)
        return _response.data

    def list_product_prices_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product prices relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_prices_relationships()
        """
        _response = self._raw_client.list_product_prices_relationships(request_options=request_options)
        return _response.data

    def list_product_variants(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product variants

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_variants()
        """
        _response = self._raw_client.list_product_variants(request_options=request_options)
        return _response.data

    def list_product_variants_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product variants relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_variants_relationships()
        """
        _response = self._raw_client.list_product_variants_relationships(request_options=request_options)
        return _response.data

    def get_product_cheapest_variant(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product cheapest variant

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_cheapest_variant()
        """
        _response = self._raw_client.get_product_cheapest_variant(request_options=request_options)
        return _response.data

    def get_product_cheapest_variant_relationship(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get product cheapest variant relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_cheapest_variant_relationship()
        """
        _response = self._raw_client.get_product_cheapest_variant_relationship(request_options=request_options)
        return _response.data

    def list_product_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product tags

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_tags()
        """
        _response = self._raw_client.list_product_tags(request_options=request_options)
        return _response.data

    def list_product_tags_relationship(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product tags relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.list_product_tags_relationship()
        """
        _response = self._raw_client.list_product_tags_relationship(request_options=request_options)
        return _response.data

    def get_product_default_url(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product default url

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_default_url()
        """
        _response = self._raw_client.get_product_default_url(request_options=request_options)
        return _response.data

    def get_product_default_url_relationship(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product default url relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.products.get_product_default_url_relationship()
        """
        _response = self._raw_client.get_product_default_url_relationship(request_options=request_options)
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

    async def get_product(
        self,
        *,
        include: typing.Optional[str] = None,
        filter_url_slug: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get product

        Parameters
        ----------
        include : typing.Optional[str]
            Include product relations

        filter_url_slug : typing.Optional[str]
            Get sigle product by its slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product(
                include="variants.prices,cheapest_variant.prices",
                filter_url_slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product(
            include=include, filter_url_slug=filter_url_slug, request_options=request_options
        )
        return _response.data

    async def list_products(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List products

        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_products(
                include="variants.prices,cheapest_variant.prices",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_products(include=include, request_options=request_options)
        return _response.data

    async def list_product_associations(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product associations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_associations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_associations(request_options=request_options)
        return _response.data

    async def list_product_associations_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List product associations relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_associations_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_associations_relationships(request_options=request_options)
        return _response.data

    async def list_product_inverse_associations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List product inverse associations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_inverse_associations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_inverse_associations(request_options=request_options)
        return _response.data

    async def list_product_inverse_associations_index_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List product inverse associations index relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_inverse_associations_index_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_inverse_associations_index_relationships(
            request_options=request_options
        )
        return _response.data

    async def get_product_brand(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product brand

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_brand()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_brand(request_options=request_options)
        return _response.data

    async def get_product_brand_relationship(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product brand relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_brand_relationship()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_brand_relationship(request_options=request_options)
        return _response.data

    async def list_product_collection(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product collection

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_collection()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_collection(request_options=request_options)
        return _response.data

    async def list_product_collection_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List product collection relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_collection_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_collection_relationships(request_options=request_options)
        return _response.data

    async def list_product_images(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product images

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_images()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_images(request_options=request_options)
        return _response.data

    async def list_product_images_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List product images relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_images_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_images_relationships(request_options=request_options)
        return _response.data

    async def get_product_thumbnail(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product thumbnail

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_thumbnail()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_thumbnail(request_options=request_options)
        return _response.data

    async def get_product_thumbnail_relationship(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get product thumbnail relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_thumbnail_relationship()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_thumbnail_relationship(request_options=request_options)
        return _response.data

    async def get_product_lowest_price(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product lowest price

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_lowest_price()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_lowest_price(request_options=request_options)
        return _response.data

    async def get_product_lowest_price_relationship(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get product lowest price relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_lowest_price_relationship()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_lowest_price_relationship(request_options=request_options)
        return _response.data

    async def list_product_prices(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product prices

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_prices()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_prices(request_options=request_options)
        return _response.data

    async def list_product_prices_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List product prices relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_prices_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_prices_relationships(request_options=request_options)
        return _response.data

    async def list_product_variants(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product variants

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_variants()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_variants(request_options=request_options)
        return _response.data

    async def list_product_variants_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List product variants relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_variants_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_variants_relationships(request_options=request_options)
        return _response.data

    async def get_product_cheapest_variant(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product cheapest variant

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_cheapest_variant()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_cheapest_variant(request_options=request_options)
        return _response.data

    async def get_product_cheapest_variant_relationship(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get product cheapest variant relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_cheapest_variant_relationship()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_cheapest_variant_relationship(request_options=request_options)
        return _response.data

    async def list_product_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product tags

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_tags(request_options=request_options)
        return _response.data

    async def list_product_tags_relationship(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List product tags relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.list_product_tags_relationship()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_product_tags_relationship(request_options=request_options)
        return _response.data

    async def get_product_default_url(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get product default url

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_default_url()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_default_url(request_options=request_options)
        return _response.data

    async def get_product_default_url_relationship(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get product default url relationship

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.products.get_product_default_url_relationship()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product_default_url_relationship(request_options=request_options)
        return _response.data

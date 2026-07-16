

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawShopsClient, RawShopsClient


class ShopsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShopsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShopsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShopsClient
        """
        return self._raw_client

    def get_storefront_details_on_a_shop(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get storefront details on a shop.

        Parameters
        ----------
        id : str

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
        client.shops.get_storefront_details_on_a_shop(
            id="id",
        )
        """
        _response = self._raw_client.get_storefront_details_on_a_shop(id, request_options=request_options)
        return _response.data

    def list_of_shipping_profiles_for_your_shop(
        self, shop_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of shipping profiles for your shop

        Parameters
        ----------
        shop_id : str

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
        client.shops.list_of_shipping_profiles_for_your_shop(
            shop_id="shop_id",
        )
        """
        _response = self._raw_client.list_of_shipping_profiles_for_your_shop(shop_id, request_options=request_options)
        return _response.data

    def get_details_on_a_shop(
        self,
        slug: str,
        *,
        include_listing_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get details on a shop.

        Parameters
        ----------
        slug : str

        include_listing_count : typing.Optional[bool]
            Include the live listing count in the response.

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
        client.shops.get_details_on_a_shop(
            slug="slug",
        )
        """
        _response = self._raw_client.get_details_on_a_shop(
            slug, include_listing_count=include_listing_count, request_options=request_options
        )
        return _response.data

    def get_sellers_feedback(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get seller's feedback

        Parameters
        ----------
        slug : str

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
        client.shops.get_sellers_feedback(
            slug="slug",
        )
        """
        _response = self._raw_client.get_sellers_feedback(slug, request_options=request_options)
        return _response.data

    def get_sellers_feedback_as_a_buyer(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get seller's feedback as a buyer

        Parameters
        ----------
        slug : str

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
        client.shops.get_sellers_feedback_as_a_buyer(
            slug="slug",
        )
        """
        _response = self._raw_client.get_sellers_feedback_as_a_buyer(slug, request_options=request_options)
        return _response.data

    def get_sellers_feedback_as_a_seller(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get seller's feedback as a seller

        Parameters
        ----------
        slug : str

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
        client.shops.get_sellers_feedback_as_a_seller(
            slug="slug",
        )
        """
        _response = self._raw_client.get_sellers_feedback_as_a_seller(slug, request_options=request_options)
        return _response.data


class AsyncShopsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShopsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShopsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShopsClient
        """
        return self._raw_client

    async def get_storefront_details_on_a_shop(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get storefront details on a shop.

        Parameters
        ----------
        id : str

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
            await client.shops.get_storefront_details_on_a_shop(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_storefront_details_on_a_shop(id, request_options=request_options)
        return _response.data

    async def list_of_shipping_profiles_for_your_shop(
        self, shop_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of shipping profiles for your shop

        Parameters
        ----------
        shop_id : str

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
            await client.shops.list_of_shipping_profiles_for_your_shop(
                shop_id="shop_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_shipping_profiles_for_your_shop(
            shop_id, request_options=request_options
        )
        return _response.data

    async def get_details_on_a_shop(
        self,
        slug: str,
        *,
        include_listing_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get details on a shop.

        Parameters
        ----------
        slug : str

        include_listing_count : typing.Optional[bool]
            Include the live listing count in the response.

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
            await client.shops.get_details_on_a_shop(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_details_on_a_shop(
            slug, include_listing_count=include_listing_count, request_options=request_options
        )
        return _response.data

    async def get_sellers_feedback(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get seller's feedback

        Parameters
        ----------
        slug : str

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
            await client.shops.get_sellers_feedback(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sellers_feedback(slug, request_options=request_options)
        return _response.data

    async def get_sellers_feedback_as_a_buyer(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get seller's feedback as a buyer

        Parameters
        ----------
        slug : str

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
            await client.shops.get_sellers_feedback_as_a_buyer(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sellers_feedback_as_a_buyer(slug, request_options=request_options)
        return _response.data

    async def get_sellers_feedback_as_a_seller(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get seller's feedback as a seller

        Parameters
        ----------
        slug : str

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
            await client.shops.get_sellers_feedback_as_a_seller(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sellers_feedback_as_a_seller(slug, request_options=request_options)
        return _response.data

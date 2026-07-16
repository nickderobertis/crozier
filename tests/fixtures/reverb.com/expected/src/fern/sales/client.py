

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSalesClient, RawSalesClient


class SalesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSalesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSalesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSalesClient
        """
        return self._raw_client

    def view_upcoming_and_live_reverb_official_sales(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View upcoming and live Reverb official sales.

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
        client.sales.view_upcoming_and_live_reverb_official_sales()
        """
        _response = self._raw_client.view_upcoming_and_live_reverb_official_sales(request_options=request_options)
        return _response.data

    def view_your_created_sales(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        View your created sales.

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
        client.sales.view_your_created_sales()
        """
        _response = self._raw_client.view_your_created_sales(request_options=request_options)
        return _response.data

    def add_listings_to_a_sale(self, sale_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Add listings to a sale

        Parameters
        ----------
        sale_id : str

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
        client.sales.add_listings_to_a_sale(
            sale_id="sale_id",
        )
        """
        _response = self._raw_client.add_listings_to_a_sale(sale_id, request_options=request_options)
        return _response.data

    def remove_a_listing_from_a_sale(
        self, sale_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a listing from a sale

        Parameters
        ----------
        sale_id : str

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
        client.sales.remove_a_listing_from_a_sale(
            sale_id="sale_id",
        )
        """
        _response = self._raw_client.remove_a_listing_from_a_sale(sale_id, request_options=request_options)
        return _response.data

    def get_sales_slug(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
        client.sales.get_sales_slug(
            slug="slug",
        )
        """
        _response = self._raw_client.get_sales_slug(slug, request_options=request_options)
        return _response.data


class AsyncSalesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSalesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSalesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSalesClient
        """
        return self._raw_client

    async def view_upcoming_and_live_reverb_official_sales(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View upcoming and live Reverb official sales.

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
            await client.sales.view_upcoming_and_live_reverb_official_sales()


        asyncio.run(main())
        """
        _response = await self._raw_client.view_upcoming_and_live_reverb_official_sales(request_options=request_options)
        return _response.data

    async def view_your_created_sales(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        View your created sales.

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
            await client.sales.view_your_created_sales()


        asyncio.run(main())
        """
        _response = await self._raw_client.view_your_created_sales(request_options=request_options)
        return _response.data

    async def add_listings_to_a_sale(
        self, sale_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add listings to a sale

        Parameters
        ----------
        sale_id : str

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
            await client.sales.add_listings_to_a_sale(
                sale_id="sale_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_listings_to_a_sale(sale_id, request_options=request_options)
        return _response.data

    async def remove_a_listing_from_a_sale(
        self, sale_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a listing from a sale

        Parameters
        ----------
        sale_id : str

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
            await client.sales.remove_a_listing_from_a_sale(
                sale_id="sale_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_a_listing_from_a_sale(sale_id, request_options=request_options)
        return _response.data

    async def get_sales_slug(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
            await client.sales.get_sales_slug(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sales_slug(slug, request_options=request_options)
        return _response.data

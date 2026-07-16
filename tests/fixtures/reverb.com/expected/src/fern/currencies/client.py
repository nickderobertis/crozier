

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCurrenciesClient, RawCurrenciesClient


class CurrenciesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCurrenciesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCurrenciesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCurrenciesClient
        """
        return self._raw_client

    def list_of_supported_display_currencies_for_browsing_listings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of supported display currencies for browsing listings

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
        client.currencies.list_of_supported_display_currencies_for_browsing_listings()
        """
        _response = self._raw_client.list_of_supported_display_currencies_for_browsing_listings(
            request_options=request_options
        )
        return _response.data

    def list_of_supported_listing_currencies_for_shops(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of supported listing currencies for shops

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
        client.currencies.list_of_supported_listing_currencies_for_shops()
        """
        _response = self._raw_client.list_of_supported_listing_currencies_for_shops(request_options=request_options)
        return _response.data


class AsyncCurrenciesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCurrenciesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCurrenciesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCurrenciesClient
        """
        return self._raw_client

    async def list_of_supported_display_currencies_for_browsing_listings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of supported display currencies for browsing listings

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
            await client.currencies.list_of_supported_display_currencies_for_browsing_listings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_supported_display_currencies_for_browsing_listings(
            request_options=request_options
        )
        return _response.data

    async def list_of_supported_listing_currencies_for_shops(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of supported listing currencies for shops

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
            await client.currencies.list_of_supported_listing_currencies_for_shops()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_supported_listing_currencies_for_shops(
            request_options=request_options
        )
        return _response.data

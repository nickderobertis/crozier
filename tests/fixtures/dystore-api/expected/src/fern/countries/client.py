

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCountriesClient, RawCountriesClient


class CountriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCountriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCountriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCountriesClient
        """
        return self._raw_client

    def list_countries(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List countries

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
        client.countries.list_countries()
        """
        _response = self._raw_client.list_countries(request_options=request_options)
        return _response.data


class AsyncCountriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCountriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCountriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCountriesClient
        """
        return self._raw_client

    async def list_countries(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List countries

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
            await client.countries.list_countries()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_countries(request_options=request_options)
        return _response.data

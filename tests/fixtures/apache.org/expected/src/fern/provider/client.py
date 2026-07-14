

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProviderClient, RawProviderClient
from .types.get_providers_response import GetProvidersResponse


class ProviderClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProviderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProviderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProviderClient
        """
        return self._raw_client

    def get_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetProvidersResponse:
        """
        Get a list of providers.

        *New in version 2.1.0*

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProvidersResponse
            List of providers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.provider.get_providers()
        """
        _response = self._raw_client.get_providers(request_options=request_options)
        return _response.data


class AsyncProviderClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProviderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProviderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProviderClient
        """
        return self._raw_client

    async def get_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetProvidersResponse:
        """
        Get a list of providers.

        *New in version 2.1.0*

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProvidersResponse
            List of providers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.provider.get_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_providers(request_options=request_options)
        return _response.data

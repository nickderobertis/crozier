

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRelaygatewayClient, RawRelaygatewayClient


class RelaygatewayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRelaygatewayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRelaygatewayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRelaygatewayClient
        """
        return self._raw_client

    def bandpricing(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Band pricing.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.relaygateway.bandpricing()
        """
        _response = self._raw_client.bandpricing(request_options=request_options)
        return _response.data

    def all_(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Every gateway.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.relaygateway.all_()
        """
        _response = self._raw_client.all_(request_options=request_options)
        return _response.data


class AsyncRelaygatewayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRelaygatewayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRelaygatewayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRelaygatewayClient
        """
        return self._raw_client

    async def bandpricing(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Band pricing.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.relaygateway.bandpricing()


        asyncio.run(main())
        """
        _response = await self._raw_client.bandpricing(request_options=request_options)
        return _response.data

    async def all_(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Every gateway.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.relaygateway.all_()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(request_options=request_options)
        return _response.data

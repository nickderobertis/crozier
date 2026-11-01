

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRelayClient, RawRelayClient


class RelayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRelayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRelayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRelayClient
        """
        return self._raw_client

    def relay_gateway_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Relay gateway details.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.relay.relay_gateway_info()
        """
        _response = self._raw_client.relay_gateway_info(request_options=request_options)
        return _response.data

    def currentstatus(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Relay status.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.relay.currentstatus()
        """
        _response = self._raw_client.currentstatus(request_options=request_options)
        return _response.data


class AsyncRelayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRelayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRelayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRelayClient
        """
        return self._raw_client

    async def relay_gateway_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Relay gateway details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.relay.relay_gateway_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.relay_gateway_info(request_options=request_options)
        return _response.data

    async def currentstatus(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Relay status.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.relay.currentstatus()


        asyncio.run(main())
        """
        _response = await self._raw_client.currentstatus(request_options=request_options)
        return _response.data

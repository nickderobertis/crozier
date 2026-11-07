

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.discovery_response import DiscoveryResponse
from .raw_client import AsyncRawDiscoveryV1Client, RawDiscoveryV1Client


class DiscoveryV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDiscoveryV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDiscoveryV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDiscoveryV1Client
        """
        return self._raw_client

    def get_ping_service_endpoints(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DiscoveryResponse:
        """
        Returns an array of all regions with a host and port that a client can directly ping. Open a websocket connection to `wss://<host>:<port>/ws` and send a packet. To calculate ping, measure the time it takes to get an echo packet back.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiscoveryResponse
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.discovery_v1.get_ping_service_endpoints()
        """
        _response = self._raw_client.get_ping_service_endpoints(request_options=request_options)
        return _response.data


class AsyncDiscoveryV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDiscoveryV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDiscoveryV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDiscoveryV1Client
        """
        return self._raw_client

    async def get_ping_service_endpoints(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DiscoveryResponse:
        """
        Returns an array of all regions with a host and port that a client can directly ping. Open a websocket connection to `wss://<host>:<port>/ws` and send a packet. To calculate ping, measure the time it takes to get an echo packet back.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiscoveryResponse
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.discovery_v1.get_ping_service_endpoints()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ping_service_endpoints(request_options=request_options)
        return _response.data

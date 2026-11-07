

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dcp_capabilities import DcpCapabilities
from .raw_client import AsyncRawDiscoveryClient, RawDiscoveryClient


class DiscoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDiscoveryClient
        """
        return self._raw_client

    def get_capabilities(self, *, request_options: typing.Optional[RequestOptions] = None) -> DcpCapabilities:
        """
        Returns supported DCP versions, algorithms, wire formats, and feature flags.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DcpCapabilities
            DCP capabilities

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.discovery.get_capabilities()
        """
        _response = self._raw_client.get_capabilities(request_options=request_options)
        return _response.data


class AsyncDiscoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDiscoveryClient
        """
        return self._raw_client

    async def get_capabilities(self, *, request_options: typing.Optional[RequestOptions] = None) -> DcpCapabilities:
        """
        Returns supported DCP versions, algorithms, wire formats, and feature flags.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DcpCapabilities
            DCP capabilities

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.discovery.get_capabilities()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_capabilities(request_options=request_options)
        return _response.data

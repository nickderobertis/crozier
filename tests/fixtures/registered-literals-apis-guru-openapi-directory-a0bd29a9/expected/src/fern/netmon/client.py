

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNetmonClient, RawNetmonClient


class NetmonClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNetmonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNetmonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNetmonClient
        """
        return self._raw_client

    def get_internal_netmon_correlation(
        self, *, mac_address: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        mac_address : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.netmon.get_internal_netmon_correlation()
        """
        _response = self._raw_client.get_internal_netmon_correlation(
            mac_address=mac_address, request_options=request_options
        )
        return _response.data


class AsyncNetmonClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNetmonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNetmonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNetmonClient
        """
        return self._raw_client

    async def get_internal_netmon_correlation(
        self, *, mac_address: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        mac_address : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.netmon.get_internal_netmon_correlation()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_internal_netmon_correlation(
            mac_address=mac_address, request_options=request_options
        )
        return _response.data

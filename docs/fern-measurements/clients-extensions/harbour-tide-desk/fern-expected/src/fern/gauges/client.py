

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.gauge import Gauge
from .raw_client import AsyncRawGaugesClient, RawGaugesClient


class GaugesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGaugesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGaugesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGaugesClient
        """
        return self._raw_client

    def list_gauges(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Gauge]:
        """
        Lists the harbour's tide gauges.
        
        Calibration files sit under E:\\
        
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        typing.List[Gauge]
            The gauges.
        
        Examples
        --------
        from fern import FernApi
        
        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.gauges.list_gauges()
        """
        _response = self._raw_client.list_gauges(request_options=request_options)
        return _response.data


class AsyncGaugesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGaugesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGaugesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGaugesClient
        """
        return self._raw_client

    async def list_gauges(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Gauge]:
        """
        Lists the harbour's tide gauges.
        
        Calibration files sit under E:\\
        
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        typing.List[Gauge]
            The gauges.
        
        Examples
        --------
        import asyncio
        
        from fern import AsyncFernApi
        
        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )
        
        
        async def main() -> None:
            await client.gauges.list_gauges()
        
        
        asyncio.run(main())
        """
        _response = await self._raw_client.list_gauges(request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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

    def read(self, pump_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Parameters
        ----------
        pump_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            The gauge reading.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.gauges.read(
            pump_id="pumpId",
        )
        """
        _response = self._raw_client.read(pump_id, request_options=request_options)
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

    async def read(self, pump_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Parameters
        ----------
        pump_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            The gauge reading.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.gauges.read(
                pump_id="pumpId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(pump_id, request_options=request_options)
        return _response.data

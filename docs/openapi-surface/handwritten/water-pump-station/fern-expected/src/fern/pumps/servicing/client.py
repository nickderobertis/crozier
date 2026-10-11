

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawServicingClient, RawServicingClient


class ServicingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServicingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServicingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServicingClient
        """
        return self._raw_client

    def flush(self, pump_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        pump_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pumps.servicing.flush(
            pump_id="pumpId",
        )
        """
        _response = self._raw_client.flush(pump_id, request_options=request_options)
        return _response.data


class AsyncServicingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServicingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServicingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServicingClient
        """
        return self._raw_client

    async def flush(self, pump_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        pump_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pumps.servicing.flush(
                pump_id="pumpId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.flush(pump_id, request_options=request_options)
        return _response.data

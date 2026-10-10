

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.relay_state import RelayState
from .raw_client import AsyncRawSignalsClient, RawSignalsClient


class SignalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSignalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSignalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSignalsClient
        """
        return self._raw_client

    def status(self, relay_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RelayState:
        """
        Parameters
        ----------
        relay_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelayState
            The relay's state.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.signals.status(
            relay_id="relayId",
        )
        """
        _response = self._raw_client.status(relay_id, request_options=request_options)
        return _response.data


class AsyncSignalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSignalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSignalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSignalsClient
        """
        return self._raw_client

    async def status(self, relay_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RelayState:
        """
        Parameters
        ----------
        relay_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelayState
            The relay's state.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.signals.status(
                relay_id="relayId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.status(relay_id, request_options=request_options)
        return _response.data

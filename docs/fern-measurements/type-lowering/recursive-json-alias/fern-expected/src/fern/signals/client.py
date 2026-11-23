

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.signal import Signal
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

    def get_signal(self, signal_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Signal:
        """
        Parameters
        ----------
        signal_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Signal
            The signal.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.signals.get_signal(
            signal_id="signalId",
        )
        """
        _response = self._raw_client.get_signal(signal_id, request_options=request_options)
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

    async def get_signal(self, signal_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Signal:
        """
        Parameters
        ----------
        signal_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Signal
            The signal.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.signals.get_signal(
                signal_id="signalId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_signal(signal_id, request_options=request_options)
        return _response.data

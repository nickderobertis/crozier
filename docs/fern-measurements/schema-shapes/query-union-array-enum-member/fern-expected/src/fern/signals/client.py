

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSignalsClient, RawSignalsClient
from .types.inspect_signals_request_kind import InspectSignalsRequestKind


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

    def inspect_signals(
        self, *, kind: InspectSignalsRequestKind, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        kind : InspectSignalsRequestKind

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Accepted signal

        Examples
        --------
        from fern.signals import InspectSignalsRequestKindZero

        from fern import FernApi

        client = FernApi()
        client.signals.inspect_signals(
            kind=InspectSignalsRequestKindZero.OPTICAL,
        )
        """
        _response = self._raw_client.inspect_signals(kind=kind, request_options=request_options)
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

    async def inspect_signals(
        self, *, kind: InspectSignalsRequestKind, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        kind : InspectSignalsRequestKind

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Accepted signal

        Examples
        --------
        import asyncio

        from fern.signals import InspectSignalsRequestKindZero

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.signals.inspect_signals(
                kind=InspectSignalsRequestKindZero.OPTICAL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_signals(kind=kind, request_options=request_options)
        return _response.data

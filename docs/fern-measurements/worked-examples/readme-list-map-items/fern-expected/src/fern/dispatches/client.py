

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.receipt import Receipt
from .raw_client import AsyncRawDispatchesClient, RawDispatchesClient


OMIT = typing.cast(typing.Any, ...)


class DispatchesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDispatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDispatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDispatchesClient
        """
        return self._raw_client

    def send_dispatch(
        self,
        *,
        channel: str,
        notes: typing.Sequence[typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Receipt:
        """
        Parameters
        ----------
        channel : str

        notes : typing.Sequence[typing.Dict[str, typing.Any]]
            Free-form note objects; each item is a placeholder map.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            Queued

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.dispatches.send_dispatch(
            channel="channel",
            notes=[{"key": "value"}],
        )
        """
        _response = self._raw_client.send_dispatch(channel=channel, notes=notes, request_options=request_options)
        return _response.data


class AsyncDispatchesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDispatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDispatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDispatchesClient
        """
        return self._raw_client

    async def send_dispatch(
        self,
        *,
        channel: str,
        notes: typing.Sequence[typing.Dict[str, typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Receipt:
        """
        Parameters
        ----------
        channel : str

        notes : typing.Sequence[typing.Dict[str, typing.Any]]
            Free-form note objects; each item is a placeholder map.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            Queued

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.dispatches.send_dispatch(
                channel="channel",
                notes=[{"key": "value"}],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_dispatch(channel=channel, notes=notes, request_options=request_options)
        return _response.data

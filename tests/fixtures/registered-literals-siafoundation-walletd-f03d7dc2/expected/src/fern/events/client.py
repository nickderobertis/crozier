

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event import Event
from ..types.hash256 import Hash256
from .raw_client import AsyncRawEventsClient, RawEventsClient


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventsClient
        """
        return self._raw_client

    def get_event(self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None) -> Event:
        """
        Parameters
        ----------
        id : Hash256
            Event ID (hash).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Event
            Event information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.events.get_event(
            id="id",
        )
        """
        _response = self._raw_client.get_event(id, request_options=request_options)
        return _response.data


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventsClient
        """
        return self._raw_client

    async def get_event(self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None) -> Event:
        """
        Parameters
        ----------
        id : Hash256
            Event ID (hash).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Event
            Event information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.events.get_event(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_event(id, request_options=request_options)
        return _response.data

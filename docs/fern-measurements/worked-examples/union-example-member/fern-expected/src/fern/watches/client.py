

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alarm import Alarm
from ..types.receipt import Receipt
from ..types.trigger import Trigger
from .raw_client import AsyncRawWatchesClient, RawWatchesClient


OMIT = typing.cast(typing.Any, ...)


class WatchesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWatchesClient
        """
        return self._raw_client

    def create_watch(
        self, *, name: str, trigger: Trigger, alarm: Alarm, request_options: typing.Optional[RequestOptions] = None
    ) -> Receipt:
        """
        Parameters
        ----------
        name : str

        trigger : Trigger

        alarm : Alarm

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            Created

        Examples
        --------
        from fern import FernApi, SurgeAlarm, TideTrigger

        client = FernApi()
        client.watches.create_watch(
            name="name",
            trigger=TideTrigger(
                station="harbour-mouth",
                height_m=2.5,
            ),
            alarm=SurgeAlarm(
                id="alarm-7",
                surge_m=1.2,
            ),
        )
        """
        _response = self._raw_client.create_watch(
            name=name, trigger=trigger, alarm=alarm, request_options=request_options
        )
        return _response.data


class AsyncWatchesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWatchesClient
        """
        return self._raw_client

    async def create_watch(
        self, *, name: str, trigger: Trigger, alarm: Alarm, request_options: typing.Optional[RequestOptions] = None
    ) -> Receipt:
        """
        Parameters
        ----------
        name : str

        trigger : Trigger

        alarm : Alarm

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SurgeAlarm, TideTrigger

        client = AsyncFernApi()


        async def main() -> None:
            await client.watches.create_watch(
                name="name",
                trigger=TideTrigger(
                    station="harbour-mouth",
                    height_m=2.5,
                ),
                alarm=SurgeAlarm(
                    id="alarm-7",
                    surge_m=1.2,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_watch(
            name=name, trigger=trigger, alarm=alarm, request_options=request_options
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.gauge_channel_two import GaugeChannelTwo
from ..types.reading import Reading
from ..types.station_code_one import StationCodeOne
from .raw_client import AsyncRawReadingsClient, RawReadingsClient


OMIT = typing.cast(typing.Any, ...)


class ReadingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReadingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReadingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReadingsClient
        """
        return self._raw_client

    def submit_reading(
        self,
        *,
        station_code: StationCodeOne,
        level_cm: float,
        channel: typing.Optional[GaugeChannelTwo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reading:
        """
        Parameters
        ----------
        station_code : StationCodeOne

        level_cm : float

        channel : typing.Optional[GaugeChannelTwo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reading
            The stored reading.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.readings.submit_reading(
            station_code="station_code",
            level_cm=1.1,
        )
        """
        _response = self._raw_client.submit_reading(
            station_code=station_code, level_cm=level_cm, channel=channel, request_options=request_options
        )
        return _response.data


class AsyncReadingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReadingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReadingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReadingsClient
        """
        return self._raw_client

    async def submit_reading(
        self,
        *,
        station_code: StationCodeOne,
        level_cm: float,
        channel: typing.Optional[GaugeChannelTwo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reading:
        """
        Parameters
        ----------
        station_code : StationCodeOne

        level_cm : float

        channel : typing.Optional[GaugeChannelTwo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reading
            The stored reading.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.readings.submit_reading(
                station_code="station_code",
                level_cm=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_reading(
            station_code=station_code, level_cm=level_cm, channel=channel, request_options=request_options
        )
        return _response.data

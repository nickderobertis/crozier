

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTidesClient, RawTidesClient
from .types.get_surge_request_since import GetSurgeRequestSince
from .types.get_surge_response import GetSurgeResponse
from .types.get_tides_request_since import GetTidesRequestSince
from .types.get_tides_response import GetTidesResponse


class TidesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTidesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTidesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTidesClient
        """
        return self._raw_client

    def get_tides(
        self,
        station_id: str,
        *,
        since: GetTidesRequestSince,
        step: float,
        gauges: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTidesResponse:
        """
        Parameters
        ----------
        station_id : str

        since : GetTidesRequestSince

        step : float

        gauges : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Gauge numbers to read

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTidesResponse
            Readings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tides.get_tides(
            station_id="station_id",
            since={"key": "value"},
            step=1.1,
        )
        """
        _response = self._raw_client.get_tides(
            station_id, since=since, step=step, gauges=gauges, request_options=request_options
        )
        return _response.data

    def get_surge(
        self,
        station_id: str,
        *,
        since: GetSurgeRequestSince,
        gauges: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSurgeResponse:
        """
        Parameters
        ----------
        station_id : str

        since : GetSurgeRequestSince

        gauges : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSurgeResponse
            Readings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tides.get_surge(
            station_id="station_id",
            since={"key": "value"},
        )
        """
        _response = self._raw_client.get_surge(station_id, since=since, gauges=gauges, request_options=request_options)
        return _response.data


class AsyncTidesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTidesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTidesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTidesClient
        """
        return self._raw_client

    async def get_tides(
        self,
        station_id: str,
        *,
        since: GetTidesRequestSince,
        step: float,
        gauges: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTidesResponse:
        """
        Parameters
        ----------
        station_id : str

        since : GetTidesRequestSince

        step : float

        gauges : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Gauge numbers to read

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTidesResponse
            Readings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tides.get_tides(
                station_id="station_id",
                since={"key": "value"},
                step=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tides(
            station_id, since=since, step=step, gauges=gauges, request_options=request_options
        )
        return _response.data

    async def get_surge(
        self,
        station_id: str,
        *,
        since: GetSurgeRequestSince,
        gauges: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSurgeResponse:
        """
        Parameters
        ----------
        station_id : str

        since : GetSurgeRequestSince

        gauges : typing.Optional[typing.Union[float, typing.Sequence[float]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSurgeResponse
            Readings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tides.get_surge(
                station_id="station_id",
                since={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_surge(
            station_id, since=since, gauges=gauges, request_options=request_options
        )
        return _response.data

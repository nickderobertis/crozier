

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawQueryClient, RawQueryClient
from .types.get_heater_metrics_request_time_end import GetHeaterMetricsRequestTimeEnd
from .types.get_heater_metrics_request_time_start import GetHeaterMetricsRequestTimeStart
from .types.get_heater_metrics_response import GetHeaterMetricsResponse
from .types.get_thermo_metrics_request_time_end import GetThermoMetricsRequestTimeEnd
from .types.get_thermo_metrics_request_time_start import GetThermoMetricsRequestTimeStart
from .types.get_thermo_metrics_response import GetThermoMetricsResponse


class QueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueryClient
        """
        return self._raw_client

    def get_thermo_metrics(
        self,
        system_id: str,
        *,
        time_start: GetThermoMetricsRequestTimeStart,
        time_end: GetThermoMetricsRequestTimeEnd,
        interval: float,
        channels: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetThermoMetricsResponse:
        """
        Query thermometer metrics data from time series database

        Parameters
        ----------
        system_id : str

        time_start : GetThermoMetricsRequestTimeStart
            Start time for the query in ISO format

        time_end : GetThermoMetricsRequestTimeEnd
            End time for the query in ISO format

        interval : float
            Interval in seconds for time bucketing

        channels : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            List of channel numbers to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetThermoMetricsResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.query.get_thermo_metrics(
            system_id="system_id",
            time_start={"key": "value"},
            time_end={"key": "value"},
            interval=1.1,
        )
        """
        _response = self._raw_client.get_thermo_metrics(
            system_id,
            time_start=time_start,
            time_end=time_end,
            interval=interval,
            channels=channels,
            request_options=request_options,
        )
        return _response.data

    def get_heater_metrics(
        self,
        system_id: str,
        *,
        time_start: GetHeaterMetricsRequestTimeStart,
        time_end: GetHeaterMetricsRequestTimeEnd,
        interval: float,
        channels: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetHeaterMetricsResponse:
        """
        Query heater metrics data from time series database

        Parameters
        ----------
        system_id : str

        time_start : GetHeaterMetricsRequestTimeStart
            Start time for the query in ISO format

        time_end : GetHeaterMetricsRequestTimeEnd
            End time for the query in ISO format

        interval : float
            Interval in seconds for time bucketing

        channels : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            List of heater channel numbers to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHeaterMetricsResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.query.get_heater_metrics(
            system_id="system_id",
            time_start={"key": "value"},
            time_end={"key": "value"},
            interval=1.1,
        )
        """
        _response = self._raw_client.get_heater_metrics(
            system_id,
            time_start=time_start,
            time_end=time_end,
            interval=interval,
            channels=channels,
            request_options=request_options,
        )
        return _response.data


class AsyncQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueryClient
        """
        return self._raw_client

    async def get_thermo_metrics(
        self,
        system_id: str,
        *,
        time_start: GetThermoMetricsRequestTimeStart,
        time_end: GetThermoMetricsRequestTimeEnd,
        interval: float,
        channels: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetThermoMetricsResponse:
        """
        Query thermometer metrics data from time series database

        Parameters
        ----------
        system_id : str

        time_start : GetThermoMetricsRequestTimeStart
            Start time for the query in ISO format

        time_end : GetThermoMetricsRequestTimeEnd
            End time for the query in ISO format

        interval : float
            Interval in seconds for time bucketing

        channels : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            List of channel numbers to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetThermoMetricsResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.query.get_thermo_metrics(
                system_id="system_id",
                time_start={"key": "value"},
                time_end={"key": "value"},
                interval=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_thermo_metrics(
            system_id,
            time_start=time_start,
            time_end=time_end,
            interval=interval,
            channels=channels,
            request_options=request_options,
        )
        return _response.data

    async def get_heater_metrics(
        self,
        system_id: str,
        *,
        time_start: GetHeaterMetricsRequestTimeStart,
        time_end: GetHeaterMetricsRequestTimeEnd,
        interval: float,
        channels: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetHeaterMetricsResponse:
        """
        Query heater metrics data from time series database

        Parameters
        ----------
        system_id : str

        time_start : GetHeaterMetricsRequestTimeStart
            Start time for the query in ISO format

        time_end : GetHeaterMetricsRequestTimeEnd
            End time for the query in ISO format

        interval : float
            Interval in seconds for time bucketing

        channels : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            List of heater channel numbers to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHeaterMetricsResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.query.get_heater_metrics(
                system_id="system_id",
                time_start={"key": "value"},
                time_end={"key": "value"},
                interval=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_heater_metrics(
            system_id,
            time_start=time_start,
            time_end=time_end,
            interval=interval,
            channels=channels,
            request_options=request_options,
        )
        return _response.data

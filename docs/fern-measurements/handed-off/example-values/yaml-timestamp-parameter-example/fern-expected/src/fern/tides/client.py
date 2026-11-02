

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tide_reading import TideReading
from .raw_client import AsyncRawTidesClient, RawTidesClient
from .types.get_gauge_response import GetGaugeResponse


OMIT = typing.cast(typing.Any, ...)


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

    def list_tides(
        self,
        *,
        since: dt.datetime,
        recorded_on: str,
        until: typing.Optional[dt.datetime] = None,
        logged_after: typing.Optional[str] = None,
        station: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[float]:
        """
        Parameters
        ----------
        since : dt.datetime

        recorded_on : str

        until : typing.Optional[dt.datetime]

        logged_after : typing.Optional[str]

        station : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            Readings

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tides.list_tides(
            since=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            recorded_on="recordedOn",
            station="pier-7",
        )
        """
        _response = self._raw_client.list_tides(
            since=since,
            recorded_on=recorded_on,
            until=until,
            logged_after=logged_after,
            station=station,
            request_options=request_options,
        )
        return _response.data

    def get_gauge(
        self,
        gauge_id: str,
        *,
        as_of: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetGaugeResponse:
        """
        Parameters
        ----------
        gauge_id : str

        as_of : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGaugeResponse
            The gauge

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tides.get_gauge(
            gauge_id="gauge-12",
        )
        """
        _response = self._raw_client.get_gauge(gauge_id, as_of=as_of, request_options=request_options)
        return _response.data

    def log_reading(
        self,
        gauge_id: str,
        *,
        level: float,
        high_water_at: dt.datetime,
        low_water_at: typing.Optional[dt.datetime] = OMIT,
        calibrated_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A body whose schema-level example gives date-time properties unquoted YAML timestamps, beside the sentinel instant the pair also drops.

        Parameters
        ----------
        gauge_id : str

        level : float

        high_water_at : dt.datetime

        low_water_at : typing.Optional[dt.datetime]

        calibrated_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tides.log_reading(
            gauge_id="gaugeId",
            level=3.4,
            high_water_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            low_water_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            calibrated_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.log_reading(
            gauge_id,
            level=level,
            high_water_at=high_water_at,
            low_water_at=low_water_at,
            calibrated_at=calibrated_at,
            request_options=request_options,
        )
        return _response.data

    def log_readings(
        self,
        gauge_id: str,
        *,
        request: typing.Sequence[TideReading],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The same schema posted as an array body.

        Parameters
        ----------
        gauge_id : str

        request : typing.Sequence[TideReading]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi, TideReading

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tides.log_readings(
            gauge_id="gaugeId",
            request=[
                TideReading(
                    level=3.4,
                    high_water_at=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    low_water_at=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    calibrated_at=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.log_readings(gauge_id, request=request, request_options=request_options)
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

    async def list_tides(
        self,
        *,
        since: dt.datetime,
        recorded_on: str,
        until: typing.Optional[dt.datetime] = None,
        logged_after: typing.Optional[str] = None,
        station: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[float]:
        """
        Parameters
        ----------
        since : dt.datetime

        recorded_on : str

        until : typing.Optional[dt.datetime]

        logged_after : typing.Optional[str]

        station : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            Readings

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tides.list_tides(
                since=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                recorded_on="recordedOn",
                station="pier-7",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tides(
            since=since,
            recorded_on=recorded_on,
            until=until,
            logged_after=logged_after,
            station=station,
            request_options=request_options,
        )
        return _response.data

    async def get_gauge(
        self,
        gauge_id: str,
        *,
        as_of: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetGaugeResponse:
        """
        Parameters
        ----------
        gauge_id : str

        as_of : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGaugeResponse
            The gauge

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tides.get_gauge(
                gauge_id="gauge-12",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gauge(gauge_id, as_of=as_of, request_options=request_options)
        return _response.data

    async def log_reading(
        self,
        gauge_id: str,
        *,
        level: float,
        high_water_at: dt.datetime,
        low_water_at: typing.Optional[dt.datetime] = OMIT,
        calibrated_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A body whose schema-level example gives date-time properties unquoted YAML timestamps, beside the sentinel instant the pair also drops.

        Parameters
        ----------
        gauge_id : str

        level : float

        high_water_at : dt.datetime

        low_water_at : typing.Optional[dt.datetime]

        calibrated_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tides.log_reading(
                gauge_id="gaugeId",
                level=3.4,
                high_water_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                low_water_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                calibrated_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.log_reading(
            gauge_id,
            level=level,
            high_water_at=high_water_at,
            low_water_at=low_water_at,
            calibrated_at=calibrated_at,
            request_options=request_options,
        )
        return _response.data

    async def log_readings(
        self,
        gauge_id: str,
        *,
        request: typing.Sequence[TideReading],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The same schema posted as an array body.

        Parameters
        ----------
        gauge_id : str

        request : typing.Sequence[TideReading]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, TideReading

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tides.log_readings(
                gauge_id="gaugeId",
                request=[
                    TideReading(
                        level=3.4,
                        high_water_at=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        low_water_at=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        calibrated_at=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.log_readings(gauge_id, request=request, request_options=request_options)
        return _response.data

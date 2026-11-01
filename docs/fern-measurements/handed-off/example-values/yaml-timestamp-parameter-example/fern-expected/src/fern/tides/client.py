

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTidesClient, RawTidesClient


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



import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.museum_hours import MuseumHours
from .raw_client import AsyncRawOperationsClient, RawOperationsClient


class OperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOperationsClient
        """
        return self._raw_client

    def get_museum_hours(
        self,
        *,
        start_date: typing.Optional[dt.date] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MuseumHours:
        """
        Get upcoming museum operating hours.

        Parameters
        ----------
        start_date : typing.Optional[dt.date]
            Starting date to retrieve future operating hours from. Defaults to today's date.

        page : typing.Optional[int]
            Page number to retrieve.

        limit : typing.Optional[int]
            Number of days per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MuseumHours
            Success.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.operations.get_museum_hours(
            start_date=datetime.date.fromisoformat(
                "2023-02-23",
            ),
            page=2,
            limit=15,
        )
        """
        _response = self._raw_client.get_museum_hours(
            start_date=start_date, page=page, limit=limit, request_options=request_options
        )
        return _response.data


class AsyncOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOperationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOperationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOperationsClient
        """
        return self._raw_client

    async def get_museum_hours(
        self,
        *,
        start_date: typing.Optional[dt.date] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MuseumHours:
        """
        Get upcoming museum operating hours.

        Parameters
        ----------
        start_date : typing.Optional[dt.date]
            Starting date to retrieve future operating hours from. Defaults to today's date.

        page : typing.Optional[int]
            Page number to retrieve.

        limit : typing.Optional[int]
            Number of days per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MuseumHours
            Success.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.operations.get_museum_hours(
                start_date=datetime.date.fromisoformat(
                    "2023-02-23",
                ),
                page=2,
                limit=15,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_museum_hours(
            start_date=start_date, page=page, limit=limit, request_options=request_options
        )
        return _response.data



import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.statistics import Statistics
from .raw_client import AsyncRawStatisticsClient, RawStatisticsClient


class StatisticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatisticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatisticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatisticsClient
        """
        return self._raw_client

    def fetch_server_statistics(
        self, *, from_: dt.datetime, to: dt.datetime, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Statistics]:
        """
        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Statistics]
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.statistics.fetch_server_statistics(
            from_=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            to=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.fetch_server_statistics(from_=from_, to=to, request_options=request_options)
        return _response.data


class AsyncStatisticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatisticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatisticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatisticsClient
        """
        return self._raw_client

    async def fetch_server_statistics(
        self, *, from_: dt.datetime, to: dt.datetime, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Statistics]:
        """
        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Statistics]
            OK

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
            await client.statistics.fetch_server_statistics(
                from_=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_server_statistics(from_=from_, to=to, request_options=request_options)
        return _response.data

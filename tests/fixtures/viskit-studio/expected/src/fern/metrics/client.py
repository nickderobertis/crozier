

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.weekly_metrics_response import WeeklyMetricsResponse
from .raw_client import AsyncRawMetricsClient, RawMetricsClient


class MetricsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetricsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetricsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetricsClient
        """
        return self._raw_client

    def get_weekly_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> WeeklyMetricsResponse:
        """
        Aggregate live metrics — current-ISO-week kits + 12-week sparklines.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeeklyMetricsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.metrics.get_weekly_metrics()
        """
        _response = self._raw_client.get_weekly_metrics(request_options=request_options)
        return _response.data


class AsyncMetricsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetricsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetricsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetricsClient
        """
        return self._raw_client

    async def get_weekly_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WeeklyMetricsResponse:
        """
        Aggregate live metrics — current-ISO-week kits + 12-week sparklines.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeeklyMetricsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.metrics.get_weekly_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_weekly_metrics(request_options=request_options)
        return _response.data

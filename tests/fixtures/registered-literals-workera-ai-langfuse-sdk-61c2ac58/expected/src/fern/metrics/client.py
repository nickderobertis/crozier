

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.daily_metrics import DailyMetrics
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

    def daily(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        trace_name: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyMetrics:
        """
        Get daily metrics of the Langfuse project

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        trace_name : typing.Optional[str]
            Optional filter by the name of the trace

        user_id : typing.Optional[str]
            Optional filter by the userId associated with the trace

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for metrics where traces include all of these tags

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for metrics where events include any of these environments

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces and observations on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces and observations before a certain datetime (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyMetrics


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.metrics.daily()
        """
        _response = self._raw_client.daily(
            page=page,
            limit=limit,
            trace_name=trace_name,
            user_id=user_id,
            tags=tags,
            environment=environment,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            request_options=request_options,
        )
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

    async def daily(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        trace_name: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyMetrics:
        """
        Get daily metrics of the Langfuse project

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        trace_name : typing.Optional[str]
            Optional filter by the name of the trace

        user_id : typing.Optional[str]
            Optional filter by the userId associated with the trace

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for metrics where traces include all of these tags

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for metrics where events include any of these environments

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces and observations on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include traces and observations before a certain datetime (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyMetrics


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.metrics.daily()


        asyncio.run(main())
        """
        _response = await self._raw_client.daily(
            page=page,
            limit=limit,
            trace_name=trace_name,
            user_id=user_id,
            tags=tags,
            environment=environment,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            request_options=request_options,
        )
        return _response.data

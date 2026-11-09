

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.metric_name import MetricName
from ..types.metrics_response import MetricsResponse
from ..types.metrics_step import MetricsStep
from ..types.process_id import ProcessId
from .raw_client import AsyncRawMetricsV1Client, RawMetricsV1Client


class MetricsV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetricsV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetricsV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetricsV1Client
        """
        return self._raw_client

    def get_metrics(
        self,
        app_id: AppId,
        process_id: ProcessId,
        *,
        metrics: typing.Optional[typing.Union[MetricName, typing.Sequence[MetricName]]] = None,
        end: typing.Optional[float] = None,
        start: typing.Optional[float] = None,
        step: typing.Optional[MetricsStep] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetricsResponse:
        """
        Get metrics for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        metrics : typing.Optional[typing.Union[MetricName, typing.Sequence[MetricName]]]
            Available metrics to query over time.

        end : typing.Optional[float]
            Unix timestamp. Default is current time.

        start : typing.Optional[float]
            Unix timestamp. Default is -1 hour from `end`.

        step : typing.Optional[MetricsStep]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricsResponse
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics_v1.get_metrics(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
        )
        """
        _response = self._raw_client.get_metrics(
            app_id, process_id, metrics=metrics, end=end, start=start, step=step, request_options=request_options
        )
        return _response.data


class AsyncMetricsV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetricsV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetricsV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetricsV1Client
        """
        return self._raw_client

    async def get_metrics(
        self,
        app_id: AppId,
        process_id: ProcessId,
        *,
        metrics: typing.Optional[typing.Union[MetricName, typing.Sequence[MetricName]]] = None,
        end: typing.Optional[float] = None,
        start: typing.Optional[float] = None,
        step: typing.Optional[MetricsStep] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetricsResponse:
        """
        Get metrics for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        metrics : typing.Optional[typing.Union[MetricName, typing.Sequence[MetricName]]]
            Available metrics to query over time.

        end : typing.Optional[float]
            Unix timestamp. Default is current time.

        start : typing.Optional[float]
            Unix timestamp. Default is -1 hour from `end`.

        step : typing.Optional[MetricsStep]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetricsResponse
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics_v1.get_metrics(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_metrics(
            app_id, process_id, metrics=metrics, end=end, start=start, step=step, request_options=request_options
        )
        return _response.data

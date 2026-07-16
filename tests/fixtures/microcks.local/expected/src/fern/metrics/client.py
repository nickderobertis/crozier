

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.counter_map import CounterMap
from ..types.daily_invocation_statistic import DailyInvocationStatistic
from ..types.test_conformance_metric import TestConformanceMetric
from ..types.test_result_summary import TestResultSummary
from ..types.weighted_metric_value import WeightedMetricValue
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

    def get_conformance_metrics_aggregation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WeightedMetricValue]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WeightedMetricValue]
            Get aggregated coverage metric value

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics.get_conformance_metrics_aggregation()
        """
        _response = self._raw_client.get_conformance_metrics_aggregation(request_options=request_options)
        return _response.data

    def get_service_test_conformance_metric(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestConformanceMetric:
        """
        Parameters
        ----------
        service_id : str
            Unique Services identifier this metrics are related to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestConformanceMetric
            Test coverage metric for Service

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics.get_service_test_conformance_metric(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.get_service_test_conformance_metric(service_id, request_options=request_options)
        return _response.data

    def get_aggregated_invocations_stats(
        self, *, day: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyInvocationStatistic:
        """
        Parameters
        ----------
        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyInvocationStatistic
            Aggregated invocation statistics for specified day

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics.get_aggregated_invocations_stats()
        """
        _response = self._raw_client.get_aggregated_invocations_stats(day=day, request_options=request_options)
        return _response.data

    def get_latest_aggregated_invocations_stats(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> CounterMap:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Number of days to get back in time. Default is 20.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CounterMap
            A map where keys are day (formatted using yyyyMMdd pattern) and values are counter of invocations on this day

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics.get_latest_aggregated_invocations_stats()
        """
        _response = self._raw_client.get_latest_aggregated_invocations_stats(
            limit=limit, request_options=request_options
        )
        return _response.data

    def get_top_ivnocations_stats_by_day(
        self,
        *,
        day: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DailyInvocationStatistic]:
        """
        Parameters
        ----------
        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        limit : typing.Optional[int]
            The number of top invoked mocks to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DailyInvocationStatistic]
            Top invocations for a defined day

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics.get_top_ivnocations_stats_by_day()
        """
        _response = self._raw_client.get_top_ivnocations_stats_by_day(
            day=day, limit=limit, request_options=request_options
        )
        return _response.data

    def get_invocation_stats_by_service(
        self,
        service_name: str,
        service_version: str,
        *,
        day: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyInvocationStatistic:
        """
        Parameters
        ----------
        service_name : str
            Name of service to get statistics for

        service_version : str
            Version of service to get statistics for

        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyInvocationStatistic
            Invocation statistics for service for specified day

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics.get_invocation_stats_by_service(
            service_name="serviceName",
            service_version="serviceVersion",
        )
        """
        _response = self._raw_client.get_invocation_stats_by_service(
            service_name, service_version, day=day, request_options=request_options
        )
        return _response.data

    def get_latest_test_results(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TestResultSummary]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Number of days to consider for test results to return. Default is 7 (one week)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestResultSummary]
            Test results summary for specified <limit> last days.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics.get_latest_test_results()
        """
        _response = self._raw_client.get_latest_test_results(limit=limit, request_options=request_options)
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

    async def get_conformance_metrics_aggregation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WeightedMetricValue]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WeightedMetricValue]
            Get aggregated coverage metric value

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics.get_conformance_metrics_aggregation()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conformance_metrics_aggregation(request_options=request_options)
        return _response.data

    async def get_service_test_conformance_metric(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestConformanceMetric:
        """
        Parameters
        ----------
        service_id : str
            Unique Services identifier this metrics are related to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestConformanceMetric
            Test coverage metric for Service

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics.get_service_test_conformance_metric(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_test_conformance_metric(
            service_id, request_options=request_options
        )
        return _response.data

    async def get_aggregated_invocations_stats(
        self, *, day: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DailyInvocationStatistic:
        """
        Parameters
        ----------
        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyInvocationStatistic
            Aggregated invocation statistics for specified day

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics.get_aggregated_invocations_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_aggregated_invocations_stats(day=day, request_options=request_options)
        return _response.data

    async def get_latest_aggregated_invocations_stats(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> CounterMap:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Number of days to get back in time. Default is 20.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CounterMap
            A map where keys are day (formatted using yyyyMMdd pattern) and values are counter of invocations on this day

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics.get_latest_aggregated_invocations_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_latest_aggregated_invocations_stats(
            limit=limit, request_options=request_options
        )
        return _response.data

    async def get_top_ivnocations_stats_by_day(
        self,
        *,
        day: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DailyInvocationStatistic]:
        """
        Parameters
        ----------
        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        limit : typing.Optional[int]
            The number of top invoked mocks to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DailyInvocationStatistic]
            Top invocations for a defined day

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics.get_top_ivnocations_stats_by_day()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_top_ivnocations_stats_by_day(
            day=day, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_invocation_stats_by_service(
        self,
        service_name: str,
        service_version: str,
        *,
        day: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DailyInvocationStatistic:
        """
        Parameters
        ----------
        service_name : str
            Name of service to get statistics for

        service_version : str
            Version of service to get statistics for

        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DailyInvocationStatistic
            Invocation statistics for service for specified day

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics.get_invocation_stats_by_service(
                service_name="serviceName",
                service_version="serviceVersion",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_invocation_stats_by_service(
            service_name, service_version, day=day, request_options=request_options
        )
        return _response.data

    async def get_latest_test_results(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TestResultSummary]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Number of days to consider for test results to return. Default is 7 (one week)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TestResultSummary]
            Test results summary for specified <limit> last days.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics.get_latest_test_results()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_latest_test_results(limit=limit, request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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

    def scrape_prometheus_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Serves the Prometheus metrics exposition when `metricsEnabled` is set, negotiating the text or OpenMetrics format from the Accept header. Returns 404 when metrics are disabled. Unlike its sibling control-plane endpoints this path has deliberately NO bare `/metrics` alias, because `/metrics` is a plausible path for a user's own mocked API and reserving it would shadow their expectation. It is gated by control-plane authentication like every neighbouring endpoint; since control-plane authentication is off by default an unauthenticated scrape keeps working on a default instance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            metrics exposition returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metrics.scrape_prometheus_metrics()
        """
        _response = self._raw_client.scrape_prometheus_metrics(request_options=request_options)
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

    async def scrape_prometheus_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Serves the Prometheus metrics exposition when `metricsEnabled` is set, negotiating the text or OpenMetrics format from the Accept header. Returns 404 when metrics are disabled. Unlike its sibling control-plane endpoints this path has deliberately NO bare `/metrics` alias, because `/metrics` is a plausible path for a user's own mocked API and reserving it would shadow their expectation. It is gated by control-plane authentication like every neighbouring endpoint; since control-plane authentication is off by default an unauthenticated scrape keeps working on a default instance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            metrics exposition returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metrics.scrape_prometheus_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.scrape_prometheus_metrics(request_options=request_options)
        return _response.data

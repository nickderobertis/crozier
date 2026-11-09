

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

    def metrics_api_get_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.metrics.metrics_api_get_metrics()
        """
        _response = self._raw_client.metrics_api_get_metrics(request_options=request_options)
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

    async def metrics_api_get_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.metrics.metrics_api_get_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.metrics_api_get_metrics(request_options=request_options)
        return _response.data

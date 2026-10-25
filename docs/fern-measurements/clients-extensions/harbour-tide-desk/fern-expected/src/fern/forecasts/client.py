

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.forecast import Forecast
from .raw_client import AsyncRawForecastsClient, RawForecastsClient


OMIT = typing.cast(typing.Any, ...)


class ForecastsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawForecastsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawForecastsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawForecastsClient
        """
        return self._raw_client

    def forecast_the_next_tide(self, *, port: str, request_options: typing.Optional[RequestOptions] = None) -> Forecast:
        """
        Parameters
        ----------
        port : str
            The port to forecast for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Forecast


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forecasts.forecast_the_next_tide(
            port="port",
        )
        """
        _response = self._raw_client.forecast_the_next_tide(port=port, request_options=request_options)
        return _response.data


class AsyncForecastsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawForecastsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawForecastsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawForecastsClient
        """
        return self._raw_client

    async def forecast_the_next_tide(
        self, *, port: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Forecast:
        """
        Parameters
        ----------
        port : str
            The port to forecast for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Forecast


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forecasts.forecast_the_next_tide(
                port="port",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.forecast_the_next_tide(port=port, request_options=request_options)
        return _response.data

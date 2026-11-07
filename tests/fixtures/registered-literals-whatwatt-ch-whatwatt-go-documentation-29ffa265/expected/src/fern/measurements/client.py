

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMeasurementsClient, RawMeasurementsClient
from .types.get_report_response import GetReportResponse


class MeasurementsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMeasurementsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMeasurementsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMeasurementsClient
        """
        return self._raw_client

    def get_report(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetReportResponse:
        """
        Returns the latest measurement envelope including instantaneous and aggregated values.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetReportResponse
            Measurement report envelope

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.measurements.get_report()
        """
        _response = self._raw_client.get_report(request_options=request_options)
        return _response.data


class AsyncMeasurementsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMeasurementsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMeasurementsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMeasurementsClient
        """
        return self._raw_client

    async def get_report(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetReportResponse:
        """
        Returns the latest measurement envelope including instantaneous and aggregated values.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetReportResponse
            Measurement report envelope

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.measurements.get_report()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_report(request_options=request_options)
        return _response.data

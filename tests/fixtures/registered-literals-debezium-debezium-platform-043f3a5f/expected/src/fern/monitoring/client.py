

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.instant import Instant
from ..types.panel_query_response import PanelQueryResponse
from ..types.panels_list_response import PanelsListResponse
from .raw_client import AsyncRawMonitoringClient, RawMonitoringClient


class MonitoringClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonitoringClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonitoringClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonitoringClient
        """
        return self._raw_client

    def list_available_monitoring_panels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PanelsListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PanelsListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitoring.list_available_monitoring_panels()
        """
        _response = self._raw_client.list_available_monitoring_panels(request_options=request_options)
        return _response.data

    def query_monitoring_panel_data_for_a_specific_pipeline(
        self,
        id: str,
        *,
        end: Instant,
        pipeline_id: str,
        start: Instant,
        step: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PanelQueryResponse:
        """
        Parameters
        ----------
        id : str

        end : Instant
            End time (ISO 8601)

        pipeline_id : str
            Pipeline identifier

        start : Instant
            Start time (ISO 8601)

        step : typing.Optional[str]
            Query resolution step (e.g. 15s, 1m)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PanelQueryResponse
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitoring.query_monitoring_panel_data_for_a_specific_pipeline(
            id="id",
            end=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            pipeline_id="pipeline_id",
            start=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.query_monitoring_panel_data_for_a_specific_pipeline(
            id, end=end, pipeline_id=pipeline_id, start=start, step=step, request_options=request_options
        )
        return _response.data


class AsyncMonitoringClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonitoringClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonitoringClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonitoringClient
        """
        return self._raw_client

    async def list_available_monitoring_panels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PanelsListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PanelsListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitoring.list_available_monitoring_panels()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_available_monitoring_panels(request_options=request_options)
        return _response.data

    async def query_monitoring_panel_data_for_a_specific_pipeline(
        self,
        id: str,
        *,
        end: Instant,
        pipeline_id: str,
        start: Instant,
        step: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PanelQueryResponse:
        """
        Parameters
        ----------
        id : str

        end : Instant
            End time (ISO 8601)

        pipeline_id : str
            Pipeline identifier

        start : Instant
            Start time (ISO 8601)

        step : typing.Optional[str]
            Query resolution step (e.g. 15s, 1m)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PanelQueryResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitoring.query_monitoring_panel_data_for_a_specific_pipeline(
                id="id",
                end=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                pipeline_id="pipeline_id",
                start=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_monitoring_panel_data_for_a_specific_pipeline(
            id, end=end, pipeline_id=pipeline_id, start=start, step=step, request_options=request_options
        )
        return _response.data

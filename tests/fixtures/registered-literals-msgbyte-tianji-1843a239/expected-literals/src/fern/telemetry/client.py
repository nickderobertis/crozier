

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTelemetryClient, RawTelemetryClient
from .types.telemetry_all_response_item import TelemetryAllResponseItem
from .types.telemetry_delete_response import TelemetryDeleteResponse
from .types.telemetry_info_response import TelemetryInfoResponse
from .types.telemetry_metrics_request_type import TelemetryMetricsRequestType
from .types.telemetry_metrics_response_item import TelemetryMetricsResponseItem
from .types.telemetry_pageviews_response import TelemetryPageviewsResponse
from .types.telemetry_stats_response import TelemetryStatsResponse
from .types.telemetry_upsert_response import TelemetryUpsertResponse


OMIT = typing.cast(typing.Any, ...)


class TelemetryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTelemetryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTelemetryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTelemetryClient
        """
        return self._raw_client

    def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TelemetryAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TelemetryAllResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.all_(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    def info(
        self, workspace_id: str, *, telemetry_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[TelemetryInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[TelemetryInfoResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.info(
            workspace_id="workspaceId",
            telemetry_id="telemetryId",
        )
        """
        _response = self._raw_client.info(workspace_id, telemetry_id=telemetry_id, request_options=request_options)
        return _response.data

    def alleventcount(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, float]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, float]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.alleventcount(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.alleventcount(workspace_id, request_options=request_options)
        return _response.data

    def eventcount(
        self, workspace_id: str, *, telemetry_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.eventcount(
            workspace_id="workspaceId",
            telemetry_id="telemetryId",
        )
        """
        _response = self._raw_client.eventcount(
            workspace_id, telemetry_id=telemetry_id, request_options=request_options
        )
        return _response.data

    def upsert(
        self,
        workspace_id: str,
        *,
        name: str,
        telemetry_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TelemetryUpsertResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        telemetry_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TelemetryUpsertResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.upsert(
            workspace_id="workspaceId",
            name="name",
        )
        """
        _response = self._raw_client.upsert(
            workspace_id, name=name, telemetry_id=telemetry_id, request_options=request_options
        )
        return _response.data

    def delete(
        self, workspace_id: str, *, telemetry_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TelemetryDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TelemetryDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.delete(
            workspace_id="workspaceId",
            telemetry_id="telemetryId",
        )
        """
        _response = self._raw_client.delete(workspace_id, telemetry_id=telemetry_id, request_options=request_options)
        return _response.data

    def pageviews(
        self,
        workspace_id: str,
        *,
        telemetry_id: str,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TelemetryPageviewsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TelemetryPageviewsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.pageviews(
            workspace_id="workspaceId",
            telemetry_id="telemetryId",
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.pageviews(
            workspace_id,
            telemetry_id=telemetry_id,
            start_at=start_at,
            end_at=end_at,
            unit=unit,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    def metrics(
        self,
        workspace_id: str,
        *,
        telemetry_id: str,
        type: TelemetryMetricsRequestType,
        start_at: float,
        end_at: float,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TelemetryMetricsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        type : TelemetryMetricsRequestType

        start_at : float

        end_at : float

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TelemetryMetricsResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.metrics(
            workspace_id="workspaceId",
            telemetry_id="telemetryId",
            type="source",
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.metrics(
            workspace_id,
            telemetry_id=telemetry_id,
            type=type,
            start_at=start_at,
            end_at=end_at,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    def stats(
        self,
        workspace_id: str,
        *,
        telemetry_id: str,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TelemetryStatsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TelemetryStatsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.telemetry.stats(
            workspace_id="workspaceId",
            telemetry_id="telemetryId",
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.stats(
            workspace_id,
            telemetry_id=telemetry_id,
            start_at=start_at,
            end_at=end_at,
            unit=unit,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data


class AsyncTelemetryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTelemetryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTelemetryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTelemetryClient
        """
        return self._raw_client

    async def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TelemetryAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TelemetryAllResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.all_(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    async def info(
        self, workspace_id: str, *, telemetry_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[TelemetryInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[TelemetryInfoResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.info(
                workspace_id="workspaceId",
                telemetry_id="telemetryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.info(
            workspace_id, telemetry_id=telemetry_id, request_options=request_options
        )
        return _response.data

    async def alleventcount(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, float]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, float]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.alleventcount(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.alleventcount(workspace_id, request_options=request_options)
        return _response.data

    async def eventcount(
        self, workspace_id: str, *, telemetry_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.eventcount(
                workspace_id="workspaceId",
                telemetry_id="telemetryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eventcount(
            workspace_id, telemetry_id=telemetry_id, request_options=request_options
        )
        return _response.data

    async def upsert(
        self,
        workspace_id: str,
        *,
        name: str,
        telemetry_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TelemetryUpsertResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        telemetry_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TelemetryUpsertResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.upsert(
                workspace_id="workspaceId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert(
            workspace_id, name=name, telemetry_id=telemetry_id, request_options=request_options
        )
        return _response.data

    async def delete(
        self, workspace_id: str, *, telemetry_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TelemetryDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TelemetryDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.delete(
                workspace_id="workspaceId",
                telemetry_id="telemetryId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            workspace_id, telemetry_id=telemetry_id, request_options=request_options
        )
        return _response.data

    async def pageviews(
        self,
        workspace_id: str,
        *,
        telemetry_id: str,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TelemetryPageviewsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TelemetryPageviewsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.pageviews(
                workspace_id="workspaceId",
                telemetry_id="telemetryId",
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pageviews(
            workspace_id,
            telemetry_id=telemetry_id,
            start_at=start_at,
            end_at=end_at,
            unit=unit,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    async def metrics(
        self,
        workspace_id: str,
        *,
        telemetry_id: str,
        type: TelemetryMetricsRequestType,
        start_at: float,
        end_at: float,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[TelemetryMetricsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        type : TelemetryMetricsRequestType

        start_at : float

        end_at : float

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TelemetryMetricsResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.metrics(
                workspace_id="workspaceId",
                telemetry_id="telemetryId",
                type="source",
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.metrics(
            workspace_id,
            telemetry_id=telemetry_id,
            type=type,
            start_at=start_at,
            end_at=end_at,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    async def stats(
        self,
        workspace_id: str,
        *,
        telemetry_id: str,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TelemetryStatsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        telemetry_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TelemetryStatsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.telemetry.stats(
                workspace_id="workspaceId",
                telemetry_id="telemetryId",
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stats(
            workspace_id,
            telemetry_id=telemetry_id,
            start_at=start_at,
            end_at=end_at,
            unit=unit,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

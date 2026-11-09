

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.aws_route import AwsRoute
from ..types.azure_route import AzureRoute
from ..types.blynk_route import BlynkRoute
from ..types.datacake_route import DatacakeRoute
from ..types.google_route import GoogleRoute
from ..types.http_route import HttpRoute
from ..types.mqtt_route import MqttRoute
from ..types.notehub_route import NotehubRoute
from ..types.notehub_route_summary import NotehubRouteSummary
from ..types.proxy_route import ProxyRoute
from ..types.qubitro_route import QubitroRoute
from ..types.rad_route import RadRoute
from ..types.route_log import RouteLog
from ..types.s3archive_route import S3ArchiveRoute
from ..types.slack_route import SlackRoute
from ..types.snowflake_route import SnowflakeRoute
from ..types.snowpipe_streaming_route import SnowpipeStreamingRoute
from ..types.thingworx_route import ThingworxRoute
from ..types.twilio_route import TwilioRoute
from .raw_client import AsyncRawRouteClient, RawRouteClient
from .types.get_route_logs_by_route_request_routing_status_item import GetRouteLogsByRouteRequestRoutingStatusItem
from .types.get_route_logs_by_route_request_sort_by import GetRouteLogsByRouteRequestSortBy
from .types.get_route_logs_by_route_request_sort_order import GetRouteLogsByRouteRequestSortOrder


OMIT = typing.cast(typing.Any, ...)


class RouteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRouteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRouteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRouteClient
        """
        return self._raw_client

    def get_routes(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotehubRouteSummary]:
        """
        Get all Routes within a Project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotehubRouteSummary]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.route.get_routes(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_routes(project_or_product_uid, request_options=request_options)
        return _response.data

    def create_route(
        self,
        project_or_product_uid: str,
        *,
        aws: typing.Optional[AwsRoute] = OMIT,
        azure: typing.Optional[AzureRoute] = OMIT,
        blynk: typing.Optional[BlynkRoute] = OMIT,
        datacake: typing.Optional[DatacakeRoute] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        google: typing.Optional[GoogleRoute] = OMIT,
        http: typing.Optional[HttpRoute] = OMIT,
        label: typing.Optional[str] = OMIT,
        modified: typing.Optional[dt.datetime] = OMIT,
        mqtt: typing.Optional[MqttRoute] = OMIT,
        notes: typing.Optional[str] = OMIT,
        proxy: typing.Optional[ProxyRoute] = OMIT,
        qubitro: typing.Optional[QubitroRoute] = OMIT,
        radnote: typing.Optional[RadRoute] = OMIT,
        s3archive: typing.Optional[S3ArchiveRoute] = OMIT,
        slack: typing.Optional[SlackRoute] = OMIT,
        snowflake: typing.Optional[SnowflakeRoute] = OMIT,
        snowpipe_streaming: typing.Optional[SnowpipeStreamingRoute] = OMIT,
        thingworx: typing.Optional[ThingworxRoute] = OMIT,
        twilio: typing.Optional[TwilioRoute] = OMIT,
        type: typing.Optional[str] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotehubRoute:
        """
        Create Route within a Project

        Parameters
        ----------
        project_or_product_uid : str

        aws : typing.Optional[AwsRoute]

        azure : typing.Optional[AzureRoute]

        blynk : typing.Optional[BlynkRoute]

        datacake : typing.Optional[DatacakeRoute]

        disabled : typing.Optional[bool]

        google : typing.Optional[GoogleRoute]

        http : typing.Optional[HttpRoute]

        label : typing.Optional[str]

        modified : typing.Optional[dt.datetime]

        mqtt : typing.Optional[MqttRoute]

        notes : typing.Optional[str]
            Optional free-form text for annotating the route.

        proxy : typing.Optional[ProxyRoute]

        qubitro : typing.Optional[QubitroRoute]

        radnote : typing.Optional[RadRoute]

        s3archive : typing.Optional[S3ArchiveRoute]

        slack : typing.Optional[SlackRoute]

        snowflake : typing.Optional[SnowflakeRoute]

        snowpipe_streaming : typing.Optional[SnowpipeStreamingRoute]

        thingworx : typing.Optional[ThingworxRoute]

        twilio : typing.Optional[TwilioRoute]

        type : typing.Optional[str]
            Mirrors hublib.RouteType.

        uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotehubRoute
            Created

        Examples
        --------
        from fern import FernApi, HttpRoute

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.route.create_route(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            http=HttpRoute(
                disable_http_headers=False,
                fleets=["fleet:1042ddc5-3b2c-4cec-b1fb-d3040538094d"],
                http_headers={"X-My-Header": "value"},
                throttle_ms=100,
                timeout=5000,
                url="https://example.com/ingest",
            ),
            label="Route Label",
        )
        """
        _response = self._raw_client.create_route(
            project_or_product_uid,
            aws=aws,
            azure=azure,
            blynk=blynk,
            datacake=datacake,
            disabled=disabled,
            google=google,
            http=http,
            label=label,
            modified=modified,
            mqtt=mqtt,
            notes=notes,
            proxy=proxy,
            qubitro=qubitro,
            radnote=radnote,
            s3archive=s3archive,
            slack=slack,
            snowflake=snowflake,
            snowpipe_streaming=snowpipe_streaming,
            thingworx=thingworx,
            twilio=twilio,
            type=type,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    def get_route(
        self, project_or_product_uid: str, route_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotehubRoute:
        """
        Get single route within a project

        Parameters
        ----------
        project_or_product_uid : str

        route_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotehubRoute
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.route.get_route(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
        )
        """
        _response = self._raw_client.get_route(project_or_product_uid, route_uid, request_options=request_options)
        return _response.data

    def update_route(
        self,
        project_or_product_uid: str,
        route_uid: str,
        *,
        aws: typing.Optional[AwsRoute] = OMIT,
        azure: typing.Optional[AzureRoute] = OMIT,
        blynk: typing.Optional[BlynkRoute] = OMIT,
        datacake: typing.Optional[DatacakeRoute] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        google: typing.Optional[GoogleRoute] = OMIT,
        http: typing.Optional[HttpRoute] = OMIT,
        label: typing.Optional[str] = OMIT,
        modified: typing.Optional[dt.datetime] = OMIT,
        mqtt: typing.Optional[MqttRoute] = OMIT,
        notes: typing.Optional[str] = OMIT,
        proxy: typing.Optional[ProxyRoute] = OMIT,
        qubitro: typing.Optional[QubitroRoute] = OMIT,
        radnote: typing.Optional[RadRoute] = OMIT,
        s3archive: typing.Optional[S3ArchiveRoute] = OMIT,
        slack: typing.Optional[SlackRoute] = OMIT,
        snowflake: typing.Optional[SnowflakeRoute] = OMIT,
        snowpipe_streaming: typing.Optional[SnowpipeStreamingRoute] = OMIT,
        thingworx: typing.Optional[ThingworxRoute] = OMIT,
        twilio: typing.Optional[TwilioRoute] = OMIT,
        type: typing.Optional[str] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotehubRoute:
        """
        Update route by UID

        Parameters
        ----------
        project_or_product_uid : str

        route_uid : str

        aws : typing.Optional[AwsRoute]

        azure : typing.Optional[AzureRoute]

        blynk : typing.Optional[BlynkRoute]

        datacake : typing.Optional[DatacakeRoute]

        disabled : typing.Optional[bool]

        google : typing.Optional[GoogleRoute]

        http : typing.Optional[HttpRoute]

        label : typing.Optional[str]

        modified : typing.Optional[dt.datetime]

        mqtt : typing.Optional[MqttRoute]

        notes : typing.Optional[str]
            Optional free-form text for annotating the route.

        proxy : typing.Optional[ProxyRoute]

        qubitro : typing.Optional[QubitroRoute]

        radnote : typing.Optional[RadRoute]

        s3archive : typing.Optional[S3ArchiveRoute]

        slack : typing.Optional[SlackRoute]

        snowflake : typing.Optional[SnowflakeRoute]

        snowpipe_streaming : typing.Optional[SnowpipeStreamingRoute]

        thingworx : typing.Optional[ThingworxRoute]

        twilio : typing.Optional[TwilioRoute]

        type : typing.Optional[str]
            Mirrors hublib.RouteType.

        uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotehubRoute
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.route.update_route(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
        )
        """
        _response = self._raw_client.update_route(
            project_or_product_uid,
            route_uid,
            aws=aws,
            azure=azure,
            blynk=blynk,
            datacake=datacake,
            disabled=disabled,
            google=google,
            http=http,
            label=label,
            modified=modified,
            mqtt=mqtt,
            notes=notes,
            proxy=proxy,
            qubitro=qubitro,
            radnote=radnote,
            s3archive=s3archive,
            slack=slack,
            snowflake=snowflake,
            snowpipe_streaming=snowpipe_streaming,
            thingworx=thingworx,
            twilio=twilio,
            type=type,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    def delete_route(
        self, project_or_product_uid: str, route_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete single route within a project

        Parameters
        ----------
        project_or_product_uid : str

        route_uid : str

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
        client.route.delete_route(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
        )
        """
        _response = self._raw_client.delete_route(project_or_product_uid, route_uid, request_options=request_options)
        return _response.data

    def get_route_logs_by_route(
        self,
        project_or_product_uid: str,
        route_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort_by: typing.Optional[GetRouteLogsByRouteRequestSortBy] = None,
        sort_order: typing.Optional[GetRouteLogsByRouteRequestSortOrder] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        system_files_only: typing.Optional[bool] = None,
        most_recent_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        routing_status: typing.Optional[
            typing.Union[
                GetRouteLogsByRouteRequestRoutingStatusItem,
                typing.Sequence[GetRouteLogsByRouteRequestRoutingStatusItem],
            ]
        ] = None,
        response_status: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RouteLog]:
        """
        Get Route Logs by Route UID

        Parameters
        ----------
        project_or_product_uid : str

        route_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sort_by : typing.Optional[GetRouteLogsByRouteRequestSortBy]

        sort_order : typing.Optional[GetRouteLogsByRouteRequestSortOrder]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        system_files_only : typing.Optional[bool]

        most_recent_only : typing.Optional[bool]

        files : typing.Optional[str]

        routing_status : typing.Optional[typing.Union[GetRouteLogsByRouteRequestRoutingStatusItem, typing.Sequence[GetRouteLogsByRouteRequestRoutingStatusItem]]]

        response_status : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RouteLog]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.route.get_route_logs_by_route(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
            files="_health.qo, data.qo",
        )
        """
        _response = self._raw_client.get_route_logs_by_route(
            project_or_product_uid,
            route_uid,
            page_size=page_size,
            page_num=page_num,
            device_uid=device_uid,
            sort_by=sort_by,
            sort_order=sort_order,
            start_date=start_date,
            end_date=end_date,
            system_files_only=system_files_only,
            most_recent_only=most_recent_only,
            files=files,
            routing_status=routing_status,
            response_status=response_status,
            request_options=request_options,
        )
        return _response.data


class AsyncRouteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRouteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRouteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRouteClient
        """
        return self._raw_client

    async def get_routes(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotehubRouteSummary]:
        """
        Get all Routes within a Project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotehubRouteSummary]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.route.get_routes(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_routes(project_or_product_uid, request_options=request_options)
        return _response.data

    async def create_route(
        self,
        project_or_product_uid: str,
        *,
        aws: typing.Optional[AwsRoute] = OMIT,
        azure: typing.Optional[AzureRoute] = OMIT,
        blynk: typing.Optional[BlynkRoute] = OMIT,
        datacake: typing.Optional[DatacakeRoute] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        google: typing.Optional[GoogleRoute] = OMIT,
        http: typing.Optional[HttpRoute] = OMIT,
        label: typing.Optional[str] = OMIT,
        modified: typing.Optional[dt.datetime] = OMIT,
        mqtt: typing.Optional[MqttRoute] = OMIT,
        notes: typing.Optional[str] = OMIT,
        proxy: typing.Optional[ProxyRoute] = OMIT,
        qubitro: typing.Optional[QubitroRoute] = OMIT,
        radnote: typing.Optional[RadRoute] = OMIT,
        s3archive: typing.Optional[S3ArchiveRoute] = OMIT,
        slack: typing.Optional[SlackRoute] = OMIT,
        snowflake: typing.Optional[SnowflakeRoute] = OMIT,
        snowpipe_streaming: typing.Optional[SnowpipeStreamingRoute] = OMIT,
        thingworx: typing.Optional[ThingworxRoute] = OMIT,
        twilio: typing.Optional[TwilioRoute] = OMIT,
        type: typing.Optional[str] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotehubRoute:
        """
        Create Route within a Project

        Parameters
        ----------
        project_or_product_uid : str

        aws : typing.Optional[AwsRoute]

        azure : typing.Optional[AzureRoute]

        blynk : typing.Optional[BlynkRoute]

        datacake : typing.Optional[DatacakeRoute]

        disabled : typing.Optional[bool]

        google : typing.Optional[GoogleRoute]

        http : typing.Optional[HttpRoute]

        label : typing.Optional[str]

        modified : typing.Optional[dt.datetime]

        mqtt : typing.Optional[MqttRoute]

        notes : typing.Optional[str]
            Optional free-form text for annotating the route.

        proxy : typing.Optional[ProxyRoute]

        qubitro : typing.Optional[QubitroRoute]

        radnote : typing.Optional[RadRoute]

        s3archive : typing.Optional[S3ArchiveRoute]

        slack : typing.Optional[SlackRoute]

        snowflake : typing.Optional[SnowflakeRoute]

        snowpipe_streaming : typing.Optional[SnowpipeStreamingRoute]

        thingworx : typing.Optional[ThingworxRoute]

        twilio : typing.Optional[TwilioRoute]

        type : typing.Optional[str]
            Mirrors hublib.RouteType.

        uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotehubRoute
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, HttpRoute

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.route.create_route(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                http=HttpRoute(
                    disable_http_headers=False,
                    fleets=["fleet:1042ddc5-3b2c-4cec-b1fb-d3040538094d"],
                    http_headers={"X-My-Header": "value"},
                    throttle_ms=100,
                    timeout=5000,
                    url="https://example.com/ingest",
                ),
                label="Route Label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_route(
            project_or_product_uid,
            aws=aws,
            azure=azure,
            blynk=blynk,
            datacake=datacake,
            disabled=disabled,
            google=google,
            http=http,
            label=label,
            modified=modified,
            mqtt=mqtt,
            notes=notes,
            proxy=proxy,
            qubitro=qubitro,
            radnote=radnote,
            s3archive=s3archive,
            slack=slack,
            snowflake=snowflake,
            snowpipe_streaming=snowpipe_streaming,
            thingworx=thingworx,
            twilio=twilio,
            type=type,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    async def get_route(
        self, project_or_product_uid: str, route_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotehubRoute:
        """
        Get single route within a project

        Parameters
        ----------
        project_or_product_uid : str

        route_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotehubRoute
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.route.get_route(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_route(project_or_product_uid, route_uid, request_options=request_options)
        return _response.data

    async def update_route(
        self,
        project_or_product_uid: str,
        route_uid: str,
        *,
        aws: typing.Optional[AwsRoute] = OMIT,
        azure: typing.Optional[AzureRoute] = OMIT,
        blynk: typing.Optional[BlynkRoute] = OMIT,
        datacake: typing.Optional[DatacakeRoute] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        google: typing.Optional[GoogleRoute] = OMIT,
        http: typing.Optional[HttpRoute] = OMIT,
        label: typing.Optional[str] = OMIT,
        modified: typing.Optional[dt.datetime] = OMIT,
        mqtt: typing.Optional[MqttRoute] = OMIT,
        notes: typing.Optional[str] = OMIT,
        proxy: typing.Optional[ProxyRoute] = OMIT,
        qubitro: typing.Optional[QubitroRoute] = OMIT,
        radnote: typing.Optional[RadRoute] = OMIT,
        s3archive: typing.Optional[S3ArchiveRoute] = OMIT,
        slack: typing.Optional[SlackRoute] = OMIT,
        snowflake: typing.Optional[SnowflakeRoute] = OMIT,
        snowpipe_streaming: typing.Optional[SnowpipeStreamingRoute] = OMIT,
        thingworx: typing.Optional[ThingworxRoute] = OMIT,
        twilio: typing.Optional[TwilioRoute] = OMIT,
        type: typing.Optional[str] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotehubRoute:
        """
        Update route by UID

        Parameters
        ----------
        project_or_product_uid : str

        route_uid : str

        aws : typing.Optional[AwsRoute]

        azure : typing.Optional[AzureRoute]

        blynk : typing.Optional[BlynkRoute]

        datacake : typing.Optional[DatacakeRoute]

        disabled : typing.Optional[bool]

        google : typing.Optional[GoogleRoute]

        http : typing.Optional[HttpRoute]

        label : typing.Optional[str]

        modified : typing.Optional[dt.datetime]

        mqtt : typing.Optional[MqttRoute]

        notes : typing.Optional[str]
            Optional free-form text for annotating the route.

        proxy : typing.Optional[ProxyRoute]

        qubitro : typing.Optional[QubitroRoute]

        radnote : typing.Optional[RadRoute]

        s3archive : typing.Optional[S3ArchiveRoute]

        slack : typing.Optional[SlackRoute]

        snowflake : typing.Optional[SnowflakeRoute]

        snowpipe_streaming : typing.Optional[SnowpipeStreamingRoute]

        thingworx : typing.Optional[ThingworxRoute]

        twilio : typing.Optional[TwilioRoute]

        type : typing.Optional[str]
            Mirrors hublib.RouteType.

        uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotehubRoute
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.route.update_route(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_route(
            project_or_product_uid,
            route_uid,
            aws=aws,
            azure=azure,
            blynk=blynk,
            datacake=datacake,
            disabled=disabled,
            google=google,
            http=http,
            label=label,
            modified=modified,
            mqtt=mqtt,
            notes=notes,
            proxy=proxy,
            qubitro=qubitro,
            radnote=radnote,
            s3archive=s3archive,
            slack=slack,
            snowflake=snowflake,
            snowpipe_streaming=snowpipe_streaming,
            thingworx=thingworx,
            twilio=twilio,
            type=type,
            uid=uid,
            request_options=request_options,
        )
        return _response.data

    async def delete_route(
        self, project_or_product_uid: str, route_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete single route within a project

        Parameters
        ----------
        project_or_product_uid : str

        route_uid : str

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
            await client.route.delete_route(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_route(
            project_or_product_uid, route_uid, request_options=request_options
        )
        return _response.data

    async def get_route_logs_by_route(
        self,
        project_or_product_uid: str,
        route_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort_by: typing.Optional[GetRouteLogsByRouteRequestSortBy] = None,
        sort_order: typing.Optional[GetRouteLogsByRouteRequestSortOrder] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        system_files_only: typing.Optional[bool] = None,
        most_recent_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        routing_status: typing.Optional[
            typing.Union[
                GetRouteLogsByRouteRequestRoutingStatusItem,
                typing.Sequence[GetRouteLogsByRouteRequestRoutingStatusItem],
            ]
        ] = None,
        response_status: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RouteLog]:
        """
        Get Route Logs by Route UID

        Parameters
        ----------
        project_or_product_uid : str

        route_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sort_by : typing.Optional[GetRouteLogsByRouteRequestSortBy]

        sort_order : typing.Optional[GetRouteLogsByRouteRequestSortOrder]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        system_files_only : typing.Optional[bool]

        most_recent_only : typing.Optional[bool]

        files : typing.Optional[str]

        routing_status : typing.Optional[typing.Union[GetRouteLogsByRouteRequestRoutingStatusItem, typing.Sequence[GetRouteLogsByRouteRequestRoutingStatusItem]]]

        response_status : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RouteLog]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.route.get_route_logs_by_route(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                route_uid="route:cbd20093cba58392c9f9bbdd0cdeb1a0",
                files="_health.qo, data.qo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_route_logs_by_route(
            project_or_product_uid,
            route_uid,
            page_size=page_size,
            page_num=page_num,
            device_uid=device_uid,
            sort_by=sort_by,
            sort_order=sort_order,
            start_date=start_date,
            end_date=end_date,
            system_files_only=system_files_only,
            most_recent_only=most_recent_only,
            files=files,
            routing_status=routing_status,
            response_status=response_status,
            request_options=request_options,
        )
        return _response.data

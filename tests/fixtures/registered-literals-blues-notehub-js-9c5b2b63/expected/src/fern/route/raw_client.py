

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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
from .types.get_route_logs_by_route_request_routing_status_item import GetRouteLogsByRouteRequestRoutingStatusItem
from .types.get_route_logs_by_route_request_sort_by import GetRouteLogsByRouteRequestSortBy
from .types.get_route_logs_by_route_request_sort_order import GetRouteLogsByRouteRequestSortOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRouteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_routes(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[NotehubRouteSummary]]:
        """
        Get all Routes within a Project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[NotehubRouteSummary]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotehubRouteSummary],
                    parse_obj_as(
                        type_=typing.List[NotehubRouteSummary],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NotehubRoute]:
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
        HttpResponse[NotehubRoute]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes",
            method="POST",
            json={
                "aws": convert_and_respect_annotation_metadata(object_=aws, annotation=AwsRoute, direction="write"),
                "azure": convert_and_respect_annotation_metadata(
                    object_=azure, annotation=AzureRoute, direction="write"
                ),
                "blynk": convert_and_respect_annotation_metadata(
                    object_=blynk, annotation=BlynkRoute, direction="write"
                ),
                "datacake": convert_and_respect_annotation_metadata(
                    object_=datacake, annotation=DatacakeRoute, direction="write"
                ),
                "disabled": disabled,
                "google": convert_and_respect_annotation_metadata(
                    object_=google, annotation=GoogleRoute, direction="write"
                ),
                "http": convert_and_respect_annotation_metadata(object_=http, annotation=HttpRoute, direction="write"),
                "label": label,
                "modified": modified,
                "mqtt": convert_and_respect_annotation_metadata(object_=mqtt, annotation=MqttRoute, direction="write"),
                "notes": notes,
                "proxy": convert_and_respect_annotation_metadata(
                    object_=proxy, annotation=ProxyRoute, direction="write"
                ),
                "qubitro": convert_and_respect_annotation_metadata(
                    object_=qubitro, annotation=QubitroRoute, direction="write"
                ),
                "radnote": convert_and_respect_annotation_metadata(
                    object_=radnote, annotation=RadRoute, direction="write"
                ),
                "s3archive": convert_and_respect_annotation_metadata(
                    object_=s3archive, annotation=S3ArchiveRoute, direction="write"
                ),
                "slack": convert_and_respect_annotation_metadata(
                    object_=slack, annotation=SlackRoute, direction="write"
                ),
                "snowflake": convert_and_respect_annotation_metadata(
                    object_=snowflake, annotation=SnowflakeRoute, direction="write"
                ),
                "snowpipe_streaming": convert_and_respect_annotation_metadata(
                    object_=snowpipe_streaming, annotation=SnowpipeStreamingRoute, direction="write"
                ),
                "thingworx": convert_and_respect_annotation_metadata(
                    object_=thingworx, annotation=ThingworxRoute, direction="write"
                ),
                "twilio": convert_and_respect_annotation_metadata(
                    object_=twilio, annotation=TwilioRoute, direction="write"
                ),
                "type": type,
                "uid": uid,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotehubRoute,
                    parse_obj_as(
                        type_=NotehubRoute,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_route(
        self, project_or_product_uid: str, route_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NotehubRoute]:
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
        HttpResponse[NotehubRoute]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes/{encode_path_param(route_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotehubRoute,
                    parse_obj_as(
                        type_=NotehubRoute,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[NotehubRoute]:
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
        HttpResponse[NotehubRoute]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes/{encode_path_param(route_uid)}",
            method="PUT",
            json={
                "aws": convert_and_respect_annotation_metadata(object_=aws, annotation=AwsRoute, direction="write"),
                "azure": convert_and_respect_annotation_metadata(
                    object_=azure, annotation=AzureRoute, direction="write"
                ),
                "blynk": convert_and_respect_annotation_metadata(
                    object_=blynk, annotation=BlynkRoute, direction="write"
                ),
                "datacake": convert_and_respect_annotation_metadata(
                    object_=datacake, annotation=DatacakeRoute, direction="write"
                ),
                "disabled": disabled,
                "google": convert_and_respect_annotation_metadata(
                    object_=google, annotation=GoogleRoute, direction="write"
                ),
                "http": convert_and_respect_annotation_metadata(object_=http, annotation=HttpRoute, direction="write"),
                "label": label,
                "modified": modified,
                "mqtt": convert_and_respect_annotation_metadata(object_=mqtt, annotation=MqttRoute, direction="write"),
                "notes": notes,
                "proxy": convert_and_respect_annotation_metadata(
                    object_=proxy, annotation=ProxyRoute, direction="write"
                ),
                "qubitro": convert_and_respect_annotation_metadata(
                    object_=qubitro, annotation=QubitroRoute, direction="write"
                ),
                "radnote": convert_and_respect_annotation_metadata(
                    object_=radnote, annotation=RadRoute, direction="write"
                ),
                "s3archive": convert_and_respect_annotation_metadata(
                    object_=s3archive, annotation=S3ArchiveRoute, direction="write"
                ),
                "slack": convert_and_respect_annotation_metadata(
                    object_=slack, annotation=SlackRoute, direction="write"
                ),
                "snowflake": convert_and_respect_annotation_metadata(
                    object_=snowflake, annotation=SnowflakeRoute, direction="write"
                ),
                "snowpipe_streaming": convert_and_respect_annotation_metadata(
                    object_=snowpipe_streaming, annotation=SnowpipeStreamingRoute, direction="write"
                ),
                "thingworx": convert_and_respect_annotation_metadata(
                    object_=thingworx, annotation=ThingworxRoute, direction="write"
                ),
                "twilio": convert_and_respect_annotation_metadata(
                    object_=twilio, annotation=TwilioRoute, direction="write"
                ),
                "type": type,
                "uid": uid,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotehubRoute,
                    parse_obj_as(
                        type_=NotehubRoute,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_route(
        self, project_or_product_uid: str, route_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes/{encode_path_param(route_uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.List[RouteLog]]:
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
        HttpResponse[typing.List[RouteLog]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes/{encode_path_param(route_uid)}/route-logs",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "deviceUID": device_uid,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "startDate": start_date,
                "endDate": end_date,
                "systemFilesOnly": system_files_only,
                "mostRecentOnly": most_recent_only,
                "files": files,
                "routingStatus": routing_status,
                "responseStatus": response_status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RouteLog],
                    parse_obj_as(
                        type_=typing.List[RouteLog],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawRouteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_routes(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[NotehubRouteSummary]]:
        """
        Get all Routes within a Project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[NotehubRouteSummary]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotehubRouteSummary],
                    parse_obj_as(
                        type_=typing.List[NotehubRouteSummary],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NotehubRoute]:
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
        AsyncHttpResponse[NotehubRoute]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes",
            method="POST",
            json={
                "aws": convert_and_respect_annotation_metadata(object_=aws, annotation=AwsRoute, direction="write"),
                "azure": convert_and_respect_annotation_metadata(
                    object_=azure, annotation=AzureRoute, direction="write"
                ),
                "blynk": convert_and_respect_annotation_metadata(
                    object_=blynk, annotation=BlynkRoute, direction="write"
                ),
                "datacake": convert_and_respect_annotation_metadata(
                    object_=datacake, annotation=DatacakeRoute, direction="write"
                ),
                "disabled": disabled,
                "google": convert_and_respect_annotation_metadata(
                    object_=google, annotation=GoogleRoute, direction="write"
                ),
                "http": convert_and_respect_annotation_metadata(object_=http, annotation=HttpRoute, direction="write"),
                "label": label,
                "modified": modified,
                "mqtt": convert_and_respect_annotation_metadata(object_=mqtt, annotation=MqttRoute, direction="write"),
                "notes": notes,
                "proxy": convert_and_respect_annotation_metadata(
                    object_=proxy, annotation=ProxyRoute, direction="write"
                ),
                "qubitro": convert_and_respect_annotation_metadata(
                    object_=qubitro, annotation=QubitroRoute, direction="write"
                ),
                "radnote": convert_and_respect_annotation_metadata(
                    object_=radnote, annotation=RadRoute, direction="write"
                ),
                "s3archive": convert_and_respect_annotation_metadata(
                    object_=s3archive, annotation=S3ArchiveRoute, direction="write"
                ),
                "slack": convert_and_respect_annotation_metadata(
                    object_=slack, annotation=SlackRoute, direction="write"
                ),
                "snowflake": convert_and_respect_annotation_metadata(
                    object_=snowflake, annotation=SnowflakeRoute, direction="write"
                ),
                "snowpipe_streaming": convert_and_respect_annotation_metadata(
                    object_=snowpipe_streaming, annotation=SnowpipeStreamingRoute, direction="write"
                ),
                "thingworx": convert_and_respect_annotation_metadata(
                    object_=thingworx, annotation=ThingworxRoute, direction="write"
                ),
                "twilio": convert_and_respect_annotation_metadata(
                    object_=twilio, annotation=TwilioRoute, direction="write"
                ),
                "type": type,
                "uid": uid,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotehubRoute,
                    parse_obj_as(
                        type_=NotehubRoute,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_route(
        self, project_or_product_uid: str, route_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NotehubRoute]:
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
        AsyncHttpResponse[NotehubRoute]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes/{encode_path_param(route_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotehubRoute,
                    parse_obj_as(
                        type_=NotehubRoute,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[NotehubRoute]:
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
        AsyncHttpResponse[NotehubRoute]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes/{encode_path_param(route_uid)}",
            method="PUT",
            json={
                "aws": convert_and_respect_annotation_metadata(object_=aws, annotation=AwsRoute, direction="write"),
                "azure": convert_and_respect_annotation_metadata(
                    object_=azure, annotation=AzureRoute, direction="write"
                ),
                "blynk": convert_and_respect_annotation_metadata(
                    object_=blynk, annotation=BlynkRoute, direction="write"
                ),
                "datacake": convert_and_respect_annotation_metadata(
                    object_=datacake, annotation=DatacakeRoute, direction="write"
                ),
                "disabled": disabled,
                "google": convert_and_respect_annotation_metadata(
                    object_=google, annotation=GoogleRoute, direction="write"
                ),
                "http": convert_and_respect_annotation_metadata(object_=http, annotation=HttpRoute, direction="write"),
                "label": label,
                "modified": modified,
                "mqtt": convert_and_respect_annotation_metadata(object_=mqtt, annotation=MqttRoute, direction="write"),
                "notes": notes,
                "proxy": convert_and_respect_annotation_metadata(
                    object_=proxy, annotation=ProxyRoute, direction="write"
                ),
                "qubitro": convert_and_respect_annotation_metadata(
                    object_=qubitro, annotation=QubitroRoute, direction="write"
                ),
                "radnote": convert_and_respect_annotation_metadata(
                    object_=radnote, annotation=RadRoute, direction="write"
                ),
                "s3archive": convert_and_respect_annotation_metadata(
                    object_=s3archive, annotation=S3ArchiveRoute, direction="write"
                ),
                "slack": convert_and_respect_annotation_metadata(
                    object_=slack, annotation=SlackRoute, direction="write"
                ),
                "snowflake": convert_and_respect_annotation_metadata(
                    object_=snowflake, annotation=SnowflakeRoute, direction="write"
                ),
                "snowpipe_streaming": convert_and_respect_annotation_metadata(
                    object_=snowpipe_streaming, annotation=SnowpipeStreamingRoute, direction="write"
                ),
                "thingworx": convert_and_respect_annotation_metadata(
                    object_=thingworx, annotation=ThingworxRoute, direction="write"
                ),
                "twilio": convert_and_respect_annotation_metadata(
                    object_=twilio, annotation=TwilioRoute, direction="write"
                ),
                "type": type,
                "uid": uid,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotehubRoute,
                    parse_obj_as(
                        type_=NotehubRoute,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_route(
        self, project_or_product_uid: str, route_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes/{encode_path_param(route_uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.List[RouteLog]]:
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
        AsyncHttpResponse[typing.List[RouteLog]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/routes/{encode_path_param(route_uid)}/route-logs",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "deviceUID": device_uid,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "startDate": start_date,
                "endDate": end_date,
                "systemFilesOnly": system_files_only,
                "mostRecentOnly": most_recent_only,
                "files": files,
                "routingStatus": routing_status,
                "responseStatus": response_status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RouteLog],
                    parse_obj_as(
                        type_=typing.List[RouteLog],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

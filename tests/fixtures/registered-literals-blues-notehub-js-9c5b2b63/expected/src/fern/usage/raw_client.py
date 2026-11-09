

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.usage_events_response import UsageEventsResponse
from .types.get_data_usage_request_aggregate import GetDataUsageRequestAggregate
from .types.get_data_usage_request_period import GetDataUsageRequestPeriod
from .types.get_data_usage_response import GetDataUsageResponse
from .types.get_events_usage_request_aggregate import GetEventsUsageRequestAggregate
from .types.get_events_usage_request_period import GetEventsUsageRequestPeriod
from .types.get_route_logs_usage_request_aggregate import GetRouteLogsUsageRequestAggregate
from .types.get_route_logs_usage_request_period import GetRouteLogsUsageRequestPeriod
from .types.get_route_logs_usage_response import GetRouteLogsUsageResponse
from .types.get_sessions_usage_request_aggregate import GetSessionsUsageRequestAggregate
from .types.get_sessions_usage_request_period import GetSessionsUsageRequestPeriod
from .types.get_sessions_usage_response import GetSessionsUsageResponse
from pydantic import ValidationError


class RawUsageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_data_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetDataUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetDataUsageRequestAggregate] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDataUsageResponse]:
        """
        Get data usage in bytes for a project with time range and period aggregation

        Parameters
        ----------
        project_or_product_uid : str

        period : GetDataUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetDataUsageRequestAggregate]
            Aggregation level for results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDataUsageResponse]
            Response body for Data Usage
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/usage/data",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "deviceUID": device_uid,
                "fleetUID": fleet_uid,
                "limit": limit,
                "period": period,
                "aggregate": aggregate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDataUsageResponse,
                    parse_obj_as(
                        type_=GetDataUsageResponse,
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

    def get_events_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetEventsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetEventsUsageRequestAggregate] = None,
        notefile: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        skip_recent_data: typing.Optional[bool] = None,
        include_notefiles: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsageEventsResponse]:
        """
        Get events usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetEventsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetEventsUsageRequestAggregate]
            Aggregation level for results

        notefile : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter to specific notefiles

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        include_notefiles : typing.Optional[bool]
            Include per-notefile event counts in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsageEventsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/usage/events",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "deviceUID": device_uid,
                "fleetUID": fleet_uid,
                "limit": limit,
                "period": period,
                "aggregate": aggregate,
                "notefile": notefile,
                "skipRecentData": skip_recent_data,
                "includeNotefiles": include_notefiles,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsageEventsResponse,
                    parse_obj_as(
                        type_=UsageEventsResponse,
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

    def get_route_logs_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetRouteLogsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        route_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetRouteLogsUsageRequestAggregate] = None,
        skip_recent_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetRouteLogsUsageResponse]:
        """
        Get route logs usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetRouteLogsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        route_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Route UID.

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetRouteLogsUsageRequestAggregate]
            Aggregation level for results

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRouteLogsUsageResponse]
            Response body for Route Log Usage
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/usage/route-logs",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "routeUID": route_uid,
                "limit": limit,
                "period": period,
                "aggregate": aggregate,
                "skipRecentData": skip_recent_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRouteLogsUsageResponse,
                    parse_obj_as(
                        type_=GetRouteLogsUsageResponse,
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

    def get_sessions_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetSessionsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetSessionsUsageRequestAggregate] = None,
        skip_recent_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSessionsUsageResponse]:
        """
        Get sessions usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetSessionsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetSessionsUsageRequestAggregate]
            Aggregation level for results

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSessionsUsageResponse]
            Response body for Session Usage
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/usage/sessions",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "deviceUID": device_uid,
                "fleetUID": fleet_uid,
                "limit": limit,
                "period": period,
                "aggregate": aggregate,
                "skipRecentData": skip_recent_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSessionsUsageResponse,
                    parse_obj_as(
                        type_=GetSessionsUsageResponse,
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


class AsyncRawUsageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_data_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetDataUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetDataUsageRequestAggregate] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDataUsageResponse]:
        """
        Get data usage in bytes for a project with time range and period aggregation

        Parameters
        ----------
        project_or_product_uid : str

        period : GetDataUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetDataUsageRequestAggregate]
            Aggregation level for results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDataUsageResponse]
            Response body for Data Usage
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/usage/data",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "deviceUID": device_uid,
                "fleetUID": fleet_uid,
                "limit": limit,
                "period": period,
                "aggregate": aggregate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDataUsageResponse,
                    parse_obj_as(
                        type_=GetDataUsageResponse,
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

    async def get_events_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetEventsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetEventsUsageRequestAggregate] = None,
        notefile: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        skip_recent_data: typing.Optional[bool] = None,
        include_notefiles: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsageEventsResponse]:
        """
        Get events usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetEventsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetEventsUsageRequestAggregate]
            Aggregation level for results

        notefile : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter to specific notefiles

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        include_notefiles : typing.Optional[bool]
            Include per-notefile event counts in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsageEventsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/usage/events",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "deviceUID": device_uid,
                "fleetUID": fleet_uid,
                "limit": limit,
                "period": period,
                "aggregate": aggregate,
                "notefile": notefile,
                "skipRecentData": skip_recent_data,
                "includeNotefiles": include_notefiles,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsageEventsResponse,
                    parse_obj_as(
                        type_=UsageEventsResponse,
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

    async def get_route_logs_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetRouteLogsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        route_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetRouteLogsUsageRequestAggregate] = None,
        skip_recent_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetRouteLogsUsageResponse]:
        """
        Get route logs usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetRouteLogsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        route_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Route UID.

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetRouteLogsUsageRequestAggregate]
            Aggregation level for results

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRouteLogsUsageResponse]
            Response body for Route Log Usage
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/usage/route-logs",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "routeUID": route_uid,
                "limit": limit,
                "period": period,
                "aggregate": aggregate,
                "skipRecentData": skip_recent_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRouteLogsUsageResponse,
                    parse_obj_as(
                        type_=GetRouteLogsUsageResponse,
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

    async def get_sessions_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetSessionsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetSessionsUsageRequestAggregate] = None,
        skip_recent_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetSessionsUsageResponse]:
        """
        Get sessions usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetSessionsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetSessionsUsageRequestAggregate]
            Aggregation level for results

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSessionsUsageResponse]
            Response body for Session Usage
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/usage/sessions",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "deviceUID": device_uid,
                "fleetUID": fleet_uid,
                "limit": limit,
                "period": period,
                "aggregate": aggregate,
                "skipRecentData": skip_recent_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSessionsUsageResponse,
                    parse_obj_as(
                        type_=GetSessionsUsageResponse,
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

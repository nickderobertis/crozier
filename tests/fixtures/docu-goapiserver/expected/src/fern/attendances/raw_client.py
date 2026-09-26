

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from .types.get_attendances_v3request_fields_item import GetAttendancesV3RequestFieldsItem
from .types.get_attendances_v3request_group_by import GetAttendancesV3RequestGroupBy
from .types.get_attendances_v3request_metrics_item import GetAttendancesV3RequestMetricsItem
from .types.get_attendances_v3request_sort_by import GetAttendancesV3RequestSortBy
from .types.get_attendances_v3response import GetAttendancesV3Response
from pydantic import ValidationError


class RawAttendancesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_attendances_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        room_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        room_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        student_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        student_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        min_hours: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetAttendancesV3RequestFieldsItem, typing.Sequence[GetAttendancesV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[GetAttendancesV3RequestSortBy] = None,
        group_by: typing.Optional[GetAttendancesV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetAttendancesV3RequestMetricsItem, typing.Sequence[GetAttendancesV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAttendancesV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide date_from AND date_to, or a positive last_n_days; mixing them returns 400. Defaults min_hours to 2; records below that threshold are excluded. room_id/room_ids and student_id/student_ids are merged. Row responses are sparse Attendance objects and support fields and pagination; sort_by on rows returns 400. group_by plus metrics selects nested AttendanceAggregate rows with a limit instead of pagination. Room/student filter counts, when positive, are returned in headers.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        room_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with room_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        room_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional room UUIDs; combined with room_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        student_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with student_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        student_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional student UUIDs; combined with student_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.

        last_n_days : typing.Optional[int]
            Positive rolling-window length; cannot be combined with either explicit date bound.

        min_hours : typing.Optional[float]
            Minimum hours attended per record. Use zero to include records below the historical two-hour threshold.

        fields : typing.Optional[typing.Union[GetAttendancesV3RequestFieldsItem, typing.Sequence[GetAttendancesV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: student_id, date, room_id, room_name, hours_attended. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[GetAttendancesV3RequestSortBy]
            Aggregate view only; sending sort_by without group_by returns 400. Default group_asc.

        group_by : typing.Optional[GetAttendancesV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetAttendancesV3RequestMetricsItem, typing.Sequence[GetAttendancesV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.

        page : typing.Optional[int]
            One-based page number. Row view only.

        per_page : typing.Optional[int]
            Items per page; values greater than 200 are clamped to 200. Row view only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAttendancesV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "attendances",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "room_id": room_id,
                "room_ids": room_ids,
                "student_id": student_id,
                "student_ids": student_ids,
                "date_from": str(date_from) if date_from is not None else None,
                "date_to": str(date_to) if date_to is not None else None,
                "last_n_days": last_n_days,
                "min_hours": min_hours,
                "fields": fields,
                "sort_by": sort_by,
                "group_by": group_by,
                "metrics": metrics,
                "limit": limit,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAttendancesV3Response,
                    parse_obj_as(
                        type_=GetAttendancesV3Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAttendancesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_attendances_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        room_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        room_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        student_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        student_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        min_hours: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetAttendancesV3RequestFieldsItem, typing.Sequence[GetAttendancesV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[GetAttendancesV3RequestSortBy] = None,
        group_by: typing.Optional[GetAttendancesV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetAttendancesV3RequestMetricsItem, typing.Sequence[GetAttendancesV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAttendancesV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide date_from AND date_to, or a positive last_n_days; mixing them returns 400. Defaults min_hours to 2; records below that threshold are excluded. room_id/room_ids and student_id/student_ids are merged. Row responses are sparse Attendance objects and support fields and pagination; sort_by on rows returns 400. group_by plus metrics selects nested AttendanceAggregate rows with a limit instead of pagination. Room/student filter counts, when positive, are returned in headers.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        room_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with room_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        room_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional room UUIDs; combined with room_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        student_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with student_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        student_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional student UUIDs; combined with student_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.

        last_n_days : typing.Optional[int]
            Positive rolling-window length; cannot be combined with either explicit date bound.

        min_hours : typing.Optional[float]
            Minimum hours attended per record. Use zero to include records below the historical two-hour threshold.

        fields : typing.Optional[typing.Union[GetAttendancesV3RequestFieldsItem, typing.Sequence[GetAttendancesV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: student_id, date, room_id, room_name, hours_attended. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[GetAttendancesV3RequestSortBy]
            Aggregate view only; sending sort_by without group_by returns 400. Default group_asc.

        group_by : typing.Optional[GetAttendancesV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetAttendancesV3RequestMetricsItem, typing.Sequence[GetAttendancesV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.

        page : typing.Optional[int]
            One-based page number. Row view only.

        per_page : typing.Optional[int]
            Items per page; values greater than 200 are clamped to 200. Row view only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAttendancesV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "attendances",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "room_id": room_id,
                "room_ids": room_ids,
                "student_id": student_id,
                "student_ids": student_ids,
                "date_from": str(date_from) if date_from is not None else None,
                "date_to": str(date_to) if date_to is not None else None,
                "last_n_days": last_n_days,
                "min_hours": min_hours,
                "fields": fields,
                "sort_by": sort_by,
                "group_by": group_by,
                "metrics": metrics,
                "limit": limit,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAttendancesV3Response,
                    parse_obj_as(
                        type_=GetAttendancesV3Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)



import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.closed_space_cell import ClosedSpaceCell
from ..types.error import Error
from ..types.spaces_snapshot import SpacesSnapshot
from ..types.update_closed_spaces_response import UpdateClosedSpacesResponse
from .types.get_spaces_detailed_list_v3request_fields_item import GetSpacesDetailedListV3RequestFieldsItem
from .types.get_spaces_detailed_list_v3request_group_by import GetSpacesDetailedListV3RequestGroupBy
from .types.get_spaces_detailed_list_v3request_metrics_item import GetSpacesDetailedListV3RequestMetricsItem
from .types.get_spaces_detailed_list_v3request_view import GetSpacesDetailedListV3RequestView
from .types.get_spaces_detailed_list_v3response import GetSpacesDetailedListV3Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSpacesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_spaces_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SpacesSnapshot]:
        """
        Requires schools assigned to the session. Only company_id and optional school_id are accepted; all other parameters return 400. With school_id, the school must be assigned to the session and its name selects the snapshot entry. Without school_id, the current implementation matches session school entries directly against the snapshot keys, which are school names; UUID-based assignments can therefore yield an empty map. Returns a nested map without pagination or collection headers.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SpacesSnapshot]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "spaces",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpacesSnapshot,
                    parse_obj_as(
                        type_=SpacesSnapshot,
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

    def get_spaces_detailed_list_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        view: typing.Optional[GetSpacesDetailedListV3RequestView] = None,
        period: typing.Optional[str] = None,
        room_id: typing.Optional[str] = None,
        room_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        only_active: typing.Optional[bool] = None,
        period_from: typing.Optional[str] = None,
        period_to: typing.Optional[str] = None,
        fields: typing.Optional[
            typing.Union[
                GetSpacesDetailedListV3RequestFieldsItem, typing.Sequence[GetSpacesDetailedListV3RequestFieldsItem]
            ]
        ] = None,
        sort_by: typing.Optional[str] = None,
        group_by: typing.Optional[GetSpacesDetailedListV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[
                GetSpacesDetailedListV3RequestMetricsItem, typing.Sequence[GetSpacesDetailedListV3RequestMetricsItem]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSpacesDetailedListV3Response]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. The selected representation determines accepted parameters; every unsupported parameter returns 400.

        | Representation | Selection | Required scope and dates | Additional parameters |
        | --- | --- | --- | --- |
        | Rows | Omit view/group_by/metrics | school_id, period | room_id, room_ids, fields, sort_by, page, per_page |
        | Aggregate | Omit view; set group_by and metrics | school_id, period | room_ids, sort_by, limit |
        | Trend | view=trend | school_id, room_id | period_from, period_to, fields |
        | Projection | view=projection | school_id | room_id, room_ids, period_from, period_to, fields |
        | Periods | view=periods | Session schools | school_ids, only_active |

        All modes accept company_id and view. Periods rejects school_id; use school_ids instead. Rows are paginated. Aggregate returns flat properties for the grouping key and metrics, with default limit 50 and cap 200. Trend, projection and periods are unpaginated. Omitting both range bounds uses the available calculated horizon. If filtering, both bounds must be present and within that horizon. An inverted range returns 400; a single bound or an out-of-horizon range fails in the data layer and currently returns 500. Projection always returns one row per room and period. Without a room filter it includes all rooms. The default projection fields omit room_id and room_name, so request those fields to distinguish rooms. fields differs between SpacesRow (rows/trend) and SpacesProjection. occupancy_rate is a ratio (0.8 means 80%).

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        view : typing.Optional[GetSpacesDetailedListV3RequestView]
            Omit for paginated rows or aggregation selected with group_by.

        period : typing.Optional[str]
            Required for rows and aggregates; not accepted in the other views.

        room_id : typing.Optional[str]
            Optional for rows/projection; required for trend; rejected for aggregates and periods.

        room_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional for rows, aggregates and projection. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Periods view only; each ID must be assigned to the session. Defaults to all assigned schools. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        only_active : typing.Optional[bool]
            Periods view only: include only active schools. Accepts true/1 and false/0, case-insensitive.

        period_from : typing.Optional[str]
            Trend/projection only: optional first monthly period. Omit both bounds or provide both within the available horizon.

        period_to : typing.Optional[str]
            Trend/projection only: optional last monthly period; must not precede period_from. Omit both bounds or provide both within the available horizon.

        fields : typing.Optional[typing.Union[GetSpacesDetailedListV3RequestFieldsItem, typing.Sequence[GetSpacesDetailedListV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Rows and trend use SpacesRow fields; projection uses SpacesProjection fields. Invalid fields for the selected view return 400. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[str]
            Rows: room_name, available_spaces, open_spaces, occupied_spaces or occupancy_rate with _asc/_desc. Aggregates: sum_available_spaces, sum_open_spaces, sum_occupied_spaces, sum_closed_spaces, sum_unavailable_spaces, capacity or occupancy_rate with _asc/_desc. Other views reject sort_by. Defaults: room_name_asc for rows; sum_open_spaces_desc for aggregates.

        group_by : typing.Optional[GetSpacesDetailedListV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetSpacesDetailedListV3RequestMetricsItem, typing.Sequence[GetSpacesDetailedListV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. If provided, must be positive.

        page : typing.Optional[int]
            One-based page number. Rows only; other representations reject pagination parameters.

        per_page : typing.Optional[int]
            Items per page; values greater than 200 are clamped to 200. Rows only; other representations reject pagination parameters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSpacesDetailedListV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "spaces/detailed_list",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "view": view,
                "period": period,
                "room_id": room_id,
                "room_ids": room_ids,
                "school_ids": school_ids,
                "only_active": only_active,
                "period_from": period_from,
                "period_to": period_to,
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
                    GetSpacesDetailedListV3Response,
                    parse_obj_as(
                        type_=GetSpacesDetailedListV3Response,
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

    def patch_spaces_closed_spaces_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        closed_spaces: typing.Sequence[ClosedSpaceCell],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateClosedSpacesResponse]:
        """
        Requires an authenticated user in the Operations or Admin group, school_id assigned to the session, and room IDs belonging to that school. Each room_id/period pair must be unique in the body. closed_spaces must be nonnegative and no greater than room capacity. Positive values create/update overrides; zero removes an existing override. All cells are validated before writes. Upserts and deletes execute separately; a later failure may leave earlier changes applied. modified counts upserts plus existing rows deleted (a zero for a missing override does not increase it).

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        closed_spaces : typing.Sequence[ClosedSpaceCell]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateClosedSpacesResponse]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "spaces/closed_spaces",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json={
                "closed_spaces": convert_and_respect_annotation_metadata(
                    object_=closed_spaces, annotation=typing.Sequence[ClosedSpaceCell], direction="write"
                ),
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
                    UpdateClosedSpacesResponse,
                    parse_obj_as(
                        type_=UpdateClosedSpacesResponse,
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
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


class AsyncRawSpacesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_spaces_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SpacesSnapshot]:
        """
        Requires schools assigned to the session. Only company_id and optional school_id are accepted; all other parameters return 400. With school_id, the school must be assigned to the session and its name selects the snapshot entry. Without school_id, the current implementation matches session school entries directly against the snapshot keys, which are school names; UUID-based assignments can therefore yield an empty map. Returns a nested map without pagination or collection headers.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SpacesSnapshot]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "spaces",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpacesSnapshot,
                    parse_obj_as(
                        type_=SpacesSnapshot,
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

    async def get_spaces_detailed_list_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        view: typing.Optional[GetSpacesDetailedListV3RequestView] = None,
        period: typing.Optional[str] = None,
        room_id: typing.Optional[str] = None,
        room_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        only_active: typing.Optional[bool] = None,
        period_from: typing.Optional[str] = None,
        period_to: typing.Optional[str] = None,
        fields: typing.Optional[
            typing.Union[
                GetSpacesDetailedListV3RequestFieldsItem, typing.Sequence[GetSpacesDetailedListV3RequestFieldsItem]
            ]
        ] = None,
        sort_by: typing.Optional[str] = None,
        group_by: typing.Optional[GetSpacesDetailedListV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[
                GetSpacesDetailedListV3RequestMetricsItem, typing.Sequence[GetSpacesDetailedListV3RequestMetricsItem]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetSpacesDetailedListV3Response]:
        """
        The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. The selected representation determines accepted parameters; every unsupported parameter returns 400.

        | Representation | Selection | Required scope and dates | Additional parameters |
        | --- | --- | --- | --- |
        | Rows | Omit view/group_by/metrics | school_id, period | room_id, room_ids, fields, sort_by, page, per_page |
        | Aggregate | Omit view; set group_by and metrics | school_id, period | room_ids, sort_by, limit |
        | Trend | view=trend | school_id, room_id | period_from, period_to, fields |
        | Projection | view=projection | school_id | room_id, room_ids, period_from, period_to, fields |
        | Periods | view=periods | Session schools | school_ids, only_active |

        All modes accept company_id and view. Periods rejects school_id; use school_ids instead. Rows are paginated. Aggregate returns flat properties for the grouping key and metrics, with default limit 50 and cap 200. Trend, projection and periods are unpaginated. Omitting both range bounds uses the available calculated horizon. If filtering, both bounds must be present and within that horizon. An inverted range returns 400; a single bound or an out-of-horizon range fails in the data layer and currently returns 500. Projection always returns one row per room and period. Without a room filter it includes all rooms. The default projection fields omit room_id and room_name, so request those fields to distinguish rooms. fields differs between SpacesRow (rows/trend) and SpacesProjection. occupancy_rate is a ratio (0.8 means 80%).

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.

        view : typing.Optional[GetSpacesDetailedListV3RequestView]
            Omit for paginated rows or aggregation selected with group_by.

        period : typing.Optional[str]
            Required for rows and aggregates; not accepted in the other views.

        room_id : typing.Optional[str]
            Optional for rows/projection; required for trend; rejected for aggregates and periods.

        room_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional for rows, aggregates and projection. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Periods view only; each ID must be assigned to the session. Defaults to all assigned schools. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        only_active : typing.Optional[bool]
            Periods view only: include only active schools. Accepts true/1 and false/0, case-insensitive.

        period_from : typing.Optional[str]
            Trend/projection only: optional first monthly period. Omit both bounds or provide both within the available horizon.

        period_to : typing.Optional[str]
            Trend/projection only: optional last monthly period; must not precede period_from. Omit both bounds or provide both within the available horizon.

        fields : typing.Optional[typing.Union[GetSpacesDetailedListV3RequestFieldsItem, typing.Sequence[GetSpacesDetailedListV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Rows and trend use SpacesRow fields; projection uses SpacesProjection fields. Invalid fields for the selected view return 400. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[str]
            Rows: room_name, available_spaces, open_spaces, occupied_spaces or occupancy_rate with _asc/_desc. Aggregates: sum_available_spaces, sum_open_spaces, sum_occupied_spaces, sum_closed_spaces, sum_unavailable_spaces, capacity or occupancy_rate with _asc/_desc. Other views reject sort_by. Defaults: room_name_asc for rows; sum_open_spaces_desc for aggregates.

        group_by : typing.Optional[GetSpacesDetailedListV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetSpacesDetailedListV3RequestMetricsItem, typing.Sequence[GetSpacesDetailedListV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. If provided, must be positive.

        page : typing.Optional[int]
            One-based page number. Rows only; other representations reject pagination parameters.

        per_page : typing.Optional[int]
            Items per page; values greater than 200 are clamped to 200. Rows only; other representations reject pagination parameters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSpacesDetailedListV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "spaces/detailed_list",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "view": view,
                "period": period,
                "room_id": room_id,
                "room_ids": room_ids,
                "school_ids": school_ids,
                "only_active": only_active,
                "period_from": period_from,
                "period_to": period_to,
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
                    GetSpacesDetailedListV3Response,
                    parse_obj_as(
                        type_=GetSpacesDetailedListV3Response,
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

    async def patch_spaces_closed_spaces_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        closed_spaces: typing.Sequence[ClosedSpaceCell],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateClosedSpacesResponse]:
        """
        Requires an authenticated user in the Operations or Admin group, school_id assigned to the session, and room IDs belonging to that school. Each room_id/period pair must be unique in the body. closed_spaces must be nonnegative and no greater than room capacity. Positive values create/update overrides; zero removes an existing override. All cells are validated before writes. Upserts and deletes execute separately; a later failure may leave earlier changes applied. modified counts upserts plus existing rows deleted (a zero for a missing override does not increase it).

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID. Must be assigned to the authenticated session.

        closed_spaces : typing.Sequence[ClosedSpaceCell]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateClosedSpacesResponse]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "spaces/closed_spaces",
            method="PATCH",
            params={
                "company_id": company_id,
                "school_id": school_id,
            },
            json={
                "closed_spaces": convert_and_respect_annotation_metadata(
                    object_=closed_spaces, annotation=typing.Sequence[ClosedSpaceCell], direction="write"
                ),
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
                    UpdateClosedSpacesResponse,
                    parse_obj_as(
                        type_=UpdateClosedSpacesResponse,
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
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
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

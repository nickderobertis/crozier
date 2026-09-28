

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.billing_plan import BillingPlan
from ..types.error import Error
from .types.get_billing_plans_v3request_group_by import GetBillingPlansV3RequestGroupBy
from .types.get_billing_plans_v3request_metrics_item import GetBillingPlansV3RequestMetricsItem
from .types.get_billing_plans_v3request_sort_by import GetBillingPlansV3RequestSortBy
from .types.get_billing_plans_v3response import GetBillingPlansV3Response
from pydantic import ValidationError


class RawBillingPlansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_billing_plans_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        room_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        room_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        plan_status: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        has_alerts: typing.Optional[bool] = None,
        active_rooms_only: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetBillingPlansV3RequestSortBy] = None,
        group_by: typing.Optional[GetBillingPlansV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetBillingPlansV3RequestMetricsItem, typing.Sequence[GetBillingPlansV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetBillingPlansV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns consolidated billing-plan rows, or nested BillingPlanAggregate rows when group_by and metrics are supplied. school_id is always required. A consolidated row keeps the ID of the first plan in its group.

        Rows support plan_status, room filters, query, has_alerts, active_rooms_only and pagination; sorting rows returns 400. Aggregates use school, room filters, plan_status (default active), group_by, metrics, sort_by and limit. query, has_alerts and active_rooms_only do not affect aggregate results, although boolean values are parsed and validated. X-Has-Alerts applies only to row responses; X-Room-Filter-Count and X-Truncated apply only to aggregates.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        room_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with room_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        room_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional room UUID filters, combined with room_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        plan_status : typing.Optional[str]
            Free-text plan status. Aggregate view defaults to active when omitted.

        query : typing.Optional[str]
            Row view only: search text.

        has_alerts : typing.Optional[bool]
            Row view only: return only plans with alerts when true. Accepts true/1 and false/0, case-insensitive.

        active_rooms_only : typing.Optional[bool]
            Row view only: restrict to active rooms. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetBillingPlansV3RequestSortBy]
            Aggregate view only. Sending sort_by without group_by returns 400.

        group_by : typing.Optional[GetBillingPlansV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetBillingPlansV3RequestMetricsItem, typing.Sequence[GetBillingPlansV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.

        page : typing.Optional[int]
            One-based page number. Row view only.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500. Row view only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBillingPlansV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "billing_plans",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "room_id": room_id,
                "room_ids": room_ids,
                "plan_status": plan_status,
                "query": query,
                "has_alerts": has_alerts,
                "active_rooms_only": active_rooms_only,
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
                    GetBillingPlansV3Response,
                    parse_obj_as(
                        type_=GetBillingPlansV3Response,
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

    def get_billing_plans_id_v3(
        self, id: str, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BillingPlan]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. The ID is the consolidated row ID returned by the collection (the first plan ID in a group). Collection filters do not affect the lookup, though the shared parser still validates any supplied room IDs and boolean filters. Returns 404 when the school has no matching consolidated plan.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BillingPlan]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"billing_plans/{encode_path_param(id)}",
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
                    BillingPlan,
                    parse_obj_as(
                        type_=BillingPlan,
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
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawBillingPlansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_billing_plans_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        room_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        room_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        plan_status: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        has_alerts: typing.Optional[bool] = None,
        active_rooms_only: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetBillingPlansV3RequestSortBy] = None,
        group_by: typing.Optional[GetBillingPlansV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetBillingPlansV3RequestMetricsItem, typing.Sequence[GetBillingPlansV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetBillingPlansV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns consolidated billing-plan rows, or nested BillingPlanAggregate rows when group_by and metrics are supplied. school_id is always required. A consolidated row keeps the ID of the first plan in its group.

        Rows support plan_status, room filters, query, has_alerts, active_rooms_only and pagination; sorting rows returns 400. Aggregates use school, room filters, plan_status (default active), group_by, metrics, sort_by and limit. query, has_alerts and active_rooms_only do not affect aggregate results, although boolean values are parsed and validated. X-Has-Alerts applies only to row responses; X-Room-Filter-Count and X-Truncated apply only to aggregates.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        room_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Alias combined with room_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        room_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional room UUID filters, combined with room_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        plan_status : typing.Optional[str]
            Free-text plan status. Aggregate view defaults to active when omitted.

        query : typing.Optional[str]
            Row view only: search text.

        has_alerts : typing.Optional[bool]
            Row view only: return only plans with alerts when true. Accepts true/1 and false/0, case-insensitive.

        active_rooms_only : typing.Optional[bool]
            Row view only: restrict to active rooms. Accepts true/1 and false/0, case-insensitive.

        sort_by : typing.Optional[GetBillingPlansV3RequestSortBy]
            Aggregate view only. Sending sort_by without group_by returns 400.

        group_by : typing.Optional[GetBillingPlansV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetBillingPlansV3RequestMetricsItem, typing.Sequence[GetBillingPlansV3RequestMetricsItem]]]
            Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        limit : typing.Optional[int]
            Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.

        page : typing.Optional[int]
            One-based page number. Row view only.

        per_page : typing.Optional[int]
            Items per page; values greater than 500 are clamped to 500. Row view only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBillingPlansV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "billing_plans",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "room_id": room_id,
                "room_ids": room_ids,
                "plan_status": plan_status,
                "query": query,
                "has_alerts": has_alerts,
                "active_rooms_only": active_rooms_only,
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
                    GetBillingPlansV3Response,
                    parse_obj_as(
                        type_=GetBillingPlansV3Response,
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

    async def get_billing_plans_id_v3(
        self, id: str, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BillingPlan]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. The ID is the consolidated row ID returned by the collection (the first plan ID in a group). Collection filters do not affect the lookup, though the shared parser still validates any supplied room IDs and boolean filters. Returns 404 when the school has no matching consolidated plan.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BillingPlan]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"billing_plans/{encode_path_param(id)}",
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
                    BillingPlan,
                    parse_obj_as(
                        type_=BillingPlan,
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
            if _response.status_code == 404:
                raise NotFoundError(
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

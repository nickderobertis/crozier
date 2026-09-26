

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
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.payment import Payment
from .types.get_payments_id_v3request_fields_item import GetPaymentsIdV3RequestFieldsItem
from .types.get_payments_v3request_fields_item import GetPaymentsV3RequestFieldsItem
from .types.get_payments_v3request_group_by import GetPaymentsV3RequestGroupBy
from .types.get_payments_v3request_metrics_item import GetPaymentsV3RequestMetricsItem
from .types.get_payments_v3response import GetPaymentsV3Response
from pydantic import ValidationError


class RawPaymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_payments_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_id: typing.Optional[str] = None,
        family_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_name: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        state: typing.Optional[str] = None,
        is_posted: typing.Optional[bool] = None,
        successful_only: typing.Optional[bool] = None,
        payment_mode: typing.Optional[str] = None,
        payment_method_sub_kind: typing.Optional[str] = None,
        min_amount: typing.Optional[float] = None,
        max_amount: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetPaymentsV3RequestFieldsItem, typing.Sequence[GetPaymentsV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[str] = None,
        group_by: typing.Optional[GetPaymentsV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetPaymentsV3RequestMetricsItem, typing.Sequence[GetPaymentsV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPaymentsV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Without group_by, returns sparse payment rows. With group_by and metrics, returns nested PaymentAggregate rows. school_id and school_ids are both applied when provided (their intersection); omitted school filters read the company scope. Row queries support family_id/family_ids; these IDs do not filter the aggregate representation. fields and pagination apply only to rows. Aggregate responses use limit, X-Total-Count and X-Truncated, without Link.

        An explicit date range requires both bounds and date_to >= date_from. These date checks occur in the data layer; failures currently produce HTTP 500 rather than 400. last_n_days and explicit bounds can both restrict the result. Item and collection school filters are independent of the session school assignments.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_id : typing.Optional[str]
            Row view only: optional family UUID. When family_ids is also supplied, the reader first restricts to this family; family_ids cannot widen that scope.

        family_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional family UUIDs; row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_name : typing.Optional[str]
            Case-insensitive family-name substring filter.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.

        last_n_days : typing.Optional[int]
            Rolling lookback on payment created_at (not transaction_date). Positive values add this filter; zero/negative values do not. May be combined with a transaction-date range.

        state : typing.Optional[str]
            Case-insensitive payment state filter.

        is_posted : typing.Optional[bool]
            Filter by posted state; omit for both states. Accepts true/1 and false/0, case-insensitive.

        successful_only : typing.Optional[bool]
            Include payments that are posted or whose normalized state is success, succeeded, completed, paid, posted, processed, settled or state_success. Only true/1 enables the filter; other values disable it.

        payment_mode : typing.Optional[str]
            Case-insensitive payment mode filter.

        payment_method_sub_kind : typing.Optional[str]
            Case-insensitive payment method subtype filter.

        min_amount : typing.Optional[float]
            Inclusive minimum payment amount.

        max_amount : typing.Optional[float]
            Inclusive maximum payment amount.

        fields : typing.Optional[typing.Union[GetPaymentsV3RequestFieldsItem, typing.Sequence[GetPaymentsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[str]
            Rows: transaction_date, amount, total_amount, created_at or family_name with _asc/_desc (default transaction_date_desc). Aggregates: group or any supported metric with _asc/_desc. Unrecognized sort keys fall back to the backend default. Aggregate default: count_desc.

        group_by : typing.Optional[GetPaymentsV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetPaymentsV3RequestMetricsItem, typing.Sequence[GetPaymentsV3RequestMetricsItem]]]
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
        HttpResponse[GetPaymentsV3Response]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "payments",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "school_ids": school_ids,
                "family_id": family_id,
                "family_ids": family_ids,
                "family_name": family_name,
                "date_from": str(date_from) if date_from is not None else None,
                "date_to": str(date_to) if date_to is not None else None,
                "last_n_days": last_n_days,
                "state": state,
                "is_posted": is_posted,
                "successful_only": successful_only,
                "payment_mode": payment_mode,
                "payment_method_sub_kind": payment_method_sub_kind,
                "min_amount": min_amount,
                "max_amount": max_amount,
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
                    GetPaymentsV3Response,
                    parse_obj_as(
                        type_=GetPaymentsV3Response,
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

    def get_payments_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[
            typing.Union[GetPaymentsIdV3RequestFieldsItem, typing.Sequence[GetPaymentsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Payment]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Only school_id/school_ids and fields affect the item lookup. The shared filter parser still validates supplied family IDs, last_n_days, is_posted and amount bounds, but collection filters do not narrow the item. Returns 404 when no payment matches its ID and school scope.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        fields : typing.Optional[typing.Union[GetPaymentsIdV3RequestFieldsItem, typing.Sequence[GetPaymentsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Payment]
            Successful response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"payments/{encode_path_param(id)}",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "school_ids": school_ids,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Payment,
                    parse_obj_as(
                        type_=Payment,
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


class AsyncRawPaymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_payments_v3(
        self,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_id: typing.Optional[str] = None,
        family_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        family_name: typing.Optional[str] = None,
        date_from: typing.Optional[dt.date] = None,
        date_to: typing.Optional[dt.date] = None,
        last_n_days: typing.Optional[int] = None,
        state: typing.Optional[str] = None,
        is_posted: typing.Optional[bool] = None,
        successful_only: typing.Optional[bool] = None,
        payment_mode: typing.Optional[str] = None,
        payment_method_sub_kind: typing.Optional[str] = None,
        min_amount: typing.Optional[float] = None,
        max_amount: typing.Optional[float] = None,
        fields: typing.Optional[
            typing.Union[GetPaymentsV3RequestFieldsItem, typing.Sequence[GetPaymentsV3RequestFieldsItem]]
        ] = None,
        sort_by: typing.Optional[str] = None,
        group_by: typing.Optional[GetPaymentsV3RequestGroupBy] = None,
        metrics: typing.Optional[
            typing.Union[GetPaymentsV3RequestMetricsItem, typing.Sequence[GetPaymentsV3RequestMetricsItem]]
        ] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPaymentsV3Response]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Without group_by, returns sparse payment rows. With group_by and metrics, returns nested PaymentAggregate rows. school_id and school_ids are both applied when provided (their intersection); omitted school filters read the company scope. Row queries support family_id/family_ids; these IDs do not filter the aggregate representation. fields and pagination apply only to rows. Aggregate responses use limit, X-Total-Count and X-Truncated, without Link.

        An explicit date range requires both bounds and date_to >= date_from. These date checks occur in the data layer; failures currently produce HTTP 500 rather than 400. last_n_days and explicit bounds can both restrict the result. Item and collection school filters are independent of the session school assignments.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_id : typing.Optional[str]
            Row view only: optional family UUID. When family_ids is also supplied, the reader first restricts to this family; family_ids cannot widen that scope.

        family_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional family UUIDs; row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        family_name : typing.Optional[str]
            Case-insensitive family-name substring filter.

        date_from : typing.Optional[dt.date]
            Inclusive start date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.

        date_to : typing.Optional[dt.date]
            Inclusive end date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.

        last_n_days : typing.Optional[int]
            Rolling lookback on payment created_at (not transaction_date). Positive values add this filter; zero/negative values do not. May be combined with a transaction-date range.

        state : typing.Optional[str]
            Case-insensitive payment state filter.

        is_posted : typing.Optional[bool]
            Filter by posted state; omit for both states. Accepts true/1 and false/0, case-insensitive.

        successful_only : typing.Optional[bool]
            Include payments that are posted or whose normalized state is success, succeeded, completed, paid, posted, processed, settled or state_success. Only true/1 enables the filter; other values disable it.

        payment_mode : typing.Optional[str]
            Case-insensitive payment mode filter.

        payment_method_sub_kind : typing.Optional[str]
            Case-insensitive payment method subtype filter.

        min_amount : typing.Optional[float]
            Inclusive minimum payment amount.

        max_amount : typing.Optional[float]
            Inclusive maximum payment amount.

        fields : typing.Optional[typing.Union[GetPaymentsV3RequestFieldsItem, typing.Sequence[GetPaymentsV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        sort_by : typing.Optional[str]
            Rows: transaction_date, amount, total_amount, created_at or family_name with _asc/_desc (default transaction_date_desc). Aggregates: group or any supported metric with _asc/_desc. Unrecognized sort keys fall back to the backend default. Aggregate default: count_desc.

        group_by : typing.Optional[GetPaymentsV3RequestGroupBy]
            Select an aggregate representation; metrics must also be supplied.

        metrics : typing.Optional[typing.Union[GetPaymentsV3RequestMetricsItem, typing.Sequence[GetPaymentsV3RequestMetricsItem]]]
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
        AsyncHttpResponse[GetPaymentsV3Response]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "payments",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "school_ids": school_ids,
                "family_id": family_id,
                "family_ids": family_ids,
                "family_name": family_name,
                "date_from": str(date_from) if date_from is not None else None,
                "date_to": str(date_to) if date_to is not None else None,
                "last_n_days": last_n_days,
                "state": state,
                "is_posted": is_posted,
                "successful_only": successful_only,
                "payment_mode": payment_mode,
                "payment_method_sub_kind": payment_method_sub_kind,
                "min_amount": min_amount,
                "max_amount": max_amount,
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
                    GetPaymentsV3Response,
                    parse_obj_as(
                        type_=GetPaymentsV3Response,
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

    async def get_payments_id_v3(
        self,
        id: str,
        *,
        company_id: str,
        school_id: typing.Optional[str] = None,
        school_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[
            typing.Union[GetPaymentsIdV3RequestFieldsItem, typing.Sequence[GetPaymentsIdV3RequestFieldsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Payment]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Only school_id/school_ids and fields affect the item lookup. The shared filter parser still validates supplied family IDs, last_n_days, is_posted and amount bounds, but collection filters do not narrow the item. Returns 404 when no payment matches its ID and school scope.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : typing.Optional[str]
            School UUID. Omit to use the operation's documented company/session scope.

        school_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        fields : typing.Optional[typing.Union[GetPaymentsIdV3RequestFieldsItem, typing.Sequence[GetPaymentsIdV3RequestFieldsItem]]]
            Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Payment]
            Successful response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"payments/{encode_path_param(id)}",
            method="GET",
            params={
                "company_id": company_id,
                "school_id": school_id,
                "school_ids": school_ids,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Payment,
                    parse_obj_as(
                        type_=Payment,
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

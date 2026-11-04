

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.action_denied_err import ActionDeniedErr
from ..types.bulk_export_resp_body import BulkExportRespBody
from ..types.cancel_order_resp_body import CancelOrderRespBody
from ..types.create_order_resp_body import CreateOrderRespBody
from ..types.currency_code import CurrencyCode
from ..types.defaults_resp_body import DefaultsRespBody
from ..types.filter_orders_resp_body import FilterOrdersRespBody
from ..types.force_ship_resp_body import ForceShipRespBody
from ..types.get_order_resp_body import GetOrderRespBody
from ..types.line_item import LineItem
from ..types.list_orders_resp_body import ListOrdersRespBody
from ..types.maintenance_window_err import MaintenanceWindowErr
from ..types.non_empty_id import NonEmptyId
from ..types.order_not_found_err import OrderNotFoundErr
from ..types.order_status import OrderStatus
from ..types.payment_failed_err import PaymentFailedErr
from ..types.payment_method import PaymentMethod
from ..types.public_health_resp_body import PublicHealthRespBody
from ..types.rate_limited_err import RateLimitedErr
from ..types.replay_resp_body import ReplayRespBody
from ..types.track_public_resp_body import TrackPublicRespBody
from ..types.unauthorized_err import UnauthorizedErr
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_order(
        self,
        *,
        customer_id: NonEmptyId,
        items: typing.Sequence[LineItem],
        currency: typing.Optional[CurrencyCode] = OMIT,
        notes: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateOrderRespBody]:
        """
        Create a new order.

        Parameters
        ----------
        customer_id : NonEmptyId

        items : typing.Sequence[LineItem]

        currency : typing.Optional[CurrencyCode]

        notes : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateOrderRespBody]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "orders",
            method="POST",
            json={
                "currency": currency,
                "customerId": customer_id,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[LineItem], direction="write"
                ),
                "notes": notes,
                "tags": tags,
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
                    CreateOrderRespBody,
                    parse_obj_as(
                        type_=CreateOrderRespBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErr,
                        parse_obj_as(
                            type_=UnauthorizedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentFailedErr,
                        parse_obj_as(
                            type_=PaymentFailedErr,
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

    def get_order(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetOrderRespBody]:
        """
        Fetch one order.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetOrderRespBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOrderRespBody,
                    parse_obj_as(
                        type_=GetOrderRespBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErr,
                        parse_obj_as(
                            type_=UnauthorizedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrderNotFoundErr,
                        parse_obj_as(
                            type_=OrderNotFoundErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        MaintenanceWindowErr,
                        parse_obj_as(
                            type_=MaintenanceWindowErr,
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

    def cancel_order(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelOrderRespBody]:
        """
        Admin cancellation. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CancelOrderRespBody]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelOrderRespBody,
                    parse_obj_as(
                        type_=CancelOrderRespBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ActionDeniedErr,
                        parse_obj_as(
                            type_=ActionDeniedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrderNotFoundErr,
                        parse_obj_as(
                            type_=OrderNotFoundErr,
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

    def replay(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReplayRespBody]:
        """
        Admin replay (parent chain only).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReplayRespBody]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}/replay",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReplayRespBody,
                    parse_obj_as(
                        type_=ReplayRespBody,
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

    def force_ship(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ForceShipRespBody]:
        """
        Admin force-ship. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ForceShipRespBody]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}/ship",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForceShipRespBody,
                    parse_obj_as(
                        type_=ForceShipRespBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ActionDeniedErr,
                        parse_obj_as(
                            type_=ActionDeniedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrderNotFoundErr,
                        parse_obj_as(
                            type_=OrderNotFoundErr,
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

    def track_public(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TrackPublicRespBody]:
        """
        Public order tracking by id - CORS only, no auth.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrackPublicRespBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}/track",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrackPublicRespBody,
                    parse_obj_as(
                        type_=TrackPublicRespBody,
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

    def filter_orders(
        self,
        *,
        status: OrderStatus,
        method: PaymentMethod,
        limit: int,
        max_price: int,
        retry_after: int,
        idem_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FilterOrdersRespBody]:
        """
        Filter orders by status - showcases @query/@header/@cookie on one DTO. Status is a @query filter (a literal sub-path keeps it from colliding with /{id}/... actions on the ServeMux).

        Parameters
        ----------
        status : OrderStatus

        method : PaymentMethod

        limit : int

        max_price : int

        retry_after : int

        idem_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilterOrdersRespBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "orders/by-status",
            method="GET",
            params={
                "status": status,
                "method": method,
                "limit": limit,
                "maxPrice": max_price,
            },
            headers={
                "idemKey": str(idem_key) if idem_key is not None else None,
                "retryAfter": str(retry_after) if retry_after is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilterOrdersRespBody,
                    parse_obj_as(
                        type_=FilterOrdersRespBody,
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

    def defaults(
        self,
        *,
        allowed_methods: typing.Optional[typing.Sequence[PaymentMethod]] = OMIT,
        currency: typing.Optional[CurrencyCode] = OMIT,
        flag: typing.Optional[bool] = OMIT,
        num: typing.Optional[int] = OMIT,
        preset: typing.Optional[typing.Sequence[str]] = OMIT,
        status: typing.Optional[OrderStatus] = OMIT,
        str: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DefaultsRespBody]:
        """
        Echo every @default form.

        Parameters
        ----------
        allowed_methods : typing.Optional[typing.Sequence[PaymentMethod]]

        currency : typing.Optional[CurrencyCode]

        flag : typing.Optional[bool]

        num : typing.Optional[int]

        preset : typing.Optional[typing.Sequence[str]]

        status : typing.Optional[OrderStatus]

        str : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DefaultsRespBody]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "orders/defaults",
            method="POST",
            json={
                "allowedMethods": allowed_methods,
                "currency": currency,
                "flag": flag,
                "num": num,
                "preset": preset,
                "status": status,
                "str": str,
                "tags": tags,
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
                    DefaultsRespBody,
                    parse_obj_as(
                        type_=DefaultsRespBody,
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

    def bulk_export(
        self,
        *,
        limit: int,
        status: typing.Optional[OrderStatus] = None,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkExportRespBody]:
        """
        Bulk export - admin only, extra body-limit/timeout on top of parent chain.

        Parameters
        ----------
        limit : int

        status : typing.Optional[OrderStatus]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkExportRespBody]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "orders/export",
            method="POST",
            params={
                "status": status,
            },
            json={
                "cursor": cursor,
                "limit": limit,
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
                    BulkExportRespBody,
                    parse_obj_as(
                        type_=BulkExportRespBody,
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

    def public_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PublicHealthRespBody]:
        """
        Public readiness probe - bypasses every parent middleware AND security.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PublicHealthRespBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "orders/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PublicHealthRespBody,
                    parse_obj_as(
                        type_=PublicHealthRespBody,
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

    def list_orders(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        status: typing.Optional[OrderStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListOrdersRespBody]:
        """
        List orders.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        status : typing.Optional[OrderStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListOrdersRespBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "orders/list-orders",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListOrdersRespBody,
                    parse_obj_as(
                        type_=ListOrdersRespBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErr,
                        parse_obj_as(
                            type_=UnauthorizedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitedErr,
                        parse_obj_as(
                            type_=RateLimitedErr,
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


class AsyncRawOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_order(
        self,
        *,
        customer_id: NonEmptyId,
        items: typing.Sequence[LineItem],
        currency: typing.Optional[CurrencyCode] = OMIT,
        notes: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateOrderRespBody]:
        """
        Create a new order.

        Parameters
        ----------
        customer_id : NonEmptyId

        items : typing.Sequence[LineItem]

        currency : typing.Optional[CurrencyCode]

        notes : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateOrderRespBody]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "orders",
            method="POST",
            json={
                "currency": currency,
                "customerId": customer_id,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[LineItem], direction="write"
                ),
                "notes": notes,
                "tags": tags,
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
                    CreateOrderRespBody,
                    parse_obj_as(
                        type_=CreateOrderRespBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErr,
                        parse_obj_as(
                            type_=UnauthorizedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentFailedErr,
                        parse_obj_as(
                            type_=PaymentFailedErr,
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

    async def get_order(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetOrderRespBody]:
        """
        Fetch one order.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetOrderRespBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOrderRespBody,
                    parse_obj_as(
                        type_=GetOrderRespBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErr,
                        parse_obj_as(
                            type_=UnauthorizedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrderNotFoundErr,
                        parse_obj_as(
                            type_=OrderNotFoundErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        MaintenanceWindowErr,
                        parse_obj_as(
                            type_=MaintenanceWindowErr,
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

    async def cancel_order(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelOrderRespBody]:
        """
        Admin cancellation. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CancelOrderRespBody]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelOrderRespBody,
                    parse_obj_as(
                        type_=CancelOrderRespBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ActionDeniedErr,
                        parse_obj_as(
                            type_=ActionDeniedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrderNotFoundErr,
                        parse_obj_as(
                            type_=OrderNotFoundErr,
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

    async def replay(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReplayRespBody]:
        """
        Admin replay (parent chain only).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReplayRespBody]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}/replay",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReplayRespBody,
                    parse_obj_as(
                        type_=ReplayRespBody,
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

    async def force_ship(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ForceShipRespBody]:
        """
        Admin force-ship. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ForceShipRespBody]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}/ship",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForceShipRespBody,
                    parse_obj_as(
                        type_=ForceShipRespBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ActionDeniedErr,
                        parse_obj_as(
                            type_=ActionDeniedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OrderNotFoundErr,
                        parse_obj_as(
                            type_=OrderNotFoundErr,
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

    async def track_public(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TrackPublicRespBody]:
        """
        Public order tracking by id - CORS only, no auth.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrackPublicRespBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"orders/{encode_path_param(id)}/track",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrackPublicRespBody,
                    parse_obj_as(
                        type_=TrackPublicRespBody,
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

    async def filter_orders(
        self,
        *,
        status: OrderStatus,
        method: PaymentMethod,
        limit: int,
        max_price: int,
        retry_after: int,
        idem_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FilterOrdersRespBody]:
        """
        Filter orders by status - showcases @query/@header/@cookie on one DTO. Status is a @query filter (a literal sub-path keeps it from colliding with /{id}/... actions on the ServeMux).

        Parameters
        ----------
        status : OrderStatus

        method : PaymentMethod

        limit : int

        max_price : int

        retry_after : int

        idem_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilterOrdersRespBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "orders/by-status",
            method="GET",
            params={
                "status": status,
                "method": method,
                "limit": limit,
                "maxPrice": max_price,
            },
            headers={
                "idemKey": str(idem_key) if idem_key is not None else None,
                "retryAfter": str(retry_after) if retry_after is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilterOrdersRespBody,
                    parse_obj_as(
                        type_=FilterOrdersRespBody,
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

    async def defaults(
        self,
        *,
        allowed_methods: typing.Optional[typing.Sequence[PaymentMethod]] = OMIT,
        currency: typing.Optional[CurrencyCode] = OMIT,
        flag: typing.Optional[bool] = OMIT,
        num: typing.Optional[int] = OMIT,
        preset: typing.Optional[typing.Sequence[str]] = OMIT,
        status: typing.Optional[OrderStatus] = OMIT,
        str: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DefaultsRespBody]:
        """
        Echo every @default form.

        Parameters
        ----------
        allowed_methods : typing.Optional[typing.Sequence[PaymentMethod]]

        currency : typing.Optional[CurrencyCode]

        flag : typing.Optional[bool]

        num : typing.Optional[int]

        preset : typing.Optional[typing.Sequence[str]]

        status : typing.Optional[OrderStatus]

        str : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DefaultsRespBody]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "orders/defaults",
            method="POST",
            json={
                "allowedMethods": allowed_methods,
                "currency": currency,
                "flag": flag,
                "num": num,
                "preset": preset,
                "status": status,
                "str": str,
                "tags": tags,
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
                    DefaultsRespBody,
                    parse_obj_as(
                        type_=DefaultsRespBody,
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

    async def bulk_export(
        self,
        *,
        limit: int,
        status: typing.Optional[OrderStatus] = None,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkExportRespBody]:
        """
        Bulk export - admin only, extra body-limit/timeout on top of parent chain.

        Parameters
        ----------
        limit : int

        status : typing.Optional[OrderStatus]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkExportRespBody]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "orders/export",
            method="POST",
            params={
                "status": status,
            },
            json={
                "cursor": cursor,
                "limit": limit,
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
                    BulkExportRespBody,
                    parse_obj_as(
                        type_=BulkExportRespBody,
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

    async def public_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PublicHealthRespBody]:
        """
        Public readiness probe - bypasses every parent middleware AND security.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PublicHealthRespBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "orders/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PublicHealthRespBody,
                    parse_obj_as(
                        type_=PublicHealthRespBody,
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

    async def list_orders(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        status: typing.Optional[OrderStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListOrdersRespBody]:
        """
        List orders.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        status : typing.Optional[OrderStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListOrdersRespBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "orders/list-orders",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListOrdersRespBody,
                    parse_obj_as(
                        type_=ListOrdersRespBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErr,
                        parse_obj_as(
                            type_=UnauthorizedErr,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitedErr,
                        parse_obj_as(
                            type_=RateLimitedErr,
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



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
from ..types.v1money import V1Money
from ..types.v1order import V1Order
from ..types.v1payment import V1Payment
from ..types.v1refund import V1Refund
from ..types.v1settlement import V1Settlement
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawV1TransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_orders(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Order]]:
        """
        Provides summary information for a merchant's online store orders.

        Parameters
        ----------
        location_id : str
            The ID of the location to list online store orders for.

        order : typing.Optional[str]
            The order in which payments are listed in the response.

        limit : typing.Optional[int]
            The maximum number of payments to return in a single response. This value cannot exceed 200.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Order]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/orders",
            method="GET",
            params={
                "order": order,
                "limit": limit,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Order],
                    parse_obj_as(
                        type_=typing.List[V1Order],
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

    def retrieve_order(
        self, location_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Order]:
        """
        Provides comprehensive information for a single online store order, including the order's history.

        Parameters
        ----------
        location_id : str
            The ID of the order's associated location.

        order_id : str
            The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Order]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/orders/{encode_path_param(order_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Order,
                    parse_obj_as(
                        type_=V1Order,
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

    def update_order(
        self,
        location_id: str,
        order_id: str,
        *,
        action: str,
        canceled_note: typing.Optional[str] = OMIT,
        completed_note: typing.Optional[str] = OMIT,
        refunded_note: typing.Optional[str] = OMIT,
        shipped_tracking_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Order]:
        """
        Updates the details of an online store order. Every update you perform on an order corresponds to one of three actions:

        Parameters
        ----------
        location_id : str
            The ID of the order's associated location.

        order_id : str
            The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint

        action : str
            The action to perform on the order (COMPLETE, CANCEL, or REFUND).

        canceled_note : typing.Optional[str]
            A merchant-specified note about the canceling of the order. Only valid if action is CANCEL.

        completed_note : typing.Optional[str]
            A merchant-specified note about the completion of the order. Only valid if action is COMPLETE.

        refunded_note : typing.Optional[str]
            A merchant-specified note about the refunding of the order. Only valid if action is REFUND.

        shipped_tracking_number : typing.Optional[str]
            The tracking number of the shipment associated with the order. Only valid if action is COMPLETE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Order]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/orders/{encode_path_param(order_id)}",
            method="PUT",
            json={
                "action": action,
                "canceled_note": canceled_note,
                "completed_note": completed_note,
                "refunded_note": refunded_note,
                "shipped_tracking_number": shipped_tracking_number,
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
                    V1Order,
                    parse_obj_as(
                        type_=V1Order,
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

    def list_payments(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        include_partial: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Payment]]:
        """
        Provides summary information for all payments taken for a given
        Square account during a date range. Date ranges cannot exceed 1 year in
        length. See Date ranges for details of inclusive and exclusive dates.

        *Note**: Details for payments processed with Square Point of Sale while
        in offline mode may not be transmitted to Square for up to 72 hours.
        Offline payments have a `created_at` value that reflects the time the
        payment was originally processed, not the time it was subsequently
        transmitted to Square. Consequently, the ListPayments endpoint might
        list an offline payment chronologically between online payments that
        were seen in a previous request.

        Parameters
        ----------
        location_id : str
            The ID of the location to list payments for. If you specify me, this endpoint returns payments aggregated from all of the business's locations.

        order : typing.Optional[str]
            The order in which payments are listed in the response.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.

        limit : typing.Optional[int]
            The maximum number of payments to return in a single response. This value cannot exceed 200.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        include_partial : typing.Optional[bool]
            Indicates whether or not to include partial payments in the response. Partial payments will have the tenders collected so far, but the itemizations will be empty until the payment is completed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Payment]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/payments",
            method="GET",
            params={
                "order": order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "batch_token": batch_token,
                "include_partial": include_partial,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Payment],
                    parse_obj_as(
                        type_=typing.List[V1Payment],
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

    def retrieve_payment(
        self, location_id: str, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Payment]:
        """
        Provides comprehensive information for a single payment.

        Parameters
        ----------
        location_id : str
            The ID of the payment's associated location.

        payment_id : str
            The Square-issued payment ID. payment_id comes from Payment objects returned by the List Payments endpoint, Settlement objects returned by the List Settlements endpoint, or Refund objects returned by the List Refunds endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Payment]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/payments/{encode_path_param(payment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Payment,
                    parse_obj_as(
                        type_=V1Payment,
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

    def list_refunds(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Refund]]:
        """
        Provides the details for all refunds initiated by a merchant or any of the merchant's mobile staff during a date range. Date ranges cannot exceed one year in length.

        Parameters
        ----------
        location_id : str
            The ID of the location to list refunds for.

        order : typing.Optional[str]
            The order in which payments are listed in the response.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.

        limit : typing.Optional[int]
            The approximate number of refunds to return in a single response. Default: 100. Max: 200. Response may contain more results than the prescribed limit when refunds are made simultaneously to multiple tenders in a payment or when refunds are generated in an exchange to account for the value of returned goods.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Refund]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/refunds",
            method="GET",
            params={
                "order": order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Refund],
                    parse_obj_as(
                        type_=typing.List[V1Refund],
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

    def create_refund(
        self,
        location_id: str,
        *,
        payment_id: str,
        reason: str,
        type: str,
        refunded_money: typing.Optional[V1Money] = OMIT,
        request_idempotence_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Refund]:
        """
        Issues a refund for a previously processed payment. You must issue
        a refund within 60 days of the associated payment.

        You cannot issue a partial refund for a split tender payment. You must
        instead issue a full or partial refund for a particular tender, by
        providing the applicable tender id to the V1CreateRefund endpoint.
        Issuing a full refund for a split tender payment refunds all tenders
        associated with the payment.

        Issuing a refund for a card payment is not reversible. For development
        purposes, you can create fake cash payments in Square Point of Sale and
        refund them.

        Parameters
        ----------
        location_id : str
            The ID of the original payment's associated location.

        payment_id : str
            The ID of the payment to refund. If you are creating a `PARTIAL`
            refund for a split tender payment, instead provide the id of the
            particular tender you want to refund.

        reason : str
            The reason for the refund.

        type : str
            The type of refund (FULL or PARTIAL).

        refunded_money : typing.Optional[V1Money]

        request_idempotence_key : typing.Optional[str]
            An optional key to ensure idempotence if you issue the same PARTIAL refund request more than once.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Refund]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/refunds",
            method="POST",
            json={
                "payment_id": payment_id,
                "reason": reason,
                "refunded_money": convert_and_respect_annotation_metadata(
                    object_=refunded_money, annotation=V1Money, direction="write"
                ),
                "request_idempotence_key": request_idempotence_key,
                "type": type,
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
                    V1Refund,
                    parse_obj_as(
                        type_=V1Refund,
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

    def list_settlements(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Settlement]]:
        """
        Provides summary information for all deposits and withdrawals
        initiated by Square to a linked bank account during a date range. Date
        ranges cannot exceed one year in length.

        *Note**: the ListSettlements endpoint does not provide entry
        information.

        Parameters
        ----------
        location_id : str
            The ID of the location to list settlements for. If you specify me, this endpoint returns settlements aggregated from all of the business's locations.

        order : typing.Optional[str]
            The order in which settlements are listed in the response.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.

        limit : typing.Optional[int]
            The maximum number of settlements to return in a single response. This value cannot exceed 200.

        status : typing.Optional[str]
            Provide this parameter to retrieve only settlements with a particular status (SENT or FAILED).

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Settlement]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/settlements",
            method="GET",
            params={
                "order": order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "status": status,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Settlement],
                    parse_obj_as(
                        type_=typing.List[V1Settlement],
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

    def retrieve_settlement(
        self, location_id: str, settlement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Settlement]:
        """
        Provides comprehensive information for a single settlement.

        The returned `Settlement` objects include an `entries` field that lists
        the transactions that contribute to the settlement total. Most
        settlement entries correspond to a payment payout, but settlement
        entries are also generated for less common events, like refunds, manual
        adjustments, or chargeback holds.

        Square initiates its regular deposits as indicated in the
        [Deposit Options with Square](https://squareup.com/help/us/en/article/3807)
        help article. Details for a regular deposit are usually not available
        from Connect API endpoints before 10 p.m. PST the same day.

        Square does not know when an initiated settlement **completes**, only
        whether it has failed. A completed settlement is typically reflected in
        a bank account within 3 business days, but in exceptional cases it may
        take longer.

        Parameters
        ----------
        location_id : str
            The ID of the settlements's associated location.

        settlement_id : str
            The settlement's Square-issued ID. You obtain this value from Settlement objects returned by the List Settlements endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Settlement]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/settlements/{encode_path_param(settlement_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Settlement,
                    parse_obj_as(
                        type_=V1Settlement,
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


class AsyncRawV1TransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_orders(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Order]]:
        """
        Provides summary information for a merchant's online store orders.

        Parameters
        ----------
        location_id : str
            The ID of the location to list online store orders for.

        order : typing.Optional[str]
            The order in which payments are listed in the response.

        limit : typing.Optional[int]
            The maximum number of payments to return in a single response. This value cannot exceed 200.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Order]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/orders",
            method="GET",
            params={
                "order": order,
                "limit": limit,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Order],
                    parse_obj_as(
                        type_=typing.List[V1Order],
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

    async def retrieve_order(
        self, location_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Order]:
        """
        Provides comprehensive information for a single online store order, including the order's history.

        Parameters
        ----------
        location_id : str
            The ID of the order's associated location.

        order_id : str
            The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Order]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/orders/{encode_path_param(order_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Order,
                    parse_obj_as(
                        type_=V1Order,
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

    async def update_order(
        self,
        location_id: str,
        order_id: str,
        *,
        action: str,
        canceled_note: typing.Optional[str] = OMIT,
        completed_note: typing.Optional[str] = OMIT,
        refunded_note: typing.Optional[str] = OMIT,
        shipped_tracking_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Order]:
        """
        Updates the details of an online store order. Every update you perform on an order corresponds to one of three actions:

        Parameters
        ----------
        location_id : str
            The ID of the order's associated location.

        order_id : str
            The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint

        action : str
            The action to perform on the order (COMPLETE, CANCEL, or REFUND).

        canceled_note : typing.Optional[str]
            A merchant-specified note about the canceling of the order. Only valid if action is CANCEL.

        completed_note : typing.Optional[str]
            A merchant-specified note about the completion of the order. Only valid if action is COMPLETE.

        refunded_note : typing.Optional[str]
            A merchant-specified note about the refunding of the order. Only valid if action is REFUND.

        shipped_tracking_number : typing.Optional[str]
            The tracking number of the shipment associated with the order. Only valid if action is COMPLETE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Order]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/orders/{encode_path_param(order_id)}",
            method="PUT",
            json={
                "action": action,
                "canceled_note": canceled_note,
                "completed_note": completed_note,
                "refunded_note": refunded_note,
                "shipped_tracking_number": shipped_tracking_number,
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
                    V1Order,
                    parse_obj_as(
                        type_=V1Order,
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

    async def list_payments(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        include_partial: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Payment]]:
        """
        Provides summary information for all payments taken for a given
        Square account during a date range. Date ranges cannot exceed 1 year in
        length. See Date ranges for details of inclusive and exclusive dates.

        *Note**: Details for payments processed with Square Point of Sale while
        in offline mode may not be transmitted to Square for up to 72 hours.
        Offline payments have a `created_at` value that reflects the time the
        payment was originally processed, not the time it was subsequently
        transmitted to Square. Consequently, the ListPayments endpoint might
        list an offline payment chronologically between online payments that
        were seen in a previous request.

        Parameters
        ----------
        location_id : str
            The ID of the location to list payments for. If you specify me, this endpoint returns payments aggregated from all of the business's locations.

        order : typing.Optional[str]
            The order in which payments are listed in the response.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.

        limit : typing.Optional[int]
            The maximum number of payments to return in a single response. This value cannot exceed 200.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        include_partial : typing.Optional[bool]
            Indicates whether or not to include partial payments in the response. Partial payments will have the tenders collected so far, but the itemizations will be empty until the payment is completed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Payment]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/payments",
            method="GET",
            params={
                "order": order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "batch_token": batch_token,
                "include_partial": include_partial,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Payment],
                    parse_obj_as(
                        type_=typing.List[V1Payment],
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

    async def retrieve_payment(
        self, location_id: str, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Payment]:
        """
        Provides comprehensive information for a single payment.

        Parameters
        ----------
        location_id : str
            The ID of the payment's associated location.

        payment_id : str
            The Square-issued payment ID. payment_id comes from Payment objects returned by the List Payments endpoint, Settlement objects returned by the List Settlements endpoint, or Refund objects returned by the List Refunds endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Payment]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/payments/{encode_path_param(payment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Payment,
                    parse_obj_as(
                        type_=V1Payment,
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

    async def list_refunds(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Refund]]:
        """
        Provides the details for all refunds initiated by a merchant or any of the merchant's mobile staff during a date range. Date ranges cannot exceed one year in length.

        Parameters
        ----------
        location_id : str
            The ID of the location to list refunds for.

        order : typing.Optional[str]
            The order in which payments are listed in the response.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.

        limit : typing.Optional[int]
            The approximate number of refunds to return in a single response. Default: 100. Max: 200. Response may contain more results than the prescribed limit when refunds are made simultaneously to multiple tenders in a payment or when refunds are generated in an exchange to account for the value of returned goods.

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Refund]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/refunds",
            method="GET",
            params={
                "order": order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Refund],
                    parse_obj_as(
                        type_=typing.List[V1Refund],
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

    async def create_refund(
        self,
        location_id: str,
        *,
        payment_id: str,
        reason: str,
        type: str,
        refunded_money: typing.Optional[V1Money] = OMIT,
        request_idempotence_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Refund]:
        """
        Issues a refund for a previously processed payment. You must issue
        a refund within 60 days of the associated payment.

        You cannot issue a partial refund for a split tender payment. You must
        instead issue a full or partial refund for a particular tender, by
        providing the applicable tender id to the V1CreateRefund endpoint.
        Issuing a full refund for a split tender payment refunds all tenders
        associated with the payment.

        Issuing a refund for a card payment is not reversible. For development
        purposes, you can create fake cash payments in Square Point of Sale and
        refund them.

        Parameters
        ----------
        location_id : str
            The ID of the original payment's associated location.

        payment_id : str
            The ID of the payment to refund. If you are creating a `PARTIAL`
            refund for a split tender payment, instead provide the id of the
            particular tender you want to refund.

        reason : str
            The reason for the refund.

        type : str
            The type of refund (FULL or PARTIAL).

        refunded_money : typing.Optional[V1Money]

        request_idempotence_key : typing.Optional[str]
            An optional key to ensure idempotence if you issue the same PARTIAL refund request more than once.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Refund]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/refunds",
            method="POST",
            json={
                "payment_id": payment_id,
                "reason": reason,
                "refunded_money": convert_and_respect_annotation_metadata(
                    object_=refunded_money, annotation=V1Money, direction="write"
                ),
                "request_idempotence_key": request_idempotence_key,
                "type": type,
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
                    V1Refund,
                    parse_obj_as(
                        type_=V1Refund,
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

    async def list_settlements(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Settlement]]:
        """
        Provides summary information for all deposits and withdrawals
        initiated by Square to a linked bank account during a date range. Date
        ranges cannot exceed one year in length.

        *Note**: the ListSettlements endpoint does not provide entry
        information.

        Parameters
        ----------
        location_id : str
            The ID of the location to list settlements for. If you specify me, this endpoint returns settlements aggregated from all of the business's locations.

        order : typing.Optional[str]
            The order in which settlements are listed in the response.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.

        limit : typing.Optional[int]
            The maximum number of settlements to return in a single response. This value cannot exceed 200.

        status : typing.Optional[str]
            Provide this parameter to retrieve only settlements with a particular status (SENT or FAILED).

        batch_token : typing.Optional[str]
            A pagination cursor to retrieve the next set of results for your
            original query to the endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Settlement]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/settlements",
            method="GET",
            params={
                "order": order,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "status": status,
                "batch_token": batch_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Settlement],
                    parse_obj_as(
                        type_=typing.List[V1Settlement],
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

    async def retrieve_settlement(
        self, location_id: str, settlement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Settlement]:
        """
        Provides comprehensive information for a single settlement.

        The returned `Settlement` objects include an `entries` field that lists
        the transactions that contribute to the settlement total. Most
        settlement entries correspond to a payment payout, but settlement
        entries are also generated for less common events, like refunds, manual
        adjustments, or chargeback holds.

        Square initiates its regular deposits as indicated in the
        [Deposit Options with Square](https://squareup.com/help/us/en/article/3807)
        help article. Details for a regular deposit are usually not available
        from Connect API endpoints before 10 p.m. PST the same day.

        Square does not know when an initiated settlement **completes**, only
        whether it has failed. A completed settlement is typically reflected in
        a bank account within 3 business days, but in exceptional cases it may
        take longer.

        Parameters
        ----------
        location_id : str
            The ID of the settlements's associated location.

        settlement_id : str
            The settlement's Square-issued ID. You obtain this value from Settlement objects returned by the List Settlements endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Settlement]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/{encode_path_param(location_id)}/settlements/{encode_path_param(settlement_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Settlement,
                    parse_obj_as(
                        type_=V1Settlement,
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



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
from ..types.get_payment_refund_response import GetPaymentRefundResponse
from ..types.list_payment_refunds_response import ListPaymentRefundsResponse
from ..types.money import Money
from ..types.refund_payment_response import RefundPaymentResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRefundsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_payment_refunds(
        self,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        source_type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPaymentRefundsResponse]:
        """
        Retrieves a list of refunds for the account making the request.

        Results are eventually consistent, and new refunds or changes to refunds might take several
        seconds to appear.

        The maximum results per page is 100.

        Parameters
        ----------
        begin_time : typing.Optional[str]
            The timestamp for the beginning of the requested reporting period, in RFC 3339 format.

            Default: The current time minus one year.

        end_time : typing.Optional[str]
            The timestamp for the end of the requested reporting period, in RFC 3339 format.

            Default: The current time.

        sort_order : typing.Optional[str]
            The order in which results are listed:
            - `ASC` - Oldest to newest.
            - `DESC` - Newest to oldest (default).

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        location_id : typing.Optional[str]
            Limit results to the location supplied. By default, results are returned
            for all locations associated with the seller.

        status : typing.Optional[str]
            If provided, only refunds with the given status are returned.
            For a list of refund status values, see [PaymentRefund](https://developer.squareup.com/reference/square_2021-08-18/objects/PaymentRefund).

            Default: If omitted, refunds are returned regardless of their status.

        source_type : typing.Optional[str]
            If provided, only refunds with the given source type are returned.
            - `CARD` - List refunds only for payments where `CARD` was specified as the payment
            source.

            Default: If omitted, refunds are returned regardless of the source type.

        limit : typing.Optional[int]
            The maximum number of results to be returned in a single page.

            It is possible to receive fewer results than the specified limit on a given page.

            If the supplied value is greater than 100, no more than 100 results are returned.

            Default: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPaymentRefundsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/refunds",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
                "location_id": location_id,
                "status": status,
                "source_type": source_type,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaymentRefundsResponse,
                    parse_obj_as(
                        type_=ListPaymentRefundsResponse,
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

    def refund_payment(
        self,
        *,
        amount_money: Money,
        idempotency_key: str,
        payment_id: str,
        app_fee_money: typing.Optional[Money] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RefundPaymentResponse]:
        """
        Refunds a payment. You can refund the entire payment amount or a
        portion of it. You can use this endpoint to refund a card payment or record a
        refund of a cash or external payment. For more information, see
        [Refund Payment](https://developer.squareup.com/docs/payments-api/refund-payments).

        Parameters
        ----------
        amount_money : Money

        idempotency_key : str
             A unique string that identifies this `RefundPayment` request. The key can be any valid string
            but must be unique for every `RefundPayment` request.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        payment_id : str
            The unique ID of the payment being refunded.

        app_fee_money : typing.Optional[Money]

        reason : typing.Optional[str]
            A description of the reason for the refund.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RefundPaymentResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/refunds",
            method="POST",
            json={
                "amount_money": convert_and_respect_annotation_metadata(
                    object_=amount_money, annotation=Money, direction="write"
                ),
                "app_fee_money": convert_and_respect_annotation_metadata(
                    object_=app_fee_money, annotation=Money, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "payment_id": payment_id,
                "reason": reason,
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
                    RefundPaymentResponse,
                    parse_obj_as(
                        type_=RefundPaymentResponse,
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

    def get_payment_refund(
        self, refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPaymentRefundResponse]:
        """
        Retrieves a specific refund using the `refund_id`.

        Parameters
        ----------
        refund_id : str
            The unique ID for the desired `PaymentRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPaymentRefundResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/refunds/{encode_path_param(refund_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPaymentRefundResponse,
                    parse_obj_as(
                        type_=GetPaymentRefundResponse,
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


class AsyncRawRefundsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_payment_refunds(
        self,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        source_type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListPaymentRefundsResponse]:
        """
        Retrieves a list of refunds for the account making the request.

        Results are eventually consistent, and new refunds or changes to refunds might take several
        seconds to appear.

        The maximum results per page is 100.

        Parameters
        ----------
        begin_time : typing.Optional[str]
            The timestamp for the beginning of the requested reporting period, in RFC 3339 format.

            Default: The current time minus one year.

        end_time : typing.Optional[str]
            The timestamp for the end of the requested reporting period, in RFC 3339 format.

            Default: The current time.

        sort_order : typing.Optional[str]
            The order in which results are listed:
            - `ASC` - Oldest to newest.
            - `DESC` - Newest to oldest (default).

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        location_id : typing.Optional[str]
            Limit results to the location supplied. By default, results are returned
            for all locations associated with the seller.

        status : typing.Optional[str]
            If provided, only refunds with the given status are returned.
            For a list of refund status values, see [PaymentRefund](https://developer.squareup.com/reference/square_2021-08-18/objects/PaymentRefund).

            Default: If omitted, refunds are returned regardless of their status.

        source_type : typing.Optional[str]
            If provided, only refunds with the given source type are returned.
            - `CARD` - List refunds only for payments where `CARD` was specified as the payment
            source.

            Default: If omitted, refunds are returned regardless of the source type.

        limit : typing.Optional[int]
            The maximum number of results to be returned in a single page.

            It is possible to receive fewer results than the specified limit on a given page.

            If the supplied value is greater than 100, no more than 100 results are returned.

            Default: 100

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPaymentRefundsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/refunds",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
                "location_id": location_id,
                "status": status,
                "source_type": source_type,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaymentRefundsResponse,
                    parse_obj_as(
                        type_=ListPaymentRefundsResponse,
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

    async def refund_payment(
        self,
        *,
        amount_money: Money,
        idempotency_key: str,
        payment_id: str,
        app_fee_money: typing.Optional[Money] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RefundPaymentResponse]:
        """
        Refunds a payment. You can refund the entire payment amount or a
        portion of it. You can use this endpoint to refund a card payment or record a
        refund of a cash or external payment. For more information, see
        [Refund Payment](https://developer.squareup.com/docs/payments-api/refund-payments).

        Parameters
        ----------
        amount_money : Money

        idempotency_key : str
             A unique string that identifies this `RefundPayment` request. The key can be any valid string
            but must be unique for every `RefundPayment` request.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        payment_id : str
            The unique ID of the payment being refunded.

        app_fee_money : typing.Optional[Money]

        reason : typing.Optional[str]
            A description of the reason for the refund.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RefundPaymentResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/refunds",
            method="POST",
            json={
                "amount_money": convert_and_respect_annotation_metadata(
                    object_=amount_money, annotation=Money, direction="write"
                ),
                "app_fee_money": convert_and_respect_annotation_metadata(
                    object_=app_fee_money, annotation=Money, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "payment_id": payment_id,
                "reason": reason,
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
                    RefundPaymentResponse,
                    parse_obj_as(
                        type_=RefundPaymentResponse,
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

    async def get_payment_refund(
        self, refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPaymentRefundResponse]:
        """
        Retrieves a specific refund using the `refund_id`.

        Parameters
        ----------
        refund_id : str
            The unique ID for the desired `PaymentRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPaymentRefundResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/refunds/{encode_path_param(refund_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPaymentRefundResponse,
                    parse_obj_as(
                        type_=GetPaymentRefundResponse,
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

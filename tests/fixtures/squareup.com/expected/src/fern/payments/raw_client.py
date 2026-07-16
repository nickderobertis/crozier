

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
from ..types.address import Address
from ..types.cancel_payment_by_idempotency_key_response import CancelPaymentByIdempotencyKeyResponse
from ..types.cancel_payment_response import CancelPaymentResponse
from ..types.cash_payment_details import CashPaymentDetails
from ..types.complete_payment_response import CompletePaymentResponse
from ..types.create_payment_response import CreatePaymentResponse
from ..types.external_payment_details import ExternalPaymentDetails
from ..types.get_payment_response import GetPaymentResponse
from ..types.list_payments_response import ListPaymentsResponse
from ..types.money import Money
from ..types.payment import Payment
from ..types.update_payment_response import UpdatePaymentResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPaymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_payments(
        self,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        total: typing.Optional[int] = None,
        last4: typing.Optional[str] = None,
        card_brand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPaymentsResponse]:
        """
        Retrieves a list of payments taken by the account making the request.

        Results are eventually consistent, and new payments or changes to payments might take several
        seconds to appear.

        The maximum results per page is 100.

        Parameters
        ----------
        begin_time : typing.Optional[str]
            The timestamp for the beginning of the reporting period, in RFC 3339 format.
            Inclusive. Default: The current time minus one year.

        end_time : typing.Optional[str]
            The timestamp for the end of the reporting period, in RFC 3339 format.

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
            for the default (main) location associated with the seller.

        total : typing.Optional[int]
            The exact amount in the `total_money` for a payment.

        last4 : typing.Optional[str]
            The last four digits of a payment card.

        card_brand : typing.Optional[str]
            The brand of the payment card (for example, VISA).

        limit : typing.Optional[int]
            The maximum number of results to be returned in a single page.
            It is possible to receive fewer results than the specified limit on a given page.

            The default value of 100 is also the maximum allowed value. If the provided value is
            greater than 100, it is ignored and the default value is used instead.

            Default: `100`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPaymentsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/payments",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
                "location_id": location_id,
                "total": total,
                "last_4": last4,
                "card_brand": card_brand,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaymentsResponse,
                    parse_obj_as(
                        type_=ListPaymentsResponse,
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

    def create_payment(
        self,
        *,
        amount_money: Money,
        idempotency_key: str,
        source_id: str,
        accept_partial_authorization: typing.Optional[bool] = OMIT,
        app_fee_money: typing.Optional[Money] = OMIT,
        autocomplete: typing.Optional[bool] = OMIT,
        billing_address: typing.Optional[Address] = OMIT,
        buyer_email_address: typing.Optional[str] = OMIT,
        cash_details: typing.Optional[CashPaymentDetails] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        delay_duration: typing.Optional[str] = OMIT,
        external_details: typing.Optional[ExternalPaymentDetails] = OMIT,
        location_id: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        order_id: typing.Optional[str] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        shipping_address: typing.Optional[Address] = OMIT,
        statement_description_identifier: typing.Optional[str] = OMIT,
        tip_money: typing.Optional[Money] = OMIT,
        verification_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatePaymentResponse]:
        """
        Creates a payment using the provided source. You can use this endpoint
        to charge a card (credit/debit card or
        Square gift card) or record a payment that the seller received outside of Square
        (cash payment from a buyer or a payment that an external entity
        processed on behalf of the seller).

        The endpoint creates a
        `Payment` object and returns it in the response.

        Parameters
        ----------
        amount_money : Money

        idempotency_key : str
            A unique string that identifies this `CreatePayment` request. Keys can be any valid string
            but must be unique for every `CreatePayment` request.

            Max: 45 characters

            Note: The number of allowed characters might be less than the stated maximum, if multi-byte
            characters are used.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        source_id : str
            The ID for the source of funds for this payment. This can be a payment token
            (card nonce) generated by the Square payment form or a card on file made with the
            Customers API. If recording a payment that the seller
            received outside of Square, specify either "CASH" or "EXTERNAL".
            For more information, see
            [Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).

        accept_partial_authorization : typing.Optional[bool]
            If set to `true` and charging a Square Gift Card, a payment might be returned with
            `amount_money` equal to less than what was requested. For example, a request for $20 when charging
            a Square Gift Card with a balance of $5 results in an APPROVED payment of $5. You might choose
            to prompt the buyer for an additional payment to cover the remainder or cancel the Gift Card
            payment. This field cannot be `true` when `autocomplete = true`.

            For more information, see
            [Partial amount with Square Gift Cards](https://developer.squareup.com/docs/payments-api/take-payments#partial-payment-gift-card).

            Default: false

        app_fee_money : typing.Optional[Money]

        autocomplete : typing.Optional[bool]
            If set to `true`, this payment will be completed when possible. If
            set to `false`, this payment is held in an approved state until either
            explicitly completed (captured) or canceled (voided). For more information, see
            [Delayed capture](https://developer.squareup.com/docs/payments-api/take-payments/card-payments#delayed-capture-of-a-card-payment).

            Default: true

        billing_address : typing.Optional[Address]

        buyer_email_address : typing.Optional[str]
            The buyer's email address.

        cash_details : typing.Optional[CashPaymentDetails]

        customer_id : typing.Optional[str]
            The [Customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) ID of the customer associated with the payment.

            This is required if the `source_id` refers to a card on file created using the Customers API.

        delay_duration : typing.Optional[str]
            The duration of time after the payment's creation when Square automatically cancels the
            payment. This automatic cancellation applies only to payments that do not reach a terminal state
            (COMPLETED, CANCELED, or FAILED) before the `delay_duration` time period.

            This parameter should be specified as a time duration, in RFC 3339 format, with a minimum value
            of 1 minute.

            Note: This feature is only supported for card payments. This parameter can only be set for a delayed
            capture payment (`autocomplete=false`).

            Default:

            - Card-present payments: "PT36H" (36 hours) from the creation time.
            - Card-not-present payments: "P7D" (7 days) from the creation time.

        external_details : typing.Optional[ExternalPaymentDetails]

        location_id : typing.Optional[str]
            The location ID to associate with the payment. If not specified, the default location is
            used.

        note : typing.Optional[str]
            An optional note to be entered by the developer when creating a payment.

            Limit 500 characters.

        order_id : typing.Optional[str]
            Associates a previously created order with this payment.

        reference_id : typing.Optional[str]
            A user-defined ID to associate with the payment.

            You can use this field to associate the payment to an entity in an external system
            (for example, you might specify an order ID that is generated by a third-party shopping cart).

            Limit 40 characters.

        shipping_address : typing.Optional[Address]

        statement_description_identifier : typing.Optional[str]
            Optional additional payment information to include on the customer's card statement
            as part of the statement description. This can be, for example, an invoice number, ticket number,
            or short description that uniquely identifies the purchase.

            Note that the `statement_description_identifier` might get truncated on the statement description
            to fit the required information including the Square identifier (SQ *) and name of the
            seller taking the payment.

        tip_money : typing.Optional[Money]

        verification_token : typing.Optional[str]
            An identifying token generated by [payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
            Verification tokens encapsulate customer device information and 3-D Secure
            challenge results to indicate that Square has verified the buyer identity.

            For more information, see [SCA Overview](https://developer.squareup.com/docs/sca-overview).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreatePaymentResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/payments",
            method="POST",
            json={
                "accept_partial_authorization": accept_partial_authorization,
                "amount_money": convert_and_respect_annotation_metadata(
                    object_=amount_money, annotation=Money, direction="write"
                ),
                "app_fee_money": convert_and_respect_annotation_metadata(
                    object_=app_fee_money, annotation=Money, direction="write"
                ),
                "autocomplete": autocomplete,
                "billing_address": convert_and_respect_annotation_metadata(
                    object_=billing_address, annotation=Address, direction="write"
                ),
                "buyer_email_address": buyer_email_address,
                "cash_details": convert_and_respect_annotation_metadata(
                    object_=cash_details, annotation=CashPaymentDetails, direction="write"
                ),
                "customer_id": customer_id,
                "delay_duration": delay_duration,
                "external_details": convert_and_respect_annotation_metadata(
                    object_=external_details, annotation=ExternalPaymentDetails, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "location_id": location_id,
                "note": note,
                "order_id": order_id,
                "reference_id": reference_id,
                "shipping_address": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=Address, direction="write"
                ),
                "source_id": source_id,
                "statement_description_identifier": statement_description_identifier,
                "tip_money": convert_and_respect_annotation_metadata(
                    object_=tip_money, annotation=Money, direction="write"
                ),
                "verification_token": verification_token,
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
                    CreatePaymentResponse,
                    parse_obj_as(
                        type_=CreatePaymentResponse,
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

    def cancel_payment_by_idempotency_key(
        self, *, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelPaymentByIdempotencyKeyResponse]:
        """
        Cancels (voids) a payment identified by the idempotency key that is specified in the
        request.

        Use this method when the status of a `CreatePayment` request is unknown (for example, after you send a
        `CreatePayment` request, a network error occurs and you do not get a response). In this case, you can
        direct Square to cancel the payment using this endpoint. In the request, you provide the same
        idempotency key that you provided in your `CreatePayment` request that you want to cancel. After
        canceling the payment, you can submit your `CreatePayment` request again.

        Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint
        returns successfully.

        Parameters
        ----------
        idempotency_key : str
            The `idempotency_key` identifying the payment to be canceled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CancelPaymentByIdempotencyKeyResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/payments/cancel",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
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
                    CancelPaymentByIdempotencyKeyResponse,
                    parse_obj_as(
                        type_=CancelPaymentByIdempotencyKeyResponse,
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

    def get_payment(
        self, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPaymentResponse]:
        """
        Retrieves details for a specific payment.

        Parameters
        ----------
        payment_id : str
            A unique ID for the desired payment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPaymentResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/payments/{encode_path_param(payment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPaymentResponse,
                    parse_obj_as(
                        type_=GetPaymentResponse,
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

    def update_payment(
        self,
        payment_id: str,
        *,
        idempotency_key: str,
        payment: typing.Optional[Payment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdatePaymentResponse]:
        """
        Updates a payment with the APPROVED status.
        You can update the `amount_money` and `tip_money` using this endpoint.

        Parameters
        ----------
        payment_id : str
            The ID of the payment to update.

        idempotency_key : str
            A unique string that identifies this `UpdatePayment` request. Keys can be any valid string
            but must be unique for every `UpdatePayment` request.

            The maximum is 45 characters.

            For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

        payment : typing.Optional[Payment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdatePaymentResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/payments/{encode_path_param(payment_id)}",
            method="PUT",
            json={
                "idempotency_key": idempotency_key,
                "payment": convert_and_respect_annotation_metadata(
                    object_=payment, annotation=Payment, direction="write"
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
                    UpdatePaymentResponse,
                    parse_obj_as(
                        type_=UpdatePaymentResponse,
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

    def cancel_payment(
        self, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelPaymentResponse]:
        """
        Cancels (voids) a payment. You can use this endpoint to cancel a payment with
        the APPROVED `status`.

        Parameters
        ----------
        payment_id : str
            The ID of the payment to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CancelPaymentResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/payments/{encode_path_param(payment_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelPaymentResponse,
                    parse_obj_as(
                        type_=CancelPaymentResponse,
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

    def complete_payment(
        self, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CompletePaymentResponse]:
        """
        Completes (captures) a payment.
        By default, payments are set to complete immediately after they are created.

        You can use this endpoint to complete a payment with the APPROVED `status`.

        Parameters
        ----------
        payment_id : str
            The unique ID identifying the payment to be completed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompletePaymentResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/payments/{encode_path_param(payment_id)}/complete",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CompletePaymentResponse,
                    parse_obj_as(
                        type_=CompletePaymentResponse,
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


class AsyncRawPaymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_payments(
        self,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        total: typing.Optional[int] = None,
        last4: typing.Optional[str] = None,
        card_brand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListPaymentsResponse]:
        """
        Retrieves a list of payments taken by the account making the request.

        Results are eventually consistent, and new payments or changes to payments might take several
        seconds to appear.

        The maximum results per page is 100.

        Parameters
        ----------
        begin_time : typing.Optional[str]
            The timestamp for the beginning of the reporting period, in RFC 3339 format.
            Inclusive. Default: The current time minus one year.

        end_time : typing.Optional[str]
            The timestamp for the end of the reporting period, in RFC 3339 format.

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
            for the default (main) location associated with the seller.

        total : typing.Optional[int]
            The exact amount in the `total_money` for a payment.

        last4 : typing.Optional[str]
            The last four digits of a payment card.

        card_brand : typing.Optional[str]
            The brand of the payment card (for example, VISA).

        limit : typing.Optional[int]
            The maximum number of results to be returned in a single page.
            It is possible to receive fewer results than the specified limit on a given page.

            The default value of 100 is also the maximum allowed value. If the provided value is
            greater than 100, it is ignored and the default value is used instead.

            Default: `100`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPaymentsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/payments",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
                "location_id": location_id,
                "total": total,
                "last_4": last4,
                "card_brand": card_brand,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaymentsResponse,
                    parse_obj_as(
                        type_=ListPaymentsResponse,
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

    async def create_payment(
        self,
        *,
        amount_money: Money,
        idempotency_key: str,
        source_id: str,
        accept_partial_authorization: typing.Optional[bool] = OMIT,
        app_fee_money: typing.Optional[Money] = OMIT,
        autocomplete: typing.Optional[bool] = OMIT,
        billing_address: typing.Optional[Address] = OMIT,
        buyer_email_address: typing.Optional[str] = OMIT,
        cash_details: typing.Optional[CashPaymentDetails] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        delay_duration: typing.Optional[str] = OMIT,
        external_details: typing.Optional[ExternalPaymentDetails] = OMIT,
        location_id: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        order_id: typing.Optional[str] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        shipping_address: typing.Optional[Address] = OMIT,
        statement_description_identifier: typing.Optional[str] = OMIT,
        tip_money: typing.Optional[Money] = OMIT,
        verification_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreatePaymentResponse]:
        """
        Creates a payment using the provided source. You can use this endpoint
        to charge a card (credit/debit card or
        Square gift card) or record a payment that the seller received outside of Square
        (cash payment from a buyer or a payment that an external entity
        processed on behalf of the seller).

        The endpoint creates a
        `Payment` object and returns it in the response.

        Parameters
        ----------
        amount_money : Money

        idempotency_key : str
            A unique string that identifies this `CreatePayment` request. Keys can be any valid string
            but must be unique for every `CreatePayment` request.

            Max: 45 characters

            Note: The number of allowed characters might be less than the stated maximum, if multi-byte
            characters are used.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        source_id : str
            The ID for the source of funds for this payment. This can be a payment token
            (card nonce) generated by the Square payment form or a card on file made with the
            Customers API. If recording a payment that the seller
            received outside of Square, specify either "CASH" or "EXTERNAL".
            For more information, see
            [Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).

        accept_partial_authorization : typing.Optional[bool]
            If set to `true` and charging a Square Gift Card, a payment might be returned with
            `amount_money` equal to less than what was requested. For example, a request for $20 when charging
            a Square Gift Card with a balance of $5 results in an APPROVED payment of $5. You might choose
            to prompt the buyer for an additional payment to cover the remainder or cancel the Gift Card
            payment. This field cannot be `true` when `autocomplete = true`.

            For more information, see
            [Partial amount with Square Gift Cards](https://developer.squareup.com/docs/payments-api/take-payments#partial-payment-gift-card).

            Default: false

        app_fee_money : typing.Optional[Money]

        autocomplete : typing.Optional[bool]
            If set to `true`, this payment will be completed when possible. If
            set to `false`, this payment is held in an approved state until either
            explicitly completed (captured) or canceled (voided). For more information, see
            [Delayed capture](https://developer.squareup.com/docs/payments-api/take-payments/card-payments#delayed-capture-of-a-card-payment).

            Default: true

        billing_address : typing.Optional[Address]

        buyer_email_address : typing.Optional[str]
            The buyer's email address.

        cash_details : typing.Optional[CashPaymentDetails]

        customer_id : typing.Optional[str]
            The [Customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) ID of the customer associated with the payment.

            This is required if the `source_id` refers to a card on file created using the Customers API.

        delay_duration : typing.Optional[str]
            The duration of time after the payment's creation when Square automatically cancels the
            payment. This automatic cancellation applies only to payments that do not reach a terminal state
            (COMPLETED, CANCELED, or FAILED) before the `delay_duration` time period.

            This parameter should be specified as a time duration, in RFC 3339 format, with a minimum value
            of 1 minute.

            Note: This feature is only supported for card payments. This parameter can only be set for a delayed
            capture payment (`autocomplete=false`).

            Default:

            - Card-present payments: "PT36H" (36 hours) from the creation time.
            - Card-not-present payments: "P7D" (7 days) from the creation time.

        external_details : typing.Optional[ExternalPaymentDetails]

        location_id : typing.Optional[str]
            The location ID to associate with the payment. If not specified, the default location is
            used.

        note : typing.Optional[str]
            An optional note to be entered by the developer when creating a payment.

            Limit 500 characters.

        order_id : typing.Optional[str]
            Associates a previously created order with this payment.

        reference_id : typing.Optional[str]
            A user-defined ID to associate with the payment.

            You can use this field to associate the payment to an entity in an external system
            (for example, you might specify an order ID that is generated by a third-party shopping cart).

            Limit 40 characters.

        shipping_address : typing.Optional[Address]

        statement_description_identifier : typing.Optional[str]
            Optional additional payment information to include on the customer's card statement
            as part of the statement description. This can be, for example, an invoice number, ticket number,
            or short description that uniquely identifies the purchase.

            Note that the `statement_description_identifier` might get truncated on the statement description
            to fit the required information including the Square identifier (SQ *) and name of the
            seller taking the payment.

        tip_money : typing.Optional[Money]

        verification_token : typing.Optional[str]
            An identifying token generated by [payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
            Verification tokens encapsulate customer device information and 3-D Secure
            challenge results to indicate that Square has verified the buyer identity.

            For more information, see [SCA Overview](https://developer.squareup.com/docs/sca-overview).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreatePaymentResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/payments",
            method="POST",
            json={
                "accept_partial_authorization": accept_partial_authorization,
                "amount_money": convert_and_respect_annotation_metadata(
                    object_=amount_money, annotation=Money, direction="write"
                ),
                "app_fee_money": convert_and_respect_annotation_metadata(
                    object_=app_fee_money, annotation=Money, direction="write"
                ),
                "autocomplete": autocomplete,
                "billing_address": convert_and_respect_annotation_metadata(
                    object_=billing_address, annotation=Address, direction="write"
                ),
                "buyer_email_address": buyer_email_address,
                "cash_details": convert_and_respect_annotation_metadata(
                    object_=cash_details, annotation=CashPaymentDetails, direction="write"
                ),
                "customer_id": customer_id,
                "delay_duration": delay_duration,
                "external_details": convert_and_respect_annotation_metadata(
                    object_=external_details, annotation=ExternalPaymentDetails, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "location_id": location_id,
                "note": note,
                "order_id": order_id,
                "reference_id": reference_id,
                "shipping_address": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=Address, direction="write"
                ),
                "source_id": source_id,
                "statement_description_identifier": statement_description_identifier,
                "tip_money": convert_and_respect_annotation_metadata(
                    object_=tip_money, annotation=Money, direction="write"
                ),
                "verification_token": verification_token,
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
                    CreatePaymentResponse,
                    parse_obj_as(
                        type_=CreatePaymentResponse,
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

    async def cancel_payment_by_idempotency_key(
        self, *, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelPaymentByIdempotencyKeyResponse]:
        """
        Cancels (voids) a payment identified by the idempotency key that is specified in the
        request.

        Use this method when the status of a `CreatePayment` request is unknown (for example, after you send a
        `CreatePayment` request, a network error occurs and you do not get a response). In this case, you can
        direct Square to cancel the payment using this endpoint. In the request, you provide the same
        idempotency key that you provided in your `CreatePayment` request that you want to cancel. After
        canceling the payment, you can submit your `CreatePayment` request again.

        Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint
        returns successfully.

        Parameters
        ----------
        idempotency_key : str
            The `idempotency_key` identifying the payment to be canceled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CancelPaymentByIdempotencyKeyResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/payments/cancel",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
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
                    CancelPaymentByIdempotencyKeyResponse,
                    parse_obj_as(
                        type_=CancelPaymentByIdempotencyKeyResponse,
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

    async def get_payment(
        self, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPaymentResponse]:
        """
        Retrieves details for a specific payment.

        Parameters
        ----------
        payment_id : str
            A unique ID for the desired payment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPaymentResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/payments/{encode_path_param(payment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPaymentResponse,
                    parse_obj_as(
                        type_=GetPaymentResponse,
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

    async def update_payment(
        self,
        payment_id: str,
        *,
        idempotency_key: str,
        payment: typing.Optional[Payment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdatePaymentResponse]:
        """
        Updates a payment with the APPROVED status.
        You can update the `amount_money` and `tip_money` using this endpoint.

        Parameters
        ----------
        payment_id : str
            The ID of the payment to update.

        idempotency_key : str
            A unique string that identifies this `UpdatePayment` request. Keys can be any valid string
            but must be unique for every `UpdatePayment` request.

            The maximum is 45 characters.

            For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

        payment : typing.Optional[Payment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdatePaymentResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/payments/{encode_path_param(payment_id)}",
            method="PUT",
            json={
                "idempotency_key": idempotency_key,
                "payment": convert_and_respect_annotation_metadata(
                    object_=payment, annotation=Payment, direction="write"
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
                    UpdatePaymentResponse,
                    parse_obj_as(
                        type_=UpdatePaymentResponse,
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

    async def cancel_payment(
        self, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelPaymentResponse]:
        """
        Cancels (voids) a payment. You can use this endpoint to cancel a payment with
        the APPROVED `status`.

        Parameters
        ----------
        payment_id : str
            The ID of the payment to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CancelPaymentResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/payments/{encode_path_param(payment_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelPaymentResponse,
                    parse_obj_as(
                        type_=CancelPaymentResponse,
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

    async def complete_payment(
        self, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CompletePaymentResponse]:
        """
        Completes (captures) a payment.
        By default, payments are set to complete immediately after they are created.

        You can use this endpoint to complete a payment with the APPROVED `status`.

        Parameters
        ----------
        payment_id : str
            The unique ID identifying the payment to be completed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompletePaymentResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/payments/{encode_path_param(payment_id)}/complete",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CompletePaymentResponse,
                    parse_obj_as(
                        type_=CompletePaymentResponse,
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

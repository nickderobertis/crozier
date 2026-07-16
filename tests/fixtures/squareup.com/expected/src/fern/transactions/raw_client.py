

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
from ..types.additional_recipient import AdditionalRecipient
from ..types.address import Address
from ..types.capture_transaction_response import CaptureTransactionResponse
from ..types.charge_response import ChargeResponse
from ..types.create_refund_response import CreateRefundResponse
from ..types.list_refunds_response import ListRefundsResponse
from ..types.list_transactions_response import ListTransactionsResponse
from ..types.money import Money
from ..types.retrieve_transaction_response import RetrieveTransactionResponse
from ..types.void_transaction_response import VoidTransactionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_refunds(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListRefundsResponse]:
        """
        Lists refunds for one of a business's locations.

        In addition to full or partial tender refunds processed through Square APIs,
        refunds may result from itemized returns or exchanges through Square's
        Point of Sale applications.

        Refunds with a `status` of `PENDING` are not currently included in this
        endpoint's response.

        Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

        Parameters
        ----------
        location_id : str
            The ID of the location to list refunds for.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time.

        sort_order : typing.Optional[str]
            The order in which results are listed in the response (`ASC` for
            oldest first, `DESC` for newest first).

            Default value: `DESC`

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListRefundsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/refunds",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRefundsResponse,
                    parse_obj_as(
                        type_=ListRefundsResponse,
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

    def list_transactions(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTransactionsResponse]:
        """
        Lists transactions for a particular location.

        Transactions include payment information from sales and exchanges and refund
        information from returns and exchanges.

        Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

        Parameters
        ----------
        location_id : str
            The ID of the location to list transactions for.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time.

        sort_order : typing.Optional[str]
            The order in which results are listed in the response (`ASC` for
            oldest first, `DESC` for newest first).

            Default value: `DESC`

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTransactionsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTransactionsResponse,
                    parse_obj_as(
                        type_=ListTransactionsResponse,
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

    def charge(
        self,
        location_id: str,
        *,
        amount_money: Money,
        idempotency_key: str,
        additional_recipients: typing.Optional[typing.Sequence[AdditionalRecipient]] = OMIT,
        billing_address: typing.Optional[Address] = OMIT,
        buyer_email_address: typing.Optional[str] = OMIT,
        card_nonce: typing.Optional[str] = OMIT,
        customer_card_id: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        delay_capture: typing.Optional[bool] = OMIT,
        note: typing.Optional[str] = OMIT,
        order_id: typing.Optional[str] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        shipping_address: typing.Optional[Address] = OMIT,
        verification_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChargeResponse]:
        """
        Charges a card represented by a card nonce or a customer's card on file.

        Your request to this endpoint must include _either_:

        - A value for the `card_nonce` parameter (to charge a card payment token generated
        with the Web Payments SDK)
        - Values for the `customer_card_id` and `customer_id` parameters (to charge
        a customer's card on file)

        In order for an eCommerce payment to potentially qualify for
        [Square chargeback protection](https://squareup.com/help/article/5394), you
        _must_ provide values for the following parameters in your request:

        - `buyer_email_address`
        - At least one of `billing_address` or `shipping_address`

        When this response is returned, the amount of Square's processing fee might not yet be
        calculated. To obtain the processing fee, wait about ten seconds and call
        [RetrieveTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/retrieve-transaction). See the `processing_fee_money`
        field of each [Tender included](https://developer.squareup.com/reference/square_2021-08-18/objects/Tender) in the transaction.

        Parameters
        ----------
        location_id : str
            The ID of the location to associate the created transaction with.

        amount_money : Money

        idempotency_key : str
            A value you specify that uniquely identifies this
            transaction among transactions you've created.

            If you're unsure whether a particular transaction succeeded,
            you can reattempt it with the same idempotency key without
            worrying about double-charging the buyer.

            See [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency) for more information.

        additional_recipients : typing.Optional[typing.Sequence[AdditionalRecipient]]
            The basic primitive of multi-party transaction. The value is optional.
            The transaction facilitated by you can be split from here.

            If you provide this value, the `amount_money` value in your additional_recipients
            must not be more than 90% of the `amount_money` value in the charge request.
            The `location_id` must be the valid location of the app owner merchant.

            This field requires the `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.

            This field is currently not supported in sandbox.

        billing_address : typing.Optional[Address]

        buyer_email_address : typing.Optional[str]
            The buyer's email address, if available. This value is optional,
            but this transaction is ineligible for chargeback protection if it is not
            provided.

        card_nonce : typing.Optional[str]
            A payment token generated from the [Card.tokenize()](https://developer.squareup.com/reference/sdks/web/payments/objects/Card#Card.tokenize) that represents the card
            to charge.

            The application that provides a payment token to this endpoint must be the
            _same application_ that generated the payment token with the Web Payments SDK.
            Otherwise, the nonce is invalid.

            Do not provide a value for this field if you provide a value for
            `customer_card_id`.

        customer_card_id : typing.Optional[str]
            The ID of the customer card on file to charge. Do
            not provide a value for this field if you provide a value for `card_nonce`.

            If you provide this value, you _must_ also provide a value for
            `customer_id`.

        customer_id : typing.Optional[str]
            The ID of the customer to associate this transaction with. This field
            is required if you provide a value for `customer_card_id`, and optional
            otherwise.

        delay_capture : typing.Optional[bool]
            If `true`, the request will only perform an Auth on the provided
            card. You can then later perform either a Capture (with the
            [CaptureTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/capture-transaction) endpoint) or a Void
            (with the [VoidTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/void-transaction) endpoint).

            Default value: `false`

        note : typing.Optional[str]
            An optional note to associate with the transaction.

            This value cannot exceed 60 characters.

        order_id : typing.Optional[str]
            The ID of the order to associate with this transaction.

            If you provide this value, the `amount_money` value of your request must
            __exactly match__ the value of the order's `total_money` field.

        reference_id : typing.Optional[str]
            An optional ID you can associate with the transaction for your own
            purposes (such as to associate the transaction with an entity ID in your
            own database).

            This value cannot exceed 40 characters.

        shipping_address : typing.Optional[Address]

        verification_token : typing.Optional[str]
            A token generated by SqPaymentForm's verifyBuyer() that represents
            customer's device info and 3ds challenge result.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChargeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions",
            method="POST",
            json={
                "additional_recipients": convert_and_respect_annotation_metadata(
                    object_=additional_recipients, annotation=typing.Sequence[AdditionalRecipient], direction="write"
                ),
                "amount_money": convert_and_respect_annotation_metadata(
                    object_=amount_money, annotation=Money, direction="write"
                ),
                "billing_address": convert_and_respect_annotation_metadata(
                    object_=billing_address, annotation=Address, direction="write"
                ),
                "buyer_email_address": buyer_email_address,
                "card_nonce": card_nonce,
                "customer_card_id": customer_card_id,
                "customer_id": customer_id,
                "delay_capture": delay_capture,
                "idempotency_key": idempotency_key,
                "note": note,
                "order_id": order_id,
                "reference_id": reference_id,
                "shipping_address": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=Address, direction="write"
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
                    ChargeResponse,
                    parse_obj_as(
                        type_=ChargeResponse,
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

    def retrieve_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveTransactionResponse]:
        """
        Retrieves details for a single transaction.

        Parameters
        ----------
        location_id : str
            The ID of the transaction's associated location.

        transaction_id : str
            The ID of the transaction to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveTransactionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions/{encode_path_param(transaction_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveTransactionResponse,
                    parse_obj_as(
                        type_=RetrieveTransactionResponse,
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

    def capture_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CaptureTransactionResponse]:
        """
        Captures a transaction that was created with the [Charge](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/charge)
        endpoint with a `delay_capture` value of `true`.


        See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
        for more information.

        Parameters
        ----------
        location_id : str


        transaction_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaptureTransactionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions/{encode_path_param(transaction_id)}/capture",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaptureTransactionResponse,
                    parse_obj_as(
                        type_=CaptureTransactionResponse,
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
        transaction_id: str,
        *,
        amount_money: Money,
        idempotency_key: str,
        tender_id: str,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateRefundResponse]:
        """
        Initiates a refund for a previously charged tender.

        You must issue a refund within 120 days of the associated payment. See
        [this article](https://squareup.com/help/us/en/article/5060) for more information
        on refund behavior.

        NOTE: Card-present transactions with Interac credit cards **cannot be
        refunded using the Connect API**. Interac transactions must refunded
        in-person (e.g., dipping the card using POS app).

        Parameters
        ----------
        location_id : str
            The ID of the original transaction's associated location.

        transaction_id : str
            The ID of the original transaction that includes the tender to refund.

        amount_money : Money

        idempotency_key : str
            A value you specify that uniquely identifies this
            refund among refunds you've created for the tender.

            If you're unsure whether a particular refund succeeded,
            you can reattempt it with the same idempotency key without
            worrying about duplicating the refund.

            See [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency) for more information.

        tender_id : str
            The ID of the tender to refund.

            A [`Transaction`](https://developer.squareup.com/reference/square_2021-08-18/objects/Transaction) has one or more `tenders` (i.e., methods
            of payment) associated with it, and you refund each tender separately with
            the Connect API.

        reason : typing.Optional[str]
            A description of the reason for the refund.

            Default value: `Refund via API`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateRefundResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions/{encode_path_param(transaction_id)}/refund",
            method="POST",
            json={
                "amount_money": convert_and_respect_annotation_metadata(
                    object_=amount_money, annotation=Money, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "reason": reason,
                "tender_id": tender_id,
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
                    CreateRefundResponse,
                    parse_obj_as(
                        type_=CreateRefundResponse,
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

    def void_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoidTransactionResponse]:
        """
        Cancels a transaction that was created with the [Charge](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/charge)
        endpoint with a `delay_capture` value of `true`.


        See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
        for more information.

        Parameters
        ----------
        location_id : str


        transaction_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoidTransactionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions/{encode_path_param(transaction_id)}/void",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoidTransactionResponse,
                    parse_obj_as(
                        type_=VoidTransactionResponse,
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


class AsyncRawTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_refunds(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListRefundsResponse]:
        """
        Lists refunds for one of a business's locations.

        In addition to full or partial tender refunds processed through Square APIs,
        refunds may result from itemized returns or exchanges through Square's
        Point of Sale applications.

        Refunds with a `status` of `PENDING` are not currently included in this
        endpoint's response.

        Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

        Parameters
        ----------
        location_id : str
            The ID of the location to list refunds for.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time.

        sort_order : typing.Optional[str]
            The order in which results are listed in the response (`ASC` for
            oldest first, `DESC` for newest first).

            Default value: `DESC`

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListRefundsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/refunds",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRefundsResponse,
                    parse_obj_as(
                        type_=ListRefundsResponse,
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

    async def list_transactions(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTransactionsResponse]:
        """
        Lists transactions for a particular location.

        Transactions include payment information from sales and exchanges and refund
        information from returns and exchanges.

        Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

        Parameters
        ----------
        location_id : str
            The ID of the location to list transactions for.

        begin_time : typing.Optional[str]
            The beginning of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time minus one year.

        end_time : typing.Optional[str]
            The end of the requested reporting period, in RFC 3339 format.

            See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

            Default value: The current time.

        sort_order : typing.Optional[str]
            The order in which results are listed in the response (`ASC` for
            oldest first, `DESC` for newest first).

            Default value: `DESC`

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTransactionsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions",
            method="GET",
            params={
                "begin_time": begin_time,
                "end_time": end_time,
                "sort_order": sort_order,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTransactionsResponse,
                    parse_obj_as(
                        type_=ListTransactionsResponse,
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

    async def charge(
        self,
        location_id: str,
        *,
        amount_money: Money,
        idempotency_key: str,
        additional_recipients: typing.Optional[typing.Sequence[AdditionalRecipient]] = OMIT,
        billing_address: typing.Optional[Address] = OMIT,
        buyer_email_address: typing.Optional[str] = OMIT,
        card_nonce: typing.Optional[str] = OMIT,
        customer_card_id: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        delay_capture: typing.Optional[bool] = OMIT,
        note: typing.Optional[str] = OMIT,
        order_id: typing.Optional[str] = OMIT,
        reference_id: typing.Optional[str] = OMIT,
        shipping_address: typing.Optional[Address] = OMIT,
        verification_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChargeResponse]:
        """
        Charges a card represented by a card nonce or a customer's card on file.

        Your request to this endpoint must include _either_:

        - A value for the `card_nonce` parameter (to charge a card payment token generated
        with the Web Payments SDK)
        - Values for the `customer_card_id` and `customer_id` parameters (to charge
        a customer's card on file)

        In order for an eCommerce payment to potentially qualify for
        [Square chargeback protection](https://squareup.com/help/article/5394), you
        _must_ provide values for the following parameters in your request:

        - `buyer_email_address`
        - At least one of `billing_address` or `shipping_address`

        When this response is returned, the amount of Square's processing fee might not yet be
        calculated. To obtain the processing fee, wait about ten seconds and call
        [RetrieveTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/retrieve-transaction). See the `processing_fee_money`
        field of each [Tender included](https://developer.squareup.com/reference/square_2021-08-18/objects/Tender) in the transaction.

        Parameters
        ----------
        location_id : str
            The ID of the location to associate the created transaction with.

        amount_money : Money

        idempotency_key : str
            A value you specify that uniquely identifies this
            transaction among transactions you've created.

            If you're unsure whether a particular transaction succeeded,
            you can reattempt it with the same idempotency key without
            worrying about double-charging the buyer.

            See [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency) for more information.

        additional_recipients : typing.Optional[typing.Sequence[AdditionalRecipient]]
            The basic primitive of multi-party transaction. The value is optional.
            The transaction facilitated by you can be split from here.

            If you provide this value, the `amount_money` value in your additional_recipients
            must not be more than 90% of the `amount_money` value in the charge request.
            The `location_id` must be the valid location of the app owner merchant.

            This field requires the `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.

            This field is currently not supported in sandbox.

        billing_address : typing.Optional[Address]

        buyer_email_address : typing.Optional[str]
            The buyer's email address, if available. This value is optional,
            but this transaction is ineligible for chargeback protection if it is not
            provided.

        card_nonce : typing.Optional[str]
            A payment token generated from the [Card.tokenize()](https://developer.squareup.com/reference/sdks/web/payments/objects/Card#Card.tokenize) that represents the card
            to charge.

            The application that provides a payment token to this endpoint must be the
            _same application_ that generated the payment token with the Web Payments SDK.
            Otherwise, the nonce is invalid.

            Do not provide a value for this field if you provide a value for
            `customer_card_id`.

        customer_card_id : typing.Optional[str]
            The ID of the customer card on file to charge. Do
            not provide a value for this field if you provide a value for `card_nonce`.

            If you provide this value, you _must_ also provide a value for
            `customer_id`.

        customer_id : typing.Optional[str]
            The ID of the customer to associate this transaction with. This field
            is required if you provide a value for `customer_card_id`, and optional
            otherwise.

        delay_capture : typing.Optional[bool]
            If `true`, the request will only perform an Auth on the provided
            card. You can then later perform either a Capture (with the
            [CaptureTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/capture-transaction) endpoint) or a Void
            (with the [VoidTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/void-transaction) endpoint).

            Default value: `false`

        note : typing.Optional[str]
            An optional note to associate with the transaction.

            This value cannot exceed 60 characters.

        order_id : typing.Optional[str]
            The ID of the order to associate with this transaction.

            If you provide this value, the `amount_money` value of your request must
            __exactly match__ the value of the order's `total_money` field.

        reference_id : typing.Optional[str]
            An optional ID you can associate with the transaction for your own
            purposes (such as to associate the transaction with an entity ID in your
            own database).

            This value cannot exceed 40 characters.

        shipping_address : typing.Optional[Address]

        verification_token : typing.Optional[str]
            A token generated by SqPaymentForm's verifyBuyer() that represents
            customer's device info and 3ds challenge result.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChargeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions",
            method="POST",
            json={
                "additional_recipients": convert_and_respect_annotation_metadata(
                    object_=additional_recipients, annotation=typing.Sequence[AdditionalRecipient], direction="write"
                ),
                "amount_money": convert_and_respect_annotation_metadata(
                    object_=amount_money, annotation=Money, direction="write"
                ),
                "billing_address": convert_and_respect_annotation_metadata(
                    object_=billing_address, annotation=Address, direction="write"
                ),
                "buyer_email_address": buyer_email_address,
                "card_nonce": card_nonce,
                "customer_card_id": customer_card_id,
                "customer_id": customer_id,
                "delay_capture": delay_capture,
                "idempotency_key": idempotency_key,
                "note": note,
                "order_id": order_id,
                "reference_id": reference_id,
                "shipping_address": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=Address, direction="write"
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
                    ChargeResponse,
                    parse_obj_as(
                        type_=ChargeResponse,
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

    async def retrieve_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveTransactionResponse]:
        """
        Retrieves details for a single transaction.

        Parameters
        ----------
        location_id : str
            The ID of the transaction's associated location.

        transaction_id : str
            The ID of the transaction to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveTransactionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions/{encode_path_param(transaction_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveTransactionResponse,
                    parse_obj_as(
                        type_=RetrieveTransactionResponse,
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

    async def capture_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CaptureTransactionResponse]:
        """
        Captures a transaction that was created with the [Charge](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/charge)
        endpoint with a `delay_capture` value of `true`.


        See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
        for more information.

        Parameters
        ----------
        location_id : str


        transaction_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaptureTransactionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions/{encode_path_param(transaction_id)}/capture",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaptureTransactionResponse,
                    parse_obj_as(
                        type_=CaptureTransactionResponse,
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
        transaction_id: str,
        *,
        amount_money: Money,
        idempotency_key: str,
        tender_id: str,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateRefundResponse]:
        """
        Initiates a refund for a previously charged tender.

        You must issue a refund within 120 days of the associated payment. See
        [this article](https://squareup.com/help/us/en/article/5060) for more information
        on refund behavior.

        NOTE: Card-present transactions with Interac credit cards **cannot be
        refunded using the Connect API**. Interac transactions must refunded
        in-person (e.g., dipping the card using POS app).

        Parameters
        ----------
        location_id : str
            The ID of the original transaction's associated location.

        transaction_id : str
            The ID of the original transaction that includes the tender to refund.

        amount_money : Money

        idempotency_key : str
            A value you specify that uniquely identifies this
            refund among refunds you've created for the tender.

            If you're unsure whether a particular refund succeeded,
            you can reattempt it with the same idempotency key without
            worrying about duplicating the refund.

            See [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency) for more information.

        tender_id : str
            The ID of the tender to refund.

            A [`Transaction`](https://developer.squareup.com/reference/square_2021-08-18/objects/Transaction) has one or more `tenders` (i.e., methods
            of payment) associated with it, and you refund each tender separately with
            the Connect API.

        reason : typing.Optional[str]
            A description of the reason for the refund.

            Default value: `Refund via API`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateRefundResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions/{encode_path_param(transaction_id)}/refund",
            method="POST",
            json={
                "amount_money": convert_and_respect_annotation_metadata(
                    object_=amount_money, annotation=Money, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "reason": reason,
                "tender_id": tender_id,
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
                    CreateRefundResponse,
                    parse_obj_as(
                        type_=CreateRefundResponse,
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

    async def void_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoidTransactionResponse]:
        """
        Cancels a transaction that was created with the [Charge](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/charge)
        endpoint with a `delay_capture` value of `true`.


        See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
        for more information.

        Parameters
        ----------
        location_id : str


        transaction_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoidTransactionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}/transactions/{encode_path_param(transaction_id)}/void",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoidTransactionResponse,
                    parse_obj_as(
                        type_=VoidTransactionResponse,
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

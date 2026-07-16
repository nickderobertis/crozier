

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawTransactionsClient, RawTransactionsClient


OMIT = typing.cast(typing.Any, ...)


class TransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransactionsClient
        """
        return self._raw_client

    def list_refunds(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRefundsResponse:
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
        ListRefundsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.transactions.list_refunds(
            location_id="location_id",
        )
        """
        _response = self._raw_client.list_refunds(
            location_id,
            begin_time=begin_time,
            end_time=end_time,
            sort_order=sort_order,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    def list_transactions(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTransactionsResponse:
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
        ListTransactionsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.transactions.list_transactions(
            location_id="location_id",
        )
        """
        _response = self._raw_client.list_transactions(
            location_id,
            begin_time=begin_time,
            end_time=end_time,
            sort_order=sort_order,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ChargeResponse:
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
        ChargeResponse
            Success

        Examples
        --------
        from fern import FernApi, Money

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.transactions.charge(
            location_id="location_id",
            amount_money=Money(),
            idempotency_key="idempotency_key",
        )
        """
        _response = self._raw_client.charge(
            location_id,
            amount_money=amount_money,
            idempotency_key=idempotency_key,
            additional_recipients=additional_recipients,
            billing_address=billing_address,
            buyer_email_address=buyer_email_address,
            card_nonce=card_nonce,
            customer_card_id=customer_card_id,
            customer_id=customer_id,
            delay_capture=delay_capture,
            note=note,
            order_id=order_id,
            reference_id=reference_id,
            shipping_address=shipping_address,
            verification_token=verification_token,
            request_options=request_options,
        )
        return _response.data

    def retrieve_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveTransactionResponse:
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
        RetrieveTransactionResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.transactions.retrieve_transaction(
            location_id="location_id",
            transaction_id="transaction_id",
        )
        """
        _response = self._raw_client.retrieve_transaction(location_id, transaction_id, request_options=request_options)
        return _response.data

    def capture_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaptureTransactionResponse:
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
        CaptureTransactionResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.transactions.capture_transaction(
            location_id="location_id",
            transaction_id="transaction_id",
        )
        """
        _response = self._raw_client.capture_transaction(location_id, transaction_id, request_options=request_options)
        return _response.data

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
    ) -> CreateRefundResponse:
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
        CreateRefundResponse
            Success

        Examples
        --------
        from fern import FernApi, Money

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.transactions.create_refund(
            location_id="location_id",
            transaction_id="transaction_id",
            amount_money=Money(),
            idempotency_key="idempotency_key",
            tender_id="tender_id",
        )
        """
        _response = self._raw_client.create_refund(
            location_id,
            transaction_id,
            amount_money=amount_money,
            idempotency_key=idempotency_key,
            tender_id=tender_id,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    def void_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoidTransactionResponse:
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
        VoidTransactionResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.transactions.void_transaction(
            location_id="location_id",
            transaction_id="transaction_id",
        )
        """
        _response = self._raw_client.void_transaction(location_id, transaction_id, request_options=request_options)
        return _response.data


class AsyncTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransactionsClient
        """
        return self._raw_client

    async def list_refunds(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRefundsResponse:
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
        ListRefundsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.list_refunds(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_refunds(
            location_id,
            begin_time=begin_time,
            end_time=end_time,
            sort_order=sort_order,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    async def list_transactions(
        self,
        location_id: str,
        *,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTransactionsResponse:
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
        ListTransactionsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.list_transactions(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_transactions(
            location_id,
            begin_time=begin_time,
            end_time=end_time,
            sort_order=sort_order,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ChargeResponse:
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
        ChargeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Money

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.charge(
                location_id="location_id",
                amount_money=Money(),
                idempotency_key="idempotency_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.charge(
            location_id,
            amount_money=amount_money,
            idempotency_key=idempotency_key,
            additional_recipients=additional_recipients,
            billing_address=billing_address,
            buyer_email_address=buyer_email_address,
            card_nonce=card_nonce,
            customer_card_id=customer_card_id,
            customer_id=customer_id,
            delay_capture=delay_capture,
            note=note,
            order_id=order_id,
            reference_id=reference_id,
            shipping_address=shipping_address,
            verification_token=verification_token,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveTransactionResponse:
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
        RetrieveTransactionResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.retrieve_transaction(
                location_id="location_id",
                transaction_id="transaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_transaction(
            location_id, transaction_id, request_options=request_options
        )
        return _response.data

    async def capture_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaptureTransactionResponse:
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
        CaptureTransactionResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.capture_transaction(
                location_id="location_id",
                transaction_id="transaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.capture_transaction(
            location_id, transaction_id, request_options=request_options
        )
        return _response.data

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
    ) -> CreateRefundResponse:
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
        CreateRefundResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Money

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.create_refund(
                location_id="location_id",
                transaction_id="transaction_id",
                amount_money=Money(),
                idempotency_key="idempotency_key",
                tender_id="tender_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_refund(
            location_id,
            transaction_id,
            amount_money=amount_money,
            idempotency_key=idempotency_key,
            tender_id=tender_id,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    async def void_transaction(
        self, location_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoidTransactionResponse:
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
        VoidTransactionResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transactions.void_transaction(
                location_id="location_id",
                transaction_id="transaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.void_transaction(
            location_id, transaction_id, request_options=request_options
        )
        return _response.data

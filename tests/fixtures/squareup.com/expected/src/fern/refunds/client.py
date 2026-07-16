

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_payment_refund_response import GetPaymentRefundResponse
from ..types.list_payment_refunds_response import ListPaymentRefundsResponse
from ..types.money import Money
from ..types.refund_payment_response import RefundPaymentResponse
from .raw_client import AsyncRawRefundsClient, RawRefundsClient


OMIT = typing.cast(typing.Any, ...)


class RefundsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRefundsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRefundsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRefundsClient
        """
        return self._raw_client

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
    ) -> ListPaymentRefundsResponse:
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
        ListPaymentRefundsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.refunds.list_payment_refunds()
        """
        _response = self._raw_client.list_payment_refunds(
            begin_time=begin_time,
            end_time=end_time,
            sort_order=sort_order,
            cursor=cursor,
            location_id=location_id,
            status=status,
            source_type=source_type,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def refund_payment(
        self,
        *,
        amount_money: Money,
        idempotency_key: str,
        payment_id: str,
        app_fee_money: typing.Optional[Money] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefundPaymentResponse:
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
        RefundPaymentResponse
            Success

        Examples
        --------
        from fern import FernApi, Money

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.refunds.refund_payment(
            amount_money=Money(),
            idempotency_key="idempotency_key",
            payment_id="payment_id",
        )
        """
        _response = self._raw_client.refund_payment(
            amount_money=amount_money,
            idempotency_key=idempotency_key,
            payment_id=payment_id,
            app_fee_money=app_fee_money,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    def get_payment_refund(
        self, refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPaymentRefundResponse:
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
        GetPaymentRefundResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.refunds.get_payment_refund(
            refund_id="refund_id",
        )
        """
        _response = self._raw_client.get_payment_refund(refund_id, request_options=request_options)
        return _response.data


class AsyncRefundsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRefundsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRefundsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRefundsClient
        """
        return self._raw_client

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
    ) -> ListPaymentRefundsResponse:
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
        ListPaymentRefundsResponse
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
            await client.refunds.list_payment_refunds()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_payment_refunds(
            begin_time=begin_time,
            end_time=end_time,
            sort_order=sort_order,
            cursor=cursor,
            location_id=location_id,
            status=status,
            source_type=source_type,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def refund_payment(
        self,
        *,
        amount_money: Money,
        idempotency_key: str,
        payment_id: str,
        app_fee_money: typing.Optional[Money] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefundPaymentResponse:
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
        RefundPaymentResponse
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
            await client.refunds.refund_payment(
                amount_money=Money(),
                idempotency_key="idempotency_key",
                payment_id="payment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refund_payment(
            amount_money=amount_money,
            idempotency_key=idempotency_key,
            payment_id=payment_id,
            app_fee_money=app_fee_money,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    async def get_payment_refund(
        self, refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPaymentRefundResponse:
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
        GetPaymentRefundResponse
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
            await client.refunds.get_payment_refund(
                refund_id="refund_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payment_refund(refund_id, request_options=request_options)
        return _response.data

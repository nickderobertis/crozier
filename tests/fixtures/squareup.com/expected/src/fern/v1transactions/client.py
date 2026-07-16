

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1money import V1Money
from ..types.v1order import V1Order
from ..types.v1payment import V1Payment
from ..types.v1refund import V1Refund
from ..types.v1settlement import V1Settlement
from .raw_client import AsyncRawV1TransactionsClient, RawV1TransactionsClient


OMIT = typing.cast(typing.Any, ...)


class V1TransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV1TransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV1TransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV1TransactionsClient
        """
        return self._raw_client

    def list_orders(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Order]:
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
        typing.List[V1Order]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1transactions.list_orders(
            location_id="location_id",
        )
        """
        _response = self._raw_client.list_orders(
            location_id, order=order, limit=limit, batch_token=batch_token, request_options=request_options
        )
        return _response.data

    def retrieve_order(
        self, location_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Order:
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
        V1Order
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1transactions.retrieve_order(
            location_id="location_id",
            order_id="order_id",
        )
        """
        _response = self._raw_client.retrieve_order(location_id, order_id, request_options=request_options)
        return _response.data

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
    ) -> V1Order:
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
        V1Order
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1transactions.update_order(
            location_id="location_id",
            order_id="order_id",
            action="action",
        )
        """
        _response = self._raw_client.update_order(
            location_id,
            order_id,
            action=action,
            canceled_note=canceled_note,
            completed_note=completed_note,
            refunded_note=refunded_note,
            shipped_tracking_number=shipped_tracking_number,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[V1Payment]:
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
        typing.List[V1Payment]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1transactions.list_payments(
            location_id="location_id",
        )
        """
        _response = self._raw_client.list_payments(
            location_id,
            order=order,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            batch_token=batch_token,
            include_partial=include_partial,
            request_options=request_options,
        )
        return _response.data

    def retrieve_payment(
        self, location_id: str, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Payment:
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
        V1Payment
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1transactions.retrieve_payment(
            location_id="location_id",
            payment_id="payment_id",
        )
        """
        _response = self._raw_client.retrieve_payment(location_id, payment_id, request_options=request_options)
        return _response.data

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
    ) -> typing.List[V1Refund]:
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
        typing.List[V1Refund]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1transactions.list_refunds(
            location_id="location_id",
        )
        """
        _response = self._raw_client.list_refunds(
            location_id,
            order=order,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            batch_token=batch_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> V1Refund:
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
        V1Refund
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1transactions.create_refund(
            location_id="location_id",
            payment_id="payment_id",
            reason="reason",
            type="type",
        )
        """
        _response = self._raw_client.create_refund(
            location_id,
            payment_id=payment_id,
            reason=reason,
            type=type,
            refunded_money=refunded_money,
            request_idempotence_key=request_idempotence_key,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[V1Settlement]:
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
        typing.List[V1Settlement]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1transactions.list_settlements(
            location_id="location_id",
        )
        """
        _response = self._raw_client.list_settlements(
            location_id,
            order=order,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            status=status,
            batch_token=batch_token,
            request_options=request_options,
        )
        return _response.data

    def retrieve_settlement(
        self, location_id: str, settlement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Settlement:
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
        V1Settlement
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.v1transactions.retrieve_settlement(
            location_id="location_id",
            settlement_id="settlement_id",
        )
        """
        _response = self._raw_client.retrieve_settlement(location_id, settlement_id, request_options=request_options)
        return _response.data


class AsyncV1TransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV1TransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV1TransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV1TransactionsClient
        """
        return self._raw_client

    async def list_orders(
        self,
        location_id: str,
        *,
        order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        batch_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Order]:
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
        typing.List[V1Order]
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
            await client.v1transactions.list_orders(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_orders(
            location_id, order=order, limit=limit, batch_token=batch_token, request_options=request_options
        )
        return _response.data

    async def retrieve_order(
        self, location_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Order:
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
        V1Order
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
            await client.v1transactions.retrieve_order(
                location_id="location_id",
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_order(location_id, order_id, request_options=request_options)
        return _response.data

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
    ) -> V1Order:
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
        V1Order
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
            await client.v1transactions.update_order(
                location_id="location_id",
                order_id="order_id",
                action="action",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_order(
            location_id,
            order_id,
            action=action,
            canceled_note=canceled_note,
            completed_note=completed_note,
            refunded_note=refunded_note,
            shipped_tracking_number=shipped_tracking_number,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[V1Payment]:
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
        typing.List[V1Payment]
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
            await client.v1transactions.list_payments(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_payments(
            location_id,
            order=order,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            batch_token=batch_token,
            include_partial=include_partial,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_payment(
        self, location_id: str, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Payment:
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
        V1Payment
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
            await client.v1transactions.retrieve_payment(
                location_id="location_id",
                payment_id="payment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_payment(location_id, payment_id, request_options=request_options)
        return _response.data

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
    ) -> typing.List[V1Refund]:
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
        typing.List[V1Refund]
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
            await client.v1transactions.list_refunds(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_refunds(
            location_id,
            order=order,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            batch_token=batch_token,
            request_options=request_options,
        )
        return _response.data

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
    ) -> V1Refund:
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
        V1Refund
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
            await client.v1transactions.create_refund(
                location_id="location_id",
                payment_id="payment_id",
                reason="reason",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_refund(
            location_id,
            payment_id=payment_id,
            reason=reason,
            type=type,
            refunded_money=refunded_money,
            request_idempotence_key=request_idempotence_key,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[V1Settlement]:
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
        typing.List[V1Settlement]
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
            await client.v1transactions.list_settlements(
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_settlements(
            location_id,
            order=order,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            status=status,
            batch_token=batch_token,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_settlement(
        self, location_id: str, settlement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Settlement:
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
        V1Settlement
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
            await client.v1transactions.retrieve_settlement(
                location_id="location_id",
                settlement_id="settlement_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_settlement(
            location_id, settlement_id, request_options=request_options
        )
        return _response.data

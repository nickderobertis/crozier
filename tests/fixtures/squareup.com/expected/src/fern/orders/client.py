

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.batch_retrieve_orders_response import BatchRetrieveOrdersResponse
from ..types.calculate_order_response import CalculateOrderResponse
from ..types.create_order_response import CreateOrderResponse
from ..types.order import Order
from ..types.order_reward import OrderReward
from ..types.pay_order_response import PayOrderResponse
from ..types.retrieve_order_response import RetrieveOrderResponse
from ..types.search_orders_query import SearchOrdersQuery
from ..types.search_orders_response import SearchOrdersResponse
from ..types.update_order_response import UpdateOrderResponse
from .raw_client import AsyncRawOrdersClient, RawOrdersClient


OMIT = typing.cast(typing.Any, ...)


class OrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrdersClient
        """
        return self._raw_client

    def create_order(
        self,
        *,
        idempotency_key: typing.Optional[str] = OMIT,
        order: typing.Optional[Order] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateOrderResponse:
        """
        Creates a new [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) that can include information about products for
        purchase and settings to apply to the purchase.

        To pay for a created order, see
        [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

        You can modify open orders using the [UpdateOrder](https://developer.squareup.com/reference/square_2021-08-18/orders-api/update-order) endpoint.

        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            A value you specify that uniquely identifies this
            order among orders you have created.

            If you are unsure whether a particular order was created successfully,
            you can try it again with the same idempotency key without
            worrying about creating duplicate orders.

            For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

        order : typing.Optional[Order]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateOrderResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.orders.create_order()
        """
        _response = self._raw_client.create_order(
            idempotency_key=idempotency_key, order=order, request_options=request_options
        )
        return _response.data

    def batch_retrieve_orders(
        self,
        *,
        order_ids: typing.Sequence[str],
        location_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchRetrieveOrdersResponse:
        """
        Retrieves a set of [orders](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by their IDs.

        If a given order ID does not exist, the ID is ignored instead of generating an error.

        Parameters
        ----------
        order_ids : typing.Sequence[str]
            The IDs of the orders to retrieve. A maximum of 100 orders can be retrieved per request.

        location_id : typing.Optional[str]
            The ID of the location for these orders. This field is optional: omit it to retrieve
            orders within the scope of the current authorization's merchant ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchRetrieveOrdersResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.orders.batch_retrieve_orders(
            order_ids=["order_ids"],
        )
        """
        _response = self._raw_client.batch_retrieve_orders(
            order_ids=order_ids, location_id=location_id, request_options=request_options
        )
        return _response.data

    def calculate_order(
        self,
        *,
        order: Order,
        proposed_rewards: typing.Optional[typing.Sequence[OrderReward]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalculateOrderResponse:
        """
        Enables applications to preview order pricing without creating an order.

        Parameters
        ----------
        order : Order

        proposed_rewards : typing.Optional[typing.Sequence[OrderReward]]
            Identifies one or more loyalty reward tiers to apply during the order calculation.
            The discounts defined by the reward tiers are added to the order only to preview the
            effect of applying the specified rewards. The rewards do not correspond to actual
            redemptions; that is, no `reward`s are created. Therefore, the reward `id`s are
            random strings used only to reference the reward tier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalculateOrderResponse
            Success

        Examples
        --------
        from fern import FernApi, Order

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.orders.calculate_order(
            order=Order(
                location_id="location_id",
            ),
        )
        """
        _response = self._raw_client.calculate_order(
            order=order, proposed_rewards=proposed_rewards, request_options=request_options
        )
        return _response.data

    def search_orders(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        query: typing.Optional[SearchOrdersQuery] = OMIT,
        return_entries: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchOrdersResponse:
        """
        Search all orders for one or more locations. Orders include all sales,
        returns, and exchanges regardless of how or when they entered the Square
        ecosystem (such as Point of Sale, Invoices, and Connect APIs).

        `SearchOrders` requests need to specify which locations to search and define a
        [SearchOrdersQuery](https://developer.squareup.com/reference/square_2021-08-18/objects/SearchOrdersQuery) object that controls
        how to sort or filter the results. Your `SearchOrdersQuery` can:

          Set filter criteria.
          Set the sort order.
          Determine whether to return results as complete `Order` objects or as
        [OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects.

        Note that details for orders processed with Square Point of Sale while in
        offline mode might not be transmitted to Square for up to 72 hours. Offline
        orders have a `created_at` value that reflects the time the order was created,
        not the time it was subsequently transmitted to Square.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        limit : typing.Optional[int]
            The maximum number of results to be returned in a single page. It is
            possible to receive fewer results than the specified limit on a given page.

            Default: `500`

        location_ids : typing.Optional[typing.Sequence[str]]
            The location IDs for the orders to query. All locations must belong to
            the same merchant.

            Min: 1 location ID.

            Max: 10 location IDs.

        query : typing.Optional[SearchOrdersQuery]

        return_entries : typing.Optional[bool]
            A Boolean that controls the format of the search results. If `true`,
            `SearchOrders` returns [OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects. If `false`, `SearchOrders`
            returns complete order objects.

            Default: `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchOrdersResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.orders.search_orders()
        """
        _response = self._raw_client.search_orders(
            cursor=cursor,
            limit=limit,
            location_ids=location_ids,
            query=query,
            return_entries=return_entries,
            request_options=request_options,
        )
        return _response.data

    def retrieve_order(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveOrderResponse:
        """
        Retrieves an [Order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by ID.

        Parameters
        ----------
        order_id : str
            The ID of the order to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveOrderResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.orders.retrieve_order(
            order_id="order_id",
        )
        """
        _response = self._raw_client.retrieve_order(order_id, request_options=request_options)
        return _response.data

    def update_order(
        self,
        order_id: str,
        *,
        fields_to_clear: typing.Optional[typing.Sequence[str]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        order: typing.Optional[Order] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateOrderResponse:
        """
        Updates an open [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by adding, replacing, or deleting
        fields. Orders with a `COMPLETED` or `CANCELED` state cannot be updated.

        An `UpdateOrder` request requires the following:

        - The `order_id` in the endpoint path, identifying the order to update.
        - The latest `version` of the order to update.
        - The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders#sparse-order-objects)
        containing only the fields to update and the version to which the update is
        being applied.
        - If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation)
        identifying the fields to clear.

        To pay for an order, see
        [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

        Parameters
        ----------
        order_id : str
            The ID of the order to update.

        fields_to_clear : typing.Optional[typing.Sequence[str]]
            The [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation)
            fields to clear. For example, `line_items[uid].note`.
            For more information, see [Deleting fields](https://developer.squareup.com/docs/orders-api/manage-orders#delete-fields).

        idempotency_key : typing.Optional[str]
            A value you specify that uniquely identifies this update request.

            If you are unsure whether a particular update was applied to an order successfully,
            you can reattempt it with the same idempotency key without
            worrying about creating duplicate updates to the order.
            The latest order version is returned.

            For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

        order : typing.Optional[Order]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateOrderResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.orders.update_order(
            order_id="order_id",
        )
        """
        _response = self._raw_client.update_order(
            order_id,
            fields_to_clear=fields_to_clear,
            idempotency_key=idempotency_key,
            order=order,
            request_options=request_options,
        )
        return _response.data

    def pay_order(
        self,
        order_id: str,
        *,
        idempotency_key: str,
        order_version: typing.Optional[int] = OMIT,
        payment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayOrderResponse:
        """
        Pay for an [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) using one or more approved [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment)
        or settle an order with a total of `0`.

        The total of the `payment_ids` listed in the request must be equal to the order
        total. Orders with a total amount of `0` can be marked as paid by specifying an empty
        array of `payment_ids` in the request.

        To be used with `PayOrder`, a payment must:

        - Reference the order by specifying the `order_id` when [creating the payment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/create-payment).
        Any approved payments that reference the same `order_id` not specified in the
        `payment_ids` is canceled.
        - Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments#delayed-capture).
        Using a delayed capture payment with `PayOrder` completes the approved payment.

        Parameters
        ----------
        order_id : str
            The ID of the order being paid.

        idempotency_key : str
            A value you specify that uniquely identifies this request among requests you have sent. If
            you are unsure whether a particular payment request was completed successfully, you can reattempt
            it with the same idempotency key without worrying about duplicate payments.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        order_version : typing.Optional[int]
            The version of the order being paid. If not supplied, the latest version will be paid.

        payment_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment) to collect.
            The payment total must match the order total.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayOrderResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.orders.pay_order(
            order_id="order_id",
            idempotency_key="idempotency_key",
        )
        """
        _response = self._raw_client.pay_order(
            order_id,
            idempotency_key=idempotency_key,
            order_version=order_version,
            payment_ids=payment_ids,
            request_options=request_options,
        )
        return _response.data


class AsyncOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrdersClient
        """
        return self._raw_client

    async def create_order(
        self,
        *,
        idempotency_key: typing.Optional[str] = OMIT,
        order: typing.Optional[Order] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateOrderResponse:
        """
        Creates a new [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) that can include information about products for
        purchase and settings to apply to the purchase.

        To pay for a created order, see
        [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

        You can modify open orders using the [UpdateOrder](https://developer.squareup.com/reference/square_2021-08-18/orders-api/update-order) endpoint.

        Parameters
        ----------
        idempotency_key : typing.Optional[str]
            A value you specify that uniquely identifies this
            order among orders you have created.

            If you are unsure whether a particular order was created successfully,
            you can try it again with the same idempotency key without
            worrying about creating duplicate orders.

            For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

        order : typing.Optional[Order]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateOrderResponse
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
            await client.orders.create_order()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_order(
            idempotency_key=idempotency_key, order=order, request_options=request_options
        )
        return _response.data

    async def batch_retrieve_orders(
        self,
        *,
        order_ids: typing.Sequence[str],
        location_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchRetrieveOrdersResponse:
        """
        Retrieves a set of [orders](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by their IDs.

        If a given order ID does not exist, the ID is ignored instead of generating an error.

        Parameters
        ----------
        order_ids : typing.Sequence[str]
            The IDs of the orders to retrieve. A maximum of 100 orders can be retrieved per request.

        location_id : typing.Optional[str]
            The ID of the location for these orders. This field is optional: omit it to retrieve
            orders within the scope of the current authorization's merchant ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchRetrieveOrdersResponse
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
            await client.orders.batch_retrieve_orders(
                order_ids=["order_ids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_retrieve_orders(
            order_ids=order_ids, location_id=location_id, request_options=request_options
        )
        return _response.data

    async def calculate_order(
        self,
        *,
        order: Order,
        proposed_rewards: typing.Optional[typing.Sequence[OrderReward]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalculateOrderResponse:
        """
        Enables applications to preview order pricing without creating an order.

        Parameters
        ----------
        order : Order

        proposed_rewards : typing.Optional[typing.Sequence[OrderReward]]
            Identifies one or more loyalty reward tiers to apply during the order calculation.
            The discounts defined by the reward tiers are added to the order only to preview the
            effect of applying the specified rewards. The rewards do not correspond to actual
            redemptions; that is, no `reward`s are created. Therefore, the reward `id`s are
            random strings used only to reference the reward tier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalculateOrderResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Order

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.calculate_order(
                order=Order(
                    location_id="location_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.calculate_order(
            order=order, proposed_rewards=proposed_rewards, request_options=request_options
        )
        return _response.data

    async def search_orders(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        location_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        query: typing.Optional[SearchOrdersQuery] = OMIT,
        return_entries: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchOrdersResponse:
        """
        Search all orders for one or more locations. Orders include all sales,
        returns, and exchanges regardless of how or when they entered the Square
        ecosystem (such as Point of Sale, Invoices, and Connect APIs).

        `SearchOrders` requests need to specify which locations to search and define a
        [SearchOrdersQuery](https://developer.squareup.com/reference/square_2021-08-18/objects/SearchOrdersQuery) object that controls
        how to sort or filter the results. Your `SearchOrdersQuery` can:

          Set filter criteria.
          Set the sort order.
          Determine whether to return results as complete `Order` objects or as
        [OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects.

        Note that details for orders processed with Square Point of Sale while in
        offline mode might not be transmitted to Square for up to 72 hours. Offline
        orders have a `created_at` value that reflects the time the order was created,
        not the time it was subsequently transmitted to Square.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        limit : typing.Optional[int]
            The maximum number of results to be returned in a single page. It is
            possible to receive fewer results than the specified limit on a given page.

            Default: `500`

        location_ids : typing.Optional[typing.Sequence[str]]
            The location IDs for the orders to query. All locations must belong to
            the same merchant.

            Min: 1 location ID.

            Max: 10 location IDs.

        query : typing.Optional[SearchOrdersQuery]

        return_entries : typing.Optional[bool]
            A Boolean that controls the format of the search results. If `true`,
            `SearchOrders` returns [OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects. If `false`, `SearchOrders`
            returns complete order objects.

            Default: `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchOrdersResponse
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
            await client.orders.search_orders()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_orders(
            cursor=cursor,
            limit=limit,
            location_ids=location_ids,
            query=query,
            return_entries=return_entries,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_order(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveOrderResponse:
        """
        Retrieves an [Order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by ID.

        Parameters
        ----------
        order_id : str
            The ID of the order to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveOrderResponse
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
            await client.orders.retrieve_order(
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_order(order_id, request_options=request_options)
        return _response.data

    async def update_order(
        self,
        order_id: str,
        *,
        fields_to_clear: typing.Optional[typing.Sequence[str]] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        order: typing.Optional[Order] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateOrderResponse:
        """
        Updates an open [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by adding, replacing, or deleting
        fields. Orders with a `COMPLETED` or `CANCELED` state cannot be updated.

        An `UpdateOrder` request requires the following:

        - The `order_id` in the endpoint path, identifying the order to update.
        - The latest `version` of the order to update.
        - The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders#sparse-order-objects)
        containing only the fields to update and the version to which the update is
        being applied.
        - If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation)
        identifying the fields to clear.

        To pay for an order, see
        [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

        Parameters
        ----------
        order_id : str
            The ID of the order to update.

        fields_to_clear : typing.Optional[typing.Sequence[str]]
            The [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation)
            fields to clear. For example, `line_items[uid].note`.
            For more information, see [Deleting fields](https://developer.squareup.com/docs/orders-api/manage-orders#delete-fields).

        idempotency_key : typing.Optional[str]
            A value you specify that uniquely identifies this update request.

            If you are unsure whether a particular update was applied to an order successfully,
            you can reattempt it with the same idempotency key without
            worrying about creating duplicate updates to the order.
            The latest order version is returned.

            For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

        order : typing.Optional[Order]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateOrderResponse
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
            await client.orders.update_order(
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_order(
            order_id,
            fields_to_clear=fields_to_clear,
            idempotency_key=idempotency_key,
            order=order,
            request_options=request_options,
        )
        return _response.data

    async def pay_order(
        self,
        order_id: str,
        *,
        idempotency_key: str,
        order_version: typing.Optional[int] = OMIT,
        payment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayOrderResponse:
        """
        Pay for an [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) using one or more approved [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment)
        or settle an order with a total of `0`.

        The total of the `payment_ids` listed in the request must be equal to the order
        total. Orders with a total amount of `0` can be marked as paid by specifying an empty
        array of `payment_ids` in the request.

        To be used with `PayOrder`, a payment must:

        - Reference the order by specifying the `order_id` when [creating the payment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/create-payment).
        Any approved payments that reference the same `order_id` not specified in the
        `payment_ids` is canceled.
        - Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments#delayed-capture).
        Using a delayed capture payment with `PayOrder` completes the approved payment.

        Parameters
        ----------
        order_id : str
            The ID of the order being paid.

        idempotency_key : str
            A value you specify that uniquely identifies this request among requests you have sent. If
            you are unsure whether a particular payment request was completed successfully, you can reattempt
            it with the same idempotency key without worrying about duplicate payments.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        order_version : typing.Optional[int]
            The version of the order being paid. If not supplied, the latest version will be paid.

        payment_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment) to collect.
            The payment total must match the order total.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayOrderResponse
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
            await client.orders.pay_order(
                order_id="order_id",
                idempotency_key="idempotency_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pay_order(
            order_id,
            idempotency_key=idempotency_key,
            order_version=order_version,
            payment_ids=payment_ids,
            request_options=request_options,
        )
        return _response.data

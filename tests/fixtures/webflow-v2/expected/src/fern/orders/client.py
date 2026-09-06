

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOrdersClient, RawOrdersClient
from .types.get_orders_response import GetOrdersResponse
from .types.list_orders_request_status import ListOrdersRequestStatus
from .types.list_orders_response import ListOrdersResponse
from .types.refund_orders_request_reason import RefundOrdersRequestReason
from .types.refund_orders_response import RefundOrdersResponse
from .types.update_fulfill_orders_response import UpdateFulfillOrdersResponse
from .types.update_orders_response import UpdateOrdersResponse
from .types.update_unfulfill_orders_response import UpdateUnfulfillOrdersResponse


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

    def list(
        self,
        site_id: str,
        *,
        status: typing.Optional[ListOrdersRequestStatus] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListOrdersResponse:
        """
        List all orders created for a given site.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        status : typing.Optional[ListOrdersRequestStatus]
            Filter the orders by status

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrdersResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list(
            site_id, status=status, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get(
        self, site_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetOrdersResponse:
        """
        Retrieve a single product by its ID. All of its SKUs will also be
        retrieved.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrdersResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.get(
            site_id="580e63e98c9a982ac9b8b741",
            order_id="5e8518516e147040726cc415",
        )
        """
        _response = self._raw_client.get(site_id, order_id, request_options=request_options)
        return _response.data

    def update(
        self,
        site_id: str,
        order_id: str,
        *,
        comment: typing.Optional[str] = OMIT,
        shipping_provider: typing.Optional[str] = OMIT,
        shipping_tracking: typing.Optional[str] = OMIT,
        shipping_tracking_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateOrdersResponse:
        """
        This API lets you update the fields, `comment`, `shippingProvider`,
        and/or `shippingTracking` for a given order. All three fields can be
        updated simultaneously or independently.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        comment : typing.Optional[str]
            Arbitrary data for your records

        shipping_provider : typing.Optional[str]
            Company or method used to ship order

        shipping_tracking : typing.Optional[str]
            Tracking number for order shipment

        shipping_tracking_url : typing.Optional[str]
            URL to track order shipment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateOrdersResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.update(
            site_id="580e63e98c9a982ac9b8b741",
            order_id="5e8518516e147040726cc415",
        )
        """
        _response = self._raw_client.update(
            site_id,
            order_id,
            comment=comment,
            shipping_provider=shipping_provider,
            shipping_tracking=shipping_tracking,
            shipping_tracking_url=shipping_tracking_url,
            request_options=request_options,
        )
        return _response.data

    def update_fulfill(
        self,
        site_id: str,
        order_id: str,
        *,
        send_order_fulfilled_email: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateFulfillOrdersResponse:
        """
        Updates an order's status to fulfilled

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        send_order_fulfilled_email : typing.Optional[bool]
            Whether or not the Order Fulfilled email should be sent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateFulfillOrdersResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.update_fulfill(
            site_id="580e63e98c9a982ac9b8b741",
            order_id="5e8518516e147040726cc415",
        )
        """
        _response = self._raw_client.update_fulfill(
            site_id, order_id, send_order_fulfilled_email=send_order_fulfilled_email, request_options=request_options
        )
        return _response.data

    def update_unfulfill(
        self, site_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateUnfulfillOrdersResponse:
        """
        Updates an order's status to unfulfilled

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateUnfulfillOrdersResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.update_unfulfill(
            site_id="580e63e98c9a982ac9b8b741",
            order_id="5e8518516e147040726cc415",
        )
        """
        _response = self._raw_client.update_unfulfill(site_id, order_id, request_options=request_options)
        return _response.data

    def refund(
        self,
        site_id: str,
        order_id: str,
        *,
        reason: typing.Optional[RefundOrdersRequestReason] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefundOrdersResponse:
        """
        This API will reverse a Stripe charge and refund an order back to a
        customer. It will also set the order's status to `refunded`.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        reason : typing.Optional[RefundOrdersRequestReason]
            The reason for the refund

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefundOrdersResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.refund(
            site_id="580e63e98c9a982ac9b8b741",
            order_id="5e8518516e147040726cc415",
        )
        """
        _response = self._raw_client.refund(site_id, order_id, reason=reason, request_options=request_options)
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

    async def list(
        self,
        site_id: str,
        *,
        status: typing.Optional[ListOrdersRequestStatus] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListOrdersResponse:
        """
        List all orders created for a given site.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        status : typing.Optional[ListOrdersRequestStatus]
            Filter the orders by status

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOrdersResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            site_id, status=status, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get(
        self, site_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetOrdersResponse:
        """
        Retrieve a single product by its ID. All of its SKUs will also be
        retrieved.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrdersResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.get(
                site_id="580e63e98c9a982ac9b8b741",
                order_id="5e8518516e147040726cc415",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(site_id, order_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        site_id: str,
        order_id: str,
        *,
        comment: typing.Optional[str] = OMIT,
        shipping_provider: typing.Optional[str] = OMIT,
        shipping_tracking: typing.Optional[str] = OMIT,
        shipping_tracking_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateOrdersResponse:
        """
        This API lets you update the fields, `comment`, `shippingProvider`,
        and/or `shippingTracking` for a given order. All three fields can be
        updated simultaneously or independently.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        comment : typing.Optional[str]
            Arbitrary data for your records

        shipping_provider : typing.Optional[str]
            Company or method used to ship order

        shipping_tracking : typing.Optional[str]
            Tracking number for order shipment

        shipping_tracking_url : typing.Optional[str]
            URL to track order shipment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateOrdersResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.update(
                site_id="580e63e98c9a982ac9b8b741",
                order_id="5e8518516e147040726cc415",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            site_id,
            order_id,
            comment=comment,
            shipping_provider=shipping_provider,
            shipping_tracking=shipping_tracking,
            shipping_tracking_url=shipping_tracking_url,
            request_options=request_options,
        )
        return _response.data

    async def update_fulfill(
        self,
        site_id: str,
        order_id: str,
        *,
        send_order_fulfilled_email: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateFulfillOrdersResponse:
        """
        Updates an order's status to fulfilled

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        send_order_fulfilled_email : typing.Optional[bool]
            Whether or not the Order Fulfilled email should be sent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateFulfillOrdersResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.update_fulfill(
                site_id="580e63e98c9a982ac9b8b741",
                order_id="5e8518516e147040726cc415",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_fulfill(
            site_id, order_id, send_order_fulfilled_email=send_order_fulfilled_email, request_options=request_options
        )
        return _response.data

    async def update_unfulfill(
        self, site_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateUnfulfillOrdersResponse:
        """
        Updates an order's status to unfulfilled

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateUnfulfillOrdersResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.update_unfulfill(
                site_id="580e63e98c9a982ac9b8b741",
                order_id="5e8518516e147040726cc415",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_unfulfill(site_id, order_id, request_options=request_options)
        return _response.data

    async def refund(
        self,
        site_id: str,
        order_id: str,
        *,
        reason: typing.Optional[RefundOrdersRequestReason] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefundOrdersResponse:
        """
        This API will reverse a Stripe charge and refund an order back to a
        customer. It will also set the order's status to `refunded`.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        order_id : str
            Unique identifier for an Order

        reason : typing.Optional[RefundOrdersRequestReason]
            The reason for the refund

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefundOrdersResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.refund(
                site_id="580e63e98c9a982ac9b8b741",
                order_id="5e8518516e147040726cc415",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refund(site_id, order_id, reason=reason, request_options=request_options)
        return _response.data

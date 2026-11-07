

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from ..types.non_empty_id import NonEmptyId
from ..types.order_status import OrderStatus
from ..types.payment_method import PaymentMethod
from ..types.public_health_resp_body import PublicHealthRespBody
from ..types.replay_resp_body import ReplayRespBody
from ..types.track_public_resp_body import TrackPublicRespBody
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
        customer_id: NonEmptyId,
        items: typing.Sequence[LineItem],
        currency: typing.Optional[CurrencyCode] = OMIT,
        notes: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateOrderRespBody:
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
        CreateOrderRespBody
            Created

        Examples
        --------
        from fern import FernApi, LineItem, ProductRef

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.create_order(
            customer_id="customerId",
            items=[
                LineItem(
                    product=ProductRef(
                        id="id",
                        name="name",
                    ),
                    quantity=1,
                    sku="sku",
                    unit_cents=1,
                )
            ],
        )
        """
        _response = self._raw_client.create_order(
            customer_id=customer_id,
            items=items,
            currency=currency,
            notes=notes,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def get_order(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetOrderRespBody:
        """
        Fetch one order.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrderRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.get_order(
            id="id",
        )
        """
        _response = self._raw_client.get_order(id, request_options=request_options)
        return _response.data

    def cancel_order(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> CancelOrderRespBody:
        """
        Admin cancellation. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelOrderRespBody
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.cancel_order(
            id="id",
        )
        """
        _response = self._raw_client.cancel_order(id, request_options=request_options)
        return _response.data

    def replay(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ReplayRespBody:
        """
        Admin replay (parent chain only).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplayRespBody
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.replay(
            id="id",
        )
        """
        _response = self._raw_client.replay(id, request_options=request_options)
        return _response.data

    def force_ship(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ForceShipRespBody:
        """
        Admin force-ship. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForceShipRespBody
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.force_ship(
            id="id",
        )
        """
        _response = self._raw_client.force_ship(id, request_options=request_options)
        return _response.data

    def track_public(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TrackPublicRespBody:
        """
        Public order tracking by id - CORS only, no auth.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackPublicRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.track_public(
            id="id",
        )
        """
        _response = self._raw_client.track_public(id, request_options=request_options)
        return _response.data

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
    ) -> FilterOrdersRespBody:
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
        FilterOrdersRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.filter_orders(
            retry_after=1,
            status="pending",
            method="card",
            limit=1,
            max_price=1,
        )
        """
        _response = self._raw_client.filter_orders(
            status=status,
            method=method,
            limit=limit,
            max_price=max_price,
            retry_after=retry_after,
            idem_key=idem_key,
            request_options=request_options,
        )
        return _response.data

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
    ) -> DefaultsRespBody:
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
        DefaultsRespBody
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.defaults()
        """
        _response = self._raw_client.defaults(
            allowed_methods=allowed_methods,
            currency=currency,
            flag=flag,
            num=num,
            preset=preset,
            status=status,
            str=str,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def bulk_export(
        self,
        *,
        limit: int,
        status: typing.Optional[OrderStatus] = None,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkExportRespBody:
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
        BulkExportRespBody
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.bulk_export(
            limit=1,
        )
        """
        _response = self._raw_client.bulk_export(
            limit=limit, status=status, cursor=cursor, request_options=request_options
        )
        return _response.data

    def public_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> PublicHealthRespBody:
        """
        Public readiness probe - bypasses every parent middleware AND security.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicHealthRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.public_health()
        """
        _response = self._raw_client.public_health(request_options=request_options)
        return _response.data

    def list_orders(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        status: typing.Optional[OrderStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListOrdersRespBody:
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
        ListOrdersRespBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_orders(
            limit=1,
        )
        """
        _response = self._raw_client.list_orders(
            limit=limit, cursor=cursor, status=status, request_options=request_options
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
        customer_id: NonEmptyId,
        items: typing.Sequence[LineItem],
        currency: typing.Optional[CurrencyCode] = OMIT,
        notes: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateOrderRespBody:
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
        CreateOrderRespBody
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LineItem, ProductRef

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.create_order(
                customer_id="customerId",
                items=[
                    LineItem(
                        product=ProductRef(
                            id="id",
                            name="name",
                        ),
                        quantity=1,
                        sku="sku",
                        unit_cents=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_order(
            customer_id=customer_id,
            items=items,
            currency=currency,
            notes=notes,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def get_order(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetOrderRespBody:
        """
        Fetch one order.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrderRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.get_order(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_order(id, request_options=request_options)
        return _response.data

    async def cancel_order(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelOrderRespBody:
        """
        Admin cancellation. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelOrderRespBody
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.cancel_order(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_order(id, request_options=request_options)
        return _response.data

    async def replay(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ReplayRespBody:
        """
        Admin replay (parent chain only).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplayRespBody
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.replay(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replay(id, request_options=request_options)
        return _response.data

    async def force_ship(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ForceShipRespBody:
        """
        Admin force-ship. Idempotent.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForceShipRespBody
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.force_ship(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.force_ship(id, request_options=request_options)
        return _response.data

    async def track_public(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrackPublicRespBody:
        """
        Public order tracking by id - CORS only, no auth.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackPublicRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.track_public(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.track_public(id, request_options=request_options)
        return _response.data

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
    ) -> FilterOrdersRespBody:
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
        FilterOrdersRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.filter_orders(
                retry_after=1,
                status="pending",
                method="card",
                limit=1,
                max_price=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.filter_orders(
            status=status,
            method=method,
            limit=limit,
            max_price=max_price,
            retry_after=retry_after,
            idem_key=idem_key,
            request_options=request_options,
        )
        return _response.data

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
    ) -> DefaultsRespBody:
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
        DefaultsRespBody
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.defaults()


        asyncio.run(main())
        """
        _response = await self._raw_client.defaults(
            allowed_methods=allowed_methods,
            currency=currency,
            flag=flag,
            num=num,
            preset=preset,
            status=status,
            str=str,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def bulk_export(
        self,
        *,
        limit: int,
        status: typing.Optional[OrderStatus] = None,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkExportRespBody:
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
        BulkExportRespBody
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.bulk_export(
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_export(
            limit=limit, status=status, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def public_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> PublicHealthRespBody:
        """
        Public readiness probe - bypasses every parent middleware AND security.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicHealthRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.public_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.public_health(request_options=request_options)
        return _response.data

    async def list_orders(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        status: typing.Optional[OrderStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListOrdersRespBody:
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
        ListOrdersRespBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_orders(
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_orders(
            limit=limit, cursor=cursor, status=status, request_options=request_options
        )
        return _response.data

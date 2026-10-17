

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOrdersClient, RawOrdersClient
from .types.update_order_request_data import UpdateOrderRequestData


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

    def get_order(
        self,
        *,
        signature: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get order

        Parameters
        ----------
        signature : typing.Optional[str]

        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.get_order(
            signature="signature",
            include="transactions",
        )
        """
        _response = self._raw_client.get_order(signature=signature, include=include, request_options=request_options)
        return _response.data

    def update_order(
        self,
        *,
        data: typing.Optional[UpdateOrderRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update order

        Parameters
        ----------
        data : typing.Optional[UpdateOrderRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.orders import UpdateOrderRequestData, UpdateOrderRequestDataAttributes

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.update_order(
            data=UpdateOrderRequestData(
                attributes=UpdateOrderRequestDataAttributes(
                    notes="What a lovely day!",
                ),
                id="1",
                type="orders",
            ),
        )
        """
        _response = self._raw_client.update_order(data=data, request_options=request_options)
        return _response.data

    def check_order_payment_status_action(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Check order payment status action

        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.check_order_payment_status_action(
            include="latest_transaction",
        )
        """
        _response = self._raw_client.check_order_payment_status_action(include=include, request_options=request_options)
        return _response.data

    def mark_pending_payment_action(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Mark pending payment action

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.mark_pending_payment_action()
        """
        _response = self._raw_client.mark_pending_payment_action(request_options=request_options)
        return _response.data

    def mark_awaiting_payment_action(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Mark awaiting payment action

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.mark_awaiting_payment_action()
        """
        _response = self._raw_client.mark_awaiting_payment_action(request_options=request_options)
        return _response.data

    def list_order_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_lines()
        """
        _response = self._raw_client.list_order_lines(request_options=request_options)
        return _response.data

    def list_order_lines_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_lines_relationships()
        """
        _response = self._raw_client.list_order_lines_relationships(request_options=request_options)
        return _response.data

    def list_order_digital_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order digital lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_digital_lines()
        """
        _response = self._raw_client.list_order_digital_lines(request_options=request_options)
        return _response.data

    def list_order_digital_lines_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List order digital lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_digital_lines_relationships()
        """
        _response = self._raw_client.list_order_digital_lines_relationships(request_options=request_options)
        return _response.data

    def list_order_physical_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order physical lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_physical_lines()
        """
        _response = self._raw_client.list_order_physical_lines(request_options=request_options)
        return _response.data

    def list_order_physical_lines_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List order physical lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_physical_lines_relationships()
        """
        _response = self._raw_client.list_order_physical_lines_relationships(request_options=request_options)
        return _response.data

    def list_order_product_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order product lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_product_lines()
        """
        _response = self._raw_client.list_order_product_lines(request_options=request_options)
        return _response.data

    def list_order_product_lines_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List order product lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_product_lines_relationships()
        """
        _response = self._raw_client.list_order_product_lines_relationships(request_options=request_options)
        return _response.data

    def list_order_shipping_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order shipping lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_shipping_lines()
        """
        _response = self._raw_client.list_order_shipping_lines(request_options=request_options)
        return _response.data

    def list_order_shipping_lines_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List order shipping lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.orders.list_order_shipping_lines_relationships()
        """
        _response = self._raw_client.list_order_shipping_lines_relationships(request_options=request_options)
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

    async def get_order(
        self,
        *,
        signature: typing.Optional[str] = None,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get order

        Parameters
        ----------
        signature : typing.Optional[str]

        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.get_order(
                signature="signature",
                include="transactions",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_order(
            signature=signature, include=include, request_options=request_options
        )
        return _response.data

    async def update_order(
        self,
        *,
        data: typing.Optional[UpdateOrderRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update order

        Parameters
        ----------
        data : typing.Optional[UpdateOrderRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.orders import UpdateOrderRequestData, UpdateOrderRequestDataAttributes

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.update_order(
                data=UpdateOrderRequestData(
                    attributes=UpdateOrderRequestDataAttributes(
                        notes="What a lovely day!",
                    ),
                    id="1",
                    type="orders",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_order(data=data, request_options=request_options)
        return _response.data

    async def check_order_payment_status_action(
        self, *, include: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Check order payment status action

        Parameters
        ----------
        include : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.check_order_payment_status_action(
                include="latest_transaction",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_order_payment_status_action(
            include=include, request_options=request_options
        )
        return _response.data

    async def mark_pending_payment_action(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Mark pending payment action

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.mark_pending_payment_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_pending_payment_action(request_options=request_options)
        return _response.data

    async def mark_awaiting_payment_action(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Mark awaiting payment action

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.mark_awaiting_payment_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_awaiting_payment_action(request_options=request_options)
        return _response.data

    async def list_order_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_lines()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_lines(request_options=request_options)
        return _response.data

    async def list_order_lines_relationships(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_lines_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_lines_relationships(request_options=request_options)
        return _response.data

    async def list_order_digital_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order digital lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_digital_lines()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_digital_lines(request_options=request_options)
        return _response.data

    async def list_order_digital_lines_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List order digital lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_digital_lines_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_digital_lines_relationships(request_options=request_options)
        return _response.data

    async def list_order_physical_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order physical lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_physical_lines()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_physical_lines(request_options=request_options)
        return _response.data

    async def list_order_physical_lines_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List order physical lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_physical_lines_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_physical_lines_relationships(request_options=request_options)
        return _response.data

    async def list_order_product_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order product lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_product_lines()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_product_lines(request_options=request_options)
        return _response.data

    async def list_order_product_lines_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List order product lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_product_lines_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_product_lines_relationships(request_options=request_options)
        return _response.data

    async def list_order_shipping_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List order shipping lines

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_shipping_lines()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_shipping_lines(request_options=request_options)
        return _response.data

    async def list_order_shipping_lines_relationships(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List order shipping lines relationships

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.orders.list_order_shipping_lines_relationships()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_order_shipping_lines_relationships(request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.order import Order
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

    def createorder(
        self,
        payment_id: str,
        *,
        merchant_reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Order:
        """
        Parameters
        ----------
        payment_id : str
            Payment identifier

        merchant_reference : typing.Optional[str]
            Merchant order reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            Order created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.orders.createorder(
            payment_id="payment_id",
        )
        """
        _response = self._raw_client.createorder(
            payment_id, merchant_reference=merchant_reference, request_options=request_options
        )
        return _response.data

    def update_order_status(
        self,
        payment_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Send order status update for a payment.

        Parameters
        ----------
        payment_id : str
            Payment ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Update order status successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.orders.update_order_status(
            payment_id="payment_id",
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.update_order_status(payment_id, request=request, request_options=request_options)
        return _response.data

    def send_shipment_info(
        self,
        payment_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Send shipment information for a payment order.

        Parameters
        ----------
        payment_id : str
            Payment ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Send shipment info successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.orders.send_shipment_info(
            payment_id="payment_id",
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.send_shipment_info(payment_id, request=request, request_options=request_options)
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

    async def createorder(
        self,
        payment_id: str,
        *,
        merchant_reference: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Order:
        """
        Parameters
        ----------
        payment_id : str
            Payment identifier

        merchant_reference : typing.Optional[str]
            Merchant order reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            Order created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.orders.createorder(
                payment_id="payment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createorder(
            payment_id, merchant_reference=merchant_reference, request_options=request_options
        )
        return _response.data

    async def update_order_status(
        self,
        payment_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Send order status update for a payment.

        Parameters
        ----------
        payment_id : str
            Payment ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Update order status successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.orders.update_order_status(
                payment_id="payment_id",
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_order_status(
            payment_id, request=request, request_options=request_options
        )
        return _response.data

    async def send_shipment_info(
        self,
        payment_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Send shipment information for a payment order.

        Parameters
        ----------
        payment_id : str
            Payment ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Send shipment info successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.orders.send_shipment_info(
                payment_id="payment_id",
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_shipment_info(
            payment_id, request=request, request_options=request_options
        )
        return _response.data

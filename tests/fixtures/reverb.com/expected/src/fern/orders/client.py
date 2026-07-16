

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOrdersClient, RawOrdersClient


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

    def feedback_details_for_an_orders_buyer(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Feedback details for an order's buyer

        Parameters
        ----------
        order_id : str

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
        client.orders.feedback_details_for_an_orders_buyer(
            order_id="order_id",
        )
        """
        _response = self._raw_client.feedback_details_for_an_orders_buyer(order_id, request_options=request_options)
        return _response.data

    def add_feedback_about_an_orders_buyer(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add feedback about an order's buyer

        Parameters
        ----------
        order_id : str

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
        client.orders.add_feedback_about_an_orders_buyer(
            order_id="order_id",
        )
        """
        _response = self._raw_client.add_feedback_about_an_orders_buyer(order_id, request_options=request_options)
        return _response.data

    def feedback_details_for_an_orders_seller(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Feedback details for an order's seller

        Parameters
        ----------
        order_id : str

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
        client.orders.feedback_details_for_an_orders_seller(
            order_id="order_id",
        )
        """
        _response = self._raw_client.feedback_details_for_an_orders_seller(order_id, request_options=request_options)
        return _response.data

    def add_feedback_about_an_orders_seller(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add feedback about an order's seller

        Parameters
        ----------
        order_id : str

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
        client.orders.add_feedback_about_an_orders_seller(
            order_id="order_id",
        )
        """
        _response = self._raw_client.add_feedback_about_an_orders_seller(order_id, request_options=request_options)
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

    async def feedback_details_for_an_orders_buyer(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Feedback details for an order's buyer

        Parameters
        ----------
        order_id : str

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
            await client.orders.feedback_details_for_an_orders_buyer(
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.feedback_details_for_an_orders_buyer(
            order_id, request_options=request_options
        )
        return _response.data

    async def add_feedback_about_an_orders_buyer(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add feedback about an order's buyer

        Parameters
        ----------
        order_id : str

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
            await client.orders.add_feedback_about_an_orders_buyer(
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_feedback_about_an_orders_buyer(order_id, request_options=request_options)
        return _response.data

    async def feedback_details_for_an_orders_seller(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Feedback details for an order's seller

        Parameters
        ----------
        order_id : str

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
            await client.orders.feedback_details_for_an_orders_seller(
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.feedback_details_for_an_orders_seller(
            order_id, request_options=request_options
        )
        return _response.data

    async def add_feedback_about_an_orders_seller(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add feedback about an order's seller

        Parameters
        ----------
        order_id : str

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
            await client.orders.add_feedback_about_an_orders_seller(
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_feedback_about_an_orders_seller(
            order_id, request_options=request_options
        )
        return _response.data

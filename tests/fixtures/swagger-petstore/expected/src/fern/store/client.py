

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.order import Order
from ..types.order_status import OrderStatus
from .raw_client import AsyncRawStoreClient, RawStoreClient


OMIT = typing.cast(typing.Any, ...)


class StoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStoreClient
        """
        return self._raw_client

    def get_inventory(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        Returns a map of status codes to quantities.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.store.get_inventory()
        """
        _response = self._raw_client.get_inventory(request_options=request_options)
        return _response.data

    def place_order(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        pet_id: typing.Optional[int] = OMIT,
        quantity: typing.Optional[int] = OMIT,
        ship_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[OrderStatus] = OMIT,
        complete: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Order:
        """
        Place a new order in the store.

        Parameters
        ----------
        id : typing.Optional[int]

        pet_id : typing.Optional[int]

        quantity : typing.Optional[int]

        ship_date : typing.Optional[dt.datetime]

        status : typing.Optional[OrderStatus]
            Order Status

        complete : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.store.place_order()
        """
        _response = self._raw_client.place_order(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
            request_options=request_options,
        )
        return _response.data

    def get_order_by_id(self, order_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Order:
        """
        For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        Parameters
        ----------
        order_id : int
            ID of order that needs to be fetched

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.store.get_order_by_id(
            order_id=1000000,
        )
        """
        _response = self._raw_client.get_order_by_id(order_id, request_options=request_options)
        return _response.data

    def delete_order(self, order_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

        Parameters
        ----------
        order_id : int
            ID of the order that needs to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.store.delete_order(
            order_id=1000000,
        )
        """
        _response = self._raw_client.delete_order(order_id, request_options=request_options)
        return _response.data


class AsyncStoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStoreClient
        """
        return self._raw_client

    async def get_inventory(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        Returns a map of status codes to quantities.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.store.get_inventory()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_inventory(request_options=request_options)
        return _response.data

    async def place_order(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        pet_id: typing.Optional[int] = OMIT,
        quantity: typing.Optional[int] = OMIT,
        ship_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[OrderStatus] = OMIT,
        complete: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Order:
        """
        Place a new order in the store.

        Parameters
        ----------
        id : typing.Optional[int]

        pet_id : typing.Optional[int]

        quantity : typing.Optional[int]

        ship_date : typing.Optional[dt.datetime]

        status : typing.Optional[OrderStatus]
            Order Status

        complete : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.store.place_order()


        asyncio.run(main())
        """
        _response = await self._raw_client.place_order(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
            request_options=request_options,
        )
        return _response.data

    async def get_order_by_id(self, order_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Order:
        """
        For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

        Parameters
        ----------
        order_id : int
            ID of order that needs to be fetched

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Order
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.store.get_order_by_id(
                order_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_order_by_id(order_id, request_options=request_options)
        return _response.data

    async def delete_order(self, order_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

        Parameters
        ----------
        order_id : int
            ID of the order that needs to be deleted

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
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.store.delete_order(
                order_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_order(order_id, request_options=request_options)
        return _response.data

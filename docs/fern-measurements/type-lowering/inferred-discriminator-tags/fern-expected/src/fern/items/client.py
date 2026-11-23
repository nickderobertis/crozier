

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.query_response import QueryResponse
from ..types.store_item import StoreItem
from .raw_client import AsyncRawItemsClient, RawItemsClient


OMIT = typing.cast(typing.Any, ...)


class ItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawItemsClient
        """
        return self._raw_client

    def get_item(self, item_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> StoreItem:
        """
        Parameters
        ----------
        item_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoreItem
            The item.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.items.get_item(
            item_id="itemId",
        )
        """
        _response = self._raw_client.get_item(item_id, request_options=request_options)
        return _response.data

    def run_query(self, *, scope_id: str, request_options: typing.Optional[RequestOptions] = None) -> QueryResponse:
        """
        Parameters
        ----------
        scope_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResponse
            The query result or status.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.items.run_query(
            scope_id="scope_id",
        )
        """
        _response = self._raw_client.run_query(scope_id=scope_id, request_options=request_options)
        return _response.data


class AsyncItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawItemsClient
        """
        return self._raw_client

    async def get_item(self, item_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> StoreItem:
        """
        Parameters
        ----------
        item_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StoreItem
            The item.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.items.get_item(
                item_id="itemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item(item_id, request_options=request_options)
        return _response.data

    async def run_query(
        self, *, scope_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> QueryResponse:
        """
        Parameters
        ----------
        scope_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryResponse
            The query result or status.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.items.run_query(
                scope_id="scope_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_query(scope_id=scope_id, request_options=request_options)
        return _response.data

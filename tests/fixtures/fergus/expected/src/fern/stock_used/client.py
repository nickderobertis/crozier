

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stock_used_list_response import StockUsedListResponse
from .raw_client import AsyncRawStockUsedClient, RawStockUsedClient


class StockUsedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStockUsedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStockUsedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStockUsedClient
        """
        return self._raw_client

    def get_stock_used(
        self,
        *,
        filter_date_from: typing.Optional[dt.date] = None,
        page_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StockUsedListResponse:
        """

          Returns historical stock used across all jobs, optionally filtered by filterDateFrom.

          Stock used is defined as material line items that:
          - Have been invoiced to the customer (sent or paid).
          - And are assigned as materials sales account.
          - And are not from purchase orders.
          - And are not invoiced from suppliers.


        Parameters
        ----------
        filter_date_from : typing.Optional[dt.date]
            Filter stock used on or after this date (yyyy-mm-dd) default is 90 days ago and max up to 180 days ago

        page_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StockUsedListResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stock_used.get_stock_used()
        """
        _response = self._raw_client.get_stock_used(
            filter_date_from=filter_date_from, page_cursor=page_cursor, request_options=request_options
        )
        return _response.data


class AsyncStockUsedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStockUsedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStockUsedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStockUsedClient
        """
        return self._raw_client

    async def get_stock_used(
        self,
        *,
        filter_date_from: typing.Optional[dt.date] = None,
        page_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StockUsedListResponse:
        """

          Returns historical stock used across all jobs, optionally filtered by filterDateFrom.

          Stock used is defined as material line items that:
          - Have been invoiced to the customer (sent or paid).
          - And are assigned as materials sales account.
          - And are not from purchase orders.
          - And are not invoiced from suppliers.


        Parameters
        ----------
        filter_date_from : typing.Optional[dt.date]
            Filter stock used on or after this date (yyyy-mm-dd) default is 90 days ago and max up to 180 days ago

        page_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StockUsedListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stock_used.get_stock_used()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stock_used(
            filter_date_from=filter_date_from, page_cursor=page_cursor, request_options=request_options
        )
        return _response.data

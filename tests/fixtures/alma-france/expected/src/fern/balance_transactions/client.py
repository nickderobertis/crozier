

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBalanceTransactionsClient, RawBalanceTransactionsClient
from .types.listbalancetransactions_response import ListbalancetransactionsResponse


class BalanceTransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBalanceTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBalanceTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBalanceTransactionsClient
        """
        return self._raw_client

    def listbalancetransactions(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListbalancetransactionsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page number

        limit : typing.Optional[int]
            Number of results per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListbalancetransactionsResponse
            List of balance transactions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.balance_transactions.listbalancetransactions()
        """
        _response = self._raw_client.listbalancetransactions(page=page, limit=limit, request_options=request_options)
        return _response.data


class AsyncBalanceTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBalanceTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBalanceTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBalanceTransactionsClient
        """
        return self._raw_client

    async def listbalancetransactions(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListbalancetransactionsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page number

        limit : typing.Optional[int]
            Number of results per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListbalancetransactionsResponse
            List of balance transactions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.balance_transactions.listbalancetransactions()


        asyncio.run(main())
        """
        _response = await self._raw_client.listbalancetransactions(
            page=page, limit=limit, request_options=request_options
        )
        return _response.data

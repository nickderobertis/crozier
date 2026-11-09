

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accounting_proxy_response import AccountingProxyResponse
from .raw_client import AsyncRawAccountingProxyClient, RawAccountingProxyClient


OMIT = typing.cast(typing.Any, ...)


class AccountingProxyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountingProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountingProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountingProxyClient
        """
        return self._raw_client

    def accounting_proxy_tunnel(
        self,
        *,
        path: str,
        method: str,
        body: typing.Optional[typing.Any] = OMIT,
        query_params: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingProxyResponse:
        """
        Call the native Accounting app's api for a specific connection

        Parameters
        ----------
        path : str

        method : str

        body : typing.Optional[typing.Any]

        query_params : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingProxyResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.accounting_proxy.accounting_proxy_tunnel(
            path="path",
            method="method",
        )
        """
        _response = self._raw_client.accounting_proxy_tunnel(
            path=path, method=method, body=body, query_params=query_params, request_options=request_options
        )
        return _response.data


class AsyncAccountingProxyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountingProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountingProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountingProxyClient
        """
        return self._raw_client

    async def accounting_proxy_tunnel(
        self,
        *,
        path: str,
        method: str,
        body: typing.Optional[typing.Any] = OMIT,
        query_params: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingProxyResponse:
        """
        Call the native Accounting app's api for a specific connection

        Parameters
        ----------
        path : str

        method : str

        body : typing.Optional[typing.Any]

        query_params : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingProxyResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounting_proxy.accounting_proxy_tunnel(
                path="path",
                method="method",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accounting_proxy_tunnel(
            path=path, method=method, body=body, query_params=query_params, request_options=request_options
        )
        return _response.data

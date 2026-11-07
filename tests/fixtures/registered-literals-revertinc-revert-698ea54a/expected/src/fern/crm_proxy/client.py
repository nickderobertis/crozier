

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.crm_proxy_response import CrmProxyResponse
from .raw_client import AsyncRawCrmProxyClient, RawCrmProxyClient


OMIT = typing.cast(typing.Any, ...)


class CrmProxyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmProxyClient
        """
        return self._raw_client

    def crm_proxy_tunnel(
        self,
        *,
        path: str,
        method: str,
        body: typing.Optional[typing.Any] = OMIT,
        query_params: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmProxyResponse:
        """
        Call the native CRM api for a specific connection

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
        CrmProxyResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_proxy.crm_proxy_tunnel(
            path="path",
            method="method",
        )
        """
        _response = self._raw_client.crm_proxy_tunnel(
            path=path, method=method, body=body, query_params=query_params, request_options=request_options
        )
        return _response.data


class AsyncCrmProxyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmProxyClient
        """
        return self._raw_client

    async def crm_proxy_tunnel(
        self,
        *,
        path: str,
        method: str,
        body: typing.Optional[typing.Any] = OMIT,
        query_params: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmProxyResponse:
        """
        Call the native CRM api for a specific connection

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
        CrmProxyResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_proxy.crm_proxy_tunnel(
                path="path",
                method="method",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_proxy_tunnel(
            path=path, method=method, body=body, query_params=query_params, request_options=request_options
        )
        return _response.data

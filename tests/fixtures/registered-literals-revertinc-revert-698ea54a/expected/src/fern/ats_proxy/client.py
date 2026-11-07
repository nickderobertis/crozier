

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ats_proxy_response import AtsProxyResponse
from .raw_client import AsyncRawAtsProxyClient, RawAtsProxyClient


OMIT = typing.cast(typing.Any, ...)


class AtsProxyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAtsProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAtsProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAtsProxyClient
        """
        return self._raw_client

    def ats_proxy_tunnel(
        self,
        *,
        path: str,
        method: str,
        body: typing.Optional[typing.Any] = OMIT,
        query_params: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsProxyResponse:
        """
        Call the native ATS api for a specific connection

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
        AtsProxyResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_proxy.ats_proxy_tunnel(
            path="path",
            method="method",
        )
        """
        _response = self._raw_client.ats_proxy_tunnel(
            path=path, method=method, body=body, query_params=query_params, request_options=request_options
        )
        return _response.data


class AsyncAtsProxyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAtsProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAtsProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAtsProxyClient
        """
        return self._raw_client

    async def ats_proxy_tunnel(
        self,
        *,
        path: str,
        method: str,
        body: typing.Optional[typing.Any] = OMIT,
        query_params: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsProxyResponse:
        """
        Call the native ATS api for a specific connection

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
        AtsProxyResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_proxy.ats_proxy_tunnel(
                path="path",
                method="method",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_proxy_tunnel(
            path=path, method=method, body=body, query_params=query_params, request_options=request_options
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ticket_proxy_response import TicketProxyResponse
from .raw_client import AsyncRawTicketProxyClient, RawTicketProxyClient


OMIT = typing.cast(typing.Any, ...)


class TicketProxyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTicketProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTicketProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTicketProxyClient
        """
        return self._raw_client

    def ticket_proxy_tunnel(
        self,
        *,
        path: str,
        method: str,
        body: typing.Optional[typing.Any] = OMIT,
        query_params: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketProxyResponse:
        """
        Call the native Ticketing app's api for a specific connection

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
        TicketProxyResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_proxy.ticket_proxy_tunnel(
            path="path",
            method="method",
        )
        """
        _response = self._raw_client.ticket_proxy_tunnel(
            path=path, method=method, body=body, query_params=query_params, request_options=request_options
        )
        return _response.data


class AsyncTicketProxyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTicketProxyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTicketProxyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTicketProxyClient
        """
        return self._raw_client

    async def ticket_proxy_tunnel(
        self,
        *,
        path: str,
        method: str,
        body: typing.Optional[typing.Any] = OMIT,
        query_params: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketProxyResponse:
        """
        Call the native Ticketing app's api for a specific connection

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
        TicketProxyResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_proxy.ticket_proxy_tunnel(
                path="path",
                method="method",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_proxy_tunnel(
            path=path, method=method, body=body, query_params=query_params, request_options=request_options
        )
        return _response.data

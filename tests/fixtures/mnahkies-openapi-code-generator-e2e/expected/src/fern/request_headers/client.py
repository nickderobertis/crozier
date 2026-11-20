

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRequestHeadersClient, RawRequestHeadersClient
from .types.get_headers_request_response import GetHeadersRequestResponse
from .types.get_headers_undeclared_response import GetHeadersUndeclaredResponse


class RequestHeadersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRequestHeadersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRequestHeadersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRequestHeadersClient
        """
        return self._raw_client

    def get_headers_undeclared(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetHeadersUndeclaredResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHeadersUndeclaredResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.request_headers.get_headers_undeclared()
        """
        _response = self._raw_client.get_headers_undeclared(request_options=request_options)
        return _response.data

    def get_headers_request(
        self,
        *,
        route_level_header: typing.Optional[str] = None,
        number_header: typing.Optional[float] = None,
        boolean_header: typing.Optional[bool] = None,
        second_boolean_header: typing.Optional[bool] = None,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetHeadersRequestResponse:
        """
        Parameters
        ----------
        route_level_header : typing.Optional[str]

        number_header : typing.Optional[float]

        boolean_header : typing.Optional[bool]

        second_boolean_header : typing.Optional[bool]

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHeadersRequestResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.request_headers.get_headers_request()
        """
        _response = self._raw_client.get_headers_request(
            route_level_header=route_level_header,
            number_header=number_header,
            boolean_header=boolean_header,
            second_boolean_header=second_boolean_header,
            authorization=authorization,
            request_options=request_options,
        )
        return _response.data


class AsyncRequestHeadersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRequestHeadersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRequestHeadersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRequestHeadersClient
        """
        return self._raw_client

    async def get_headers_undeclared(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetHeadersUndeclaredResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHeadersUndeclaredResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.request_headers.get_headers_undeclared()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_headers_undeclared(request_options=request_options)
        return _response.data

    async def get_headers_request(
        self,
        *,
        route_level_header: typing.Optional[str] = None,
        number_header: typing.Optional[float] = None,
        boolean_header: typing.Optional[bool] = None,
        second_boolean_header: typing.Optional[bool] = None,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetHeadersRequestResponse:
        """
        Parameters
        ----------
        route_level_header : typing.Optional[str]

        number_header : typing.Optional[float]

        boolean_header : typing.Optional[bool]

        second_boolean_header : typing.Optional[bool]

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHeadersRequestResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.request_headers.get_headers_request()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_headers_request(
            route_level_header=route_level_header,
            number_header=number_header,
            boolean_header=boolean_header,
            second_boolean_header=second_boolean_header,
            authorization=authorization,
            request_options=request_options,
        )
        return _response.data

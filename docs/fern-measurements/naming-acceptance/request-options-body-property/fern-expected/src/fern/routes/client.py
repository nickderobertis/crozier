

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.route_page import RoutePage
from .raw_client import AsyncRawRoutesClient, RawRoutesClient


class RoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoutesClient
        """
        return self._raw_client

    def list_routes(
        self,
        *,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[str] = None,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[str, RoutePage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[str, RoutePage]
            a page of routes

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        response = client.routes.list_routes()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_routes(
            page=page, request_options=request_options, _request_options=_request_options
        )


class AsyncRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoutesClient
        """
        return self._raw_client

    async def list_routes(
        self,
        *,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[str] = None,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[str, RoutePage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[str, RoutePage]
            a page of routes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            response = await client.routes.list_routes()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_routes(
            page=page, request_options=request_options, _request_options=_request_options
        )

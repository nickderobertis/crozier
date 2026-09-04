

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.pagination import AsyncPager, SyncPager
from ...core.request_options import RequestOptions
from ...types.widget import Widget
from ...types.widget_page import WidgetPage
from .raw_client import AsyncRawWidgetsClient, RawWidgetsClient


class WidgetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWidgetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWidgetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWidgetsClient
        """
        return self._raw_client

    def list(
        self, *, page_token: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[Widget, WidgetPage]:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Opaque cursor from a previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Widget, WidgetPage]
            A page of widgets.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.catalog.widgets.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(page_token=page_token, request_options=request_options)


class AsyncWidgetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWidgetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWidgetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWidgetsClient
        """
        return self._raw_client

    async def list(
        self, *, page_token: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[Widget, WidgetPage]:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Opaque cursor from a previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Widget, WidgetPage]
            A page of widgets.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.catalog.widgets.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(page_token=page_token, request_options=request_options)

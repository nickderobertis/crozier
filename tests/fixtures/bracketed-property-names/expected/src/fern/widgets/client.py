

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWidgetsClient, RawWidgetsClient
from .types.search_widgets_response import SearchWidgetsResponse


OMIT = typing.cast(typing.Any, ...)


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

    def search_widgets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        filter_name: typing.Optional[str] = OMIT,
        filter_color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchWidgetsResponse:
        """
        Parameters
        ----------
        page_size : typing.Optional[int]

        page_number : typing.Optional[int]

        filter_name : typing.Optional[str]

        filter_color : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchWidgetsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.widgets.search_widgets()
        """
        _response = self._raw_client.search_widgets(
            page_size=page_size,
            page_number=page_number,
            filter_name=filter_name,
            filter_color=filter_color,
            request_options=request_options,
        )
        return _response.data


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

    async def search_widgets(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        filter_name: typing.Optional[str] = OMIT,
        filter_color: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchWidgetsResponse:
        """
        Parameters
        ----------
        page_size : typing.Optional[int]

        page_number : typing.Optional[int]

        filter_name : typing.Optional[str]

        filter_color : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchWidgetsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.widgets.search_widgets()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_widgets(
            page_size=page_size,
            page_number=page_number,
            filter_name=filter_name,
            filter_color=filter_color,
            request_options=request_options,
        )
        return _response.data

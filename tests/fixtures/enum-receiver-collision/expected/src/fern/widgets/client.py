

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.widget import Widget
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

    def list_widgets(self, *, request_options: typing.Optional[RequestOptions] = None) -> Widget:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Widget
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.widgets.list_widgets()
        """
        _response = self._raw_client.list_widgets(request_options=request_options)
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

    async def list_widgets(self, *, request_options: typing.Optional[RequestOptions] = None) -> Widget:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Widget
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.widgets.list_widgets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_widgets(request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWidgetpartClient, RawWidgetpartClient


class WidgetpartClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWidgetpartClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWidgetpartClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWidgetpartClient
        """
        return self._raw_client

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.widgetpart.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data


class AsyncWidgetpartClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWidgetpartClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWidgetpartClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWidgetpartClient
        """
        return self._raw_client

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.widgetpart.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

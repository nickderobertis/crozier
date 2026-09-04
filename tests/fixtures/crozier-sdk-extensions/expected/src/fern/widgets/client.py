

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.widget_event import WidgetEvent
from .raw_client import AsyncRawWidgetsClient, RawWidgetsClient


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

    def watch_stream(
        self, *, note: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[WidgetEvent]:
        """
        Parameters
        ----------
        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[WidgetEvent]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.widgets.watch_stream()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.watch_stream(note=note, request_options=request_options) as r:
            yield from r.data

    def watch(
        self, *, note: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> WidgetEvent:
        """
        Parameters
        ----------
        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WidgetEvent


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.widgets.watch()
        """
        _response = self._raw_client.watch(note=note, request_options=request_options)
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

    async def watch_stream(
        self, *, note: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[WidgetEvent]:
        """
        Parameters
        ----------
        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[WidgetEvent]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.widgets.watch_stream()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.watch_stream(note=note, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def watch(
        self, *, note: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> WidgetEvent:
        """
        Parameters
        ----------
        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WidgetEvent


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.widgets.watch()


        asyncio.run(main())
        """
        _response = await self._raw_client.watch(note=note, request_options=request_options)
        return _response.data

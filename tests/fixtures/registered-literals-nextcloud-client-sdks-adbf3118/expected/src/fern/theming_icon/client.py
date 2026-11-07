

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawThemingIconClient, RawThemingIconClient


class ThemingIconClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThemingIconClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThemingIconClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThemingIconClient
        """
        return self._raw_client

    def get_favicon(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Favicon returned
        """
        with self._raw_client.get_favicon(app, request_options=request_options) as r:
            yield from r.data

    def get_touch_icon(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Touch icon returned
        """
        with self._raw_client.get_touch_icon(app, request_options=request_options) as r:
            yield from r.data

    def get_themed_icon(
        self, app: str, image: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        app : str
            ID of the app

        image : str
            image file name (svg required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Themed icon returned
        """
        with self._raw_client.get_themed_icon(app, image, request_options=request_options) as r:
            yield from r.data


class AsyncThemingIconClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThemingIconClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThemingIconClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThemingIconClient
        """
        return self._raw_client

    async def get_favicon(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Favicon returned
        """
        async with self._raw_client.get_favicon(app, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_touch_icon(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Touch icon returned
        """
        async with self._raw_client.get_touch_icon(app, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_themed_icon(
        self, app: str, image: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        app : str
            ID of the app

        image : str
            image file name (svg required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Themed icon returned
        """
        async with self._raw_client.get_themed_icon(app, image, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

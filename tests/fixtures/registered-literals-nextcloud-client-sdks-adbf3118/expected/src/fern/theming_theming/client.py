

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.theming_theming_get_manifest200response import ThemingThemingGetManifest200Response
from .raw_client import AsyncRawThemingThemingClient, RawThemingThemingClient


class ThemingThemingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThemingThemingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThemingThemingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThemingThemingClient
        """
        return self._raw_client

    def get_theme_stylesheet(
        self,
        theme_id: str,
        *,
        plain: typing.Optional[int] = None,
        with_custom_css: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        theme_id : str
            ID of the theme

        plain : typing.Optional[int]
            Let the browser decide the CSS priority

        with_custom_css : typing.Optional[int]
            Include custom CSS

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Stylesheet returned
        """
        with self._raw_client.get_theme_stylesheet(
            theme_id, plain=plain, with_custom_css=with_custom_css, request_options=request_options
        ) as r:
            yield from r.data

    def get_image(
        self, key: str, *, use_svg: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        key : str
            Key of the image

        use_svg : typing.Optional[int]
            Return image as SVG

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Image returned
        """
        with self._raw_client.get_image(key, use_svg=use_svg, request_options=request_options) as r:
            yield from r.data

    def get_manifest(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThemingThemingGetManifest200Response:
        """
        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThemingThemingGetManifest200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theming_theming.get_manifest(
            app="app",
        )
        """
        _response = self._raw_client.get_manifest(app, request_options=request_options)
        return _response.data


class AsyncThemingThemingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThemingThemingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThemingThemingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThemingThemingClient
        """
        return self._raw_client

    async def get_theme_stylesheet(
        self,
        theme_id: str,
        *,
        plain: typing.Optional[int] = None,
        with_custom_css: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        theme_id : str
            ID of the theme

        plain : typing.Optional[int]
            Let the browser decide the CSS priority

        with_custom_css : typing.Optional[int]
            Include custom CSS

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Stylesheet returned
        """
        async with self._raw_client.get_theme_stylesheet(
            theme_id, plain=plain, with_custom_css=with_custom_css, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_image(
        self, key: str, *, use_svg: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        key : str
            Key of the image

        use_svg : typing.Optional[int]
            Return image as SVG

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Image returned
        """
        async with self._raw_client.get_image(key, use_svg=use_svg, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_manifest(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThemingThemingGetManifest200Response:
        """
        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThemingThemingGetManifest200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.theming_theming.get_manifest(
                app="app",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_manifest(app, request_options=request_options)
        return _response.data

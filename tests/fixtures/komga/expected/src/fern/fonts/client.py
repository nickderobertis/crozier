

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFontsClient, RawFontsClient


class FontsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFontsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFontsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFontsClient
        """
        return self._raw_client

    def get_fonts(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        List all available font families.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fonts.get_fonts()
        """
        _response = self._raw_client.get_fonts(request_options=request_options)
        return _response.data

    def get_font_family_as_css(
        self, font_family: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Download a CSS file with the @font-face block for the font family. This is used by the Epub Reader to change fonts.

        Parameters
        ----------
        font_family : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fonts.get_font_family_as_css(
            font_family="fontFamily",
        )
        """
        with self._raw_client.get_font_family_as_css(font_family, request_options=request_options) as r:
            yield from r.data

    def get_font_file(
        self, font_family: str, font_file: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        font_family : str

        font_file : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.fonts.get_font_file(
            font_family="fontFamily",
            font_file="fontFile",
        )
        """
        with self._raw_client.get_font_file(font_family, font_file, request_options=request_options) as r:
            yield from r.data


class AsyncFontsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFontsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFontsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFontsClient
        """
        return self._raw_client

    async def get_fonts(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        List all available font families.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fonts.get_fonts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fonts(request_options=request_options)
        return _response.data

    async def get_font_family_as_css(
        self, font_family: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Download a CSS file with the @font-face block for the font family. This is used by the Epub Reader to change fonts.

        Parameters
        ----------
        font_family : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fonts.get_font_family_as_css(
                font_family="fontFamily",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_font_family_as_css(font_family, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_font_file(
        self, font_family: str, font_file: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        font_family : str

        font_file : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.fonts.get_font_file(
                font_family="fontFamily",
                font_file="fontFile",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_font_file(font_family, font_file, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

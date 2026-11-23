

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_response import ExportResponse
from ..types.theme import Theme
from .raw_client import AsyncRawThemesClient, RawThemesClient


class ThemesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThemesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThemesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThemesClient
        """
        return self._raw_client

    def get_theme(self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Parameters
        ----------
        theme_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            The theme.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.themes.get_theme(
            theme_id="themeId",
        )
        """
        _response = self._raw_client.get_theme(theme_id, request_options=request_options)
        return _response.data

    def export_metadata(self, *, request_options: typing.Optional[RequestOptions] = None) -> ExportResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportResponse
            The exported metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.themes.export_metadata()
        """
        _response = self._raw_client.export_metadata(request_options=request_options)
        return _response.data


class AsyncThemesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThemesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThemesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThemesClient
        """
        return self._raw_client

    async def get_theme(self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Theme:
        """
        Parameters
        ----------
        theme_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Theme
            The theme.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.themes.get_theme(
                theme_id="themeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_theme(theme_id, request_options=request_options)
        return _response.data

    async def export_metadata(self, *, request_options: typing.Optional[RequestOptions] = None) -> ExportResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportResponse
            The exported metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.themes.export_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.export_metadata(request_options=request_options)
        return _response.data

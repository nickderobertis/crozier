

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.theming_background import ThemingBackground
from .raw_client import AsyncRawThemingUserThemeClient, RawThemingUserThemeClient


class ThemingUserThemeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThemingUserThemeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThemingUserThemeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThemingUserThemeClient
        """
        return self._raw_client

    def get_background(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Background image returned
        """
        with self._raw_client.get_background(request_options=request_options) as r:
            yield from r.data

    def set_background(
        self,
        type: str,
        *,
        value: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThemingBackground:
        """
        Parameters
        ----------
        type : str
            Type of background

        value : typing.Optional[str]
            Path of the background image

        color : typing.Optional[str]
            Color for the background

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThemingBackground
            Background set successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theming_user_theme.set_background(
            type="type",
        )
        """
        _response = self._raw_client.set_background(type, value=value, color=color, request_options=request_options)
        return _response.data

    def delete_background(self, *, request_options: typing.Optional[RequestOptions] = None) -> ThemingBackground:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThemingBackground


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theming_user_theme.delete_background()
        """
        _response = self._raw_client.delete_background(request_options=request_options)
        return _response.data

    def enable_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        theme_id : str
            the theme ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Theme enabled successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theming_user_theme.enable_theme(
            theme_id="themeId",
        )
        """
        _response = self._raw_client.enable_theme(theme_id, request_options=request_options)
        return _response.data

    def disable_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        theme_id : str
            the theme ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Theme disabled successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.theming_user_theme.disable_theme(
            theme_id="themeId",
        )
        """
        _response = self._raw_client.disable_theme(theme_id, request_options=request_options)
        return _response.data


class AsyncThemingUserThemeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThemingUserThemeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThemingUserThemeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThemingUserThemeClient
        """
        return self._raw_client

    async def get_background(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Background image returned
        """
        async with self._raw_client.get_background(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def set_background(
        self,
        type: str,
        *,
        value: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThemingBackground:
        """
        Parameters
        ----------
        type : str
            Type of background

        value : typing.Optional[str]
            Path of the background image

        color : typing.Optional[str]
            Color for the background

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThemingBackground
            Background set successfully

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
            await client.theming_user_theme.set_background(
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_background(
            type, value=value, color=color, request_options=request_options
        )
        return _response.data

    async def delete_background(self, *, request_options: typing.Optional[RequestOptions] = None) -> ThemingBackground:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThemingBackground


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
            await client.theming_user_theme.delete_background()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_background(request_options=request_options)
        return _response.data

    async def enable_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        theme_id : str
            the theme ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Theme enabled successfully

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
            await client.theming_user_theme.enable_theme(
                theme_id="themeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_theme(theme_id, request_options=request_options)
        return _response.data

    async def disable_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        theme_id : str
            the theme ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Theme disabled successfully

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
            await client.theming_user_theme.disable_theme(
                theme_id="themeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_theme(theme_id, request_options=request_options)
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_settings import CommonSettings
from .raw_client import AsyncRawSettingsClient, RawSettingsClient


class SettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSettingsClient
        """
        return self._raw_client

    def returns_current_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> CommonSettings:
        """
        Returns current settings. For users with the Standard Registry role only.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonSettings
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.settings.returns_current_settings()
        """
        _response = self._raw_client.returns_current_settings(request_options=request_options)
        return _response.data

    def set_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Set settings. For users with the Standard Registry role only.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.settings.set_settings()
        """
        _response = self._raw_client.set_settings(request_options=request_options)
        return _response.data

    def returns_current_environment_name(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns current environment name.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.settings.returns_current_environment_name()
        """
        _response = self._raw_client.returns_current_environment_name(request_options=request_options)
        return _response.data

    def settings_api_get_about(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.settings.settings_api_get_about()
        """
        _response = self._raw_client.settings_api_get_about(request_options=request_options)
        return _response.data


class AsyncSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSettingsClient
        """
        return self._raw_client

    async def returns_current_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommonSettings:
        """
        Returns current settings. For users with the Standard Registry role only.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonSettings
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.settings.returns_current_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_current_settings(request_options=request_options)
        return _response.data

    async def set_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Set settings. For users with the Standard Registry role only.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.settings.set_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_settings(request_options=request_options)
        return _response.data

    async def returns_current_environment_name(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns current environment name.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.settings.returns_current_environment_name()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_current_environment_name(request_options=request_options)
        return _response.data

    async def settings_api_get_about(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.settings.settings_api_get_about()


        asyncio.run(main())
        """
        _response = await self._raw_client.settings_api_get_about(request_options=request_options)
        return _response.data

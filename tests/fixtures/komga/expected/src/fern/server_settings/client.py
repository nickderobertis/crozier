

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.settings_dto import SettingsDto
from .raw_client import AsyncRawServerSettingsClient, RawServerSettingsClient
from .types.settings_update_dto_thumbnail_size import SettingsUpdateDtoThumbnailSize


OMIT = typing.cast(typing.Any, ...)


class ServerSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServerSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServerSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServerSettingsClient
        """
        return self._raw_client

    def get_server_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> SettingsDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.server_settings.get_server_settings()
        """
        _response = self._raw_client.get_server_settings(request_options=request_options)
        return _response.data

    def update_server_settings(
        self,
        *,
        delete_empty_collections: typing.Optional[bool] = OMIT,
        delete_empty_read_lists: typing.Optional[bool] = OMIT,
        kepubify_path: typing.Optional[str] = OMIT,
        kobo_port: typing.Optional[int] = OMIT,
        kobo_proxy: typing.Optional[bool] = OMIT,
        remember_me_duration_days: typing.Optional[int] = OMIT,
        renew_remember_me_key: typing.Optional[bool] = OMIT,
        server_context_path: typing.Optional[str] = OMIT,
        server_port: typing.Optional[int] = OMIT,
        task_pool_size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[SettingsUpdateDtoThumbnailSize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        You can omit fields you don't want to update

        Required role: **ADMIN**

        Parameters
        ----------
        delete_empty_collections : typing.Optional[bool]

        delete_empty_read_lists : typing.Optional[bool]

        kepubify_path : typing.Optional[str]
            Will be removed in a future version

        kobo_port : typing.Optional[int]

        kobo_proxy : typing.Optional[bool]

        remember_me_duration_days : typing.Optional[int]

        renew_remember_me_key : typing.Optional[bool]

        server_context_path : typing.Optional[str]

        server_port : typing.Optional[int]

        task_pool_size : typing.Optional[int]

        thumbnail_size : typing.Optional[SettingsUpdateDtoThumbnailSize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.server_settings.update_server_settings()
        """
        _response = self._raw_client.update_server_settings(
            delete_empty_collections=delete_empty_collections,
            delete_empty_read_lists=delete_empty_read_lists,
            kepubify_path=kepubify_path,
            kobo_port=kobo_port,
            kobo_proxy=kobo_proxy,
            remember_me_duration_days=remember_me_duration_days,
            renew_remember_me_key=renew_remember_me_key,
            server_context_path=server_context_path,
            server_port=server_port,
            task_pool_size=task_pool_size,
            thumbnail_size=thumbnail_size,
            request_options=request_options,
        )
        return _response.data


class AsyncServerSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServerSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServerSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServerSettingsClient
        """
        return self._raw_client

    async def get_server_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> SettingsDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.server_settings.get_server_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_server_settings(request_options=request_options)
        return _response.data

    async def update_server_settings(
        self,
        *,
        delete_empty_collections: typing.Optional[bool] = OMIT,
        delete_empty_read_lists: typing.Optional[bool] = OMIT,
        kepubify_path: typing.Optional[str] = OMIT,
        kobo_port: typing.Optional[int] = OMIT,
        kobo_proxy: typing.Optional[bool] = OMIT,
        remember_me_duration_days: typing.Optional[int] = OMIT,
        renew_remember_me_key: typing.Optional[bool] = OMIT,
        server_context_path: typing.Optional[str] = OMIT,
        server_port: typing.Optional[int] = OMIT,
        task_pool_size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[SettingsUpdateDtoThumbnailSize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        You can omit fields you don't want to update

        Required role: **ADMIN**

        Parameters
        ----------
        delete_empty_collections : typing.Optional[bool]

        delete_empty_read_lists : typing.Optional[bool]

        kepubify_path : typing.Optional[str]
            Will be removed in a future version

        kobo_port : typing.Optional[int]

        kobo_proxy : typing.Optional[bool]

        remember_me_duration_days : typing.Optional[int]

        renew_remember_me_key : typing.Optional[bool]

        server_context_path : typing.Optional[str]

        server_port : typing.Optional[int]

        task_pool_size : typing.Optional[int]

        thumbnail_size : typing.Optional[SettingsUpdateDtoThumbnailSize]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.server_settings.update_server_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_server_settings(
            delete_empty_collections=delete_empty_collections,
            delete_empty_read_lists=delete_empty_read_lists,
            kepubify_path=kepubify_path,
            kobo_port=kobo_port,
            kobo_proxy=kobo_proxy,
            remember_me_duration_days=remember_me_duration_days,
            renew_remember_me_key=renew_remember_me_key,
            server_context_path=server_context_path,
            server_port=server_port,
            task_pool_size=task_pool_size,
            thumbnail_size=thumbnail_size,
            request_options=request_options,
        )
        return _response.data

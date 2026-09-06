

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.client_setting_dto import ClientSettingDto
from ..types.client_setting_global_update_dto import ClientSettingGlobalUpdateDto
from ..types.client_setting_user_update_dto import ClientSettingUserUpdateDto
from .raw_client import AsyncRawClientSettingsClient, RawClientSettingsClient


OMIT = typing.cast(typing.Any, ...)


class ClientSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientSettingsClient
        """
        return self._raw_client

    def delete_global_settings(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Setting key should be a valid lowercase namespace string like 'application.domain.key'

        Required role: **ADMIN**

        Parameters
        ----------
        request : typing.Sequence[str]

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
        client.client_settings.delete_global_settings(
            request=["application.key1", "application.key2"],
        )
        """
        _response = self._raw_client.delete_global_settings(request=request, request_options=request_options)
        return _response.data

    def save_global_setting(
        self,
        *,
        request: typing.Dict[str, ClientSettingGlobalUpdateDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Setting key should be a valid lowercase namespace string like 'application.domain.key'

        Required role: **ADMIN**

        Parameters
        ----------
        request : typing.Dict[str, ClientSettingGlobalUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import ClientSettingGlobalUpdateDto, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.client_settings.save_global_setting(
            request={
                "application.key1": ClientSettingGlobalUpdateDto(
                    allow_unauthorized=True,
                    value="a string value",
                ),
                "application.key2": ClientSettingGlobalUpdateDto(
                    allow_unauthorized=False,
                    value='{"json":"object"}',
                ),
            },
        )
        """
        _response = self._raw_client.save_global_setting(request=request, request_options=request_options)
        return _response.data

    def get_global_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ClientSettingDto]:
        """
        For unauthenticated users, only settings with 'allowUnauthorized=true' will be returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ClientSettingDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.client_settings.get_global_settings()
        """
        _response = self._raw_client.get_global_settings(request_options=request_options)
        return _response.data

    def delete_user_settings(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Setting key should be a valid lowercase namespace string like 'application.domain.key'

        Parameters
        ----------
        request : typing.Sequence[str]

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
        client.client_settings.delete_user_settings(
            request=["application.key1", "application.key2"],
        )
        """
        _response = self._raw_client.delete_user_settings(request=request, request_options=request_options)
        return _response.data

    def save_user_setting(
        self,
        *,
        request: typing.Dict[str, ClientSettingUserUpdateDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Setting key should be a valid lowercase namespace string like 'application.domain.key'

        Parameters
        ----------
        request : typing.Dict[str, ClientSettingUserUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import ClientSettingUserUpdateDto, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.client_settings.save_user_setting(
            request={
                "application.key1": ClientSettingUserUpdateDto(
                    value="a string value",
                ),
                "application.key2": ClientSettingUserUpdateDto(
                    value='{"json":"object"}',
                ),
            },
        )
        """
        _response = self._raw_client.save_user_setting(request=request, request_options=request_options)
        return _response.data

    def get_user_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ClientSettingDto]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ClientSettingDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.client_settings.get_user_settings()
        """
        _response = self._raw_client.get_user_settings(request_options=request_options)
        return _response.data


class AsyncClientSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientSettingsClient
        """
        return self._raw_client

    async def delete_global_settings(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Setting key should be a valid lowercase namespace string like 'application.domain.key'

        Required role: **ADMIN**

        Parameters
        ----------
        request : typing.Sequence[str]

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
            await client.client_settings.delete_global_settings(
                request=["application.key1", "application.key2"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_global_settings(request=request, request_options=request_options)
        return _response.data

    async def save_global_setting(
        self,
        *,
        request: typing.Dict[str, ClientSettingGlobalUpdateDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Setting key should be a valid lowercase namespace string like 'application.domain.key'

        Required role: **ADMIN**

        Parameters
        ----------
        request : typing.Dict[str, ClientSettingGlobalUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ClientSettingGlobalUpdateDto

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.client_settings.save_global_setting(
                request={
                    "application.key1": ClientSettingGlobalUpdateDto(
                        allow_unauthorized=True,
                        value="a string value",
                    ),
                    "application.key2": ClientSettingGlobalUpdateDto(
                        allow_unauthorized=False,
                        value='{"json":"object"}',
                    ),
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_global_setting(request=request, request_options=request_options)
        return _response.data

    async def get_global_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ClientSettingDto]:
        """
        For unauthenticated users, only settings with 'allowUnauthorized=true' will be returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ClientSettingDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.client_settings.get_global_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_global_settings(request_options=request_options)
        return _response.data

    async def delete_user_settings(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Setting key should be a valid lowercase namespace string like 'application.domain.key'

        Parameters
        ----------
        request : typing.Sequence[str]

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
            await client.client_settings.delete_user_settings(
                request=["application.key1", "application.key2"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_settings(request=request, request_options=request_options)
        return _response.data

    async def save_user_setting(
        self,
        *,
        request: typing.Dict[str, ClientSettingUserUpdateDto],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Setting key should be a valid lowercase namespace string like 'application.domain.key'

        Parameters
        ----------
        request : typing.Dict[str, ClientSettingUserUpdateDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ClientSettingUserUpdateDto

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.client_settings.save_user_setting(
                request={
                    "application.key1": ClientSettingUserUpdateDto(
                        value="a string value",
                    ),
                    "application.key2": ClientSettingUserUpdateDto(
                        value='{"json":"object"}',
                    ),
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_user_setting(request=request, request_options=request_options)
        return _response.data

    async def get_user_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ClientSettingDto]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ClientSettingDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.client_settings.get_user_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_settings(request_options=request_options)
        return _response.data

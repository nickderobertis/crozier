

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.settings_policy_patch_request import SettingsPolicyPatchRequest
from ..types.settings_policy_response import SettingsPolicyResponse
from .raw_client import AsyncRawSettingsClient, RawSettingsClient


OMIT = typing.cast(typing.Any, ...)


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

    def get_settings_policy(self, *, request_options: typing.Optional[RequestOptions] = None) -> SettingsPolicyResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsPolicyResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.settings.get_settings_policy()
        """
        _response = self._raw_client.get_settings_policy(request_options=request_options)
        return _response.data

    def update_settings_policy(
        self, *, request: SettingsPolicyPatchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> SettingsPolicyResponse:
        """
        Parameters
        ----------
        request : SettingsPolicyPatchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsPolicyResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, SettingsPolicyPatchRequestPath

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.settings.update_settings_policy(
            request=SettingsPolicyPatchRequestPath(
                scope={"key": "value"},
                path={"key": "value"},
                value={"key": "value"},
            ),
        )
        """
        _response = self._raw_client.update_settings_policy(request=request, request_options=request_options)
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

    async def get_settings_policy(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SettingsPolicyResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsPolicyResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.settings.get_settings_policy()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_settings_policy(request_options=request_options)
        return _response.data

    async def update_settings_policy(
        self, *, request: SettingsPolicyPatchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> SettingsPolicyResponse:
        """
        Parameters
        ----------
        request : SettingsPolicyPatchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SettingsPolicyResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SettingsPolicyPatchRequestPath

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.settings.update_settings_policy(
                request=SettingsPolicyPatchRequestPath(
                    scope={"key": "value"},
                    path={"key": "value"},
                    value={"key": "value"},
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_settings_policy(request=request, request_options=request_options)
        return _response.data

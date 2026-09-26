

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_user_settings_response import GetUserSettingsResponse
from ..types.json_value import JsonValue
from ..types.list_user_settings_response import ListUserSettingsResponse
from ..types.put_user_settings_response import PutUserSettingsResponse
from ..types.user_settings_document_key import UserSettingsDocumentKey
from .raw_client import AsyncRawUserSettingsClient, RawUserSettingsClient


OMIT = typing.cast(typing.Any, ...)


class UserSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserSettingsClient
        """
        return self._raw_client

    def list_user_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUserSettingsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUserSettingsResponse
            List user settings documents

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_settings.list_user_settings()
        """
        _response = self._raw_client.list_user_settings(request_options=request_options)
        return _response.data

    def get_user_settings(
        self, document_key: UserSettingsDocumentKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserSettingsResponse:
        """
        Parameters
        ----------
        document_key : UserSettingsDocumentKey

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserSettingsResponse
            Get a user settings document

        Examples
        --------
        from fern import FernApi, UserSettingsDocumentKey

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_settings.get_user_settings(
            document_key=UserSettingsDocumentKey.MATCH_TIME_SETTINGS,
        )
        """
        _response = self._raw_client.get_user_settings(document_key, request_options=request_options)
        return _response.data

    def put_user_settings(
        self,
        document_key: UserSettingsDocumentKey,
        *,
        value: typing.Optional[JsonValue] = OMIT,
        expected_version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutUserSettingsResponse:
        """
        Parameters
        ----------
        document_key : UserSettingsDocumentKey

        value : typing.Optional[JsonValue]

        expected_version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutUserSettingsResponse
            Updated user settings document

        Examples
        --------
        from fern import FernApi, UserSettingsDocumentKey

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.user_settings.put_user_settings(
            document_key=UserSettingsDocumentKey.MATCH_TIME_SETTINGS,
        )
        """
        _response = self._raw_client.put_user_settings(
            document_key, value=value, expected_version=expected_version, request_options=request_options
        )
        return _response.data


class AsyncUserSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserSettingsClient
        """
        return self._raw_client

    async def list_user_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUserSettingsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUserSettingsResponse
            List user settings documents

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_settings.list_user_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_settings(request_options=request_options)
        return _response.data

    async def get_user_settings(
        self, document_key: UserSettingsDocumentKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserSettingsResponse:
        """
        Parameters
        ----------
        document_key : UserSettingsDocumentKey

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserSettingsResponse
            Get a user settings document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UserSettingsDocumentKey

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_settings.get_user_settings(
                document_key=UserSettingsDocumentKey.MATCH_TIME_SETTINGS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_settings(document_key, request_options=request_options)
        return _response.data

    async def put_user_settings(
        self,
        document_key: UserSettingsDocumentKey,
        *,
        value: typing.Optional[JsonValue] = OMIT,
        expected_version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutUserSettingsResponse:
        """
        Parameters
        ----------
        document_key : UserSettingsDocumentKey

        value : typing.Optional[JsonValue]

        expected_version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutUserSettingsResponse
            Updated user settings document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UserSettingsDocumentKey

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.user_settings.put_user_settings(
                document_key=UserSettingsDocumentKey.MATCH_TIME_SETTINGS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_user_settings(
            document_key, value=value, expected_version=expected_version, request_options=request_options
        )
        return _response.data

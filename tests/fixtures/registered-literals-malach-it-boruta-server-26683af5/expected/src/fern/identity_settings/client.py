

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentitySettingsClient, RawIdentitySettingsClient


OMIT = typing.cast(typing.Any, ...)


class IdentitySettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentitySettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentitySettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentitySettingsClient
        """
        return self._raw_client

    def display_account_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_settings.display_account_settings()
        """
        _response = self._raw_client.display_account_settings(request_options=request_options)
        return _response.data

    def update_account_settings(
        self,
        *,
        user_email: typing.Optional[str] = OMIT,
        user_password: typing.Optional[str] = OMIT,
        user_password_confirmation: typing.Optional[str] = OMIT,
        user_current_password: typing.Optional[str] = OMIT,
        user_metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        user_email : typing.Optional[str]

        user_password : typing.Optional[str]

        user_password_confirmation : typing.Optional[str]

        user_current_password : typing.Optional[str]

        user_metadata : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_settings.update_account_settings()
        """
        _response = self._raw_client.update_account_settings(
            user_email=user_email,
            user_password=user_password,
            user_password_confirmation=user_password_confirmation,
            user_current_password=user_current_password,
            user_metadata=user_metadata,
            request_options=request_options,
        )
        return _response.data

    def delete_the_current_account(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.identity_settings.delete_the_current_account()
        """
        _response = self._raw_client.delete_the_current_account(request_options=request_options)
        return _response.data


class AsyncIdentitySettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentitySettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentitySettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentitySettingsClient
        """
        return self._raw_client

    async def display_account_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_settings.display_account_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_account_settings(request_options=request_options)
        return _response.data

    async def update_account_settings(
        self,
        *,
        user_email: typing.Optional[str] = OMIT,
        user_password: typing.Optional[str] = OMIT,
        user_password_confirmation: typing.Optional[str] = OMIT,
        user_current_password: typing.Optional[str] = OMIT,
        user_metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        user_email : typing.Optional[str]

        user_password : typing.Optional[str]

        user_password_confirmation : typing.Optional[str]

        user_current_password : typing.Optional[str]

        user_metadata : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_settings.update_account_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_account_settings(
            user_email=user_email,
            user_password=user_password,
            user_password_confirmation=user_password_confirmation,
            user_current_password=user_current_password,
            user_metadata=user_metadata,
            request_options=request_options,
        )
        return _response.data

    async def delete_the_current_account(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.identity_settings.delete_the_current_account()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_the_current_account(request_options=request_options)
        return _response.data

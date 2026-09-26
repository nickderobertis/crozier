

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.auth_session_response import AuthSessionResponse
from ..types.ok_response import OkResponse
from ..types.update_profile_response import UpdateProfileResponse
from .raw_client import AsyncRawAuthClient, RawAuthClient


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def get_auth_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> AuthSessionResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthSessionResponse
            Get current auth session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth.get_auth_session()
        """
        _response = self._raw_client.get_auth_session(request_options=request_options)
        return _response.data

    def update_auth_profile(
        self, *, display_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateProfileResponse:
        """
        Parameters
        ----------
        display_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateProfileResponse
            Updated auth profile

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth.update_auth_profile(
            display_name="displayName",
        )
        """
        _response = self._raw_client.update_auth_profile(display_name=display_name, request_options=request_options)
        return _response.data

    def logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> OkResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            Logged out

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth.logout()
        """
        _response = self._raw_client.logout(request_options=request_options)
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def get_auth_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> AuthSessionResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthSessionResponse
            Get current auth session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth.get_auth_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_auth_session(request_options=request_options)
        return _response.data

    async def update_auth_profile(
        self, *, display_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateProfileResponse:
        """
        Parameters
        ----------
        display_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateProfileResponse
            Updated auth profile

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth.update_auth_profile(
                display_name="displayName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_auth_profile(
            display_name=display_name, request_options=request_options
        )
        return _response.data

    async def logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> OkResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            Logged out

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth.logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.logout(request_options=request_options)
        return _response.data

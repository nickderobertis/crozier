

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_user_info_response import GetUserInfoResponse
from .raw_client import AsyncRawUserClient, RawUserClient


class UserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserClient
        """
        return self._raw_client

    def get_current_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetUserInfoResponse:
        """
        Returns information about the currently authenticated user.

        The user information includes:

        - **Principal**: Unique identifier (email, UUID, etc.) from authentication system
        - **Display Name**: Human-readable name for display in UI
        - **Picture URL**: Optional avatar/profile picture URL

        The principal is extracted from the `X-Remote-User` header set by the upstream authentication proxy (oauth2-proxy, nginx, etc.).

        **Use Cases**:

        - Display user info in application header
        - Show "logged in as" indicators
        - Personalize UI with user's name/avatar
        - Verify authentication status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserInfoResponse
            User information retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.user.get_current_user()
        """
        _response = self._raw_client.get_current_user(request_options=request_options)
        return _response.data


class AsyncUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserClient
        """
        return self._raw_client

    async def get_current_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetUserInfoResponse:
        """
        Returns information about the currently authenticated user.

        The user information includes:

        - **Principal**: Unique identifier (email, UUID, etc.) from authentication system
        - **Display Name**: Human-readable name for display in UI
        - **Picture URL**: Optional avatar/profile picture URL

        The principal is extracted from the `X-Remote-User` header set by the upstream authentication proxy (oauth2-proxy, nginx, etc.).

        **Use Cases**:

        - Display user info in application header
        - Show "logged in as" indicators
        - Personalize UI with user's name/avatar
        - Verify authentication status

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserInfoResponse
            User information retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user.get_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user(request_options=request_options)
        return _response.data

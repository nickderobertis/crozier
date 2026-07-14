

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_info import UserInfo
from .raw_client import AsyncRawUsersClient, RawUsersClient


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def get_current_user_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserInfo:
        """
        Returns information about the currently authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfo
            Response when the endpoint is successfully invoked.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.users.get_current_user_info()
        """
        _response = self._raw_client.get_current_user_info(request_options=request_options)
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def get_current_user_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserInfo:
        """
        Returns information about the currently authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfo
            Response when the endpoint is successfully invoked.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.users.get_current_user_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user_info(request_options=request_options)
        return _response.data

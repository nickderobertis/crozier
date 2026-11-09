

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat_get_users_response import ChatGetUsersResponse
from .raw_client import AsyncRawChatUsersClient, RawChatUsersClient


class ChatUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChatUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChatUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChatUsersClient
        """
        return self._raw_client

    def chat_users_get_users(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatGetUsersResponse:
        """
        Get all the users

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatGetUsersResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chat_users.chat_users_get_users()
        """
        _response = self._raw_client.chat_users_get_users(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data


class AsyncChatUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChatUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChatUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChatUsersClient
        """
        return self._raw_client

    async def chat_users_get_users(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatGetUsersResponse:
        """
        Get all the users

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatGetUsersResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chat_users.chat_users_get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.chat_users_get_users(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data



import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPrivateMessagesClient, RawPrivateMessagesClient
from .types.get_user_sent_private_messages_response import GetUserSentPrivateMessagesResponse
from .types.list_user_private_messages_response import ListUserPrivateMessagesResponse


class PrivateMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrivateMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrivateMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrivateMessagesClient
        """
        return self._raw_client

    def get_user_sent_private_messages(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserSentPrivateMessagesResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserSentPrivateMessagesResponse
            private messages

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.private_messages.get_user_sent_private_messages(
            username="username",
        )
        """
        _response = self._raw_client.get_user_sent_private_messages(username, request_options=request_options)
        return _response.data

    def list_user_private_messages(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUserPrivateMessagesResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUserPrivateMessagesResponse
            private messages

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.private_messages.list_user_private_messages(
            username="username",
        )
        """
        _response = self._raw_client.list_user_private_messages(username, request_options=request_options)
        return _response.data


class AsyncPrivateMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrivateMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrivateMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrivateMessagesClient
        """
        return self._raw_client

    async def get_user_sent_private_messages(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserSentPrivateMessagesResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserSentPrivateMessagesResponse
            private messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.private_messages.get_user_sent_private_messages(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_sent_private_messages(username, request_options=request_options)
        return _response.data

    async def list_user_private_messages(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUserPrivateMessagesResponse:
        """
        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUserPrivateMessagesResponse
            private messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.private_messages.list_user_private_messages(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_private_messages(username, request_options=request_options)
        return _response.data

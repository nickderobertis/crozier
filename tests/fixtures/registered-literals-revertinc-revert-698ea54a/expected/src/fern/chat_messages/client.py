

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat_createor_update_message_response import ChatCreateorUpdateMessageResponse
from .raw_client import AsyncRawChatMessagesClient, RawChatMessagesClient


OMIT = typing.cast(typing.Any, ...)


class ChatMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChatMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChatMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChatMessagesClient
        """
        return self._raw_client

    def chat_messages_create_message(
        self, *, text: str, channel_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ChatCreateorUpdateMessageResponse:
        """
        Create a new message

        Parameters
        ----------
        text : str
            Message sent by user

        channel_id : str
            Id of channel to which message was sent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatCreateorUpdateMessageResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chat_messages.chat_messages_create_message(
            text="text",
            channel_id="channelId",
        )
        """
        _response = self._raw_client.chat_messages_create_message(
            text=text, channel_id=channel_id, request_options=request_options
        )
        return _response.data


class AsyncChatMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChatMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChatMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChatMessagesClient
        """
        return self._raw_client

    async def chat_messages_create_message(
        self, *, text: str, channel_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ChatCreateorUpdateMessageResponse:
        """
        Create a new message

        Parameters
        ----------
        text : str
            Message sent by user

        channel_id : str
            Id of channel to which message was sent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatCreateorUpdateMessageResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chat_messages.chat_messages_create_message(
                text="text",
                channel_id="channelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chat_messages_create_message(
            text=text, channel_id=channel_id, request_options=request_options
        )
        return _response.data

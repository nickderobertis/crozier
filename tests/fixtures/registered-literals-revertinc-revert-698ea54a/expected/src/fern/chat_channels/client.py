

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat_get_channels_response import ChatGetChannelsResponse
from .raw_client import AsyncRawChatChannelsClient, RawChatChannelsClient


class ChatChannelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChatChannelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChatChannelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChatChannelsClient
        """
        return self._raw_client

    def chat_channels_get_channels(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatGetChannelsResponse:
        """
        Get all the channels

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatGetChannelsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chat_channels.chat_channels_get_channels()
        """
        _response = self._raw_client.chat_channels_get_channels(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data


class AsyncChatChannelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChatChannelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChatChannelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChatChannelsClient
        """
        return self._raw_client

    async def chat_channels_get_channels(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatGetChannelsResponse:
        """
        Get all the channels

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatGetChannelsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chat_channels.chat_channels_get_channels()


        asyncio.run(main())
        """
        _response = await self._raw_client.chat_channels_get_channels(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

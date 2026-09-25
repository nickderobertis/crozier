

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat_message import ChatMessage
from .raw_client import AsyncRawChatClient, RawChatClient


OMIT = typing.cast(typing.Any, ...)


class ChatClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChatClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChatClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChatClient
        """
        return self._raw_client

    def list_chat_messages(
        self,
        group_slug: str,
        *,
        session_id: str,
        channel: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ChatMessage]:
        """
        Retrieve chat messages from a Skool group's chat.

        Parameters
        ----------
        group_slug : str

        session_id : str

        channel : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ChatMessage]
            List of chat messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.chat.list_chat_messages(
            group_slug="group_slug",
            session_id="session_id",
        )
        """
        _response = self._raw_client.list_chat_messages(
            group_slug, session_id=session_id, channel=channel, limit=limit, request_options=request_options
        )
        return _response.data

    def send_chat_message(
        self,
        group_slug: str,
        *,
        session_id: str,
        content: str,
        channel: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Send a message to a group chat channel.

        Parameters
        ----------
        group_slug : str

        session_id : str

        content : str

        channel : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.chat.send_chat_message(
            group_slug="group_slug",
            session_id="session_id",
            content="content",
        )
        """
        _response = self._raw_client.send_chat_message(
            group_slug, session_id=session_id, content=content, channel=channel, request_options=request_options
        )
        return _response.data


class AsyncChatClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChatClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChatClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChatClient
        """
        return self._raw_client

    async def list_chat_messages(
        self,
        group_slug: str,
        *,
        session_id: str,
        channel: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ChatMessage]:
        """
        Retrieve chat messages from a Skool group's chat.

        Parameters
        ----------
        group_slug : str

        session_id : str

        channel : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ChatMessage]
            List of chat messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.chat.list_chat_messages(
                group_slug="group_slug",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_chat_messages(
            group_slug, session_id=session_id, channel=channel, limit=limit, request_options=request_options
        )
        return _response.data

    async def send_chat_message(
        self,
        group_slug: str,
        *,
        session_id: str,
        content: str,
        channel: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Send a message to a group chat channel.

        Parameters
        ----------
        group_slug : str

        session_id : str

        content : str

        channel : typing.Optional[str]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.chat.send_chat_message(
                group_slug="group_slug",
                session_id="session_id",
                content="content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_chat_message(
            group_slug, session_id=session_id, content=content, channel=channel, request_options=request_options
        )
        return _response.data

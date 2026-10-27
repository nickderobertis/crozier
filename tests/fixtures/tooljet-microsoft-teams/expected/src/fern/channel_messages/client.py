

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat_message import ChatMessage
from ..types.chat_message_attachment import ChatMessageAttachment
from .raw_client import AsyncRawChannelMessagesClient, RawChannelMessagesClient
from .types.get_channel_message_request_expand import GetChannelMessageRequestExpand
from .types.list_channel_messages_request_expand import ListChannelMessagesRequestExpand
from .types.list_channel_messages_response import ListChannelMessagesResponse
from .types.send_channel_message_request_body import SendChannelMessageRequestBody
from .types.send_channel_message_request_hosted_contents_item import SendChannelMessageRequestHostedContentsItem
from .types.send_channel_message_request_importance import SendChannelMessageRequestImportance
from .types.send_channel_message_request_mentions_item import SendChannelMessageRequestMentionsItem
from .types.update_channel_message_request_body import UpdateChannelMessageRequestBody


OMIT = typing.cast(typing.Any, ...)


class ChannelMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChannelMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChannelMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChannelMessagesClient
        """
        return self._raw_client

    def list_channel_messages(
        self,
        team_id: str,
        channel_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        expand: typing.Optional[ListChannelMessagesRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChannelMessagesResponse:
        """
        Retrieve the list of messages in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        expand : typing.Optional[ListChannelMessagesRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChannelMessagesResponse
            Successfully retrieved channel messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channel_messages.list_channel_messages(
            team_id="team-id",
            channel_id="channel-id",
        )
        """
        _response = self._raw_client.list_channel_messages(
            team_id, channel_id, top=top, skip=skip, expand=expand, request_options=request_options
        )
        return _response.data

    def send_channel_message(
        self,
        team_id: str,
        channel_id: str,
        *,
        body: SendChannelMessageRequestBody,
        importance: typing.Optional[SendChannelMessageRequestImportance] = OMIT,
        subject: typing.Optional[str] = OMIT,
        mentions: typing.Optional[typing.Sequence[SendChannelMessageRequestMentionsItem]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ChatMessageAttachment]] = OMIT,
        hosted_contents: typing.Optional[typing.Sequence[SendChannelMessageRequestHostedContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatMessage:
        """
        Send a new message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        body : SendChannelMessageRequestBody

        importance : typing.Optional[SendChannelMessageRequestImportance]

        subject : typing.Optional[str]
            The subject of the channel message

        mentions : typing.Optional[typing.Sequence[SendChannelMessageRequestMentionsItem]]

        attachments : typing.Optional[typing.Sequence[ChatMessageAttachment]]

        hosted_contents : typing.Optional[typing.Sequence[SendChannelMessageRequestHostedContentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatMessage
            Message sent successfully

        Examples
        --------
        from fern.channel_messages import SendChannelMessageRequestBody

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channel_messages.send_channel_message(
            team_id="team-id",
            channel_id="channel-id",
            body=SendChannelMessageRequestBody(
                content="content",
            ),
        )
        """
        _response = self._raw_client.send_channel_message(
            team_id,
            channel_id,
            body=body,
            importance=importance,
            subject=subject,
            mentions=mentions,
            attachments=attachments,
            hosted_contents=hosted_contents,
            request_options=request_options,
        )
        return _response.data

    def get_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        expand: typing.Optional[GetChannelMessageRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatMessage:
        """
        Retrieve a specific message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        expand : typing.Optional[GetChannelMessageRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatMessage
            Successfully retrieved channel message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.channel_messages.get_channel_message(
            team_id="team-id",
            channel_id="channel-id",
            chat_message_id="chatMessage-id",
        )
        """
        _response = self._raw_client.get_channel_message(
            team_id, channel_id, chat_message_id, expand=expand, request_options=request_options
        )
        return _response.data

    def delete_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Soft delete a message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

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
        client.channel_messages.delete_channel_message(
            team_id="team-id",
            channel_id="channel-id",
            chat_message_id="chatMessage-id",
        )
        """
        _response = self._raw_client.delete_channel_message(
            team_id, channel_id, chat_message_id, request_options=request_options
        )
        return _response.data

    def update_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        body: typing.Optional[UpdateChannelMessageRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        body : typing.Optional[UpdateChannelMessageRequestBody]

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
        client.channel_messages.update_channel_message(
            team_id="team-id",
            channel_id="channel-id",
            chat_message_id="chatMessage-id",
        )
        """
        _response = self._raw_client.update_channel_message(
            team_id, channel_id, chat_message_id, body=body, request_options=request_options
        )
        return _response.data


class AsyncChannelMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChannelMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChannelMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChannelMessagesClient
        """
        return self._raw_client

    async def list_channel_messages(
        self,
        team_id: str,
        channel_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        expand: typing.Optional[ListChannelMessagesRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChannelMessagesResponse:
        """
        Retrieve the list of messages in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        expand : typing.Optional[ListChannelMessagesRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChannelMessagesResponse
            Successfully retrieved channel messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channel_messages.list_channel_messages(
                team_id="team-id",
                channel_id="channel-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_channel_messages(
            team_id, channel_id, top=top, skip=skip, expand=expand, request_options=request_options
        )
        return _response.data

    async def send_channel_message(
        self,
        team_id: str,
        channel_id: str,
        *,
        body: SendChannelMessageRequestBody,
        importance: typing.Optional[SendChannelMessageRequestImportance] = OMIT,
        subject: typing.Optional[str] = OMIT,
        mentions: typing.Optional[typing.Sequence[SendChannelMessageRequestMentionsItem]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ChatMessageAttachment]] = OMIT,
        hosted_contents: typing.Optional[typing.Sequence[SendChannelMessageRequestHostedContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatMessage:
        """
        Send a new message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        body : SendChannelMessageRequestBody

        importance : typing.Optional[SendChannelMessageRequestImportance]

        subject : typing.Optional[str]
            The subject of the channel message

        mentions : typing.Optional[typing.Sequence[SendChannelMessageRequestMentionsItem]]

        attachments : typing.Optional[typing.Sequence[ChatMessageAttachment]]

        hosted_contents : typing.Optional[typing.Sequence[SendChannelMessageRequestHostedContentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatMessage
            Message sent successfully

        Examples
        --------
        import asyncio

        from fern.channel_messages import SendChannelMessageRequestBody

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channel_messages.send_channel_message(
                team_id="team-id",
                channel_id="channel-id",
                body=SendChannelMessageRequestBody(
                    content="content",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_channel_message(
            team_id,
            channel_id,
            body=body,
            importance=importance,
            subject=subject,
            mentions=mentions,
            attachments=attachments,
            hosted_contents=hosted_contents,
            request_options=request_options,
        )
        return _response.data

    async def get_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        expand: typing.Optional[GetChannelMessageRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatMessage:
        """
        Retrieve a specific message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        expand : typing.Optional[GetChannelMessageRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatMessage
            Successfully retrieved channel message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.channel_messages.get_channel_message(
                team_id="team-id",
                channel_id="channel-id",
                chat_message_id="chatMessage-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_channel_message(
            team_id, channel_id, chat_message_id, expand=expand, request_options=request_options
        )
        return _response.data

    async def delete_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Soft delete a message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

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
            await client.channel_messages.delete_channel_message(
                team_id="team-id",
                channel_id="channel-id",
                chat_message_id="chatMessage-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_channel_message(
            team_id, channel_id, chat_message_id, request_options=request_options
        )
        return _response.data

    async def update_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        body: typing.Optional[UpdateChannelMessageRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        body : typing.Optional[UpdateChannelMessageRequestBody]

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
            await client.channel_messages.update_channel_message(
                team_id="team-id",
                channel_id="channel-id",
                chat_message_id="chatMessage-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_channel_message(
            team_id, channel_id, chat_message_id, body=body, request_options=request_options
        )
        return _response.data

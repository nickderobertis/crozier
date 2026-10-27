

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat_message import ChatMessage
from ..types.chat_message_attachment import ChatMessageAttachment
from .raw_client import AsyncRawChatMessagesClient, RawChatMessagesClient
from .types.get_all_messages_for_user_request_model import GetAllMessagesForUserRequestModel
from .types.get_all_messages_for_user_response import GetAllMessagesForUserResponse
from .types.get_chat_message_request_expand import GetChatMessageRequestExpand
from .types.list_chat_messages_response import ListChatMessagesResponse
from .types.send_chat_message_request_body import SendChatMessageRequestBody
from .types.send_chat_message_request_hosted_contents_item import SendChatMessageRequestHostedContentsItem
from .types.send_chat_message_request_importance import SendChatMessageRequestImportance
from .types.send_chat_message_request_mentions_item import SendChatMessageRequestMentionsItem
from .types.update_chat_message_request_body import UpdateChatMessageRequestBody


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

    def list_chat_messages(
        self,
        chat_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        orderby: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChatMessagesResponse:
        """
        Retrieve the list of messages in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        orderby : typing.Optional[str]
            OData orderby query

        filter : typing.Optional[str]
            OData filter query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChatMessagesResponse
            Successfully retrieved chat messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat_messages.list_chat_messages(
            chat_id="chat-id",
            orderby="createdDateTime desc",
            filter="lastModifiedDateTime gt 2022-09-22T00:00:00.000Z",
        )
        """
        _response = self._raw_client.list_chat_messages(
            chat_id, top=top, skip=skip, orderby=orderby, filter=filter, request_options=request_options
        )
        return _response.data

    def send_chat_message(
        self,
        chat_id: str,
        *,
        body: SendChatMessageRequestBody,
        importance: typing.Optional[SendChatMessageRequestImportance] = OMIT,
        mentions: typing.Optional[typing.Sequence[SendChatMessageRequestMentionsItem]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ChatMessageAttachment]] = OMIT,
        hosted_contents: typing.Optional[typing.Sequence[SendChatMessageRequestHostedContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatMessage:
        """
        Send a new message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        body : SendChatMessageRequestBody

        importance : typing.Optional[SendChatMessageRequestImportance]

        mentions : typing.Optional[typing.Sequence[SendChatMessageRequestMentionsItem]]

        attachments : typing.Optional[typing.Sequence[ChatMessageAttachment]]

        hosted_contents : typing.Optional[typing.Sequence[SendChatMessageRequestHostedContentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatMessage
            Message sent successfully

        Examples
        --------
        from fern.chat_messages import SendChatMessageRequestBody

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat_messages.send_chat_message(
            chat_id="chat-id",
            body=SendChatMessageRequestBody(
                content="content",
            ),
        )
        """
        _response = self._raw_client.send_chat_message(
            chat_id,
            body=body,
            importance=importance,
            mentions=mentions,
            attachments=attachments,
            hosted_contents=hosted_contents,
            request_options=request_options,
        )
        return _response.data

    def get_chat_message(
        self,
        chat_id: str,
        chat_message_id: str,
        *,
        expand: typing.Optional[GetChatMessageRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatMessage:
        """
        Retrieve a specific message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        expand : typing.Optional[GetChatMessageRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatMessage
            Successfully retrieved chat message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat_messages.get_chat_message(
            chat_id="chat-id",
            chat_message_id="chatMessage-id",
        )
        """
        _response = self._raw_client.get_chat_message(
            chat_id, chat_message_id, expand=expand, request_options=request_options
        )
        return _response.data

    def delete_chat_message(
        self, chat_id: str, chat_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Soft delete a message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

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
        client.chat_messages.delete_chat_message(
            chat_id="chat-id",
            chat_message_id="chatMessage-id",
        )
        """
        _response = self._raw_client.delete_chat_message(chat_id, chat_message_id, request_options=request_options)
        return _response.data

    def update_chat_message(
        self,
        chat_id: str,
        chat_message_id: str,
        *,
        body: typing.Optional[UpdateChatMessageRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        body : typing.Optional[UpdateChatMessageRequestBody]

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
        client.chat_messages.update_chat_message(
            chat_id="chat-id",
            chat_message_id="chatMessage-id",
        )
        """
        _response = self._raw_client.update_chat_message(
            chat_id, chat_message_id, body=body, request_options=request_options
        )
        return _response.data

    def get_all_messages_for_user(
        self,
        *,
        model: typing.Optional[GetAllMessagesForUserRequestModel] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAllMessagesForUserResponse:
        """
        Get all messages from all chats that a user is a participant in

        Parameters
        ----------
        model : typing.Optional[GetAllMessagesForUserRequestModel]
            Payment model for metered API

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAllMessagesForUserResponse
            Successfully retrieved all messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat_messages.get_all_messages_for_user()
        """
        _response = self._raw_client.get_all_messages_for_user(
            model=model, top=top, skip=skip, request_options=request_options
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

    async def list_chat_messages(
        self,
        chat_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        orderby: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChatMessagesResponse:
        """
        Retrieve the list of messages in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        orderby : typing.Optional[str]
            OData orderby query

        filter : typing.Optional[str]
            OData filter query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChatMessagesResponse
            Successfully retrieved chat messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat_messages.list_chat_messages(
                chat_id="chat-id",
                orderby="createdDateTime desc",
                filter="lastModifiedDateTime gt 2022-09-22T00:00:00.000Z",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_chat_messages(
            chat_id, top=top, skip=skip, orderby=orderby, filter=filter, request_options=request_options
        )
        return _response.data

    async def send_chat_message(
        self,
        chat_id: str,
        *,
        body: SendChatMessageRequestBody,
        importance: typing.Optional[SendChatMessageRequestImportance] = OMIT,
        mentions: typing.Optional[typing.Sequence[SendChatMessageRequestMentionsItem]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ChatMessageAttachment]] = OMIT,
        hosted_contents: typing.Optional[typing.Sequence[SendChatMessageRequestHostedContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatMessage:
        """
        Send a new message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        body : SendChatMessageRequestBody

        importance : typing.Optional[SendChatMessageRequestImportance]

        mentions : typing.Optional[typing.Sequence[SendChatMessageRequestMentionsItem]]

        attachments : typing.Optional[typing.Sequence[ChatMessageAttachment]]

        hosted_contents : typing.Optional[typing.Sequence[SendChatMessageRequestHostedContentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatMessage
            Message sent successfully

        Examples
        --------
        import asyncio

        from fern.chat_messages import SendChatMessageRequestBody

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat_messages.send_chat_message(
                chat_id="chat-id",
                body=SendChatMessageRequestBody(
                    content="content",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_chat_message(
            chat_id,
            body=body,
            importance=importance,
            mentions=mentions,
            attachments=attachments,
            hosted_contents=hosted_contents,
            request_options=request_options,
        )
        return _response.data

    async def get_chat_message(
        self,
        chat_id: str,
        chat_message_id: str,
        *,
        expand: typing.Optional[GetChatMessageRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatMessage:
        """
        Retrieve a specific message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        expand : typing.Optional[GetChatMessageRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatMessage
            Successfully retrieved chat message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat_messages.get_chat_message(
                chat_id="chat-id",
                chat_message_id="chatMessage-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_chat_message(
            chat_id, chat_message_id, expand=expand, request_options=request_options
        )
        return _response.data

    async def delete_chat_message(
        self, chat_id: str, chat_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Soft delete a message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

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
            await client.chat_messages.delete_chat_message(
                chat_id="chat-id",
                chat_message_id="chatMessage-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_chat_message(
            chat_id, chat_message_id, request_options=request_options
        )
        return _response.data

    async def update_chat_message(
        self,
        chat_id: str,
        chat_message_id: str,
        *,
        body: typing.Optional[UpdateChatMessageRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        body : typing.Optional[UpdateChatMessageRequestBody]

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
            await client.chat_messages.update_chat_message(
                chat_id="chat-id",
                chat_message_id="chatMessage-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_chat_message(
            chat_id, chat_message_id, body=body, request_options=request_options
        )
        return _response.data

    async def get_all_messages_for_user(
        self,
        *,
        model: typing.Optional[GetAllMessagesForUserRequestModel] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAllMessagesForUserResponse:
        """
        Get all messages from all chats that a user is a participant in

        Parameters
        ----------
        model : typing.Optional[GetAllMessagesForUserRequestModel]
            Payment model for metered API

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAllMessagesForUserResponse
            Successfully retrieved all messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat_messages.get_all_messages_for_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_messages_for_user(
            model=model, top=top, skip=skip, request_options=request_options
        )
        return _response.data

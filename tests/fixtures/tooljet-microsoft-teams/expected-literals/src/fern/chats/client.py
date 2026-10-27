

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat import Chat
from ..types.conversation_member_input import ConversationMemberInput
from .raw_client import AsyncRawChatsClient, RawChatsClient
from .types.create_chat_request_chat_type import CreateChatRequestChatType
from .types.create_chat_request_installed_apps_item import CreateChatRequestInstalledAppsItem
from .types.get_chat_request_expand import GetChatRequestExpand
from .types.list_chats_request_expand import ListChatsRequestExpand
from .types.list_chats_response import ListChatsResponse


OMIT = typing.cast(typing.Any, ...)


class ChatsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChatsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChatsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChatsClient
        """
        return self._raw_client

    def list_chats(
        self,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        orderby: typing.Optional[str] = None,
        expand: typing.Optional[ListChatsRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChatsResponse:
        """
        Retrieve the list of chats that the user is part of

        Parameters
        ----------
        top : typing.Optional[int]
            Number of items to return (default is 10, max is 50)

        skip : typing.Optional[int]
            Number of items to skip for pagination

        filter : typing.Optional[str]
            OData filter query

        orderby : typing.Optional[str]
            OData orderby query

        expand : typing.Optional[ListChatsRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChatsResponse
            Successfully retrieved chats

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chats.list_chats(
            orderby="lastMessagePreview/createdDateTime desc",
        )
        """
        _response = self._raw_client.list_chats(
            top=top, skip=skip, filter=filter, orderby=orderby, expand=expand, request_options=request_options
        )
        return _response.data

    def create_chat(
        self,
        *,
        chat_type: CreateChatRequestChatType,
        members: typing.Sequence[ConversationMemberInput],
        topic: typing.Optional[str] = OMIT,
        installed_apps: typing.Optional[typing.Sequence[CreateChatRequestInstalledAppsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Chat:
        """
        Create a new one-on-one or group chat

        Parameters
        ----------
        chat_type : CreateChatRequestChatType

        members : typing.Sequence[ConversationMemberInput]

        topic : typing.Optional[str]
            Subject or topic for the chat (only for group chats)

        installed_apps : typing.Optional[typing.Sequence[CreateChatRequestInstalledAppsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Chat
            Chat created successfully

        Examples
        --------
        from fern import ConversationMemberInput, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chats.create_chat(
            chat_type="oneOnOne",
            members=[
                ConversationMemberInput(
                    odata_type="#microsoft.graph.aadUserConversationMember",
                    user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
                )
            ],
        )
        """
        _response = self._raw_client.create_chat(
            chat_type=chat_type,
            members=members,
            topic=topic,
            installed_apps=installed_apps,
            request_options=request_options,
        )
        return _response.data

    def get_chat(
        self,
        chat_id: str,
        *,
        expand: typing.Optional[GetChatRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Chat:
        """
        Retrieve the properties and relationships of a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        expand : typing.Optional[GetChatRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Chat
            Successfully retrieved chat

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chats.get_chat(
            chat_id="chat-id",
        )
        """
        _response = self._raw_client.get_chat(chat_id, expand=expand, request_options=request_options)
        return _response.data

    def delete_chat(self, chat_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

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
        client.chats.delete_chat(
            chat_id="chat-id",
        )
        """
        _response = self._raw_client.delete_chat(chat_id, request_options=request_options)
        return _response.data

    def update_chat(
        self,
        chat_id: str,
        *,
        topic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the properties of a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        topic : typing.Optional[str]
            Subject or topic for the chat

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
        client.chats.update_chat(
            chat_id="chat-id",
        )
        """
        _response = self._raw_client.update_chat(chat_id, topic=topic, request_options=request_options)
        return _response.data


class AsyncChatsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChatsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChatsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChatsClient
        """
        return self._raw_client

    async def list_chats(
        self,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        orderby: typing.Optional[str] = None,
        expand: typing.Optional[ListChatsRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChatsResponse:
        """
        Retrieve the list of chats that the user is part of

        Parameters
        ----------
        top : typing.Optional[int]
            Number of items to return (default is 10, max is 50)

        skip : typing.Optional[int]
            Number of items to skip for pagination

        filter : typing.Optional[str]
            OData filter query

        orderby : typing.Optional[str]
            OData orderby query

        expand : typing.Optional[ListChatsRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChatsResponse
            Successfully retrieved chats

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chats.list_chats(
                orderby="lastMessagePreview/createdDateTime desc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_chats(
            top=top, skip=skip, filter=filter, orderby=orderby, expand=expand, request_options=request_options
        )
        return _response.data

    async def create_chat(
        self,
        *,
        chat_type: CreateChatRequestChatType,
        members: typing.Sequence[ConversationMemberInput],
        topic: typing.Optional[str] = OMIT,
        installed_apps: typing.Optional[typing.Sequence[CreateChatRequestInstalledAppsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Chat:
        """
        Create a new one-on-one or group chat

        Parameters
        ----------
        chat_type : CreateChatRequestChatType

        members : typing.Sequence[ConversationMemberInput]

        topic : typing.Optional[str]
            Subject or topic for the chat (only for group chats)

        installed_apps : typing.Optional[typing.Sequence[CreateChatRequestInstalledAppsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Chat
            Chat created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConversationMemberInput

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chats.create_chat(
                chat_type="oneOnOne",
                members=[
                    ConversationMemberInput(
                        odata_type="#microsoft.graph.aadUserConversationMember",
                        user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_chat(
            chat_type=chat_type,
            members=members,
            topic=topic,
            installed_apps=installed_apps,
            request_options=request_options,
        )
        return _response.data

    async def get_chat(
        self,
        chat_id: str,
        *,
        expand: typing.Optional[GetChatRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Chat:
        """
        Retrieve the properties and relationships of a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        expand : typing.Optional[GetChatRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Chat
            Successfully retrieved chat

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chats.get_chat(
                chat_id="chat-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_chat(chat_id, expand=expand, request_options=request_options)
        return _response.data

    async def delete_chat(self, chat_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

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
            await client.chats.delete_chat(
                chat_id="chat-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_chat(chat_id, request_options=request_options)
        return _response.data

    async def update_chat(
        self,
        chat_id: str,
        *,
        topic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the properties of a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        topic : typing.Optional[str]
            Subject or topic for the chat

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
            await client.chats.update_chat(
                chat_id="chat-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_chat(chat_id, topic=topic, request_options=request_options)
        return _response.data

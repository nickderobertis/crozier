

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.conversation_member import ConversationMember
from ..types.conversation_member_input import ConversationMemberInput
from ..types.conversation_member_input_roles_item import ConversationMemberInputRolesItem
from .raw_client import AsyncRawChatMembersClient, RawChatMembersClient
from .types.add_multiple_chat_members_response_item import AddMultipleChatMembersResponseItem
from .types.list_chat_members_response import ListChatMembersResponse
from .types.update_chat_member_request_roles_item import UpdateChatMemberRequestRolesItem


OMIT = typing.cast(typing.Any, ...)


class ChatMembersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChatMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChatMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChatMembersClient
        """
        return self._raw_client

    def list_chat_members(
        self,
        chat_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChatMembersResponse:
        """
        Retrieve a list of members in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChatMembersResponse
            Successfully retrieved chat members

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat_members.list_chat_members(
            chat_id="chat-id",
        )
        """
        _response = self._raw_client.list_chat_members(chat_id, top=top, skip=skip, request_options=request_options)
        return _response.data

    def add_chat_member(
        self,
        chat_id: str,
        *,
        odata_type: str,
        user_odata_bind: str,
        roles: typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]] = OMIT,
        visible_history_start_date_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationMember:
        """
        Add a member to a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        odata_type : str

        user_odata_bind : str

        roles : typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]]

        visible_history_start_date_time : typing.Optional[dt.datetime]
            Timestamp from which the member can see messages

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationMember
            Member added successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat_members.add_chat_member(
            chat_id="chat-id",
            odata_type="#microsoft.graph.aadUserConversationMember",
            user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
        )
        """
        _response = self._raw_client.add_chat_member(
            chat_id,
            odata_type=odata_type,
            user_odata_bind=user_odata_bind,
            roles=roles,
            visible_history_start_date_time=visible_history_start_date_time,
            request_options=request_options,
        )
        return _response.data

    def add_multiple_chat_members(
        self,
        chat_id: str,
        *,
        values: typing.Sequence[ConversationMemberInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AddMultipleChatMembersResponseItem]:
        """
        Add multiple members to a chat in a single request

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        values : typing.Sequence[ConversationMemberInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AddMultipleChatMembersResponseItem]
            Members addition completed

        Examples
        --------
        from fern import ConversationMemberInput, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat_members.add_multiple_chat_members(
            chat_id="chat-id",
            values=[
                ConversationMemberInput(
                    odata_type="#microsoft.graph.aadUserConversationMember",
                    user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
                )
            ],
        )
        """
        _response = self._raw_client.add_multiple_chat_members(chat_id, values=values, request_options=request_options)
        return _response.data

    def get_chat_member(
        self, chat_id: str, conversation_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConversationMember:
        """
        Retrieve a specific member of a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        conversation_member_id : str
            The unique identifier of the conversation member

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationMember
            Successfully retrieved chat member

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chat_members.get_chat_member(
            chat_id="chat-id",
            conversation_member_id="conversationMember-id",
        )
        """
        _response = self._raw_client.get_chat_member(chat_id, conversation_member_id, request_options=request_options)
        return _response.data

    def remove_chat_member(
        self, chat_id: str, conversation_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a member from a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        conversation_member_id : str
            The unique identifier of the conversation member

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
        client.chat_members.remove_chat_member(
            chat_id="chat-id",
            conversation_member_id="conversationMember-id",
        )
        """
        _response = self._raw_client.remove_chat_member(
            chat_id, conversation_member_id, request_options=request_options
        )
        return _response.data

    def update_chat_member(
        self,
        chat_id: str,
        conversation_member_id: str,
        *,
        odata_type: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[UpdateChatMemberRequestRolesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a member's role in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        conversation_member_id : str
            The unique identifier of the conversation member

        odata_type : typing.Optional[str]

        roles : typing.Optional[typing.Sequence[UpdateChatMemberRequestRolesItem]]

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
        client.chat_members.update_chat_member(
            chat_id="chat-id",
            conversation_member_id="conversationMember-id",
        )
        """
        _response = self._raw_client.update_chat_member(
            chat_id, conversation_member_id, odata_type=odata_type, roles=roles, request_options=request_options
        )
        return _response.data


class AsyncChatMembersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChatMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChatMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChatMembersClient
        """
        return self._raw_client

    async def list_chat_members(
        self,
        chat_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChatMembersResponse:
        """
        Retrieve a list of members in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListChatMembersResponse
            Successfully retrieved chat members

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat_members.list_chat_members(
                chat_id="chat-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_chat_members(
            chat_id, top=top, skip=skip, request_options=request_options
        )
        return _response.data

    async def add_chat_member(
        self,
        chat_id: str,
        *,
        odata_type: str,
        user_odata_bind: str,
        roles: typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]] = OMIT,
        visible_history_start_date_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationMember:
        """
        Add a member to a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        odata_type : str

        user_odata_bind : str

        roles : typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]]

        visible_history_start_date_time : typing.Optional[dt.datetime]
            Timestamp from which the member can see messages

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationMember
            Member added successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat_members.add_chat_member(
                chat_id="chat-id",
                odata_type="#microsoft.graph.aadUserConversationMember",
                user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_chat_member(
            chat_id,
            odata_type=odata_type,
            user_odata_bind=user_odata_bind,
            roles=roles,
            visible_history_start_date_time=visible_history_start_date_time,
            request_options=request_options,
        )
        return _response.data

    async def add_multiple_chat_members(
        self,
        chat_id: str,
        *,
        values: typing.Sequence[ConversationMemberInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AddMultipleChatMembersResponseItem]:
        """
        Add multiple members to a chat in a single request

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        values : typing.Sequence[ConversationMemberInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AddMultipleChatMembersResponseItem]
            Members addition completed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConversationMemberInput

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat_members.add_multiple_chat_members(
                chat_id="chat-id",
                values=[
                    ConversationMemberInput(
                        odata_type="#microsoft.graph.aadUserConversationMember",
                        user_odata_bind="https://graph.microsoft.com/v1.0/users('userId')",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_multiple_chat_members(
            chat_id, values=values, request_options=request_options
        )
        return _response.data

    async def get_chat_member(
        self, chat_id: str, conversation_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConversationMember:
        """
        Retrieve a specific member of a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        conversation_member_id : str
            The unique identifier of the conversation member

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationMember
            Successfully retrieved chat member

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chat_members.get_chat_member(
                chat_id="chat-id",
                conversation_member_id="conversationMember-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_chat_member(
            chat_id, conversation_member_id, request_options=request_options
        )
        return _response.data

    async def remove_chat_member(
        self, chat_id: str, conversation_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a member from a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        conversation_member_id : str
            The unique identifier of the conversation member

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
            await client.chat_members.remove_chat_member(
                chat_id="chat-id",
                conversation_member_id="conversationMember-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_chat_member(
            chat_id, conversation_member_id, request_options=request_options
        )
        return _response.data

    async def update_chat_member(
        self,
        chat_id: str,
        conversation_member_id: str,
        *,
        odata_type: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[UpdateChatMemberRequestRolesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a member's role in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        conversation_member_id : str
            The unique identifier of the conversation member

        odata_type : typing.Optional[str]

        roles : typing.Optional[typing.Sequence[UpdateChatMemberRequestRolesItem]]

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
            await client.chat_members.update_chat_member(
                chat_id="chat-id",
                conversation_member_id="conversationMember-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_chat_member(
            chat_id, conversation_member_id, odata_type=odata_type, roles=roles, request_options=request_options
        )
        return _response.data

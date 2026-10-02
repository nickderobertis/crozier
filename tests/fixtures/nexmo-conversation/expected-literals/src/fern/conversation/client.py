

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.action import Action
from ..types.display_name import DisplayName
from ..types.event_method import EventMethod
from ..types.event_url import EventUrl
from ..types.format import Format
from ..types.image_url import ImageUrl
from ..types.name_conversation import NameConversation
from ..types.page_size import PageSize
from ..types.record_index import RecordIndex
from ..types.split import Split
from .raw_client import AsyncRawConversationClient, RawConversationClient
from .types.create_conversation_request_properties import CreateConversationRequestProperties
from .types.create_conversation_response import CreateConversationResponse
from .types.list_conversations_request_order import ListConversationsRequestOrder
from .types.list_conversations_response import ListConversationsResponse
from .types.replace_conversation_request_properties import ReplaceConversationRequestProperties
from .types.replace_conversation_response import ReplaceConversationResponse
from .types.retrieve_conversation_response import RetrieveConversationResponse


OMIT = typing.cast(typing.Any, ...)


class ConversationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConversationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConversationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConversationClient
        """
        return self._raw_client

    def list_conversations(
        self,
        *,
        date_start: typing.Optional[str] = None,
        date_end: typing.Optional[str] = None,
        page_size: typing.Optional[PageSize] = None,
        record_index: typing.Optional[RecordIndex] = None,
        order: typing.Optional[ListConversationsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListConversationsResponse:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/conversations](/api/conversation.v2#get-conversations).

        List all conversations associated with your application. This endpoint required an admin JWT. To find all conversations for the currently logged in user, see [GET /users/:id/conversations](#getuserConversations)

        Parameters
        ----------
        date_start : typing.Optional[str]
            Return the records that occurred after this point in time.

        date_end : typing.Optional[str]
            Return the records that occurred before this point in time.

        page_size : typing.Optional[PageSize]
            Return this amount of records in the response

        record_index : typing.Optional[RecordIndex]
            Return calls from this index in the response

        order : typing.Optional[ListConversationsRequestOrder]
            Return the records in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListConversationsResponse
            List Conversations Response Payload Object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversation.list_conversations(
            page_size=50.0,
            record_index=0.0,
        )
        """
        _response = self._raw_client.list_conversations(
            date_start=date_start,
            date_end=date_end,
            page_size=page_size,
            record_index=record_index,
            order=order,
            request_options=request_options,
        )
        return _response.data

    def create_conversation(
        self,
        *,
        display_name: typing.Optional[DisplayName] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameConversation] = OMIT,
        properties: typing.Optional[CreateConversationRequestProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConversationResponse:
        """
        Parameters
        ----------
        display_name : typing.Optional[DisplayName]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameConversation]

        properties : typing.Optional[CreateConversationRequestProperties]
            Conversation properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConversationResponse
            Create / Update Conversation Response Payload Object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversation.create_conversation()
        """
        _response = self._raw_client.create_conversation(
            display_name=display_name,
            image_url=image_url,
            name=name,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def retrieve_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveConversationResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveConversationResponse
            Retrieve a conversation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversation.retrieve_conversation(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
        )
        """
        _response = self._raw_client.retrieve_conversation(conversation_id, request_options=request_options)
        return _response.data

    def replace_conversation(
        self,
        conversation_id: str,
        *,
        display_name: typing.Optional[DisplayName] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameConversation] = OMIT,
        properties: typing.Optional[ReplaceConversationRequestProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceConversationResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        display_name : typing.Optional[DisplayName]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameConversation]

        properties : typing.Optional[ReplaceConversationRequestProperties]
            Conversation properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceConversationResponse
            Create / Update Conversation Response Payload Object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversation.replace_conversation(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
        )
        """
        _response = self._raw_client.replace_conversation(
            conversation_id,
            display_name=display_name,
            image_url=image_url,
            name=name,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def delete_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversation.delete_conversation(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
        )
        """
        _response = self._raw_client.delete_conversation(conversation_id, request_options=request_options)
        return _response.data

    def record_conversation(
        self,
        conversation_id: str,
        *,
        action: Action,
        event_method: typing.Optional[EventMethod] = OMIT,
        event_url: typing.Optional[EventUrl] = OMIT,
        format: typing.Optional[Format] = OMIT,
        split: typing.Optional[Split] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        action : Action

        event_method : typing.Optional[EventMethod]

        event_url : typing.Optional[EventUrl]

        format : typing.Optional[Format]

        split : typing.Optional[Split]

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
        client.conversation.record_conversation(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            action="start",
        )
        """
        _response = self._raw_client.record_conversation(
            conversation_id,
            action=action,
            event_method=event_method,
            event_url=event_url,
            format=format,
            split=split,
            request_options=request_options,
        )
        return _response.data


class AsyncConversationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConversationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConversationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConversationClient
        """
        return self._raw_client

    async def list_conversations(
        self,
        *,
        date_start: typing.Optional[str] = None,
        date_end: typing.Optional[str] = None,
        page_size: typing.Optional[PageSize] = None,
        record_index: typing.Optional[RecordIndex] = None,
        order: typing.Optional[ListConversationsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListConversationsResponse:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/conversations](/api/conversation.v2#get-conversations).

        List all conversations associated with your application. This endpoint required an admin JWT. To find all conversations for the currently logged in user, see [GET /users/:id/conversations](#getuserConversations)

        Parameters
        ----------
        date_start : typing.Optional[str]
            Return the records that occurred after this point in time.

        date_end : typing.Optional[str]
            Return the records that occurred before this point in time.

        page_size : typing.Optional[PageSize]
            Return this amount of records in the response

        record_index : typing.Optional[RecordIndex]
            Return calls from this index in the response

        order : typing.Optional[ListConversationsRequestOrder]
            Return the records in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListConversationsResponse
            List Conversations Response Payload Object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversation.list_conversations(
                page_size=50.0,
                record_index=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_conversations(
            date_start=date_start,
            date_end=date_end,
            page_size=page_size,
            record_index=record_index,
            order=order,
            request_options=request_options,
        )
        return _response.data

    async def create_conversation(
        self,
        *,
        display_name: typing.Optional[DisplayName] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameConversation] = OMIT,
        properties: typing.Optional[CreateConversationRequestProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConversationResponse:
        """
        Parameters
        ----------
        display_name : typing.Optional[DisplayName]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameConversation]

        properties : typing.Optional[CreateConversationRequestProperties]
            Conversation properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConversationResponse
            Create / Update Conversation Response Payload Object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversation.create_conversation()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_conversation(
            display_name=display_name,
            image_url=image_url,
            name=name,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveConversationResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveConversationResponse
            Retrieve a conversation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversation.retrieve_conversation(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_conversation(conversation_id, request_options=request_options)
        return _response.data

    async def replace_conversation(
        self,
        conversation_id: str,
        *,
        display_name: typing.Optional[DisplayName] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameConversation] = OMIT,
        properties: typing.Optional[ReplaceConversationRequestProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceConversationResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        display_name : typing.Optional[DisplayName]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameConversation]

        properties : typing.Optional[ReplaceConversationRequestProperties]
            Conversation properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceConversationResponse
            Create / Update Conversation Response Payload Object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversation.replace_conversation(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_conversation(
            conversation_id,
            display_name=display_name,
            image_url=image_url,
            name=name,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def delete_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversation.delete_conversation(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_conversation(conversation_id, request_options=request_options)
        return _response.data

    async def record_conversation(
        self,
        conversation_id: str,
        *,
        action: Action,
        event_method: typing.Optional[EventMethod] = OMIT,
        event_url: typing.Optional[EventUrl] = OMIT,
        format: typing.Optional[Format] = OMIT,
        split: typing.Optional[Split] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        action : Action

        event_method : typing.Optional[EventMethod]

        event_url : typing.Optional[EventUrl]

        format : typing.Optional[Format]

        split : typing.Optional[Split]

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
            await client.conversation.record_conversation(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
                action="start",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_conversation(
            conversation_id,
            action=action,
            event_method=event_method,
            event_url=event_url,
            format=format,
            split=split,
            request_options=request_options,
        )
        return _response.data

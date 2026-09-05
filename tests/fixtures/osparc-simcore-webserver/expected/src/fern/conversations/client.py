

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.conversation_message_type import ConversationMessageType
from ..types.conversation_name import ConversationName
from ..types.conversation_status import ConversationStatus
from ..types.conversation_type import ConversationType
from ..types.envelope_conversation_message_rest_get import EnvelopeConversationMessageRestGet
from ..types.envelope_conversation_rest_get import EnvelopeConversationRestGet
from ..types.page_conversation_message_rest_get import PageConversationMessageRestGet
from ..types.page_conversation_rest_get import PageConversationRestGet
from .raw_client import AsyncRawConversationsClient, RawConversationsClient


OMIT = typing.cast(typing.Any, ...)


class ConversationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConversationsClient
        """
        return self._raw_client

    def list_conversations(
        self,
        *,
        type: ConversationType,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ConversationStatus] = None,
        is_read_by_user: typing.Optional[bool] = None,
        is_read_by_support: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageConversationRestGet:
        """
        Parameters
        ----------
        type : ConversationType

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[ConversationStatus]

        is_read_by_user : typing.Optional[bool]

        is_read_by_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageConversationRestGet
            Successful Response

        Examples
        --------
        from fern import ConversationType, FernApi

        client = FernApi()
        client.conversations.list_conversations(
            type=ConversationType.PROJECT_STATIC,
        )
        """
        _response = self._raw_client.list_conversations(
            type=type,
            limit=limit,
            offset=offset,
            status=status,
            is_read_by_user=is_read_by_user,
            is_read_by_support=is_read_by_support,
            request_options=request_options,
        )
        return _response.data

    def create_conversation(
        self,
        *,
        type: ConversationType,
        name: typing.Optional[ConversationName] = OMIT,
        extra_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        type : ConversationType

        name : typing.Optional[ConversationName]

        extra_context : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        from fern import ConversationType, FernApi

        client = FernApi()
        client.conversations.create_conversation(
            type=ConversationType.PROJECT_STATIC,
        )
        """
        _response = self._raw_client.create_conversation(
            type=type, name=name, extra_context=extra_context, request_options=request_options
        )
        return _response.data

    def get_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversations.get_conversation(
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.get_conversation(conversation_id, request_options=request_options)
        return _response.data

    def delete_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversations.delete_conversation(
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.delete_conversation(conversation_id, request_options=request_options)
        return _response.data

    def update_conversation(
        self,
        conversation_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        extra_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        is_read_by_user: typing.Optional[bool] = OMIT,
        is_read_by_support: typing.Optional[bool] = OMIT,
        status: typing.Optional[ConversationStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        name : typing.Optional[str]

        extra_context : typing.Optional[typing.Dict[str, typing.Any]]

        is_read_by_user : typing.Optional[bool]

        is_read_by_support : typing.Optional[bool]

        status : typing.Optional[ConversationStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversations.update_conversation(
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.update_conversation(
            conversation_id,
            name=name,
            extra_context=extra_context,
            is_read_by_user=is_read_by_user,
            is_read_by_support=is_read_by_support,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def list_conversation_messages(
        self,
        conversation_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageConversationMessageRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageConversationMessageRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversations.list_conversation_messages(
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.list_conversation_messages(
            conversation_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def create_conversation_message(
        self,
        conversation_id: str,
        *,
        content: str,
        type: ConversationMessageType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        content : str

        type : ConversationMessageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        from fern import ConversationMessageType, FernApi

        client = FernApi()
        client.conversations.create_conversation_message(
            conversation_id="conversation_id",
            content="content",
            type=ConversationMessageType.MESSAGE,
        )
        """
        _response = self._raw_client.create_conversation_message(
            conversation_id, content=content, type=type, request_options=request_options
        )
        return _response.data

    def get_conversation_message(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversations.get_conversation_message(
            conversation_id="conversation_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.get_conversation_message(
            conversation_id, message_id, request_options=request_options
        )
        return _response.data

    def update_conversation_message(
        self,
        conversation_id: str,
        message_id: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversations.update_conversation_message(
            conversation_id="conversation_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.update_conversation_message(
            conversation_id, message_id, content=content, request_options=request_options
        )
        return _response.data

    def delete_conversation_message(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversations.delete_conversation_message(
            conversation_id="conversation_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.delete_conversation_message(
            conversation_id, message_id, request_options=request_options
        )
        return _response.data

    def trigger_chatbot_processing(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.conversations.trigger_chatbot_processing(
            conversation_id="conversation_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.trigger_chatbot_processing(
            conversation_id, message_id, request_options=request_options
        )
        return _response.data


class AsyncConversationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConversationsClient
        """
        return self._raw_client

    async def list_conversations(
        self,
        *,
        type: ConversationType,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ConversationStatus] = None,
        is_read_by_user: typing.Optional[bool] = None,
        is_read_by_support: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageConversationRestGet:
        """
        Parameters
        ----------
        type : ConversationType

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[ConversationStatus]

        is_read_by_user : typing.Optional[bool]

        is_read_by_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageConversationRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConversationType

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.list_conversations(
                type=ConversationType.PROJECT_STATIC,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_conversations(
            type=type,
            limit=limit,
            offset=offset,
            status=status,
            is_read_by_user=is_read_by_user,
            is_read_by_support=is_read_by_support,
            request_options=request_options,
        )
        return _response.data

    async def create_conversation(
        self,
        *,
        type: ConversationType,
        name: typing.Optional[ConversationName] = OMIT,
        extra_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        type : ConversationType

        name : typing.Optional[ConversationName]

        extra_context : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConversationType

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.create_conversation(
                type=ConversationType.PROJECT_STATIC,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_conversation(
            type=type, name=name, extra_context=extra_context, request_options=request_options
        )
        return _response.data

    async def get_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.get_conversation(
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conversation(conversation_id, request_options=request_options)
        return _response.data

    async def delete_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.delete_conversation(
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_conversation(conversation_id, request_options=request_options)
        return _response.data

    async def update_conversation(
        self,
        conversation_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        extra_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        is_read_by_user: typing.Optional[bool] = OMIT,
        is_read_by_support: typing.Optional[bool] = OMIT,
        status: typing.Optional[ConversationStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        name : typing.Optional[str]

        extra_context : typing.Optional[typing.Dict[str, typing.Any]]

        is_read_by_user : typing.Optional[bool]

        is_read_by_support : typing.Optional[bool]

        status : typing.Optional[ConversationStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.update_conversation(
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_conversation(
            conversation_id,
            name=name,
            extra_context=extra_context,
            is_read_by_user=is_read_by_user,
            is_read_by_support=is_read_by_support,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def list_conversation_messages(
        self,
        conversation_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageConversationMessageRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageConversationMessageRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.list_conversation_messages(
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_conversation_messages(
            conversation_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_conversation_message(
        self,
        conversation_id: str,
        *,
        content: str,
        type: ConversationMessageType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        content : str

        type : ConversationMessageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConversationMessageType

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.create_conversation_message(
                conversation_id="conversation_id",
                content="content",
                type=ConversationMessageType.MESSAGE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_conversation_message(
            conversation_id, content=content, type=type, request_options=request_options
        )
        return _response.data

    async def get_conversation_message(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.get_conversation_message(
                conversation_id="conversation_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conversation_message(
            conversation_id, message_id, request_options=request_options
        )
        return _response.data

    async def update_conversation_message(
        self,
        conversation_id: str,
        message_id: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeConversationMessageRestGet:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeConversationMessageRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.update_conversation_message(
                conversation_id="conversation_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_conversation_message(
            conversation_id, message_id, content=content, request_options=request_options
        )
        return _response.data

    async def delete_conversation_message(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.delete_conversation_message(
                conversation_id="conversation_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_conversation_message(
            conversation_id, message_id, request_options=request_options
        )
        return _response.data

    async def trigger_chatbot_processing(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.conversations.trigger_chatbot_processing(
                conversation_id="conversation_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trigger_chatbot_processing(
            conversation_id, message_id, request_options=request_options
        )
        return _response.data

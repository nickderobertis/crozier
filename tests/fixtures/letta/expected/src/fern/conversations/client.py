

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.client_tool_schema import ClientToolSchema
from ..types.compaction_request import CompactionRequest
from ..types.compaction_response import CompactionResponse
from ..types.conversation import Conversation
from ..types.letta_message_union import LettaMessageUnion
from ..types.letta_streaming_request_input import LettaStreamingRequestInput
from ..types.letta_streaming_request_messages_item import LettaStreamingRequestMessagesItem
from ..types.letta_streaming_response import LettaStreamingResponse
from ..types.message_type import MessageType
from .raw_client import AsyncRawConversationsClient, RawConversationsClient
from .types.list_conversation_messages_request_order import ListConversationMessagesRequestOrder
from .types.list_conversation_messages_request_order_by import ListConversationMessagesRequestOrderBy


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
        agent_id: str,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Conversation]:
        """
        List all conversations for an agent.

        Parameters
        ----------
        agent_id : str
            The agent ID to list conversations for

        limit : typing.Optional[int]
            Maximum number of conversations to return

        after : typing.Optional[str]
            Cursor for pagination (conversation ID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Conversation]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.list_conversations(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.list_conversations(
            agent_id=agent_id, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    def create_conversation(
        self,
        *,
        agent_id: str,
        summary: typing.Optional[str] = OMIT,
        isolated_block_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Conversation:
        """
        Create a new conversation for an agent.

        Parameters
        ----------
        agent_id : str
            The agent ID to create a conversation for

        summary : typing.Optional[str]
            A summary of the conversation.

        isolated_block_labels : typing.Optional[typing.Sequence[str]]
            List of block labels that should be isolated (conversation-specific) rather than shared across conversations. New blocks will be created as copies of the agent's blocks with these labels.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.create_conversation(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.create_conversation(
            agent_id=agent_id,
            summary=summary,
            isolated_block_labels=isolated_block_labels,
            request_options=request_options,
        )
        return _response.data

    def retrieve_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Conversation:
        """
        Retrieve a specific conversation.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.retrieve_conversation(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_conversation(conversation_id, request_options=request_options)
        return _response.data

    def update_conversation(
        self,
        conversation_id: str,
        *,
        summary: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Conversation:
        """
        Update a conversation.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        summary : typing.Optional[str]
            A summary of the conversation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.update_conversation(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.update_conversation(
            conversation_id, summary=summary, request_options=request_options
        )
        return _response.data

    def list_conversation_messages(
        self,
        conversation_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListConversationMessagesRequestOrder] = None,
        order_by: typing.Optional[ListConversationMessagesRequestOrderBy] = None,
        group_id: typing.Optional[str] = None,
        include_err: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LettaMessageUnion]:
        """
        List all messages in a conversation.

        Returns LettaMessage objects (UserMessage, AssistantMessage, etc.) for all
        messages in the conversation, with support for cursor-based pagination.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListConversationMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListConversationMessagesRequestOrderBy]
            Field to sort by

        group_id : typing.Optional[str]
            Group ID to filter messages by.

        include_err : typing.Optional[bool]
            Whether to include error messages and error statuses. For debugging purposes only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.list_conversation_messages(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_conversation_messages(
            conversation_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            group_id=group_id,
            include_err=include_err,
            request_options=request_options,
        )
        return _response.data

    def send_conversation_message(
        self,
        conversation_id: str,
        *,
        messages: typing.Optional[typing.Sequence[LettaStreamingRequestMessagesItem]] = OMIT,
        input: typing.Optional[LettaStreamingRequestInput] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        client_tools: typing.Optional[typing.Sequence[ClientToolSchema]] = OMIT,
        override_model: typing.Optional[str] = OMIT,
        streaming: typing.Optional[bool] = OMIT,
        stream_tokens: typing.Optional[bool] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        background: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LettaStreamingResponse:
        """
        Send a message to a conversation and get a streaming response.

        This endpoint sends a message to an existing conversation and streams
        the agent's response back.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        messages : typing.Optional[typing.Sequence[LettaStreamingRequestMessagesItem]]
            The messages to be sent to the agent.

        input : typing.Optional[LettaStreamingRequestInput]
            Syntactic sugar for a single user message. Equivalent to messages=[{'role': 'user', 'content': input}].

        max_steps : typing.Optional[int]
            Maximum number of steps the agent should take to process the request.

        use_assistant_message : typing.Optional[bool]
            Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument in the designated message tool. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.

        include_return_message_types : typing.Optional[typing.Sequence[MessageType]]
            Only return specified message types in the response. If `None` (default) returns all messages.

        enable_thinking : typing.Optional[str]
            If set to True, enables reasoning before responses or tool calls from the agent.

        client_tools : typing.Optional[typing.Sequence[ClientToolSchema]]
            Client-side tools that the agent can call. When the agent calls a client-side tool, execution pauses and returns control to the client to execute the tool and provide the result via a ToolReturn.

        override_model : typing.Optional[str]
            Model handle to use for this request instead of the agent's default model. This allows sending a message to a different model without changing the agent's configuration.

        streaming : typing.Optional[bool]
            If True, returns a streaming response (Server-Sent Events). If False (default), returns a complete response.

        stream_tokens : typing.Optional[bool]
            Flag to determine if individual tokens should be streamed, rather than streaming per step (only used when streaming=true).

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts (only used when streaming=true).

        background : typing.Optional[bool]
            Whether to process the request in the background (only used when streaming=true).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LettaStreamingResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.send_conversation_message(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.send_conversation_message(
            conversation_id,
            messages=messages,
            input=input,
            max_steps=max_steps,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_return_message_types=include_return_message_types,
            enable_thinking=enable_thinking,
            client_tools=client_tools,
            override_model=override_model,
            streaming=streaming,
            stream_tokens=stream_tokens,
            include_pings=include_pings,
            background=background,
            request_options=request_options,
        )
        return _response.data

    def retrieve_conversation_stream(
        self,
        conversation_id: str,
        *,
        starting_after: typing.Optional[int] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        poll_interval: typing.Optional[float] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Resume the stream for the most recent active run in a conversation.

        This endpoint allows you to reconnect to an active background stream
        for a conversation, enabling recovery from network interruptions.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        starting_after : typing.Optional[int]
            Sequence id to use as a cursor for pagination. Response will start streaming after this chunk sequence id

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.

        poll_interval : typing.Optional[float]
            Seconds to wait between polls when no new data.

        batch_size : typing.Optional[int]
            Number of entries to read per batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.retrieve_conversation_stream(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_conversation_stream(
            conversation_id,
            starting_after=starting_after,
            include_pings=include_pings,
            poll_interval=poll_interval,
            batch_size=batch_size,
            request_options=request_options,
        )
        return _response.data

    def cancel_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Cancel runs associated with a conversation.

        Note: To cancel active runs, Redis is required.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.cancel_conversation(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.cancel_conversation(conversation_id, request_options=request_options)
        return _response.data

    def compact_conversation(
        self,
        conversation_id: str,
        *,
        request: typing.Optional[CompactionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompactionResponse:
        """
        Compact (summarize) a conversation's message history.

        This endpoint summarizes the in-context messages for a specific conversation,
        reducing the message count while preserving important context.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        request : typing.Optional[CompactionRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompactionResponse
            Successful Response

        Examples
        --------
        from fern import CompactionRequest, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.compact_conversation(
            conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
            request=CompactionRequest(),
        )
        """
        _response = self._raw_client.compact_conversation(
            conversation_id, request=request, request_options=request_options
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
        agent_id: str,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Conversation]:
        """
        List all conversations for an agent.

        Parameters
        ----------
        agent_id : str
            The agent ID to list conversations for

        limit : typing.Optional[int]
            Maximum number of conversations to return

        after : typing.Optional[str]
            Cursor for pagination (conversation ID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Conversation]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.list_conversations(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_conversations(
            agent_id=agent_id, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    async def create_conversation(
        self,
        *,
        agent_id: str,
        summary: typing.Optional[str] = OMIT,
        isolated_block_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Conversation:
        """
        Create a new conversation for an agent.

        Parameters
        ----------
        agent_id : str
            The agent ID to create a conversation for

        summary : typing.Optional[str]
            A summary of the conversation.

        isolated_block_labels : typing.Optional[typing.Sequence[str]]
            List of block labels that should be isolated (conversation-specific) rather than shared across conversations. New blocks will be created as copies of the agent's blocks with these labels.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.create_conversation(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_conversation(
            agent_id=agent_id,
            summary=summary,
            isolated_block_labels=isolated_block_labels,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Conversation:
        """
        Retrieve a specific conversation.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.retrieve_conversation(
                conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_conversation(conversation_id, request_options=request_options)
        return _response.data

    async def update_conversation(
        self,
        conversation_id: str,
        *,
        summary: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Conversation:
        """
        Update a conversation.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        summary : typing.Optional[str]
            A summary of the conversation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Conversation
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.update_conversation(
                conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_conversation(
            conversation_id, summary=summary, request_options=request_options
        )
        return _response.data

    async def list_conversation_messages(
        self,
        conversation_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListConversationMessagesRequestOrder] = None,
        order_by: typing.Optional[ListConversationMessagesRequestOrderBy] = None,
        group_id: typing.Optional[str] = None,
        include_err: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LettaMessageUnion]:
        """
        List all messages in a conversation.

        Returns LettaMessage objects (UserMessage, AssistantMessage, etc.) for all
        messages in the conversation, with support for cursor-based pagination.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListConversationMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListConversationMessagesRequestOrderBy]
            Field to sort by

        group_id : typing.Optional[str]
            Group ID to filter messages by.

        include_err : typing.Optional[bool]
            Whether to include error messages and error statuses. For debugging purposes only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.list_conversation_messages(
                conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_conversation_messages(
            conversation_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            group_id=group_id,
            include_err=include_err,
            request_options=request_options,
        )
        return _response.data

    async def send_conversation_message(
        self,
        conversation_id: str,
        *,
        messages: typing.Optional[typing.Sequence[LettaStreamingRequestMessagesItem]] = OMIT,
        input: typing.Optional[LettaStreamingRequestInput] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        client_tools: typing.Optional[typing.Sequence[ClientToolSchema]] = OMIT,
        override_model: typing.Optional[str] = OMIT,
        streaming: typing.Optional[bool] = OMIT,
        stream_tokens: typing.Optional[bool] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        background: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LettaStreamingResponse:
        """
        Send a message to a conversation and get a streaming response.

        This endpoint sends a message to an existing conversation and streams
        the agent's response back.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        messages : typing.Optional[typing.Sequence[LettaStreamingRequestMessagesItem]]
            The messages to be sent to the agent.

        input : typing.Optional[LettaStreamingRequestInput]
            Syntactic sugar for a single user message. Equivalent to messages=[{'role': 'user', 'content': input}].

        max_steps : typing.Optional[int]
            Maximum number of steps the agent should take to process the request.

        use_assistant_message : typing.Optional[bool]
            Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument in the designated message tool. Still supported for legacy agent types, but deprecated for letta_v1_agent onward.

        include_return_message_types : typing.Optional[typing.Sequence[MessageType]]
            Only return specified message types in the response. If `None` (default) returns all messages.

        enable_thinking : typing.Optional[str]
            If set to True, enables reasoning before responses or tool calls from the agent.

        client_tools : typing.Optional[typing.Sequence[ClientToolSchema]]
            Client-side tools that the agent can call. When the agent calls a client-side tool, execution pauses and returns control to the client to execute the tool and provide the result via a ToolReturn.

        override_model : typing.Optional[str]
            Model handle to use for this request instead of the agent's default model. This allows sending a message to a different model without changing the agent's configuration.

        streaming : typing.Optional[bool]
            If True, returns a streaming response (Server-Sent Events). If False (default), returns a complete response.

        stream_tokens : typing.Optional[bool]
            Flag to determine if individual tokens should be streamed, rather than streaming per step (only used when streaming=true).

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts (only used when streaming=true).

        background : typing.Optional[bool]
            Whether to process the request in the background (only used when streaming=true).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LettaStreamingResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.send_conversation_message(
                conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_conversation_message(
            conversation_id,
            messages=messages,
            input=input,
            max_steps=max_steps,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            include_return_message_types=include_return_message_types,
            enable_thinking=enable_thinking,
            client_tools=client_tools,
            override_model=override_model,
            streaming=streaming,
            stream_tokens=stream_tokens,
            include_pings=include_pings,
            background=background,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_conversation_stream(
        self,
        conversation_id: str,
        *,
        starting_after: typing.Optional[int] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        poll_interval: typing.Optional[float] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Resume the stream for the most recent active run in a conversation.

        This endpoint allows you to reconnect to an active background stream
        for a conversation, enabling recovery from network interruptions.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        starting_after : typing.Optional[int]
            Sequence id to use as a cursor for pagination. Response will start streaming after this chunk sequence id

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.

        poll_interval : typing.Optional[float]
            Seconds to wait between polls when no new data.

        batch_size : typing.Optional[int]
            Number of entries to read per batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.retrieve_conversation_stream(
                conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_conversation_stream(
            conversation_id,
            starting_after=starting_after,
            include_pings=include_pings,
            poll_interval=poll_interval,
            batch_size=batch_size,
            request_options=request_options,
        )
        return _response.data

    async def cancel_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Cancel runs associated with a conversation.

        Note: To cancel active runs, Redis is required.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.cancel_conversation(
                conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_conversation(conversation_id, request_options=request_options)
        return _response.data

    async def compact_conversation(
        self,
        conversation_id: str,
        *,
        request: typing.Optional[CompactionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompactionResponse:
        """
        Compact (summarize) a conversation's message history.

        This endpoint summarizes the in-context messages for a specific conversation,
        reducing the message count while preserving important context.

        Parameters
        ----------
        conversation_id : str
            The ID of the conv in the format 'conv-<uuid4>'

        request : typing.Optional[CompactionRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompactionResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CompactionRequest

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.compact_conversation(
                conversation_id="conv-123e4567-e89b-42d3-8456-426614174000",
                request=CompactionRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compact_conversation(
            conversation_id, request=request, request_options=request_options
        )
        return _response.data

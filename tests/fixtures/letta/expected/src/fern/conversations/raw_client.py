

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.client_tool_schema import ClientToolSchema
from ..types.compaction_request import CompactionRequest
from ..types.compaction_response import CompactionResponse
from ..types.conversation import Conversation
from ..types.http_validation_error import HttpValidationError
from ..types.letta_message_union import LettaMessageUnion
from ..types.letta_streaming_request_input import LettaStreamingRequestInput
from ..types.letta_streaming_request_messages_item import LettaStreamingRequestMessagesItem
from ..types.letta_streaming_response import LettaStreamingResponse
from ..types.message_type import MessageType
from .types.list_conversation_messages_request_order import ListConversationMessagesRequestOrder
from .types.list_conversation_messages_request_order_by import ListConversationMessagesRequestOrderBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConversationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_conversations(
        self,
        *,
        agent_id: str,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Conversation]]:
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
        HttpResponse[typing.List[Conversation]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/conversations/",
            method="GET",
            params={
                "agent_id": agent_id,
                "limit": limit,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Conversation],
                    parse_obj_as(
                        type_=typing.List[Conversation],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_conversation(
        self,
        *,
        agent_id: str,
        summary: typing.Optional[str] = OMIT,
        isolated_block_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Conversation]:
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
        HttpResponse[Conversation]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/conversations/",
            method="POST",
            params={
                "agent_id": agent_id,
            },
            json={
                "summary": summary,
                "isolated_block_labels": isolated_block_labels,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Conversation]:
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
        HttpResponse[Conversation]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_conversation(
        self,
        conversation_id: str,
        *,
        summary: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Conversation]:
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
        HttpResponse[Conversation]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}",
            method="PATCH",
            json={
                "summary": summary,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.List[LettaMessageUnion]]:
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
        HttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "group_id": group_id,
                "include_err": include_err,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LettaMessageUnion],
                    parse_obj_as(
                        type_=typing.List[LettaMessageUnion],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[LettaStreamingResponse]:
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
        HttpResponse[LettaStreamingResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/messages",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Optional[typing.Sequence[LettaStreamingRequestMessagesItem]],
                    direction="write",
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[LettaStreamingRequestInput], direction="write"
                ),
                "max_steps": max_steps,
                "use_assistant_message": use_assistant_message,
                "assistant_message_tool_name": assistant_message_tool_name,
                "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                "include_return_message_types": include_return_message_types,
                "enable_thinking": enable_thinking,
                "client_tools": convert_and_respect_annotation_metadata(
                    object_=client_tools,
                    annotation=typing.Optional[typing.Sequence[ClientToolSchema]],
                    direction="write",
                ),
                "override_model": override_model,
                "streaming": streaming,
                "stream_tokens": stream_tokens,
                "include_pings": include_pings,
                "background": background,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LettaStreamingResponse,
                    parse_obj_as(
                        type_=LettaStreamingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_conversation_stream(
        self,
        conversation_id: str,
        *,
        starting_after: typing.Optional[int] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        poll_interval: typing.Optional[float] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/stream",
            method="POST",
            json={
                "starting_after": starting_after,
                "include_pings": include_pings,
                "poll_interval": poll_interval,
                "batch_size": batch_size,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
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
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def compact_conversation(
        self,
        conversation_id: str,
        *,
        request: typing.Optional[CompactionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CompactionResponse]:
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
        HttpResponse[CompactionResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/compact",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[CompactionRequest], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CompactionResponse,
                    parse_obj_as(
                        type_=CompactionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawConversationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_conversations(
        self,
        *,
        agent_id: str,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Conversation]]:
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
        AsyncHttpResponse[typing.List[Conversation]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/conversations/",
            method="GET",
            params={
                "agent_id": agent_id,
                "limit": limit,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Conversation],
                    parse_obj_as(
                        type_=typing.List[Conversation],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_conversation(
        self,
        *,
        agent_id: str,
        summary: typing.Optional[str] = OMIT,
        isolated_block_labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Conversation]:
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
        AsyncHttpResponse[Conversation]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/conversations/",
            method="POST",
            params={
                "agent_id": agent_id,
            },
            json={
                "summary": summary,
                "isolated_block_labels": isolated_block_labels,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Conversation]:
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
        AsyncHttpResponse[Conversation]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_conversation(
        self,
        conversation_id: str,
        *,
        summary: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Conversation]:
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
        AsyncHttpResponse[Conversation]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}",
            method="PATCH",
            json={
                "summary": summary,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.List[LettaMessageUnion]]:
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
        AsyncHttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "group_id": group_id,
                "include_err": include_err,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LettaMessageUnion],
                    parse_obj_as(
                        type_=typing.List[LettaMessageUnion],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[LettaStreamingResponse]:
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
        AsyncHttpResponse[LettaStreamingResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/messages",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Optional[typing.Sequence[LettaStreamingRequestMessagesItem]],
                    direction="write",
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[LettaStreamingRequestInput], direction="write"
                ),
                "max_steps": max_steps,
                "use_assistant_message": use_assistant_message,
                "assistant_message_tool_name": assistant_message_tool_name,
                "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
                "include_return_message_types": include_return_message_types,
                "enable_thinking": enable_thinking,
                "client_tools": convert_and_respect_annotation_metadata(
                    object_=client_tools,
                    annotation=typing.Optional[typing.Sequence[ClientToolSchema]],
                    direction="write",
                ),
                "override_model": override_model,
                "streaming": streaming,
                "stream_tokens": stream_tokens,
                "include_pings": include_pings,
                "background": background,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LettaStreamingResponse,
                    parse_obj_as(
                        type_=LettaStreamingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_conversation_stream(
        self,
        conversation_id: str,
        *,
        starting_after: typing.Optional[int] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        poll_interval: typing.Optional[float] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/stream",
            method="POST",
            json={
                "starting_after": starting_after,
                "include_pings": include_pings,
                "poll_interval": poll_interval,
                "batch_size": batch_size,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
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
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def compact_conversation(
        self,
        conversation_id: str,
        *,
        request: typing.Optional[CompactionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CompactionResponse]:
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
        AsyncHttpResponse[CompactionResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(conversation_id)}/compact",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[CompactionRequest], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CompactionResponse,
                    parse_obj_as(
                        type_=CompactionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)



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
from ..types.group import Group
from ..types.http_validation_error import HttpValidationError
from ..types.letta_message_union import LettaMessageUnion
from ..types.letta_request_input import LettaRequestInput
from ..types.letta_request_messages_item import LettaRequestMessagesItem
from ..types.letta_response import LettaResponse
from ..types.letta_streaming_request_input import LettaStreamingRequestInput
from ..types.letta_streaming_request_messages_item import LettaStreamingRequestMessagesItem
from ..types.manager_type import ManagerType
from ..types.message_type import MessageType
from .types.group_create_manager_config import GroupCreateManagerConfig
from .types.group_update_manager_config import GroupUpdateManagerConfig
from .types.list_group_messages_request_order import ListGroupMessagesRequestOrder
from .types.list_group_messages_request_order_by import ListGroupMessagesRequestOrderBy
from .types.list_groups_request_order import ListGroupsRequestOrder
from .types.list_groups_request_order_by import ListGroupsRequestOrderBy
from .types.modify_group_message_request_body import ModifyGroupMessageRequestBody
from .types.modify_group_message_response import ModifyGroupMessageResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_groups(
        self,
        *,
        manager_type: typing.Optional[ManagerType] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListGroupsRequestOrder] = None,
        order_by: typing.Optional[ListGroupsRequestOrderBy] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Group]]:
        """
        Fetch all multi-agent groups matching query.

        Parameters
        ----------
        manager_type : typing.Optional[ManagerType]
            Search groups by manager type

        before : typing.Optional[str]
            Group ID cursor for pagination. Returns groups that come before this group ID in the specified sort order

        after : typing.Optional[str]
            Group ID cursor for pagination. Returns groups that come after this group ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of groups to return

        order : typing.Optional[ListGroupsRequestOrder]
            Sort order for groups by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListGroupsRequestOrderBy]
            Field to sort by

        project_id : typing.Optional[str]
            Search groups by project id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Group]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/groups/",
            method="GET",
            params={
                "manager_type": manager_type,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "project_id": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Group],
                    parse_obj_as(
                        type_=typing.List[Group],
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

    def create_group(
        self,
        *,
        agent_ids: typing.Sequence[str],
        description: str,
        project: typing.Optional[str] = None,
        manager_config: typing.Optional[GroupCreateManagerConfig] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        shared_block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Group]:
        """
        Create a new multi-agent group with the specified configuration.

        Parameters
        ----------
        agent_ids : typing.Sequence[str]


        description : str


        project : typing.Optional[str]
            The project slug to associate with the group (cloud only).

        manager_config : typing.Optional[GroupCreateManagerConfig]


        project_id : typing.Optional[str]
            The associated project id.

        shared_block_ids : typing.Optional[typing.Sequence[str]]


        hidden : typing.Optional[bool]
            If set to True, the group will be hidden.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/groups/",
            method="POST",
            json={
                "agent_ids": agent_ids,
                "description": description,
                "manager_config": convert_and_respect_annotation_metadata(
                    object_=manager_config, annotation=GroupCreateManagerConfig, direction="write"
                ),
                "project_id": project_id,
                "shared_block_ids": shared_block_ids,
                "hidden": hidden,
            },
            headers={
                "content-type": "application/json",
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
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

    def count_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[int]:
        """
        Get the count of all groups associated with a given user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/groups/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    def retrieve_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Group]:
        """
        Retrieve the group by id.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
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

    def delete_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a multi-agent group.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
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

    def modify_group(
        self,
        group_id: str,
        *,
        project: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        manager_config: typing.Optional[GroupUpdateManagerConfig] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        shared_block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Group]:
        """
        Create a new multi-agent group with the specified configuration.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        project : typing.Optional[str]
            The project slug to associate with the group (cloud only).

        agent_ids : typing.Optional[typing.Sequence[str]]


        description : typing.Optional[str]


        manager_config : typing.Optional[GroupUpdateManagerConfig]


        project_id : typing.Optional[str]
            The associated project id.

        shared_block_ids : typing.Optional[typing.Sequence[str]]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}",
            method="PATCH",
            json={
                "agent_ids": agent_ids,
                "description": description,
                "manager_config": convert_and_respect_annotation_metadata(
                    object_=manager_config, annotation=typing.Optional[GroupUpdateManagerConfig], direction="write"
                ),
                "project_id": project_id,
                "shared_block_ids": shared_block_ids,
            },
            headers={
                "content-type": "application/json",
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
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

    def list_group_messages(
        self,
        group_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListGroupMessagesRequestOrder] = None,
        order_by: typing.Optional[ListGroupMessagesRequestOrderBy] = None,
        use_assistant_message: typing.Optional[bool] = None,
        assistant_message_tool_name: typing.Optional[str] = None,
        assistant_message_tool_kwarg: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[LettaMessageUnion]]:
        """
        Retrieve message history for an agent.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to retrieve

        order : typing.Optional[ListGroupMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListGroupMessagesRequestOrderBy]
            Field to sort by

        use_assistant_message : typing.Optional[bool]
            Whether to use assistant messages

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "use_assistant_message": use_assistant_message,
                "assistant_message_tool_name": assistant_message_tool_name,
                "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
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

    def send_group_message(
        self,
        group_id: str,
        *,
        messages: typing.Optional[typing.Sequence[LettaRequestMessagesItem]] = OMIT,
        input: typing.Optional[LettaRequestInput] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        client_tools: typing.Optional[typing.Sequence[ClientToolSchema]] = OMIT,
        override_model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LettaResponse]:
        """
        Process a user message and return the group's response.
        This endpoint accepts a message from a user and processes it through through agents in the group based on the specified pattern

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        messages : typing.Optional[typing.Sequence[LettaRequestMessagesItem]]
            The messages to be sent to the agent.

        input : typing.Optional[LettaRequestInput]
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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LettaResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/messages",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Optional[typing.Sequence[LettaRequestMessagesItem]],
                    direction="write",
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[LettaRequestInput], direction="write"
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
                    LettaResponse,
                    parse_obj_as(
                        type_=LettaResponse,
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

    def send_group_message_streaming(
        self,
        group_id: str,
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
    ) -> HttpResponse[typing.Any]:
        """
        Process a user message and return the group's responses.
        This endpoint accepts a message from a user and processes it through agents in the group based on the specified pattern.
        It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

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
        HttpResponse[typing.Any]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/messages/stream",
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

    def modify_group_message(
        self,
        group_id: str,
        message_id: str,
        *,
        request: ModifyGroupMessageRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ModifyGroupMessageResponse]:
        """
        Update the details of a message associated with an agent.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        message_id : str
            The ID of the message in the format 'message-<uuid4>'

        request : ModifyGroupMessageRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ModifyGroupMessageResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/messages/{encode_path_param(message_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ModifyGroupMessageRequestBody, direction="write"
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
                    ModifyGroupMessageResponse,
                    parse_obj_as(
                        type_=ModifyGroupMessageResponse,
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

    def reset_group_messages(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete the group messages for all agents that are part of the multi-agent group.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/reset-messages",
            method="PATCH",
            request_options=request_options,
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

    def attach_block_to_group(
        self, group_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Attach a block to a group.
        This will add the block to the group and all agents within the group.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        block_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/blocks/attach/{encode_path_param(block_id)}",
            method="PATCH",
            request_options=request_options,
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

    def detach_block_from_group(
        self, group_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Detach a block from a group.
        This will remove the block from the group and all agents within the group.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        block_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/blocks/detach/{encode_path_param(block_id)}",
            method="PATCH",
            request_options=request_options,
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


class AsyncRawGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_groups(
        self,
        *,
        manager_type: typing.Optional[ManagerType] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListGroupsRequestOrder] = None,
        order_by: typing.Optional[ListGroupsRequestOrderBy] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Group]]:
        """
        Fetch all multi-agent groups matching query.

        Parameters
        ----------
        manager_type : typing.Optional[ManagerType]
            Search groups by manager type

        before : typing.Optional[str]
            Group ID cursor for pagination. Returns groups that come before this group ID in the specified sort order

        after : typing.Optional[str]
            Group ID cursor for pagination. Returns groups that come after this group ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of groups to return

        order : typing.Optional[ListGroupsRequestOrder]
            Sort order for groups by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListGroupsRequestOrderBy]
            Field to sort by

        project_id : typing.Optional[str]
            Search groups by project id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Group]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/groups/",
            method="GET",
            params={
                "manager_type": manager_type,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "project_id": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Group],
                    parse_obj_as(
                        type_=typing.List[Group],
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

    async def create_group(
        self,
        *,
        agent_ids: typing.Sequence[str],
        description: str,
        project: typing.Optional[str] = None,
        manager_config: typing.Optional[GroupCreateManagerConfig] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        shared_block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Group]:
        """
        Create a new multi-agent group with the specified configuration.

        Parameters
        ----------
        agent_ids : typing.Sequence[str]


        description : str


        project : typing.Optional[str]
            The project slug to associate with the group (cloud only).

        manager_config : typing.Optional[GroupCreateManagerConfig]


        project_id : typing.Optional[str]
            The associated project id.

        shared_block_ids : typing.Optional[typing.Sequence[str]]


        hidden : typing.Optional[bool]
            If set to True, the group will be hidden.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/groups/",
            method="POST",
            json={
                "agent_ids": agent_ids,
                "description": description,
                "manager_config": convert_and_respect_annotation_metadata(
                    object_=manager_config, annotation=GroupCreateManagerConfig, direction="write"
                ),
                "project_id": project_id,
                "shared_block_ids": shared_block_ids,
                "hidden": hidden,
            },
            headers={
                "content-type": "application/json",
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
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

    async def count_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[int]:
        """
        Get the count of all groups associated with a given user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/groups/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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

    async def retrieve_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Group]:
        """
        Retrieve the group by id.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
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

    async def delete_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a multi-agent group.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def modify_group(
        self,
        group_id: str,
        *,
        project: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        manager_config: typing.Optional[GroupUpdateManagerConfig] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        shared_block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Group]:
        """
        Create a new multi-agent group with the specified configuration.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        project : typing.Optional[str]
            The project slug to associate with the group (cloud only).

        agent_ids : typing.Optional[typing.Sequence[str]]


        description : typing.Optional[str]


        manager_config : typing.Optional[GroupUpdateManagerConfig]


        project_id : typing.Optional[str]
            The associated project id.

        shared_block_ids : typing.Optional[typing.Sequence[str]]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}",
            method="PATCH",
            json={
                "agent_ids": agent_ids,
                "description": description,
                "manager_config": convert_and_respect_annotation_metadata(
                    object_=manager_config, annotation=typing.Optional[GroupUpdateManagerConfig], direction="write"
                ),
                "project_id": project_id,
                "shared_block_ids": shared_block_ids,
            },
            headers={
                "content-type": "application/json",
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
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

    async def list_group_messages(
        self,
        group_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListGroupMessagesRequestOrder] = None,
        order_by: typing.Optional[ListGroupMessagesRequestOrderBy] = None,
        use_assistant_message: typing.Optional[bool] = None,
        assistant_message_tool_name: typing.Optional[str] = None,
        assistant_message_tool_kwarg: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[LettaMessageUnion]]:
        """
        Retrieve message history for an agent.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to retrieve

        order : typing.Optional[ListGroupMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListGroupMessagesRequestOrderBy]
            Field to sort by

        use_assistant_message : typing.Optional[bool]
            Whether to use assistant messages

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "use_assistant_message": use_assistant_message,
                "assistant_message_tool_name": assistant_message_tool_name,
                "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
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

    async def send_group_message(
        self,
        group_id: str,
        *,
        messages: typing.Optional[typing.Sequence[LettaRequestMessagesItem]] = OMIT,
        input: typing.Optional[LettaRequestInput] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        client_tools: typing.Optional[typing.Sequence[ClientToolSchema]] = OMIT,
        override_model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LettaResponse]:
        """
        Process a user message and return the group's response.
        This endpoint accepts a message from a user and processes it through through agents in the group based on the specified pattern

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        messages : typing.Optional[typing.Sequence[LettaRequestMessagesItem]]
            The messages to be sent to the agent.

        input : typing.Optional[LettaRequestInput]
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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LettaResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/messages",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Optional[typing.Sequence[LettaRequestMessagesItem]],
                    direction="write",
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[LettaRequestInput], direction="write"
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
                    LettaResponse,
                    parse_obj_as(
                        type_=LettaResponse,
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

    async def send_group_message_streaming(
        self,
        group_id: str,
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
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Process a user message and return the group's responses.
        This endpoint accepts a message from a user and processes it through agents in the group based on the specified pattern.
        It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

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
        AsyncHttpResponse[typing.Any]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/messages/stream",
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

    async def modify_group_message(
        self,
        group_id: str,
        message_id: str,
        *,
        request: ModifyGroupMessageRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ModifyGroupMessageResponse]:
        """
        Update the details of a message associated with an agent.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        message_id : str
            The ID of the message in the format 'message-<uuid4>'

        request : ModifyGroupMessageRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ModifyGroupMessageResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/messages/{encode_path_param(message_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ModifyGroupMessageRequestBody, direction="write"
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
                    ModifyGroupMessageResponse,
                    parse_obj_as(
                        type_=ModifyGroupMessageResponse,
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

    async def reset_group_messages(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete the group messages for all agents that are part of the multi-agent group.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/reset-messages",
            method="PATCH",
            request_options=request_options,
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

    async def attach_block_to_group(
        self, group_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Attach a block to a group.
        This will add the block to the group and all agents within the group.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        block_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/blocks/attach/{encode_path_param(block_id)}",
            method="PATCH",
            request_options=request_options,
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

    async def detach_block_from_group(
        self, group_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Detach a block from a group.
        This will remove the block from the group and all agents within the group.

        Parameters
        ----------
        group_id : str
            The ID of the group in the format 'group-<uuid4>'

        block_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_id)}/blocks/detach/{encode_path_param(block_id)}",
            method="PATCH",
            request_options=request_options,
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

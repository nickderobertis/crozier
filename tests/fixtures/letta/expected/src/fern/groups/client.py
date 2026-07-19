

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.client_tool_schema import ClientToolSchema
from ..types.group import Group
from ..types.letta_message_union import LettaMessageUnion
from ..types.letta_request_input import LettaRequestInput
from ..types.letta_request_messages_item import LettaRequestMessagesItem
from ..types.letta_response import LettaResponse
from ..types.letta_streaming_request_input import LettaStreamingRequestInput
from ..types.letta_streaming_request_messages_item import LettaStreamingRequestMessagesItem
from ..types.manager_type import ManagerType
from ..types.message_type import MessageType
from .raw_client import AsyncRawGroupsClient, RawGroupsClient
from .types.group_create_manager_config import GroupCreateManagerConfig
from .types.group_update_manager_config import GroupUpdateManagerConfig
from .types.list_group_messages_request_order import ListGroupMessagesRequestOrder
from .types.list_group_messages_request_order_by import ListGroupMessagesRequestOrderBy
from .types.list_groups_request_order import ListGroupsRequestOrder
from .types.list_groups_request_order_by import ListGroupsRequestOrderBy
from .types.modify_group_message_request_body import ModifyGroupMessageRequestBody
from .types.modify_group_message_response import ModifyGroupMessageResponse


OMIT = typing.cast(typing.Any, ...)


class GroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGroupsClient
        """
        return self._raw_client

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
    ) -> typing.List[Group]:
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
        typing.List[Group]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.list_groups()
        """
        _response = self._raw_client.list_groups(
            manager_type=manager_type,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Group:
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
        Group
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.create_group(
            agent_ids=["agent_ids"],
            description="description",
        )
        """
        _response = self._raw_client.create_group(
            agent_ids=agent_ids,
            description=description,
            project=project,
            manager_config=manager_config,
            project_id=project_id,
            shared_block_ids=shared_block_ids,
            hidden=hidden,
            request_options=request_options,
        )
        return _response.data

    def count_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Get the count of all groups associated with a given user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.count_groups()
        """
        _response = self._raw_client.count_groups(request_options=request_options)
        return _response.data

    def retrieve_group(self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
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
        Group
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.retrieve_group(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_group(group_id, request_options=request_options)
        return _response.data

    def delete_group(self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.delete_group(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_group(group_id, request_options=request_options)
        return _response.data

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
    ) -> Group:
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
        Group
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.modify_group(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.modify_group(
            group_id,
            project=project,
            agent_ids=agent_ids,
            description=description,
            manager_config=manager_config,
            project_id=project_id,
            shared_block_ids=shared_block_ids,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[LettaMessageUnion]:
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
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.list_group_messages(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_group_messages(
            group_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            request_options=request_options,
        )
        return _response.data

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
    ) -> LettaResponse:
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
        LettaResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.send_group_message(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.send_group_message(
            group_id,
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
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.send_group_message_streaming(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.send_group_message_streaming(
            group_id,
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

    def modify_group_message(
        self,
        group_id: str,
        message_id: str,
        *,
        request: ModifyGroupMessageRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModifyGroupMessageResponse:
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
        ModifyGroupMessageResponse
            Successful Response

        Examples
        --------
        from fern.groups import ModifyGroupMessageRequestBody_SystemMessage

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.modify_group_message(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
            request=ModifyGroupMessageRequestBody_SystemMessage(
                content="content",
            ),
        )
        """
        _response = self._raw_client.modify_group_message(
            group_id, message_id, request=request, request_options=request_options
        )
        return _response.data

    def reset_group_messages(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.reset_group_messages(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.reset_group_messages(group_id, request_options=request_options)
        return _response.data

    def attach_block_to_group(
        self, group_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.attach_block_to_group(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
            block_id="block_id",
        )
        """
        _response = self._raw_client.attach_block_to_group(group_id, block_id, request_options=request_options)
        return _response.data

    def detach_block_from_group(
        self, group_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.groups.detach_block_from_group(
            group_id="group-123e4567-e89b-42d3-8456-426614174000",
            block_id="block_id",
        )
        """
        _response = self._raw_client.detach_block_from_group(group_id, block_id, request_options=request_options)
        return _response.data


class AsyncGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGroupsClient
        """
        return self._raw_client

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
    ) -> typing.List[Group]:
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
        typing.List[Group]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.list_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_groups(
            manager_type=manager_type,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Group:
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
        Group
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.create_group(
                agent_ids=["agent_ids"],
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_group(
            agent_ids=agent_ids,
            description=description,
            project=project,
            manager_config=manager_config,
            project_id=project_id,
            shared_block_ids=shared_block_ids,
            hidden=hidden,
            request_options=request_options,
        )
        return _response.data

    async def count_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Get the count of all groups associated with a given user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.count_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_groups(request_options=request_options)
        return _response.data

    async def retrieve_group(self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
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
        Group
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.retrieve_group(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_group(group_id, request_options=request_options)
        return _response.data

    async def delete_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.delete_group(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group(group_id, request_options=request_options)
        return _response.data

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
    ) -> Group:
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
        Group
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.modify_group(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_group(
            group_id,
            project=project,
            agent_ids=agent_ids,
            description=description,
            manager_config=manager_config,
            project_id=project_id,
            shared_block_ids=shared_block_ids,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[LettaMessageUnion]:
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
            await client.groups.list_group_messages(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_group_messages(
            group_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            use_assistant_message=use_assistant_message,
            assistant_message_tool_name=assistant_message_tool_name,
            assistant_message_tool_kwarg=assistant_message_tool_kwarg,
            request_options=request_options,
        )
        return _response.data

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
    ) -> LettaResponse:
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
        LettaResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.send_group_message(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_group_message(
            group_id,
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
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
            await client.groups.send_group_message_streaming(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_group_message_streaming(
            group_id,
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

    async def modify_group_message(
        self,
        group_id: str,
        message_id: str,
        *,
        request: ModifyGroupMessageRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModifyGroupMessageResponse:
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
        ModifyGroupMessageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.groups import ModifyGroupMessageRequestBody_SystemMessage

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.modify_group_message(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
                request=ModifyGroupMessageRequestBody_SystemMessage(
                    content="content",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_group_message(
            group_id, message_id, request=request, request_options=request_options
        )
        return _response.data

    async def reset_group_messages(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.reset_group_messages(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_group_messages(group_id, request_options=request_options)
        return _response.data

    async def attach_block_to_group(
        self, group_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.attach_block_to_group(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.attach_block_to_group(group_id, block_id, request_options=request_options)
        return _response.data

    async def detach_block_from_group(
        self, group_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.groups.detach_block_from_group(
                group_id="group-123e4567-e89b-42d3-8456-426614174000",
                block_id="block_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detach_block_from_group(group_id, block_id, request_options=request_options)
        return _response.data

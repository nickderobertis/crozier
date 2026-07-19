

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.agent_state import AgentState
from ..types.agent_type import AgentType
from ..types.archival_memory_search_response import ArchivalMemorySearchResponse
from ..types.block_response import BlockResponse
from ..types.client_tool_schema import ClientToolSchema
from ..types.compaction_request import CompactionRequest
from ..types.compaction_response import CompactionResponse
from ..types.compaction_settings_input import CompactionSettingsInput
from ..types.context_window_overview import ContextWindowOverview
from ..types.create_block import CreateBlock
from ..types.embedding_config import EmbeddingConfig
from ..types.group import Group
from ..types.http_validation_error import HttpValidationError
from ..types.imported_agents_response import ImportedAgentsResponse
from ..types.letta_message_union import LettaMessageUnion
from ..types.letta_response import LettaResponse
from ..types.letta_streaming_request_input import LettaStreamingRequestInput
from ..types.letta_streaming_request_messages_item import LettaStreamingRequestMessagesItem
from ..types.letta_streaming_response import LettaStreamingResponse
from ..types.llm_config import LlmConfig
from ..types.memory import Memory
from ..types.message_create import MessageCreate
from ..types.message_role import MessageRole
from ..types.message_search_result import MessageSearchResult
from ..types.message_type import MessageType
from ..types.modify_approval_request import ModifyApprovalRequest
from ..types.paginated_agent_files import PaginatedAgentFiles
from ..types.passage import Passage
from ..types.run import Run
from ..types.source import Source
from ..types.stop_reason_type import StopReasonType
from ..types.tool import Tool
from ..types.tool_execution_result import ToolExecutionResult
from .types.agents_get_agent_variables_response import AgentsGetAgentVariablesResponse
from .types.agents_search_deployed_agents_request_combinator import AgentsSearchDeployedAgentsRequestCombinator
from .types.agents_search_deployed_agents_request_search_item import AgentsSearchDeployedAgentsRequestSearchItem
from .types.agents_search_deployed_agents_request_sort_by import AgentsSearchDeployedAgentsRequestSortBy
from .types.agents_search_deployed_agents_response import AgentsSearchDeployedAgentsResponse
from .types.create_agent_request_model_settings import CreateAgentRequestModelSettings
from .types.create_agent_request_response_format import CreateAgentRequestResponseFormat
from .types.create_agent_request_tool_rules_item import CreateAgentRequestToolRulesItem
from .types.letta_async_request_input import LettaAsyncRequestInput
from .types.letta_async_request_messages_item import LettaAsyncRequestMessagesItem
from .types.list_agent_sources_request_order import ListAgentSourcesRequestOrder
from .types.list_agent_sources_request_order_by import ListAgentSourcesRequestOrderBy
from .types.list_agents_request_include_item import ListAgentsRequestIncludeItem
from .types.list_agents_request_order import ListAgentsRequestOrder
from .types.list_agents_request_order_by import ListAgentsRequestOrderBy
from .types.list_core_memory_blocks_request_order import ListCoreMemoryBlocksRequestOrder
from .types.list_core_memory_blocks_request_order_by import ListCoreMemoryBlocksRequestOrderBy
from .types.list_files_for_agent_request_order import ListFilesForAgentRequestOrder
from .types.list_files_for_agent_request_order_by import ListFilesForAgentRequestOrderBy
from .types.list_folders_for_agent_request_order import ListFoldersForAgentRequestOrder
from .types.list_folders_for_agent_request_order_by import ListFoldersForAgentRequestOrderBy
from .types.list_groups_for_agent_request_order import ListGroupsForAgentRequestOrder
from .types.list_groups_for_agent_request_order_by import ListGroupsForAgentRequestOrderBy
from .types.list_messages_request_order import ListMessagesRequestOrder
from .types.list_messages_request_order_by import ListMessagesRequestOrderBy
from .types.list_tools_for_agent_request_order import ListToolsForAgentRequestOrder
from .types.list_tools_for_agent_request_order_by import ListToolsForAgentRequestOrderBy
from .types.message_search_request_search_mode import MessageSearchRequestSearchMode
from .types.modify_message_request_body import ModifyMessageRequestBody
from .types.modify_message_response import ModifyMessageResponse
from .types.preview_model_request_request_body import PreviewModelRequestRequestBody
from .types.retrieve_agent_request_include_item import RetrieveAgentRequestIncludeItem
from .types.search_archival_memory_request_tag_match_mode import SearchArchivalMemoryRequestTagMatchMode
from .types.update_agent_model_settings import UpdateAgentModelSettings
from .types.update_agent_response_format import UpdateAgentResponseFormat
from .types.update_agent_tool_rules_item import UpdateAgentToolRulesItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_agents(
        self,
        *,
        name: typing.Optional[str] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        match_all_tags: typing.Optional[bool] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query_text: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        base_template_id: typing.Optional[str] = None,
        identity_id: typing.Optional[str] = None,
        identifier_keys: typing.Optional[typing.Sequence[str]] = None,
        include_relationships: typing.Optional[typing.Sequence[str]] = None,
        include: typing.Optional[
            typing.Union[ListAgentsRequestIncludeItem, typing.Sequence[ListAgentsRequestIncludeItem]]
        ] = None,
        order: typing.Optional[ListAgentsRequestOrder] = None,
        order_by: typing.Optional[ListAgentsRequestOrderBy] = None,
        ascending: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        last_stop_reason: typing.Optional[StopReasonType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[AgentState]]:
        """
        Get a list of all agents.

        Parameters
        ----------
        name : typing.Optional[str]
            Name of the agent

        tags : typing.Optional[typing.Sequence[str]]
            List of tags to filter agents by

        match_all_tags : typing.Optional[bool]
            If True, only returns agents that match ALL given tags. Otherwise, return agents that have ANY of the passed-in tags.

        before : typing.Optional[str]
            Cursor for pagination

        after : typing.Optional[str]
            Cursor for pagination

        limit : typing.Optional[int]
            Limit for pagination

        query_text : typing.Optional[str]
            Search agents by name

        project_id : typing.Optional[str]
            Search agents by project ID - this will default to your default project on cloud

        template_id : typing.Optional[str]
            Search agents by template ID

        base_template_id : typing.Optional[str]
            Search agents by base template ID

        identity_id : typing.Optional[str]
            Search agents by identity ID

        identifier_keys : typing.Optional[typing.Sequence[str]]
            Search agents by identifier keys

        include_relationships : typing.Optional[typing.Sequence[str]]
            Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.

        include : typing.Optional[typing.Union[ListAgentsRequestIncludeItem, typing.Sequence[ListAgentsRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        order : typing.Optional[ListAgentsRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsRequestOrderBy]
            Field to sort by

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default)

        sort_by : typing.Optional[str]
            Field to sort by. Options: 'created_at' (default), 'last_run_completion'

        last_stop_reason : typing.Optional[StopReasonType]
            Filter agents by their last stop reason.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/",
            method="GET",
            params={
                "name": name,
                "tags": tags,
                "match_all_tags": match_all_tags,
                "before": before,
                "after": after,
                "limit": limit,
                "query_text": query_text,
                "project_id": project_id,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "identity_id": identity_id,
                "identifier_keys": identifier_keys,
                "include_relationships": include_relationships,
                "include": include,
                "order": order,
                "order_by": order_by,
                "ascending": ascending,
                "sort_by": sort_by,
                "last_stop_reason": last_stop_reason,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentState],
                    parse_obj_as(
                        type_=typing.List[AgentState],
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

    def create_agent(
        self,
        *,
        project: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        memory_blocks: typing.Optional[typing.Sequence[CreateBlock]] = OMIT,
        tools: typing.Optional[typing.Sequence[str]] = OMIT,
        tool_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        tool_rules: typing.Optional[typing.Sequence[CreateAgentRequestToolRulesItem]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        system: typing.Optional[str] = OMIT,
        agent_type: typing.Optional[AgentType] = OMIT,
        initial_message_sequence: typing.Optional[typing.Sequence[MessageCreate]] = OMIT,
        include_base_tools: typing.Optional[bool] = OMIT,
        include_multi_agent_tools: typing.Optional[bool] = OMIT,
        include_base_tool_rules: typing.Optional[bool] = OMIT,
        include_default_source: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_config: typing.Optional[LlmConfig] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        model: typing.Optional[str] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        model_settings: typing.Optional[CreateAgentRequestModelSettings] = OMIT,
        compaction_settings: typing.Optional[CompactionSettingsInput] = OMIT,
        context_window_limit: typing.Optional[int] = OMIT,
        embedding_chunk_size: typing.Optional[int] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        max_reasoning_tokens: typing.Optional[int] = OMIT,
        enable_reasoner: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[bool] = OMIT,
        from_template: typing.Optional[str] = OMIT,
        template: typing.Optional[bool] = OMIT,
        create_agent_request_project: typing.Optional[str] = OMIT,
        tool_exec_environment_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        memory_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        identity_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        message_buffer_autoclear: typing.Optional[bool] = OMIT,
        enable_sleeptime: typing.Optional[bool] = OMIT,
        response_format: typing.Optional[CreateAgentRequestResponseFormat] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        max_files_open: typing.Optional[int] = OMIT,
        per_file_view_window_char_limit: typing.Optional[int] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentState]:
        """
        Create an agent.

        Parameters
        ----------
        project : typing.Optional[str]
            The project slug to associate with the agent (cloud only).

        name : typing.Optional[str]
            The name of the agent.

        memory_blocks : typing.Optional[typing.Sequence[CreateBlock]]
            The blocks to create in the agent's in-context memory.

        tools : typing.Optional[typing.Sequence[str]]
            The tools used by the agent.

        tool_ids : typing.Optional[typing.Sequence[str]]
            The ids of the tools used by the agent.

        source_ids : typing.Optional[typing.Sequence[str]]
            Deprecated: Use `folder_ids` field instead. The ids of the sources used by the agent.

        folder_ids : typing.Optional[typing.Sequence[str]]
            The ids of the folders used by the agent.

        block_ids : typing.Optional[typing.Sequence[str]]
            The ids of the blocks used by the agent.

        tool_rules : typing.Optional[typing.Sequence[CreateAgentRequestToolRulesItem]]
            The tool rules governing the agent.

        tags : typing.Optional[typing.Sequence[str]]
            The tags associated with the agent.

        system : typing.Optional[str]
            The system prompt used by the agent.

        agent_type : typing.Optional[AgentType]
            The type of agent.

        initial_message_sequence : typing.Optional[typing.Sequence[MessageCreate]]
            The initial set of messages to put in the agent's in-context memory.

        include_base_tools : typing.Optional[bool]
            If true, attaches the Letta core tools (e.g. core_memory related functions).

        include_multi_agent_tools : typing.Optional[bool]
            If true, attaches the Letta multi-agent tools (e.g. sending a message to another agent).

        include_base_tool_rules : typing.Optional[bool]
            If true, attaches the Letta base tool rules (e.g. deny all tools not explicitly allowed).

        include_default_source : typing.Optional[bool]
            If true, automatically creates and attaches a default data source for this agent.

        description : typing.Optional[str]
            The description of the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            The metadata of the agent.

        llm_config : typing.Optional[LlmConfig]
            Deprecated: Use `model` field instead. The LLM configuration used by the agent.

        embedding_config : typing.Optional[EmbeddingConfig]
            Deprecated: Use `embedding` field instead. The embedding configuration used by the agent.

        model : typing.Optional[str]
            The model handle for the agent to use (format: provider/model-name).

        embedding : typing.Optional[str]
            The embedding model handle used by the agent (format: provider/model-name).

        model_settings : typing.Optional[CreateAgentRequestModelSettings]
            The model settings for the agent.

        compaction_settings : typing.Optional[CompactionSettingsInput]
            The compaction settings configuration used for compaction.

        context_window_limit : typing.Optional[int]
            The context window limit used by the agent.

        embedding_chunk_size : typing.Optional[int]
            Deprecated: No longer used. The embedding chunk size used by the agent.

        max_tokens : typing.Optional[int]
            Deprecated: Use `model` field to configure max output tokens instead. The maximum number of tokens to generate, including reasoning step.

        max_reasoning_tokens : typing.Optional[int]
            Deprecated: Use `model` field to configure reasoning tokens instead. The maximum number of tokens to generate for reasoning step.

        enable_reasoner : typing.Optional[bool]
            Deprecated: Use `model` field to configure reasoning instead. Whether to enable internal extended thinking step for a reasoner model.

        reasoning : typing.Optional[bool]
            Deprecated: Use `model` field to configure reasoning instead. Whether to enable reasoning for this agent.

        from_template : typing.Optional[str]
            Deprecated: please use the 'create agents from a template' endpoint instead.

        template : typing.Optional[bool]
            Deprecated: No longer used.

        create_agent_request_project : typing.Optional[str]
            Deprecated: Project should now be passed via the X-Project header instead of in the request body. If using the SDK, this can be done via the x_project parameter.

        tool_exec_environment_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: Use `secrets` field instead. Environment variables for tool execution.

        secrets : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The environment variables for tool execution specific to this agent.

        memory_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: Only relevant for creating agents from a template. Use the 'create agents from a template' endpoint instead.

        project_id : typing.Optional[str]
            Deprecated: No longer used. The id of the project the agent belongs to.

        template_id : typing.Optional[str]
            Deprecated: No longer used. The id of the template the agent belongs to.

        base_template_id : typing.Optional[str]
            Deprecated: No longer used. The base template id of the agent.

        identity_ids : typing.Optional[typing.Sequence[str]]
            The ids of the identities associated with this agent.

        message_buffer_autoclear : typing.Optional[bool]
            If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.

        enable_sleeptime : typing.Optional[bool]
            If set to True, memory management will move to a background agent thread.

        response_format : typing.Optional[CreateAgentRequestResponseFormat]
            Deprecated: Use `model_settings` field to configure response format instead. The response format for the agent.

        timezone : typing.Optional[str]
            The timezone of the agent (IANA format).

        max_files_open : typing.Optional[int]
            Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.

        per_file_view_window_char_limit : typing.Optional[int]
            The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.

        hidden : typing.Optional[bool]
            Deprecated: No longer used. If set to True, the agent will be hidden.

        parallel_tool_calls : typing.Optional[bool]
            Deprecated: Use `model_settings` to configure parallel tool calls instead. If set to True, enables parallel tool calling.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/",
            method="POST",
            json={
                "name": name,
                "memory_blocks": convert_and_respect_annotation_metadata(
                    object_=memory_blocks, annotation=typing.Optional[typing.Sequence[CreateBlock]], direction="write"
                ),
                "tools": tools,
                "tool_ids": tool_ids,
                "source_ids": source_ids,
                "folder_ids": folder_ids,
                "block_ids": block_ids,
                "tool_rules": convert_and_respect_annotation_metadata(
                    object_=tool_rules,
                    annotation=typing.Optional[typing.Sequence[CreateAgentRequestToolRulesItem]],
                    direction="write",
                ),
                "tags": tags,
                "system": system,
                "agent_type": agent_type,
                "initial_message_sequence": convert_and_respect_annotation_metadata(
                    object_=initial_message_sequence,
                    annotation=typing.Optional[typing.Sequence[MessageCreate]],
                    direction="write",
                ),
                "include_base_tools": include_base_tools,
                "include_multi_agent_tools": include_multi_agent_tools,
                "include_base_tool_rules": include_base_tool_rules,
                "include_default_source": include_default_source,
                "description": description,
                "metadata": metadata,
                "llm_config": convert_and_respect_annotation_metadata(
                    object_=llm_config, annotation=typing.Optional[LlmConfig], direction="write"
                ),
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
                "model": model,
                "embedding": embedding,
                "model_settings": convert_and_respect_annotation_metadata(
                    object_=model_settings,
                    annotation=typing.Optional[CreateAgentRequestModelSettings],
                    direction="write",
                ),
                "compaction_settings": convert_and_respect_annotation_metadata(
                    object_=compaction_settings, annotation=typing.Optional[CompactionSettingsInput], direction="write"
                ),
                "context_window_limit": context_window_limit,
                "embedding_chunk_size": embedding_chunk_size,
                "max_tokens": max_tokens,
                "max_reasoning_tokens": max_reasoning_tokens,
                "enable_reasoner": enable_reasoner,
                "reasoning": reasoning,
                "from_template": from_template,
                "template": template,
                "project": create_agent_request_project,
                "tool_exec_environment_variables": tool_exec_environment_variables,
                "secrets": secrets,
                "memory_variables": memory_variables,
                "project_id": project_id,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "identity_ids": identity_ids,
                "message_buffer_autoclear": message_buffer_autoclear,
                "enable_sleeptime": enable_sleeptime,
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format,
                    annotation=typing.Optional[CreateAgentRequestResponseFormat],
                    direction="write",
                ),
                "timezone": timezone,
                "max_files_open": max_files_open,
                "per_file_view_window_char_limit": per_file_view_window_char_limit,
                "hidden": hidden,
                "parallel_tool_calls": parallel_tool_calls,
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
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    def count_agents(
        self,
        *,
        name: typing.Optional[str] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        match_all_tags: typing.Optional[bool] = None,
        query_text: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        base_template_id: typing.Optional[str] = None,
        identity_id: typing.Optional[str] = None,
        identifier_keys: typing.Optional[typing.Sequence[str]] = None,
        last_stop_reason: typing.Optional[StopReasonType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Get the total number of agents with optional filtering.
        Supports the same filters as list_agents for consistent querying.

        Parameters
        ----------
        name : typing.Optional[str]
            Name of the agent

        tags : typing.Optional[typing.Sequence[str]]
            List of tags to filter agents by

        match_all_tags : typing.Optional[bool]
            If True, only counts agents that match ALL given tags. Otherwise, counts agents that have ANY of the passed-in tags.

        query_text : typing.Optional[str]
            Search agents by name

        project_id : typing.Optional[str]
            Search agents by project ID - this will default to your default project on cloud

        template_id : typing.Optional[str]
            Search agents by template ID

        base_template_id : typing.Optional[str]
            Search agents by base template ID

        identity_id : typing.Optional[str]
            Search agents by identity ID

        identifier_keys : typing.Optional[typing.Sequence[str]]
            Search agents by identifier keys

        last_stop_reason : typing.Optional[StopReasonType]
            Filter agents by their last stop reason.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/count",
            method="GET",
            params={
                "name": name,
                "tags": tags,
                "match_all_tags": match_all_tags,
                "query_text": query_text,
                "project_id": project_id,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "identity_id": identity_id,
                "identifier_keys": identifier_keys,
                "last_stop_reason": last_stop_reason,
            },
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

    def export_agent(
        self,
        agent_id: str,
        *,
        max_steps: typing.Optional[int] = None,
        use_legacy_format: typing.Optional[bool] = None,
        conversation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Export the serialized JSON representation of an agent, formatted with indentation.

        Parameters
        ----------
        agent_id : str

        max_steps : typing.Optional[int]

        use_legacy_format : typing.Optional[bool]
            If True, exports using the legacy single-agent 'v1' format with inline tools/blocks. If False, exports using the new multi-entity 'v2' format, with separate agents, tools, blocks, files, etc.

        conversation_id : typing.Optional[str]
            Conversation ID to export. If provided, uses messages from this conversation instead of the agent's global message history.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/export",
            method="GET",
            params={
                "max_steps": max_steps,
                "use_legacy_format": use_legacy_format,
                "conversation_id": conversation_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def import_agent(
        self,
        *,
        file: core.File,
        override_embedding_model: typing.Optional[str] = None,
        override_existing_tools: typing.Optional[bool] = OMIT,
        strip_messages: typing.Optional[bool] = OMIT,
        secrets: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        append_copy_suffix: typing.Optional[bool] = OMIT,
        override_name: typing.Optional[str] = OMIT,
        override_embedding_handle: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        env_vars_json: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImportedAgentsResponse]:
        """
        Import a serialized agent file and recreate the agent(s) in the system.
        Returns the IDs of all imported agents.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        override_embedding_model : typing.Optional[str]

        override_existing_tools : typing.Optional[bool]
            If set to True, existing tools can get their source code overwritten by the uploaded tool definitions. Note that Letta core tools can never be updated externally.

        strip_messages : typing.Optional[bool]
            If set to True, strips all messages from the agent before importing.

        secrets : typing.Optional[str]
            Secrets as a JSON string to pass to the agent for tool execution.

        name : typing.Optional[str]
            If provided, overrides the agent name with this value.

        embedding : typing.Optional[str]
            Embedding handle to override with.

        append_copy_suffix : typing.Optional[bool]
            If set to True, appends "_copy" to the end of the agent name.

        override_name : typing.Optional[str]
            If provided, overrides the agent name with this value. Use 'name' instead.

        override_embedding_handle : typing.Optional[str]
            Override import with specific embedding handle. Use 'embedding' instead.

        project_id : typing.Optional[str]
            The project ID to associate the uploaded agent with. This is now passed via headers.

        env_vars_json : typing.Optional[str]
            Environment variables as a JSON string to pass to the agent for tool execution. Use 'secrets' instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportedAgentsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/import",
            method="POST",
            data={
                "override_existing_tools": override_existing_tools,
                "strip_messages": strip_messages,
                "secrets": secrets,
                "name": name,
                "embedding": embedding,
                "append_copy_suffix": append_copy_suffix,
                "override_name": override_name,
                "override_embedding_handle": override_embedding_handle,
                "project_id": project_id,
                "env_vars_json": env_vars_json,
            },
            files={
                "file": file,
            },
            headers={
                "x-override-embedding-model": str(override_embedding_model)
                if override_embedding_model is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportedAgentsResponse,
                    parse_obj_as(
                        type_=ImportedAgentsResponse,
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

    def retrieve_agent_context_window(
        self,
        agent_id: str,
        *,
        conversation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContextWindowOverview]:
        """
        Retrieve the context window of a specific agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        conversation_id : typing.Optional[str]
            Conversation ID to get context window for. If provided, uses messages from this conversation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextWindowOverview]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/context",
            method="GET",
            params={
                "conversation_id": conversation_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextWindowOverview,
                    parse_obj_as(
                        type_=ContextWindowOverview,
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

    def retrieve_agent(
        self,
        agent_id: str,
        *,
        include_relationships: typing.Optional[typing.Sequence[str]] = None,
        include: typing.Optional[
            typing.Union[RetrieveAgentRequestIncludeItem, typing.Sequence[RetrieveAgentRequestIncludeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentState]:
        """
        Get the state of the agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        include_relationships : typing.Optional[typing.Sequence[str]]
            Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.

        include : typing.Optional[typing.Union[RetrieveAgentRequestIncludeItem, typing.Sequence[RetrieveAgentRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}",
            method="GET",
            params={
                "include_relationships": include_relationships,
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    def delete_agent(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}",
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

    def modify_agent(
        self,
        agent_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        tool_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        system: typing.Optional[str] = OMIT,
        tool_rules: typing.Optional[typing.Sequence[UpdateAgentToolRulesItem]] = OMIT,
        message_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tool_exec_environment_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        identity_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        message_buffer_autoclear: typing.Optional[bool] = OMIT,
        model: typing.Optional[str] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        model_settings: typing.Optional[UpdateAgentModelSettings] = OMIT,
        compaction_settings: typing.Optional[CompactionSettingsInput] = OMIT,
        context_window_limit: typing.Optional[int] = OMIT,
        reasoning: typing.Optional[bool] = OMIT,
        llm_config: typing.Optional[LlmConfig] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        response_format: typing.Optional[UpdateAgentResponseFormat] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        enable_sleeptime: typing.Optional[bool] = OMIT,
        last_run_completion: typing.Optional[dt.datetime] = OMIT,
        last_run_duration_ms: typing.Optional[int] = OMIT,
        last_stop_reason: typing.Optional[StopReasonType] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        max_files_open: typing.Optional[int] = OMIT,
        per_file_view_window_char_limit: typing.Optional[int] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentState]:
        """
        Update an existing agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        name : typing.Optional[str]
            The name of the agent.

        tool_ids : typing.Optional[typing.Sequence[str]]
            The ids of the tools used by the agent.

        source_ids : typing.Optional[typing.Sequence[str]]
            Deprecated: Use `folder_ids` field instead. The ids of the sources used by the agent.

        folder_ids : typing.Optional[typing.Sequence[str]]
            The ids of the folders used by the agent.

        block_ids : typing.Optional[typing.Sequence[str]]
            The ids of the blocks used by the agent.

        tags : typing.Optional[typing.Sequence[str]]
            The tags associated with the agent.

        system : typing.Optional[str]
            The system prompt used by the agent.

        tool_rules : typing.Optional[typing.Sequence[UpdateAgentToolRulesItem]]
            The tool rules governing the agent.

        message_ids : typing.Optional[typing.Sequence[str]]
            The ids of the messages in the agent's in-context memory.

        description : typing.Optional[str]
            The description of the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            The metadata of the agent.

        tool_exec_environment_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: use `secrets` field instead

        secrets : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The environment variables for tool execution specific to this agent.

        project_id : typing.Optional[str]
            The id of the project the agent belongs to.

        template_id : typing.Optional[str]
            The id of the template the agent belongs to.

        base_template_id : typing.Optional[str]
            The base template id of the agent.

        identity_ids : typing.Optional[typing.Sequence[str]]
            The ids of the identities associated with this agent.

        message_buffer_autoclear : typing.Optional[bool]
            If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.

        model : typing.Optional[str]
            The model handle used by the agent (format: provider/model-name).

        embedding : typing.Optional[str]
            The embedding model handle used by the agent (format: provider/model-name).

        model_settings : typing.Optional[UpdateAgentModelSettings]
            The model settings for the agent.

        compaction_settings : typing.Optional[CompactionSettingsInput]
            The compaction settings configuration used for compaction.

        context_window_limit : typing.Optional[int]
            The context window limit used by the agent.

        reasoning : typing.Optional[bool]
            Deprecated: Use `model` field to configure reasoning instead. Whether to enable reasoning for this agent.

        llm_config : typing.Optional[LlmConfig]
            Deprecated: Use `model` field instead. The LLM configuration used by the agent.

        embedding_config : typing.Optional[EmbeddingConfig]
            The embedding configuration used by the agent.

        parallel_tool_calls : typing.Optional[bool]
            Deprecated: Use `model_settings` to configure parallel tool calls instead. If set to True, enables parallel tool calling.

        response_format : typing.Optional[UpdateAgentResponseFormat]
            Deprecated: Use `model_settings` field to configure response format instead. The response format for the agent.

        max_tokens : typing.Optional[int]
            Deprecated: Use `model` field to configure max output tokens instead. The maximum number of tokens to generate, including reasoning step.

        enable_sleeptime : typing.Optional[bool]
            If set to True, memory management will move to a background agent thread.

        last_run_completion : typing.Optional[dt.datetime]
            The timestamp when the agent last completed a run.

        last_run_duration_ms : typing.Optional[int]
            The duration in milliseconds of the agent's last run.

        last_stop_reason : typing.Optional[StopReasonType]
            The stop reason from the agent's last run.

        timezone : typing.Optional[str]
            The timezone of the agent (IANA format).

        max_files_open : typing.Optional[int]
            Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.

        per_file_view_window_char_limit : typing.Optional[int]
            The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.

        hidden : typing.Optional[bool]
            If set to True, the agent will be hidden.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}",
            method="PATCH",
            json={
                "name": name,
                "tool_ids": tool_ids,
                "source_ids": source_ids,
                "folder_ids": folder_ids,
                "block_ids": block_ids,
                "tags": tags,
                "system": system,
                "tool_rules": convert_and_respect_annotation_metadata(
                    object_=tool_rules,
                    annotation=typing.Optional[typing.Sequence[UpdateAgentToolRulesItem]],
                    direction="write",
                ),
                "message_ids": message_ids,
                "description": description,
                "metadata": metadata,
                "tool_exec_environment_variables": tool_exec_environment_variables,
                "secrets": secrets,
                "project_id": project_id,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "identity_ids": identity_ids,
                "message_buffer_autoclear": message_buffer_autoclear,
                "model": model,
                "embedding": embedding,
                "model_settings": convert_and_respect_annotation_metadata(
                    object_=model_settings, annotation=typing.Optional[UpdateAgentModelSettings], direction="write"
                ),
                "compaction_settings": convert_and_respect_annotation_metadata(
                    object_=compaction_settings, annotation=typing.Optional[CompactionSettingsInput], direction="write"
                ),
                "context_window_limit": context_window_limit,
                "reasoning": reasoning,
                "llm_config": convert_and_respect_annotation_metadata(
                    object_=llm_config, annotation=typing.Optional[LlmConfig], direction="write"
                ),
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
                "parallel_tool_calls": parallel_tool_calls,
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format, annotation=typing.Optional[UpdateAgentResponseFormat], direction="write"
                ),
                "max_tokens": max_tokens,
                "enable_sleeptime": enable_sleeptime,
                "last_run_completion": last_run_completion,
                "last_run_duration_ms": last_run_duration_ms,
                "last_stop_reason": last_stop_reason,
                "timezone": timezone,
                "max_files_open": max_files_open,
                "per_file_view_window_char_limit": per_file_view_window_char_limit,
                "hidden": hidden,
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
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    def list_tools_for_agent(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListToolsForAgentRequestOrder] = None,
        order_by: typing.Optional[ListToolsForAgentRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Tool]]:
        """
        Get tools from an existing agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Tool ID cursor for pagination. Returns tools that come before this tool ID in the specified sort order

        after : typing.Optional[str]
            Tool ID cursor for pagination. Returns tools that come after this tool ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of tools to return

        order : typing.Optional[ListToolsForAgentRequestOrder]
            Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListToolsForAgentRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Tool]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Tool],
                    parse_obj_as(
                        type_=typing.List[Tool],
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

    def attach_tool_to_agent(
        self, agent_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AgentState]]:
        """
        Attach a tool to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools/attach/{encode_path_param(tool_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    def detach_tool_from_agent(
        self, agent_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AgentState]]:
        """
        Detach a tool from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools/detach/{encode_path_param(tool_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    def modify_approval_for_tool(
        self,
        agent_id: str,
        tool_name: str,
        *,
        requires_approval: typing.Optional[bool] = None,
        request: typing.Optional[ModifyApprovalRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[AgentState]]:
        """
        Modify the approval requirement for a tool attached to an agent.

        Accepts requires_approval via request body (preferred) or query parameter (deprecated).

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        tool_name : str

        requires_approval : typing.Optional[bool]
            Whether the tool requires approval before execution

        request : typing.Optional[ModifyApprovalRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools/approval/{encode_path_param(tool_name)}",
            method="PATCH",
            params={
                "requires_approval": requires_approval,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ModifyApprovalRequest], direction="write"
            ),
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
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    def run_tool_for_agent(
        self,
        agent_id: str,
        tool_name: str,
        *,
        args: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolExecutionResult]:
        """
        Trigger a tool by name on a specific agent, providing the necessary arguments.

        This endpoint executes a tool that is attached to the agent, using the agent's
        state and environment variables for execution context.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        tool_name : str

        args : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the tool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToolExecutionResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools/{encode_path_param(tool_name)}/run",
            method="POST",
            json={
                "args": args,
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
                    ToolExecutionResult,
                    parse_obj_as(
                        type_=ToolExecutionResult,
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

    def attach_source_to_agent(
        self, agent_id: str, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgentState]:
        """
        Attach a source to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/sources/attach/{encode_path_param(source_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    def attach_folder_to_agent(
        self, agent_id: str, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AgentState]]:
        """
        Attach a folder to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/folders/attach/{encode_path_param(folder_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    def detach_source_from_agent(
        self, agent_id: str, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgentState]:
        """
        Detach a source from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/sources/detach/{encode_path_param(source_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    def detach_folder_from_agent(
        self, agent_id: str, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AgentState]]:
        """
        Detach a folder from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/folders/detach/{encode_path_param(folder_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    def close_all_files_for_agent(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Closes all currently open files for a given agent.

        This endpoint updates the file state for the agent so that no files are marked as open.
        Typically used to reset the working memory view for the agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/files/close-all",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def open_file_for_agent(
        self, agent_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Opens a specific file for a given agent.

        This endpoint marks a specific file as open in the agent's file state.
        The file will be included in the agent's working memory view.
        Returns a list of file names that were closed due to LRU eviction.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/files/{encode_path_param(file_id)}/open",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def close_file_for_agent(
        self, agent_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Closes a specific file for a given agent.

        This endpoint marks a specific file as closed in the agent's file state.
        The file will be removed from the agent's working memory view.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/files/{encode_path_param(file_id)}/close",
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

    def list_agent_sources(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentSourcesRequestOrder] = None,
        order_by: typing.Optional[ListAgentSourcesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Source]]:
        """
        Get the sources associated with an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Source ID cursor for pagination. Returns sources that come before this source ID in the specified sort order

        after : typing.Optional[str]
            Source ID cursor for pagination. Returns sources that come after this source ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of sources to return

        order : typing.Optional[ListAgentSourcesRequestOrder]
            Sort order for sources by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentSourcesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Source]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/sources",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Source],
                    parse_obj_as(
                        type_=typing.List[Source],
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

    def list_folders_for_agent(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFoldersForAgentRequestOrder] = None,
        order_by: typing.Optional[ListFoldersForAgentRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Source]]:
        """
        Get the folders associated with an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Source ID cursor for pagination. Returns sources that come before this source ID in the specified sort order

        after : typing.Optional[str]
            Source ID cursor for pagination. Returns sources that come after this source ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of sources to return

        order : typing.Optional[ListFoldersForAgentRequestOrder]
            Sort order for sources by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFoldersForAgentRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Source]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/folders",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Source],
                    parse_obj_as(
                        type_=typing.List[Source],
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

    def list_files_for_agent(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFilesForAgentRequestOrder] = None,
        order_by: typing.Optional[ListFilesForAgentRequestOrderBy] = None,
        cursor: typing.Optional[str] = None,
        is_open: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedAgentFiles]:
        """
        Get the files attached to an agent with their open/closed status.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            File ID cursor for pagination. Returns files that come before this file ID in the specified sort order

        after : typing.Optional[str]
            File ID cursor for pagination. Returns files that come after this file ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of files to return

        order : typing.Optional[ListFilesForAgentRequestOrder]
            Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFilesForAgentRequestOrderBy]
            Field to sort by

        cursor : typing.Optional[str]
            Pagination cursor from previous response (deprecated, use before/after)

        is_open : typing.Optional[bool]
            Filter by open status (true for open files, false for closed files)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedAgentFiles]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/files",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "cursor": cursor,
                "is_open": is_open,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedAgentFiles,
                    parse_obj_as(
                        type_=PaginatedAgentFiles,
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

    def retrieve_agent_memory(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Memory]:
        """
        Retrieve the memory state of a specific agent.
        This endpoint fetches the current memory state of the agent identified by the user ID and agent ID.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Memory]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Memory,
                    parse_obj_as(
                        type_=Memory,
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

    def retrieve_core_memory_block(
        self, agent_id: str, block_label: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BlockResponse]:
        """
        Retrieve a core memory block from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BlockResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks/{encode_path_param(block_label)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
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

    def modify_core_memory_block(
        self,
        agent_id: str,
        block_label: str,
        *,
        value: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BlockResponse]:
        """
        Updates a core memory block of an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_label : str

        value : typing.Optional[str]
            Value of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]
            Whether the block is a template (e.g. saved human/persona options).

        template_id : typing.Optional[str]
            The id of the template.

        base_template_id : typing.Optional[str]
            The base template id of the block.

        deployment_id : typing.Optional[str]
            The id of the deployment.

        entity_id : typing.Optional[str]
            The id of the entity within the template.

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

        label : typing.Optional[str]
            Label of the block (e.g. 'human', 'persona') in the context window.

        read_only : typing.Optional[bool]
            Whether the agent has read-only access to the block.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the block.

        hidden : typing.Optional[bool]
            If set to True, the block will be hidden.

        tags : typing.Optional[typing.Sequence[str]]
            The tags to associate with the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BlockResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks/{encode_path_param(block_label)}",
            method="PATCH",
            json={
                "value": value,
                "limit": limit,
                "project_id": project_id,
                "template_name": template_name,
                "is_template": is_template,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "deployment_id": deployment_id,
                "entity_id": entity_id,
                "preserve_on_migration": preserve_on_migration,
                "label": label,
                "read_only": read_only,
                "description": description,
                "metadata": metadata,
                "hidden": hidden,
                "tags": tags,
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
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
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

    def list_core_memory_blocks(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListCoreMemoryBlocksRequestOrder] = None,
        order_by: typing.Optional[ListCoreMemoryBlocksRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[BlockResponse]]:
        """
        Retrieve the core memory blocks of a specific agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of blocks to return

        order : typing.Optional[ListCoreMemoryBlocksRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListCoreMemoryBlocksRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[BlockResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BlockResponse],
                    parse_obj_as(
                        type_=typing.List[BlockResponse],
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

    def attach_core_memory_block(
        self, agent_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgentState]:
        """
        Attach a core memory block to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks/attach/{encode_path_param(block_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    def detach_core_memory_block(
        self, agent_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgentState]:
        """
        Detach a core memory block from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks/detach/{encode_path_param(block_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    def attach_archive_to_agent(
        self, agent_id: str, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Attach an archive to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        archive_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archives/attach/{encode_path_param(archive_id)}",
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

    def detach_archive_from_agent(
        self, agent_id: str, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Detach an archive from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        archive_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archives/detach/{encode_path_param(archive_id)}",
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

    def attach_identity_to_agent(
        self, agent_id: str, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Attach an identity to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/identities/attach/{encode_path_param(identity_id)}",
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

    def detach_identity_from_agent(
        self, agent_id: str, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Detach an identity from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/identities/detach/{encode_path_param(identity_id)}",
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

    def list_passages(
        self,
        agent_id: str,
        *,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Passage]]:
        """
        Retrieve the memories in an agent's archival memory store (paginated query).

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        after : typing.Optional[str]
            Unique ID of the memory to start the query range at.

        before : typing.Optional[str]
            Unique ID of the memory to end the query range at.

        limit : typing.Optional[int]
            How many results to include in the response.

        search : typing.Optional[str]
            Search passages by text

        ascending : typing.Optional[bool]
            Whether to sort passages oldest to newest (True, default) or newest to oldest (False)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Passage]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archival-memory",
            method="GET",
            params={
                "after": after,
                "before": before,
                "limit": limit,
                "search": search,
                "ascending": ascending,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],
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

    def create_passage(
        self,
        agent_id: str,
        *,
        text: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Passage]]:
        """
        Insert a memory into an agent's archival memory store.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        text : str
            Text to write to archival memory.

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of tags to attach to the memory.

        created_at : typing.Optional[dt.datetime]
            Optional timestamp for the memory (defaults to current UTC time).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Passage]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archival-memory",
            method="POST",
            json={
                "text": text,
                "tags": tags,
                "created_at": created_at,
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
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],
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

    def search_archival_memory(
        self,
        agent_id: str,
        *,
        query: str,
        tags: typing.Optional[typing.Sequence[str]] = None,
        tag_match_mode: typing.Optional[SearchArchivalMemoryRequestTagMatchMode] = None,
        top_k: typing.Optional[int] = None,
        start_datetime: typing.Optional[dt.datetime] = None,
        end_datetime: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ArchivalMemorySearchResponse]:
        """
        Search archival memory using semantic (embedding-based) search with optional temporal filtering.

        This endpoint allows manual triggering of archival memory searches, enabling users to query
        an agent's archival memory store directly via the API. The search uses the same functionality
        as the agent's archival_memory_search tool but is accessible for external API usage.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        query : str
            String to search for using semantic similarity

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of tags to filter search results

        tag_match_mode : typing.Optional[SearchArchivalMemoryRequestTagMatchMode]
            How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags

        top_k : typing.Optional[int]
            Maximum number of results to return. Uses system default if not specified

        start_datetime : typing.Optional[dt.datetime]
            Filter results to passages created after this datetime

        end_datetime : typing.Optional[dt.datetime]
            Filter results to passages created before this datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArchivalMemorySearchResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archival-memory/search",
            method="GET",
            params={
                "query": query,
                "tags": tags,
                "tag_match_mode": tag_match_mode,
                "top_k": top_k,
                "start_datetime": serialize_datetime(start_datetime) if start_datetime is not None else None,
                "end_datetime": serialize_datetime(end_datetime) if end_datetime is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArchivalMemorySearchResponse,
                    parse_obj_as(
                        type_=ArchivalMemorySearchResponse,
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

    def delete_passage(
        self, agent_id: str, memory_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a memory from an agent's archival memory store.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        memory_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archival-memory/{encode_path_param(memory_id)}",
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

    def list_messages(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesRequestOrder] = None,
        order_by: typing.Optional[ListMessagesRequestOrderBy] = None,
        group_id: typing.Optional[str] = None,
        conversation_id: typing.Optional[str] = None,
        use_assistant_message: typing.Optional[bool] = None,
        assistant_message_tool_name: typing.Optional[str] = None,
        assistant_message_tool_kwarg: typing.Optional[str] = None,
        include_err: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[LettaMessageUnion]]:
        """
        Retrieve message history for an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesRequestOrderBy]
            Field to sort by

        group_id : typing.Optional[str]
            Group ID to filter messages by.

        conversation_id : typing.Optional[str]
            Conversation ID to filter messages by.

        use_assistant_message : typing.Optional[bool]
            Whether to use assistant messages

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument.

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
            f"v1/agents/{encode_path_param(agent_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "group_id": group_id,
                "conversation_id": conversation_id,
                "use_assistant_message": use_assistant_message,
                "assistant_message_tool_name": assistant_message_tool_name,
                "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
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

    def send_message(
        self,
        agent_id: str,
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
    ) -> HttpResponse[LettaResponse]:
        """
        Process a user message and return the agent's response.
        This endpoint accepts a message from a user and processes it through the agent.

        The response format is controlled by the `streaming` field in the request body:
        - If `streaming=false` (default): Returns a complete LettaResponse with all messages
        - If `streaming=true`: Returns a Server-Sent Events (SSE) stream

        Additional streaming options (only used when streaming=true):
        - `stream_tokens`: Stream individual tokens instead of complete steps
        - `include_pings`: Include keepalive pings to prevent connection timeouts
        - `background`: Process the request in the background

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

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
        HttpResponse[LettaResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages",
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

    def modify_message(
        self,
        agent_id: str,
        message_id: str,
        *,
        request: ModifyMessageRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ModifyMessageResponse]:
        """
        Update the details of a message associated with an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        message_id : str
            The ID of the message in the format 'message-<uuid4>'

        request : ModifyMessageRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ModifyMessageResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages/{encode_path_param(message_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ModifyMessageRequestBody, direction="write"
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
                    ModifyMessageResponse,
                    parse_obj_as(
                        type_=ModifyMessageResponse,
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

    def create_agent_message_stream(
        self,
        agent_id: str,
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
        Process a user message and return the agent's response.

        Deprecated: Use the `POST /{agent_id}/messages` endpoint with `streaming=true` in the request body instead.

        This endpoint accepts a message from a user and processes it through the agent.
        It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

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
            f"v1/agents/{encode_path_param(agent_id)}/messages/stream",
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

    def cancel_message(
        self,
        agent_id: str,
        *,
        run_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Cancel runs associated with an agent. If run_ids are passed in, cancel those in particular.

        Note to cancel active runs associated with an agent, redis is required.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        run_ids : typing.Optional[typing.Sequence[str]]
            Optional list of run IDs to cancel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages/cancel",
            method="POST",
            json={
                "run_ids": run_ids,
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

    def search_messages(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        search_mode: typing.Optional[MessageSearchRequestSearchMode] = OMIT,
        roles: typing.Optional[typing.Sequence[MessageRole]] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[MessageSearchResult]]:
        """
        Search messages across the entire organization with optional project and template filtering. Returns messages with FTS/vector ranks and total RRF score.

        This is a cloud-only feature.

        Parameters
        ----------
        query : typing.Optional[str]
            Text query for full-text search

        search_mode : typing.Optional[MessageSearchRequestSearchMode]
            Search mode to use

        roles : typing.Optional[typing.Sequence[MessageRole]]
            Filter messages by role

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        project_id : typing.Optional[str]
            Filter messages by project ID

        template_id : typing.Optional[str]
            Filter messages by template ID

        conversation_id : typing.Optional[str]
            Filter messages by conversation ID

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter messages created after this date

        end_date : typing.Optional[dt.datetime]
            Filter messages created on or before this date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[MessageSearchResult]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/messages/search",
            method="POST",
            json={
                "query": query,
                "search_mode": search_mode,
                "roles": roles,
                "agent_id": agent_id,
                "project_id": project_id,
                "template_id": template_id,
                "conversation_id": conversation_id,
                "limit": limit,
                "start_date": start_date,
                "end_date": end_date,
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
                    typing.List[MessageSearchResult],
                    parse_obj_as(
                        type_=typing.List[MessageSearchResult],
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

    def create_agent_message_async(
        self,
        agent_id: str,
        *,
        messages: typing.Optional[typing.Sequence[LettaAsyncRequestMessagesItem]] = OMIT,
        input: typing.Optional[LettaAsyncRequestInput] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        client_tools: typing.Optional[typing.Sequence[ClientToolSchema]] = OMIT,
        override_model: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Run]:
        """
        Asynchronously process a user message and return a run object.
        The actual processing happens in the background, and the status can be checked using the run ID.

        This is "asynchronous" in the sense that it's a background run and explicitly must be fetched by the run ID.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        messages : typing.Optional[typing.Sequence[LettaAsyncRequestMessagesItem]]
            The messages to be sent to the agent.

        input : typing.Optional[LettaAsyncRequestInput]
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

        callback_url : typing.Optional[str]
            Optional callback URL to POST to when the job completes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Run]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages/async",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Optional[typing.Sequence[LettaAsyncRequestMessagesItem]],
                    direction="write",
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[LettaAsyncRequestInput], direction="write"
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
                "callback_url": callback_url,
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
                    Run,
                    parse_obj_as(
                        type_=Run,
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

    def reset_messages(
        self,
        agent_id: str,
        *,
        add_default_initial_messages: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[AgentState]]:
        """
        Resets the messages for an agent

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        add_default_initial_messages : typing.Optional[bool]
            If true, adds the default initial messages after resetting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/reset-messages",
            method="PATCH",
            json={
                "add_default_initial_messages": add_default_initial_messages,
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
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    def list_groups_for_agent(
        self,
        agent_id: str,
        *,
        manager_type: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListGroupsForAgentRequestOrder] = None,
        order_by: typing.Optional[ListGroupsForAgentRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Group]]:
        """
        Lists the groups for an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        manager_type : typing.Optional[str]
            Manager type to filter groups by

        before : typing.Optional[str]
            Group ID cursor for pagination. Returns groups that come before this group ID in the specified sort order

        after : typing.Optional[str]
            Group ID cursor for pagination. Returns groups that come after this group ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of groups to return

        order : typing.Optional[ListGroupsForAgentRequestOrder]
            Sort order for groups by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListGroupsForAgentRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Group]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/groups",
            method="GET",
            params={
                "manager_type": manager_type,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
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

    def preview_model_request(
        self,
        agent_id: str,
        *,
        request: PreviewModelRequestRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Inspect the raw LLM request payload without sending it.

        This endpoint processes the message through the agent loop up until
        the LLM request, then returns the raw request payload that would
        be sent to the LLM provider. Useful for debugging and inspection.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request : PreviewModelRequestRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages/preview-raw-payload",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PreviewModelRequestRequestBody, direction="write"
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

    def summarize_messages(
        self,
        agent_id: str,
        *,
        request: typing.Optional[CompactionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CompactionResponse]:
        """
        Summarize an agent's conversation history.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request : typing.Optional[CompactionRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompactionResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/summarize",
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

    def searchdeployedagents(
        self,
        *,
        search: typing.Optional[typing.Sequence[AgentsSearchDeployedAgentsRequestSearchItem]] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        combinator: typing.Optional[AgentsSearchDeployedAgentsRequestCombinator] = OMIT,
        limit: typing.Optional[float] = OMIT,
        after: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[AgentsSearchDeployedAgentsRequestSortBy] = OMIT,
        ascending: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentsSearchDeployedAgentsResponse]:
        """
        Search deployed agents

        Parameters
        ----------
        search : typing.Optional[typing.Sequence[AgentsSearchDeployedAgentsRequestSearchItem]]

        project_id : typing.Optional[str]

        combinator : typing.Optional[AgentsSearchDeployedAgentsRequestCombinator]

        limit : typing.Optional[float]

        after : typing.Optional[str]

        sort_by : typing.Optional[AgentsSearchDeployedAgentsRequestSortBy]

        ascending : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentsSearchDeployedAgentsResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/agents/search",
            method="POST",
            json={
                "search": convert_and_respect_annotation_metadata(
                    object_=search,
                    annotation=typing.Sequence[AgentsSearchDeployedAgentsRequestSearchItem],
                    direction="write",
                ),
                "project_id": project_id,
                "combinator": combinator,
                "limit": limit,
                "after": after,
                "sortBy": sort_by,
                "ascending": ascending,
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
                    AgentsSearchDeployedAgentsResponse,
                    parse_obj_as(
                        type_=AgentsSearchDeployedAgentsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getagentvariables(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgentsGetAgentVariablesResponse]:
        """
        Get the variables associated with an agent

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentsGetAgentVariablesResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentsGetAgentVariablesResponse,
                    parse_obj_as(
                        type_=AgentsGetAgentVariablesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_agents(
        self,
        *,
        name: typing.Optional[str] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        match_all_tags: typing.Optional[bool] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query_text: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        base_template_id: typing.Optional[str] = None,
        identity_id: typing.Optional[str] = None,
        identifier_keys: typing.Optional[typing.Sequence[str]] = None,
        include_relationships: typing.Optional[typing.Sequence[str]] = None,
        include: typing.Optional[
            typing.Union[ListAgentsRequestIncludeItem, typing.Sequence[ListAgentsRequestIncludeItem]]
        ] = None,
        order: typing.Optional[ListAgentsRequestOrder] = None,
        order_by: typing.Optional[ListAgentsRequestOrderBy] = None,
        ascending: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        last_stop_reason: typing.Optional[StopReasonType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[AgentState]]:
        """
        Get a list of all agents.

        Parameters
        ----------
        name : typing.Optional[str]
            Name of the agent

        tags : typing.Optional[typing.Sequence[str]]
            List of tags to filter agents by

        match_all_tags : typing.Optional[bool]
            If True, only returns agents that match ALL given tags. Otherwise, return agents that have ANY of the passed-in tags.

        before : typing.Optional[str]
            Cursor for pagination

        after : typing.Optional[str]
            Cursor for pagination

        limit : typing.Optional[int]
            Limit for pagination

        query_text : typing.Optional[str]
            Search agents by name

        project_id : typing.Optional[str]
            Search agents by project ID - this will default to your default project on cloud

        template_id : typing.Optional[str]
            Search agents by template ID

        base_template_id : typing.Optional[str]
            Search agents by base template ID

        identity_id : typing.Optional[str]
            Search agents by identity ID

        identifier_keys : typing.Optional[typing.Sequence[str]]
            Search agents by identifier keys

        include_relationships : typing.Optional[typing.Sequence[str]]
            Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.

        include : typing.Optional[typing.Union[ListAgentsRequestIncludeItem, typing.Sequence[ListAgentsRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        order : typing.Optional[ListAgentsRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsRequestOrderBy]
            Field to sort by

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default)

        sort_by : typing.Optional[str]
            Field to sort by. Options: 'created_at' (default), 'last_run_completion'

        last_stop_reason : typing.Optional[StopReasonType]
            Filter agents by their last stop reason.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/",
            method="GET",
            params={
                "name": name,
                "tags": tags,
                "match_all_tags": match_all_tags,
                "before": before,
                "after": after,
                "limit": limit,
                "query_text": query_text,
                "project_id": project_id,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "identity_id": identity_id,
                "identifier_keys": identifier_keys,
                "include_relationships": include_relationships,
                "include": include,
                "order": order,
                "order_by": order_by,
                "ascending": ascending,
                "sort_by": sort_by,
                "last_stop_reason": last_stop_reason,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentState],
                    parse_obj_as(
                        type_=typing.List[AgentState],
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

    async def create_agent(
        self,
        *,
        project: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        memory_blocks: typing.Optional[typing.Sequence[CreateBlock]] = OMIT,
        tools: typing.Optional[typing.Sequence[str]] = OMIT,
        tool_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        tool_rules: typing.Optional[typing.Sequence[CreateAgentRequestToolRulesItem]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        system: typing.Optional[str] = OMIT,
        agent_type: typing.Optional[AgentType] = OMIT,
        initial_message_sequence: typing.Optional[typing.Sequence[MessageCreate]] = OMIT,
        include_base_tools: typing.Optional[bool] = OMIT,
        include_multi_agent_tools: typing.Optional[bool] = OMIT,
        include_base_tool_rules: typing.Optional[bool] = OMIT,
        include_default_source: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_config: typing.Optional[LlmConfig] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        model: typing.Optional[str] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        model_settings: typing.Optional[CreateAgentRequestModelSettings] = OMIT,
        compaction_settings: typing.Optional[CompactionSettingsInput] = OMIT,
        context_window_limit: typing.Optional[int] = OMIT,
        embedding_chunk_size: typing.Optional[int] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        max_reasoning_tokens: typing.Optional[int] = OMIT,
        enable_reasoner: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[bool] = OMIT,
        from_template: typing.Optional[str] = OMIT,
        template: typing.Optional[bool] = OMIT,
        create_agent_request_project: typing.Optional[str] = OMIT,
        tool_exec_environment_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        memory_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        identity_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        message_buffer_autoclear: typing.Optional[bool] = OMIT,
        enable_sleeptime: typing.Optional[bool] = OMIT,
        response_format: typing.Optional[CreateAgentRequestResponseFormat] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        max_files_open: typing.Optional[int] = OMIT,
        per_file_view_window_char_limit: typing.Optional[int] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentState]:
        """
        Create an agent.

        Parameters
        ----------
        project : typing.Optional[str]
            The project slug to associate with the agent (cloud only).

        name : typing.Optional[str]
            The name of the agent.

        memory_blocks : typing.Optional[typing.Sequence[CreateBlock]]
            The blocks to create in the agent's in-context memory.

        tools : typing.Optional[typing.Sequence[str]]
            The tools used by the agent.

        tool_ids : typing.Optional[typing.Sequence[str]]
            The ids of the tools used by the agent.

        source_ids : typing.Optional[typing.Sequence[str]]
            Deprecated: Use `folder_ids` field instead. The ids of the sources used by the agent.

        folder_ids : typing.Optional[typing.Sequence[str]]
            The ids of the folders used by the agent.

        block_ids : typing.Optional[typing.Sequence[str]]
            The ids of the blocks used by the agent.

        tool_rules : typing.Optional[typing.Sequence[CreateAgentRequestToolRulesItem]]
            The tool rules governing the agent.

        tags : typing.Optional[typing.Sequence[str]]
            The tags associated with the agent.

        system : typing.Optional[str]
            The system prompt used by the agent.

        agent_type : typing.Optional[AgentType]
            The type of agent.

        initial_message_sequence : typing.Optional[typing.Sequence[MessageCreate]]
            The initial set of messages to put in the agent's in-context memory.

        include_base_tools : typing.Optional[bool]
            If true, attaches the Letta core tools (e.g. core_memory related functions).

        include_multi_agent_tools : typing.Optional[bool]
            If true, attaches the Letta multi-agent tools (e.g. sending a message to another agent).

        include_base_tool_rules : typing.Optional[bool]
            If true, attaches the Letta base tool rules (e.g. deny all tools not explicitly allowed).

        include_default_source : typing.Optional[bool]
            If true, automatically creates and attaches a default data source for this agent.

        description : typing.Optional[str]
            The description of the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            The metadata of the agent.

        llm_config : typing.Optional[LlmConfig]
            Deprecated: Use `model` field instead. The LLM configuration used by the agent.

        embedding_config : typing.Optional[EmbeddingConfig]
            Deprecated: Use `embedding` field instead. The embedding configuration used by the agent.

        model : typing.Optional[str]
            The model handle for the agent to use (format: provider/model-name).

        embedding : typing.Optional[str]
            The embedding model handle used by the agent (format: provider/model-name).

        model_settings : typing.Optional[CreateAgentRequestModelSettings]
            The model settings for the agent.

        compaction_settings : typing.Optional[CompactionSettingsInput]
            The compaction settings configuration used for compaction.

        context_window_limit : typing.Optional[int]
            The context window limit used by the agent.

        embedding_chunk_size : typing.Optional[int]
            Deprecated: No longer used. The embedding chunk size used by the agent.

        max_tokens : typing.Optional[int]
            Deprecated: Use `model` field to configure max output tokens instead. The maximum number of tokens to generate, including reasoning step.

        max_reasoning_tokens : typing.Optional[int]
            Deprecated: Use `model` field to configure reasoning tokens instead. The maximum number of tokens to generate for reasoning step.

        enable_reasoner : typing.Optional[bool]
            Deprecated: Use `model` field to configure reasoning instead. Whether to enable internal extended thinking step for a reasoner model.

        reasoning : typing.Optional[bool]
            Deprecated: Use `model` field to configure reasoning instead. Whether to enable reasoning for this agent.

        from_template : typing.Optional[str]
            Deprecated: please use the 'create agents from a template' endpoint instead.

        template : typing.Optional[bool]
            Deprecated: No longer used.

        create_agent_request_project : typing.Optional[str]
            Deprecated: Project should now be passed via the X-Project header instead of in the request body. If using the SDK, this can be done via the x_project parameter.

        tool_exec_environment_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: Use `secrets` field instead. Environment variables for tool execution.

        secrets : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The environment variables for tool execution specific to this agent.

        memory_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: Only relevant for creating agents from a template. Use the 'create agents from a template' endpoint instead.

        project_id : typing.Optional[str]
            Deprecated: No longer used. The id of the project the agent belongs to.

        template_id : typing.Optional[str]
            Deprecated: No longer used. The id of the template the agent belongs to.

        base_template_id : typing.Optional[str]
            Deprecated: No longer used. The base template id of the agent.

        identity_ids : typing.Optional[typing.Sequence[str]]
            The ids of the identities associated with this agent.

        message_buffer_autoclear : typing.Optional[bool]
            If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.

        enable_sleeptime : typing.Optional[bool]
            If set to True, memory management will move to a background agent thread.

        response_format : typing.Optional[CreateAgentRequestResponseFormat]
            Deprecated: Use `model_settings` field to configure response format instead. The response format for the agent.

        timezone : typing.Optional[str]
            The timezone of the agent (IANA format).

        max_files_open : typing.Optional[int]
            Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.

        per_file_view_window_char_limit : typing.Optional[int]
            The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.

        hidden : typing.Optional[bool]
            Deprecated: No longer used. If set to True, the agent will be hidden.

        parallel_tool_calls : typing.Optional[bool]
            Deprecated: Use `model_settings` to configure parallel tool calls instead. If set to True, enables parallel tool calling.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/",
            method="POST",
            json={
                "name": name,
                "memory_blocks": convert_and_respect_annotation_metadata(
                    object_=memory_blocks, annotation=typing.Optional[typing.Sequence[CreateBlock]], direction="write"
                ),
                "tools": tools,
                "tool_ids": tool_ids,
                "source_ids": source_ids,
                "folder_ids": folder_ids,
                "block_ids": block_ids,
                "tool_rules": convert_and_respect_annotation_metadata(
                    object_=tool_rules,
                    annotation=typing.Optional[typing.Sequence[CreateAgentRequestToolRulesItem]],
                    direction="write",
                ),
                "tags": tags,
                "system": system,
                "agent_type": agent_type,
                "initial_message_sequence": convert_and_respect_annotation_metadata(
                    object_=initial_message_sequence,
                    annotation=typing.Optional[typing.Sequence[MessageCreate]],
                    direction="write",
                ),
                "include_base_tools": include_base_tools,
                "include_multi_agent_tools": include_multi_agent_tools,
                "include_base_tool_rules": include_base_tool_rules,
                "include_default_source": include_default_source,
                "description": description,
                "metadata": metadata,
                "llm_config": convert_and_respect_annotation_metadata(
                    object_=llm_config, annotation=typing.Optional[LlmConfig], direction="write"
                ),
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
                "model": model,
                "embedding": embedding,
                "model_settings": convert_and_respect_annotation_metadata(
                    object_=model_settings,
                    annotation=typing.Optional[CreateAgentRequestModelSettings],
                    direction="write",
                ),
                "compaction_settings": convert_and_respect_annotation_metadata(
                    object_=compaction_settings, annotation=typing.Optional[CompactionSettingsInput], direction="write"
                ),
                "context_window_limit": context_window_limit,
                "embedding_chunk_size": embedding_chunk_size,
                "max_tokens": max_tokens,
                "max_reasoning_tokens": max_reasoning_tokens,
                "enable_reasoner": enable_reasoner,
                "reasoning": reasoning,
                "from_template": from_template,
                "template": template,
                "project": create_agent_request_project,
                "tool_exec_environment_variables": tool_exec_environment_variables,
                "secrets": secrets,
                "memory_variables": memory_variables,
                "project_id": project_id,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "identity_ids": identity_ids,
                "message_buffer_autoclear": message_buffer_autoclear,
                "enable_sleeptime": enable_sleeptime,
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format,
                    annotation=typing.Optional[CreateAgentRequestResponseFormat],
                    direction="write",
                ),
                "timezone": timezone,
                "max_files_open": max_files_open,
                "per_file_view_window_char_limit": per_file_view_window_char_limit,
                "hidden": hidden,
                "parallel_tool_calls": parallel_tool_calls,
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
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    async def count_agents(
        self,
        *,
        name: typing.Optional[str] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        match_all_tags: typing.Optional[bool] = None,
        query_text: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        base_template_id: typing.Optional[str] = None,
        identity_id: typing.Optional[str] = None,
        identifier_keys: typing.Optional[typing.Sequence[str]] = None,
        last_stop_reason: typing.Optional[StopReasonType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Get the total number of agents with optional filtering.
        Supports the same filters as list_agents for consistent querying.

        Parameters
        ----------
        name : typing.Optional[str]
            Name of the agent

        tags : typing.Optional[typing.Sequence[str]]
            List of tags to filter agents by

        match_all_tags : typing.Optional[bool]
            If True, only counts agents that match ALL given tags. Otherwise, counts agents that have ANY of the passed-in tags.

        query_text : typing.Optional[str]
            Search agents by name

        project_id : typing.Optional[str]
            Search agents by project ID - this will default to your default project on cloud

        template_id : typing.Optional[str]
            Search agents by template ID

        base_template_id : typing.Optional[str]
            Search agents by base template ID

        identity_id : typing.Optional[str]
            Search agents by identity ID

        identifier_keys : typing.Optional[typing.Sequence[str]]
            Search agents by identifier keys

        last_stop_reason : typing.Optional[StopReasonType]
            Filter agents by their last stop reason.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/count",
            method="GET",
            params={
                "name": name,
                "tags": tags,
                "match_all_tags": match_all_tags,
                "query_text": query_text,
                "project_id": project_id,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "identity_id": identity_id,
                "identifier_keys": identifier_keys,
                "last_stop_reason": last_stop_reason,
            },
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

    async def export_agent(
        self,
        agent_id: str,
        *,
        max_steps: typing.Optional[int] = None,
        use_legacy_format: typing.Optional[bool] = None,
        conversation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Export the serialized JSON representation of an agent, formatted with indentation.

        Parameters
        ----------
        agent_id : str

        max_steps : typing.Optional[int]

        use_legacy_format : typing.Optional[bool]
            If True, exports using the legacy single-agent 'v1' format with inline tools/blocks. If False, exports using the new multi-entity 'v2' format, with separate agents, tools, blocks, files, etc.

        conversation_id : typing.Optional[str]
            Conversation ID to export. If provided, uses messages from this conversation instead of the agent's global message history.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/export",
            method="GET",
            params={
                "max_steps": max_steps,
                "use_legacy_format": use_legacy_format,
                "conversation_id": conversation_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def import_agent(
        self,
        *,
        file: core.File,
        override_embedding_model: typing.Optional[str] = None,
        override_existing_tools: typing.Optional[bool] = OMIT,
        strip_messages: typing.Optional[bool] = OMIT,
        secrets: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        append_copy_suffix: typing.Optional[bool] = OMIT,
        override_name: typing.Optional[str] = OMIT,
        override_embedding_handle: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        env_vars_json: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImportedAgentsResponse]:
        """
        Import a serialized agent file and recreate the agent(s) in the system.
        Returns the IDs of all imported agents.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        override_embedding_model : typing.Optional[str]

        override_existing_tools : typing.Optional[bool]
            If set to True, existing tools can get their source code overwritten by the uploaded tool definitions. Note that Letta core tools can never be updated externally.

        strip_messages : typing.Optional[bool]
            If set to True, strips all messages from the agent before importing.

        secrets : typing.Optional[str]
            Secrets as a JSON string to pass to the agent for tool execution.

        name : typing.Optional[str]
            If provided, overrides the agent name with this value.

        embedding : typing.Optional[str]
            Embedding handle to override with.

        append_copy_suffix : typing.Optional[bool]
            If set to True, appends "_copy" to the end of the agent name.

        override_name : typing.Optional[str]
            If provided, overrides the agent name with this value. Use 'name' instead.

        override_embedding_handle : typing.Optional[str]
            Override import with specific embedding handle. Use 'embedding' instead.

        project_id : typing.Optional[str]
            The project ID to associate the uploaded agent with. This is now passed via headers.

        env_vars_json : typing.Optional[str]
            Environment variables as a JSON string to pass to the agent for tool execution. Use 'secrets' instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportedAgentsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/import",
            method="POST",
            data={
                "override_existing_tools": override_existing_tools,
                "strip_messages": strip_messages,
                "secrets": secrets,
                "name": name,
                "embedding": embedding,
                "append_copy_suffix": append_copy_suffix,
                "override_name": override_name,
                "override_embedding_handle": override_embedding_handle,
                "project_id": project_id,
                "env_vars_json": env_vars_json,
            },
            files={
                "file": file,
            },
            headers={
                "x-override-embedding-model": str(override_embedding_model)
                if override_embedding_model is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportedAgentsResponse,
                    parse_obj_as(
                        type_=ImportedAgentsResponse,
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

    async def retrieve_agent_context_window(
        self,
        agent_id: str,
        *,
        conversation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContextWindowOverview]:
        """
        Retrieve the context window of a specific agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        conversation_id : typing.Optional[str]
            Conversation ID to get context window for. If provided, uses messages from this conversation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextWindowOverview]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/context",
            method="GET",
            params={
                "conversation_id": conversation_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextWindowOverview,
                    parse_obj_as(
                        type_=ContextWindowOverview,
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

    async def retrieve_agent(
        self,
        agent_id: str,
        *,
        include_relationships: typing.Optional[typing.Sequence[str]] = None,
        include: typing.Optional[
            typing.Union[RetrieveAgentRequestIncludeItem, typing.Sequence[RetrieveAgentRequestIncludeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentState]:
        """
        Get the state of the agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        include_relationships : typing.Optional[typing.Sequence[str]]
            Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.

        include : typing.Optional[typing.Union[RetrieveAgentRequestIncludeItem, typing.Sequence[RetrieveAgentRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}",
            method="GET",
            params={
                "include_relationships": include_relationships,
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    async def delete_agent(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}",
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

    async def modify_agent(
        self,
        agent_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        tool_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        system: typing.Optional[str] = OMIT,
        tool_rules: typing.Optional[typing.Sequence[UpdateAgentToolRulesItem]] = OMIT,
        message_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tool_exec_environment_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        identity_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        message_buffer_autoclear: typing.Optional[bool] = OMIT,
        model: typing.Optional[str] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        model_settings: typing.Optional[UpdateAgentModelSettings] = OMIT,
        compaction_settings: typing.Optional[CompactionSettingsInput] = OMIT,
        context_window_limit: typing.Optional[int] = OMIT,
        reasoning: typing.Optional[bool] = OMIT,
        llm_config: typing.Optional[LlmConfig] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        response_format: typing.Optional[UpdateAgentResponseFormat] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        enable_sleeptime: typing.Optional[bool] = OMIT,
        last_run_completion: typing.Optional[dt.datetime] = OMIT,
        last_run_duration_ms: typing.Optional[int] = OMIT,
        last_stop_reason: typing.Optional[StopReasonType] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        max_files_open: typing.Optional[int] = OMIT,
        per_file_view_window_char_limit: typing.Optional[int] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentState]:
        """
        Update an existing agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        name : typing.Optional[str]
            The name of the agent.

        tool_ids : typing.Optional[typing.Sequence[str]]
            The ids of the tools used by the agent.

        source_ids : typing.Optional[typing.Sequence[str]]
            Deprecated: Use `folder_ids` field instead. The ids of the sources used by the agent.

        folder_ids : typing.Optional[typing.Sequence[str]]
            The ids of the folders used by the agent.

        block_ids : typing.Optional[typing.Sequence[str]]
            The ids of the blocks used by the agent.

        tags : typing.Optional[typing.Sequence[str]]
            The tags associated with the agent.

        system : typing.Optional[str]
            The system prompt used by the agent.

        tool_rules : typing.Optional[typing.Sequence[UpdateAgentToolRulesItem]]
            The tool rules governing the agent.

        message_ids : typing.Optional[typing.Sequence[str]]
            The ids of the messages in the agent's in-context memory.

        description : typing.Optional[str]
            The description of the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            The metadata of the agent.

        tool_exec_environment_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: use `secrets` field instead

        secrets : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The environment variables for tool execution specific to this agent.

        project_id : typing.Optional[str]
            The id of the project the agent belongs to.

        template_id : typing.Optional[str]
            The id of the template the agent belongs to.

        base_template_id : typing.Optional[str]
            The base template id of the agent.

        identity_ids : typing.Optional[typing.Sequence[str]]
            The ids of the identities associated with this agent.

        message_buffer_autoclear : typing.Optional[bool]
            If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.

        model : typing.Optional[str]
            The model handle used by the agent (format: provider/model-name).

        embedding : typing.Optional[str]
            The embedding model handle used by the agent (format: provider/model-name).

        model_settings : typing.Optional[UpdateAgentModelSettings]
            The model settings for the agent.

        compaction_settings : typing.Optional[CompactionSettingsInput]
            The compaction settings configuration used for compaction.

        context_window_limit : typing.Optional[int]
            The context window limit used by the agent.

        reasoning : typing.Optional[bool]
            Deprecated: Use `model` field to configure reasoning instead. Whether to enable reasoning for this agent.

        llm_config : typing.Optional[LlmConfig]
            Deprecated: Use `model` field instead. The LLM configuration used by the agent.

        embedding_config : typing.Optional[EmbeddingConfig]
            The embedding configuration used by the agent.

        parallel_tool_calls : typing.Optional[bool]
            Deprecated: Use `model_settings` to configure parallel tool calls instead. If set to True, enables parallel tool calling.

        response_format : typing.Optional[UpdateAgentResponseFormat]
            Deprecated: Use `model_settings` field to configure response format instead. The response format for the agent.

        max_tokens : typing.Optional[int]
            Deprecated: Use `model` field to configure max output tokens instead. The maximum number of tokens to generate, including reasoning step.

        enable_sleeptime : typing.Optional[bool]
            If set to True, memory management will move to a background agent thread.

        last_run_completion : typing.Optional[dt.datetime]
            The timestamp when the agent last completed a run.

        last_run_duration_ms : typing.Optional[int]
            The duration in milliseconds of the agent's last run.

        last_stop_reason : typing.Optional[StopReasonType]
            The stop reason from the agent's last run.

        timezone : typing.Optional[str]
            The timezone of the agent (IANA format).

        max_files_open : typing.Optional[int]
            Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.

        per_file_view_window_char_limit : typing.Optional[int]
            The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.

        hidden : typing.Optional[bool]
            If set to True, the agent will be hidden.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}",
            method="PATCH",
            json={
                "name": name,
                "tool_ids": tool_ids,
                "source_ids": source_ids,
                "folder_ids": folder_ids,
                "block_ids": block_ids,
                "tags": tags,
                "system": system,
                "tool_rules": convert_and_respect_annotation_metadata(
                    object_=tool_rules,
                    annotation=typing.Optional[typing.Sequence[UpdateAgentToolRulesItem]],
                    direction="write",
                ),
                "message_ids": message_ids,
                "description": description,
                "metadata": metadata,
                "tool_exec_environment_variables": tool_exec_environment_variables,
                "secrets": secrets,
                "project_id": project_id,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "identity_ids": identity_ids,
                "message_buffer_autoclear": message_buffer_autoclear,
                "model": model,
                "embedding": embedding,
                "model_settings": convert_and_respect_annotation_metadata(
                    object_=model_settings, annotation=typing.Optional[UpdateAgentModelSettings], direction="write"
                ),
                "compaction_settings": convert_and_respect_annotation_metadata(
                    object_=compaction_settings, annotation=typing.Optional[CompactionSettingsInput], direction="write"
                ),
                "context_window_limit": context_window_limit,
                "reasoning": reasoning,
                "llm_config": convert_and_respect_annotation_metadata(
                    object_=llm_config, annotation=typing.Optional[LlmConfig], direction="write"
                ),
                "embedding_config": convert_and_respect_annotation_metadata(
                    object_=embedding_config, annotation=typing.Optional[EmbeddingConfig], direction="write"
                ),
                "parallel_tool_calls": parallel_tool_calls,
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format, annotation=typing.Optional[UpdateAgentResponseFormat], direction="write"
                ),
                "max_tokens": max_tokens,
                "enable_sleeptime": enable_sleeptime,
                "last_run_completion": last_run_completion,
                "last_run_duration_ms": last_run_duration_ms,
                "last_stop_reason": last_stop_reason,
                "timezone": timezone,
                "max_files_open": max_files_open,
                "per_file_view_window_char_limit": per_file_view_window_char_limit,
                "hidden": hidden,
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
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    async def list_tools_for_agent(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListToolsForAgentRequestOrder] = None,
        order_by: typing.Optional[ListToolsForAgentRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Tool]]:
        """
        Get tools from an existing agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Tool ID cursor for pagination. Returns tools that come before this tool ID in the specified sort order

        after : typing.Optional[str]
            Tool ID cursor for pagination. Returns tools that come after this tool ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of tools to return

        order : typing.Optional[ListToolsForAgentRequestOrder]
            Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListToolsForAgentRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Tool]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Tool],
                    parse_obj_as(
                        type_=typing.List[Tool],
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

    async def attach_tool_to_agent(
        self, agent_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AgentState]]:
        """
        Attach a tool to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools/attach/{encode_path_param(tool_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    async def detach_tool_from_agent(
        self, agent_id: str, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AgentState]]:
        """
        Detach a tool from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools/detach/{encode_path_param(tool_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    async def modify_approval_for_tool(
        self,
        agent_id: str,
        tool_name: str,
        *,
        requires_approval: typing.Optional[bool] = None,
        request: typing.Optional[ModifyApprovalRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[AgentState]]:
        """
        Modify the approval requirement for a tool attached to an agent.

        Accepts requires_approval via request body (preferred) or query parameter (deprecated).

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        tool_name : str

        requires_approval : typing.Optional[bool]
            Whether the tool requires approval before execution

        request : typing.Optional[ModifyApprovalRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools/approval/{encode_path_param(tool_name)}",
            method="PATCH",
            params={
                "requires_approval": requires_approval,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[ModifyApprovalRequest], direction="write"
            ),
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
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    async def run_tool_for_agent(
        self,
        agent_id: str,
        tool_name: str,
        *,
        args: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ToolExecutionResult]:
        """
        Trigger a tool by name on a specific agent, providing the necessary arguments.

        This endpoint executes a tool that is attached to the agent, using the agent's
        state and environment variables for execution context.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        tool_name : str

        args : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the tool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToolExecutionResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/tools/{encode_path_param(tool_name)}/run",
            method="POST",
            json={
                "args": args,
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
                    ToolExecutionResult,
                    parse_obj_as(
                        type_=ToolExecutionResult,
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

    async def attach_source_to_agent(
        self, agent_id: str, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgentState]:
        """
        Attach a source to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/sources/attach/{encode_path_param(source_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    async def attach_folder_to_agent(
        self, agent_id: str, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AgentState]]:
        """
        Attach a folder to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/folders/attach/{encode_path_param(folder_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    async def detach_source_from_agent(
        self, agent_id: str, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgentState]:
        """
        Detach a source from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/sources/detach/{encode_path_param(source_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    async def detach_folder_from_agent(
        self, agent_id: str, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AgentState]]:
        """
        Detach a folder from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/folders/detach/{encode_path_param(folder_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    async def close_all_files_for_agent(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Closes all currently open files for a given agent.

        This endpoint updates the file state for the agent so that no files are marked as open.
        Typically used to reset the working memory view for the agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/files/close-all",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def open_file_for_agent(
        self, agent_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Opens a specific file for a given agent.

        This endpoint marks a specific file as open in the agent's file state.
        The file will be included in the agent's working memory view.
        Returns a list of file names that were closed due to LRU eviction.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/files/{encode_path_param(file_id)}/open",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def close_file_for_agent(
        self, agent_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Closes a specific file for a given agent.

        This endpoint marks a specific file as closed in the agent's file state.
        The file will be removed from the agent's working memory view.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/files/{encode_path_param(file_id)}/close",
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

    async def list_agent_sources(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentSourcesRequestOrder] = None,
        order_by: typing.Optional[ListAgentSourcesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Source]]:
        """
        Get the sources associated with an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Source ID cursor for pagination. Returns sources that come before this source ID in the specified sort order

        after : typing.Optional[str]
            Source ID cursor for pagination. Returns sources that come after this source ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of sources to return

        order : typing.Optional[ListAgentSourcesRequestOrder]
            Sort order for sources by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentSourcesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Source]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/sources",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Source],
                    parse_obj_as(
                        type_=typing.List[Source],
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

    async def list_folders_for_agent(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFoldersForAgentRequestOrder] = None,
        order_by: typing.Optional[ListFoldersForAgentRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Source]]:
        """
        Get the folders associated with an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Source ID cursor for pagination. Returns sources that come before this source ID in the specified sort order

        after : typing.Optional[str]
            Source ID cursor for pagination. Returns sources that come after this source ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of sources to return

        order : typing.Optional[ListFoldersForAgentRequestOrder]
            Sort order for sources by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFoldersForAgentRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Source]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/folders",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Source],
                    parse_obj_as(
                        type_=typing.List[Source],
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

    async def list_files_for_agent(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFilesForAgentRequestOrder] = None,
        order_by: typing.Optional[ListFilesForAgentRequestOrderBy] = None,
        cursor: typing.Optional[str] = None,
        is_open: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedAgentFiles]:
        """
        Get the files attached to an agent with their open/closed status.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            File ID cursor for pagination. Returns files that come before this file ID in the specified sort order

        after : typing.Optional[str]
            File ID cursor for pagination. Returns files that come after this file ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of files to return

        order : typing.Optional[ListFilesForAgentRequestOrder]
            Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFilesForAgentRequestOrderBy]
            Field to sort by

        cursor : typing.Optional[str]
            Pagination cursor from previous response (deprecated, use before/after)

        is_open : typing.Optional[bool]
            Filter by open status (true for open files, false for closed files)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedAgentFiles]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/files",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "cursor": cursor,
                "is_open": is_open,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedAgentFiles,
                    parse_obj_as(
                        type_=PaginatedAgentFiles,
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

    async def retrieve_agent_memory(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Memory]:
        """
        Retrieve the memory state of a specific agent.
        This endpoint fetches the current memory state of the agent identified by the user ID and agent ID.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Memory]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Memory,
                    parse_obj_as(
                        type_=Memory,
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

    async def retrieve_core_memory_block(
        self, agent_id: str, block_label: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BlockResponse]:
        """
        Retrieve a core memory block from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BlockResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks/{encode_path_param(block_label)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
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

    async def modify_core_memory_block(
        self,
        agent_id: str,
        block_label: str,
        *,
        value: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BlockResponse]:
        """
        Updates a core memory block of an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_label : str

        value : typing.Optional[str]
            Value of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]
            Whether the block is a template (e.g. saved human/persona options).

        template_id : typing.Optional[str]
            The id of the template.

        base_template_id : typing.Optional[str]
            The base template id of the block.

        deployment_id : typing.Optional[str]
            The id of the deployment.

        entity_id : typing.Optional[str]
            The id of the entity within the template.

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

        label : typing.Optional[str]
            Label of the block (e.g. 'human', 'persona') in the context window.

        read_only : typing.Optional[bool]
            Whether the agent has read-only access to the block.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the block.

        hidden : typing.Optional[bool]
            If set to True, the block will be hidden.

        tags : typing.Optional[typing.Sequence[str]]
            The tags to associate with the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BlockResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks/{encode_path_param(block_label)}",
            method="PATCH",
            json={
                "value": value,
                "limit": limit,
                "project_id": project_id,
                "template_name": template_name,
                "is_template": is_template,
                "template_id": template_id,
                "base_template_id": base_template_id,
                "deployment_id": deployment_id,
                "entity_id": entity_id,
                "preserve_on_migration": preserve_on_migration,
                "label": label,
                "read_only": read_only,
                "description": description,
                "metadata": metadata,
                "hidden": hidden,
                "tags": tags,
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
                    BlockResponse,
                    parse_obj_as(
                        type_=BlockResponse,
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

    async def list_core_memory_blocks(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListCoreMemoryBlocksRequestOrder] = None,
        order_by: typing.Optional[ListCoreMemoryBlocksRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[BlockResponse]]:
        """
        Retrieve the core memory blocks of a specific agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of blocks to return

        order : typing.Optional[ListCoreMemoryBlocksRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListCoreMemoryBlocksRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[BlockResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BlockResponse],
                    parse_obj_as(
                        type_=typing.List[BlockResponse],
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

    async def attach_core_memory_block(
        self, agent_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgentState]:
        """
        Attach a core memory block to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks/attach/{encode_path_param(block_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    async def detach_core_memory_block(
        self, agent_id: str, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgentState]:
        """
        Detach a core memory block from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/blocks/detach/{encode_path_param(block_id)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentState,
                    parse_obj_as(
                        type_=AgentState,
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

    async def attach_archive_to_agent(
        self, agent_id: str, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Attach an archive to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        archive_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archives/attach/{encode_path_param(archive_id)}",
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

    async def detach_archive_from_agent(
        self, agent_id: str, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Detach an archive from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        archive_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archives/detach/{encode_path_param(archive_id)}",
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

    async def attach_identity_to_agent(
        self, agent_id: str, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Attach an identity to an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/identities/attach/{encode_path_param(identity_id)}",
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

    async def detach_identity_from_agent(
        self, agent_id: str, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Detach an identity from an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/identities/detach/{encode_path_param(identity_id)}",
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

    async def list_passages(
        self,
        agent_id: str,
        *,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Passage]]:
        """
        Retrieve the memories in an agent's archival memory store (paginated query).

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        after : typing.Optional[str]
            Unique ID of the memory to start the query range at.

        before : typing.Optional[str]
            Unique ID of the memory to end the query range at.

        limit : typing.Optional[int]
            How many results to include in the response.

        search : typing.Optional[str]
            Search passages by text

        ascending : typing.Optional[bool]
            Whether to sort passages oldest to newest (True, default) or newest to oldest (False)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Passage]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archival-memory",
            method="GET",
            params={
                "after": after,
                "before": before,
                "limit": limit,
                "search": search,
                "ascending": ascending,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],
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

    async def create_passage(
        self,
        agent_id: str,
        *,
        text: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Passage]]:
        """
        Insert a memory into an agent's archival memory store.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        text : str
            Text to write to archival memory.

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of tags to attach to the memory.

        created_at : typing.Optional[dt.datetime]
            Optional timestamp for the memory (defaults to current UTC time).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Passage]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archival-memory",
            method="POST",
            json={
                "text": text,
                "tags": tags,
                "created_at": created_at,
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
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],
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

    async def search_archival_memory(
        self,
        agent_id: str,
        *,
        query: str,
        tags: typing.Optional[typing.Sequence[str]] = None,
        tag_match_mode: typing.Optional[SearchArchivalMemoryRequestTagMatchMode] = None,
        top_k: typing.Optional[int] = None,
        start_datetime: typing.Optional[dt.datetime] = None,
        end_datetime: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ArchivalMemorySearchResponse]:
        """
        Search archival memory using semantic (embedding-based) search with optional temporal filtering.

        This endpoint allows manual triggering of archival memory searches, enabling users to query
        an agent's archival memory store directly via the API. The search uses the same functionality
        as the agent's archival_memory_search tool but is accessible for external API usage.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        query : str
            String to search for using semantic similarity

        tags : typing.Optional[typing.Sequence[str]]
            Optional list of tags to filter search results

        tag_match_mode : typing.Optional[SearchArchivalMemoryRequestTagMatchMode]
            How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags

        top_k : typing.Optional[int]
            Maximum number of results to return. Uses system default if not specified

        start_datetime : typing.Optional[dt.datetime]
            Filter results to passages created after this datetime

        end_datetime : typing.Optional[dt.datetime]
            Filter results to passages created before this datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArchivalMemorySearchResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archival-memory/search",
            method="GET",
            params={
                "query": query,
                "tags": tags,
                "tag_match_mode": tag_match_mode,
                "top_k": top_k,
                "start_datetime": serialize_datetime(start_datetime) if start_datetime is not None else None,
                "end_datetime": serialize_datetime(end_datetime) if end_datetime is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArchivalMemorySearchResponse,
                    parse_obj_as(
                        type_=ArchivalMemorySearchResponse,
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

    async def delete_passage(
        self, agent_id: str, memory_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a memory from an agent's archival memory store.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        memory_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/archival-memory/{encode_path_param(memory_id)}",
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

    async def list_messages(
        self,
        agent_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesRequestOrder] = None,
        order_by: typing.Optional[ListMessagesRequestOrderBy] = None,
        group_id: typing.Optional[str] = None,
        conversation_id: typing.Optional[str] = None,
        use_assistant_message: typing.Optional[bool] = None,
        assistant_message_tool_name: typing.Optional[str] = None,
        assistant_message_tool_kwarg: typing.Optional[str] = None,
        include_err: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[LettaMessageUnion]]:
        """
        Retrieve message history for an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesRequestOrderBy]
            Field to sort by

        group_id : typing.Optional[str]
            Group ID to filter messages by.

        conversation_id : typing.Optional[str]
            Conversation ID to filter messages by.

        use_assistant_message : typing.Optional[bool]
            Whether to use assistant messages

        assistant_message_tool_name : typing.Optional[str]
            The name of the designated message tool.

        assistant_message_tool_kwarg : typing.Optional[str]
            The name of the message argument.

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
            f"v1/agents/{encode_path_param(agent_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "group_id": group_id,
                "conversation_id": conversation_id,
                "use_assistant_message": use_assistant_message,
                "assistant_message_tool_name": assistant_message_tool_name,
                "assistant_message_tool_kwarg": assistant_message_tool_kwarg,
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

    async def send_message(
        self,
        agent_id: str,
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
    ) -> AsyncHttpResponse[LettaResponse]:
        """
        Process a user message and return the agent's response.
        This endpoint accepts a message from a user and processes it through the agent.

        The response format is controlled by the `streaming` field in the request body:
        - If `streaming=false` (default): Returns a complete LettaResponse with all messages
        - If `streaming=true`: Returns a Server-Sent Events (SSE) stream

        Additional streaming options (only used when streaming=true):
        - `stream_tokens`: Stream individual tokens instead of complete steps
        - `include_pings`: Include keepalive pings to prevent connection timeouts
        - `background`: Process the request in the background

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

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
        AsyncHttpResponse[LettaResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages",
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

    async def modify_message(
        self,
        agent_id: str,
        message_id: str,
        *,
        request: ModifyMessageRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ModifyMessageResponse]:
        """
        Update the details of a message associated with an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        message_id : str
            The ID of the message in the format 'message-<uuid4>'

        request : ModifyMessageRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ModifyMessageResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages/{encode_path_param(message_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ModifyMessageRequestBody, direction="write"
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
                    ModifyMessageResponse,
                    parse_obj_as(
                        type_=ModifyMessageResponse,
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

    async def create_agent_message_stream(
        self,
        agent_id: str,
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
        Process a user message and return the agent's response.

        Deprecated: Use the `POST /{agent_id}/messages` endpoint with `streaming=true` in the request body instead.

        This endpoint accepts a message from a user and processes it through the agent.
        It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

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
            f"v1/agents/{encode_path_param(agent_id)}/messages/stream",
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

    async def cancel_message(
        self,
        agent_id: str,
        *,
        run_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Cancel runs associated with an agent. If run_ids are passed in, cancel those in particular.

        Note to cancel active runs associated with an agent, redis is required.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        run_ids : typing.Optional[typing.Sequence[str]]
            Optional list of run IDs to cancel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages/cancel",
            method="POST",
            json={
                "run_ids": run_ids,
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

    async def search_messages(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        search_mode: typing.Optional[MessageSearchRequestSearchMode] = OMIT,
        roles: typing.Optional[typing.Sequence[MessageRole]] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[MessageSearchResult]]:
        """
        Search messages across the entire organization with optional project and template filtering. Returns messages with FTS/vector ranks and total RRF score.

        This is a cloud-only feature.

        Parameters
        ----------
        query : typing.Optional[str]
            Text query for full-text search

        search_mode : typing.Optional[MessageSearchRequestSearchMode]
            Search mode to use

        roles : typing.Optional[typing.Sequence[MessageRole]]
            Filter messages by role

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        project_id : typing.Optional[str]
            Filter messages by project ID

        template_id : typing.Optional[str]
            Filter messages by template ID

        conversation_id : typing.Optional[str]
            Filter messages by conversation ID

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter messages created after this date

        end_date : typing.Optional[dt.datetime]
            Filter messages created on or before this date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[MessageSearchResult]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/messages/search",
            method="POST",
            json={
                "query": query,
                "search_mode": search_mode,
                "roles": roles,
                "agent_id": agent_id,
                "project_id": project_id,
                "template_id": template_id,
                "conversation_id": conversation_id,
                "limit": limit,
                "start_date": start_date,
                "end_date": end_date,
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
                    typing.List[MessageSearchResult],
                    parse_obj_as(
                        type_=typing.List[MessageSearchResult],
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

    async def create_agent_message_async(
        self,
        agent_id: str,
        *,
        messages: typing.Optional[typing.Sequence[LettaAsyncRequestMessagesItem]] = OMIT,
        input: typing.Optional[LettaAsyncRequestInput] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        use_assistant_message: typing.Optional[bool] = OMIT,
        assistant_message_tool_name: typing.Optional[str] = OMIT,
        assistant_message_tool_kwarg: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[typing.Sequence[MessageType]] = OMIT,
        enable_thinking: typing.Optional[str] = OMIT,
        client_tools: typing.Optional[typing.Sequence[ClientToolSchema]] = OMIT,
        override_model: typing.Optional[str] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Run]:
        """
        Asynchronously process a user message and return a run object.
        The actual processing happens in the background, and the status can be checked using the run ID.

        This is "asynchronous" in the sense that it's a background run and explicitly must be fetched by the run ID.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        messages : typing.Optional[typing.Sequence[LettaAsyncRequestMessagesItem]]
            The messages to be sent to the agent.

        input : typing.Optional[LettaAsyncRequestInput]
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

        callback_url : typing.Optional[str]
            Optional callback URL to POST to when the job completes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Run]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages/async",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Optional[typing.Sequence[LettaAsyncRequestMessagesItem]],
                    direction="write",
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[LettaAsyncRequestInput], direction="write"
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
                "callback_url": callback_url,
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
                    Run,
                    parse_obj_as(
                        type_=Run,
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

    async def reset_messages(
        self,
        agent_id: str,
        *,
        add_default_initial_messages: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[AgentState]]:
        """
        Resets the messages for an agent

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        add_default_initial_messages : typing.Optional[bool]
            If true, adds the default initial messages after resetting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/reset-messages",
            method="PATCH",
            json={
                "add_default_initial_messages": add_default_initial_messages,
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
                    typing.Optional[AgentState],
                    parse_obj_as(
                        type_=typing.Optional[AgentState],
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

    async def list_groups_for_agent(
        self,
        agent_id: str,
        *,
        manager_type: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListGroupsForAgentRequestOrder] = None,
        order_by: typing.Optional[ListGroupsForAgentRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Group]]:
        """
        Lists the groups for an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        manager_type : typing.Optional[str]
            Manager type to filter groups by

        before : typing.Optional[str]
            Group ID cursor for pagination. Returns groups that come before this group ID in the specified sort order

        after : typing.Optional[str]
            Group ID cursor for pagination. Returns groups that come after this group ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of groups to return

        order : typing.Optional[ListGroupsForAgentRequestOrder]
            Sort order for groups by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListGroupsForAgentRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Group]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/groups",
            method="GET",
            params={
                "manager_type": manager_type,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
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

    async def preview_model_request(
        self,
        agent_id: str,
        *,
        request: PreviewModelRequestRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Inspect the raw LLM request payload without sending it.

        This endpoint processes the message through the agent loop up until
        the LLM request, then returns the raw request payload that would
        be sent to the LLM provider. Useful for debugging and inspection.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request : PreviewModelRequestRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/messages/preview-raw-payload",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PreviewModelRequestRequestBody, direction="write"
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

    async def summarize_messages(
        self,
        agent_id: str,
        *,
        request: typing.Optional[CompactionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CompactionResponse]:
        """
        Summarize an agent's conversation history.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        request : typing.Optional[CompactionRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompactionResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/summarize",
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

    async def searchdeployedagents(
        self,
        *,
        search: typing.Optional[typing.Sequence[AgentsSearchDeployedAgentsRequestSearchItem]] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        combinator: typing.Optional[AgentsSearchDeployedAgentsRequestCombinator] = OMIT,
        limit: typing.Optional[float] = OMIT,
        after: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[AgentsSearchDeployedAgentsRequestSortBy] = OMIT,
        ascending: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentsSearchDeployedAgentsResponse]:
        """
        Search deployed agents

        Parameters
        ----------
        search : typing.Optional[typing.Sequence[AgentsSearchDeployedAgentsRequestSearchItem]]

        project_id : typing.Optional[str]

        combinator : typing.Optional[AgentsSearchDeployedAgentsRequestCombinator]

        limit : typing.Optional[float]

        after : typing.Optional[str]

        sort_by : typing.Optional[AgentsSearchDeployedAgentsRequestSortBy]

        ascending : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentsSearchDeployedAgentsResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/agents/search",
            method="POST",
            json={
                "search": convert_and_respect_annotation_metadata(
                    object_=search,
                    annotation=typing.Sequence[AgentsSearchDeployedAgentsRequestSearchItem],
                    direction="write",
                ),
                "project_id": project_id,
                "combinator": combinator,
                "limit": limit,
                "after": after,
                "sortBy": sort_by,
                "ascending": ascending,
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
                    AgentsSearchDeployedAgentsResponse,
                    parse_obj_as(
                        type_=AgentsSearchDeployedAgentsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getagentvariables(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgentsGetAgentVariablesResponse]:
        """
        Get the variables associated with an agent

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentsGetAgentVariablesResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/core-memory/variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentsGetAgentVariablesResponse,
                    parse_obj_as(
                        type_=AgentsGetAgentVariablesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

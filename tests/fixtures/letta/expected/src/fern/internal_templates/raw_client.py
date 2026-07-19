

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
from ..types.agent_state import AgentState
from ..types.agent_type import AgentType
from ..types.block import Block
from ..types.compaction_settings_input import CompactionSettingsInput
from ..types.create_block import CreateBlock
from ..types.delete_deployment_response import DeleteDeploymentResponse
from ..types.embedding_config import EmbeddingConfig
from ..types.group import Group
from ..types.http_validation_error import HttpValidationError
from ..types.internal_template_block_create import InternalTemplateBlockCreate
from ..types.list_deployment_entities_response import ListDeploymentEntitiesResponse
from ..types.llm_config import LlmConfig
from ..types.message_create import MessageCreate
from .types.internal_template_agent_create_model_settings import InternalTemplateAgentCreateModelSettings
from .types.internal_template_agent_create_response_format import InternalTemplateAgentCreateResponseFormat
from .types.internal_template_agent_create_tool_rules_item import InternalTemplateAgentCreateToolRulesItem
from .types.internal_template_group_create_manager_config import InternalTemplateGroupCreateManagerConfig
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInternalTemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_internal_template_group(
        self,
        *,
        agent_ids: typing.Sequence[str],
        description: str,
        base_template_id: str,
        template_id: str,
        deployment_id: str,
        manager_config: typing.Optional[InternalTemplateGroupCreateManagerConfig] = OMIT,
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


        base_template_id : str
            The id of the base template.

        template_id : str
            The id of the template.

        deployment_id : str
            The id of the deployment.

        manager_config : typing.Optional[InternalTemplateGroupCreateManagerConfig]


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
            "v1/_internal_templates/groups",
            method="POST",
            json={
                "agent_ids": agent_ids,
                "description": description,
                "manager_config": convert_and_respect_annotation_metadata(
                    object_=manager_config, annotation=InternalTemplateGroupCreateManagerConfig, direction="write"
                ),
                "project_id": project_id,
                "shared_block_ids": shared_block_ids,
                "hidden": hidden,
                "base_template_id": base_template_id,
                "template_id": template_id,
                "deployment_id": deployment_id,
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

    def create_internal_template_agent(
        self,
        *,
        template_id: str,
        base_template_id: str,
        deployment_id: str,
        entity_id: str,
        name: typing.Optional[str] = OMIT,
        memory_blocks: typing.Optional[typing.Sequence[CreateBlock]] = OMIT,
        tools: typing.Optional[typing.Sequence[str]] = OMIT,
        tool_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        tool_rules: typing.Optional[typing.Sequence[InternalTemplateAgentCreateToolRulesItem]] = OMIT,
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
        model_settings: typing.Optional[InternalTemplateAgentCreateModelSettings] = OMIT,
        compaction_settings: typing.Optional[CompactionSettingsInput] = OMIT,
        context_window_limit: typing.Optional[int] = OMIT,
        embedding_chunk_size: typing.Optional[int] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        max_reasoning_tokens: typing.Optional[int] = OMIT,
        enable_reasoner: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[bool] = OMIT,
        from_template: typing.Optional[str] = OMIT,
        template: typing.Optional[bool] = OMIT,
        project: typing.Optional[str] = OMIT,
        tool_exec_environment_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        memory_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        identity_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        message_buffer_autoclear: typing.Optional[bool] = OMIT,
        enable_sleeptime: typing.Optional[bool] = OMIT,
        response_format: typing.Optional[InternalTemplateAgentCreateResponseFormat] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        max_files_open: typing.Optional[int] = OMIT,
        per_file_view_window_char_limit: typing.Optional[int] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentState]:
        """
        Create a new agent with template-related fields.

        Parameters
        ----------
        template_id : str
            The id of the template.

        base_template_id : str
            The id of the base template.

        deployment_id : str
            The id of the deployment.

        entity_id : str
            The id of the entity within the template.

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

        tool_rules : typing.Optional[typing.Sequence[InternalTemplateAgentCreateToolRulesItem]]
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

        model_settings : typing.Optional[InternalTemplateAgentCreateModelSettings]
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

        project : typing.Optional[str]
            Deprecated: Project should now be passed via the X-Project header instead of in the request body. If using the SDK, this can be done via the x_project parameter.

        tool_exec_environment_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: Use `secrets` field instead. Environment variables for tool execution.

        secrets : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The environment variables for tool execution specific to this agent.

        memory_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: Only relevant for creating agents from a template. Use the 'create agents from a template' endpoint instead.

        project_id : typing.Optional[str]
            Deprecated: No longer used. The id of the project the agent belongs to.

        identity_ids : typing.Optional[typing.Sequence[str]]
            The ids of the identities associated with this agent.

        message_buffer_autoclear : typing.Optional[bool]
            If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.

        enable_sleeptime : typing.Optional[bool]
            If set to True, memory management will move to a background agent thread.

        response_format : typing.Optional[InternalTemplateAgentCreateResponseFormat]
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
            "v1/_internal_templates/agents",
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
                    annotation=typing.Optional[typing.Sequence[InternalTemplateAgentCreateToolRulesItem]],
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
                    annotation=typing.Optional[InternalTemplateAgentCreateModelSettings],
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
                "project": project,
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
                    annotation=typing.Optional[InternalTemplateAgentCreateResponseFormat],
                    direction="write",
                ),
                "timezone": timezone,
                "max_files_open": max_files_open,
                "per_file_view_window_char_limit": per_file_view_window_char_limit,
                "hidden": hidden,
                "parallel_tool_calls": parallel_tool_calls,
                "deployment_id": deployment_id,
                "entity_id": entity_id,
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

    def create_internal_template_block(
        self,
        *,
        value: str,
        template_id: str,
        base_template_id: str,
        deployment_id: str,
        entity_id: str,
        label: str,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Block]:
        """
        Create a new block with template-related fields.

        Parameters
        ----------
        value : str
            Value of the block.

        template_id : str
            The id of the template.

        base_template_id : str
            The id of the base template.

        deployment_id : str
            The id of the deployment.

        entity_id : str
            The id of the entity within the template.

        label : str
            Label of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

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
        HttpResponse[Block]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/_internal_templates/blocks",
            method="POST",
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
                    Block,
                    parse_obj_as(
                        type_=Block,
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

    def create_internal_template_blocks_batch(
        self,
        *,
        request: typing.Sequence[InternalTemplateBlockCreate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Block]]:
        """
        Create multiple blocks with template-related fields.

        Parameters
        ----------
        request : typing.Sequence[InternalTemplateBlockCreate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Block]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/_internal_templates/blocks/batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[InternalTemplateBlockCreate], direction="write"
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
                    typing.List[Block],
                    parse_obj_as(
                        type_=typing.List[Block],
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

    def list_deployment_entities(
        self,
        deployment_id: str,
        *,
        entity_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDeploymentEntitiesResponse]:
        """
        List all entities (blocks, agents, groups) with the specified deployment_id.
        Optionally filter by entity types.

        Parameters
        ----------
        deployment_id : str

        entity_types : typing.Optional[typing.Sequence[str]]
            Filter by entity types (block, agent, group)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDeploymentEntitiesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/_internal_templates/deployment/{encode_path_param(deployment_id)}",
            method="GET",
            params={
                "entity_types": entity_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDeploymentEntitiesResponse,
                    parse_obj_as(
                        type_=ListDeploymentEntitiesResponse,
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

    def delete_deployment(
        self, deployment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteDeploymentResponse]:
        """
        Delete all entities (blocks, agents, groups) with the specified deployment_id.
        Deletion order: blocks -> agents -> groups to maintain referential integrity.

        Parameters
        ----------
        deployment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDeploymentResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/_internal_templates/deployment/{encode_path_param(deployment_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDeploymentResponse,
                    parse_obj_as(
                        type_=DeleteDeploymentResponse,
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


class AsyncRawInternalTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_internal_template_group(
        self,
        *,
        agent_ids: typing.Sequence[str],
        description: str,
        base_template_id: str,
        template_id: str,
        deployment_id: str,
        manager_config: typing.Optional[InternalTemplateGroupCreateManagerConfig] = OMIT,
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


        base_template_id : str
            The id of the base template.

        template_id : str
            The id of the template.

        deployment_id : str
            The id of the deployment.

        manager_config : typing.Optional[InternalTemplateGroupCreateManagerConfig]


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
            "v1/_internal_templates/groups",
            method="POST",
            json={
                "agent_ids": agent_ids,
                "description": description,
                "manager_config": convert_and_respect_annotation_metadata(
                    object_=manager_config, annotation=InternalTemplateGroupCreateManagerConfig, direction="write"
                ),
                "project_id": project_id,
                "shared_block_ids": shared_block_ids,
                "hidden": hidden,
                "base_template_id": base_template_id,
                "template_id": template_id,
                "deployment_id": deployment_id,
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

    async def create_internal_template_agent(
        self,
        *,
        template_id: str,
        base_template_id: str,
        deployment_id: str,
        entity_id: str,
        name: typing.Optional[str] = OMIT,
        memory_blocks: typing.Optional[typing.Sequence[CreateBlock]] = OMIT,
        tools: typing.Optional[typing.Sequence[str]] = OMIT,
        tool_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        folder_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        tool_rules: typing.Optional[typing.Sequence[InternalTemplateAgentCreateToolRulesItem]] = OMIT,
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
        model_settings: typing.Optional[InternalTemplateAgentCreateModelSettings] = OMIT,
        compaction_settings: typing.Optional[CompactionSettingsInput] = OMIT,
        context_window_limit: typing.Optional[int] = OMIT,
        embedding_chunk_size: typing.Optional[int] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        max_reasoning_tokens: typing.Optional[int] = OMIT,
        enable_reasoner: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[bool] = OMIT,
        from_template: typing.Optional[str] = OMIT,
        template: typing.Optional[bool] = OMIT,
        project: typing.Optional[str] = OMIT,
        tool_exec_environment_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        memory_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        identity_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        message_buffer_autoclear: typing.Optional[bool] = OMIT,
        enable_sleeptime: typing.Optional[bool] = OMIT,
        response_format: typing.Optional[InternalTemplateAgentCreateResponseFormat] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        max_files_open: typing.Optional[int] = OMIT,
        per_file_view_window_char_limit: typing.Optional[int] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        parallel_tool_calls: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentState]:
        """
        Create a new agent with template-related fields.

        Parameters
        ----------
        template_id : str
            The id of the template.

        base_template_id : str
            The id of the base template.

        deployment_id : str
            The id of the deployment.

        entity_id : str
            The id of the entity within the template.

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

        tool_rules : typing.Optional[typing.Sequence[InternalTemplateAgentCreateToolRulesItem]]
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

        model_settings : typing.Optional[InternalTemplateAgentCreateModelSettings]
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

        project : typing.Optional[str]
            Deprecated: Project should now be passed via the X-Project header instead of in the request body. If using the SDK, this can be done via the x_project parameter.

        tool_exec_environment_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: Use `secrets` field instead. Environment variables for tool execution.

        secrets : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            The environment variables for tool execution specific to this agent.

        memory_variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]
            Deprecated: Only relevant for creating agents from a template. Use the 'create agents from a template' endpoint instead.

        project_id : typing.Optional[str]
            Deprecated: No longer used. The id of the project the agent belongs to.

        identity_ids : typing.Optional[typing.Sequence[str]]
            The ids of the identities associated with this agent.

        message_buffer_autoclear : typing.Optional[bool]
            If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.

        enable_sleeptime : typing.Optional[bool]
            If set to True, memory management will move to a background agent thread.

        response_format : typing.Optional[InternalTemplateAgentCreateResponseFormat]
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
            "v1/_internal_templates/agents",
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
                    annotation=typing.Optional[typing.Sequence[InternalTemplateAgentCreateToolRulesItem]],
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
                    annotation=typing.Optional[InternalTemplateAgentCreateModelSettings],
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
                "project": project,
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
                    annotation=typing.Optional[InternalTemplateAgentCreateResponseFormat],
                    direction="write",
                ),
                "timezone": timezone,
                "max_files_open": max_files_open,
                "per_file_view_window_char_limit": per_file_view_window_char_limit,
                "hidden": hidden,
                "parallel_tool_calls": parallel_tool_calls,
                "deployment_id": deployment_id,
                "entity_id": entity_id,
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

    async def create_internal_template_block(
        self,
        *,
        value: str,
        template_id: str,
        base_template_id: str,
        deployment_id: str,
        entity_id: str,
        label: str,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Block]:
        """
        Create a new block with template-related fields.

        Parameters
        ----------
        value : str
            Value of the block.

        template_id : str
            The id of the template.

        base_template_id : str
            The id of the base template.

        deployment_id : str
            The id of the deployment.

        entity_id : str
            The id of the entity within the template.

        label : str
            Label of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

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
        AsyncHttpResponse[Block]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/_internal_templates/blocks",
            method="POST",
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
                    Block,
                    parse_obj_as(
                        type_=Block,
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

    async def create_internal_template_blocks_batch(
        self,
        *,
        request: typing.Sequence[InternalTemplateBlockCreate],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Block]]:
        """
        Create multiple blocks with template-related fields.

        Parameters
        ----------
        request : typing.Sequence[InternalTemplateBlockCreate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Block]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/_internal_templates/blocks/batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[InternalTemplateBlockCreate], direction="write"
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
                    typing.List[Block],
                    parse_obj_as(
                        type_=typing.List[Block],
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

    async def list_deployment_entities(
        self,
        deployment_id: str,
        *,
        entity_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDeploymentEntitiesResponse]:
        """
        List all entities (blocks, agents, groups) with the specified deployment_id.
        Optionally filter by entity types.

        Parameters
        ----------
        deployment_id : str

        entity_types : typing.Optional[typing.Sequence[str]]
            Filter by entity types (block, agent, group)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDeploymentEntitiesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/_internal_templates/deployment/{encode_path_param(deployment_id)}",
            method="GET",
            params={
                "entity_types": entity_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDeploymentEntitiesResponse,
                    parse_obj_as(
                        type_=ListDeploymentEntitiesResponse,
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

    async def delete_deployment(
        self, deployment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteDeploymentResponse]:
        """
        Delete all entities (blocks, agents, groups) with the specified deployment_id.
        Deletion order: blocks -> agents -> groups to maintain referential integrity.

        Parameters
        ----------
        deployment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDeploymentResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/_internal_templates/deployment/{encode_path_param(deployment_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDeploymentResponse,
                    parse_obj_as(
                        type_=DeleteDeploymentResponse,
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

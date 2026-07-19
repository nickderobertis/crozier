

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_type import AgentType
from .compaction_settings_input import CompactionSettingsInput
from .create_block import CreateBlock
from .embedding_config import EmbeddingConfig
from .file_agent_schema import FileAgentSchema
from .letta_schemas_agent_file_agent_schema_model_settings import LettaSchemasAgentFileAgentSchemaModelSettings
from .letta_schemas_agent_file_agent_schema_response_format import LettaSchemasAgentFileAgentSchemaResponseFormat
from .letta_schemas_agent_file_agent_schema_tool_rules_item import LettaSchemasAgentFileAgentSchemaToolRulesItem
from .letta_schemas_agent_file_message_schema import LettaSchemasAgentFileMessageSchema
from .llm_config import LlmConfig
from .message_create import MessageCreate


class LettaSchemasAgentFileAgentSchema(UniversalBaseModel):
    """
    Agent with human-readable ID for agent file
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the agent.
    """

    memory_blocks: typing.Optional[typing.List[CreateBlock]] = pydantic.Field(default=None)
    """
    The blocks to create in the agent's in-context memory.
    """

    tools: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tools used by the agent.
    """

    tool_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The ids of the tools used by the agent.
    """

    source_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Deprecated: Use `folder_ids` field instead. The ids of the sources used by the agent.
    """

    folder_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The ids of the folders used by the agent.
    """

    block_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The ids of the blocks used by the agent.
    """

    tool_rules: typing.Optional[typing.List[LettaSchemasAgentFileAgentSchemaToolRulesItem]] = pydantic.Field(
        default=None
    )
    """
    The tool rules governing the agent.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tags associated with the agent.
    """

    system: typing.Optional[str] = pydantic.Field(default=None)
    """
    The system prompt used by the agent.
    """

    agent_type: typing.Optional[AgentType] = pydantic.Field(default=None)
    """
    The type of agent.
    """

    initial_message_sequence: typing.Optional[typing.List[MessageCreate]] = pydantic.Field(default=None)
    """
    The initial set of messages to put in the agent's in-context memory.
    """

    include_base_tools: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, attaches the Letta core tools (e.g. core_memory related functions).
    """

    include_multi_agent_tools: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, attaches the Letta multi-agent tools (e.g. sending a message to another agent).
    """

    include_base_tool_rules: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, attaches the Letta base tool rules (e.g. deny all tools not explicitly allowed).
    """

    include_default_source: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, automatically creates and attaches a default data source for this agent.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the agent.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The metadata of the agent.
    """

    llm_config: typing.Optional[LlmConfig] = pydantic.Field(default=None)
    """
    Deprecated: Use `model` field instead. The LLM configuration used by the agent.
    """

    embedding_config: typing.Optional[EmbeddingConfig] = pydantic.Field(default=None)
    """
    Deprecated: Use `embedding` field instead. The embedding configuration used by the agent.
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model handle for the agent to use (format: provider/model-name).
    """

    embedding: typing.Optional[str] = pydantic.Field(default=None)
    """
    The embedding model handle used by the agent (format: provider/model-name).
    """

    model_settings: typing.Optional[LettaSchemasAgentFileAgentSchemaModelSettings] = pydantic.Field(default=None)
    """
    The model settings for the agent.
    """

    compaction_settings: typing.Optional[CompactionSettingsInput] = pydantic.Field(default=None)
    """
    The compaction settings configuration used for compaction.
    """

    context_window_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The context window limit used by the agent.
    """

    embedding_chunk_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated: No longer used. The embedding chunk size used by the agent.
    """

    max_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated: Use `model` field to configure max output tokens instead. The maximum number of tokens to generate, including reasoning step.
    """

    max_reasoning_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated: Use `model` field to configure reasoning tokens instead. The maximum number of tokens to generate for reasoning step.
    """

    enable_reasoner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deprecated: Use `model` field to configure reasoning instead. Whether to enable internal extended thinking step for a reasoner model.
    """

    reasoning: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deprecated: Use `model` field to configure reasoning instead. Whether to enable reasoning for this agent.
    """

    from_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: please use the 'create agents from a template' endpoint instead.
    """

    template: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deprecated: No longer used.
    """

    project: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: Project should now be passed via the X-Project header instead of in the request body. If using the SDK, this can be done via the x_project parameter.
    """

    tool_exec_environment_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(
        default=None
    )
    """
    Deprecated: Use `secrets` field instead. Environment variables for tool execution.
    """

    secrets: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    The environment variables for tool execution specific to this agent.
    """

    memory_variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Deprecated: Only relevant for creating agents from a template. Use the 'create agents from a template' endpoint instead.
    """

    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: No longer used. The id of the project the agent belongs to.
    """

    template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: No longer used. The id of the template the agent belongs to.
    """

    base_template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: No longer used. The base template id of the agent.
    """

    identity_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The ids of the identities associated with this agent.
    """

    message_buffer_autoclear: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.
    """

    enable_sleeptime: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to True, memory management will move to a background agent thread.
    """

    response_format: typing.Optional[LettaSchemasAgentFileAgentSchemaResponseFormat] = pydantic.Field(default=None)
    """
    Deprecated: Use `model_settings` field to configure response format instead. The response format for the agent.
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timezone of the agent (IANA format).
    """

    max_files_open: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.
    """

    per_file_view_window_char_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.
    """

    hidden: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deprecated: No longer used. If set to True, the agent will be hidden.
    """

    parallel_tool_calls: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deprecated: Use `model_settings` to configure parallel tool calls instead. If set to True, enables parallel tool calling.
    """

    id: str = pydantic.Field()
    """
    Human-readable identifier for this agent in the file
    """

    in_context_message_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of message IDs that are currently in the agent's context
    """

    messages: typing.Optional[typing.List[LettaSchemasAgentFileMessageSchema]] = pydantic.Field(default=None)
    """
    List of messages in the agent's conversation history
    """

    files_agents: typing.Optional[typing.List[FileAgentSchema]] = pydantic.Field(default=None)
    """
    List of file-agent relationships for this agent
    """

    group_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of groups that the agent manages
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

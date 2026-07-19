

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_environment_variable import AgentEnvironmentVariable
from .agent_state_model_settings import AgentStateModelSettings
from .agent_state_response_format import AgentStateResponseFormat
from .agent_state_tool_rules_item import AgentStateToolRulesItem
from .agent_type import AgentType
from .approval_request_message import ApprovalRequestMessage
from .block import Block
from .compaction_settings_output import CompactionSettingsOutput
from .embedding_config import EmbeddingConfig
from .group import Group
from .identity import Identity
from .llm_config import LlmConfig
from .memory import Memory
from .source import Source
from .stop_reason_type import StopReasonType
from .tool import Tool


class AgentState(UniversalBaseModel):
    """
    Representation of an agent's state. This is the state of the agent at a given time, and is persisted in the DB backend. The state has all the information needed to recreate a persisted agent.
    """

    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was last updated.
    """

    id: str = pydantic.Field()
    """
    The id of the agent. Assigned by the database.
    """

    name: str = pydantic.Field()
    """
    The name of the agent.
    """

    tool_rules: typing.Optional[typing.List[AgentStateToolRulesItem]] = pydantic.Field(default=None)
    """
    The list of tool rules.
    """

    message_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The ids of the messages in the agent's in-context memory.
    """

    system: str = pydantic.Field()
    """
    The system prompt used by the agent.
    """

    agent_type: AgentType = pydantic.Field()
    """
    The type of agent.
    """

    llm_config: LlmConfig = pydantic.Field()
    """
    Deprecated: Use `model` field instead. The LLM configuration used by the agent.
    """

    embedding_config: typing.Optional[EmbeddingConfig] = pydantic.Field(default=None)
    """
    Deprecated: Use `embedding` field instead. The embedding configuration used by the agent.
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model handle used by the agent (format: provider/model-name).
    """

    embedding: typing.Optional[str] = pydantic.Field(default=None)
    """
    The embedding model handle used by the agent (format: provider/model-name).
    """

    model_settings: typing.Optional[AgentStateModelSettings] = pydantic.Field(default=None)
    """
    The model settings used by the agent.
    """

    compaction_settings: typing.Optional[CompactionSettingsOutput] = pydantic.Field(default=None)
    """
    The compaction settings configuration used for compaction.
    """

    response_format: typing.Optional[AgentStateResponseFormat] = pydantic.Field(default=None)
    """
    The response format used by the agent
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the agent.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The metadata of the agent.
    """

    memory: Memory = pydantic.Field()
    """
    Deprecated: Use `blocks` field instead. The in-context memory of the agent.
    """

    blocks: typing.List[Block] = pydantic.Field()
    """
    The memory blocks used by the agent.
    """

    tools: typing.List[Tool] = pydantic.Field()
    """
    The tools used by the agent.
    """

    sources: typing.List[Source] = pydantic.Field()
    """
    Deprecated: Use `folders` field instead. The sources used by the agent.
    """

    tags: typing.List[str] = pydantic.Field()
    """
    The tags associated with the agent.
    """

    tool_exec_environment_variables: typing.Optional[typing.List[AgentEnvironmentVariable]] = pydantic.Field(
        default=None
    )
    """
    Deprecated: use `secrets` field instead.
    """

    secrets: typing.Optional[typing.List[AgentEnvironmentVariable]] = pydantic.Field(default=None)
    """
    The environment variables for tool execution specific to this agent.
    """

    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the project the agent belongs to.
    """

    template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the template the agent belongs to.
    """

    base_template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The base template id of the agent.
    """

    deployment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the deployment.
    """

    entity_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the entity within the template.
    """

    identity_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Deprecated: Use `identities` field instead. The ids of the identities associated with this agent.
    """

    identities: typing.Optional[typing.List[Identity]] = pydantic.Field(default=None)
    """
    The identities associated with this agent.
    """

    pending_approval: typing.Optional[ApprovalRequestMessage] = pydantic.Field(default=None)
    """
    The latest approval request message pending for this agent, if any.
    """

    message_buffer_autoclear: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.
    """

    enable_sleeptime: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to True, memory management will move to a background agent thread.
    """

    multi_agent_group: typing.Optional[Group] = pydantic.Field(default=None)
    """
    Deprecated: Use `managed_group` field instead. The multi-agent group that this agent manages.
    """

    managed_group: typing.Optional[Group] = pydantic.Field(default=None)
    """
    The multi-agent group that this agent manages
    """

    last_run_completion: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the agent last completed a run.
    """

    last_run_duration_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    The duration in milliseconds of the agent's last run.
    """

    last_stop_reason: typing.Optional[StopReasonType] = pydantic.Field(default=None)
    """
    The stop reason from the agent's last run.
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
    If set to True, the agent will be hidden.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

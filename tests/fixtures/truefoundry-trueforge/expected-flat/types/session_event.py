

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_info import AgentInfo
from .agent_parent import AgentParent
from .finish_reason import FinishReason
from .mcp_server_auth_info import McpServerAuthInfo
from .mcp_server_init_info import McpServerInitInfo
from .model_message_event_content import ModelMessageEventContent
from .model_message_usage import ModelMessageUsage
from .thread_state import ThreadState
from .tool_call import ToolCall
from .tool_call_ref import ToolCallRef
from .turn_done_event_state import TurnDoneEventState
from .turn_input_item import TurnInputItem
from .turn_state_running import TurnStateRunning


class SessionEvent_McpAuthRequired(UniversalBaseModel):
    type: typing.Literal["mcp.auth_required"] = "mcp.auth_required"
    mcp_servers: typing.List[McpServerAuthInfo]
    created_at: str
    id: str
    thread_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_McpInitialize(UniversalBaseModel):
    type: typing.Literal["mcp.initialize"] = "mcp.initialize"
    created_at: str
    id: str
    mcp_servers: typing.List[McpServerInitInfo]
    thread_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_ModelMessage(UniversalBaseModel):
    type: typing.Literal["model.message"] = "model.message"
    content: typing.Optional[ModelMessageEventContent] = None
    created_at: str
    finish_reason: typing.Optional[FinishReason] = None
    id: str
    name: typing.Optional[str] = None
    reasoning_content: typing.Optional[str] = None
    refusal: typing.Optional[str] = None
    thread_id: str
    tool_calls: typing.Optional[typing.List[ToolCall]] = None
    usage: typing.Optional[ModelMessageUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_SandboxCreated(UniversalBaseModel):
    type: typing.Literal["sandbox.created"] = "sandbox.created"
    created_at: str
    id: str
    sandbox_id: str
    thread_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_ThreadCreated(UniversalBaseModel):
    type: typing.Literal["thread.created"] = "thread.created"
    agent_info: AgentInfo
    created_at: str
    id: str
    parent: AgentParent
    thread_id: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_ThreadDone(UniversalBaseModel):
    type: typing.Literal["thread.done"] = "thread.done"
    created_at: str
    id: str
    state: ThreadState
    parent: typing.Optional[AgentParent] = None
    thread_id: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_ToolApprovalRequired(UniversalBaseModel):
    type: typing.Literal["tool.approval_required"] = "tool.approval_required"
    created_at: str
    id: str
    thread_id: str
    tool_calls: typing.List[ToolCallRef]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_ToolResponse(UniversalBaseModel):
    type: typing.Literal["tool.response"] = "tool.response"
    content: str
    created_at: str
    id: str
    thread_id: str
    tool_call_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_ToolResponseRequired(UniversalBaseModel):
    type: typing.Literal["tool.response_required"] = "tool.response_required"
    created_at: str
    id: str
    thread_id: str
    tool_calls: typing.List[ToolCallRef]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_TurnCreated(UniversalBaseModel):
    type: typing.Literal["turn.created"] = "turn.created"
    created_at: str
    id: str
    input: typing.Optional[typing.List[TurnInputItem]] = None
    previous_turn_id: typing.Optional[str] = None
    state: TurnStateRunning
    thread_id: typing.Optional[str] = None
    turn_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionEvent_TurnDone(UniversalBaseModel):
    type: typing.Literal["turn.done"] = "turn.done"
    created_at: str
    id: str
    state: TurnDoneEventState
    thread_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SessionEvent = typing_extensions.Annotated[
    typing.Union[
        SessionEvent_McpAuthRequired,
        SessionEvent_McpInitialize,
        SessionEvent_ModelMessage,
        SessionEvent_SandboxCreated,
        SessionEvent_ThreadCreated,
        SessionEvent_ThreadDone,
        SessionEvent_ToolApprovalRequired,
        SessionEvent_ToolResponse,
        SessionEvent_ToolResponseRequired,
        SessionEvent_TurnCreated,
        SessionEvent_TurnDone,
    ],
    pydantic.Field(discriminator="type"),
]

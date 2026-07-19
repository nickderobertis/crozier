

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .approval_request_message_tool_call import ApprovalRequestMessageToolCall
from .approval_request_message_tool_calls import ApprovalRequestMessageToolCalls
from .approval_response_message_approvals_item import ApprovalResponseMessageApprovalsItem
from .assistant_message_content import AssistantMessageContent
from .event_message_event_type import EventMessageEventType
from .hidden_reasoning_message_state import HiddenReasoningMessageState
from .letta_schemas_letta_message_tool_return import LettaSchemasLettaMessageToolReturn
from .reasoning_message_source import ReasoningMessageSource
from .tool_call_message_tool_call import ToolCallMessageToolCall
from .tool_call_message_tool_calls import ToolCallMessageToolCalls
from .tool_return_message_status import ToolReturnMessageStatus
from .user_message_content import UserMessageContent


class LettaMessageUnion_SystemMessage(UniversalBaseModel):
    message_type: typing.Literal["system_message"] = "system_message"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    content: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_UserMessage(UniversalBaseModel):
    message_type: typing.Literal["user_message"] = "user_message"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    content: UserMessageContent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_ReasoningMessage(UniversalBaseModel):
    message_type: typing.Literal["reasoning_message"] = "reasoning_message"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    source: typing.Optional[ReasoningMessageSource] = None
    reasoning: str
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_HiddenReasoningMessage(UniversalBaseModel):
    message_type: typing.Literal["hidden_reasoning_message"] = "hidden_reasoning_message"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    state: HiddenReasoningMessageState
    hidden_reasoning: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_ToolCallMessage(UniversalBaseModel):
    message_type: typing.Literal["tool_call_message"] = "tool_call_message"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    tool_call: ToolCallMessageToolCall
    tool_calls: typing.Optional[ToolCallMessageToolCalls] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_ToolReturnMessage(UniversalBaseModel):
    message_type: typing.Literal["tool_return_message"] = "tool_return_message"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    tool_return: str
    status: ToolReturnMessageStatus
    tool_call_id: str
    stdout: typing.Optional[typing.List[str]] = None
    stderr: typing.Optional[typing.List[str]] = None
    tool_returns: typing.Optional[typing.List[LettaSchemasLettaMessageToolReturn]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_AssistantMessage(UniversalBaseModel):
    message_type: typing.Literal["assistant_message"] = "assistant_message"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    content: AssistantMessageContent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_ApprovalRequestMessage(UniversalBaseModel):
    message_type: typing.Literal["approval_request_message"] = "approval_request_message"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    tool_call: ApprovalRequestMessageToolCall
    tool_calls: typing.Optional[ApprovalRequestMessageToolCalls] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_ApprovalResponseMessage(UniversalBaseModel):
    message_type: typing.Literal["approval_response_message"] = "approval_response_message"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    approvals: typing.Optional[typing.List[ApprovalResponseMessageApprovalsItem]] = None
    approve: typing.Optional[bool] = None
    approval_request_id: typing.Optional[str] = None
    reason: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_Summary(UniversalBaseModel):
    message_type: typing.Literal["summary"] = "summary"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    summary: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageUnion_Event(UniversalBaseModel):
    message_type: typing.Literal["event"] = "event"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    event_type: EventMessageEventType
    event_data: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LettaMessageUnion = typing_extensions.Annotated[
    typing.Union[
        LettaMessageUnion_SystemMessage,
        LettaMessageUnion_UserMessage,
        LettaMessageUnion_ReasoningMessage,
        LettaMessageUnion_HiddenReasoningMessage,
        LettaMessageUnion_ToolCallMessage,
        LettaMessageUnion_ToolReturnMessage,
        LettaMessageUnion_AssistantMessage,
        LettaMessageUnion_ApprovalRequestMessage,
        LettaMessageUnion_ApprovalResponseMessage,
        LettaMessageUnion_Summary,
        LettaMessageUnion_Event,
    ],
    pydantic.Field(discriminator="message_type"),
]

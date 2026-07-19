

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
from .hidden_reasoning_message_state import HiddenReasoningMessageState
from .letta_schemas_letta_message_tool_return import LettaSchemasLettaMessageToolReturn
from .reasoning_message_source import ReasoningMessageSource
from .stop_reason_type import StopReasonType
from .tool_call_message_tool_call import ToolCallMessageToolCall
from .tool_call_message_tool_calls import ToolCallMessageToolCalls
from .tool_return_message_status import ToolReturnMessageStatus
from .user_message_content import UserMessageContent


class LettaStreamingResponse_ApprovalRequestMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

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


class LettaStreamingResponse_ApprovalResponseMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

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


class LettaStreamingResponse_AssistantMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

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


class LettaStreamingResponse_ErrorMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

    message_type: typing.Literal["error_message"] = "error_message"
    run_id: str
    error_type: str
    message: str
    detail: typing.Optional[str] = None
    seq_id: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaStreamingResponse_HiddenReasoningMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

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


class LettaStreamingResponse_Ping(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

    message_type: typing.Literal["ping"] = "ping"
    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaStreamingResponse_ReasoningMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

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


class LettaStreamingResponse_StopReason(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

    message_type: typing.Literal["stop_reason"] = "stop_reason"
    stop_reason: StopReasonType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaStreamingResponse_SystemMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

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


class LettaStreamingResponse_ToolCallMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

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


class LettaStreamingResponse_ToolReturnMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

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


class LettaStreamingResponse_UsageStatistics(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

    message_type: typing.Literal["usage_statistics"] = "usage_statistics"
    completion_tokens: typing.Optional[int] = None
    prompt_tokens: typing.Optional[int] = None
    total_tokens: typing.Optional[int] = None
    step_count: typing.Optional[int] = None
    run_ids: typing.Optional[typing.List[str]] = None
    cached_input_tokens: typing.Optional[int] = None
    cache_write_tokens: typing.Optional[int] = None
    reasoning_tokens: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaStreamingResponse_UserMessage(UniversalBaseModel):
    """
    Streaming response type for Server-Sent Events (SSE) endpoints.
    Each event in the stream will be one of these types.
    """

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


LettaStreamingResponse = typing_extensions.Annotated[
    typing.Union[
        LettaStreamingResponse_ApprovalRequestMessage,
        LettaStreamingResponse_ApprovalResponseMessage,
        LettaStreamingResponse_AssistantMessage,
        LettaStreamingResponse_ErrorMessage,
        LettaStreamingResponse_HiddenReasoningMessage,
        LettaStreamingResponse_Ping,
        LettaStreamingResponse_ReasoningMessage,
        LettaStreamingResponse_StopReason,
        LettaStreamingResponse_SystemMessage,
        LettaStreamingResponse_ToolCallMessage,
        LettaStreamingResponse_ToolReturnMessage,
        LettaStreamingResponse_UsageStatistics,
        LettaStreamingResponse_UserMessage,
    ],
    pydantic.Field(discriminator="message_type"),
]

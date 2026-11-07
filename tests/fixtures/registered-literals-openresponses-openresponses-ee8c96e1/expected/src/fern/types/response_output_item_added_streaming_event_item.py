

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_call_output_output import FunctionCallOutputOutput
from .function_call_output_status import FunctionCallOutputStatus
from .function_call_status import FunctionCallStatus
from .message_content_item import MessageContentItem
from .message_role import MessageRole
from .message_status import MessageStatus
from .reasoning_body_content_item import ReasoningBodyContentItem
from .reasoning_body_summary_item import ReasoningBodySummaryItem


class ResponseOutputItemAddedStreamingEventItem_Message(UniversalBaseModel):
    """
    An item representing a message, tool call, tool output, reasoning, or other response element.
    """

    type: typing.Literal["message"] = "message"
    id: str
    status: MessageStatus
    role: MessageRole
    content: typing.List[MessageContentItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseOutputItemAddedStreamingEventItem_FunctionCall(UniversalBaseModel):
    """
    An item representing a message, tool call, tool output, reasoning, or other response element.
    """

    type: typing.Literal["function_call"] = "function_call"
    id: str
    call_id: str
    name: str
    arguments: str
    status: FunctionCallStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseOutputItemAddedStreamingEventItem_FunctionCallOutput(UniversalBaseModel):
    """
    An item representing a message, tool call, tool output, reasoning, or other response element.
    """

    type: typing.Literal["function_call_output"] = "function_call_output"
    id: str
    call_id: str
    output: FunctionCallOutputOutput
    status: FunctionCallOutputStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseOutputItemAddedStreamingEventItem_Reasoning(UniversalBaseModel):
    """
    An item representing a message, tool call, tool output, reasoning, or other response element.
    """

    type: typing.Literal["reasoning"] = "reasoning"
    id: str
    content: typing.Optional[typing.List[ReasoningBodyContentItem]] = None
    summary: typing.List[ReasoningBodySummaryItem]
    encrypted_content: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ResponseOutputItemAddedStreamingEventItem = typing_extensions.Annotated[
    typing.Union[
        ResponseOutputItemAddedStreamingEventItem_Message,
        ResponseOutputItemAddedStreamingEventItem_FunctionCall,
        ResponseOutputItemAddedStreamingEventItem_FunctionCallOutput,
        ResponseOutputItemAddedStreamingEventItem_Reasoning,
    ],
    pydantic.Field(discriminator="type"),
]

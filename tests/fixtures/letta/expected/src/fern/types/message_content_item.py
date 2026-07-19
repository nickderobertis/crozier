

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_content_source import ImageContentSource
from .summarized_reasoning_content_part import SummarizedReasoningContentPart


class MessageContentItem_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    source: ImageContentSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageContentItem_OmittedReasoning(UniversalBaseModel):
    type: typing.Literal["omitted_reasoning"] = "omitted_reasoning"
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageContentItem_Reasoning(UniversalBaseModel):
    type: typing.Literal["reasoning"] = "reasoning"
    is_native: bool
    reasoning: str
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageContentItem_RedactedReasoning(UniversalBaseModel):
    type: typing.Literal["redacted_reasoning"] = "redacted_reasoning"
    data: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageContentItem_SummarizedReasoning(UniversalBaseModel):
    type: typing.Literal["summarized_reasoning"] = "summarized_reasoning"
    id: str
    summary: typing.List[SummarizedReasoningContentPart]
    encrypted_content: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageContentItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageContentItem_ToolCall(UniversalBaseModel):
    type: typing.Literal["tool_call"] = "tool_call"
    id: str
    name: str
    input: typing.Dict[str, typing.Any]
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageContentItem_ToolReturn(UniversalBaseModel):
    type: typing.Literal["tool_return"] = "tool_return"
    tool_call_id: str
    content: str
    is_error: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MessageContentItem = typing_extensions.Annotated[
    typing.Union[
        MessageContentItem_Image,
        MessageContentItem_OmittedReasoning,
        MessageContentItem_Reasoning,
        MessageContentItem_RedactedReasoning,
        MessageContentItem_SummarizedReasoning,
        MessageContentItem_Text,
        MessageContentItem_ToolCall,
        MessageContentItem_ToolReturn,
    ],
    pydantic.Field(discriminator="type"),
]

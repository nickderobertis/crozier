

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.image_content_source import ImageContentSource
from ...types.summarized_reasoning_content_part import SummarizedReasoningContentPart


class LettaAsyncRequestInputOneItem_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    source: ImageContentSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaAsyncRequestInputOneItem_OmittedReasoning(UniversalBaseModel):
    type: typing.Literal["omitted_reasoning"] = "omitted_reasoning"
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaAsyncRequestInputOneItem_Reasoning(UniversalBaseModel):
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


class LettaAsyncRequestInputOneItem_RedactedReasoning(UniversalBaseModel):
    type: typing.Literal["redacted_reasoning"] = "redacted_reasoning"
    data: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaAsyncRequestInputOneItem_SummarizedReasoning(UniversalBaseModel):
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


class LettaAsyncRequestInputOneItem_Text(UniversalBaseModel):
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


class LettaAsyncRequestInputOneItem_ToolCall(UniversalBaseModel):
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


class LettaAsyncRequestInputOneItem_ToolReturn(UniversalBaseModel):
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


LettaAsyncRequestInputOneItem = typing_extensions.Annotated[
    typing.Union[
        LettaAsyncRequestInputOneItem_Image,
        LettaAsyncRequestInputOneItem_OmittedReasoning,
        LettaAsyncRequestInputOneItem_Reasoning,
        LettaAsyncRequestInputOneItem_RedactedReasoning,
        LettaAsyncRequestInputOneItem_SummarizedReasoning,
        LettaAsyncRequestInputOneItem_Text,
        LettaAsyncRequestInputOneItem_ToolCall,
        LettaAsyncRequestInputOneItem_ToolReturn,
    ],
    pydantic.Field(discriminator="type"),
]



from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_content_source import ImageContentSource


class LettaMessageContentUnion_Text(UniversalBaseModel):
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


class LettaMessageContentUnion_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    source: ImageContentSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageContentUnion_ToolCall(UniversalBaseModel):
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


class LettaMessageContentUnion_ToolReturn(UniversalBaseModel):
    type: typing.Literal["tool_return"] = "tool_return"
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


class LettaMessageContentUnion_Reasoning(UniversalBaseModel):
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


class LettaMessageContentUnion_RedactedReasoning(UniversalBaseModel):
    type: typing.Literal["redacted_reasoning"] = "redacted_reasoning"
    data: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaMessageContentUnion_OmittedReasoning(UniversalBaseModel):
    type: typing.Literal["omitted_reasoning"] = "omitted_reasoning"
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LettaMessageContentUnion = typing_extensions.Annotated[
    typing.Union[
        LettaMessageContentUnion_Text,
        LettaMessageContentUnion_Image,
        LettaMessageContentUnion_ToolCall,
        LettaMessageContentUnion_ToolReturn,
        LettaMessageContentUnion_Reasoning,
        LettaMessageContentUnion_RedactedReasoning,
        LettaMessageContentUnion_OmittedReasoning,
    ],
    pydantic.Field(discriminator="type"),
]

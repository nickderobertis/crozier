

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .annotation import Annotation
from .input_image_content_detail import InputImageContentDetail
from .log_prob import LogProb


class ResponseContentPartAddedStreamingEventPart_InputText(UniversalBaseModel):
    """
    A content part that makes up an input or output item.
    """

    type: typing.Literal["input_text"] = "input_text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseContentPartAddedStreamingEventPart_OutputText(UniversalBaseModel):
    """
    A content part that makes up an input or output item.
    """

    type: typing.Literal["output_text"] = "output_text"
    text: str
    annotations: typing.List[Annotation]
    logprobs: typing.List[LogProb]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseContentPartAddedStreamingEventPart_Text(UniversalBaseModel):
    """
    A content part that makes up an input or output item.
    """

    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseContentPartAddedStreamingEventPart_SummaryText(UniversalBaseModel):
    """
    A content part that makes up an input or output item.
    """

    type: typing.Literal["summary_text"] = "summary_text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseContentPartAddedStreamingEventPart_ReasoningText(UniversalBaseModel):
    """
    A content part that makes up an input or output item.
    """

    type: typing.Literal["reasoning_text"] = "reasoning_text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseContentPartAddedStreamingEventPart_Refusal(UniversalBaseModel):
    """
    A content part that makes up an input or output item.
    """

    type: typing.Literal["refusal"] = "refusal"
    refusal: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseContentPartAddedStreamingEventPart_InputImage(UniversalBaseModel):
    """
    A content part that makes up an input or output item.
    """

    type: typing.Literal["input_image"] = "input_image"
    image_url: typing.Optional[str] = None
    detail: InputImageContentDetail

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResponseContentPartAddedStreamingEventPart_InputFile(UniversalBaseModel):
    """
    A content part that makes up an input or output item.
    """

    type: typing.Literal["input_file"] = "input_file"
    filename: typing.Optional[str] = None
    file_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ResponseContentPartAddedStreamingEventPart = typing_extensions.Annotated[
    typing.Union[
        ResponseContentPartAddedStreamingEventPart_InputText,
        ResponseContentPartAddedStreamingEventPart_OutputText,
        ResponseContentPartAddedStreamingEventPart_Text,
        ResponseContentPartAddedStreamingEventPart_SummaryText,
        ResponseContentPartAddedStreamingEventPart_ReasoningText,
        ResponseContentPartAddedStreamingEventPart_Refusal,
        ResponseContentPartAddedStreamingEventPart_InputImage,
        ResponseContentPartAddedStreamingEventPart_InputFile,
    ],
    pydantic.Field(discriminator="type"),
]

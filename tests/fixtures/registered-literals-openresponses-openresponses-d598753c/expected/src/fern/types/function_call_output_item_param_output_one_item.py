

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_image_content_param_auto_param_detail import InputImageContentParamAutoParamDetail


class FunctionCallOutputItemParamOutputOneItem_InputText(UniversalBaseModel):
    """
    A piece of message content, such as text, an image, or a file.
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


class FunctionCallOutputItemParamOutputOneItem_InputImage(UniversalBaseModel):
    """
    A piece of message content, such as text, an image, or a file.
    """

    type: typing.Literal["input_image"] = "input_image"
    image_url: typing.Optional[str] = None
    detail: typing.Optional[InputImageContentParamAutoParamDetail] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FunctionCallOutputItemParamOutputOneItem_InputFile(UniversalBaseModel):
    """
    A piece of message content, such as text, an image, or a file.
    """

    type: typing.Literal["input_file"] = "input_file"
    filename: typing.Optional[str] = None
    file_data: typing.Optional[str] = None
    file_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class FunctionCallOutputItemParamOutputOneItem_InputVideo(UniversalBaseModel):
    """
    A piece of message content, such as text, an image, or a file.
    """

    type: typing.Literal["input_video"] = "input_video"
    video_url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


FunctionCallOutputItemParamOutputOneItem = typing_extensions.Annotated[
    typing.Union[
        FunctionCallOutputItemParamOutputOneItem_InputText,
        FunctionCallOutputItemParamOutputOneItem_InputImage,
        FunctionCallOutputItemParamOutputOneItem_InputFile,
        FunctionCallOutputItemParamOutputOneItem_InputVideo,
    ],
    pydantic.Field(discriminator="type"),
]

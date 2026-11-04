

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_file import FileFile
from .image_url import ImageUrl
from .input_audio import InputAudio


class ChatCompletionUserMessageParamContentOneItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionUserMessageParamContentOneItem_ImageUrl(UniversalBaseModel):
    type: typing.Literal["image_url"] = "image_url"
    image_url: ImageUrl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionUserMessageParamContentOneItem_InputAudio(UniversalBaseModel):
    type: typing.Literal["input_audio"] = "input_audio"
    input_audio: InputAudio

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionUserMessageParamContentOneItem_File(UniversalBaseModel):
    type: typing.Literal["file"] = "file"
    file: FileFile

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChatCompletionUserMessageParamContentOneItem = typing_extensions.Annotated[
    typing.Union[
        ChatCompletionUserMessageParamContentOneItem_Text,
        ChatCompletionUserMessageParamContentOneItem_ImageUrl,
        ChatCompletionUserMessageParamContentOneItem_InputAudio,
        ChatCompletionUserMessageParamContentOneItem_File,
    ],
    pydantic.Field(discriminator="type"),
]

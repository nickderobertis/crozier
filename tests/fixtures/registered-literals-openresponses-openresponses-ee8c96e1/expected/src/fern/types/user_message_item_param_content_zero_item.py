

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_image_content_param_auto_param_detail import InputImageContentParamAutoParamDetail


class UserMessageItemParamContentZeroItem_InputText(UniversalBaseModel):
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


class UserMessageItemParamContentZeroItem_InputImage(UniversalBaseModel):
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


class UserMessageItemParamContentZeroItem_InputFile(UniversalBaseModel):
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


UserMessageItemParamContentZeroItem = typing_extensions.Annotated[
    typing.Union[
        UserMessageItemParamContentZeroItem_InputText,
        UserMessageItemParamContentZeroItem_InputImage,
        UserMessageItemParamContentZeroItem_InputFile,
    ],
    pydantic.Field(discriminator="type"),
]

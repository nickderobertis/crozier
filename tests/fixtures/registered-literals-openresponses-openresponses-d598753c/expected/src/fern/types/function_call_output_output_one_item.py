

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_image_content_detail import InputImageContentDetail


class FunctionCallOutputOutputOneItem_InputText(UniversalBaseModel):
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


class FunctionCallOutputOutputOneItem_InputImage(UniversalBaseModel):
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


class FunctionCallOutputOutputOneItem_InputFile(UniversalBaseModel):
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


FunctionCallOutputOutputOneItem = typing_extensions.Annotated[
    typing.Union[
        FunctionCallOutputOutputOneItem_InputText,
        FunctionCallOutputOutputOneItem_InputImage,
        FunctionCallOutputOutputOneItem_InputFile,
    ],
    pydantic.Field(discriminator="type"),
]

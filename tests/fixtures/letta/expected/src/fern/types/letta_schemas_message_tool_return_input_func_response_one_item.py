

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_content_source import ImageContentSource


class LettaSchemasMessageToolReturnInputFuncResponseOneItem_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    source: ImageContentSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LettaSchemasMessageToolReturnInputFuncResponseOneItem_Text(UniversalBaseModel):
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


LettaSchemasMessageToolReturnInputFuncResponseOneItem = typing_extensions.Annotated[
    typing.Union[
        LettaSchemasMessageToolReturnInputFuncResponseOneItem_Image,
        LettaSchemasMessageToolReturnInputFuncResponseOneItem_Text,
    ],
    pydantic.Field(discriminator="type"),
]

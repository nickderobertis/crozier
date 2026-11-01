

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ComplexTypesDiscriminatedUnionRequest_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    content: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ComplexTypesDiscriminatedUnionRequest_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    url: str
    width: float
    height: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ComplexTypesDiscriminatedUnionRequest_Video(UniversalBaseModel):
    type: typing.Literal["video"] = "video"
    url: str
    duration: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ComplexTypesDiscriminatedUnionRequest = typing_extensions.Annotated[
    typing.Union[
        ComplexTypesDiscriminatedUnionRequest_Text,
        ComplexTypesDiscriminatedUnionRequest_Image,
        ComplexTypesDiscriminatedUnionRequest_Video,
    ],
    pydantic.Field(discriminator="type"),
]



from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Shape_Circle(UniversalBaseModel):
    type: typing.Literal["circle"] = "circle"
    radius: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Shape_Square(UniversalBaseModel):
    type: typing.Literal["square"] = "square"
    side: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Shape = typing_extensions.Annotated[typing.Union[Shape_Circle, Shape_Square], pydantic.Field(discriminator="type")]

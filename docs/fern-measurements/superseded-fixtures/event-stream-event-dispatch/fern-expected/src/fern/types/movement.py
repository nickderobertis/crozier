

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .berth import Berth


class Movement_Departed(UniversalBaseModel):
    event: typing.Literal["departed"] = "departed"
    data: Berth

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Movement_Arrived(UniversalBaseModel):
    event: typing.Literal["arrived"] = "arrived"
    data: Berth

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Movement = typing_extensions.Annotated[
    typing.Union[Movement_Departed, Movement_Arrived], pydantic.Field(discriminator="event")
]



from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .berth import Berth


class GangwayChange_Lowered(UniversalBaseModel):
    event: typing.Literal["lowered"] = "lowered"
    data: Berth

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GangwayChange_Raised(UniversalBaseModel):
    event: typing.Literal["raised"] = "raised"
    data: Berth

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GangwayChange = typing_extensions.Annotated[
    typing.Union[GangwayChange_Lowered, GangwayChange_Raised], pydantic.Field(discriminator="event")
]

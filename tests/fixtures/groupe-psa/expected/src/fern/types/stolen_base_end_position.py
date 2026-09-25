

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .point import Point
from .stolen_base_end_position_properties import StolenBaseEndPositionProperties
from .stolen_base_end_position_type import StolenBaseEndPositionType


class StolenBaseEndPosition(UniversalBaseModel):
    type: StolenBaseEndPositionType
    geometry: Point
    properties: StolenBaseEndPositionProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

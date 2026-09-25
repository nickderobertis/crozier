

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .point import Point
from .stolen_base_start_position_properties import StolenBaseStartPositionProperties
from .stolen_base_start_position_type import StolenBaseStartPositionType


class StolenBaseStartPosition(UniversalBaseModel):
    type: StolenBaseStartPositionType
    geometry: Point
    properties: StolenBaseStartPositionProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

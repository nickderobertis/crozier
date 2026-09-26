

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .point import Point
from .position_base_properties import PositionBaseProperties
from .position_base_type import PositionBaseType


class PositionBase(UniversalBaseModel):
    type: PositionBaseType
    geometry: Point
    properties: PositionBaseProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

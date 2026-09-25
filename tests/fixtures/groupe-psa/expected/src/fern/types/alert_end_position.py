

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_end_position_properties import AlertEndPositionProperties
from .alert_end_position_type import AlertEndPositionType
from .point import Point


class AlertEndPosition(UniversalBaseModel):
    type: AlertEndPositionType
    geometry: Point
    properties: AlertEndPositionProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

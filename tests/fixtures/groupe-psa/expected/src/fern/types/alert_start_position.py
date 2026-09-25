

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_start_position_properties import AlertStartPositionProperties
from .alert_start_position_type import AlertStartPositionType
from .point import Point


class AlertStartPosition(UniversalBaseModel):
    type: AlertStartPositionType
    geometry: Point
    properties: AlertStartPositionProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

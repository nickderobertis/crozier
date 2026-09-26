

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base_alarm_trigger_position_properties import BaseAlarmTriggerPositionProperties
from .base_alarm_trigger_position_type import BaseAlarmTriggerPositionType
from .point import Point


class BaseAlarmTriggerPosition(UniversalBaseModel):
    type: BaseAlarmTriggerPositionType
    geometry: Point
    properties: BaseAlarmTriggerPositionProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

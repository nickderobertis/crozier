

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_alarm_trigger import BaseAlarmTrigger
from .created_at_field import CreatedAtField


class AlarmTrigger(CreatedAtField, BaseAlarmTrigger):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base_alarm_status import BaseAlarmStatus
from .base_alarm_trigger import BaseAlarmTrigger


class BaseAlarm(UniversalBaseModel):
    """
    Describe a vehicle alarm status and trigger.
    """

    status: typing.Optional[BaseAlarmStatus] = None
    trigger: typing.Optional[BaseAlarmTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alarm_status import AlarmStatus
from .alarm_trigger import AlarmTrigger


class VehicleStatusAlarm(UniversalBaseModel):
    """
    Describes the current vehicle alarm status and the latest (if available) trigger.
    """

    trigger: typing.Optional[AlarmTrigger] = None
    status: typing.Optional[AlarmStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

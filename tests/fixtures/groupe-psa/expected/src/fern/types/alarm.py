

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alarm_status import AlarmStatus
from .alarm_trigger import AlarmTrigger


class Alarm(UniversalBaseModel):
    """
    Describes the vehicle alarm status or trigger. Only one is present.
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

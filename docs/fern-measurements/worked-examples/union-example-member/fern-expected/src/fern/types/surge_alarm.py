

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .alarm_base import AlarmBase


class SurgeAlarm(AlarmBase):
    surge_m: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

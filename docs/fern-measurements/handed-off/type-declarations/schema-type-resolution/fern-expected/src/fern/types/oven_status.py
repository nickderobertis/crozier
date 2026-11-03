

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alarm import Alarm
from .alarm_history import AlarmHistory
from .oven_status_trays_item import OvenStatusTraysItem


class OvenStatus(UniversalBaseModel):
    alarms: typing.Optional[typing.List[Alarm]] = pydantic.Field(default=None)
    """
    Alarms raised by the oven controller.
    """

    trays: typing.Optional[typing.List[OvenStatusTraysItem]] = None
    history: typing.Optional[AlarmHistory] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

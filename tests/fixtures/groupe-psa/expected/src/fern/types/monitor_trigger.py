

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_trigger import DataTrigger
from .time_trigger import TimeTrigger
from .zone_trigger import ZoneTrigger


class MonitorTrigger(UniversalBaseModel):
    """
    Monitor trigger.```Only one```of *Zone, Time or Data* is supported at a time. Otherwise it would cause a bad request response.
    """

    name: str = pydantic.Field()
    """
    The trigger name must be uniq and respect the following pattern
    """

    zone: typing.Optional[ZoneTrigger] = None
    time: typing.Optional[TimeTrigger] = None
    data: typing.Optional[DataTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

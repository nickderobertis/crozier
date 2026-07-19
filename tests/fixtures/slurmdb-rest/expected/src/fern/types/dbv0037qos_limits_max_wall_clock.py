

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_max_wall_clock_per import Dbv0037QosLimitsMaxWallClockPer


class Dbv0037QosLimitsMaxWallClock(UniversalBaseModel):
    """
    Limit on wallclock settings
    """

    per: typing.Optional[Dbv0037QosLimitsMaxWallClockPer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

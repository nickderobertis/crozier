

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_max_accruing import Dbv0037QosLimitsMaxAccruing
from .dbv0037qos_limits_max_jobs import Dbv0037QosLimitsMaxJobs
from .dbv0037qos_limits_max_tres import Dbv0037QosLimitsMaxTres
from .dbv0037qos_limits_max_wall_clock import Dbv0037QosLimitsMaxWallClock


class Dbv0037QosLimitsMax(UniversalBaseModel):
    """
    Limits on max settings
    """

    wall_clock: typing.Optional[Dbv0037QosLimitsMaxWallClock] = None
    jobs: typing.Optional[Dbv0037QosLimitsMaxJobs] = None
    accruing: typing.Optional[Dbv0037QosLimitsMaxAccruing] = None
    tres: typing.Optional[Dbv0037QosLimitsMaxTres] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_max_accruing_per import Dbv0037QosLimitsMaxAccruingPer


class Dbv0037QosLimitsMaxAccruing(UniversalBaseModel):
    """
    Limits on accruing priority
    """

    per: typing.Optional[Dbv0037QosLimitsMaxAccruingPer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

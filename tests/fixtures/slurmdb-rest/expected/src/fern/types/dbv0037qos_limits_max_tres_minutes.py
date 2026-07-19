

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_max_tres_minutes_per import Dbv0037QosLimitsMaxTresMinutesPer


class Dbv0037QosLimitsMaxTresMinutes(UniversalBaseModel):
    """
    Max TRES minutes settings
    """

    per: typing.Optional[Dbv0037QosLimitsMaxTresMinutesPer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

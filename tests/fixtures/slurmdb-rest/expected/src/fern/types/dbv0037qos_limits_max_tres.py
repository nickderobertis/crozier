

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_max_tres_minutes import Dbv0037QosLimitsMaxTresMinutes
from .dbv0037qos_limits_max_tres_per import Dbv0037QosLimitsMaxTresPer


class Dbv0037QosLimitsMaxTres(UniversalBaseModel):
    """
    Limits on TRES
    """

    minutes: typing.Optional[Dbv0037QosLimitsMaxTresMinutes] = None
    per: typing.Optional[Dbv0037QosLimitsMaxTresPer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

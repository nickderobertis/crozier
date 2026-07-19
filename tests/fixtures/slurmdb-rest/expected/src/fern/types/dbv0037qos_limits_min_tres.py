

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_min_tres_per import Dbv0037QosLimitsMinTresPer


class Dbv0037QosLimitsMinTres(UniversalBaseModel):
    """
    Min tres settings
    """

    per: typing.Optional[Dbv0037QosLimitsMinTresPer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

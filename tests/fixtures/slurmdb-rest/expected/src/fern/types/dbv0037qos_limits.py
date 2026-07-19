

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_max import Dbv0037QosLimitsMax
from .dbv0037qos_limits_min import Dbv0037QosLimitsMin


class Dbv0037QosLimits(UniversalBaseModel):
    """
    Assigned limits
    """

    max: typing.Optional[Dbv0037QosLimitsMax] = None
    min: typing.Optional[Dbv0037QosLimitsMin] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

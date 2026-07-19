

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_min_tres import Dbv0037QosLimitsMinTres


class Dbv0037QosLimitsMin(UniversalBaseModel):
    """
    Min limit settings
    """

    priority_threshold: typing.Optional[int] = pydantic.Field(default=None)
    """
    Min priority threshold
    """

    tres: typing.Optional[Dbv0037QosLimitsMinTres] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

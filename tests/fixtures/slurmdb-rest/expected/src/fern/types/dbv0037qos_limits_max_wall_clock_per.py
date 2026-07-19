

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037QosLimitsMaxWallClockPer(UniversalBaseModel):
    """
    Limit on wallclock per settings
    """

    qos: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max wallclock per QOS
    """

    job: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max wallclock per job
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

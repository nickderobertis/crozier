

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_max_jobs_per import Dbv0037QosLimitsMaxJobsPer


class Dbv0037QosLimitsMaxJobs(UniversalBaseModel):
    """
    Limits on jobs settings
    """

    per: typing.Optional[Dbv0037QosLimitsMaxJobsPer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

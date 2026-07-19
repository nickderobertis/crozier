

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_min_tres_per_job_item import Dbv0037QosLimitsMinTresPerJobItem


class Dbv0037QosLimitsMinTresPer(UniversalBaseModel):
    """
    Min tres per settings
    """

    job: typing.Optional[typing.List[Dbv0037QosLimitsMinTresPerJobItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

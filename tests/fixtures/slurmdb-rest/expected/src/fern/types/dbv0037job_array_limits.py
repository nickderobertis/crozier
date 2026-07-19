

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_array_limits_max import Dbv0037JobArrayLimitsMax


class Dbv0037JobArrayLimits(UniversalBaseModel):
    """
    Limits on array settings
    """

    max: typing.Optional[Dbv0037JobArrayLimitsMax] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

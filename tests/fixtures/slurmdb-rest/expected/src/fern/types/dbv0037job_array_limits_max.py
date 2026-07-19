

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_array_limits_max_running import Dbv0037JobArrayLimitsMaxRunning


class Dbv0037JobArrayLimitsMax(UniversalBaseModel):
    """
    Limits on array settings
    """

    running: typing.Optional[Dbv0037JobArrayLimitsMaxRunning] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

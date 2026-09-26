

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .performance_counter import PerformanceCounter


class PerformanceCountersItemCountersItemThree(PerformanceCounter):
    """
    Simple latency performance counter information.
    """

    sum: typing.Optional[int] = None
    hits: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

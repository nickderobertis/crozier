

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .performance_counter import PerformanceCounter


class PerformanceCountersItemCountersItemTwo(PerformanceCounter):
    """
    Rate performance counter information.
    """

    delta_ns: typing.Optional[int] = None
    current: typing.Optional[int] = None
    previous: typing.Optional[int] = None
    rate: typing.Optional[int] = None
    vadd: typing.Optional[int] = None
    vsub: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

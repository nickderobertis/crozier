

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .performance_counter import PerformanceCounter
from .performance_counters_item_counters_item_four_histogram_item import (
    PerformanceCountersItemCountersItemFourHistogramItem,
)


class PerformanceCountersItemCountersItemFour(PerformanceCounter):
    """
    Latency performance counter information.
    """

    minimum: typing.Optional[int] = None
    maximum: typing.Optional[int] = None
    average: typing.Optional[int] = None
    sum: typing.Optional[int] = None
    hits: typing.Optional[int] = None
    percentage: typing.Optional[float] = None
    histogram: typing.Optional[typing.List[PerformanceCountersItemCountersItemFourHistogramItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

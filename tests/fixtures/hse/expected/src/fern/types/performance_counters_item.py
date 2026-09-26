

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .performance_counters_item_counters_item import PerformanceCountersItemCountersItem


class PerformanceCountersItem(UniversalBaseModel):
    path: typing.Optional[str] = None
    name: typing.Optional[str] = None
    enabled: typing.Optional[int] = None
    counters: typing.Optional[typing.List[PerformanceCountersItemCountersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

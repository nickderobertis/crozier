

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .performance_counter_type import PerformanceCounterType


class PerformanceCounter(UniversalBaseModel):
    """
    Common performance counter information.
    """

    name: typing.Optional[str] = None
    header: typing.Optional[str] = None
    description: typing.Optional[str] = None
    type: typing.Optional[PerformanceCounterType] = None
    level: typing.Optional[int] = None
    enabled: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

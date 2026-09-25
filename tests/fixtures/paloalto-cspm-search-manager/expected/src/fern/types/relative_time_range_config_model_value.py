

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .relative_time_range_config_model_value_unit import RelativeTimeRangeConfigModelValueUnit


class RelativeTimeRangeConfigModelValue(UniversalBaseModel):
    """
    Time range object
    """

    amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of time units
    """

    unit: typing.Optional[RelativeTimeRangeConfigModelValueUnit] = pydantic.Field(default=None)
    """
    Time unit
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

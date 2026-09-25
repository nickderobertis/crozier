

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_time_range_config_model_value import AbsoluteTimeRangeConfigModelValue


class AbsoluteTimeRangeConfigModel(UniversalBaseModel):
    value: AbsoluteTimeRangeConfigModelValue = pydantic.Field()
    """
    Time range object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

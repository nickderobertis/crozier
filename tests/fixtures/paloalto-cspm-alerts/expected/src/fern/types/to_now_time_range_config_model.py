

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .to_now_time_range_config_model_value import ToNowTimeRangeConfigModelValue


class ToNowTimeRangeConfigModel(UniversalBaseModel):
    value: typing.Optional[ToNowTimeRangeConfigModelValue] = pydantic.Field(default=None)
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

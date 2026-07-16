

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .power_feed_status_label import PowerFeedStatusLabel
from .power_feed_status_value import PowerFeedStatusValue


class PowerFeedStatus(UniversalBaseModel):
    label: PowerFeedStatusLabel
    value: PowerFeedStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

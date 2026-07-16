

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .power_feed_supply_label import PowerFeedSupplyLabel
from .power_feed_supply_value import PowerFeedSupplyValue


class PowerFeedSupply(UniversalBaseModel):
    label: PowerFeedSupplyLabel
    value: PowerFeedSupplyValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .power_outlet_feed_leg_label import PowerOutletFeedLegLabel
from .power_outlet_feed_leg_value import PowerOutletFeedLegValue


class PowerOutletFeedLeg(UniversalBaseModel):
    label: PowerOutletFeedLegLabel
    value: PowerOutletFeedLegValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

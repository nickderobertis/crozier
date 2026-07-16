

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .power_outlet_template_feed_leg_label import PowerOutletTemplateFeedLegLabel
from .power_outlet_template_feed_leg_value import PowerOutletTemplateFeedLegValue


class PowerOutletTemplateFeedLeg(UniversalBaseModel):
    label: PowerOutletTemplateFeedLegLabel
    value: PowerOutletTemplateFeedLegValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

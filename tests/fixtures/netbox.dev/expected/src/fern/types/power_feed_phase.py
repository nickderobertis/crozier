

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .power_feed_phase_label import PowerFeedPhaseLabel
from .power_feed_phase_value import PowerFeedPhaseValue


class PowerFeedPhase(UniversalBaseModel):
    label: PowerFeedPhaseLabel
    value: PowerFeedPhaseValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

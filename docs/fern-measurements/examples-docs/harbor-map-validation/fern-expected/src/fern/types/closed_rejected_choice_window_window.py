

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .closed_rejected_choice_window_window_lookback import ClosedRejectedChoiceWindowWindowLookback


class ClosedRejectedChoiceWindowWindow(UniversalBaseModel):
    lookback: ClosedRejectedChoiceWindowWindowLookback

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .streak_response_dto_output_current import StreakResponseDtoOutputCurrent
from .streak_response_dto_output_longest import StreakResponseDtoOutputLongest


class StreakResponseDtoOutput(UniversalBaseModel):
    current: StreakResponseDtoOutputCurrent
    longest: StreakResponseDtoOutputLongest

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

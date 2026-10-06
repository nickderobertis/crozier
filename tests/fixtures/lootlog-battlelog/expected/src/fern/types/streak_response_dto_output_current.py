

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .streak_response_dto_output_current_type import StreakResponseDtoOutputCurrentType


class StreakResponseDtoOutputCurrent(UniversalBaseModel):
    type: StreakResponseDtoOutputCurrentType
    count: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

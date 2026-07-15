

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schedule_work_pattern_even_weeks import ScheduleWorkPatternEvenWeeks
from .schedule_work_pattern_odd_weeks import ScheduleWorkPatternOddWeeks


class ScheduleWorkPattern(UniversalBaseModel):
    even_weeks: typing.Optional[ScheduleWorkPatternEvenWeeks] = None
    odd_weeks: typing.Optional[ScheduleWorkPatternOddWeeks] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

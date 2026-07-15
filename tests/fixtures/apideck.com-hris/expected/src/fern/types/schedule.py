

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .id import Id
from .schedule_work_pattern import ScheduleWorkPattern


class Schedule(UniversalBaseModel):
    end_date: str = pydantic.Field()
    """
    The end date, inclusive, of the schedule period.
    """

    id: typing.Optional[Id] = None
    start_date: str = pydantic.Field()
    """
    The start date, inclusive, of the schedule period.
    """

    work_pattern: ScheduleWorkPattern

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

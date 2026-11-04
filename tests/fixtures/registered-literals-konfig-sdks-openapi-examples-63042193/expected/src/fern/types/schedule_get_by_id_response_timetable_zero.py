

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schedule_get_by_id_response_timetable_zero_days_of_week_item import (
    ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem,
)
from .schedule_get_by_id_response_timetable_zero_months_item import ScheduleGetByIdResponseTimetableZeroMonthsItem


class ScheduleGetByIdResponseTimetableZero(UniversalBaseModel):
    per_hour: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="per-hour"),
        pydantic.Field(
            alias="per-hour", description="Number of times a schedule triggers per hour, value must be between 1 and 60"
        ),
    ]
    """
    Number of times a schedule triggers per hour, value must be between 1 and 60
    """

    hours_of_day: typing_extensions.Annotated[
        typing.List[int],
        FieldMetadata(alias="hours-of-day"),
        pydantic.Field(alias="hours-of-day", description="Hours in a day in which the schedule triggers."),
    ]
    """
    Hours in a day in which the schedule triggers.
    """

    days_of_week: typing_extensions.Annotated[
        typing.List[ScheduleGetByIdResponseTimetableZeroDaysOfWeekItem],
        FieldMetadata(alias="days-of-week"),
        pydantic.Field(alias="days-of-week", description="Days in a week in which the schedule triggers."),
    ]
    """
    Days in a week in which the schedule triggers.
    """

    days_of_month: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="days-of-month"),
        pydantic.Field(
            alias="days-of-month",
            description="Days in a month in which the schedule triggers. This is mutually exclusive with days in a week.",
        ),
    ] = None
    """
    Days in a month in which the schedule triggers. This is mutually exclusive with days in a week.
    """

    months: typing.Optional[typing.List[ScheduleGetByIdResponseTimetableZeroMonthsItem]] = pydantic.Field(default=None)
    """
    Months in which the schedule triggers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

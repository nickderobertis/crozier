

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .schedule_update_schedule_request_timetable_days_of_week_item import (
    ScheduleUpdateScheduleRequestTimetableDaysOfWeekItem,
)
from .schedule_update_schedule_request_timetable_months_item import ScheduleUpdateScheduleRequestTimetableMonthsItem


class ScheduleUpdateScheduleRequestTimetable(UniversalBaseModel):
    """
    Timetable that specifies when a schedule triggers.
    """

    per_hour: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="per-hour"),
        pydantic.Field(
            alias="per-hour", description="Number of times a schedule triggers per hour, value must be between 1 and 60"
        ),
    ] = None
    """
    Number of times a schedule triggers per hour, value must be between 1 and 60
    """

    hours_of_day: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="hours-of-day"),
        pydantic.Field(alias="hours-of-day", description="Hours in a day in which the schedule triggers."),
    ] = None
    """
    Hours in a day in which the schedule triggers.
    """

    days_of_week: typing_extensions.Annotated[
        typing.Optional[typing.List[ScheduleUpdateScheduleRequestTimetableDaysOfWeekItem]],
        FieldMetadata(alias="days-of-week"),
        pydantic.Field(alias="days-of-week", description="Days in a week in which the schedule triggers."),
    ] = None
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

    months: typing.Optional[typing.List[ScheduleUpdateScheduleRequestTimetableMonthsItem]] = pydantic.Field(
        default=None
    )
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

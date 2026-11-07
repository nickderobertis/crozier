

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schedule_get_all_schedules_response_items_item_timetable_one_days_of_week_item import (
    ScheduleGetAllSchedulesResponseItemsItemTimetableOneDaysOfWeekItem,
)
from .schedule_get_all_schedules_response_items_item_timetable_one_months_item import (
    ScheduleGetAllSchedulesResponseItemsItemTimetableOneMonthsItem,
)


class ScheduleGetAllSchedulesResponseItemsItemTimetableOne(UniversalBaseModel):
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

    days_of_month: typing_extensions.Annotated[
        typing.List[int],
        FieldMetadata(alias="days-of-month"),
        pydantic.Field(
            alias="days-of-month",
            description="Days in a month in which the schedule triggers. This is mutually exclusive with days in a week.",
        ),
    ]
    """
    Days in a month in which the schedule triggers. This is mutually exclusive with days in a week.
    """

    days_of_week: typing_extensions.Annotated[
        typing.Optional[typing.List[ScheduleGetAllSchedulesResponseItemsItemTimetableOneDaysOfWeekItem]],
        FieldMetadata(alias="days-of-week"),
        pydantic.Field(alias="days-of-week", description="Days in a week in which the schedule triggers."),
    ] = None
    """
    Days in a week in which the schedule triggers.
    """

    months: typing.Optional[typing.List[ScheduleGetAllSchedulesResponseItemsItemTimetableOneMonthsItem]] = (
        pydantic.Field(default=None)
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

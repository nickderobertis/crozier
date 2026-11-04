

import typing

from .schedule_get_all_schedules_response_items_item_timetable_one import (
    ScheduleGetAllSchedulesResponseItemsItemTimetableOne,
)
from .schedule_get_all_schedules_response_items_item_timetable_zero import (
    ScheduleGetAllSchedulesResponseItemsItemTimetableZero,
)

ScheduleGetAllSchedulesResponseItemsItemTimetable = typing.Union[
    ScheduleGetAllSchedulesResponseItemsItemTimetableZero, ScheduleGetAllSchedulesResponseItemsItemTimetableOne
]

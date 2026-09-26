

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAttendancesV3RequestMetricsItem(enum.StrEnum):
    ATTENDANCE_DAYS = "attendance_days"
    TOTAL_RECORDS = "total_records"
    SUM_HOURS = "sum_hours"
    AVG_HOURS = "avg_hours"
    DISTINCT_STUDENTS = "distinct_students"

    def visit(
        self,
        attendance_days: typing.Callable[[], T_Result],
        total_records: typing.Callable[[], T_Result],
        sum_hours: typing.Callable[[], T_Result],
        avg_hours: typing.Callable[[], T_Result],
        distinct_students: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAttendancesV3RequestMetricsItem.ATTENDANCE_DAYS:
            return attendance_days()
        if self is GetAttendancesV3RequestMetricsItem.TOTAL_RECORDS:
            return total_records()
        if self is GetAttendancesV3RequestMetricsItem.SUM_HOURS:
            return sum_hours()
        if self is GetAttendancesV3RequestMetricsItem.AVG_HOURS:
            return avg_hours()
        if self is GetAttendancesV3RequestMetricsItem.DISTINCT_STUDENTS:
            return distinct_students()



import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAttendancesV3RequestSortBy(enum.StrEnum):
    GROUP_ASC = "group_asc"
    GROUP_DESC = "group_desc"
    ATTENDANCE_DAYS_ASC = "attendance_days_asc"
    ATTENDANCE_DAYS_DESC = "attendance_days_desc"
    TOTAL_RECORDS_ASC = "total_records_asc"
    TOTAL_RECORDS_DESC = "total_records_desc"
    SUM_HOURS_ASC = "sum_hours_asc"
    SUM_HOURS_DESC = "sum_hours_desc"
    AVG_HOURS_ASC = "avg_hours_asc"
    AVG_HOURS_DESC = "avg_hours_desc"
    DISTINCT_STUDENTS_ASC = "distinct_students_asc"
    DISTINCT_STUDENTS_DESC = "distinct_students_desc"

    def visit(
        self,
        group_asc: typing.Callable[[], T_Result],
        group_desc: typing.Callable[[], T_Result],
        attendance_days_asc: typing.Callable[[], T_Result],
        attendance_days_desc: typing.Callable[[], T_Result],
        total_records_asc: typing.Callable[[], T_Result],
        total_records_desc: typing.Callable[[], T_Result],
        sum_hours_asc: typing.Callable[[], T_Result],
        sum_hours_desc: typing.Callable[[], T_Result],
        avg_hours_asc: typing.Callable[[], T_Result],
        avg_hours_desc: typing.Callable[[], T_Result],
        distinct_students_asc: typing.Callable[[], T_Result],
        distinct_students_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAttendancesV3RequestSortBy.GROUP_ASC:
            return group_asc()
        if self is GetAttendancesV3RequestSortBy.GROUP_DESC:
            return group_desc()
        if self is GetAttendancesV3RequestSortBy.ATTENDANCE_DAYS_ASC:
            return attendance_days_asc()
        if self is GetAttendancesV3RequestSortBy.ATTENDANCE_DAYS_DESC:
            return attendance_days_desc()
        if self is GetAttendancesV3RequestSortBy.TOTAL_RECORDS_ASC:
            return total_records_asc()
        if self is GetAttendancesV3RequestSortBy.TOTAL_RECORDS_DESC:
            return total_records_desc()
        if self is GetAttendancesV3RequestSortBy.SUM_HOURS_ASC:
            return sum_hours_asc()
        if self is GetAttendancesV3RequestSortBy.SUM_HOURS_DESC:
            return sum_hours_desc()
        if self is GetAttendancesV3RequestSortBy.AVG_HOURS_ASC:
            return avg_hours_asc()
        if self is GetAttendancesV3RequestSortBy.AVG_HOURS_DESC:
            return avg_hours_desc()
        if self is GetAttendancesV3RequestSortBy.DISTINCT_STUDENTS_ASC:
            return distinct_students_asc()
        if self is GetAttendancesV3RequestSortBy.DISTINCT_STUDENTS_DESC:
            return distinct_students_desc()

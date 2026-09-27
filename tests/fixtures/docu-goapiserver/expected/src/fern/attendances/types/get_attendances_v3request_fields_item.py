

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAttendancesV3RequestFieldsItem(enum.StrEnum):
    ATTENDANCE_ID = "attendance_id"
    STUDENT_ID = "student_id"
    DATE = "date"
    ROOM_ID = "room_id"
    ROOM_NAME = "room_name"
    HOURS_ATTENDED = "hours_attended"
    SIGN_IN_TIME = "sign_in_time"
    SIGN_OUT_TIME = "sign_out_time"

    def visit(
        self,
        attendance_id: typing.Callable[[], T_Result],
        student_id: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        room_id: typing.Callable[[], T_Result],
        room_name: typing.Callable[[], T_Result],
        hours_attended: typing.Callable[[], T_Result],
        sign_in_time: typing.Callable[[], T_Result],
        sign_out_time: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAttendancesV3RequestFieldsItem.ATTENDANCE_ID:
            return attendance_id()
        if self is GetAttendancesV3RequestFieldsItem.STUDENT_ID:
            return student_id()
        if self is GetAttendancesV3RequestFieldsItem.DATE:
            return date()
        if self is GetAttendancesV3RequestFieldsItem.ROOM_ID:
            return room_id()
        if self is GetAttendancesV3RequestFieldsItem.ROOM_NAME:
            return room_name()
        if self is GetAttendancesV3RequestFieldsItem.HOURS_ATTENDED:
            return hours_attended()
        if self is GetAttendancesV3RequestFieldsItem.SIGN_IN_TIME:
            return sign_in_time()
        if self is GetAttendancesV3RequestFieldsItem.SIGN_OUT_TIME:
            return sign_out_time()

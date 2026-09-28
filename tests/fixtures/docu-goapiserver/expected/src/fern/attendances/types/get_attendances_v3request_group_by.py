

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAttendancesV3RequestGroupBy(enum.StrEnum):
    STUDENT_ID = "student_id"
    ROOM_ID = "room_id"
    ROOM_NAME = "room_name"
    DATE = "date"
    MONTH = "month"

    def visit(
        self,
        student_id: typing.Callable[[], T_Result],
        room_id: typing.Callable[[], T_Result],
        room_name: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAttendancesV3RequestGroupBy.STUDENT_ID:
            return student_id()
        if self is GetAttendancesV3RequestGroupBy.ROOM_ID:
            return room_id()
        if self is GetAttendancesV3RequestGroupBy.ROOM_NAME:
            return room_name()
        if self is GetAttendancesV3RequestGroupBy.DATE:
            return date()
        if self is GetAttendancesV3RequestGroupBy.MONTH:
            return month()

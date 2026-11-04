

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserStatusClearAtTimeType(enum.StrEnum):
    DAY = "day"
    WEEK = "week"

    def visit(self, day: typing.Callable[[], T_Result], week: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserStatusClearAtTimeType.DAY:
            return day()
        if self is UserStatusClearAtTimeType.WEEK:
            return week()

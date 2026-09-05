

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserNotificationResourceIdZero(enum.StrEnum):
    EMPTY = ""

    def visit(self, empty: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserNotificationResourceIdZero.EMPTY:
            return empty()

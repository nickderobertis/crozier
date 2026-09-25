

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReminderType(enum.StrEnum):
    """
    The type of the reminder. Always set to `"private"`.
    """

    PRIVATE = "private"

    def visit(self, private: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReminderType.PRIVATE:
            return private()

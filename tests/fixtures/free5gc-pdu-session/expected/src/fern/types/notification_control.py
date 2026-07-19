

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationControl(enum.StrEnum):
    REQUESTED = "REQUESTED"
    NOT_REQUESTED = "NOT_REQUESTED"

    def visit(self, requested: typing.Callable[[], T_Result], not_requested: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotificationControl.REQUESTED:
            return requested()
        if self is NotificationControl.NOT_REQUESTED:
            return not_requested()

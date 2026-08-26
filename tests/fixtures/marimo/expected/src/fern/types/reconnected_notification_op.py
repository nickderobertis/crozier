

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReconnectedNotificationOp(enum.StrEnum):
    RECONNECTED = "reconnected"

    def visit(self, reconnected: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReconnectedNotificationOp.RECONNECTED:
            return reconnected()

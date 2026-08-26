

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertNotificationOp(enum.StrEnum):
    ALERT = "alert"

    def visit(self, alert: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertNotificationOp.ALERT:
            return alert()

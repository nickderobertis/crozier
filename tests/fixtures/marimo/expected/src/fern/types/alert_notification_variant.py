

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertNotificationVariant(enum.StrEnum):
    DANGER = "danger"

    def visit(self, danger: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertNotificationVariant.DANGER:
            return danger()

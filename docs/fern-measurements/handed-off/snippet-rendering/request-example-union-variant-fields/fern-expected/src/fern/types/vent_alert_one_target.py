

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VentAlertOneTarget(enum.StrEnum):
    VENT = "vent"

    def visit(self, vent: typing.Callable[[], T_Result]) -> T_Result:
        if self is VentAlertOneTarget.VENT:
            return vent()

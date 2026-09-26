

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WipingBladesStateBaseSpeed(enum.StrEnum):
    """
    Wiping speed. This field is present only if active field is set to true.
    """

    HIGH = "High"
    LOW = "Low"

    def visit(self, high: typing.Callable[[], T_Result], low: typing.Callable[[], T_Result]) -> T_Result:
        if self is WipingBladesStateBaseSpeed.HIGH:
            return high()
        if self is WipingBladesStateBaseSpeed.LOW:
            return low()



import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListWidgetsRequestLevel(enum.StrEnum):
    LOW = "low"
    HIGH = "high"

    def visit(self, low: typing.Callable[[], T_Result], high: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListWidgetsRequestLevel.LOW:
            return low()
        if self is ListWidgetsRequestLevel.HIGH:
            return high()

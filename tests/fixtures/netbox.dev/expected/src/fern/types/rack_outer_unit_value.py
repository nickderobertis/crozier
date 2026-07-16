

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RackOuterUnitValue(enum.StrEnum):
    MM = "mm"
    IN = "in"

    def visit(self, mm: typing.Callable[[], T_Result], in_: typing.Callable[[], T_Result]) -> T_Result:
        if self is RackOuterUnitValue.MM:
            return mm()
        if self is RackOuterUnitValue.IN:
            return in_()

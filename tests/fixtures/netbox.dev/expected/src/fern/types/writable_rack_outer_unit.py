

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableRackOuterUnit(str, enum.Enum):
    MM = "mm"
    IN = "in"

    def visit(self, mm: typing.Callable[[], T_Result], in_: typing.Callable[[], T_Result]) -> T_Result:
        if self is WritableRackOuterUnit.MM:
            return mm()
        if self is WritableRackOuterUnit.IN:
            return in_()

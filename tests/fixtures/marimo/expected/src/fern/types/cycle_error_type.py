

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CycleErrorType(enum.StrEnum):
    CYCLE = "cycle"

    def visit(self, cycle: typing.Callable[[], T_Result]) -> T_Result:
        if self is CycleErrorType.CYCLE:
            return cycle()

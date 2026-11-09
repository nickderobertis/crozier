

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RangeNotSatisfiableErrorBodyErrorCode(enum.StrEnum):
    RANGE_NOT_SATISFIABLE = "RANGE_NOT_SATISFIABLE"

    def visit(self, range_not_satisfiable: typing.Callable[[], T_Result]) -> T_Result:
        if self is RangeNotSatisfiableErrorBodyErrorCode.RANGE_NOT_SATISFIABLE:
            return range_not_satisfiable()

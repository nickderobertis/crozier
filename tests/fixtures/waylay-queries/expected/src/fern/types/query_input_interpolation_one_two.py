

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryInputInterpolationOneTwo(enum.StrEnum):
    """
    Same as pad, but using the last observed value. This method also extrapolates
    """

    BACKFILL = "backfill"

    def visit(self, backfill: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryInputInterpolationOneTwo.BACKFILL:
            return backfill()

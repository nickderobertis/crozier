

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableRunDispatchLimitType(enum.StrEnum):
    """
    Unit the cap counts.
    """

    ROWS = "rows"

    def visit(self, rows: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2TableRunDispatchLimitType.ROWS:
            return rows()

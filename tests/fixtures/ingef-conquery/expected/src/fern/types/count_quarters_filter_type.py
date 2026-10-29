

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CountQuartersFilterType(enum.StrEnum):
    COUNT_QUARTERS = "COUNT_QUARTERS"

    def visit(self, count_quarters: typing.Callable[[], T_Result]) -> T_Result:
        if self is CountQuartersFilterType.COUNT_QUARTERS:
            return count_quarters()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PriceUnit(enum.StrEnum):
    COUNT = "count"
    USD = "$"
    MS = "ms"

    def visit(
        self,
        count: typing.Callable[[], T_Result],
        usd: typing.Callable[[], T_Result],
        ms: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PriceUnit.COUNT:
            return count()
        if self is PriceUnit.USD:
            return usd()
        if self is PriceUnit.MS:
            return ms()

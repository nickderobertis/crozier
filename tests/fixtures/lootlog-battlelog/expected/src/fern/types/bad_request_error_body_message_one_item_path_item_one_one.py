

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorBodyMessageOneItemPathItemOneOne(enum.StrEnum):
    INFINITY = "Infinity"
    NA_N = "NaN"

    def visit(self, infinity: typing.Callable[[], T_Result], na_n: typing.Callable[[], T_Result]) -> T_Result:
        if self is BadRequestErrorBodyMessageOneItemPathItemOneOne.INFINITY:
            return infinity()
        if self is BadRequestErrorBodyMessageOneItemPathItemOneOne.NA_N:
            return na_n()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FilterBandOne(enum.StrEnum):
    GREEN = "green"

    def visit(self, green: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilterBandOne.GREEN:
            return green()

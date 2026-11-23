

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FilterBandZero(enum.StrEnum):
    RED = "red"

    def visit(self, red: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilterBandZero.RED:
            return red()

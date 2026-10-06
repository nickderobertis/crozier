

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListWeighedHarvestsRequestUnitZero(enum.StrEnum):
    KILOGRAMS = "kilograms"

    def visit(self, kilograms: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListWeighedHarvestsRequestUnitZero.KILOGRAMS:
            return kilograms()

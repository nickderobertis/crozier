

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListWeighedHarvestsRequestUnitOne(enum.StrEnum):
    POUNDS = "pounds"

    def visit(self, pounds: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListWeighedHarvestsRequestUnitOne.POUNDS:
            return pounds()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoVegaDataChartSelectionOne(enum.StrEnum):
    POINT = "point"

    def visit(self, point: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoVegaDataChartSelectionOne.POINT:
            return point()

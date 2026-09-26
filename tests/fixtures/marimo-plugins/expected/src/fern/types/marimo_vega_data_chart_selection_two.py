

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoVegaDataChartSelectionTwo(enum.StrEnum):
    INTERVAL = "interval"

    def visit(self, interval: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoVegaDataChartSelectionTwo.INTERVAL:
            return interval()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PredictionPreprocessConfigImageQuality(enum.StrEnum):
    LOW = "LOW"
    HIGH = "HIGH"

    def visit(self, low: typing.Callable[[], T_Result], high: typing.Callable[[], T_Result]) -> T_Result:
        if self is PredictionPreprocessConfigImageQuality.LOW:
            return low()
        if self is PredictionPreprocessConfigImageQuality.HIGH:
            return high()

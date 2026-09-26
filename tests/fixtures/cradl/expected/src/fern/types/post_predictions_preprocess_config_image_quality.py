

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostPredictionsPreprocessConfigImageQuality(enum.StrEnum):
    LOW = "LOW"
    HIGH = "HIGH"

    def visit(self, low: typing.Callable[[], T_Result], high: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostPredictionsPreprocessConfigImageQuality.LOW:
            return low()
        if self is PostPredictionsPreprocessConfigImageQuality.HIGH:
            return high()

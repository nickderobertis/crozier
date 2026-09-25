

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelPreprocessConfigImageQuality(enum.StrEnum):
    LOW = "LOW"
    HIGH = "HIGH"

    def visit(self, low: typing.Callable[[], T_Result], high: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelPreprocessConfigImageQuality.LOW:
            return low()
        if self is ModelPreprocessConfigImageQuality.HIGH:
            return high()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetectedDataSourceConfidence(enum.StrEnum):
    HIGH = "high"
    MEDIUM = "medium"

    def visit(self, high: typing.Callable[[], T_Result], medium: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetectedDataSourceConfidence.HIGH:
            return high()
        if self is DetectedDataSourceConfidence.MEDIUM:
            return medium()

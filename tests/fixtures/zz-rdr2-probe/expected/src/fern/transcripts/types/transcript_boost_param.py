

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TranscriptBoostParam(enum.StrEnum):
    """
    How much to boost specified words
    """

    LOW = "low"
    DEFAULT = "default"
    HIGH = "high"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        default: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TranscriptBoostParam.LOW:
            return low()
        if self is TranscriptBoostParam.DEFAULT:
            return default()
        if self is TranscriptBoostParam.HIGH:
            return high()

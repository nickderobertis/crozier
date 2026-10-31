

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfidenceSourceScale(enum.StrEnum):
    ZERO_TO_ONE = "zero_to_one"
    ZERO_TO_HUNDRED = "zero_to_hundred"
    LOG_PROBABILITY = "log_probability"
    UNKNOWN = "unknown"

    def visit(
        self,
        zero_to_one: typing.Callable[[], T_Result],
        zero_to_hundred: typing.Callable[[], T_Result],
        log_probability: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConfidenceSourceScale.ZERO_TO_ONE:
            return zero_to_one()
        if self is ConfidenceSourceScale.ZERO_TO_HUNDRED:
            return zero_to_hundred()
        if self is ConfidenceSourceScale.LOG_PROBABILITY:
            return log_probability()
        if self is ConfidenceSourceScale.UNKNOWN:
            return unknown()

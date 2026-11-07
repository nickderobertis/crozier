

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConditionStatus(enum.StrEnum):
    """
    Status is the status of the condition. Can be True, False, Unknown.
    """

    TRUE = "TRUE"
    FALSE = "FALSE"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        true: typing.Callable[[], T_Result],
        false: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConditionStatus.TRUE:
            return true()
        if self is ConditionStatus.FALSE:
            return false()
        if self is ConditionStatus.UNKNOWN:
            return unknown()

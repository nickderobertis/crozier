

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReasonCondition(enum.StrEnum):
    """
    The reason condition
    """

    EQUALS = "equals"
    GREATER_THAN_OR_EQUALS = "greater_than_or_equals"
    UNKNOWN = "unknown"

    def visit(
        self,
        equals: typing.Callable[[], T_Result],
        greater_than_or_equals: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReasonCondition.EQUALS:
            return equals()
        if self is ReasonCondition.GREATER_THAN_OR_EQUALS:
            return greater_than_or_equals()
        if self is ReasonCondition.UNKNOWN:
            return unknown()
